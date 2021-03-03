import atexit
import cmd
import readline


from rich.emoji import Emoji

from ziggy.settings import Settings
from ziggy.bot import Bot


class ZiggyShell(cmd.Cmd):
    prompt = Emoji.replace(":robot: ")

    def __init__(
        self, locals=None, filename="<ziggy>", histfile=Settings.HISTORY_PATH
    ):
        cmd.Cmd.__init__(self)
        self.init_history(histfile)
        self.bot = Bot()

    def init_history(self, histfile):
        readline.parse_and_bind("tab: complete")
        if hasattr(readline, "read_history_file"):
            try:
                readline.read_history_file(histfile)
            except FileNotFoundError:
                pass
            atexit.register(self.save_history, histfile)

    def save_history(self, histfile):
        readline.set_history_length(Settings.HISTORY_LENGTH)
        readline.write_history_file(histfile)

    def default(self, instruction):
        response = self.bot.execute(instruction)

        if response is not None:
            response.render()

    def do_greet(self, line):
        print("hello,", line)

    def do_adios(self, line):
        print("Live long and prosper")
        return True


if __name__ == "__main__":
    shell = ZiggyShell()
    shell.cmdloop()
