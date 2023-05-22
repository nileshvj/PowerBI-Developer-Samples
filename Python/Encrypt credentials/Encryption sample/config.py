# Copyright (c) Microsoft Corporation.
# Licensed under the MIT license.

class BaseConfig(object):

    # Can be set to 'MasterUser' or 'ServicePrincipal'
    AUTHENTICATION_MODE = 'ServicePrincipal'

    # Id of the Azure tenant in which AAD app and Power BI report is hosted. Required only for ServicePrincipal authentication mode.
    TENANT_ID = '5bf3c1fd-b8c2-4e49-9ee8-c50d58176587'

    # Client Id (Application Id) of the AAD app
    CLIENT_ID = '95770262-7d67-44df-b32c-d9010da0412f'

    # Client Secret (App Secret) of the AAD app. Required only for ServicePrincipal authentication mode.
    CLIENT_SECRET = 'tdO8Q~rVitRJ5W30C-PMXG2~bDQwDrALutvJXcvQ'

    # Scope Base of AAD app. Use the below configuration to use all the permissions provided in the AAD app through Azure portal.
    SCOPE_BASE = ['https://analysis.windows.net/powerbi/api/.default']

    # URL used for initiating authorization request
    AUTHORITY_URL = 'https://login.microsoftonline.com/5bf3c1fd-b8c2-4e49-9ee8-c50d58176587'

    # End point URL for Power BI API
    POWER_BI_API_URL = 'https://api.powerbi.com/'

    # Master user email address. Required only for MasterUser authentication mode.
    POWER_BI_USER = ''

    # Master user password. Required only for MasterUser authentication mode.
    POWER_BI_PASS = ''
