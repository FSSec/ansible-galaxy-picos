
# Ansible Galaxy PICOS Reference Guide

`fssec.picos` is an Ansible collection designed to manage and automate configurations for Pica8 network devices. This collection provides modules and playbooks to simplify network automation tasks.

## Features

- Automate configuration of Pica8 devices.
- Manage device settings, interfaces, and VLANs by basic config.
- Support for common network automation workflows.

## Installation

To install the `fssec.picos` collection, use the following steps:

1. Ensure you have Ansible installed. You can install Ansible using pip:
   ```bash
   pip install ansible
   ```

2. Install the collection from the repository:
   ```bash
   ansible-galaxy collection install fssec.picos
   ```

3. Verify the installation:
   ```bash
   ansible-galaxy collection list
   ```

## Usage

1. Import the collection in your playbooks by roles:
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
   
2. configure your group variables:
```yaml
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
   
   ssh_user: admin
   ssh_home: "/home/admin"
```
   
2. configure your hosts:
```yaml 
   ## hosts
      [pica8_devices]
      192.168.1.1 ansible_user=admin ansible_password=xxx ansible_ssh_common_args='-o UserKnownHostsFile=/dev/null -o StrictHostKeyChecking=no'
```


2. Run the playbook:
```bash
   ansible-playbook -i hosts playbook.yaml
```

## Modules

The collection includes the following modules:

- **picos_config**: Manage cli configurations on Pica8 devices.

##  Used **picos_config** Modules Example

You can directly use the custom module picos_config to assemble your own tasks for Pica8 devices:

```yaml
- name: Run CLI show command
  fssec.picos.picos_config:
    cmd: "show version"
    mode: cli_show
```

## Contributing

Contributions are welcome! Please submit issues or pull requests to improve the collection.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

## Support

For support or questions, please contact **[sec@feisu.com]**.
