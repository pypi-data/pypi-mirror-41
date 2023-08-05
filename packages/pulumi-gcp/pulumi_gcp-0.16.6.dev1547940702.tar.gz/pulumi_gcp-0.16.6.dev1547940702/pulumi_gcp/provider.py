# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import pulumi
import pulumi.runtime
from . import utilities, tables

class Provider(pulumi.ProviderResource):
    def __init__(__self__, __name__, __opts__=None, credentials=None, project=None, region=None, zone=None):
        """
        The provider type for the google package. By default, resources use package-wide configuration
        settings, however an explicit `Provider` instance may be created and passed during resource
        construction to achieve fine-grained programmatic control over provider settings. See the
        [documentation](https://pulumi.io/reference/programming-model.html#providers) for more information.
        
        :param str __name__: The name of the resource.
        :param pulumi.ResourceOptions __opts__: Options for the resource.
        :param pulumi.Input[str] credentials
        :param pulumi.Input[str] project
        :param pulumi.Input[str] region
        :param pulumi.Input[str] zone
        """
        if not __name__:
            raise TypeError('Missing resource name argument (for URN creation)')
        if not isinstance(__name__, str):
            raise TypeError('Expected resource name to be a string')
        if __opts__ and not isinstance(__opts__, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')

        __props__ = dict()

        if not credentials:
            credentials = utilities.get_env('GOOGLE_CREDENTIALS', 'GOOGLE_CLOUD_KEYFILE_JSON', 'GCLOUD_KEYFILE_JSON')
        __props__['credentials'] = credentials

        if not project:
            project = utilities.get_env('GOOGLE_PROJECT', 'GOOGLE_CLOUD_PROJECT', 'GCLOUD_PROJECT', 'CLOUDSDK_CORE_PROJECT')
        __props__['project'] = project

        if not region:
            region = utilities.get_env('GOOGLE_REGION', 'GCLOUD_REGION', 'CLOUDSDK_COMPUTE_REGION')
        __props__['region'] = region

        if not zone:
            zone = utilities.get_env('GOOGLE_ZONE', 'GCLOUD_ZONE', 'CLOUDSDK_COMPUTE_ZONE')
        __props__['zone'] = zone

        super(Provider, __self__).__init__(
            'gcp',
            __name__,
            __props__,
            __opts__)


    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

