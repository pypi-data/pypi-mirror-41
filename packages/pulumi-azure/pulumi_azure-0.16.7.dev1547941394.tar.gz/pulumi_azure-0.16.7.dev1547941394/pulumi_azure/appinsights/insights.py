# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import pulumi
import pulumi.runtime
from .. import utilities, tables

class Insights(pulumi.CustomResource):
    app_id: pulumi.Output[str]
    """
    The App ID associated with this Application Insights component.
    """
    application_type: pulumi.Output[str]
    """
    Specifies the type of Application Insights to create. Valid values are `Java`, `iOS`, `MobileCenter`, `Other`, `Phone`, `Store`, `Web` and `Node.JS`.
    """
    instrumentation_key: pulumi.Output[str]
    """
    The Instrumentation Key for this Application Insights component.
    """
    location: pulumi.Output[str]
    """
    Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.
    """
    name: pulumi.Output[str]
    """
    Specifies the name of the Application Insights component. Changing this forces a
    new resource to be created.
    """
    resource_group_name: pulumi.Output[str]
    """
    The name of the resource group in which to
    create the Application Insights component.
    """
    tags: pulumi.Output[dict]
    """
    A mapping of tags to assign to the resource.
    """
    def __init__(__self__, __name__, __opts__=None, application_type=None, location=None, name=None, resource_group_name=None, tags=None):
        """
        Manage an Application Insights component.
        
        
        :param str __name__: The name of the resource.
        :param pulumi.ResourceOptions __opts__: Options for the resource.
        :param pulumi.Input[str] application_type: Specifies the type of Application Insights to create. Valid values are `Java`, `iOS`, `MobileCenter`, `Other`, `Phone`, `Store`, `Web` and `Node.JS`.
        :param pulumi.Input[str] location: Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.
        :param pulumi.Input[str] name: Specifies the name of the Application Insights component. Changing this forces a
               new resource to be created.
        :param pulumi.Input[str] resource_group_name: The name of the resource group in which to
               create the Application Insights component.
        :param pulumi.Input[dict] tags: A mapping of tags to assign to the resource.
        """
        if not __name__:
            raise TypeError('Missing resource name argument (for URN creation)')
        if not isinstance(__name__, str):
            raise TypeError('Expected resource name to be a string')
        if __opts__ and not isinstance(__opts__, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')

        __props__ = dict()

        if not application_type:
            raise TypeError('Missing required property application_type')
        __props__['application_type'] = application_type

        if not location:
            raise TypeError('Missing required property location')
        __props__['location'] = location

        __props__['name'] = name

        if not resource_group_name:
            raise TypeError('Missing required property resource_group_name')
        __props__['resource_group_name'] = resource_group_name

        __props__['tags'] = tags

        __props__['app_id'] = None
        __props__['instrumentation_key'] = None

        super(Insights, __self__).__init__(
            'azure:appinsights/insights:Insights',
            __name__,
            __props__,
            __opts__)


    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

