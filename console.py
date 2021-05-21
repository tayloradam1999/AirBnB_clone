#!/usr/bin/python3
"""
    Command interpreter for AnA-BnB
"""
import cmd
import sys
import os
import inspect
import shlex
from models.base_model import BaseModel
import models


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

    def do_create(self, arg):
        """Creates a new instance of BaseModel, saves it to JSON file
            and prints the id"""
        if arg is None or arg == "":
            print ("** class name missing **")
        elif arg != "BaseModel":
            print ("** class doesn't exist **")
        else:
            my_model = BaseModel()
            my_model.save()
            print (my_model.id)

    def do_show(self, arg):
        """Prints the string representation of an instance based
            on the class name and id"""
        if arg is None or arg == "":
            print ("** class name missing **")
        elif arg.split(" ")[0] != "BaseModel":
            print ("** class doesn't exist **")
        elif " " not in arg:
            print ("** instance id missing **")
        elif arg.replace(" ", ".") not in models.storage.all():
            print ("** no instance found **")
        else:
            obj = models.storage.all()[arg.replace(" ", ".")]
            print (obj)

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id
            (save the change into the JSON file)"""
        if arg is None or arg == "":
            print ("** class name missing **")
        elif arg.split(" ")[0] != "BaseModel":
            print ("** class doesn't exist **")
        elif " " not in arg:
            print ("** instance id missing **")
        elif arg.replace(" ", ".") not in models.storage.all():
            print ("** no instance found **")
        else:
            models.storage.remove(arg.replace(" ", "."))

    def do_all(self, arg):
        """Prints all string representation of all instances
            based or not on the class name"""
        if arg != "BaseModel" and arg != "":
            print ("** class doesn't exist **")
        else:
            print (models.storage.all())

    def do_update(self, arg):
        """Updates an instance based on the class name and id by
        adding or updating attribute (save the change into the JSON file)"""
        a = shlex.split(arg)
        if len(a) == 0:
            print ("** class name missing **")
        elif a[0] != "BaseModel":
            print ("** class doesn't exist **")
        elif len(a) < 2:
            print ("** instance id missing **")
        elif "{}.{}".format(a[0], a[1]) not in models.storage.all():
            print ("** no instance found **")
        elif len(a) < 3:
            print ("** attribute name missing **")
        elif len(a) < 4:
            print ("** value missing **")
        else:
            k = "{}.{}".format(a[0], a[1])
            models.storage.update(models.storage.all()[k], a[2], a[3])

if __name__ == '__main__':
    HBNBCommand().cmdloop()
