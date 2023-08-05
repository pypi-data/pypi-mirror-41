# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import pulumi
import pulumi.runtime
from .. import utilities, tables

class AdmChannel(pulumi.CustomResource):
    application_id: pulumi.Output[str]
    """
    The application ID.
    """
    client_id: pulumi.Output[str]
    """
    Client ID (part of OAuth Credentials) obtained via Amazon Developer Account.
    """
    client_secret: pulumi.Output[str]
    """
    Client Secret (part of OAuth Credentials) obtained via Amazon Developer Account.
    """
    enabled: pulumi.Output[bool]
    """
    Specifies whether to enable the channel. Defaults to `true`.
    """
    def __init__(__self__, __name__, __opts__=None, application_id=None, client_id=None, client_secret=None, enabled=None):
        """
        Provides a Pinpoint ADM (Amazon Device Messaging) Channel resource.
        
        > **Note:** All arguments including the Client ID and Client Secret will be stored in the raw state as plain-text.
        [Read more about sensitive data in state](https://www.terraform.io/docs/state/sensitive-data.html).
        
        
        
        :param str __name__: The name of the resource.
        :param pulumi.ResourceOptions __opts__: Options for the resource.
        :param pulumi.Input[str] application_id: The application ID.
        :param pulumi.Input[str] client_id: Client ID (part of OAuth Credentials) obtained via Amazon Developer Account.
        :param pulumi.Input[str] client_secret: Client Secret (part of OAuth Credentials) obtained via Amazon Developer Account.
        :param pulumi.Input[bool] enabled: Specifies whether to enable the channel. Defaults to `true`.
        """
        if not __name__:
            raise TypeError('Missing resource name argument (for URN creation)')
        if not isinstance(__name__, str):
            raise TypeError('Expected resource name to be a string')
        if __opts__ and not isinstance(__opts__, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')

        __props__ = dict()

        if not application_id:
            raise TypeError('Missing required property application_id')
        __props__['application_id'] = application_id

        if not client_id:
            raise TypeError('Missing required property client_id')
        __props__['client_id'] = client_id

        if not client_secret:
            raise TypeError('Missing required property client_secret')
        __props__['client_secret'] = client_secret

        __props__['enabled'] = enabled

        super(AdmChannel, __self__).__init__(
            'aws:pinpoint/admChannel:AdmChannel',
            __name__,
            __props__,
            __opts__)


    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

