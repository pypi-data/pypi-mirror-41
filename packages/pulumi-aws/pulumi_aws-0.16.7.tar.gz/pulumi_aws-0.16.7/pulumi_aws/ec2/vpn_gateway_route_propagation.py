# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import pulumi
import pulumi.runtime
from .. import utilities, tables

class VpnGatewayRoutePropagation(pulumi.CustomResource):
    route_table_id: pulumi.Output[str]
    """
    The id of the `aws_route_table` to propagate routes into.
    """
    vpn_gateway_id: pulumi.Output[str]
    """
    The id of the `aws_vpn_gateway` to propagate routes from.
    """
    def __init__(__self__, __name__, __opts__=None, route_table_id=None, vpn_gateway_id=None):
        """
        Requests automatic route propagation between a VPN gateway and a route table.
        
        > **Note:** This resource should not be used with a route table that has
        the `propagating_vgws` argument set. If that argument is set, any route
        propagation not explicitly listed in its value will be removed.
        
        
        :param str __name__: The name of the resource.
        :param pulumi.ResourceOptions __opts__: Options for the resource.
        :param pulumi.Input[str] route_table_id: The id of the `aws_route_table` to propagate routes into.
        :param pulumi.Input[str] vpn_gateway_id: The id of the `aws_vpn_gateway` to propagate routes from.
        """
        if not __name__:
            raise TypeError('Missing resource name argument (for URN creation)')
        if not isinstance(__name__, str):
            raise TypeError('Expected resource name to be a string')
        if __opts__ and not isinstance(__opts__, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')

        __props__ = dict()

        if not route_table_id:
            raise TypeError('Missing required property route_table_id')
        __props__['route_table_id'] = route_table_id

        if not vpn_gateway_id:
            raise TypeError('Missing required property vpn_gateway_id')
        __props__['vpn_gateway_id'] = vpn_gateway_id

        super(VpnGatewayRoutePropagation, __self__).__init__(
            'aws:ec2/vpnGatewayRoutePropagation:VpnGatewayRoutePropagation',
            __name__,
            __props__,
            __opts__)


    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

