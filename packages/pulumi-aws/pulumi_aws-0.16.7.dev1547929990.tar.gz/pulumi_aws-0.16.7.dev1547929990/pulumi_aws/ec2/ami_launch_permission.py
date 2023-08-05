# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import pulumi
import pulumi.runtime
from .. import utilities, tables

class AmiLaunchPermission(pulumi.CustomResource):
    account_id: pulumi.Output[str]
    """
    An AWS Account ID to add launch permissions.
    """
    image_id: pulumi.Output[str]
    """
    A region-unique name for the AMI.
    """
    def __init__(__self__, __name__, __opts__=None, account_id=None, image_id=None):
        """
        Adds launch permission to Amazon Machine Image (AMI) from another AWS account.
        
        
        :param str __name__: The name of the resource.
        :param pulumi.ResourceOptions __opts__: Options for the resource.
        :param pulumi.Input[str] account_id: An AWS Account ID to add launch permissions.
        :param pulumi.Input[str] image_id: A region-unique name for the AMI.
        """
        if not __name__:
            raise TypeError('Missing resource name argument (for URN creation)')
        if not isinstance(__name__, str):
            raise TypeError('Expected resource name to be a string')
        if __opts__ and not isinstance(__opts__, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')

        __props__ = dict()

        if not account_id:
            raise TypeError('Missing required property account_id')
        __props__['account_id'] = account_id

        if not image_id:
            raise TypeError('Missing required property image_id')
        __props__['image_id'] = image_id

        super(AmiLaunchPermission, __self__).__init__(
            'aws:ec2/amiLaunchPermission:AmiLaunchPermission',
            __name__,
            __props__,
            __opts__)


    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

