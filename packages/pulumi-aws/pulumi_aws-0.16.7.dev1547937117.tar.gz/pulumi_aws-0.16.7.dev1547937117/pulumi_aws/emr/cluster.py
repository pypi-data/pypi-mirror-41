# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import pulumi
import pulumi.runtime
from .. import utilities, tables

class Cluster(pulumi.CustomResource):
    additional_info: pulumi.Output[str]
    """
    A JSON string for selecting additional features such as adding proxy information. Note: Currently there is no API to retrieve the value of this argument after EMR cluster creation from provider, therefore Terraform cannot detect drift from the actual EMR cluster if its value is changed outside Terraform.
    """
    applications: pulumi.Output[list]
    """
    A list of applications for the cluster. Valid values are: `Flink`, `Hadoop`, `Hive`, `Mahout`, `Pig`, `Spark`, and `JupyterHub` (as of EMR 5.14.0). Case insensitive
    """
    autoscaling_role: pulumi.Output[str]
    """
    An IAM role for automatic scaling policies. The IAM role provides permissions that the automatic scaling feature requires to launch and terminate EC2 instances in an instance group.
    """
    bootstrap_actions: pulumi.Output[list]
    """
    List of bootstrap actions that will be run before Hadoop is started on the cluster nodes. Defined below
    """
    cluster_state: pulumi.Output[str]
    configurations: pulumi.Output[str]
    """
    List of configurations supplied for the EMR cluster you are creating
    """
    configurations_json: pulumi.Output[str]
    """
    A JSON string for supplying list of configurations for the EMR cluster.
    """
    core_instance_count: pulumi.Output[int]
    """
    Number of Amazon EC2 instances used to execute the job flow. EMR will use one node as the cluster's master node and use the remainder of the nodes (`core_instance_count`-1) as core nodes. Cannot be specified if `instance_groups` is set. Default `1`
    """
    core_instance_type: pulumi.Output[str]
    """
    The EC2 instance type of the slave nodes. Cannot be specified if `instance_groups` is set
    """
    custom_ami_id: pulumi.Output[str]
    """
    A custom Amazon Linux AMI for the cluster (instead of an EMR-owned AMI). Available in Amazon EMR version 5.7.0 and later.
    """
    ebs_root_volume_size: pulumi.Output[int]
    """
    Size in GiB of the EBS root device volume of the Linux AMI that is used for each EC2 instance. Available in Amazon EMR version 4.x and later.
    """
    ec2_attributes: pulumi.Output[dict]
    """
    Attributes for the EC2 instances running the job flow. Defined below
    """
    instance_groups: pulumi.Output[list]
    """
    A list of `instance_group` objects for each instance group in the cluster. Exactly one of `master_instance_type` and `instance_group` must be specified. If `instance_group` is set, then it must contain a configuration block for at least the `MASTER` instance group type (as well as any additional instance groups). Defined below
    """
    keep_job_flow_alive_when_no_steps: pulumi.Output[bool]
    """
    Switch on/off run cluster with no steps or when all steps are complete (default is on)
    """
    kerberos_attributes: pulumi.Output[dict]
    """
    Kerberos configuration for the cluster. Defined below
    """
    log_uri: pulumi.Output[str]
    """
    S3 bucket to write the log files of the job flow. If a value is not provided, logs are not created
    """
    master_instance_type: pulumi.Output[str]
    """
    The EC2 instance type of the master node. Exactly one of `master_instance_type` and `instance_group` must be specified.
    """
    master_public_dns: pulumi.Output[str]
    """
    The public DNS name of the master EC2 instance.
    """
    name: pulumi.Output[str]
    """
    The name of the job flow
    """
    release_label: pulumi.Output[str]
    """
    The release label for the Amazon EMR release
    """
    scale_down_behavior: pulumi.Output[str]
    """
    The way that individual Amazon EC2 instances terminate when an automatic scale-in activity occurs or an `instance group` is resized.
    """
    security_configuration: pulumi.Output[str]
    """
    The security configuration name to attach to the EMR cluster. Only valid for EMR clusters with `release_label` 4.8.0 or greater
    """
    service_role: pulumi.Output[str]
    """
    IAM role that will be assumed by the Amazon EMR service to access AWS resources
    """
    steps: pulumi.Output[list]
    """
    List of steps to run when creating the cluster. Defined below. It is highly recommended to utilize the [lifecycle configuration block](https://www.terraform.io/docs/configuration/resources.html) with `ignore_changes` if other steps are being managed outside of Terraform.
    """
    tags: pulumi.Output[dict]
    """
    list of tags to apply to the EMR Cluster
    """
    termination_protection: pulumi.Output[bool]
    """
    Switch on/off termination protection (default is off)
    """
    visible_to_all_users: pulumi.Output[bool]
    """
    Whether the job flow is visible to all IAM users of the AWS account associated with the job flow. Default `true`
    """
    def __init__(__self__, __name__, __opts__=None, additional_info=None, applications=None, autoscaling_role=None, bootstrap_actions=None, configurations=None, configurations_json=None, core_instance_count=None, core_instance_type=None, custom_ami_id=None, ebs_root_volume_size=None, ec2_attributes=None, instance_groups=None, keep_job_flow_alive_when_no_steps=None, kerberos_attributes=None, log_uri=None, master_instance_type=None, name=None, release_label=None, scale_down_behavior=None, security_configuration=None, service_role=None, steps=None, tags=None, termination_protection=None, visible_to_all_users=None):
        """
        Provides an Elastic MapReduce Cluster, a web service that makes it easy to
        process large amounts of data efficiently. See [Amazon Elastic MapReduce Documentation](https://aws.amazon.com/documentation/elastic-mapreduce/)
        for more information.
        
        
        :param str __name__: The name of the resource.
        :param pulumi.ResourceOptions __opts__: Options for the resource.
        :param pulumi.Input[str] additional_info: A JSON string for selecting additional features such as adding proxy information. Note: Currently there is no API to retrieve the value of this argument after EMR cluster creation from provider, therefore Terraform cannot detect drift from the actual EMR cluster if its value is changed outside Terraform.
        :param pulumi.Input[list] applications: A list of applications for the cluster. Valid values are: `Flink`, `Hadoop`, `Hive`, `Mahout`, `Pig`, `Spark`, and `JupyterHub` (as of EMR 5.14.0). Case insensitive
        :param pulumi.Input[str] autoscaling_role: An IAM role for automatic scaling policies. The IAM role provides permissions that the automatic scaling feature requires to launch and terminate EC2 instances in an instance group.
        :param pulumi.Input[list] bootstrap_actions: List of bootstrap actions that will be run before Hadoop is started on the cluster nodes. Defined below
        :param pulumi.Input[str] configurations: List of configurations supplied for the EMR cluster you are creating
        :param pulumi.Input[str] configurations_json: A JSON string for supplying list of configurations for the EMR cluster.
        :param pulumi.Input[int] core_instance_count: Number of Amazon EC2 instances used to execute the job flow. EMR will use one node as the cluster's master node and use the remainder of the nodes (`core_instance_count`-1) as core nodes. Cannot be specified if `instance_groups` is set. Default `1`
        :param pulumi.Input[str] core_instance_type: The EC2 instance type of the slave nodes. Cannot be specified if `instance_groups` is set
        :param pulumi.Input[str] custom_ami_id: A custom Amazon Linux AMI for the cluster (instead of an EMR-owned AMI). Available in Amazon EMR version 5.7.0 and later.
        :param pulumi.Input[int] ebs_root_volume_size: Size in GiB of the EBS root device volume of the Linux AMI that is used for each EC2 instance. Available in Amazon EMR version 4.x and later.
        :param pulumi.Input[dict] ec2_attributes: Attributes for the EC2 instances running the job flow. Defined below
        :param pulumi.Input[list] instance_groups: A list of `instance_group` objects for each instance group in the cluster. Exactly one of `master_instance_type` and `instance_group` must be specified. If `instance_group` is set, then it must contain a configuration block for at least the `MASTER` instance group type (as well as any additional instance groups). Defined below
        :param pulumi.Input[bool] keep_job_flow_alive_when_no_steps: Switch on/off run cluster with no steps or when all steps are complete (default is on)
        :param pulumi.Input[dict] kerberos_attributes: Kerberos configuration for the cluster. Defined below
        :param pulumi.Input[str] log_uri: S3 bucket to write the log files of the job flow. If a value is not provided, logs are not created
        :param pulumi.Input[str] master_instance_type: The EC2 instance type of the master node. Exactly one of `master_instance_type` and `instance_group` must be specified.
        :param pulumi.Input[str] name: The name of the job flow
        :param pulumi.Input[str] release_label: The release label for the Amazon EMR release
        :param pulumi.Input[str] scale_down_behavior: The way that individual Amazon EC2 instances terminate when an automatic scale-in activity occurs or an `instance group` is resized.
        :param pulumi.Input[str] security_configuration: The security configuration name to attach to the EMR cluster. Only valid for EMR clusters with `release_label` 4.8.0 or greater
        :param pulumi.Input[str] service_role: IAM role that will be assumed by the Amazon EMR service to access AWS resources
        :param pulumi.Input[list] steps: List of steps to run when creating the cluster. Defined below. It is highly recommended to utilize the [lifecycle configuration block](https://www.terraform.io/docs/configuration/resources.html) with `ignore_changes` if other steps are being managed outside of Terraform.
        :param pulumi.Input[dict] tags: list of tags to apply to the EMR Cluster
        :param pulumi.Input[bool] termination_protection: Switch on/off termination protection (default is off)
        :param pulumi.Input[bool] visible_to_all_users: Whether the job flow is visible to all IAM users of the AWS account associated with the job flow. Default `true`
        """
        if not __name__:
            raise TypeError('Missing resource name argument (for URN creation)')
        if not isinstance(__name__, str):
            raise TypeError('Expected resource name to be a string')
        if __opts__ and not isinstance(__opts__, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')

        __props__ = dict()

        __props__['additional_info'] = additional_info

        __props__['applications'] = applications

        __props__['autoscaling_role'] = autoscaling_role

        __props__['bootstrap_actions'] = bootstrap_actions

        __props__['configurations'] = configurations

        __props__['configurations_json'] = configurations_json

        __props__['core_instance_count'] = core_instance_count

        __props__['core_instance_type'] = core_instance_type

        __props__['custom_ami_id'] = custom_ami_id

        __props__['ebs_root_volume_size'] = ebs_root_volume_size

        __props__['ec2_attributes'] = ec2_attributes

        __props__['instance_groups'] = instance_groups

        __props__['keep_job_flow_alive_when_no_steps'] = keep_job_flow_alive_when_no_steps

        __props__['kerberos_attributes'] = kerberos_attributes

        __props__['log_uri'] = log_uri

        __props__['master_instance_type'] = master_instance_type

        __props__['name'] = name

        if not release_label:
            raise TypeError('Missing required property release_label')
        __props__['release_label'] = release_label

        __props__['scale_down_behavior'] = scale_down_behavior

        __props__['security_configuration'] = security_configuration

        if not service_role:
            raise TypeError('Missing required property service_role')
        __props__['service_role'] = service_role

        __props__['steps'] = steps

        __props__['tags'] = tags

        __props__['termination_protection'] = termination_protection

        __props__['visible_to_all_users'] = visible_to_all_users

        __props__['cluster_state'] = None
        __props__['master_public_dns'] = None

        super(Cluster, __self__).__init__(
            'aws:emr/cluster:Cluster',
            __name__,
            __props__,
            __opts__)


    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

