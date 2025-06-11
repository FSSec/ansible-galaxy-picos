#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
@author: Charlie.Chen
@project: Pica8
@file: picos_config.py
@function:
@time: 2022/3/14 15:54
"""

DOCUMENTATION = r'''
---
module: picos_config
short_description: Manage PicOS CLI configuration
version_added: "1.0.0"
description:
  - This module executes commands on Pica8 switches in different modes such as shell, cli_show, cli_config, and config_load.
options:
  cmd:
    description:
      - The command or script to execute on the switch.
    required: true
    type: str
  mode:
    description:
      - Mode to apply the command.
      - Must be one of C(shell), C(cli_show), C(cli_config), or C(config_load).
    required: false
    type: str
    choices: [shell, cli_show, cli_config, config_load]
author:
  - FS-Pica8 Developer Office
'''

EXAMPLES = r'''
- name: Run CLI show command
  fssec.picos.picos_config:
    cmd: "show version"
    mode: cli_show

- name: Run CLI config command
  fssec.picos.picos_config:
    cmd: "set system hostname spine1"
    mode: cli_config

- name: Run shell command
  fssec.picos.picos_config:
    cmd: "ls -l"
    mode: shell

- name: Load config from file
  fssec.picos.picos_config:
    cmd: "/home/admin/my_config.conf"
    mode: config_load
'''

RETURN = r'''
stdout:
  description: The output returned from the command execution.
  type: str
  returned: always
rc:
  description: The return code from the command.
  type: int
  returned: always
changed:
  description: Whether the command made changes to the system.
  type: bool
  returned: always
msg:
  description: Optional message if the command failed.
  type: str
  returned: on failure
'''


import os
import re
import sys

if sys.version_info.major >= 3:
    import subprocess
else:
    import commands as subprocess

from ansible.module_utils.basic import AnsibleModule




class SwitchMode(object):
    def __init__(self, cmd):
        self.cmd = cmd
        self.changed_flag = False
        self.status = None
        self.output = None
    
    @staticmethod
    def __generate_tmp_config(cmd):
        with open("/home/admin/ansible_config_tmp_new.conf", 'w') as config_file:
            for config_line in cmd:
                config_file.write(config_line)
        return 0
    
    @staticmethod
    def __remove_tmp_config():
        # tips: code & msg must be (0, ''), don't return
        subprocess.getstatusoutput("rm -f /home/admin/ansible_config_tmp_new.conf")
    
    @staticmethod
    def __read_config_file(file):
        orig_cmd_str_list = list()
        if os.path.exists(file):
            with open(file) as cf:
                orig_cmd_str_list = cf.readlines()
        return ";".join(orig_cmd_str_list)
    
    @staticmethod
    def __get_cmd():
        cmd = "/pica/bin/pica_sh -c 'configure;show | display set'"
        status, output = subprocess.getstatusoutput(cmd)
        if status == 0:
            cmd_array = re.findall("(set .*)", output)
            return cmd_array
    
    def __check_cmd_str(self, cmd_str):
        cmd_array = cmd_str.split(";")
        full_config_list = self.__get_cmd()
        if not isinstance(full_config_list, list):
            return -1
        full_config_str = ''.join(full_config_list)
        new_cmd = list()
        for cmd in cmd_array:
            if full_config_str.find(cmd.replace('\n', '').replace('\r', '').replace('\\', '')) == -1:
                new_cmd.append(cmd)
        return new_cmd
    
    def mode_shell(self):
        self.status, self.output = subprocess.getstatusoutput(self.cmd)
    
    def mode_cli_show(self):
        self.status, self.output = subprocess.getstatusoutput("/pica/bin/pica_sh -c \'" + self.cmd + "\'")
    
    def mode_cli_config(self):
        new_cmd_str = self.__check_cmd_str(self.cmd)
        if new_cmd_str == -1:
            self.status, self.output = 1, 'can not get config'
        elif len(new_cmd_str) > 0:
            new_cmd_str = ";".join(new_cmd_str)
            run_cmd = "/pica/bin/pica_sh -c \'" + "configure;" + new_cmd_str + ";commit\'"
            self.status, self.output = subprocess.getstatusoutput(run_cmd)
            self.changed_flag = True
        else:
            self.status, self.output = 0, "Need not configure switch"
    
    def mode_config_load(self):
        orig_cmd_str = self.__read_config_file(self.cmd)
        if not orig_cmd_str:
            self.status, self.output = 0, 'can not get config file'
            return
        new_cmd_array = self.__check_cmd_str(orig_cmd_str)
        if new_cmd_array == -1:
            self.status, self.output = 1, 'can not get config'
        elif len(new_cmd_array) > 0:
            # generate the new config file in switch after checking
            if self.__generate_tmp_config(new_cmd_array) == 0:
                cmd_str = "configure;execute /home/admin/ansible_config_tmp_new.conf;"
                run_cmd = "/pica/bin/pica_sh -c \'" + cmd_str + "commit\'"
                self.status, self.output = subprocess.getstatusoutput(run_cmd)
                if "failed" in self.output:
                    self.status = 1
                    self.changed_flag = False
                else:
                    self.status = 0
                    self.changed_flag = True
            else:
                self.status = 1
                self.output = "Failed to create temperlate config in switch."
            # remove the temp config file after load the configuration file
            self.__remove_tmp_config()
        else:
            self.status, self.output = 0, "Need not configure switch"
    
    def get_mode(self, mode_name):
        func = getattr(self, "mode_%s" % mode_name)
        func()


def run_module():
    # define available arguments/parameters a user can pass to the module
    module_args = dict(
        mode=dict(type='str', default='shell', choices=['shell', 'cli_show', 'cli_config', 'config_load']),
        cmd=dict(type='str', required=True)
    )
    
    # the AnsibleModule object will be our abstraction working with Ansible
    # this includes instantiation, a couple of common attr would be the
    # args/params passed to the execution, as well as if the module
    # supports check mode
    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True
    )
    
    cmd = module.params['cmd']
    mode = module.params['mode']
    
    sm = SwitchMode(cmd)
    sm.get_mode(mode)
    
    # if the user is working with this module in only check mode we do not
    # want to make any changes to the environment, just return the current
    # state with no modifications
    if sm.status == 0:
        result = dict(module='picos_config', stdout=sm.output, changed=sm.changed_flag, rc=sm.status)
        module.exit_json(**result)
    else:
        result = dict(msg='execute failed', stdout=sm.output, changed=False, rc=sm.status)
        module.fail_json(**result)


def main():
    run_module()


if __name__ == '__main__':
    main()

