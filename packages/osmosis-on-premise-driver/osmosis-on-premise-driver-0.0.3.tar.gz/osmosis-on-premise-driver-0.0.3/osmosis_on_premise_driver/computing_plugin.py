from osmosis_driver_interface.computing_plugin import AbstractPlugin


class Plugin(AbstractPlugin):
    def type(self):
        """str: the type of this plugin (``'On premise'``)"""
        return 'On premise'

    def create_vm(self):
        pass

    def start_vm(self, instance_name):
        pass

    def stop_vm(self, instance_name):
        pass

    def run_command(self, instance_name, command):
        pass

    def delete_vm(self, instance_name):
        pass

    def status_vm(self, instance_name):
        pass

    def copy(self, instance_name, source_path, dest_path):
        pass

    def retrieve_computation_proof(self):
        pass

    def retrieve_vm_logs(self):
        pass
