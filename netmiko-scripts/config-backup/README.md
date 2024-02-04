## Telnet Config Backup
### Prerequisites
python, netmiko, SSH enabled on the network device
### Description
Record the "show running-config" of the devices listed in the Netmiko python script.  Push the output to a file. To run this script, configure your network devices in the python script.  Filling in device_type, ip, username, and password:

```
example_device_X = {
    'device_type': 'cisco_ios',
    'ip': 'ip_addr',
    'username': 'username',
    'password': 'password'

}
```

Add the devices to the list of devices:
```devices = [example_device_1, example_device_2, example_device_etc]```
 
