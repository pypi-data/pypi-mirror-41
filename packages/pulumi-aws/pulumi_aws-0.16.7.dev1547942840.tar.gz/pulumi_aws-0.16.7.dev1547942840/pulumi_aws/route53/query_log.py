# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import pulumi
import pulumi.runtime
from .. import utilities, tables

class QueryLog(pulumi.CustomResource):
    cloudwatch_log_group_arn: pulumi.Output[str]
    """
    CloudWatch log group ARN to send query logs.
    """
    zone_id: pulumi.Output[str]
    """
    Route53 hosted zone ID to enable query logs.
    """
    def __init__(__self__, __name__, __opts__=None, cloudwatch_log_group_arn=None, zone_id=None):
        """
        Provides a Route53 query logging configuration resource.
        
        > **NOTE:** There are restrictions on the configuration of query logging. Notably,
        the CloudWatch log group must be in the `us-east-1` region,
        a permissive CloudWatch log resource policy must be in place, and
        the Route53 hosted zone must be public.
        See [Configuring Logging for DNS Queries](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/query-logs.html?console_help=true#query-logs-configuring) for additional details.
        
        
        :param str __name__: The name of the resource.
        :param pulumi.ResourceOptions __opts__: Options for the resource.
        :param pulumi.Input[str] cloudwatch_log_group_arn: CloudWatch log group ARN to send query logs.
        :param pulumi.Input[str] zone_id: Route53 hosted zone ID to enable query logs.
        """
        if not __name__:
            raise TypeError('Missing resource name argument (for URN creation)')
        if not isinstance(__name__, str):
            raise TypeError('Expected resource name to be a string')
        if __opts__ and not isinstance(__opts__, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')

        __props__ = dict()

        if not cloudwatch_log_group_arn:
            raise TypeError('Missing required property cloudwatch_log_group_arn')
        __props__['cloudwatch_log_group_arn'] = cloudwatch_log_group_arn

        if not zone_id:
            raise TypeError('Missing required property zone_id')
        __props__['zone_id'] = zone_id

        super(QueryLog, __self__).__init__(
            'aws:route53/queryLog:QueryLog',
            __name__,
            __props__,
            __opts__)


    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

