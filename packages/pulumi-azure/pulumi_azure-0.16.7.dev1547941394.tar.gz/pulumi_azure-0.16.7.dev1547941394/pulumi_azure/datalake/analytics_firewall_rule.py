# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import pulumi
import pulumi.runtime
from .. import utilities, tables

class AnalyticsFirewallRule(pulumi.CustomResource):
    account_name: pulumi.Output[str]
    """
    Specifies the name of the Data Lake Analytics for which the Firewall Rule should take effect.
    """
    end_ip_address: pulumi.Output[str]
    """
    The End IP Address for the firewall rule.
    """
    name: pulumi.Output[str]
    """
    Specifies the name of the Data Lake Analytics. Changing this forces a new resource to be created. Has to be between 3 to 24 characters.
    """
    resource_group_name: pulumi.Output[str]
    """
    The name of the resource group in which to create the Data Lake Analytics.
    """
    start_ip_address: pulumi.Output[str]
    """
    The Start IP address for the firewall rule.
    """
    def __init__(__self__, __name__, __opts__=None, account_name=None, end_ip_address=None, name=None, resource_group_name=None, start_ip_address=None):
        """
        Manage a Azure Data Lake Analytics Firewall Rule.
        
        
        :param str __name__: The name of the resource.
        :param pulumi.ResourceOptions __opts__: Options for the resource.
        :param pulumi.Input[str] account_name: Specifies the name of the Data Lake Analytics for which the Firewall Rule should take effect.
        :param pulumi.Input[str] end_ip_address: The End IP Address for the firewall rule.
        :param pulumi.Input[str] name: Specifies the name of the Data Lake Analytics. Changing this forces a new resource to be created. Has to be between 3 to 24 characters.
        :param pulumi.Input[str] resource_group_name: The name of the resource group in which to create the Data Lake Analytics.
        :param pulumi.Input[str] start_ip_address: The Start IP address for the firewall rule.
        """
        if not __name__:
            raise TypeError('Missing resource name argument (for URN creation)')
        if not isinstance(__name__, str):
            raise TypeError('Expected resource name to be a string')
        if __opts__ and not isinstance(__opts__, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')

        __props__ = dict()

        if not account_name:
            raise TypeError('Missing required property account_name')
        __props__['account_name'] = account_name

        if not end_ip_address:
            raise TypeError('Missing required property end_ip_address')
        __props__['end_ip_address'] = end_ip_address

        __props__['name'] = name

        if not resource_group_name:
            raise TypeError('Missing required property resource_group_name')
        __props__['resource_group_name'] = resource_group_name

        if not start_ip_address:
            raise TypeError('Missing required property start_ip_address')
        __props__['start_ip_address'] = start_ip_address

        super(AnalyticsFirewallRule, __self__).__init__(
            'azure:datalake/analyticsFirewallRule:AnalyticsFirewallRule',
            __name__,
            __props__,
            __opts__)


    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

