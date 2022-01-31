from prompt_toolkit.key_binding import KeyBindings

kb = KeyBindings()


@kb.add('c-q')
def exit_(event):
    """
    Pressing Ctrl-Q will exist the user interface
    """
    event.app.exit()
