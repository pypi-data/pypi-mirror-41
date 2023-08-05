# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import pulumi
import pulumi.runtime
from .. import utilities, tables

class LogProfile(pulumi.CustomResource):
    categories: pulumi.Output[list]
    """
    List of categories of the logs.
    """
    locations: pulumi.Output[list]
    """
    List of regions for which Activity Log events are stored or streamed.
    """
    name: pulumi.Output[str]
    """
    The name of the Log Profile. Changing this forces a
    new resource to be created.
    """
    retention_policy: pulumi.Output[dict]
    """
    A `retention_policy` block as documented below. A retention policy for how long Activity Logs are retained in the storage account.
    """
    servicebus_rule_id: pulumi.Output[str]
    """
    The service bus (or event hub) rule ID of the service bus (or event hub) namespace in which the Activity Log is streamed to. At least one of `storage_account_id` or `servicebus_rule_id` must be set.
    """
    storage_account_id: pulumi.Output[str]
    """
    The resource ID of the storage account in which the Activity Log is stored. At least one of `storage_account_id` or `servicebus_rule_id` must be set.
    """
    def __init__(__self__, __name__, __opts__=None, categories=None, locations=None, name=None, retention_policy=None, servicebus_rule_id=None, storage_account_id=None):
        """
        Manages a [Log Profile](https://docs.microsoft.com/en-us/azure/monitoring-and-diagnostics/monitoring-overview-activity-logs#export-the-activity-log-with-a-log-profile). A Log Profile configures how Activity Logs are exported.
        
        -> **NOTE:** It's only possible to configure one Log Profile per Subscription. If you are trying to create more than one Log Profile, an error with `StatusCode=409` will occur.
        
        
        :param str __name__: The name of the resource.
        :param pulumi.ResourceOptions __opts__: Options for the resource.
        :param pulumi.Input[list] categories: List of categories of the logs.
        :param pulumi.Input[list] locations: List of regions for which Activity Log events are stored or streamed.
        :param pulumi.Input[str] name: The name of the Log Profile. Changing this forces a
               new resource to be created.
        :param pulumi.Input[dict] retention_policy: A `retention_policy` block as documented below. A retention policy for how long Activity Logs are retained in the storage account.
        :param pulumi.Input[str] servicebus_rule_id: The service bus (or event hub) rule ID of the service bus (or event hub) namespace in which the Activity Log is streamed to. At least one of `storage_account_id` or `servicebus_rule_id` must be set.
        :param pulumi.Input[str] storage_account_id: The resource ID of the storage account in which the Activity Log is stored. At least one of `storage_account_id` or `servicebus_rule_id` must be set.
        """
        if not __name__:
            raise TypeError('Missing resource name argument (for URN creation)')
        if not isinstance(__name__, str):
            raise TypeError('Expected resource name to be a string')
        if __opts__ and not isinstance(__opts__, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')

        __props__ = dict()

        if not categories:
            raise TypeError('Missing required property categories')
        __props__['categories'] = categories

        if not locations:
            raise TypeError('Missing required property locations')
        __props__['locations'] = locations

        __props__['name'] = name

        if not retention_policy:
            raise TypeError('Missing required property retention_policy')
        __props__['retention_policy'] = retention_policy

        __props__['servicebus_rule_id'] = servicebus_rule_id

        __props__['storage_account_id'] = storage_account_id

        super(LogProfile, __self__).__init__(
            'azure:monitoring/logProfile:LogProfile',
            __name__,
            __props__,
            __opts__)


    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

