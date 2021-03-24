import os
import sys

if sys.version_info < (3, 0):
    sys.stdout.write("Sorry, dirsearch requires Python 3.x\n")
    sys.exit(1)

from lib.core import ArgumentParser
from lib.controller import Controller
from lib.output import CLIOutput, PrintOutput


class Program(object):
    def __init__(self):
        self.script_path = os.path.dirname(os.path.realpath(__file__))

        self.arguments = ArgumentParser(self.script_path)

        if self.arguments.quiet:
            self.output = PrintOutput()
        else:
            self.output = CLIOutput()

        self.controller = Controller(self.script_path, self.arguments, self.output)


if __name__ == "__main__":
    main = Program()
