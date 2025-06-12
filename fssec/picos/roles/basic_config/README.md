## Basic Role Configuration for PICA8 Switches Example

```yaml
hostname: PICA8-SPINE01
management_ip: 10.37.16.121/24
gateway: 10.37.16.254

ntp_server: 10.37.16.121
timezone: Asia/Shanghai

enable_lldp: true
enable_ssh: true
login_banner: "Unauthorized access prohibited"

username: admin
password: admin
owner_user: admin
group_user: xorp

ssh_user: admin
ssh_home: "/home/admin"
ssh_public_key: ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQDJb5ytIV4kRKa4M/A8po3r/Rdy6x6vMSAUu3ssuBY6gg8QdZo+opnJmnku7cQ3vXzoB+cMkoIWrRUbymQJSytkEBEukN2QCaFCrYRhvMO6GlistDYV6aQgHNJ7RrsBsqD1vObVzV2p3mMLfhPZRZo+furlUs6N8RIAK2wJZGkqrPc0zI1vNHbSuTmDd

snmp_community: public
snmp_authorization: read-only

LAG_CONFIG:
  - name: ae1
    description: test11
    lacp_enable: true
    native_vlan_id: 3966
    vlan_members: 20, 30, 3966

vlans_config:
  - vlan_id: 10
    description: test11
  - vlan_id: 20
    description: test22

vlans_delete:
  - vlan_id: 10
  - vlan_id: 20

show_uptime: true

dns_server_ip: 10.10.10.12
```
