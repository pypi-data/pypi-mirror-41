# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import pulumi
import pulumi.runtime
from .. import utilities, tables

class GetSecretResult(object):
    """
    A collection of values returned by getSecret.
    """
    def __init__(__self__, arn=None, description=None, kms_key_id=None, name=None, policy=None, rotation_enabled=None, rotation_lambda_arn=None, rotation_rules=None, tags=None, id=None):
        if arn and not isinstance(arn, str):
            raise TypeError('Expected argument arn to be a str')
        __self__.arn = arn
        """
        The Amazon Resource Name (ARN) of the secret.
        """
        if description and not isinstance(description, str):
            raise TypeError('Expected argument description to be a str')
        __self__.description = description
        """
        A description of the secret.
        """
        if kms_key_id and not isinstance(kms_key_id, str):
            raise TypeError('Expected argument kms_key_id to be a str')
        __self__.kms_key_id = kms_key_id
        """
        The Key Management Service (KMS) Customer Master Key (CMK) associated with the secret.
        """
        if name and not isinstance(name, str):
            raise TypeError('Expected argument name to be a str')
        __self__.name = name
        if policy and not isinstance(policy, str):
            raise TypeError('Expected argument policy to be a str')
        __self__.policy = policy
        """
        The resource-based policy document that's attached to the secret.
        """
        if rotation_enabled and not isinstance(rotation_enabled, bool):
            raise TypeError('Expected argument rotation_enabled to be a bool')
        __self__.rotation_enabled = rotation_enabled
        """
        Whether rotation is enabled or not.
        """
        if rotation_lambda_arn and not isinstance(rotation_lambda_arn, str):
            raise TypeError('Expected argument rotation_lambda_arn to be a str')
        __self__.rotation_lambda_arn = rotation_lambda_arn
        """
        Rotation Lambda function Amazon Resource Name (ARN) if rotation is enabled.
        """
        if rotation_rules and not isinstance(rotation_rules, list):
            raise TypeError('Expected argument rotation_rules to be a list')
        __self__.rotation_rules = rotation_rules
        """
        Rotation rules if rotation is enabled.
        """
        if tags and not isinstance(tags, dict):
            raise TypeError('Expected argument tags to be a dict')
        __self__.tags = tags
        """
        Tags of the secret.
        """
        if id and not isinstance(id, str):
            raise TypeError('Expected argument id to be a str')
        __self__.id = id
        """
        id is the provider-assigned unique ID for this managed resource.
        """

async def get_secret(arn=None, name=None):
    """
    Retrieve metadata information about a Secrets Manager secret. To retrieve a secret value, see the [`aws_secretsmanager_secret_version` data source](https://www.terraform.io/docs/providers/aws/d/secretsmanager_secret_version.html).
    """
    __args__ = dict()

    __args__['arn'] = arn
    __args__['name'] = name
    __ret__ = await pulumi.runtime.invoke('aws:secretsmanager/getSecret:getSecret', __args__)

    return GetSecretResult(
        arn=__ret__.get('arn'),
        description=__ret__.get('description'),
        kms_key_id=__ret__.get('kmsKeyId'),
        name=__ret__.get('name'),
        policy=__ret__.get('policy'),
        rotation_enabled=__ret__.get('rotationEnabled'),
        rotation_lambda_arn=__ret__.get('rotationLambdaArn'),
        rotation_rules=__ret__.get('rotationRules'),
        tags=__ret__.get('tags'),
        id=__ret__.get('id'))
