#!/usr/bin/python3
"""
    Command interpreter for AnA-BnB
"""
import cmd
import sys


class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '
    file = None

    def do_EOF(self, arg):
        """Implements EOF"""
        return True

    def do_quit(self, arg):
        """Implements EOF"""

        return True

    def emptyline(self):
        """An empty line + 'enter' shoudln't execute anything"""
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
