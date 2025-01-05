#!/usr/bin/python3
"""Command interpreter for Holberton AirBnB project"""

import cmd
import shlex
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """Command interpreter class"""

    prompt = '(hbnb) '
    classes = {
        'BaseModel': BaseModel,
        'User': User,
        'Place': Place,
        'State': State,
        'City': City,
        'Amenity': Amenity,
        'Review': Review
    }

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        return True

    def emptyline(self):
        """Empty line"""
        pass

    def do_create(self, arg):
        """Creates a new instance of a class with given parameters

        Usage: create <Class name> <param 1> <param 2> <param 3>...
        Params should be in the format: <key name>=<value>
        """
        if not arg:
            print("** class name missing **")
            return

        args = shlex.split(arg)
        class_name = args[0]

        if class_name not in self.classes:
            print("** class doesn't exist **")
            return

        new_instance = self.classes[class_name]()

        for param in args[1:]:
            if '=' not in param:
                continue

            key, value = param.split('=', 1)

            if value.startswith('"') and value.endswith('"'):
                value = value[1:-1]  # Remove surrounding quotes
                value = value.replace('_', ' ') \
                             .replace('"', '\\"')  # Handle escaped quotes
            elif '.' in value:
                try:
                    value = float(value)
                except ValueError:
                    continue
            else:
                try:
                    value = int(value)
                except ValueError:
                    continue

            if hasattr(new_instance, key):
                setattr(new_instance, key, value)

        new_instance.save()
        print(new_instance.id)

    def do_show(self, arg):
        """Prints string representation of an instance"""
        args = shlex.split(arg)
        if len(args) == 0:
            print("** class name missing **")
            return
        if args[0] not in self.classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = "{}.{}".format(args[0], args[1])
        if key not in storage.all():
            print("** no instance found **")
            return
        print(storage.all()[key])

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        args = shlex.split(arg)
        if len(args) == 0:
            print("** class name missing **")
            return
        if args[0] not in self.classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = "{}.{}".format(args[0], args[1])
        if key not in storage.all():
            print("** no instance found **")
            return
        del storage.all()[key]
        storage.save()

    def do_all(self, arg):
        """Prints string representation of all instances"""
        args = shlex.split(arg)
        obj_list = []
        if len(args) == 0:
            for value in storage.all().values():
                obj_list.append(str(value))
        elif args[0] in self.classes:
            for key, value in storage.all().items():
                if key.split('.')[0] == args[0]:
                    obj_list.append(str(value))
        else:
            print("** class doesn't exist **")
            return
        print(obj_list)

    def do_update(self, arg):
        """Updates an instance based on the class name and id"""
        args = shlex.split(arg)
        if len(args) == 0:
            print("** class name missing **")
            return
        if args[0] not in self.classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = "{}.{}".format(args[0], args[1])
        if key not in storage.all():
            print("** no instance found **")
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        if len(args) < 4:
            print("** value missing **")
            return

        instance = storage.all()[key]
        attr_name = args[2]
        attr_value = args[3]

        try:
            attr_value = eval(attr_value)
        except (NameError, SyntaxError):
            pass

        setattr(instance, attr_name, attr_value)
        instance.save()

    def default(self, arg):
        """Handle class commands: <class name>.<command>()"""
        parts = arg.split('.')
        if len(parts) != 2:
            return cmd.Cmd.default(self, arg)

        class_name = parts[0]
        if class_name not in self.classes:
            return cmd.Cmd.default(self, arg)

        command = parts[1].split('(')[0]
        method_name = 'do_' + command
        if not hasattr(self, method_name):
            return cmd.Cmd.default(self, arg)

        if command == 'all':
            return self.do_all(class_name)
        elif command == 'count':
            count = sum(
                1 for key in storage.all() if key.startswith(class_name + '.')
            )
            print(count)
            return
        elif command == 'show':
            id_arg = parts[1].split('(')[1].rstrip(')').strip('"\'')
            return self.do_show(f"{class_name} {id_arg}")
        elif command == 'destroy':
            id_arg = parts[1].split('(')[1].rstrip(')').strip('"\'')
            return self.do_destroy(f"{class_name} {id_arg}")
        elif command == 'update':
            args = parts[1].split('(')[1].rstrip(')').split(',')
            if not args:
                return cmd.Cmd.default(self, arg)
            id_arg = args[0].strip('" ')
            if len(args) < 2:
                return self.do_update(f"{class_name} {id_arg}")
            attr_name = args[1].strip('" ')
            if len(args) < 3:
                return self.do_update(f"{class_name} {id_arg} {attr_name}")
            attr_value = args[2].strip('" ')
            return self.do_update(
                f"{class_name} {id_arg} {attr_name} {attr_value}"
            )


if __name__ == '__main__':
    HBNBCommand().cmdloop()
