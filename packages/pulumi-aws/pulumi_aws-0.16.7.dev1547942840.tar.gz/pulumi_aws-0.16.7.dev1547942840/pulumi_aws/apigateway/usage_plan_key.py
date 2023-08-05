# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import pulumi
import pulumi.runtime
from .. import utilities, tables

class UsagePlanKey(pulumi.CustomResource):
    key_id: pulumi.Output[str]
    """
    The identifier of the API key resource.
    """
    key_type: pulumi.Output[str]
    """
    The type of the API key resource. Currently, the valid key type is API_KEY.
    """
    name: pulumi.Output[str]
    """
    The name of a usage plan key.
    """
    usage_plan_id: pulumi.Output[str]
    """
    The Id of the usage plan resource representing to associate the key to.
    """
    value: pulumi.Output[str]
    """
    The value of a usage plan key.
    """
    def __init__(__self__, __name__, __opts__=None, key_id=None, key_type=None, usage_plan_id=None):
        """
        Provides an API Gateway Usage Plan Key.
        
        
        :param str __name__: The name of the resource.
        :param pulumi.ResourceOptions __opts__: Options for the resource.
        :param pulumi.Input[str] key_id: The identifier of the API key resource.
        :param pulumi.Input[str] key_type: The type of the API key resource. Currently, the valid key type is API_KEY.
        :param pulumi.Input[str] usage_plan_id: The Id of the usage plan resource representing to associate the key to.
        """
        if not __name__:
            raise TypeError('Missing resource name argument (for URN creation)')
        if not isinstance(__name__, str):
            raise TypeError('Expected resource name to be a string')
        if __opts__ and not isinstance(__opts__, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')

        __props__ = dict()

        if not key_id:
            raise TypeError('Missing required property key_id')
        __props__['key_id'] = key_id

        if not key_type:
            raise TypeError('Missing required property key_type')
        __props__['key_type'] = key_type

        if not usage_plan_id:
            raise TypeError('Missing required property usage_plan_id')
        __props__['usage_plan_id'] = usage_plan_id

        __props__['name'] = None
        __props__['value'] = None

        super(UsagePlanKey, __self__).__init__(
            'aws:apigateway/usagePlanKey:UsagePlanKey',
            __name__,
            __props__,
            __opts__)


    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

