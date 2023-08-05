"""
    DarkNet, implemented in Gluon.
    Original source: 'Darknet: Open source neural networks in c,' https://github.com/pjreddie/darknet.
"""

__all__ = ['DarkNet', 'darknet_ref', 'darknet_tiny', 'darknet19']

import os
from mxnet import cpu
from mxnet.gluon import nn, HybridBlock
from .common import conv1x1_block, conv3x3_block


def dark_convYxY(in_channels,
                 out_channels,
                 bn_use_global_stats,
                 alpha,
                 pointwise):
    """
    DarkNet unit.

    Parameters:
    ----------
    in_channels : int
        Number of input channels.
    out_channels : int
        Number of output channels.
    bn_use_global_stats : bool
        Whether global moving statistics is used instead of local batch-norm for BatchNorm layers.
    alpha : float
        Slope coefficient for Leaky ReLU activation.
    pointwise : bool
        Whether use 1x1 (pointwise) convolution or 3x3 convolution.
    """
    if pointwise:
        return conv1x1_block(
            in_channels=in_channels,
            out_channels=out_channels,
            bn_use_global_stats=bn_use_global_stats,
            activation=nn.LeakyReLU(alpha=alpha))
    else:
        return conv3x3_block(
            in_channels=in_channels,
            out_channels=out_channels,
            bn_use_global_stats=bn_use_global_stats,
            activation=nn.LeakyReLU(alpha=alpha))


class DarkNet(HybridBlock):
    """
    DarkNet model from 'Darknet: Open source neural networks in c,' https://github.com/pjreddie/darknet.

    Parameters:
    ----------
    channels : list of list of int
        Number of output channels for each unit.
    odd_pointwise : bool
        Whether pointwise convolution layer is used for each odd unit.
    avg_pool_size : int
        Window size of the final average pooling.
    cls_activ : bool
        Whether classification convolution layer uses an activation.
    alpha : float, default 0.1
        Slope coefficient for Leaky ReLU activation.
    bn_use_global_stats : bool, default False
        Whether global moving statistics is used instead of local batch-norm for BatchNorm layers.
        Useful for fine-tuning.
    in_channels : int, default 3
        Number of input channels.
    in_size : tuple of two ints, default (224, 224)
        Spatial size of the expected input image.
    classes : int, default 1000
        Number of classification classes.
    """
    def __init__(self,
                 channels,
                 odd_pointwise,
                 avg_pool_size,
                 cls_activ,
                 alpha=0.1,
                 bn_use_global_stats=False,
                 in_channels=3,
                 in_size=(224, 224),
                 classes=1000,
                 **kwargs):
        super(DarkNet, self).__init__(**kwargs)
        self.in_size = in_size
        self.classes = classes

        with self.name_scope():
            self.features = nn.HybridSequential(prefix='')
            for i, channels_per_stage in enumerate(channels):
                stage = nn.HybridSequential(prefix='stage{}_'.format(i + 1))
                with stage.name_scope():
                    for j, out_channels in enumerate(channels_per_stage):
                        stage.add(dark_convYxY(
                            in_channels=in_channels,
                            out_channels=out_channels,
                            bn_use_global_stats=bn_use_global_stats,
                            alpha=alpha,
                            pointwise=(len(channels_per_stage) > 1) and not(((j + 1) % 2 == 1) ^ odd_pointwise)))
                        in_channels = out_channels
                    if i != len(channels) - 1:
                        stage.add(nn.MaxPool2D(
                            pool_size=2,
                            strides=2))
                self.features.add(stage)

            self.output = nn.HybridSequential(prefix='')
            self.output.add(nn.Conv2D(
                channels=classes,
                kernel_size=1,
                in_channels=in_channels))
            if cls_activ:
                self.output.add(nn.LeakyReLU(alpha=alpha))
            self.output.add(nn.AvgPool2D(
                pool_size=avg_pool_size,
                strides=1))
            self.output.add(nn.Flatten())

    def hybrid_forward(self, F, x):
        x = self.features(x)
        x = self.output(x)
        return x


def get_darknet(version,
                model_name=None,
                pretrained=False,
                ctx=cpu(),
                root=os.path.join('~', '.mxnet', 'models'),
                **kwargs):
    """
    Create DarkNet model with specific parameters.

    Parameters:
    ----------
    version : str
        Version of SqueezeNet ('ref', 'tiny' or '19').
    model_name : str or None, default None
        Model name for loading pretrained model.
    pretrained : bool, default False
        Whether to load the pretrained weights for model.
    ctx : Context, default CPU
        The context in which to load the pretrained weights.
    root : str, default '~/.mxnet/models'
        Location for keeping the model parameters.
    """

    if version == 'ref':
        channels = [[16], [32], [64], [128], [256], [512], [1024]]
        odd_pointwise = False
        avg_pool_size = 3
        cls_activ = True
    elif version == 'tiny':
        channels = [[16], [32], [16, 128, 16, 128], [32, 256, 32, 256], [64, 512, 64, 512, 128]]
        odd_pointwise = True
        avg_pool_size = 14
        cls_activ = False
    elif version == '19':
        channels = [[32], [64], [128, 64, 128], [256, 128, 256], [512, 256, 512, 256, 512],
                    [1024, 512, 1024, 512, 1024]]
        odd_pointwise = False
        avg_pool_size = 7
        cls_activ = False
    else:
        raise ValueError("Unsupported DarkNet version {}".format(version))

    net = DarkNet(
        channels=channels,
        odd_pointwise=odd_pointwise,
        avg_pool_size=avg_pool_size,
        cls_activ=cls_activ,
        **kwargs)

    if pretrained:
        if (model_name is None) or (not model_name):
            raise ValueError("Parameter `model_name` should be properly initialized for loading pretrained model.")
        from .model_store import get_model_file
        net.load_parameters(
            filename=get_model_file(
                model_name=model_name,
                local_model_store_dir_path=root),
            ctx=ctx)

    return net


def darknet_ref(**kwargs):
    """
    DarkNet 'Reference' model from 'Darknet: Open source neural networks in c,' https://github.com/pjreddie/darknet.

    Parameters:
    ----------
    pretrained : bool, default False
        Whether to load the pretrained weights for model.
    ctx : Context, default CPU
        The context in which to load the pretrained weights.
    root : str, default '~/.mxnet/models'
        Location for keeping the model parameters.
    """
    return get_darknet(version="ref", model_name="darknet_ref", **kwargs)


def darknet_tiny(**kwargs):
    """
    DarkNet Tiny model from 'Darknet: Open source neural networks in c,' https://github.com/pjreddie/darknet.

    Parameters:
    ----------
    pretrained : bool, default False
        Whether to load the pretrained weights for model.
    ctx : Context, default CPU
        The context in which to load the pretrained weights.
    root : str, default '~/.mxnet/models'
        Location for keeping the model parameters.
    """
    return get_darknet(version="tiny", model_name="darknet_tiny", **kwargs)


def darknet19(**kwargs):
    """
    DarkNet-19 model from 'Darknet: Open source neural networks in c,' https://github.com/pjreddie/darknet.

    Parameters:
    ----------
    pretrained : bool, default False
        Whether to load the pretrained weights for model.
    ctx : Context, default CPU
        The context in which to load the pretrained weights.
    root : str, default '~/.mxnet/models'
        Location for keeping the model parameters.
    """
    return get_darknet(version="19", model_name="darknet19", **kwargs)


def _test():
    import numpy as np
    import mxnet as mx

    pretrained = False

    models = [
        darknet_ref,
        darknet_tiny,
        darknet19,
    ]

    for model in models:

        net = model(pretrained=pretrained)

        ctx = mx.cpu()
        if not pretrained:
            net.initialize(ctx=ctx)

        # net.hybridize()
        net_params = net.collect_params()
        weight_count = 0
        for param in net_params.values():
            if (param.shape is None) or (not param._differentiable):
                continue
            weight_count += np.prod(param.shape)
        print("m={}, {}".format(model.__name__, weight_count))
        assert (model != darknet_ref or weight_count == 7319416)
        assert (model != darknet_tiny or weight_count == 1042104)
        assert (model != darknet19 or weight_count == 20842376)

        x = mx.nd.zeros((1, 3, 224, 224), ctx=ctx)
        y = net(x)
        assert (y.shape == (1, 1000))


if __name__ == "__main__":
    _test()
