# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import pulumi
import pulumi.runtime
from .. import utilities, tables

class BucketIAMBinding(pulumi.CustomResource):
    bucket: pulumi.Output[str]
    """
    The name of the bucket it applies to.
    """
    etag: pulumi.Output[str]
    """
    (Computed) The etag of the storage bucket's IAM policy.
    """
    members: pulumi.Output[list]
    role: pulumi.Output[str]
    """
    The role that should be applied. Note that custom roles must be of the format
    `[projects|organizations]/{parent-name}/roles/{role-name}`.
    """
    def __init__(__self__, __name__, __opts__=None, bucket=None, members=None, role=None):
        """
        Three different resources help you manage your IAM policy for storage bucket. Each of these resources serves a different use case:
        
        * `google_storage_bucket_iam_binding`: Authoritative for a given role. Updates the IAM policy to grant a role to a list of members. Other roles within the IAM policy for the storage bucket are preserved.
        * `google_storage_bucket_iam_member`: Non-authoritative. Updates the IAM policy to grant a role to a new member. Other members for the role for the storage bucket are preserved.
        * `google_storage_bucket_iam_policy`: Setting a policy removes all other permissions on the bucket, and if done incorrectly, there's a real chance you will lock yourself out of the bucket. If possible for your use case, using multiple google_storage_bucket_iam_binding resources will be much safer. See the usage example on how to work with policy correctly.
        
        
        > **Note:** `google_storage_bucket_iam_binding` resources **can be** used in conjunction with `google_storage_bucket_iam_member` resources **only if** they do not grant privilege to the same role.
        
        
        :param str __name__: The name of the resource.
        :param pulumi.ResourceOptions __opts__: Options for the resource.
        :param pulumi.Input[str] bucket: The name of the bucket it applies to.
        :param pulumi.Input[list] members
        :param pulumi.Input[str] role: The role that should be applied. Note that custom roles must be of the format
               `[projects|organizations]/{parent-name}/roles/{role-name}`.
        """
        if not __name__:
            raise TypeError('Missing resource name argument (for URN creation)')
        if not isinstance(__name__, str):
            raise TypeError('Expected resource name to be a string')
        if __opts__ and not isinstance(__opts__, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')

        __props__ = dict()

        if not bucket:
            raise TypeError('Missing required property bucket')
        __props__['bucket'] = bucket

        if not members:
            raise TypeError('Missing required property members')
        __props__['members'] = members

        if not role:
            raise TypeError('Missing required property role')
        __props__['role'] = role

        __props__['etag'] = None

        super(BucketIAMBinding, __self__).__init__(
            'gcp:storage/bucketIAMBinding:BucketIAMBinding',
            __name__,
            __props__,
            __opts__)


    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

