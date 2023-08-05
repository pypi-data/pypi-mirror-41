# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import pulumi
import pulumi.runtime
from .. import utilities, tables

class Definition(pulumi.CustomResource):
    assignable_scopes: pulumi.Output[list]
    """
    One or more assignable scopes for this Role Definition, such as `/subscriptions/0b1f6471-1bf0-4dda-aec3-111122223333`, `/subscriptions/0b1f6471-1bf0-4dda-aec3-111122223333/resourceGroups/myGroup`, or `/subscriptions/0b1f6471-1bf0-4dda-aec3-111122223333/resourceGroups/myGroup/providers/Microsoft.Compute/virtualMachines/myVM`.
    """
    description: pulumi.Output[str]
    """
    A description of the Role Definition.
    """
    name: pulumi.Output[str]
    """
    The name of the Role Definition. Changing this forces a new resource to be created.
    """
    permissions: pulumi.Output[list]
    """
    A `permissions` block as defined below.
    """
    role_definition_id: pulumi.Output[str]
    """
    A unique UUID/GUID which identifies this role - one will be generated if not specified. Changing this forces a new resource to be created.
    """
    scope: pulumi.Output[str]
    """
    The scope at which the Role Definition applies too, such as `/subscriptions/0b1f6471-1bf0-4dda-aec3-111122223333`, `/subscriptions/0b1f6471-1bf0-4dda-aec3-111122223333/resourceGroups/myGroup`, or `/subscriptions/0b1f6471-1bf0-4dda-aec3-111122223333/resourceGroups/myGroup/providers/Microsoft.Compute/virtualMachines/myVM`. Changing this forces a new resource to be created.
    """
    def __init__(__self__, __name__, __opts__=None, assignable_scopes=None, description=None, name=None, permissions=None, role_definition_id=None, scope=None):
        """
        Manages a custom Role Definition, used to assign Roles to Users/Principals. See ['Understand role definitions'](https://docs.microsoft.com/en-us/azure/role-based-access-control/role-definitions) in the Azure documentation for more details.
        
        
        :param str __name__: The name of the resource.
        :param pulumi.ResourceOptions __opts__: Options for the resource.
        :param pulumi.Input[list] assignable_scopes: One or more assignable scopes for this Role Definition, such as `/subscriptions/0b1f6471-1bf0-4dda-aec3-111122223333`, `/subscriptions/0b1f6471-1bf0-4dda-aec3-111122223333/resourceGroups/myGroup`, or `/subscriptions/0b1f6471-1bf0-4dda-aec3-111122223333/resourceGroups/myGroup/providers/Microsoft.Compute/virtualMachines/myVM`.
        :param pulumi.Input[str] description: A description of the Role Definition.
        :param pulumi.Input[str] name: The name of the Role Definition. Changing this forces a new resource to be created.
        :param pulumi.Input[list] permissions: A `permissions` block as defined below.
        :param pulumi.Input[str] role_definition_id: A unique UUID/GUID which identifies this role - one will be generated if not specified. Changing this forces a new resource to be created.
        :param pulumi.Input[str] scope: The scope at which the Role Definition applies too, such as `/subscriptions/0b1f6471-1bf0-4dda-aec3-111122223333`, `/subscriptions/0b1f6471-1bf0-4dda-aec3-111122223333/resourceGroups/myGroup`, or `/subscriptions/0b1f6471-1bf0-4dda-aec3-111122223333/resourceGroups/myGroup/providers/Microsoft.Compute/virtualMachines/myVM`. Changing this forces a new resource to be created.
        """
        if not __name__:
            raise TypeError('Missing resource name argument (for URN creation)')
        if not isinstance(__name__, str):
            raise TypeError('Expected resource name to be a string')
        if __opts__ and not isinstance(__opts__, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')

        __props__ = dict()

        if not assignable_scopes:
            raise TypeError('Missing required property assignable_scopes')
        __props__['assignable_scopes'] = assignable_scopes

        __props__['description'] = description

        __props__['name'] = name

        if not permissions:
            raise TypeError('Missing required property permissions')
        __props__['permissions'] = permissions

        __props__['role_definition_id'] = role_definition_id

        if not scope:
            raise TypeError('Missing required property scope')
        __props__['scope'] = scope

        super(Definition, __self__).__init__(
            'azure:role/definition:Definition',
            __name__,
            __props__,
            __opts__)


    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

