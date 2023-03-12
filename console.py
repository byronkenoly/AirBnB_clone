#!/usr/bin/python3
"""
contains the entry point of the command interpreter
"""

import cmd

class HBNBCommand(cmd.Cmd):
    """
    command interpreter class
    """
    prompt = '(hbnb)'

    def do_quit(self, line):
        """Quit command to exit the program
        """
        return True

    def do_EOF(self, line):
        """Quit command to exit the program
        """
        return True

    def emptyline(self):
        """an empty line + ENTER shouldn’t execute anything
        """
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
