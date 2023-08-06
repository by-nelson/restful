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
'''

EXAMPLES = r'''
# TODO
'''

RETURN = r'''
# TODO
'''

from ansible.module_utils.basic import AnsibleModule
import requests

def run_module():

    module_args = dict(
        url       = dict(type='str', required=True),
        auth_type = dict(type='str', required=True, choices=["token", "Bearer", "Basic"]),
        token     = dict(type='str', required=False,),
        username  = dict(type='str', required=False,),
        password  = dict(type='str', required=False,),
    )

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

    result = dict(
        message = 'module started execution with authentication type: ' + module.params.get('auth_type') 
    )

    if module.check_mode:
        module.exit_json(**result)

    module.exit_json(**result)


def main():
    run_module()

if __name__ == '__main__':
    main()
