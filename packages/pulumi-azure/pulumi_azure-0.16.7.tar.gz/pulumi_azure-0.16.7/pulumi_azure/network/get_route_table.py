# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import pulumi
import pulumi.runtime
from .. import utilities, tables

class GetRouteTableResult(object):
    """
    A collection of values returned by getRouteTable.
    """
    def __init__(__self__, location=None, routes=None, subnets=None, tags=None, id=None):
        if location and not isinstance(location, str):
            raise TypeError('Expected argument location to be a str')
        __self__.location = location
        """
        The Azure Region in which the Route Table exists.
        """
        if routes and not isinstance(routes, list):
            raise TypeError('Expected argument routes to be a list')
        __self__.routes = routes
        """
        One or more `route` blocks as documented below.
        """
        if subnets and not isinstance(subnets, list):
            raise TypeError('Expected argument subnets to be a list')
        __self__.subnets = subnets
        """
        The collection of Subnets associated with this route table.
        """
        if tags and not isinstance(tags, dict):
            raise TypeError('Expected argument tags to be a dict')
        __self__.tags = tags
        """
        A mapping of tags assigned to the Route Table.
        """
        if id and not isinstance(id, str):
            raise TypeError('Expected argument id to be a str')
        __self__.id = id
        """
        id is the provider-assigned unique ID for this managed resource.
        """

async def get_route_table(name=None, resource_group_name=None):
    """
    Use this data source to access information about an existing Route Table.
    """
    __args__ = dict()

    __args__['name'] = name
    __args__['resourceGroupName'] = resource_group_name
    __ret__ = await pulumi.runtime.invoke('azure:network/getRouteTable:getRouteTable', __args__)

    return GetRouteTableResult(
        location=__ret__.get('location'),
        routes=__ret__.get('routes'),
        subnets=__ret__.get('subnets'),
        tags=__ret__.get('tags'),
        id=__ret__.get('id'))
