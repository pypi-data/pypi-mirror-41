# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import pulumi
import pulumi.runtime
from .. import utilities, tables

class Instance(pulumi.CustomResource):
    configuration_id: pulumi.Output[str]
    """
    Configuration ID to be attached to the instance. Database instance
    will be rebooted when configuration is detached.
    """
    databases: pulumi.Output[list]
    """
    An array of database name, charset and collate. The database
    object structure is documented below.
    """
    datastore: pulumi.Output[dict]
    """
    An array of database engine type and version. The datastore
    object structure is documented below. Changing this creates a new instance.
    """
    flavor_id: pulumi.Output[str]
    """
    The flavor ID of the desired flavor for the instance.
    Changing this creates new instance.
    """
    name: pulumi.Output[str]
    """
    A unique name for the resource.
    """
    networks: pulumi.Output[list]
    """
    An array of one or more networks to attach to the
    instance. The network object structure is documented below. Changing this
    creates a new instance.
    """
    region: pulumi.Output[str]
    """
    The region in which to create the db instance. Changing this
    creates a new instance.
    """
    size: pulumi.Output[int]
    """
    Specifies the volume size in GB. Changing this creates new instance.
    """
    users: pulumi.Output[list]
    """
    An array of username, password, host and databases. The user
    object structure is documented below.
    """
    def __init__(__self__, __name__, __opts__=None, configuration_id=None, databases=None, datastore=None, flavor_id=None, name=None, networks=None, region=None, size=None, users=None):
        """
        Manages a V1 DB instance resource within OpenStack.
        
        
        :param str __name__: The name of the resource.
        :param pulumi.ResourceOptions __opts__: Options for the resource.
        :param pulumi.Input[str] configuration_id: Configuration ID to be attached to the instance. Database instance
               will be rebooted when configuration is detached.
        :param pulumi.Input[list] databases: An array of database name, charset and collate. The database
               object structure is documented below.
        :param pulumi.Input[dict] datastore: An array of database engine type and version. The datastore
               object structure is documented below. Changing this creates a new instance.
        :param pulumi.Input[str] flavor_id: The flavor ID of the desired flavor for the instance.
               Changing this creates new instance.
        :param pulumi.Input[str] name: A unique name for the resource.
        :param pulumi.Input[list] networks: An array of one or more networks to attach to the
               instance. The network object structure is documented below. Changing this
               creates a new instance.
        :param pulumi.Input[str] region: The region in which to create the db instance. Changing this
               creates a new instance.
        :param pulumi.Input[int] size: Specifies the volume size in GB. Changing this creates new instance.
        :param pulumi.Input[list] users: An array of username, password, host and databases. The user
               object structure is documented below.
        """
        if not __name__:
            raise TypeError('Missing resource name argument (for URN creation)')
        if not isinstance(__name__, str):
            raise TypeError('Expected resource name to be a string')
        if __opts__ and not isinstance(__opts__, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')

        __props__ = dict()

        __props__['configuration_id'] = configuration_id

        __props__['databases'] = databases

        if not datastore:
            raise TypeError('Missing required property datastore')
        __props__['datastore'] = datastore

        __props__['flavor_id'] = flavor_id

        __props__['name'] = name

        __props__['networks'] = networks

        if not region:
            raise TypeError('Missing required property region')
        __props__['region'] = region

        if not size:
            raise TypeError('Missing required property size')
        __props__['size'] = size

        __props__['users'] = users

        super(Instance, __self__).__init__(
            'openstack:database/instance:Instance',
            __name__,
            __props__,
            __opts__)


    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

