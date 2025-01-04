from netmiko import ConnectHandler
from pprint import pprint


# Class for managing network device interactions
class NetworkDevice:
    def __init__(self, device_params):
        self.device_params = device_params
        self.connection = None

    def connect(self):
        try:
            self.connection = ConnectHandler(**self.device_params)
            print(f"Connected to {self.device_params['host']}")
        except Exception as e:
            print(f"Failed to connect to {self.device_params['host']}: {e}")
            self.connection = None

    def disconnect(self):
        if self.connection:
            self.connection.disconnect()
            print(f"Disconnected from {self.device_params['host']}.")

    def send_command(self, command):
        if self.connection:
            return self.connection.send_command(command)
        else:
            return "No connection established."

    def send_config(self, config_commands):
        if self.connection:
            return self.connection.send_config_set(config_commands)
        else:
            return "No connection established."

    def send_config_from_file(self, file_path):
        if self.connection:
            return self.connection.send_config_from_file(file_path)
        else:
            return "No connection established."


# Function to check if a file exists before reading
def read_file(file_path):
    try:
        with open(file_path, "r") as file:
            return file.read()
    except FileNotFoundError:
        return f"File {file_path} not found."


# Function to send show commands to multiple devices
def send_show_to_multiple_devices(devices, command):
    results = {}
    for device_params in devices:
        device = NetworkDevice(device_params)
        device.connect()
        if device.connection:
            results[device.device_params["host"]] = device.send_command(command)
        device.disconnect()
    return results


# Function to send configuration commands to multiple devices
def send_config_to_multiple_devices(devices, config_commands):
    results = {}
    for device_params in devices:
        device = NetworkDevice(device_params)
        device.connect()
        if device.connection:
            results[device.device_params["host"]] = device.send_config(config_commands)
        device.disconnect()
    return results


# Device details for multiple devices
devices = [
    {
        "device_type": "cisco_ios",
        "host": "192.168.56.101",
        "port": 22,
        "username": "cisco",
        "password": "cisco123!",
    },
    {
        "device_type": "cisco_ios",
        "host": "192.168.56.102",
        "port": 22,
        "username": "cisco",
        "password": "cisco123!",
    },
]

# Main script logic
if __name__ == "__main__":
    device = NetworkDevice(devices[0])  # Using the first device for single operations
    device.connect()

    if device.connection:
        # 1. Send a show command
        show_output = device.send_command("show ip interface brief")
        pprint(show_output)

        pprint("-------------------------")

        # 2. Configure hostname
        hostname_config = ["hostname Router1"]
        config_output = device.send_config(hostname_config)
        pprint(config_output)

        pprint("-------------------------")

        # 3. Save show command output to a file
        show_output = device.send_command("show ip interface brief")
        with open("output.txt", "w") as file:
            file.write(show_output)

        saved_output = read_file("output.txt")
        pprint("Output from output.txt:")
        pprint(saved_output)

        pprint("-------------------------")

        # 4. Backup device configuration
        backup_config = device.send_command("show run")
        with open("backup.txt", "w") as file:
            file.write(backup_config)

        backup_output = read_file("backup.txt")
        pprint("Output from backup.txt:")
        pprint(backup_output)

        pprint("-------------------------")

        # 5. Send configuration from a file
        config_file = "config_file.txt"
        config_from_file = device.send_config_from_file(config_file)
        if "File not found" not in config_from_file:
            pprint(config_from_file)
        else:
            pprint("Configuration file not found, skipping.")

        pprint("-------------------------")

        # 6. Configure a subset of interfaces
        interfaces_to_configure = [
            {"interface": "GigabitEthernet1", "description": "g1"}
        ]

        for i in interfaces_to_configure:
            commands = [
                f"interface {i['interface']}",
                f"description {i['description']}",
                "no shutdown",
            ]
            config_subnets = device.send_config(commands)
            pprint(config_subnets)

        pprint("-------------------------")

    else:
        print("Could not establish a connection to the device.")

    device.disconnect()

    # 7. Send show commands to multiple devices
    print("Sending show commands to multiple devices...")
    show_results = send_show_to_multiple_devices(devices, "show ip interface brief")
    for host, output in show_results.items():
        print(f"\nShow command output for {host}:")
        pprint(output)

    pprint("-------------------------")

    # 8. Send configuration commands to multiple devices
    print("Sending configuration commands to multiple devices...")
    config_commands = ["logging buffered 20000", "logging console informational"]
    config_results = send_config_to_multiple_devices(devices, config_commands)
    for host, output in config_results.items():
        print(f"\nConfiguration results for {host}:")
        pprint(output)
