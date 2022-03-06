#!/usr/bin/python3
""" Entry point for the command interpreter """


import cmd
import models
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class HBNBCommand(cmd.Cmd):
    """ Overrides methods to personalize command interpreter """

    prompt = "(hbnb) "
    classes = {"BaseModel": BaseModel, "Amenity": Amenity, "City": City,
               "Place": Place, "Review": Review, "State": State,
               "User": User}

    """--- HBNB Commands ---"""

    def do_create(self, arg):
        """Creates a new instance of class provided as argument """

        args = arg.split()
        error = HBNBCommand.find_error(args, 1)
        if (error is None):
            class_name = HBNBCommand.classes[args[0]]
            new_obj = class_name()
            print(new_obj.id)
            models.storage.save()
        else:
            print(error)

    def do_show(self, arg):
        """ prints string representation of an instance from
        class name and id """
        args = arg.split()
        error = HBNBCommand.find_error(args, 2)
        if (error is None):
            obj_key = HBNBCommand.form_key(args[0], args[1])
            print(models.storage.all()[obj_key])
        else:
            print(error)

    def do_all(self, arg):
        """ prints string representation of all objects
        from a certain class (or all objects if no class
        is specified"""
        args = arg.split()
        # If no args given, it'll return missing_class
        error = HBNBCommand.find_error(args, 1)
        if (error == HBNBCommand.class_ntexist_err):
            print(error)
        if (error == HBNBCommand.class_missing_err or
                error is None):
            # If the only error is class missing
            # that means no args were given
            # So code can continue
            all_objs = models.storage.all()
            obj_list = []

        # -- If no class is given print all objects

            if len(args) == 0:
                obj_list = [all_objs[key].__str__() for key in all_objs]
                print(obj_list)
            else:
                # Iterate through all_objs and add to obj_list
                # the instances that have the class given in its
                # string representation (__class__)
                for key in all_objs:
                    if args[0] in all_objs[key].__str__():
                        obj_list.append(all_objs[key].__str__())
                print(obj_list)

    def do_destroy(self, arg):
        """Deletes an instance based on class name and id"""
        args = arg.split()
        error = HBNBCommand.find_error(args, 2)
        if error is not None:
            print(error)
        else:
            obj_key = HBNBCommand.form_key(args[0], args[1])
            models.storage.all().pop(obj_key)
            models.storage.save()

    def do_update(self, arg):
        """ Updates instance based on class_name, id, attribute and value"""
        args = arg.split()
        error = HBNBCommand.find_error(args, 4)
        if error is None:
            # fetches object through id, then checks attr_type
            # if attr_type is a simple type it'll set the attr
            # using args[4], and converts it
            simple_types = {"int": int, "str": str, "float": float}
            obj_key = HBNBCommand.form_key(args[0], args[1])
            obj = models.storage.all()[obj_key]
            attr_type = type(getattr(obj, args[2]))
            setattr(models.storage.all()[obj_key], args[2], attr_type(args[3]))
            models.storage.save()
        else:
            print(error)

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
        """ creates obj_key to find specific instances """
        return classname + "." + uuid

    def find_error(args, expected=0):
        """ Primary error handling function """
        if len(args) >= 2:
            obj_key = HBNBCommand.form_key(args[0], args[1])
        if len(args) < expected:
            if len(args) == 0:
                # 0 args means missing class
                return HBNBCommand.class_missing_err

            elif len(args) == 1:
                if HBNBCommand.class_exists(args[0]) is False:
                    # if only one arg, check if class exists

                    return HBNBCommand.class_ntexist_err

                else:
                    # if class exists, we're missing instance id

                    return HBNBCommand.instance_id_missing_err

            elif len(args) == 2:
                # if at least 2 args check if class exists
                # then check if id is valid
                if (HBNBCommand.class_exists(args[0]) is False):

                    return HBNBCommand.class_ntexist_err

                if (HBNBCommand.instance_exists(obj_key) is False):

                    return HBNBCommand.no_instance_found_err
                else:
                    # if id is valid, we're missing attribute name

                    return HBNBCommand.attr_name_missing_err

            elif (len(args) == 3):
                # if 3 args, check if class and attr_id exists
                if (HBNBCommand.class_exists(args[0]) is False):
                    return HBNBCommand.class_ntexist_err

                if (HBNBCommand.instance_exists(obj_key) is False):
                    return HBNBCommand.no_instance_found_err

                # if only 3 arguments, attr value is missing

                return HBNBCommand.value_missing_err

        elif len(args) >= expected:
            if HBNBCommand.class_exists(args[0]) is False:
                # correct number of args,
                # so check if class exists
                return HBNBCommand.class_ntexist_err
            elif (expected >= 2 and
                  HBNBCommand.instance_exists(obj_key) is False):
                # If we have an id but id is invalid
                # Then return an error
                return HBNBCommand.no_instance_found_err
            else:
                # If no errors found, return no error
                return None

    def class_exists(class_name):
        """ Checks if class class_name exists """
        if class_name not in HBNBCommand.classes:
            return False
        else:
            return True

    def instance_exists(obj_key):
        """ Checks if instance exists with obj_key given """
        if obj_key not in models.storage.all():
            return False
        else:
            return True

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
