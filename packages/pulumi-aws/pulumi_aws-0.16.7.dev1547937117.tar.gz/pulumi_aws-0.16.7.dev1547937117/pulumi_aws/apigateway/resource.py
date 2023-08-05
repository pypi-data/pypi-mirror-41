# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import pulumi
import pulumi.runtime
from .. import utilities, tables

class Resource(pulumi.CustomResource):
    parent_id: pulumi.Output[str]
    """
    The ID of the parent API resource
    """
    path: pulumi.Output[str]
    """
    The complete path for this API resource, including all parent paths.
    """
    path_part: pulumi.Output[str]
    """
    The last path segment of this API resource.
    """
    rest_api: pulumi.Output[str]
    """
    The ID of the associated REST API
    """
    def __init__(__self__, __name__, __opts__=None, parent_id=None, path_part=None, rest_api=None):
        """
        Provides an API Gateway Resource.
        
        
        :param str __name__: The name of the resource.
        :param pulumi.ResourceOptions __opts__: Options for the resource.
        :param pulumi.Input[str] parent_id: The ID of the parent API resource
        :param pulumi.Input[str] path_part: The last path segment of this API resource.
        :param pulumi.Input[str] rest_api: The ID of the associated REST API
        """
        if not __name__:
            raise TypeError('Missing resource name argument (for URN creation)')
        if not isinstance(__name__, str):
            raise TypeError('Expected resource name to be a string')
        if __opts__ and not isinstance(__opts__, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')

        __props__ = dict()

        if not parent_id:
            raise TypeError('Missing required property parent_id')
        __props__['parent_id'] = parent_id

        if not path_part:
            raise TypeError('Missing required property path_part')
        __props__['path_part'] = path_part

        if not rest_api:
            raise TypeError('Missing required property rest_api')
        __props__['rest_api'] = rest_api

        __props__['path'] = None

        super(Resource, __self__).__init__(
            'aws:apigateway/resource:Resource',
            __name__,
            __props__,
            __opts__)


    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

