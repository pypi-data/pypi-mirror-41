# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import pulumi
import pulumi.runtime
from .. import utilities, tables

class Member(pulumi.CustomResource):
    account_id: pulumi.Output[str]
    """
    AWS account ID for member account.
    """
    detector_id: pulumi.Output[str]
    """
    The detector ID of the GuardDuty account where you want to create member accounts.
    """
    disable_email_notification: pulumi.Output[bool]
    """
    Boolean whether an email notification is sent to the accounts. Defaults to `false`.
    """
    email: pulumi.Output[str]
    """
    Email address for member account.
    """
    invitation_message: pulumi.Output[str]
    """
    Message for invitation.
    """
    invite: pulumi.Output[bool]
    """
    Boolean whether to invite the account to GuardDuty as a member. Defaults to `false`. To detect if an invitation needs to be (re-)sent, the Terraform state value is `true` based on a `relationship_status` of `Disabled`, `Enabled`, `Invited`, or `EmailVerificationInProgress`.
    """
    relationship_status: pulumi.Output[str]
    """
    The status of the relationship between the member account and its master account. More information can be found in [Amazon GuardDuty API Reference](https://docs.aws.amazon.com/guardduty/latest/ug/get-members.html).
    """
    def __init__(__self__, __name__, __opts__=None, account_id=None, detector_id=None, disable_email_notification=None, email=None, invitation_message=None, invite=None):
        """
        Provides a resource to manage a GuardDuty member.
        
        > **NOTE:** Currently after using this resource, you must manually accept member account invitations before GuardDuty will begin sending cross-account events. More information for how to accomplish this via the AWS Console or API can be found in the [GuardDuty User Guide](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_accounts.html). Terraform implementation of the member acceptance resource can be tracked in [Github](https://github.com/terraform-providers/terraform-provider-aws/issues/2489).
        
        
        :param str __name__: The name of the resource.
        :param pulumi.ResourceOptions __opts__: Options for the resource.
        :param pulumi.Input[str] account_id: AWS account ID for member account.
        :param pulumi.Input[str] detector_id: The detector ID of the GuardDuty account where you want to create member accounts.
        :param pulumi.Input[bool] disable_email_notification: Boolean whether an email notification is sent to the accounts. Defaults to `false`.
        :param pulumi.Input[str] email: Email address for member account.
        :param pulumi.Input[str] invitation_message: Message for invitation.
        :param pulumi.Input[bool] invite: Boolean whether to invite the account to GuardDuty as a member. Defaults to `false`. To detect if an invitation needs to be (re-)sent, the Terraform state value is `true` based on a `relationship_status` of `Disabled`, `Enabled`, `Invited`, or `EmailVerificationInProgress`.
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

        if not detector_id:
            raise TypeError('Missing required property detector_id')
        __props__['detector_id'] = detector_id

        __props__['disable_email_notification'] = disable_email_notification

        if not email:
            raise TypeError('Missing required property email')
        __props__['email'] = email

        __props__['invitation_message'] = invitation_message

        __props__['invite'] = invite

        __props__['relationship_status'] = None

        super(Member, __self__).__init__(
            'aws:guardduty/member:Member',
            __name__,
            __props__,
            __opts__)


    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

