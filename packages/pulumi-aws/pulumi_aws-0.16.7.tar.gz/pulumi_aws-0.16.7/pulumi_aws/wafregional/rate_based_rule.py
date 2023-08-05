# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import pulumi
import pulumi.runtime
from .. import utilities, tables

class RateBasedRule(pulumi.CustomResource):
    metric_name: pulumi.Output[str]
    """
    The name or description for the Amazon CloudWatch metric of this rule.
    """
    name: pulumi.Output[str]
    """
    The name or description of the rule.
    """
    predicates: pulumi.Output[list]
    """
    One of ByteMatchSet, IPSet, SizeConstraintSet, SqlInjectionMatchSet, or XssMatchSet objects to include in a rule.
    """
    rate_key: pulumi.Output[str]
    """
    Valid value is IP.
    """
    rate_limit: pulumi.Output[int]
    """
    The maximum number of requests, which have an identical value in the field specified by the RateKey, allowed in a five-minute period. Minimum value is 2000.
    """
    def __init__(__self__, __name__, __opts__=None, metric_name=None, name=None, predicates=None, rate_key=None, rate_limit=None):
        """
        Provides a WAF Rate Based Rule Resource
        
        
        :param str __name__: The name of the resource.
        :param pulumi.ResourceOptions __opts__: Options for the resource.
        :param pulumi.Input[str] metric_name: The name or description for the Amazon CloudWatch metric of this rule.
        :param pulumi.Input[str] name: The name or description of the rule.
        :param pulumi.Input[list] predicates: One of ByteMatchSet, IPSet, SizeConstraintSet, SqlInjectionMatchSet, or XssMatchSet objects to include in a rule.
        :param pulumi.Input[str] rate_key: Valid value is IP.
        :param pulumi.Input[int] rate_limit: The maximum number of requests, which have an identical value in the field specified by the RateKey, allowed in a five-minute period. Minimum value is 2000.
        """
        if not __name__:
            raise TypeError('Missing resource name argument (for URN creation)')
        if not isinstance(__name__, str):
            raise TypeError('Expected resource name to be a string')
        if __opts__ and not isinstance(__opts__, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')

        __props__ = dict()

        if not metric_name:
            raise TypeError('Missing required property metric_name')
        __props__['metric_name'] = metric_name

        __props__['name'] = name

        __props__['predicates'] = predicates

        if not rate_key:
            raise TypeError('Missing required property rate_key')
        __props__['rate_key'] = rate_key

        if not rate_limit:
            raise TypeError('Missing required property rate_limit')
        __props__['rate_limit'] = rate_limit

        super(RateBasedRule, __self__).__init__(
            'aws:wafregional/rateBasedRule:RateBasedRule',
            __name__,
            __props__,
            __opts__)


    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

