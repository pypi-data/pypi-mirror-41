# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import pulumi
import pulumi.runtime
from .. import utilities, tables

class DefaultVpcDhcpOptions(pulumi.CustomResource):
    domain_name: pulumi.Output[str]
    domain_name_servers: pulumi.Output[str]
    netbios_name_servers: pulumi.Output[list]
    """
    List of NETBIOS name servers.
    """
    netbios_node_type: pulumi.Output[str]
    """
    The NetBIOS node type (1, 2, 4, or 8). AWS recommends to specify 2 since broadcast and multicast are not supported in their network. For more information about these node types, see [RFC 2132](http://www.ietf.org/rfc/rfc2132.txt).
    """
    ntp_servers: pulumi.Output[str]
    owner_id: pulumi.Output[str]
    """
    The ID of the AWS account that owns the DHCP options set.
    """
    tags: pulumi.Output[dict]
    """
    A mapping of tags to assign to the resource.
    """
    def __init__(__self__, __name__, __opts__=None, netbios_name_servers=None, netbios_node_type=None, tags=None):
        """
        Provides a resource to manage the [default AWS DHCP Options Set](http://docs.aws.amazon.com/AmazonVPC/latest/UserGuide/VPC_DHCP_Options.html#AmazonDNS)
        in the current region.
        
        Each AWS region comes with a default set of DHCP options.
        **This is an advanced resource**, and has special caveats to be aware of when
        using it. Please read this document in its entirety before using this resource.
        
        The `aws_default_vpc_dhcp_options` behaves differently from normal resources, in that
        Terraform does not _create_ this resource, but instead "adopts" it
        into management.
        
        
        :param str __name__: The name of the resource.
        :param pulumi.ResourceOptions __opts__: Options for the resource.
        :param pulumi.Input[list] netbios_name_servers: List of NETBIOS name servers.
        :param pulumi.Input[str] netbios_node_type: The NetBIOS node type (1, 2, 4, or 8). AWS recommends to specify 2 since broadcast and multicast are not supported in their network. For more information about these node types, see [RFC 2132](http://www.ietf.org/rfc/rfc2132.txt).
        :param pulumi.Input[dict] tags: A mapping of tags to assign to the resource.
        """
        if not __name__:
            raise TypeError('Missing resource name argument (for URN creation)')
        if not isinstance(__name__, str):
            raise TypeError('Expected resource name to be a string')
        if __opts__ and not isinstance(__opts__, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')

        __props__ = dict()

        __props__['netbios_name_servers'] = netbios_name_servers

        __props__['netbios_node_type'] = netbios_node_type

        __props__['tags'] = tags

        __props__['domain_name'] = None
        __props__['domain_name_servers'] = None
        __props__['ntp_servers'] = None
        __props__['owner_id'] = None

        super(DefaultVpcDhcpOptions, __self__).__init__(
            'aws:ec2/defaultVpcDhcpOptions:DefaultVpcDhcpOptions',
            __name__,
            __props__,
            __opts__)


    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

