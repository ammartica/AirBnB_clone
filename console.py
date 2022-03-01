#!/usr/bin/python3
""" Entry point for the command interpreter """


import cmd


class HBNBCommand(cmd.Cmd):
    """ Overrides methods to personalize command interpreter """

    prompt = "(hbnb) "
    """ HBNB Commands """

    """ Basic Commands """

    def do_quit(self, arg):
        """ Quit command to exit the program """
        return True

    def do_EOF(self, arg):
        """ Quit command to exit the program """
        return True

    """ Overwritten methods """

    def emptyline(self):
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
