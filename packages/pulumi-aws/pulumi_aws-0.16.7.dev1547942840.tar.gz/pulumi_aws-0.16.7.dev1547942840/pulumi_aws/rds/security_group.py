# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import pulumi
import pulumi.runtime
from .. import utilities, tables

class SecurityGroup(pulumi.CustomResource):
    arn: pulumi.Output[str]
    """
    The arn of the DB security group.
    """
    description: pulumi.Output[str]
    """
    The description of the DB security group. Defaults to "Managed by Terraform".
    """
    ingress: pulumi.Output[list]
    """
    A list of ingress rules.
    """
    name: pulumi.Output[str]
    """
    The name of the DB security group.
    """
    tags: pulumi.Output[dict]
    """
    A mapping of tags to assign to the resource.
    """
    def __init__(__self__, __name__, __opts__=None, description=None, ingress=None, name=None, tags=None):
        """
        Provides an RDS security group resource. This is only for DB instances in the
        EC2-Classic Platform. For instances inside a VPC, use the
        [`aws_db_instance.vpc_security_group_ids`](https://www.terraform.io/docs/providers/aws/r/db_instance.html#vpc_security_group_ids)
        attribute instead.
        
        
        :param str __name__: The name of the resource.
        :param pulumi.ResourceOptions __opts__: Options for the resource.
        :param pulumi.Input[str] description: The description of the DB security group. Defaults to "Managed by Terraform".
        :param pulumi.Input[list] ingress: A list of ingress rules.
        :param pulumi.Input[str] name: The name of the DB security group.
        :param pulumi.Input[dict] tags: A mapping of tags to assign to the resource.
        """
        if not __name__:
            raise TypeError('Missing resource name argument (for URN creation)')
        if not isinstance(__name__, str):
            raise TypeError('Expected resource name to be a string')
        if __opts__ and not isinstance(__opts__, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')

        __props__ = dict()

        if not description:
            description = 'Managed by Pulumi'
        __props__['description'] = description

        if not ingress:
            raise TypeError('Missing required property ingress')
        __props__['ingress'] = ingress

        __props__['name'] = name

        __props__['tags'] = tags

        __props__['arn'] = None

        super(SecurityGroup, __self__).__init__(
            'aws:rds/securityGroup:SecurityGroup',
            __name__,
            __props__,
            __opts__)


    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

