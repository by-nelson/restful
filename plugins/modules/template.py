#!/usr/bin/python

# Copyright: (c) 2023, ${your_name} <${your_email}>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

DOCUMENTATION = r'''
module: TODO
'''

EXAMPLES = r'''
# TODO
'''

RETURN = r'''
# TODO
'''

from ansible.module_utils.basic import AnsibleModule

def run_module():

    module_args = dict(
        argument = dict(type='str', required=False),
    )

    module = AnsibleModule(
        argument_spec = module_args,
        supports_check_mode = True
    )

    result = dict(
        message = 'module started execution with argument: ' + module.params.get('argument') 
    )

    if module.check_mode:
        module.exit_json(**result)

    module.exit_json(**result)


def main():
    run_module()

if __name__ == '__main__':
    main()
