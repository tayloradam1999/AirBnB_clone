#!/susr/bin/python3
"""
    Command interpreter for AnA-BnB
"""
import cmd
import sys


class AirbnbShell(cmd.Cmd):
    intro = "Welcome to the turtle shell.   Type help or ? to list commands.\n"
    prompt = "(hbnb) "
    file = None

    def do_hello(self, arg):
        """ Print 'Hello', followed by arg: HELLO HOLBERTON """
        print("Hello, {}".format(arg))

    def do_bye(self, arg):
        'Stop recording, close the hbnb window, and exit:  BYE'
        print('Thank you for using hbnb')
        self.close()
        return True

    def precmd(self, line):
        line = line.lower()
        if self.file and 'playback' not in line:
            print(line, file=self.file)
        return line

    def close(self):
        if self.file:
            self.file.close()
            self.file = None


def parse(arg):
    'Convert a series of zero or more numbers to an argument tuple'
    return tuple(map(int, arg.split()))

if __name__ == '__main__':
    AirbnbShell().cmdloop()
