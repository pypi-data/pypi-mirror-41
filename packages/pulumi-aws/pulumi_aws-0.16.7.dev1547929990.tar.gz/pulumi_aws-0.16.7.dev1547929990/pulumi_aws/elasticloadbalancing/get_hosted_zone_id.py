# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import pulumi
import pulumi.runtime
from .. import utilities, tables

class GetHostedZoneIdResult(object):
    """
    A collection of values returned by getHostedZoneId.
    """
    def __init__(__self__, id=None):
        if id and not isinstance(id, str):
            raise TypeError('Expected argument id to be a str')
        __self__.id = id
        """
        id is the provider-assigned unique ID for this managed resource.
        """

async def get_hosted_zone_id(region=None):
    """
    Use this data source to get the HostedZoneId of the AWS Elastic Load Balancing HostedZoneId
    in a given region for the purpose of using in an AWS Route53 Alias.
    """
    __args__ = dict()

    __args__['region'] = region
    __ret__ = await pulumi.runtime.invoke('aws:elasticloadbalancing/getHostedZoneId:getHostedZoneId', __args__)

    return GetHostedZoneIdResult(
        id=__ret__.get('id'))
