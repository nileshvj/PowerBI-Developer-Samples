# Copyright (c) Microsoft Corporation.
# Licensed under the MIT license.

class BaseConfig(object):

    # Can be set to 'MasterUser' or 'ServicePrincipal'
    AUTHENTICATION_MODE = 'ServicePrincipal'

    # Workspace Id in which the report is present 
    WORKSPACE_ID = 'f6d227dc-0a60-4744-94a8-de619a9db6e2' #njo_pbiemb_dev
    
    # Report Id for which Embed token needs to be generated
    #REPORT_ID = '832b9323-0d7e-45d0-b4d1-5afd2dd61af0' #US Sales Analysis
    REPORT_ID = '90bda401-67d3-4469-9079-e7978fe9566c' #Customer_RLSDemoReport
    
    
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

    # Master user email address. Required only for MasterUser authentication mode.
    POWER_BI_USER = ''
    
    # Master user email password. Required only for MasterUser authentication mode.
    POWER_BI_PASS = ''