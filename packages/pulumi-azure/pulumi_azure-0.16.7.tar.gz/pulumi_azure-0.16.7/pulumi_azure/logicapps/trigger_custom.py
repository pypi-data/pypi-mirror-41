# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import pulumi
import pulumi.runtime
from .. import utilities, tables

class TriggerCustom(pulumi.CustomResource):
    body: pulumi.Output[str]
    """
    Specifies the JSON Blob defining the Body of this Custom Trigger.
    """
    logic_app_id: pulumi.Output[str]
    """
    Specifies the ID of the Logic App Workflow. Changing this forces a new resource to be created.
    """
    name: pulumi.Output[str]
    """
    Specifies the name of the HTTP Trigger to be created within the Logic App Workflow. Changing this forces a new resource to be created.
    """
    def __init__(__self__, __name__, __opts__=None, body=None, logic_app_id=None, name=None):
        """
        Manages a Custom Trigger within a Logic App Workflow
        
        
        :param str __name__: The name of the resource.
        :param pulumi.ResourceOptions __opts__: Options for the resource.
        :param pulumi.Input[str] body: Specifies the JSON Blob defining the Body of this Custom Trigger.
        :param pulumi.Input[str] logic_app_id: Specifies the ID of the Logic App Workflow. Changing this forces a new resource to be created.
        :param pulumi.Input[str] name: Specifies the name of the HTTP Trigger to be created within the Logic App Workflow. Changing this forces a new resource to be created.
        """
        if not __name__:
            raise TypeError('Missing resource name argument (for URN creation)')
        if not isinstance(__name__, str):
            raise TypeError('Expected resource name to be a string')
        if __opts__ and not isinstance(__opts__, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')

        __props__ = dict()

        if not body:
            raise TypeError('Missing required property body')
        __props__['body'] = body

        if not logic_app_id:
            raise TypeError('Missing required property logic_app_id')
        __props__['logic_app_id'] = logic_app_id

        __props__['name'] = name

        super(TriggerCustom, __self__).__init__(
            'azure:logicapps/triggerCustom:TriggerCustom',
            __name__,
            __props__,
            __opts__)


    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

