import math
import numpy as np
import cntk as C
import cntkx as Cx
from cntk.default_options import default_override_or
from cntk.layers.blocks import identity
from cntk.layers import SequentialConvolution, Recurrence
from cntk.layers import MaxPooling, Convolution2D


def QRNN(window: int = 1, hidden_dim=None, activation=C.tanh, return_full_state=False):
    """
    Quasi-Recurrent Neural Networks layer

    This is the CNTK implementation of [Salesforce Research](https://einstein.ai/)'s
    [Quasi-Recurrent Neural Networks](https://arxiv.org/abs/1611.01576) paper.

    More details on tuning and application can be found in this paper:
    [An Analysis of Neural Language Modeling at Multiple Scales](https://arxiv.org/abs/1803.08240)

    From the authors:
        The QRNN provides similar accuracy to the LSTM but can be between
        2 and 17 times faster than the highly optimized NVIDIA cuDNN LSTM
        implementation depending on the use case.
        If you use this code or our results in your research, please cite:
        @article{bradbury2016quasi,
          title={{Quasi-Recurrent Neural Networks}},
          author={Bradbury, James and Merity, Stephen and Xiong, Caiming and Socher, Richard},
          journal={International Conference on Learning Representations (ICLR 2017)},
          year={2017}
        }

    Arguments:
        window (`int`):  Defines the size of the convolutional window (how many previous
          tokens to look when computing the QRNN values). Defaults 1.
        hidden_dim (int): size of hidden dim of h, c and o
        activation: cell activation function
        return_full_state: if to return cell and hidden states. Default false.

    Returns:
        :class:`~cntk.ops.functions.Function`: OR
        tuple of :class:`~cntk.ops.functions.Function`:

    """

    def FoPool(c, fz):
        f = C.slice(fz, 0, 0, hidden_dim)
        z = C.slice(fz, 0, hidden_dim, 2 * hidden_dim)
        return f * c + (1 - f) * z

    def model(input_tensor):
        filter_shape = (window, ) + input_tensor.shape

        input_sequence = input_tensor
        if window > 1:
            # to ensure causal relation is still preserved
            input_sequence = Cx.sequence.pad(input_sequence, (window - 1, 0), constant_value=0)

        gate_values = SequentialConvolution(filter_shape=filter_shape, num_filters=3 * hidden_dim, pad=False,
                                            reduction_rank=0)(input_sequence) >> C.squeeze

        x = C.slice(gate_values, -1, 0, hidden_dim)
        forget = C.slice(gate_values, -1, hidden_dim, 2 * hidden_dim)
        output = C.slice(gate_values, -1, 2 * hidden_dim, 3 * hidden_dim)

        z = activation(x)
        f = C.sigmoid(forget)
        o = C.sigmoid(output)

        # FoPooling
        c = Recurrence(FoPool)(C.splice(f, z))
        h = o * c

        if return_full_state:
            return h, c
        else:
            return h

    return model


def SinusoidalPositionalEmbedding(min_timescale=1.0, max_timescale=1.0e4, name: str = ''):
    """ Gets a bunch of sinusoids of different frequencies and add it to the input sequence

    Each channel of the input Tensor is incremented by a sinusoid of a different
    frequency and phase. This allows attention to learn to use absolute and relative positions.

    Timing signals should be added to some precursors of both the query and the
    memory inputs to attention. The use of relative position is possible because
    sin(x+y) and cos(x+y) can be expressed in terms of y, sin(x) and cos(x).

    In particular, we use a geometric sequence of timescales starting with
    min_timescale and ending with max_timescale. The number of different
    timescales is equal to channels / 2. For each timescale, we
    generate the two sinusoidal signals sin(timestep/timescale) and
    cos(timestep/timescale).  All of these sinusoids are concatenated in
    the channels dimension.

    This matches the implementation in tensor2tensor, but differs slightly
    from the description in Section 3.5 of "Attention Is All You Need" in
    that if input_dim is odd, the last dim will be a zero value.

    This implementation is equivalent to get_timing_signal_1d() in tensorflow's tensor2tensor:
        https://github.com/tensorflow/tensor2tensor/blob/23bd23b9830059fbc349381b70d9429b5c40a139/
          tensor2tensor/layers/common_attention.py

    Arguments:
        min_timescale (float): geometric sequence of timescales starting with min_timescale
        max_timescale (float): geometric sequence of timescales ending with max_timescale
        name (str): a name for this layer.

    Returns:
        :class:`~cntk.ops.functions.Function`: same shape as input sequence tensor

    """

    @C.Function
    def position(p, x):
        return p + x * 0 + 1

    def embedding(x):
        dim = x.shape[0]
        num_timescales = dim // 2
        log_timescale_increment = (math.log(float(max_timescale) / float(min_timescale)) / (num_timescales - 1))
        inv_timescales = C.constant(min_timescale * np.exp(np.arange(num_timescales) * -log_timescale_increment),
                                    dtype=np.float32)

        pos = Recurrence(position)(C.slice(x, 0, 0, num_timescales))
        scaled_time = pos * inv_timescales
        s = C.sin(scaled_time)
        c = C.cos(scaled_time)
        signal = C.splice(s, c)

        # last dim gets a 0 value is input_dim is odd
        if dim % 2 != 0:
            signal = C.pad(signal, [[0, 1]])

        return C.plus(signal, x, name=name)

    return embedding


def Conv2DMaxPool(n, conv_filter_shape,  # shape of receptive field, e.g. (3,3). Must be a 2-element tuple.
                  pool_filter_shape,  # shape of receptive field, e.g. (3,3)
                  conv_num_filters=None,  # e.g. 64 or None (which means 1 channel and don't add a dimension)
                  activation=default_override_or(identity),
                  init=default_override_or(C.glorot_uniform()),
                  conv_pad=default_override_or(False),
                  conv_strides=1,
                  bias=default_override_or(True),
                  init_bias=default_override_or(0),
                  reduction_rank=1,  # (0 means input has no depth dimension, e.g. audio signal or B&W image)
                  dilation=1,
                  groups=1,
                  pool_strides=1,
                  pool_pad=default_override_or(False),
                  name_prefix=''):
    """ Stack of Convolution 2D followed by one max pooling layer. Convenience wrapper. """

    conv_stack = Convolution2DStack(n, conv_filter_shape, conv_num_filters, activation, init, conv_pad, conv_strides,
                                    bias, init_bias, reduction_rank, dilation, groups, name_prefix)

    maxpool = MaxPooling(pool_filter_shape, pool_strides, pool_pad, name_prefix + '_pool')

    def layer(x):
        x = conv_stack(x)
        x = maxpool(x)
        return x

    return layer


def Convolution2DStack(num_conv_layers,  # num of convolutional layers in the stack
                       filter_shape,  # shape of receptive field, e.g. (3,3). Must be a 2-element tuple.
                       num_filters=None,  # e.g. 64 or None (which means 1 channel and don't add a dimension)
                       activation=default_override_or(identity),
                       init=default_override_or(C.glorot_uniform()),
                       pad=default_override_or(False),
                       strides=1,
                       bias=default_override_or(True),
                       init_bias=default_override_or(0),
                       reduction_rank=1,  # (0 means input has no depth dimension, e.g. audio signal or B&W image)
                       dilation=1,
                       groups=1,
                       name_prefix=''):
    """ A stack of of convolutional layers. Convenience wrapper. """

    convs = [Convolution2D(filter_shape, num_filters, activation, init, pad, strides, bias,
                           init_bias, reduction_rank, dilation, groups,
                           name_prefix + f'_conv_{i}') for i in range(num_conv_layers)]

    def inner(x):

        for conv in convs:
            x = conv(x)

        return x

    return inner


def SpatialPyramidPooling(bins: tuple, name=''):
    """ Spatial pyramid pooling layer for 2D inputs.

    See Spatial Pyramid Pooling in Deep Convolutional Networks for Visual Recognition,
    K. He, X. Zhang, S. Ren, J. Sun (https://arxiv.org/abs/1406.4729)

    SSP is used for multi-sized training where during training we implement the varying-input-size SPP-net
    by two fixed-size networks that share parameters. SSP layer will be different for the 2 network that
    shares parameters since the SSP would have different windows and stride.

    The final output shape would be input_num_filters * reduce_sum(square(bins))
    e.g. bins = (1, 3, 5) and input_num_filters = 32 then output_shape = (32 * (1 * 1 + 3 * 3 + 5 * 5), ) regardless
    of input feature map's spatial dimension.

    Arguments:
        bins (tuple): tuple of ints stating the depth of the pyramid and number of bins at each level.
        name (str, optional): name of layer

    Returns:
        :class:`~cntk.ops.functions.Function`:

    """

    def spp(x):
        spatial = x.shape[1:]
        filter_shapes = [tuple(math.ceil(s / bin) for s in spatial) for bin in bins]
        strides = [tuple(math.floor(s / bin) for s in spatial) for bin in bins]

        pools = [MaxPooling(filter_shape, stride, pad=False) for filter_shape, stride in zip(filter_shapes, strides)]
        features = [C.flatten(pool(x)) for pool in pools]
        return C.squeeze(C.splice(*features), name=name)

    return spp
