
# Ansible Galaxy PICOS Reference Guide

**fssec.picos** is an Ansible collection designed to manage and automate configurations for Pica8 network devices. This collection provides modules and playbooks to simplify network automation tasks.

## Features

- Automate configuration of Pica8 devices.
- Manage device settings, interfaces, and VLANs by basic config.
- Support for common network automation workflows.

## Installation

To install the `fssec.picos` collection, use the following steps:

- Ensure you have Ansible installed. You can install Ansible using pip:
```bash
pip install ansible
```

- Install the collection from the repository:
```bash
ansible-galaxy collection install fssec.picos
```

- Verify the installation:
```bash
ansible-galaxy collection list
```

## Usage

- Import the collection in your playbooks by roles:
 ```yaml
 ## playbook.yaml
 ## configure your path to variables
 ---
 - name: Basic switch config
   hosts: pica8_devices
   become: true
   gather_facts: no
   vars_files:
     - /path/to/variables/pica8_devices.yml
   roles:
     - fssec.picos.basic_config
```
   
- configure your group variables:
```bash
## pica8_devices.yml 
## Do not need to configure all configuration items. The following configuration items are optional and only perform tasks related to the configured variables.

hostname: PICA8-SPINE01
management_ip: 10.37.16.121/24
gateway: 10.37.16.254

ntp_server: 10.37.16.121
timezone: Asia/Shanghai

enable_lldp: true
enable_ssh: true
login_banner: "Unauthorized access prohibited"

username: admin
password: pica8@123
owner_user: admin
group_user: xorp

ssh_user: admin
ssh_home: "/home/admin"
ssh_public_key: ssh-rsa *****************

snmp_community: public
snmp_authorization: read-only

spine_ints:
  - name: ae1
    description: test11
  - name: ae2
    description: test22

spine_vlans_config:
  - vlan_id: 10
    description: test11
  - vlan_id: 20
    description: test22

spine_vlans_delete:
  - vlan_id: 10
  - vlan_id: 20

show_uptime: true

dns_server_ip: 10.10.10.12
```
   
- configure your hosts:
```bash
## hosts
[pica8_devices]
192.168.1.1 ansible_user=admin ansible_password=xxx ansible_ssh_common_args='-o UserKnownHostsFile=/dev/null -o StrictHostKeyChecking=no'
```


- Run the playbook:
```bash
ansible-playbook -i hosts playbook.yaml
```

- Output:
```bash
[WARNING]: While constructing a mapping from /home/pica8/pica8_devices.yaml, line 1, column 1, found a duplicate dict key (ssh_user). Using last defined value only.

PLAY [Basic switch config] **********************************************************************************************************************************************************************************************************************************

TASK [fssec.picos.basic_config : include_tasks] *************************************************************************************************************************************************************************************************************
included: /home/pica8/.ansible/collections/ansible_collections/fssec/picos/roles/basic_config/tasks/hostname.yml for xx.xx.xx.xx

TASK [fssec.picos.basic_config : Set hostname] **************************************************************************************************************************************************************************************************************
changed: [xx.xx.xx.xx]

TASK [fssec.picos.basic_config : include_tasks] *************************************************************************************************************************************************************************************************************
included: /home/pica8/.ansible/collections/ansible_collections/fssec/picos/roles/basic_config/tasks/management.yml for xx.xx.xx.xx

TASK [fssec.picos.basic_config : Configure management IP] ***************************************************************************************************************************************************************************************************
changed: [xx.xx.xx.xx]

TASK [fssec.picos.basic_config : Configure default gateway] *************************************************************************************************************************************************************************************************
ok: [xx.xx.xx.xx]

TASK [fssec.picos.basic_config : include_tasks] *************************************************************************************************************************************************************************************************************
included: /home/pica8/.ansible/collections/ansible_collections/fssec/picos/roles/basic_config/tasks/users.yml for xx.xx.xx.xx

TASK [fssec.picos.basic_config : Configure user account] ****************************************************************************************************************************************************************************************************
changed: [xx.xx.xx.xx]

TASK [fssec.picos.basic_config : include_tasks] *************************************************************************************************************************************************************************************************************
included: /home/pica8/.ansible/collections/ansible_collections/fssec/picos/roles/basic_config/tasks/ssh_keys.yml for xx.xx.xx.xx

TASK [fssec.picos.basic_config : Ensure .ssh directory exists] **********************************************************************************************************************************************************************************************
ok: [xx.xx.xx.xx]

TASK [fssec.picos.basic_config : Ensure .ssh directory exists] **********************************************************************************************************************************************************************************************
ok: [xx.xx.xx.xx]

TASK [fssec.picos.basic_config : Add SSH public key to authorized_keys] *************************************************************************************************************************************************************************************
ok: [xx.xx.xx.xx]

TASK [fssec.picos.basic_config : Ensure PubkeyAuthentication is enabled] ************************************************************************************************************************************************************************************
ok: [xx.xx.xx.xx]

TASK [fssec.picos.basic_config : Ensure AuthorizedKeysFile is configured] ***********************************************************************************************************************************************************************************
ok: [xx.xx.xx.xx]

TASK [fssec.picos.basic_config : include_tasks] *************************************************************************************************************************************************************************************************************
included: /home/pica8/.ansible/collections/ansible_collections/fssec/picos/roles/basic_config/tasks/ntp.yml for xx.xx.xx.xx

TASK [fssec.picos.basic_config : Configure NTP server] ******************************************************************************************************************************************************************************************************
ok: [xx.xx.xx.xx]

TASK [fssec.picos.basic_config : include_tasks] *************************************************************************************************************************************************************************************************************
included: /home/pica8/.ansible/collections/ansible_collections/fssec/picos/roles/basic_config/tasks/dns.yml for xx.xx.xx.xx

TASK [fssec.picos.basic_config : Set System DNS Server IP] **************************************************************************************************************************************************************************************************
ok: [xx.xx.xx.xx]

TASK [fssec.picos.basic_config : include_tasks] *************************************************************************************************************************************************************************************************************
included: /home/pica8/.ansible/collections/ansible_collections/fssec/picos/roles/basic_config/tasks/timezone.yml for xx.xx.xx.xx

TASK [fssec.picos.basic_config : Configure timezone] ********************************************************************************************************************************************************************************************************
changed: [xx.xx.xx.xx]

TASK [fssec.picos.basic_config : include_tasks] *************************************************************************************************************************************************************************************************************
included: /home/pica8/.ansible/collections/ansible_collections/fssec/picos/roles/basic_config/tasks/snmp.yml for xx.xx.xx.xx

TASK [fssec.picos.basic_config : Configure SNMP] ************************************************************************************************************************************************************************************************************
changed: [xx.xx.xx.xx]

TASK [fssec.picos.basic_config : include_tasks] *************************************************************************************************************************************************************************************************************
included: /home/pica8/.ansible/collections/ansible_collections/fssec/picos/roles/basic_config/tasks/interfaces.yml for xx.xx.xx.xx

TASK [fssec.picos.basic_config : Configure interfaces] ******************************************************************************************************************************************************************************************************
changed: [xx.xx.xx.xx] => (item={'name': 'ae1', 'description': 'test11'})
changed: [xx.xx.xx.xx] => (item={'name': 'ae2', 'description': 'test22'})

TASK [fssec.picos.basic_config : include_tasks] *************************************************************************************************************************************************************************************************************
included: /home/pica8/.ansible/collections/ansible_collections/fssec/picos/roles/basic_config/tasks/services.yml for xx.xx.xx.xx

TASK [fssec.picos.basic_config : Enable LLDP] ***************************************************************************************************************************************************************************************************************
ok: [xx.xx.xx.xx]

TASK [fssec.picos.basic_config : Enable SSH] ****************************************************************************************************************************************************************************************************************
changed: [xx.xx.xx.xx]

TASK [fssec.picos.basic_config : Set login banner] **********************************************************************************************************************************************************************************************************
changed: [xx.xx.xx.xx]

TASK [fssec.picos.basic_config : include_tasks] *************************************************************************************************************************************************************************************************************
included: /home/pica8/.ansible/collections/ansible_collections/fssec/picos/roles/basic_config/tasks/uptime.yml for xx.xx.xx.xx

TASK [fssec.picos.basic_config : Shows uptime info for all switches] ****************************************************************************************************************************************************************************************
ok: [xx.xx.xx.xx]

TASK [fssec.picos.basic_config : Show exec_result] **********************************************************************************************************************************************************************************************************
ok: [xx.xx.xx.xx] => {
    "exec_result.stdout_lines": [
        " 14:40:18 up 7 min,  1 user,  load average: 0.27, 0.26, 0.16"
    ]
}

TASK [fssec.picos.basic_config : include_tasks] *************************************************************************************************************************************************************************************************************
included: /home/pica8/.ansible/collections/ansible_collections/fssec/picos/roles/basic_config/tasks/vlans.yml for xx.xx.xx.xx

TASK [fssec.picos.basic_config : Configure vlans] ***********************************************************************************************************************************************************************************************************
changed: [xx.xx.xx.xx] => (item={'vlan_id': 10, 'description': 'test11'})
changed: [xx.xx.xx.xx] => (item={'vlan_id': 20, 'description': 'test22'})

TASK [fssec.picos.basic_config : Delete vlans] **************************************************************************************************************************************************************************************************************
changed: [xx.xx.xx.xx] => (item={'vlan_id': 10})
changed: [xx.xx.xx.xx] => (item={'vlan_id': 20})

PLAY RECAP **************************************************************************************************************************************************************************************************************************************************
xx.xx.xx.xx               : ok=33   changed=10   unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
```

## Modules

The collection includes the following modules:

- **picos_config**: Manage cli configurations on Pica8 devices.

##  Used **picos_config** Modules Example

You can directly use the custom module picos_config to assemble your own tasks for Pica8 devices:

```yaml
---
- name: Run CLI show command and get output
  hosts: all
  tasks:
    - name: Run "show version" command on the switch
      fssec.picos.picos_config:
        cmd: "show version"
        mode: cli_show
      register: show_version_output

    - name: Display the command output
      debug:
        var: show_version_output
```

## Output:
```bash
PLAY [Run CLI show command and get output] ******************************************************************************************************************************************************************************************************************

TASK [Gathering Facts] **************************************************************************************************************************************************************************************************************************************
ok: [xx.xx.xx.xx]

TASK [Run "show version" command on the switch] *************************************************************************************************************************************************************************************************************
ok: [xx.xx.xx.xx]

TASK [Display the command output] ***************************************************************************************************************************************************************************************************************************
ok: [xx.xx.xx.xx] => {
    "show_version_output": {
        "changed": false,
        "failed": false,
        "module": "picos_config",
        "rc": 0,
        "stdout": "Synchronizing configuration...OK.\nWelcome to PICOS\nadmin@PICA8-SPINE01> \nExecute command: show version\n.\nCopyright                     : Copyright (C) 2009-2025 Pica8, Inc. All Rights Reserved.\nModel                         : AS5812_54X\nSoftware Version              : 4.6.0E/9482280ad7\nSoftware Released Date        : 03/30/2025\nSerial Number                 : 140E356C6E22\nSystem Uptime                 : 0 day 0 hour 14 minute\nHardware ID                   : License Type                  : Uninstalled\nDevice MAC Address            : 0c:68:e0:0f:00:01\nadmin@PICA8-SPINE01> ",
        "stdout_lines": [
            "Synchronizing configuration...OK.",
            "Welcome to PICOS",
            "admin@PICA8-SPINE01> ",
            "Execute command: show version",
            ".",
            "Copyright                     : Copyright (C) 2009-2025 Pica8, Inc. All Rights Reserved.",
            "Model                         : AS5812_54X",
            "Software Version              : 4.6.0E/9482280ad7",
            "Software Released Date        : 03/30/2025",
            "Serial Number                 : 140E356C6E22",
            "System Uptime                 : 0 day 0 hour 14 minute",
            "Hardware ID                   : License Type                  : Uninstalled",
            "Device MAC Address            : 0c:68:e0:0f:00:01",
            "admin@PICA8-SPINE01> "
        ]
    }
}

PLAY RECAP **************************************************************************************************************************************************************************************************************************************************
xx.xx.xx.xx               : ok=3    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
```

## Contributing

Contributions are welcome! Please submit issues or pull requests to improve the collection.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

## Support

For support or questions, please contact **[sec@feisu.com]**.

