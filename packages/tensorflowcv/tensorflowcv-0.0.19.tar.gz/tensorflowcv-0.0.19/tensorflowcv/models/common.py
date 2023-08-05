"""
    Common routines for models in TensorFlow.
"""

__all__ = ['conv2d', 'conv1x1', 'conv3x3', 'depthwise_conv3x3', 'batchnorm', 'maxpool2d', 'avgpool2d', 'conv_block',
           'conv1x1_block', 'conv3x3_block', 'conv7x7_block', 'dwconv3x3_block', 'pre_conv_block', 'pre_conv1x1_block',
           'pre_conv3x3_block', 'se_block', 'channel_shuffle', 'channel_shuffle2']

import math
import tensorflow as tf


def conv2d(x,
           in_channels,
           out_channels,
           kernel_size,
           strides=1,
           padding=0,
           dilation=1,
           groups=1,
           use_bias=True,
           name="conv2d"):
    """
    Convolution 2D layer wrapper.

    Parameters:
    ----------
    x : Tensor
        Input tensor.
    in_channels : int
        Number of input channels.
    out_channels : int
        Number of output channels.
    kernel_size : int or tuple/list of 2 int
        Convolution window size.
    strides : int or tuple/list of 2 int
        Strides of the convolution.
    padding : int or tuple/list of 2 int
        Padding value for convolution layer.
    dilation : int or tuple/list of 2 int, default 1
        Dilation value for convolution layer.
    groups : int, default 1
        Number of groups.
    use_bias : bool, default False
        Whether the layer uses a bias vector.
    name : str, default 'conv2d'
        Layer name.

    Returns
    -------
    Tensor
        Resulted tensor.
    """
    if isinstance(kernel_size, int):
        kernel_size = (kernel_size, kernel_size)
    if isinstance(strides, int):
        strides = (strides, strides)
    if isinstance(padding, int):
        padding = (padding, padding)
    if isinstance(dilation, int):
        dilation = (dilation, dilation)

    if (padding[0] > 0) or (padding[1] > 0):
        x = tf.pad(x, [[0, 0], [0, 0], list(padding), list(padding)])

    if groups == 1:
        x = tf.layers.conv2d(
            inputs=x,
            filters=out_channels,
            kernel_size=kernel_size,
            strides=strides,
            padding='valid',
            data_format='channels_first',
            dilation_rate=dilation,
            use_bias=use_bias,
            kernel_initializer=tf.contrib.layers.variance_scaling_initializer(2.0),
            name=name)
    elif (groups == out_channels) and (out_channels == in_channels):
        assert (dilation[0] == 1) and (dilation[1] == 1)
        kernel = tf.get_variable(
            name=name + '/dw_kernel',
            shape=kernel_size + (in_channels, 1),
            initializer=tf.variance_scaling_initializer(2.0))
        x = tf.nn.depthwise_conv2d(
            input=x,
            filter=kernel,
            strides=(1, 1) + strides,
            padding='VALID',
            rate=(1, 1),
            name=name,
            data_format='NCHW')
        if use_bias:
            raise NotImplementedError
    else:
        assert (in_channels % groups == 0)
        assert (out_channels % groups == 0)
        in_group_channels = in_channels // groups
        out_group_channels = out_channels // groups
        group_list = []
        for gi in range(groups):
            xi = x[:, gi * in_group_channels:(gi + 1) * in_group_channels, :, :]
            xi = tf.layers.conv2d(
                inputs=xi,
                filters=out_group_channels,
                kernel_size=kernel_size,
                strides=strides,
                padding='valid',
                data_format='channels_first',
                dilation_rate=dilation,
                use_bias=use_bias,
                kernel_initializer=tf.contrib.layers.variance_scaling_initializer(2.0),
                name=name + "/convgroup{}".format(gi + 1))
            group_list.append(xi)
        x = tf.concat(group_list, axis=1, name=name + "/concat")

    return x


def conv1x1(x,
            in_channels,
            out_channels,
            strides=1,
            groups=1,
            use_bias=False,
            name="conv1x1"):
    """
    Convolution 1x1 layer.

    Parameters:
    ----------
    x : Tensor
        Input tensor.
    in_channels : int
        Number of input channels.
    out_channels : int
        Number of output channels.
    strides : int or tuple/list of 2 int, default 1
        Strides of the convolution.
    groups : int, default 1
        Number of groups.
    use_bias : bool, default False
        Whether the layer uses a bias vector.
    name : str, default 'conv1x1'
        Layer name.

    Returns
    -------
    Tensor
        Resulted tensor.
    """
    return conv2d(
        x=x,
        in_channels=in_channels,
        out_channels=out_channels,
        kernel_size=1,
        strides=strides,
        groups=groups,
        use_bias=use_bias,
        name=name)


def conv3x3(x,
            in_channels,
            out_channels,
            strides=1,
            padding=1,
            groups=1,
            use_bias=False,
            name="conv3x3"):
    """
    Convolution 3x3 layer.

    Parameters:
    ----------
    x : Tensor
        Input tensor.
    in_channels : int
        Number of input channels.
    out_channels : int
        Number of output channels.
    strides : int or tuple/list of 2 int, default 1
        Strides of the convolution.
    padding : int or tuple/list of 2 int, default 1
        Padding value for convolution layer.
    groups : int, default 1
        Number of groups.
    use_bias : bool, default False
        Whether the layer uses a bias vector.
    name : str, default 'conv3x3'
        Block name.

    Returns
    -------
    Tensor
        Resulted tensor.
    """
    return conv2d(
        x=x,
        in_channels=in_channels,
        out_channels=out_channels,
        kernel_size=3,
        strides=strides,
        padding=padding,
        groups=groups,
        use_bias=use_bias,
        name=name)


def depthwise_conv3x3(x,
                      channels,
                      strides,
                      name="depthwise_conv3x3"):
    """
    Depthwise convolution 3x3 layer.

    Parameters:
    ----------
    x : Tensor
        Input tensor.
    channels : int
        Number of input/output channels.
    strides : int or tuple/list of 2 int
        Strides of the convolution.
    name : str, default 'depthwise_conv3x3'
        Block name.

    Returns
    -------
    Tensor
        Resulted tensor.
    """
    return conv2d(
        x=x,
        in_channels=channels,
        out_channels=channels,
        kernel_size=3,
        strides=strides,
        padding=1,
        groups=channels,
        use_bias=False,
        name=name)


def batchnorm(x,
              momentum=0.9,
              epsilon=1e-5,
              training=False,
              name=None):
    """
    Batch normalization layer.

    Parameters:
    ----------
    x : Tensor
        Input tensor.
    momentum : float, default 0.9
        Momentum for the moving average.
    epsilon : float, default 1e-5
        Small float added to variance to avoid dividing by zero.
    training : bool, or a TensorFlow boolean scalar tensor, default False
      Whether to return the output in training mode or in inference mode.
    name : str, default 'conv2d'
        Layer name.

    Returns
    -------
    Tensor
        Resulted tensor.
    """
    x = tf.layers.batch_normalization(
        inputs=x,
        axis=1,
        momentum=momentum,
        epsilon=epsilon,
        training=training,
        name=name)
    return x


def maxpool2d(x,
              pool_size,
              strides,
              padding=0,
              ceil_mode=False,
              name=None):
    """
    Max pooling operation for two dimensional (spatial) data.

    Parameters:
    ----------
    x : Tensor
        Input tensor.
    pool_size : int or tuple/list of 2 int
        Size of the max pooling windows.
    strides : int or tuple/list of 2 int
        Strides of the pooling.
    padding : int or tuple/list of 2 int, default 0
        Padding value for convolution layer.
    ceil_mode : bool, default False
        When `True`, will use ceil instead of floor to compute the output shape.
    name : str, default 'conv2d'
        Layer name.

    Returns
    -------
    Tensor
        Resulted tensor.
    """
    if isinstance(pool_size, int):
        pool_size = (pool_size, pool_size)
    if isinstance(strides, int):
        strides = (strides, strides)
    if isinstance(padding, int):
        padding = (padding, padding)

    if ceil_mode:
        height = int(x.shape[2])
        out_height = float(height + 2 * padding[0] - pool_size[0]) / strides[0] + 1.0
        if math.ceil(out_height) > math.floor(out_height):
            padding = (padding[0] + 1, padding[1])
        width = int(x.shape[3])
        out_width = float(width + 2 * padding[1] - pool_size[1]) / strides[1] + 1.0
        if math.ceil(out_width) > math.floor(out_width):
            padding = (padding[0], padding[1] + 1)

    if (padding[0] > 0) or (padding[1] > 0):
        x = tf.pad(x, [[0, 0], [0, 0], list(padding), list(padding)], mode="REFLECT")

    x = tf.layers.max_pooling2d(
        inputs=x,
        pool_size=pool_size,
        strides=strides,
        padding='valid',
        data_format='channels_first',
        name=name)
    return x


def avgpool2d(x,
              pool_size,
              strides,
              padding=0,
              ceil_mode=False,
              name=None):
    """
    Average pooling operation for two dimensional (spatial) data.

    Parameters:
    ----------
    x : Tensor
        Input tensor.
    pool_size : int or tuple/list of 2 int
        Size of the max pooling windows.
    strides : int or tuple/list of 2 int
        Strides of the pooling.
    padding : int or tuple/list of 2 int, default 0
        Padding value for convolution layer.
    ceil_mode : bool, default False
        When `True`, will use ceil instead of floor to compute the output shape.
    name : str, default 'conv2d'
        Layer name.

    Returns
    -------
    Tensor
        Resulted tensor.
    """
    if isinstance(pool_size, int):
        pool_size = (pool_size, pool_size)
    if isinstance(strides, int):
        strides = (strides, strides)
    if isinstance(padding, int):
        padding = (padding, padding)

    if ceil_mode:
        height = int(x.shape[2])
        out_height = float(height + 2 * padding[0] - pool_size[0]) / strides[0] + 1.0
        if math.ceil(out_height) > math.floor(out_height):
            padding = (padding[0] + 1, padding[1])
        width = int(x.shape[3])
        out_width = float(width + 2 * padding[1] - pool_size[1]) / strides[1] + 1.0
        if math.ceil(out_width) > math.floor(out_width):
            padding = (padding[0], padding[1] + 1)

    if (padding[0] > 0) or (padding[1] > 0):
        x = tf.pad(x, [[0, 0], [0, 0], list(padding), list(padding)], mode="CONSTANT")

    x = tf.layers.average_pooling2d(
        inputs=x,
        pool_size=pool_size,
        strides=1,
        padding='valid',
        data_format='channels_first',
        name=name)

    if (strides[0] > 1) or (strides[1] > 1):
        x = tf.layers.average_pooling2d(
            inputs=x,
            pool_size=1,
            strides=strides,
            padding='valid',
            data_format='channels_first',
            name=name + "/stride")
    return x


def conv_block(x,
               in_channels,
               out_channels,
               kernel_size,
               strides,
               padding,
               dilation=1,
               groups=1,
               use_bias=False,
               activation="relu",
               activate=True,
               training=False,
               name="conv_block"):
    """
    Standard convolution block with Batch normalization and ReLU/ReLU6 activation.

    Parameters:
    ----------
    x : Tensor
        Input tensor.
    in_channels : int
        Number of input channels.
    out_channels : int
        Number of output channels.
    kernel_size : int or tuple/list of 2 int
        Convolution window size.
    strides : int or tuple/list of 2 int
        Strides of the convolution.
    padding : int or tuple/list of 2 int
        Padding value for convolution layer.
    dilation : int or tuple/list of 2 int, default 1
        Dilation value for convolution layer.
    groups : int, default 1
        Number of groups.
    use_bias : bool, default False
        Whether the layer uses a bias vector.
    activation : function or str or None, default 'relu'
        Activation function or name of activation function.
    activate : bool, default True
        Whether activate the convolution block.
    training : bool, or a TensorFlow boolean scalar tensor, default False
      Whether to return the output in training mode or in inference mode.
    name : str, default 'conv_block'
        Block name.

    Returns
    -------
    Tensor
        Resulted tensor.
    """
    x = conv2d(
        x=x,
        in_channels=in_channels,
        out_channels=out_channels,
        kernel_size=kernel_size,
        strides=strides,
        padding=padding,
        dilation=dilation,
        groups=groups,
        use_bias=use_bias,
        name=name + "/conv")
    x = batchnorm(
        x=x,
        training=training,
        name=name + "/bn")
    if activate:
        assert (activation is not None)
        if isinstance(activation, str):
            if activation == "relu":
                x = tf.nn.relu(x, name=name + "/activ")
            elif activation == "relu6":
                x = tf.nn.relu6(x, name=name + "/activ")
            else:
                raise NotImplementedError()
        else:
            x = activation(x)
    return x


def conv1x1_block(x,
                  in_channels,
                  out_channels,
                  strides=1,
                  groups=1,
                  use_bias=False,
                  activation="relu",
                  activate=True,
                  training=False,
                  name="conv1x1_block"):
    """
    1x1 version of the standard convolution block.

    Parameters:
    ----------
    x : Tensor
        Input tensor.
    in_channels : int
        Number of input channels.
    out_channels : int
        Number of output channels.
    strides : int or tuple/list of 2 int, default 1
        Strides of the convolution.
    groups : int, default 1
        Number of groups.
    use_bias : bool, default False
        Whether the layer uses a bias vector.
    activation : function or str or None, default 'relu'
        Activation function or name of activation function.
    activate : bool, default True
        Whether activate the convolution block.
    training : bool, or a TensorFlow boolean scalar tensor, default False
      Whether to return the output in training mode or in inference mode.
    name : str, default 'conv1x1_block'
        Block name.

    Returns
    -------
    Tensor
        Resulted tensor.
    """
    return conv_block(
        x=x,
        in_channels=in_channels,
        out_channels=out_channels,
        kernel_size=1,
        strides=strides,
        padding=0,
        groups=groups,
        use_bias=use_bias,
        activation=activation,
        activate=activate,
        training=training,
        name=name)


def conv3x3_block(x,
                  in_channels,
                  out_channels,
                  strides=1,
                  padding=1,
                  dilation=1,
                  groups=1,
                  use_bias=False,
                  activation="relu",
                  activate=True,
                  training=False,
                  name="conv3x3_block"):
    """
    3x3 version of the standard convolution block.

    Parameters:
    ----------
    x : Tensor
        Input tensor.
    in_channels : int
        Number of input channels.
    out_channels : int
        Number of output channels.
    strides : int or tuple/list of 2 int, default 1
        Strides of the convolution.
    padding : int or tuple/list of 2 int, default 1
        Padding value for convolution layer.
    dilation : int or tuple/list of 2 int, default 1
        Dilation value for convolution layer.
    groups : int, default 1
        Number of groups.
    use_bias : bool, default False
        Whether the layer uses a bias vector.
    activation : function or str or None, default 'relu'
        Activation function or name of activation function.
    activate : bool, default True
        Whether activate the convolution block.
    training : bool, or a TensorFlow boolean scalar tensor, default False
      Whether to return the output in training mode or in inference mode.
    name : str, default 'conv3x3_block'
        Block name.

    Returns
    -------
    Tensor
        Resulted tensor.
    """
    return conv_block(
        x=x,
        in_channels=in_channels,
        out_channels=out_channels,
        kernel_size=3,
        strides=strides,
        padding=padding,
        dilation=dilation,
        groups=groups,
        use_bias=use_bias,
        activation=activation,
        activate=activate,
        training=training,
        name=name)


def conv7x7_block(x,
                  in_channels,
                  out_channels,
                  strides=1,
                  padding=3,
                  use_bias=False,
                  activation="relu",
                  activate=True,
                  training=False,
                  name="conv7x7_block"):
    """
    3x3 version of the standard convolution block.

    Parameters:
    ----------
    x : Tensor
        Input tensor.
    in_channels : int
        Number of input channels.
    out_channels : int
        Number of output channels.
    strides : int or tuple/list of 2 int, default 1
        Strides of the convolution.
    padding : int or tuple/list of 2 int, default 3
        Padding value for convolution layer.
    use_bias : bool, default False
        Whether the layer uses a bias vector.
    activation : function or str or None, default 'relu'
        Activation function or name of activation function.
    activate : bool, default True
        Whether activate the convolution block.
    training : bool, or a TensorFlow boolean scalar tensor, default False
      Whether to return the output in training mode or in inference mode.
    name : str, default 'conv7x7_block'
        Block name.

    Returns
    -------
    Tensor
        Resulted tensor.
    """
    return conv_block(
        x=x,
        in_channels=in_channels,
        out_channels=out_channels,
        kernel_size=7,
        strides=strides,
        padding=padding,
        use_bias=use_bias,
        activation=activation,
        activate=activate,
        training=training,
        name=name)


def dwconv3x3_block(x,
                    in_channels,
                    out_channels,
                    strides,
                    padding=1,
                    dilation=1,
                    use_bias=False,
                    activation="relu",
                    activate=True,
                    training=False,
                    name="dwconv3x3_block"):
    """
    3x3 depthwise version of the standard convolution block with ReLU6 activation.

    Parameters:
    ----------
    x : Tensor
        Input tensor.
    in_channels : int
        Number of input channels.
    out_channels : int
        Number of output channels.
    strides : int or tuple/list of 2 int
        Strides of the convolution.
    padding : int or tuple/list of 2 int, default 1
        Padding value for convolution layer.
    dilation : int or tuple/list of 2 int, default 1
        Dilation value for convolution layer.
    use_bias : bool, default False
        Whether the layer uses a bias vector.
    activation : function or str or None, default 'relu'
        Activation function or name of activation function.
    activate : bool, default True
        Whether activate the convolution block.
    training : bool, or a TensorFlow boolean scalar tensor, default False
      Whether to return the output in training mode or in inference mode.
    name : str, default 'dwconv3x3_block'
        Block name.

    Returns
    -------
    Tensor
        Resulted tensor.
    """
    return conv3x3_block(
        x=x,
        in_channels=in_channels,
        out_channels=out_channels,
        strides=strides,
        padding=padding,
        dilation=dilation,
        groups=out_channels,
        use_bias=use_bias,
        activation=activation,
        activate=activate,
        training=training,
        name=name)


def pre_conv_block(x,
                   in_channels,
                   out_channels,
                   kernel_size,
                   strides,
                   padding,
                   return_preact=False,
                   training=False,
                   name="pre_conv_block"):
    """
    Convolution block with Batch normalization and ReLU pre-activation.

    Parameters:
    ----------
    x : Tensor
        Input tensor.
    in_channels : int
        Number of input channels.
    out_channels : int
        Number of output channels.
    kernel_size : int or tuple/list of 2 int
        Convolution window size.
    strides : int or tuple/list of 2 int
        Strides of the convolution.
    padding : int or tuple/list of 2 int
        Padding value for convolution layer.
    return_preact : bool, default False
        Whether return pre-activation. It's used by PreResNet.
    training : bool, or a TensorFlow boolean scalar tensor, default False
      Whether to return the output in training mode or in inference mode.
    name : str, default 'pre_conv_block'
        Block name.

    Returns
    -------
    tuple of two Tensors
        Resulted tensor and preactivated input tensor.
    """
    x = batchnorm(
        x=x,
        training=training,
        name=name + "/bn")
    x = tf.nn.relu(x, name=name + "/activ")
    if return_preact:
        x_pre_activ = x
    x = conv2d(
        x=x,
        in_channels=in_channels,
        out_channels=out_channels,
        kernel_size=kernel_size,
        strides=strides,
        padding=padding,
        use_bias=False,
        name=name + "/conv")
    if return_preact:
        return x, x_pre_activ
    else:
        return x


def pre_conv1x1_block(x,
                      in_channels,
                      out_channels,
                      strides=1,
                      return_preact=False,
                      training=False,
                      name="pre_conv1x1_block"):
    """
    1x1 version of the pre-activated convolution block.

    Parameters:
    ----------
    x : Tensor
        Input tensor.
    in_channels : int
        Number of input channels.
    out_channels : int
        Number of output channels.
    strides : int or tuple/list of 2 int, default 1
        Strides of the convolution.
    return_preact : bool, default False
        Whether return pre-activation. It's used by PreResNet.
    training : bool, or a TensorFlow boolean scalar tensor, default False
      Whether to return the output in training mode or in inference mode.
    name : str, default 'pre_conv1x1_block'
        Block name.

    Returns
    -------
    tuple of two Tensors
        Resulted tensor and preactivated input tensor.
    """
    return pre_conv_block(
        x=x,
        in_channels=in_channels,
        out_channels=out_channels,
        kernel_size=1,
        strides=strides,
        padding=0,
        return_preact=return_preact,
        training=training,
        name=name)


def pre_conv3x3_block(x,
                      in_channels,
                      out_channels,
                      strides=1,
                      return_preact=False,
                      training=False,
                      name="pre_conv3x3_block"):
    """
    3x3 version of the pre-activated convolution block.

    Parameters:
    ----------
    x : Tensor
        Input tensor.
    in_channels : int
        Number of input channels.
    out_channels : int
        Number of output channels.
    strides : int or tuple/list of 2 int, default 1
        Strides of the convolution.
    return_preact : bool, default False
        Whether return pre-activation. It's used by PreResNet.
    training : bool, or a TensorFlow boolean scalar tensor, default False
      Whether to return the output in training mode or in inference mode.
    name : str, default 'pre_conv3x3_block'
        Block name.

    Returns
    -------
    tuple of two Tensors
        Resulted tensor and preactivated input tensor.
    """
    return pre_conv_block(
        x=x,
        in_channels=in_channels,
        out_channels=out_channels,
        kernel_size=3,
        strides=strides,
        padding=1,
        return_preact=return_preact,
        training=training,
        name=name)


def channel_shuffle(x,
                    groups):
    """
    Channel shuffle operation from 'ShuffleNet: An Extremely Efficient Convolutional Neural Network for Mobile Devices,'
    https://arxiv.org/abs/1707.01083.

    Parameters:
    ----------
    x : Tensor
        Input tensor.
    groups : int
        Number of groups.

    Returns
    -------
    keras.Tensor
        Resulted tensor.
    """
    x_shape = x.get_shape().as_list()
    channels = x_shape[1]
    height = x_shape[2]
    width = x_shape[3]

    assert (channels % groups == 0)
    channels_per_group = channels // groups

    x = tf.reshape(x, shape=(-1, groups, channels_per_group, height, width))
    x = tf.transpose(x, perm=(0, 2, 1, 3, 4))
    x = tf.reshape(x, shape=(-1, channels, height, width))
    return x


def channel_shuffle2(x,
                     groups):
    """
    Channel shuffle operation from 'ShuffleNet: An Extremely Efficient Convolutional Neural Network for Mobile Devices,'
    https://arxiv.org/abs/1707.01083.
    The alternative version.

    Parameters:
    ----------
    x : Tensor
        Input tensor.
    groups : int
        Number of groups.

    Returns
    -------
    keras.Tensor
        Resulted tensor.
    """
    x_shape = x.get_shape().as_list()
    channels = x_shape[1]
    height = x_shape[2]
    width = x_shape[3]

    assert (channels % groups == 0)
    channels_per_group = channels // groups

    x = tf.reshape(x, shape=(-1, channels_per_group, groups, height, width))
    x = tf.transpose(x, perm=(0, 2, 1, 3, 4))
    x = tf.reshape(x, shape=(-1, channels, height, width))
    return x


def se_block(x,
             channels,
             reduction=16,
             name="se_block"):
    """
    Squeeze-and-Excitation block from 'Squeeze-and-Excitation Networks,' https://arxiv.org/abs/1709.01507.

    Parameters:
    ----------
    x : Tensor
        Input tensor.
    channels : int
        Number of channels.
    reduction : int, default 16
        Squeeze reduction value.
    name : str, default 'se_block'
        Block name.

    Returns
    -------
    Tensor
        Resulted tensor.
    """
    assert(len(x.shape) == 4)
    mid_cannels = channels // reduction
    pool_size = x.shape[2:4]

    w = tf.layers.average_pooling2d(
        inputs=x,
        pool_size=pool_size,
        strides=1,
        data_format='channels_first',
        name=name + "/pool")
    w = conv1x1(
        x=w,
        in_channels=channels,
        out_channels=mid_cannels,
        use_bias=True,
        name=name + "/conv1/conv")
    w = tf.nn.relu(w, name=name + "/relu")
    w = conv1x1(
        x=w,
        in_channels=mid_cannels,
        out_channels=channels,
        use_bias=True,
        name=name + "/conv2/conv")
    w = tf.nn.sigmoid(w, name=name + "/sigmoid")
    x = x * w
    return x
