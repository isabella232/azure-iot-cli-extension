# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class Tenant(Model):
    """Tenant Class.

    :param azure_ad_tenant_name: Gets or sets the name of the azure ad tenant.
    :type azure_ad_tenant_name: str
    :param azure_ad_tenant_id: Gets or sets the azure ad tenant identifier.
    :type azure_ad_tenant_id: str
    :param microsoft_partner_network_id: Gets or sets the microsoft partner
     network identifier.
    :type microsoft_partner_network_id: str
    :param number_of_models_created: Gets or sets the number of models
     created.
    :type number_of_models_created: int
    :param number_of_models_published: Gets or sets the number of models
     published.
    :type number_of_models_published: int
    :param tenant_id: Gets or sets the tenant identifier.
    :type tenant_id: str
    """

    _attribute_map = {
        'azure_ad_tenant_name': {'key': 'azureAdTenantName', 'type': 'str'},
        'azure_ad_tenant_id': {'key': 'azureAdTenantId', 'type': 'str'},
        'microsoft_partner_network_id': {'key': 'microsoftPartnerNetworkId', 'type': 'str'},
        'number_of_models_created': {'key': 'numberOfModelsCreated', 'type': 'int'},
        'number_of_models_published': {'key': 'numberOfModelsPublished', 'type': 'int'},
        'tenant_id': {'key': 'tenantId', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(Tenant, self).__init__(**kwargs)
        self.azure_ad_tenant_name = kwargs.get('azure_ad_tenant_name', None)
        self.azure_ad_tenant_id = kwargs.get('azure_ad_tenant_id', None)
        self.microsoft_partner_network_id = kwargs.get('microsoft_partner_network_id', None)
        self.number_of_models_created = kwargs.get('number_of_models_created', None)
        self.number_of_models_published = kwargs.get('number_of_models_published', None)
        self.tenant_id = kwargs.get('tenant_id', None)