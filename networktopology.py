class NetworkTopology:
    def __init__(self):
        self.switches = {}  # Stores Switch objects

    def add_switch(self, switch: Switch):
        """ Adds a switch to the topology. """
        if switch.name in self.switches:
            print(f"Switch ({switch.name}) already exists.")
            return
        self.switches[switch.name] = switch
        print(f"{switch.role.capitalize()} switch added: {switch.name}")

    def remove_switch(self, switch_name: str):
        """ Removes a switch from the topology. """
        if switch_name in self.switches:
            del self.switches[switch_name]
            print(f"Switch removed: {switch_name}")
        else:
            print(f"Switch ({switch_name}) not found.")

    def connect_switches(self, switch_name1: str, port1: str, switch_name2: str, port2: str):
        """ Connects two switches using specified ports. """
        if not all(switch in self.switches for switch in [switch_name1, switch_name2]):
            print("Both switches must exist in the topology.")
            return
        if port1 not in self.switches[switch_name1].ports or port2 not in self.switches[switch_name2].ports:
            print("Both ports must exist on the respective switches.")
            return
        # Additional logic to handle port states and types can be added here

        # Simulating connection by setting port types to 'link'
        self.switches[switch_name1].ports[port1].type = "link"
        self.switches[switch_name2].ports[port2].type = "link"
        print(f"Connected {switch_name1} {port1} with {switch_name2} {port2}")

    def disconnect_switches(self, switch_name1: str, port1: str, switch_name2: str, port2: str):
        """ Disconnects two switches on specified ports. """
        if not all(switch in self.switches for switch in [switch_name1, switch_name2]):
            print("Both switches must exist in the topology.")
            return
        if port1 not in self.switches[switch_name1].ports or port2 not in self.switches[switch_name2].ports:
            print("Both ports must exist on the respective switches.")
            return
        # Additional logic to handle port states and types can be added here

        # Simulating disconnection by resetting port types
        self.switches[switch_name1].ports[port1].type = "access"  # or original type
        self.switches[switch_name2].ports[port2].type = "access"  # or original type
        print(f"Disconnected {switch_name1} {port1} and {switch_name2} {port2}")

    def print_topology(self):
        """ Prints the current network topology. """
        for switch in self.switches.values():
            print(f"Switch: {switch.name}, Role: {switch.role}, Ports: {switch.ports}")

# Example usage
topology = NetworkTopology()
topology.add_switch(Switch(name="Core1", role="core", ovs_name="ovs-core1"))
topology.add_switch(Switch(name="Access1", role="access", ovs_name="ovs-access1"))
# Assuming ports have been added to the switches
topology.connect_switches("Core1", "Port1", "Access1", "Port1")
topology.print_topology()
topology.disconnect_switches("Core1", "Port1", "Access1", "Port1")
topology.print_topology()
