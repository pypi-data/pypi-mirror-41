# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import pulumi
import pulumi.runtime
from .. import utilities, tables

class SSLCertificate(pulumi.CustomResource):
    certificate: pulumi.Output[str]
    certificate_id: pulumi.Output[int]
    creation_timestamp: pulumi.Output[str]
    description: pulumi.Output[str]
    name: pulumi.Output[str]
    name_prefix: pulumi.Output[str]
    """
    Creates a unique name beginning with the
    specified prefix. Conflicts with `name`.
    """
    private_key: pulumi.Output[str]
    project: pulumi.Output[str]
    """
    The ID of the project in which the resource belongs.
    If it is not provided, the provider project is used.
    """
    self_link: pulumi.Output[str]
    """
    The URI of the created resource.
    """
    def __init__(__self__, __name__, __opts__=None, certificate=None, description=None, name=None, name_prefix=None, private_key=None, project=None):
        """
        An SslCertificate resource, used for HTTPS load balancing. This resource
        provides a mechanism to upload an SSL key and certificate to
        the load balancer to serve secure connections from the user.
        
        
        To get more information about SslCertificate, see:
        
        * [API documentation](https://cloud.google.com/compute/docs/reference/rest/v1/sslCertificates)
        * How-to Guides
            * [Official Documentation](https://cloud.google.com/load-balancing/docs/ssl-certificates)
        
        <div class = "oics-button" style="float: right; margin: 0 0 -15px">
          <a href="https://console.cloud.google.com/cloudshell/open?cloudshell_git_repo=https%3A%2F%2Fgithub.com%2Fterraform-google-modules%2Fdocs-examples.git&cloudshell_working_dir=ssl_certificate_basic&cloudshell_image=gcr.io%2Fgraphite-cloud-shell-images%2Fterraform%3Alatest&open_in_editor=main.tf&cloudshell_print=.%2Fmotd&cloudshell_tutorial=.%2Ftutorial.md" target="_blank">
            <img alt="Open in Cloud Shell" src="//gstatic.com/cloudssh/images/open-btn.svg" style="max-height: 44px; margin: 32px auto; max-width: 100%;">
          </a>
        </div>
        
        :param str __name__: The name of the resource.
        :param pulumi.ResourceOptions __opts__: Options for the resource.
        :param pulumi.Input[str] certificate
        :param pulumi.Input[str] description
        :param pulumi.Input[str] name
        :param pulumi.Input[str] name_prefix: Creates a unique name beginning with the
               specified prefix. Conflicts with `name`.
        :param pulumi.Input[str] private_key
        :param pulumi.Input[str] project: The ID of the project in which the resource belongs.
               If it is not provided, the provider project is used.
        """
        if not __name__:
            raise TypeError('Missing resource name argument (for URN creation)')
        if not isinstance(__name__, str):
            raise TypeError('Expected resource name to be a string')
        if __opts__ and not isinstance(__opts__, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')

        __props__ = dict()

        if not certificate:
            raise TypeError('Missing required property certificate')
        __props__['certificate'] = certificate

        __props__['description'] = description

        __props__['name'] = name

        __props__['name_prefix'] = name_prefix

        if not private_key:
            raise TypeError('Missing required property private_key')
        __props__['private_key'] = private_key

        __props__['project'] = project

        __props__['certificate_id'] = None
        __props__['creation_timestamp'] = None
        __props__['self_link'] = None

        super(SSLCertificate, __self__).__init__(
            'gcp:compute/sSLCertificate:SSLCertificate',
            __name__,
            __props__,
            __opts__)


    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

