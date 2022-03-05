#!/usr/bin/python3
""" Entry point for the command interpreter """


import cmd
import models
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """ Overrides methods to personalize command interpreter """

    prompt = "(hbnb) "
    classes = {"BaseModel": BaseModel}

    """--- HBNB Commands ---"""

    def do_create(self, arg):
        """Creates a new instance of class provided as argument """

        args = arg.split()
        if len(args) != 1:
            print(HBNBCommand.class_missing_err)
        if len(args) == 1:
            try:
                class_name = HBNBCommand.classes[args[0]]
                new_obj = class_name()
                print(new_obj.id)
                models.storage.save()
            except KeyError:
                print(HBNBCommand.class_ntexist_err)
        else:
            print("Usage: create <class_name>")

    def do_show(self, arg):
        """ prints string representation of an instance from
        class name and id """
        args = arg.split()
        if len(args) == 2:
            obj_key = HBNBCommand.form_key(args[0], args[1])
            if args[0] not in HBNBCommand.classes:
                print(HBNBCommand.class_ntexist_err)
            elif obj_key not in models.storage.all():
                print(HBNBCommand.no_instance_found_err)
            else:
                print(models.storage.all()[obj_key])
        else:
            if len(args) == 0:
                print(HBNBCommand.class_missing_err)
            elif len(args) == 1:
                print(HBNBCommand.instance_id_missing_err)

    def do_all(self, arg):
        """ prints string representation of all objects
        from a certain class (or all objects if no class
        is specified"""
        args = arg.split()
        all_objs = models.storage.all()
        obj_list = []
        if len(args) == 0:
            obj_list = [all_objs[key].__str__() for key in all_objs]
            print(obj_list)
        else:
            if args[0] not in HBNBCommand.classes:
                print(HBNBCommand.class_ntexist_err)
            else:
                # Iterate through all_objs and add to obj_list
                # the instances that have the class given in its
                # string representation (__class__)
                for key in all_objs:
                    if args[0] in all_objs[key].__str__():
                        obj_list.append(all_objs[key].__str__())
                print(obj_list)

    # ---Basic Commands---

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """Quit command to exit the program"""
        return True

    # ---Overwritten methods---

    def emptyline(self):
        pass

    # ---Helper methods---

    def form_key(classname, uuid):
        return classname + "." + uuid

    def do_printkey(self, arg):
        args = arg.split()
        print(HBNBCommand.form_key(args[0], args[1]))

    def do_showall(self, arg):
        print(models.storage.all())

    # ---ERROR MESSAGES---

    class_missing_err = "** class name missing **"
    class_ntexist_err = "** class doesn't exist **"
    class_no_id_err = "** instance id missing **"
    no_instance_found_err = " ** no instance found **"
    instance_id_missing_err = " ** instance id missing **"
    attr_name_missing_err = "** attribute name missing **"
    value_missing_err = " ** value missing **"


if __name__ == '__main__':
    HBNBCommand().cmdloop()
