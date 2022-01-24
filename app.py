from prompt_toolkit import PromptSession
from prompt_toolkit.completion import FuzzyWordCompleter
from prompt_toolkit.styles import Style
from sshconf import read_ssh_config
import os

SSH_CONFIG = os.environ.get("HOME") + "/.ssh/config"


def parse_ssh_config():
    config = read_ssh_config(SSH_CONFIG)
    return list(config.hosts())


host_completer = FuzzyWordCompleter(parse_ssh_config())

style = Style.from_dict({
    'completion-menu.completion': 'bg:#008888 #ffffff',
    'completion-menu.completion.current': 'bg:#00aaaa #000000',
    'scrollbar.background': 'bg:#88aaaa',
    'scrollbar.button': 'bg:#222222',
})


def initiate_connection(host, host_info):
    print(f'Connecting to {host}...')
    os.system(f'ssh {host}')


def main():
    session = PromptSession(completer=host_completer, style=style)

    input = ''
    while input != 'quit':
        try:
            input = session.prompt('>> ')
        except KeyboardInterrupt:
            break
        except EOFError:
            break
        else:
            if input == 'quit':
                break
            config = read_ssh_config(SSH_CONFIG)
            if input not in parse_ssh_config():
                print(f'Could not find host {input}')
            else:
                initiate_connection(input, config.host(input))
    print('Goodbye!')


if __name__ == "__main__":
    main()
