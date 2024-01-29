class Switch:
    def __init__(self, name, role, ovs_name):
        self.name = name
        self.role = role
        self.ovs_name = ovs_name  # OVS switch name
        self.ports = {}
        self.create_ovs_switch()

    def run_ovs_command(self, command):
        """ Executes an OVS command. """
        try:
            subprocess.run(command, check=True, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        except subprocess.CalledProcessError as e:
            print(f"Error occurred while executing OVS command: {e}")

    def create_ovs_switch(self):
        """ Creates an OVS switch. """
        self.run_ovs_command(f"ovs-vsctl add-br {self.ovs_name}")
        print(f"OVS switch created: {self.ovs_name}")
