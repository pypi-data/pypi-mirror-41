# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import pulumi
import pulumi.runtime
from .. import utilities, tables

class WebAcl(pulumi.CustomResource):
    default_action: pulumi.Output[dict]
    """
    The action that you want AWS WAF to take when a request doesn't match the criteria in any of the rules that are associated with the web ACL.
    """
    metric_name: pulumi.Output[str]
    """
    The name or description for the Amazon CloudWatch metric of this web ACL.
    """
    name: pulumi.Output[str]
    """
    The name or description of the web ACL.
    """
    rules: pulumi.Output[list]
    """
    The rules to associate with the web ACL and the settings for each rule.
    """
    def __init__(__self__, __name__, __opts__=None, default_action=None, metric_name=None, name=None, rules=None):
        """
        Provides a WAF Web ACL Resource
        
        
        :param str __name__: The name of the resource.
        :param pulumi.ResourceOptions __opts__: Options for the resource.
        :param pulumi.Input[dict] default_action: The action that you want AWS WAF to take when a request doesn't match the criteria in any of the rules that are associated with the web ACL.
        :param pulumi.Input[str] metric_name: The name or description for the Amazon CloudWatch metric of this web ACL.
        :param pulumi.Input[str] name: The name or description of the web ACL.
        :param pulumi.Input[list] rules: The rules to associate with the web ACL and the settings for each rule.
        """
        if not __name__:
            raise TypeError('Missing resource name argument (for URN creation)')
        if not isinstance(__name__, str):
            raise TypeError('Expected resource name to be a string')
        if __opts__ and not isinstance(__opts__, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')

        __props__ = dict()

        if not default_action:
            raise TypeError('Missing required property default_action')
        __props__['default_action'] = default_action

        if not metric_name:
            raise TypeError('Missing required property metric_name')
        __props__['metric_name'] = metric_name

        __props__['name'] = name

        __props__['rules'] = rules

        super(WebAcl, __self__).__init__(
            'aws:waf/webAcl:WebAcl',
            __name__,
            __props__,
            __opts__)


    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

