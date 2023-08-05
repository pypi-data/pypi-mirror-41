# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import pulumi
import pulumi.runtime
from .. import utilities, tables

__config__ = pulumi.Config('openstack')

auth_url = __config__.get('authUrl') or utilities.get_env('OS_AUTH_URL')
"""
The Identity authentication URL.
"""

cacert_file = __config__.get('cacertFile') or utilities.get_env('OS_CACERT')
"""
A Custom CA certificate.
"""

cert = __config__.get('cert') or utilities.get_env('OS_CERT')
"""
A client certificate to authenticate with.
"""

cloud = __config__.get('cloud') or utilities.get_env('OS_CLOUD')
"""
An entry in a `clouds.yaml` file to use.
"""

default_domain = __config__.get('defaultDomain') or (utilities.get_env('OS_DEFAULT_DOMAIN') or 'default')
"""
The name of the Domain ID to scope to if no other domain is specified. Defaults to `default` (Identity v3).
"""

domain_id = __config__.get('domainId') or utilities.get_env('OS_DOMAIN_ID')
"""
The ID of the Domain to scope to (Identity v3).
"""

domain_name = __config__.get('domainName') or utilities.get_env('OS_DOMAIN_NAME')
"""
The name of the Domain to scope to (Identity v3).
"""

endpoint_overrides = __config__.get('endpointOverrides')
"""
A map of services with an endpoint to override what was from the Keystone catalog
"""

endpoint_type = __config__.get('endpointType') or utilities.get_env('OS_ENDPOINT_TYPE')

insecure = __config__.get('insecure') or utilities.get_env_bool('OS_INSECURE')
"""
Trust self-signed certificates.
"""

key = __config__.get('key') or utilities.get_env('OS_KEY')
"""
A client private key to authenticate with.
"""

max_retries = __config__.get('maxRetries')
"""
How many times HTTP connection should be retried until giving up.
"""

password = __config__.get('password') or utilities.get_env('OS_PASSWORD')
"""
Password to login with.
"""

project_domain_id = __config__.get('projectDomainId') or utilities.get_env('OS_PROJECT_DOMAIN_ID')
"""
The ID of the domain where the proejct resides (Identity v3).
"""

project_domain_name = __config__.get('projectDomainName') or utilities.get_env('OS_PROJECT_DOMAIN_NAME')
"""
The name of the domain where the project resides (Identity v3).
"""

region = __config__.get('region') or utilities.get_env('OS_REGION_NAME')
"""
The OpenStack region to connect to.
"""

swauth = __config__.get('swauth') or utilities.get_env_bool('OS_SWAUTH')
"""
Use Swift's authentication system instead of Keystone. Only used for interaction with Swift.
"""

tenant_id = __config__.get('tenantId') or utilities.get_env('OS_TENANT_ID', 'OS_PROJECT_ID')
"""
The ID of the Tenant (Identity v2) or Project (Identity v3) to login with.
"""

tenant_name = __config__.get('tenantName') or utilities.get_env('OS_TENANT_NAME', 'OS_PROJECT_NAME')
"""
The name of the Tenant (Identity v2) or Project (Identity v3) to login with.
"""

token = __config__.get('token') or utilities.get_env('OS_TOKEN', 'OS_AUTH_TOKEN')
"""
Authentication token to use as an alternative to username/password.
"""

use_octavia = __config__.get('useOctavia') or utilities.get_env_bool('OS_USE_OCTAVIA')
"""
If set to `true`, API requests will go the Load Balancer service (Octavia) instead of the Networking service (Neutron).
"""

user_domain_id = __config__.get('userDomainId') or utilities.get_env('OS_USER_DOMAIN_ID')
"""
The ID of the domain where the user resides (Identity v3).
"""

user_domain_name = __config__.get('userDomainName') or utilities.get_env('OS_USER_DOMAIN_NAME')
"""
The name of the domain where the user resides (Identity v3).
"""

user_id = __config__.get('userId') or utilities.get_env('OS_USER_ID')
"""
Username to login with.
"""

user_name = __config__.get('userName') or utilities.get_env('OS_USERNAME')
"""
Username to login with.
"""

