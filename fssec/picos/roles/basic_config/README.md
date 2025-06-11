# basic_config

This role configures basic settings on PicOS switches such as hostname, users, NTP, management IP, SNMP, vlans and SSH keys.

## Role Variables

Example:

```yaml
    hostname: PICA8-SPINE
    management_ip: 192.168.0.12/24
    gateway: 192.168.0.254
    
    ntp_server: 192.168.0.122
    timezone: Asia/Shanghai
    
    enable_lldp: true
    enable_ssh: true
    login_banner: "Unauthorized access prohibited"
    
    username: xxx
    password: xxx
    owner_user: admin
    group_user: xorp
    
    ssh_user: admin
    ssh_public_key: ssh-rsa *****
    
    snmp_community: public
    snmp_authorization: read-only
    
    spine_ints:
      - name: ae1
        description: test11
      - name: ae2
        description: test22
```

