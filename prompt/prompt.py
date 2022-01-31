from prompt_toolkit import PromptSession
from prompt_toolkit.completion import FuzzyWordCompleter
from prompt_toolkit.styles import Style
from sshconf import read_ssh_config
import os


class SSHPrompt():
    """Main class for SSHPrompt. Generates the intial prompt and loads
    all defaults"""

    def __init__(self):
        self.SSH_CONFIG = os.environ.get("HOME") + "/.ssh/config"
        self.host_completer = FuzzyWordCompleter(self.parse_ssh_config())

        self.style = Style.from_dict({
            'completion-menu.completion': 'bg:#008888 #ffffff',
            'completion-menu.completion.current': 'bg:#00aaaa #000000',
            'scrollbar.background': 'bg:#88aaaa',
            'scrollbar.button': 'bg:#222222',
        })
        self.session = PromptSession(
            completer=self.host_completer, style=self.style)

    def parse_ssh_config(self):
        config = read_ssh_config(self.SSH_CONFIG)
        return list(config.hosts())

    def initiate_connection(self, host, host_info):
        print(f'Connecting to {host}...')
        os.system(f'ssh {host}')

    def run(self):
        input = ''
        while input != 'quit':
            try:
                input = self.session.prompt('>> ')
            except KeyboardInterrupt:
                break
            except EOFError:
                break
            else:
                if input == 'quit':
                    break
                config = read_ssh_config(self.SSH_CONFIG)
                if input not in self.parse_ssh_config():
                    print(f'Could not find host {input}')
                else:
                    self.initiate_connection(input, config.host(input))
        print('Goodbye!')
