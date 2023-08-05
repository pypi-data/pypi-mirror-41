# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import pulumi
import pulumi.runtime
from .. import utilities, tables

class RouterRoute(pulumi.CustomResource):
    destination_cidr: pulumi.Output[str]
    """
    CIDR block to match on the packet’s destination IP. Changing
    this creates a new routing entry.
    """
    next_hop: pulumi.Output[str]
    """
    IP address of the next hop gateway.  Changing
    this creates a new routing entry.
    """
    region: pulumi.Output[str]
    """
    The region in which to obtain the V2 networking client.
    A networking client is needed to configure a routing entry on a router. If omitted, the
    `region` argument of the provider is used. Changing this creates a new
    routing entry.
    """
    router_id: pulumi.Output[str]
    """
    ID of the router this routing entry belongs to. Changing
    this creates a new routing entry.
    """
    def __init__(__self__, __name__, __opts__=None, destination_cidr=None, next_hop=None, region=None, router_id=None):
        """
        Creates a routing entry on a OpenStack V2 router.
        
        
        :param str __name__: The name of the resource.
        :param pulumi.ResourceOptions __opts__: Options for the resource.
        :param pulumi.Input[str] destination_cidr: CIDR block to match on the packet’s destination IP. Changing
               this creates a new routing entry.
        :param pulumi.Input[str] next_hop: IP address of the next hop gateway.  Changing
               this creates a new routing entry.
        :param pulumi.Input[str] region: The region in which to obtain the V2 networking client.
               A networking client is needed to configure a routing entry on a router. If omitted, the
               `region` argument of the provider is used. Changing this creates a new
               routing entry.
        :param pulumi.Input[str] router_id: ID of the router this routing entry belongs to. Changing
               this creates a new routing entry.
        """
        if not __name__:
            raise TypeError('Missing resource name argument (for URN creation)')
        if not isinstance(__name__, str):
            raise TypeError('Expected resource name to be a string')
        if __opts__ and not isinstance(__opts__, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')

        __props__ = dict()

        if not destination_cidr:
            raise TypeError('Missing required property destination_cidr')
        __props__['destination_cidr'] = destination_cidr

        if not next_hop:
            raise TypeError('Missing required property next_hop')
        __props__['next_hop'] = next_hop

        __props__['region'] = region

        if not router_id:
            raise TypeError('Missing required property router_id')
        __props__['router_id'] = router_id

        super(RouterRoute, __self__).__init__(
            'openstack:networking/routerRoute:RouterRoute',
            __name__,
            __props__,
            __opts__)


    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

