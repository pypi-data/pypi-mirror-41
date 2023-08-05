# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import pulumi
import pulumi.runtime
from .. import utilities, tables

class GetRegistryResult(object):
    """
    A collection of values returned by getRegistry.
    """
    def __init__(__self__, admin_enabled=None, admin_password=None, admin_username=None, location=None, login_server=None, sku=None, storage_account_id=None, tags=None, id=None):
        if admin_enabled and not isinstance(admin_enabled, bool):
            raise TypeError('Expected argument admin_enabled to be a bool')
        __self__.admin_enabled = admin_enabled
        """
        Is the Administrator account enabled for this Container Registry.
        """
        if admin_password and not isinstance(admin_password, str):
            raise TypeError('Expected argument admin_password to be a str')
        __self__.admin_password = admin_password
        """
        The Password associated with the Container Registry Admin account - if the admin account is enabled.
        """
        if admin_username and not isinstance(admin_username, str):
            raise TypeError('Expected argument admin_username to be a str')
        __self__.admin_username = admin_username
        """
        The Username associated with the Container Registry Admin account - if the admin account is enabled.
        """
        if location and not isinstance(location, str):
            raise TypeError('Expected argument location to be a str')
        __self__.location = location
        """
        The Azure Region in which this Container Registry exists.
        """
        if login_server and not isinstance(login_server, str):
            raise TypeError('Expected argument login_server to be a str')
        __self__.login_server = login_server
        """
        The URL that can be used to log into the container registry.
        """
        if sku and not isinstance(sku, str):
            raise TypeError('Expected argument sku to be a str')
        __self__.sku = sku
        """
        The SKU of this Container Registry, such as `Basic`.
        """
        if storage_account_id and not isinstance(storage_account_id, str):
            raise TypeError('Expected argument storage_account_id to be a str')
        __self__.storage_account_id = storage_account_id
        """
        The ID of the Storage Account used for this Container Registry. This is only returned for `Classic` SKU's.
        """
        if tags and not isinstance(tags, dict):
            raise TypeError('Expected argument tags to be a dict')
        __self__.tags = tags
        """
        A map of tags assigned to the Container Registry.
        """
        if id and not isinstance(id, str):
            raise TypeError('Expected argument id to be a str')
        __self__.id = id
        """
        id is the provider-assigned unique ID for this managed resource.
        """

async def get_registry(name=None, resource_group_name=None):
    """
    Use this data source to access information about an existing Container Registry.
    """
    __args__ = dict()

    __args__['name'] = name
    __args__['resourceGroupName'] = resource_group_name
    __ret__ = await pulumi.runtime.invoke('azure:containerservice/getRegistry:getRegistry', __args__)

    return GetRegistryResult(
        admin_enabled=__ret__.get('adminEnabled'),
        admin_password=__ret__.get('adminPassword'),
        admin_username=__ret__.get('adminUsername'),
        location=__ret__.get('location'),
        login_server=__ret__.get('loginServer'),
        sku=__ret__.get('sku'),
        storage_account_id=__ret__.get('storageAccountId'),
        tags=__ret__.get('tags'),
        id=__ret__.get('id'))
