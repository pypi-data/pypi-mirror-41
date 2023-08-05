# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import pulumi
import pulumi.runtime
from .. import utilities, tables

class DefaultVpc(pulumi.CustomResource):
    arn: pulumi.Output[str]
    """
    Amazon Resource Name (ARN) of VPC
    """
    assign_generated_ipv6_cidr_block: pulumi.Output[bool]
    """
    Whether or not an Amazon-provided IPv6 CIDR
    block with a /56 prefix length for the VPC was assigned
    """
    cidr_block: pulumi.Output[str]
    """
    The CIDR block of the VPC
    """
    default_network_acl_id: pulumi.Output[str]
    """
    The ID of the network ACL created by default on VPC creation
    """
    default_route_table_id: pulumi.Output[str]
    """
    The ID of the route table created by default on VPC creation
    """
    default_security_group_id: pulumi.Output[str]
    """
    The ID of the security group created by default on VPC creation
    """
    dhcp_options_id: pulumi.Output[str]
    enable_classiclink: pulumi.Output[bool]
    """
    A boolean flag to enable/disable ClassicLink
    for the VPC. Only valid in regions and accounts that support EC2 Classic.
    See the [ClassicLink documentation][1] for more information. Defaults false.
    """
    enable_classiclink_dns_support: pulumi.Output[bool]
    enable_dns_hostnames: pulumi.Output[bool]
    """
    A boolean flag to enable/disable DNS hostnames in the VPC. Defaults false.
    """
    enable_dns_support: pulumi.Output[bool]
    """
    A boolean flag to enable/disable DNS support in the VPC. Defaults true.
    """
    instance_tenancy: pulumi.Output[str]
    """
    Tenancy of instances spin up within VPC.
    """
    ipv6_association_id: pulumi.Output[str]
    """
    The association ID for the IPv6 CIDR block of the VPC
    """
    ipv6_cidr_block: pulumi.Output[str]
    """
    The IPv6 CIDR block of the VPC
    """
    main_route_table_id: pulumi.Output[str]
    """
    The ID of the main route table associated with
    this VPC. Note that you can change a VPC's main route table by using an
    [`aws_main_route_table_association`](https://www.terraform.io/docs/providers/aws/r/main_route_table_assoc.html)
    """
    owner_id: pulumi.Output[str]
    """
    The ID of the AWS account that owns the VPC.
    """
    tags: pulumi.Output[dict]
    """
    A mapping of tags to assign to the resource.
    """
    def __init__(__self__, __name__, __opts__=None, enable_classiclink=None, enable_classiclink_dns_support=None, enable_dns_hostnames=None, enable_dns_support=None, tags=None):
        """
        Provides a resource to manage the [default AWS VPC](http://docs.aws.amazon.com/AmazonVPC/latest/UserGuide/default-vpc.html)
        in the current region.
        
        For AWS accounts created after 2013-12-04, each region comes with a Default VPC.
        **This is an advanced resource**, and has special caveats to be aware of when
        using it. Please read this document in its entirety before using this resource.
        
        The `aws_default_vpc` behaves differently from normal resources, in that
        Terraform does not _create_ this resource, but instead "adopts" it
        into management.
        
        
        :param str __name__: The name of the resource.
        :param pulumi.ResourceOptions __opts__: Options for the resource.
        :param pulumi.Input[bool] enable_classiclink: A boolean flag to enable/disable ClassicLink
               for the VPC. Only valid in regions and accounts that support EC2 Classic.
               See the [ClassicLink documentation][1] for more information. Defaults false.
        :param pulumi.Input[bool] enable_classiclink_dns_support
        :param pulumi.Input[bool] enable_dns_hostnames: A boolean flag to enable/disable DNS hostnames in the VPC. Defaults false.
        :param pulumi.Input[bool] enable_dns_support: A boolean flag to enable/disable DNS support in the VPC. Defaults true.
        :param pulumi.Input[dict] tags: A mapping of tags to assign to the resource.
        """
        if not __name__:
            raise TypeError('Missing resource name argument (for URN creation)')
        if not isinstance(__name__, str):
            raise TypeError('Expected resource name to be a string')
        if __opts__ and not isinstance(__opts__, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')

        __props__ = dict()

        __props__['enable_classiclink'] = enable_classiclink

        __props__['enable_classiclink_dns_support'] = enable_classiclink_dns_support

        __props__['enable_dns_hostnames'] = enable_dns_hostnames

        __props__['enable_dns_support'] = enable_dns_support

        __props__['tags'] = tags

        __props__['arn'] = None
        __props__['assign_generated_ipv6_cidr_block'] = None
        __props__['cidr_block'] = None
        __props__['default_network_acl_id'] = None
        __props__['default_route_table_id'] = None
        __props__['default_security_group_id'] = None
        __props__['dhcp_options_id'] = None
        __props__['instance_tenancy'] = None
        __props__['ipv6_association_id'] = None
        __props__['ipv6_cidr_block'] = None
        __props__['main_route_table_id'] = None
        __props__['owner_id'] = None

        super(DefaultVpc, __self__).__init__(
            'aws:ec2/defaultVpc:DefaultVpc',
            __name__,
            __props__,
            __opts__)


    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

