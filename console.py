#!/usr/bin/python3
""" Entry point for the command interpreter """


import cmd
import models


class HBNBCommand(cmd.Cmd):
    """ Overrides methods to personalize command interpreter """

    prompt = "(hbnb) "

    """--- HBNB Commands ---"""

    def do_create(self, arg):
        """Creates a new instance of class provided as argument """

        args = arg.split()
        if len(args) != 1:
            print(HBNBCommand.class_missing_err)
        else:
            try:
                class_name = getattr(models, classname)
                obj = class_name()
            except NameError:
                print(HBNBCommand.class_ntexist_err)

        def do_show(self, arg):
            """ prints string representation of an instance from
            class name and id """
            args = arg.split()

    """ ---Basic Commands--- """

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """Quit command to exit the program"""
        return True

    """---Overwritten methods---"""

    def emptyline(self):
        pass

    """---Helper methods---"""

    """---ERROR MESSAGES---"""

    class_missing_err = "** class name missing **"
    class_ntexist_err = "** class doesn't exist **"
    class_no_id_err = "** instance id missing **"


if __name__ == '__main__':
    HBNBCommand().cmdloop()
