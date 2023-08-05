# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import pulumi
import pulumi.runtime
from .. import utilities, tables

class GetFolderResult(object):
    """
    A collection of values returned by getFolder.
    """
    def __init__(__self__, create_time=None, display_name=None, lifecycle_state=None, name=None, organization=None, parent=None, id=None):
        if create_time and not isinstance(create_time, str):
            raise TypeError('Expected argument create_time to be a str')
        __self__.create_time = create_time
        """
        Timestamp when the Organization was created. A timestamp in RFC3339 UTC "Zulu" format, accurate to nanoseconds. Example: "2014-10-02T15:01:23.045123456Z".
        """
        if display_name and not isinstance(display_name, str):
            raise TypeError('Expected argument display_name to be a str')
        __self__.display_name = display_name
        """
        The folder's display name.
        """
        if lifecycle_state and not isinstance(lifecycle_state, str):
            raise TypeError('Expected argument lifecycle_state to be a str')
        __self__.lifecycle_state = lifecycle_state
        """
        The Folder's current lifecycle state.
        """
        if name and not isinstance(name, str):
            raise TypeError('Expected argument name to be a str')
        __self__.name = name
        """
        The resource name of the Folder in the form `folders/{organization_id}`.
        """
        if organization and not isinstance(organization, str):
            raise TypeError('Expected argument organization to be a str')
        __self__.organization = organization
        """
        If `lookup_organization` is enable, the resource name of the Organization that the folder belongs.
        """
        if parent and not isinstance(parent, str):
            raise TypeError('Expected argument parent to be a str')
        __self__.parent = parent
        """
        The resource name of the parent Folder or Organization.
        """
        if id and not isinstance(id, str):
            raise TypeError('Expected argument id to be a str')
        __self__.id = id
        """
        id is the provider-assigned unique ID for this managed resource.
        """

async def get_folder(folder=None, lookup_organization=None):
    """
    Use this data source to get information about a Google Cloud Folder.
    
    ```hcl
    # Get folder by id
    data "google_folder" "my_folder_1" {
      folder = "folders/12345"
      lookup_organization = true
    }
    
    # Search by fields
    data "google_folder" "my_folder_2" {
      folder = "folders/23456"
    }
    
    output "my_folder_1_organization" {
      value = "${data.google_folder.my_folder_1.organization}"
    }
    
    output "my_folder_2_parent" {
      value = "${data.google_folder.my_folder_2.parent}"
    }
    
    ```
    """
    __args__ = dict()

    __args__['folder'] = folder
    __args__['lookupOrganization'] = lookup_organization
    __ret__ = await pulumi.runtime.invoke('gcp:organizations/getFolder:getFolder', __args__)

    return GetFolderResult(
        create_time=__ret__.get('createTime'),
        display_name=__ret__.get('displayName'),
        lifecycle_state=__ret__.get('lifecycleState'),
        name=__ret__.get('name'),
        organization=__ret__.get('organization'),
        parent=__ret__.get('parent'),
        id=__ret__.get('id'))
