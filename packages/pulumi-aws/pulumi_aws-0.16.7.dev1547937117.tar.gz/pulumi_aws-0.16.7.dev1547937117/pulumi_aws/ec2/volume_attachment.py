# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import pulumi
import pulumi.runtime
from .. import utilities, tables

class VolumeAttachment(pulumi.CustomResource):
    device_name: pulumi.Output[str]
    """
    The device name to expose to the instance (for
    example, `/dev/sdh` or `xvdh`)
    """
    force_detach: pulumi.Output[bool]
    """
    Set to `true` if you want to force the
    volume to detach. Useful if previous attempts failed, but use this option only
    as a last resort, as this can result in **data loss**. See
    [Detaching an Amazon EBS Volume from an Instance][1] for more information.
    """
    instance_id: pulumi.Output[str]
    """
    ID of the Instance to attach to
    """
    skip_destroy: pulumi.Output[bool]
    """
    Set this to true if you do not wish
    to detach the volume from the instance to which it is attached at destroy
    time, and instead just remove the attachment from Terraform state. This is
    useful when destroying an instance which has volumes created by some other
    means attached.
    """
    volume_id: pulumi.Output[str]
    """
    ID of the Volume to be attached
    """
    def __init__(__self__, __name__, __opts__=None, device_name=None, force_detach=None, instance_id=None, skip_destroy=None, volume_id=None):
        """
        Provides an AWS EBS Volume Attachment as a top level resource, to attach and
        detach volumes from AWS Instances.
        
        > **NOTE on EBS block devices:** If you use `ebs_block_device` on an `aws_instance`, Terraform will assume management over the full set of non-root EBS block devices for the instance, and treats additional block devices as drift. For this reason, `ebs_block_device` cannot be mixed with external `aws_ebs_volume` + `aws_ebs_volume_attachment` resources for a given instance.
        
        
        :param str __name__: The name of the resource.
        :param pulumi.ResourceOptions __opts__: Options for the resource.
        :param pulumi.Input[str] device_name: The device name to expose to the instance (for
               example, `/dev/sdh` or `xvdh`)
        :param pulumi.Input[bool] force_detach: Set to `true` if you want to force the
               volume to detach. Useful if previous attempts failed, but use this option only
               as a last resort, as this can result in **data loss**. See
               [Detaching an Amazon EBS Volume from an Instance][1] for more information.
        :param pulumi.Input[str] instance_id: ID of the Instance to attach to
        :param pulumi.Input[bool] skip_destroy: Set this to true if you do not wish
               to detach the volume from the instance to which it is attached at destroy
               time, and instead just remove the attachment from Terraform state. This is
               useful when destroying an instance which has volumes created by some other
               means attached.
        :param pulumi.Input[str] volume_id: ID of the Volume to be attached
        """
        if not __name__:
            raise TypeError('Missing resource name argument (for URN creation)')
        if not isinstance(__name__, str):
            raise TypeError('Expected resource name to be a string')
        if __opts__ and not isinstance(__opts__, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')

        __props__ = dict()

        if not device_name:
            raise TypeError('Missing required property device_name')
        __props__['device_name'] = device_name

        __props__['force_detach'] = force_detach

        if not instance_id:
            raise TypeError('Missing required property instance_id')
        __props__['instance_id'] = instance_id

        __props__['skip_destroy'] = skip_destroy

        if not volume_id:
            raise TypeError('Missing required property volume_id')
        __props__['volume_id'] = volume_id

        super(VolumeAttachment, __self__).__init__(
            'aws:ec2/volumeAttachment:VolumeAttachment',
            __name__,
            __props__,
            __opts__)


    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

