# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import pulumi
import pulumi.runtime
from .. import utilities, tables

class ApiKey(pulumi.CustomResource):
    api_key: pulumi.Output[str]
    """
    The API Key secret (Sensitive).
    """
    application_insights_id: pulumi.Output[str]
    """
    The ID of the Application Insights component on which the API key operates. Changing this forces a new resource to be created.
    """
    name: pulumi.Output[str]
    """
    Specifies the name of the Application Insights API key. Changing this forces a
    new resource to be created.
    """
    read_permissions: pulumi.Output[list]
    """
    Specifies the list of read permissions granted to the API key. Valid values are `agentconfig`, `aggregate`, `api`, `draft`, `extendqueries`, `search`. Please note these values are case sensitive. Changing this forces a new resource to be created. 
    """
    write_permissions: pulumi.Output[list]
    """
    Specifies the list of write permissions granted to the API key. Valid values are `annotations`. Please note these values are case sensitive. Changing this forces a new resource to be created.
    """
    def __init__(__self__, __name__, __opts__=None, application_insights_id=None, name=None, read_permissions=None, write_permissions=None):
        """
        Manages an Application Insights API key.
        
        
        :param str __name__: The name of the resource.
        :param pulumi.ResourceOptions __opts__: Options for the resource.
        :param pulumi.Input[str] application_insights_id: The ID of the Application Insights component on which the API key operates. Changing this forces a new resource to be created.
        :param pulumi.Input[str] name: Specifies the name of the Application Insights API key. Changing this forces a
               new resource to be created.
        :param pulumi.Input[list] read_permissions: Specifies the list of read permissions granted to the API key. Valid values are `agentconfig`, `aggregate`, `api`, `draft`, `extendqueries`, `search`. Please note these values are case sensitive. Changing this forces a new resource to be created. 
        :param pulumi.Input[list] write_permissions: Specifies the list of write permissions granted to the API key. Valid values are `annotations`. Please note these values are case sensitive. Changing this forces a new resource to be created.
        """
        if not __name__:
            raise TypeError('Missing resource name argument (for URN creation)')
        if not isinstance(__name__, str):
            raise TypeError('Expected resource name to be a string')
        if __opts__ and not isinstance(__opts__, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')

        __props__ = dict()

        if not application_insights_id:
            raise TypeError('Missing required property application_insights_id')
        __props__['application_insights_id'] = application_insights_id

        __props__['name'] = name

        __props__['read_permissions'] = read_permissions

        __props__['write_permissions'] = write_permissions

        __props__['api_key'] = None

        super(ApiKey, __self__).__init__(
            'azure:appinsights/apiKey:ApiKey',
            __name__,
            __props__,
            __opts__)


    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

