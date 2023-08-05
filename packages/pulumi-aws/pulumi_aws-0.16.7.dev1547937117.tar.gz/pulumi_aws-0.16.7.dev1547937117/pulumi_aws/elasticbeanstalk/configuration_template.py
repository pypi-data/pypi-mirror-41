# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import pulumi
import pulumi.runtime
from .. import utilities, tables

class ConfigurationTemplate(pulumi.CustomResource):
    application: pulumi.Output[str]
    """
    name of the application to associate with this configuration template
    """
    description: pulumi.Output[str]
    """
    Short description of the Template
    """
    environment_id: pulumi.Output[str]
    """
    The ID of the environment used with this configuration template
    """
    name: pulumi.Output[str]
    """
    A unique name for this Template.
    """
    settings: pulumi.Output[list]
    """
    Option settings to configure the new Environment. These
    override specific values that are set as defaults. The format is detailed
    below in Option Settings
    """
    solution_stack_name: pulumi.Output[str]
    """
    A solution stack to base your Template
    off of. Example stacks can be found in the [Amazon API documentation][1]
    """
    def __init__(__self__, __name__, __opts__=None, application=None, description=None, environment_id=None, name=None, settings=None, solution_stack_name=None):
        """
        Provides an Elastic Beanstalk Configuration Template, which are associated with
        a specific application and are used to deploy different versions of the
        application with the same configuration settings.
        
        
        :param str __name__: The name of the resource.
        :param pulumi.ResourceOptions __opts__: Options for the resource.
        :param pulumi.Input[str] application: name of the application to associate with this configuration template
        :param pulumi.Input[str] description: Short description of the Template
        :param pulumi.Input[str] environment_id: The ID of the environment used with this configuration template
        :param pulumi.Input[str] name: A unique name for this Template.
        :param pulumi.Input[list] settings: Option settings to configure the new Environment. These
               override specific values that are set as defaults. The format is detailed
               below in Option Settings
        :param pulumi.Input[str] solution_stack_name: A solution stack to base your Template
               off of. Example stacks can be found in the [Amazon API documentation][1]
        """
        if not __name__:
            raise TypeError('Missing resource name argument (for URN creation)')
        if not isinstance(__name__, str):
            raise TypeError('Expected resource name to be a string')
        if __opts__ and not isinstance(__opts__, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')

        __props__ = dict()

        if not application:
            raise TypeError('Missing required property application')
        __props__['application'] = application

        __props__['description'] = description

        __props__['environment_id'] = environment_id

        __props__['name'] = name

        __props__['settings'] = settings

        __props__['solution_stack_name'] = solution_stack_name

        super(ConfigurationTemplate, __self__).__init__(
            'aws:elasticbeanstalk/configurationTemplate:ConfigurationTemplate',
            __name__,
            __props__,
            __opts__)


    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

