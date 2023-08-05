# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import pulumi
import pulumi.runtime
from .. import utilities, tables

class ReceiptRule(pulumi.CustomResource):
    add_header_actions: pulumi.Output[list]
    """
    A list of Add Header Action blocks. Documented below.
    """
    after: pulumi.Output[str]
    """
    The name of the rule to place this rule after
    """
    bounce_actions: pulumi.Output[list]
    """
    A list of Bounce Action blocks. Documented below.
    """
    enabled: pulumi.Output[bool]
    """
    If true, the rule will be enabled
    """
    lambda_actions: pulumi.Output[list]
    """
    A list of Lambda Action blocks. Documented below.
    """
    name: pulumi.Output[str]
    """
    The name of the rule
    """
    recipients: pulumi.Output[list]
    """
    A list of email addresses
    """
    rule_set_name: pulumi.Output[str]
    """
    The name of the rule set
    """
    s3_actions: pulumi.Output[list]
    """
    A list of S3 Action blocks. Documented below.
    """
    scan_enabled: pulumi.Output[bool]
    """
    If true, incoming emails will be scanned for spam and viruses
    """
    sns_actions: pulumi.Output[list]
    """
    A list of SNS Action blocks. Documented below.
    """
    stop_actions: pulumi.Output[list]
    """
    A list of Stop Action blocks. Documented below.
    """
    tls_policy: pulumi.Output[str]
    """
    Require or Optional
    """
    workmail_actions: pulumi.Output[list]
    """
    A list of WorkMail Action blocks. Documented below.
    """
    def __init__(__self__, __name__, __opts__=None, add_header_actions=None, after=None, bounce_actions=None, enabled=None, lambda_actions=None, name=None, recipients=None, rule_set_name=None, s3_actions=None, scan_enabled=None, sns_actions=None, stop_actions=None, tls_policy=None, workmail_actions=None):
        """
        Provides an SES receipt rule resource
        
        
        :param str __name__: The name of the resource.
        :param pulumi.ResourceOptions __opts__: Options for the resource.
        :param pulumi.Input[list] add_header_actions: A list of Add Header Action blocks. Documented below.
        :param pulumi.Input[str] after: The name of the rule to place this rule after
        :param pulumi.Input[list] bounce_actions: A list of Bounce Action blocks. Documented below.
        :param pulumi.Input[bool] enabled: If true, the rule will be enabled
        :param pulumi.Input[list] lambda_actions: A list of Lambda Action blocks. Documented below.
        :param pulumi.Input[str] name: The name of the rule
        :param pulumi.Input[list] recipients: A list of email addresses
        :param pulumi.Input[str] rule_set_name: The name of the rule set
        :param pulumi.Input[list] s3_actions: A list of S3 Action blocks. Documented below.
        :param pulumi.Input[bool] scan_enabled: If true, incoming emails will be scanned for spam and viruses
        :param pulumi.Input[list] sns_actions: A list of SNS Action blocks. Documented below.
        :param pulumi.Input[list] stop_actions: A list of Stop Action blocks. Documented below.
        :param pulumi.Input[str] tls_policy: Require or Optional
        :param pulumi.Input[list] workmail_actions: A list of WorkMail Action blocks. Documented below.
        """
        if not __name__:
            raise TypeError('Missing resource name argument (for URN creation)')
        if not isinstance(__name__, str):
            raise TypeError('Expected resource name to be a string')
        if __opts__ and not isinstance(__opts__, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')

        __props__ = dict()

        __props__['add_header_actions'] = add_header_actions

        __props__['after'] = after

        __props__['bounce_actions'] = bounce_actions

        __props__['enabled'] = enabled

        __props__['lambda_actions'] = lambda_actions

        __props__['name'] = name

        __props__['recipients'] = recipients

        if not rule_set_name:
            raise TypeError('Missing required property rule_set_name')
        __props__['rule_set_name'] = rule_set_name

        __props__['s3_actions'] = s3_actions

        __props__['scan_enabled'] = scan_enabled

        __props__['sns_actions'] = sns_actions

        __props__['stop_actions'] = stop_actions

        __props__['tls_policy'] = tls_policy

        __props__['workmail_actions'] = workmail_actions

        super(ReceiptRule, __self__).__init__(
            'aws:ses/receiptRule:ReceiptRule',
            __name__,
            __props__,
            __opts__)


    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

