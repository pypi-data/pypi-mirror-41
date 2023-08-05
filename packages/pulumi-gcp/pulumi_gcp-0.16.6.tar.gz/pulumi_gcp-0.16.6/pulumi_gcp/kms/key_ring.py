# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import pulumi
import pulumi.runtime
from .. import utilities, tables

class KeyRing(pulumi.CustomResource):
    location: pulumi.Output[str]
    """
    The Google Cloud Platform location for the KeyRing.
    A full list of valid locations can be found by running `gcloud kms locations list`.
    """
    name: pulumi.Output[str]
    """
    The KeyRing's name.
    A KeyRing’s name must be unique within a location and match the regular expression `[a-zA-Z0-9_-]{1,63}`
    """
    project: pulumi.Output[str]
    """
    The project in which the resource belongs. If it
    is not provided, the provider project is used.
    """
    self_link: pulumi.Output[str]
    """
    The self link of the created KeyRing. Its format is `projects/{projectId}/locations/{location}/keyRings/{keyRingName}`.
    """
    def __init__(__self__, __name__, __opts__=None, location=None, name=None, project=None):
        """
        Allows creation of a Google Cloud Platform KMS KeyRing. For more information see
        [the official documentation](https://cloud.google.com/kms/docs/object-hierarchy#keyring)
        and 
        [API](https://cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings).
        
        A KeyRing is a grouping of CryptoKeys for organizational purposes. A KeyRing belongs to a Google Cloud Platform Project
        and resides in a specific location.
        
        > Note: KeyRings cannot be deleted from Google Cloud Platform. Destroying a Terraform-managed KeyRing will remove it
        from state but **will not delete the resource on the server**.
        
        
        :param str __name__: The name of the resource.
        :param pulumi.ResourceOptions __opts__: Options for the resource.
        :param pulumi.Input[str] location: The Google Cloud Platform location for the KeyRing.
               A full list of valid locations can be found by running `gcloud kms locations list`.
        :param pulumi.Input[str] name: The KeyRing's name.
               A KeyRing’s name must be unique within a location and match the regular expression `[a-zA-Z0-9_-]{1,63}`
        :param pulumi.Input[str] project: The project in which the resource belongs. If it
               is not provided, the provider project is used.
        """
        if not __name__:
            raise TypeError('Missing resource name argument (for URN creation)')
        if not isinstance(__name__, str):
            raise TypeError('Expected resource name to be a string')
        if __opts__ and not isinstance(__opts__, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')

        __props__ = dict()

        if not location:
            raise TypeError('Missing required property location')
        __props__['location'] = location

        __props__['name'] = name

        __props__['project'] = project

        __props__['self_link'] = None

        super(KeyRing, __self__).__init__(
            'gcp:kms/keyRing:KeyRing',
            __name__,
            __props__,
            __opts__)


    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

