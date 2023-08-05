# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import pulumi
import pulumi.runtime
from .. import utilities, tables

class GetSolutionStackResult(object):
    """
    A collection of values returned by getSolutionStack.
    """
    def __init__(__self__, name=None, id=None):
        if name and not isinstance(name, str):
            raise TypeError('Expected argument name to be a str')
        __self__.name = name
        """
        The name of the solution stack.
        """
        if id and not isinstance(id, str):
            raise TypeError('Expected argument id to be a str')
        __self__.id = id
        """
        id is the provider-assigned unique ID for this managed resource.
        """

async def get_solution_stack(most_recent=None, name_regex=None):
    """
    Use this data source to get the name of a elastic beanstalk solution stack.
    """
    __args__ = dict()

    __args__['mostRecent'] = most_recent
    __args__['nameRegex'] = name_regex
    __ret__ = await pulumi.runtime.invoke('aws:elasticbeanstalk/getSolutionStack:getSolutionStack', __args__)

    return GetSolutionStackResult(
        name=__ret__.get('name'),
        id=__ret__.get('id'))
