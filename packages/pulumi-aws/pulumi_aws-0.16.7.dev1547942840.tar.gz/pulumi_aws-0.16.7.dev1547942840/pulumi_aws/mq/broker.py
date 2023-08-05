# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import pulumi
import pulumi.runtime
from .. import utilities, tables

class Broker(pulumi.CustomResource):
    apply_immediately: pulumi.Output[bool]
    """
    Specifies whether any broker modifications
    are applied immediately, or during the next maintenance window. Default is `false`.
    """
    arn: pulumi.Output[str]
    """
    The ARN of the broker.
    """
    auto_minor_version_upgrade: pulumi.Output[bool]
    """
    Enables automatic upgrades to new minor versions for brokers, as Apache releases the versions.
    """
    broker_name: pulumi.Output[str]
    """
    The name of the broker.
    """
    configuration: pulumi.Output[dict]
    """
    Configuration of the broker. See below.
    """
    deployment_mode: pulumi.Output[str]
    """
    The deployment mode of the broker. Supported: `SINGLE_INSTANCE` and `ACTIVE_STANDBY_MULTI_AZ`. Defaults to `SINGLE_INSTANCE`.
    """
    engine_type: pulumi.Output[str]
    """
    The type of broker engine. Currently, Amazon MQ supports only `ActiveMQ`.
    """
    engine_version: pulumi.Output[str]
    """
    The version of the broker engine. Currently, Amazon MQ supports only `5.15.0` or `5.15.6`.
    """
    host_instance_type: pulumi.Output[str]
    """
    The broker's instance type. e.g. `mq.t2.micro` or `mq.m4.large`
    """
    instances: pulumi.Output[list]
    """
    A list of information about allocated brokers (both active & standby).
    * `instances.0.console_url` - The URL of the broker's [ActiveMQ Web Console](http://activemq.apache.org/web-console.html).
    * `instances.0.ip_address` - The IP Address of the broker.
    * `instances.0.endpoints` - The broker's wire-level protocol endpoints in the following order & format referenceable e.g. as `instances.0.endpoints.0` (SSL):
    * `ssl://broker-id.mq.us-west-2.amazonaws.com:61617`
    * `amqp+ssl://broker-id.mq.us-west-2.amazonaws.com:5671`
    * `stomp+ssl://broker-id.mq.us-west-2.amazonaws.com:61614`
    * `mqtt+ssl://broker-id.mq.us-west-2.amazonaws.com:8883`
    * `wss://broker-id.mq.us-west-2.amazonaws.com:61619`
    """
    logs: pulumi.Output[dict]
    """
    Logging configuration of the broker. See below.
    """
    maintenance_window_start_time: pulumi.Output[dict]
    """
    Maintenance window start time. See below.
    """
    publicly_accessible: pulumi.Output[bool]
    """
    Whether to enable connections from applications outside of the VPC that hosts the broker's subnets.
    """
    security_groups: pulumi.Output[list]
    """
    The list of security group IDs assigned to the broker.
    """
    subnet_ids: pulumi.Output[list]
    """
    The list of subnet IDs in which to launch the broker. A `SINGLE_INSTANCE` deployment requires one subnet. An `ACTIVE_STANDBY_MULTI_AZ` deployment requires two subnets.
    """
    users: pulumi.Output[list]
    """
    The list of all ActiveMQ usernames for the specified broker. See below.
    """
    def __init__(__self__, __name__, __opts__=None, apply_immediately=None, auto_minor_version_upgrade=None, broker_name=None, configuration=None, deployment_mode=None, engine_type=None, engine_version=None, host_instance_type=None, logs=None, maintenance_window_start_time=None, publicly_accessible=None, security_groups=None, subnet_ids=None, users=None):
        """
        Provides an MQ Broker Resource. This resources also manages users for the broker.
        
        For more information on Amazon MQ, see [Amazon MQ documentation](https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/welcome.html).
        
        Changes to an MQ Broker can occur when you change a
        parameter, such as `configuration` or `user`, and are reflected in the next maintenance
        window. Because of this, Terraform may report a difference in its planning
        phase because a modification has not yet taken place. You can use the
        `apply_immediately` flag to instruct the service to apply the change immediately
        (see documentation below).
        
        > **Note:** using `apply_immediately` can result in a
        brief downtime as the broker reboots.
        
        > **Note:** All arguments including the username and password will be stored in the raw state as plain-text.
        [Read more about sensitive data in state](https://www.terraform.io/docs/state/sensitive-data.html).
        
        
        :param str __name__: The name of the resource.
        :param pulumi.ResourceOptions __opts__: Options for the resource.
        :param pulumi.Input[bool] apply_immediately: Specifies whether any broker modifications
               are applied immediately, or during the next maintenance window. Default is `false`.
        :param pulumi.Input[bool] auto_minor_version_upgrade: Enables automatic upgrades to new minor versions for brokers, as Apache releases the versions.
        :param pulumi.Input[str] broker_name: The name of the broker.
        :param pulumi.Input[dict] configuration: Configuration of the broker. See below.
        :param pulumi.Input[str] deployment_mode: The deployment mode of the broker. Supported: `SINGLE_INSTANCE` and `ACTIVE_STANDBY_MULTI_AZ`. Defaults to `SINGLE_INSTANCE`.
        :param pulumi.Input[str] engine_type: The type of broker engine. Currently, Amazon MQ supports only `ActiveMQ`.
        :param pulumi.Input[str] engine_version: The version of the broker engine. Currently, Amazon MQ supports only `5.15.0` or `5.15.6`.
        :param pulumi.Input[str] host_instance_type: The broker's instance type. e.g. `mq.t2.micro` or `mq.m4.large`
        :param pulumi.Input[dict] logs: Logging configuration of the broker. See below.
        :param pulumi.Input[dict] maintenance_window_start_time: Maintenance window start time. See below.
        :param pulumi.Input[bool] publicly_accessible: Whether to enable connections from applications outside of the VPC that hosts the broker's subnets.
        :param pulumi.Input[list] security_groups: The list of security group IDs assigned to the broker.
        :param pulumi.Input[list] subnet_ids: The list of subnet IDs in which to launch the broker. A `SINGLE_INSTANCE` deployment requires one subnet. An `ACTIVE_STANDBY_MULTI_AZ` deployment requires two subnets.
        :param pulumi.Input[list] users: The list of all ActiveMQ usernames for the specified broker. See below.
        """
        if not __name__:
            raise TypeError('Missing resource name argument (for URN creation)')
        if not isinstance(__name__, str):
            raise TypeError('Expected resource name to be a string')
        if __opts__ and not isinstance(__opts__, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')

        __props__ = dict()

        __props__['apply_immediately'] = apply_immediately

        __props__['auto_minor_version_upgrade'] = auto_minor_version_upgrade

        if not broker_name:
            raise TypeError('Missing required property broker_name')
        __props__['broker_name'] = broker_name

        __props__['configuration'] = configuration

        __props__['deployment_mode'] = deployment_mode

        if not engine_type:
            raise TypeError('Missing required property engine_type')
        __props__['engine_type'] = engine_type

        if not engine_version:
            raise TypeError('Missing required property engine_version')
        __props__['engine_version'] = engine_version

        if not host_instance_type:
            raise TypeError('Missing required property host_instance_type')
        __props__['host_instance_type'] = host_instance_type

        __props__['logs'] = logs

        __props__['maintenance_window_start_time'] = maintenance_window_start_time

        __props__['publicly_accessible'] = publicly_accessible

        if not security_groups:
            raise TypeError('Missing required property security_groups')
        __props__['security_groups'] = security_groups

        __props__['subnet_ids'] = subnet_ids

        if not users:
            raise TypeError('Missing required property users')
        __props__['users'] = users

        __props__['arn'] = None
        __props__['instances'] = None

        super(Broker, __self__).__init__(
            'aws:mq/broker:Broker',
            __name__,
            __props__,
            __opts__)


    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

