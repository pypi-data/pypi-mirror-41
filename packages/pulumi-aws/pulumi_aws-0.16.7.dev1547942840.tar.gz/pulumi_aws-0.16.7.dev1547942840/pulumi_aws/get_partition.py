# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import pulumi
import pulumi.runtime
from . import utilities, tables

class GetPartitionResult(object):
    """
    A collection of values returned by getPartition.
    """
    def __init__(__self__, partition=None, id=None):
        if partition and not isinstance(partition, str):
            raise TypeError('Expected argument partition to be a str')
        __self__.partition = partition
        if id and not isinstance(id, str):
            raise TypeError('Expected argument id to be a str')
        __self__.id = id
        """
        id is the provider-assigned unique ID for this managed resource.
        """

async def get_partition():
    """
    Use this data source to lookup current AWS partition in which Terraform is working
    """
    __args__ = dict()

    __ret__ = await pulumi.runtime.invoke('aws:index/getPartition:getPartition', __args__)

    return GetPartitionResult(
        partition=__ret__.get('partition'),
        id=__ret__.get('id'))
