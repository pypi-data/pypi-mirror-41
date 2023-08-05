# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import pulumi
import pulumi.runtime
from .. import utilities, tables

class SslNegotiationPolicy(pulumi.CustomResource):
    attributes: pulumi.Output[list]
    """
    An SSL Negotiation policy attribute. Each has two properties:
    """
    lb_port: pulumi.Output[int]
    """
    The load balancer port to which the policy
    should be applied. This must be an active listener on the load
    balancer.
    """
    load_balancer: pulumi.Output[str]
    """
    The load balancer to which the policy
    should be attached.
    """
    name: pulumi.Output[str]
    """
    The name of the attribute
    """
    def __init__(__self__, __name__, __opts__=None, attributes=None, lb_port=None, load_balancer=None, name=None):
        """
        Provides a load balancer SSL negotiation policy, which allows an ELB to control the ciphers and protocols that are supported during SSL negotiations between a client and a load balancer.
        
        
        :param str __name__: The name of the resource.
        :param pulumi.ResourceOptions __opts__: Options for the resource.
        :param pulumi.Input[list] attributes: An SSL Negotiation policy attribute. Each has two properties:
        :param pulumi.Input[int] lb_port: The load balancer port to which the policy
               should be applied. This must be an active listener on the load
               balancer.
        :param pulumi.Input[str] load_balancer: The load balancer to which the policy
               should be attached.
        :param pulumi.Input[str] name: The name of the attribute
        """
        if not __name__:
            raise TypeError('Missing resource name argument (for URN creation)')
        if not isinstance(__name__, str):
            raise TypeError('Expected resource name to be a string')
        if __opts__ and not isinstance(__opts__, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')

        __props__ = dict()

        __props__['attributes'] = attributes

        if not lb_port:
            raise TypeError('Missing required property lb_port')
        __props__['lb_port'] = lb_port

        if not load_balancer:
            raise TypeError('Missing required property load_balancer')
        __props__['load_balancer'] = load_balancer

        __props__['name'] = name

        super(SslNegotiationPolicy, __self__).__init__(
            'aws:elasticloadbalancing/sslNegotiationPolicy:SslNegotiationPolicy',
            __name__,
            __props__,
            __opts__)


    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

