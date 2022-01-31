from prompt_toolkit import Application
from prompt_toolkit.buffer import Buffer
from prompt_toolkit.layout.containers import Window, VSplit
from prompt_toolkit.layout.controls import BufferControl, FormattedTextControl
from prompt_toolkit.layout.layout import Layout
from prompt_toolkit.input.defaults import create_input
from prompt_toolkit.output.defaults import create_output

from .key_bindings import kb

from paramiko.client import SSHClient

import sys
import time


class Session():
    def __init__(self, host_info):
        print(host_info)
        self.hostname = host_info['hostname']
        self.user = host_info['user']
        self.identityfile = host_info['identityfile']

    def test(self):
        print("hello")

    def _initialize_app(self):
        client = SSHClient()
        client.load_host_keys()
        client.connect(host=self.hostname, username=self.user,
                       key_filename=self.identityfile)
        buffer1 = Buffer()
        root_container = VSplit([
            Window(content=BufferControl(buffer=buffer1)),
        ])

        layout = Layout(root_container)
        self.session = Application(
            layout=layout,
            full_screen=True,
            key_bindings=kb,
            input=create_input(),
            output=create_output(stdout=sys.stdout))

    def connect(self):
        self._initialize_app()
        time.sleep(.5)
        self.session.run()
