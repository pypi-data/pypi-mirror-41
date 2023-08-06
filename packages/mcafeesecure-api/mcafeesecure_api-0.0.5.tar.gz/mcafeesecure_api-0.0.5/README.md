# python-api

McAfee SECURE API - Python Module

This Python module interfaces with the McAfee SECURE API to issue
API requests.

Your API Key may be found at https://www.mcafeesecure.com/user/account/api or by contacting support@mcafeesecure.com.

This module requires one non-standard package:
    requests - a Python HTTP library

Example Uses:

    import mcafeesecure_api as ms
    ms.scan_targets()
    ms.scan_target(args.target_id)
    ms.scan_result(args.target_id, args.scan_id)
    ms.scan_vuln(args.vuln_id)


General API Notes:

    Full Documentation may be found at https://www.mcafeesecure.com/user/support/api/

        The McAfee Secure API enables customers and partners to integrate certain components
        of the McAfee Secure service into their application.

        All requests should be made to a URL similar to the following:

            https://api.mcafeesecure.com/api/v1/[METHOD].json


        To authenticate include an "x-apikey" header in your request. API keys are provisioned
        and configured by our support team. You can view your API keys here.

            curl --header "x-apikey: APIKEY" https://api.mcafeesecure.com/api/v1/[METHOD].json

        By default API calls are executed in the company that owns the API key. If the company is
        a reseller or otherwise has companies that it manages, those companies can be modified by
        including a "companyId" parameter in any request.

Changes:

    * 0.0.1 - [1/14/19]
        - Support added for: scan_targets, scan_target, scan_result, scan_vuln
    * 0.0.2 - [1/17/19]
        - Support added for: account_create, account_create_lite, site_add, site_update,
            site_get, site_delete, site_lookup, subscription_list, subscription_add,
            user_add, company_get, sso
    * 0.0.3 - [1/18/19]
        - Test candidate for PyPI-Test package submission
    * 0.0.4 - [1/18/19]
        - Bug fix to __init__.py
    * 0.0.5 - [1/28/19]
        - Working fix for __init__ importing, Pushed to PyPI

