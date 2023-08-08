#!/usr/bin/python

# Copyright: (c) 2023, ${your_name} <${your_email}>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

DOCUMENTATION = r'''
module: auth

short_description: authenticates against a REST API and returns an authentication token or other mechanism by which to continue authentication

requirements:
    - requests 2.31.0
    - base64
'''

EXAMPLES = r'''
# TODO
'''

RETURN = r'''
# TODO
'''

from ansible.module_utils.basic import AnsibleModule
import requests, base64

def collect_headers(*headers):

    headers_dict = dict()

    for header in headers:
        for key, value in header.items():
            headers_dict[key] = value

    return headers_dict
     

def dispatch_requests():

    auth_type = module.params.get('auth_type')
    auth = dict()

    if auth_type == 'token':
        auth['Authorization'] = "token " + module.params.get('token')
    elif auth_type == 'Bearer':
        auth['Authorization'] = "Bearer " + module.params.get('token')
    elif auth_type == 'Basic':

        message = module.params.get('username') + ":" + module.params.get('password')
        message = message.encode('ascii')

        encoded = base64.b64encode(message)
        encoded = encoded.decode('ascii')

        auth['Authorization'] = "Basic " + encoded
        


    headers = collect_headers(dict(Accept = "application/json"), auth)
    response = requests.get(module.params.get('url'), headers=headers)  
        
    result['changed'] = True

    if response.status_code >= 200 and response.status_code <= 300:

        result['response'] = response.json()

        return response 
    else:
        result['message'] = "Request failed: " + response.text
        return None

def run_module():

    module_args = dict(
        url       = dict(type='str', required=True),
        auth_type = dict(type='str', required=True, choices=["token", "Bearer", "Basic"]),
        token     = dict(type='str', required=False,),
        username  = dict(type='str', required=False,),
        password  = dict(type='str', required=False,),
    )

    global module
    module = AnsibleModule(
        argument_spec = module_args,
        required_if = [
            ('auth_type', 'token', ('token',), False),   
            ('auth_type', 'Bearer', ('token',), False),   
            ('auth_type', 'Basic', ('username', 'password'), False),
        ],
        required_together = [
            ('username', 'password'),
        ],
        mutually_exclusive = [
            ('token', 'password'),
        ],
        supports_check_mode = True
    )

    global result
    result = dict(
        changed = False,
        message = 'module started execution with authentication type: ' + module.params.get('auth_type'),
    )

    if module.check_mode:
        module.exit_json(**result)

    if dispatch_requests() is None:
        module.fail_json(result['message']);
    else:
        module.exit_json(**result)


def main():
    run_module()

if __name__ == '__main__':
    main()
