from logging import config
from netmiko import ConnectHandler

example_device_1 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.88.8',
    'username': 'matt',
    'password': '071499'
}

example_device_2 = {
    'device_type': 'cisco_ios',
    'ip': 'ip_addr',
    'username': 'username',
    'password': 'password'
}

# Configure devices above, add newly configured devices to list of devices
devices = [example_device_1]

for device in devices:
    net_connect = ConnectHandler(**device)
    config_commands = ["do show run\n"]
    output = net_connect.send_config_set(config_commands)
    f = open(f"config_{device['ip']}", "w")
    f.write(output)


print(output)