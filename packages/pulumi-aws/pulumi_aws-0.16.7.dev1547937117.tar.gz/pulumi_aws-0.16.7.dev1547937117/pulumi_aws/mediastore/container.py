# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import pulumi
import pulumi.runtime
from .. import utilities, tables

class Container(pulumi.CustomResource):
    arn: pulumi.Output[str]
    """
    The ARN of the container.
    """
    endpoint: pulumi.Output[str]
    """
    The DNS endpoint of the container.
    """
    name: pulumi.Output[str]
    """
    The name of the container. Must contain alphanumeric characters or underscores.
    """
    def __init__(__self__, __name__, __opts__=None, name=None):
        """
        Provides a MediaStore Container.
        
        
        :param str __name__: The name of the resource.
        :param pulumi.ResourceOptions __opts__: Options for the resource.
        :param pulumi.Input[str] name: The name of the container. Must contain alphanumeric characters or underscores.
        """
        if not __name__:
            raise TypeError('Missing resource name argument (for URN creation)')
        if not isinstance(__name__, str):
            raise TypeError('Expected resource name to be a string')
        if __opts__ and not isinstance(__opts__, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')

        __props__ = dict()

        __props__['name'] = name

        __props__['arn'] = None
        __props__['endpoint'] = None

        super(Container, __self__).__init__(
            'aws:mediastore/container:Container',
            __name__,
            __props__,
            __opts__)


    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

