# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import pulumi
import pulumi.runtime
from . import utilities, tables

class RandomInteger(pulumi.CustomResource):
    keepers: pulumi.Output[dict]
    """
    Arbitrary map of values that, when changed, will
    trigger a new id to be generated. See
    the main provider documentation for more information.
    """
    max: pulumi.Output[int]
    """
    The maximum inclusive value of the range.
    """
    min: pulumi.Output[int]
    """
    The minimum inclusive value of the range.
    """
    result: pulumi.Output[int]
    """
    (int) The random Integer result.
    """
    seed: pulumi.Output[str]
    """
    A custom seed to always produce the same value.
    """
    def __init__(__self__, __name__, __opts__=None, keepers=None, max=None, min=None, seed=None):
        """
        The resource `random_integer` generates random values from a given range, described by the `min` and `max` attributes of a given resource.
        
        This resource can be used in conjunction with resources that have
        the `create_before_destroy` lifecycle flag set, to avoid conflicts with
        unique names during the brief period where both the old and new resources
        exist concurrently.
        
        
        :param str __name__: The name of the resource.
        :param pulumi.ResourceOptions __opts__: Options for the resource.
        :param pulumi.Input[dict] keepers: Arbitrary map of values that, when changed, will
               trigger a new id to be generated. See
               the main provider documentation for more information.
        :param pulumi.Input[int] max: The maximum inclusive value of the range.
        :param pulumi.Input[int] min: The minimum inclusive value of the range.
        :param pulumi.Input[str] seed: A custom seed to always produce the same value.
        """
        if not __name__:
            raise TypeError('Missing resource name argument (for URN creation)')
        if not isinstance(__name__, str):
            raise TypeError('Expected resource name to be a string')
        if __opts__ and not isinstance(__opts__, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')

        __props__ = dict()

        __props__['keepers'] = keepers

        if not max:
            raise TypeError('Missing required property max')
        __props__['max'] = max

        if not min:
            raise TypeError('Missing required property min')
        __props__['min'] = min

        __props__['seed'] = seed

        __props__['result'] = None

        super(RandomInteger, __self__).__init__(
            'random:index/randomInteger:RandomInteger',
            __name__,
            __props__,
            __opts__)


    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

