# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import pulumi
import pulumi.runtime
from .. import utilities, tables

class HostedPrivateVirtualInterface(pulumi.CustomResource):
    address_family: pulumi.Output[str]
    """
    The address family for the BGP peer. `ipv4 ` or `ipv6`.
    """
    amazon_address: pulumi.Output[str]
    """
    The IPv4 CIDR address to use to send traffic to Amazon. Required for IPv4 BGP peers.
    """
    arn: pulumi.Output[str]
    """
    The ARN of the virtual interface.
    """
    bgp_asn: pulumi.Output[int]
    """
    The autonomous system (AS) number for Border Gateway Protocol (BGP) configuration.
    """
    bgp_auth_key: pulumi.Output[str]
    """
    The authentication key for BGP configuration.
    """
    connection_id: pulumi.Output[str]
    """
    The ID of the Direct Connect connection (or LAG) on which to create the virtual interface.
    """
    customer_address: pulumi.Output[str]
    """
    The IPv4 CIDR destination address to which Amazon should send traffic. Required for IPv4 BGP peers.
    """
    jumbo_frame_capable: pulumi.Output[bool]
    """
    Indicates whether jumbo frames (9001 MTU) are supported.
    """
    mtu: pulumi.Output[int]
    """
    The maximum transmission unit (MTU) is the size, in bytes, of the largest permissible packet that can be passed over the connection. The MTU of a virtual private interface can be either `1500` or `9001` (jumbo frames). Default is `1500`.
    """
    name: pulumi.Output[str]
    """
    The name for the virtual interface.
    """
    owner_account_id: pulumi.Output[str]
    """
    The AWS account that will own the new virtual interface.
    """
    vlan: pulumi.Output[int]
    """
    The VLAN ID.
    """
    def __init__(__self__, __name__, __opts__=None, address_family=None, amazon_address=None, bgp_asn=None, bgp_auth_key=None, connection_id=None, customer_address=None, mtu=None, name=None, owner_account_id=None, vlan=None):
        """
        Provides a Direct Connect hosted private virtual interface resource. This resource represents the allocator's side of the hosted virtual interface.
        A hosted virtual interface is a virtual interface that is owned by another AWS account.
        
        
        :param str __name__: The name of the resource.
        :param pulumi.ResourceOptions __opts__: Options for the resource.
        :param pulumi.Input[str] address_family: The address family for the BGP peer. `ipv4 ` or `ipv6`.
        :param pulumi.Input[str] amazon_address: The IPv4 CIDR address to use to send traffic to Amazon. Required for IPv4 BGP peers.
        :param pulumi.Input[int] bgp_asn: The autonomous system (AS) number for Border Gateway Protocol (BGP) configuration.
        :param pulumi.Input[str] bgp_auth_key: The authentication key for BGP configuration.
        :param pulumi.Input[str] connection_id: The ID of the Direct Connect connection (or LAG) on which to create the virtual interface.
        :param pulumi.Input[str] customer_address: The IPv4 CIDR destination address to which Amazon should send traffic. Required for IPv4 BGP peers.
        :param pulumi.Input[int] mtu: The maximum transmission unit (MTU) is the size, in bytes, of the largest permissible packet that can be passed over the connection. The MTU of a virtual private interface can be either `1500` or `9001` (jumbo frames). Default is `1500`.
        :param pulumi.Input[str] name: The name for the virtual interface.
        :param pulumi.Input[str] owner_account_id: The AWS account that will own the new virtual interface.
        :param pulumi.Input[int] vlan: The VLAN ID.
        """
        if not __name__:
            raise TypeError('Missing resource name argument (for URN creation)')
        if not isinstance(__name__, str):
            raise TypeError('Expected resource name to be a string')
        if __opts__ and not isinstance(__opts__, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')

        __props__ = dict()

        if not address_family:
            raise TypeError('Missing required property address_family')
        __props__['address_family'] = address_family

        __props__['amazon_address'] = amazon_address

        if not bgp_asn:
            raise TypeError('Missing required property bgp_asn')
        __props__['bgp_asn'] = bgp_asn

        __props__['bgp_auth_key'] = bgp_auth_key

        if not connection_id:
            raise TypeError('Missing required property connection_id')
        __props__['connection_id'] = connection_id

        __props__['customer_address'] = customer_address

        __props__['mtu'] = mtu

        __props__['name'] = name

        if not owner_account_id:
            raise TypeError('Missing required property owner_account_id')
        __props__['owner_account_id'] = owner_account_id

        if not vlan:
            raise TypeError('Missing required property vlan')
        __props__['vlan'] = vlan

        __props__['arn'] = None
        __props__['jumbo_frame_capable'] = None

        super(HostedPrivateVirtualInterface, __self__).__init__(
            'aws:directconnect/hostedPrivateVirtualInterface:HostedPrivateVirtualInterface',
            __name__,
            __props__,
            __opts__)


    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

