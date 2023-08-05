# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import pulumi
import pulumi.runtime
from .. import utilities, tables

class AccountPublicAccessBlock(pulumi.CustomResource):
    account_id: pulumi.Output[str]
    """
    AWS account ID to configure. Defaults to automatically determined account ID of the Terraform AWS provider.
    """
    block_public_acls: pulumi.Output[bool]
    """
    Whether Amazon S3 should block public ACLs for buckets in this account. Defaults to `false`. Enabling this setting does not affect existing policies or ACLs. When set to `true` causes the following behavior:
    * PUT Bucket acl and PUT Object acl calls will fail if the specified ACL allows public access.
    * PUT Object calls will fail if the request includes an object ACL.
    """
    block_public_policy: pulumi.Output[bool]
    """
    Whether Amazon S3 should block public bucket policies for buckets in this account. Defaults to `false`. Enabling this setting does not affect existing bucket policies. When set to `true` causes Amazon S3 to:
    * Reject calls to PUT Bucket policy if the specified bucket policy allows public access.
    """
    ignore_public_acls: pulumi.Output[bool]
    """
    Whether Amazon S3 should ignore public ACLs for buckets in this account. Defaults to `false`. Enabling this setting does not affect the persistence of any existing ACLs and doesn't prevent new public ACLs from being set. When set to `true` causes Amazon S3 to:
    * Ignore all public ACLs on buckets in this account and any objects that they contain.
    """
    restrict_public_buckets: pulumi.Output[bool]
    """
    Whether Amazon S3 should restrict public bucket policies for buckets in this account. Defaults to `false`. Enabling this setting does not affect previously stored bucket policies, except that public and cross-account access within any public bucket policy, including non-public delegation to specific accounts, is blocked. When set to `true`:
    * Only the bucket owner and AWS Services can access buckets with public policies.
    """
    def __init__(__self__, __name__, __opts__=None, account_id=None, block_public_acls=None, block_public_policy=None, ignore_public_acls=None, restrict_public_buckets=None):
        """
        Manages S3 account-level Public Access Block configuration. For more information about these settings, see the [AWS S3 Block Public Access documentation](https://docs.aws.amazon.com/AmazonS3/latest/dev/access-control-block-public-access.html).
        
        > **NOTE:** Each AWS account may only have one S3 Public Access Block configuration. Multiple configurations of the resource against the same AWS account will cause a perpetual difference.
        
        -> Advanced usage: To use a custom API endpoint for this Terraform resource, use the [`s3control` endpoint provider configuration](https://www.terraform.io/docs/providers/aws/index.html#s3control), not the `s3` endpoint provider configuration.
        
        
        :param str __name__: The name of the resource.
        :param pulumi.ResourceOptions __opts__: Options for the resource.
        :param pulumi.Input[str] account_id: AWS account ID to configure. Defaults to automatically determined account ID of the Terraform AWS provider.
        :param pulumi.Input[bool] block_public_acls: Whether Amazon S3 should block public ACLs for buckets in this account. Defaults to `false`. Enabling this setting does not affect existing policies or ACLs. When set to `true` causes the following behavior:
               * PUT Bucket acl and PUT Object acl calls will fail if the specified ACL allows public access.
               * PUT Object calls will fail if the request includes an object ACL.
        :param pulumi.Input[bool] block_public_policy: Whether Amazon S3 should block public bucket policies for buckets in this account. Defaults to `false`. Enabling this setting does not affect existing bucket policies. When set to `true` causes Amazon S3 to:
               * Reject calls to PUT Bucket policy if the specified bucket policy allows public access.
        :param pulumi.Input[bool] ignore_public_acls: Whether Amazon S3 should ignore public ACLs for buckets in this account. Defaults to `false`. Enabling this setting does not affect the persistence of any existing ACLs and doesn't prevent new public ACLs from being set. When set to `true` causes Amazon S3 to:
               * Ignore all public ACLs on buckets in this account and any objects that they contain.
        :param pulumi.Input[bool] restrict_public_buckets: Whether Amazon S3 should restrict public bucket policies for buckets in this account. Defaults to `false`. Enabling this setting does not affect previously stored bucket policies, except that public and cross-account access within any public bucket policy, including non-public delegation to specific accounts, is blocked. When set to `true`:
               * Only the bucket owner and AWS Services can access buckets with public policies.
        """
        if not __name__:
            raise TypeError('Missing resource name argument (for URN creation)')
        if not isinstance(__name__, str):
            raise TypeError('Expected resource name to be a string')
        if __opts__ and not isinstance(__opts__, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')

        __props__ = dict()

        __props__['account_id'] = account_id

        __props__['block_public_acls'] = block_public_acls

        __props__['block_public_policy'] = block_public_policy

        __props__['ignore_public_acls'] = ignore_public_acls

        __props__['restrict_public_buckets'] = restrict_public_buckets

        super(AccountPublicAccessBlock, __self__).__init__(
            'aws:s3/accountPublicAccessBlock:AccountPublicAccessBlock',
            __name__,
            __props__,
            __opts__)


    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

