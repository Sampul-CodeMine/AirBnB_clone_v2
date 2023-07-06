#!/usr/bin/python3
"""Importing some Standard modules and modules from our packages"""
import cmd
import sys
from shlex import split
from models import storage
from datetime import datetime
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

"""
This is a Python class that will act as an interface for the first phase
of the AirBnB Clone project.
"""


class HBNBCommand(cmd.Cmd):
    """
    This is a class modelling the inteface (CLI) for AirBnB Clone project.
    """
    
    __classes = {
        "BaseModel",
        "User",
        "State",
        "City",
        "Amenity",
        "Place",
        "Review"
    }
    
    """Specify the prompt for the CLI"""
    prompt = '(hbnb) ' if sys.__stdin__.isatty() else ''
    
    def preloop(self) -> None:
        """Prints if isatty is false"""
        if not sys.__stdin__.isatty():
            print('(hbnb) ')

    def emptyline(self) -> None:
        """Method that does nothing when the ENTER key is pressed without a
        command."""
        pass

    def do_quit(self, line) -> bool:
        """Quit command to exit the program."""
        return True

    def help_quit(self) -> None:
        """Display the help information for quit"""
        print("")
        print("The `quit` command issues a command to quit the CLI.\n")
        print("Usage:\n(hbnb) quit\n")

    def do_EOF(self, line) -> bool:
        """EOF signal to exit the program, returns True and breaks loop."""
        print("")
        return True

    def help_EOF(self) -> None:
        """Displays the help information for EOF"""
        print("")
        print("The `EOF` command returns True to break the cmdloop", end=" ")
        print("and exits the CLI.\n")
        print("Usage:\n(hbnb) EOF\nor\n(hbnb) <CTRL + C>")
        print("or\n(hbnb) <CTRL + Z>\n")

    def do_create(self, line) -> None:
        """Public instance method that creates new instance of a class, save
        it to a JSON file and print the `id` of the instance"""
        try:
            if not line:
                raise SyntaxError()
            my_list = line.split(" ")

            kwargs = {}
            for i in range(1, len(my_list)):
                key, value = tuple(my_list[i].split("="))
                if value[0] == '"':
                    value = value.strip('"').replace("_", " ")
                else:
                    try:
                        value = eval(value)
                    except (SyntaxError, NameError):
                        continue
                kwargs[key] = value

            if kwargs == {}:
                obj = eval(my_list[0])()
            else:
                obj = eval(my_list[0])(**kwargs)
                storage.new(obj)
            print(obj.id)
            obj.save()

        except SyntaxError:
            print("** class name missing **")
        except NameError:
            print("** class doesn't exist **")

    def help_create(self) -> None:
        """Displays the help information for create"""
        print("")
        print("The `create` command creates an instance of a class, ", end="")
        print("saves it to the storage and prints out the ID of the", end=" ")
        print("instance created.\n")
        print("Models available includes:\n")
        print("\tAmenity\n\tBaseModel\n\tCity\n\tPlace\n\tReview\n\t", end="")
        print("State\n\tUser\n")
        print("Usage:\n(hbnb) create User\n")

    def do_show(self, line) -> None:
        """Public instance method that displays the string instance of a
        class, based on the instance id and classname specified"""
        try:
            if not line:
                raise SyntaxError()
            my_list = line.split(" ")
            if my_list[0] not in self.__classes:
                raise NameError()
            if len(my_list) < 2:
                raise IndexError()
            objects = storage.all()
            key = my_list[0] + '.' + my_list[1]
            if key in objects:
                print(objects[key])
            else:
                raise KeyError()
        except SyntaxError:
            print("** class name missing **")
        except NameError:
            print("** class doesn't exist **")
        except IndexError:
            print("** instance id missing **")
        except KeyError:
            print("** no instance found **")

    def help_show(self) -> None:
        """Displays the help information for show"""
        print("")
        print("The `show` command displays the details and string", end=" ")
        print("representation of an instance based on class name", end=" ")
        print("and instance id provided.\n")
        print("Usage:\n(hbnb) show User 51a155c1-214a-4923-8d53-523900fed722")
        print("")

    def do_destroy(self, line) -> None:
        """Public instance method that deletes the instance of a class,
        based on the instance id and classname specified"""
        try:
            if not line:
                raise SyntaxError()
            my_list = line.split(" ")
            if my_list[0] not in self.__classes:
                raise NameError()
            if len(my_list) < 2:
                raise IndexError()
            objects = storage.all()
            key = my_list[0] + '.' + my_list[1]
            if key in objects:
                del objects[key]
                storage.save()
            else:
                raise KeyError()
        except SyntaxError:
            print("** class name missing **")
        except NameError:
            print("** class doesn't exist **")
        except IndexError:
            print("** instance id missing **")
        except KeyError:
            print("** no instance found **")

    def help_destroy(self) -> None:
        """Displays the help information for destroy"""
        print("")
        print("The `destroy` command deletes the details of an ", end="")
        print("instance based on class name and instance id provided.\n")
        print("Usage:\n(hbnb) destroy User 51a155c1-214a-4923-8d53-52fed22\n")

    def do_all(self, line) -> None:
        """Public instance method that displays the string instance of all
        the instances of a class based on the classname specified or no
        classname specified"""
        if not line:
            o = storage.all()
            print([o[k].__str__() for k in o])
            return
        try:
            args = line.split(" ")
            if args[0] not in self.__classes:
                raise NameError()

            o = storage.all(eval(args[0]))
            print([o[k].__str__() for k in o])

        except NameError:
            print("** class doesn't exist **")

    def help_all(self) -> None:
        """Updates the help for all"""
        print("")
        print("The `all` command displays the string representation", end="")
        print(" of all class instances present in the storage.\n")
        print("Usage:\n(hbnb) all User\nor\n(hbnb) User.all()\n")

    def do_update(self, line) -> None:
        """Public instance method that updates a specified instance of a class
        using the id and either adding more attributes or updating an
        attribute"""
        try:
            if not line:
                raise SyntaxError()
            my_list = split(line, " ")
            if my_list[0] not in self.__classes:
                raise NameError()
            if len(my_list) < 2:
                raise IndexError()
            objects = storage.all()
            key = my_list[0] + '.' + my_list[1]
            if key not in objects:
                raise KeyError()
            if len(my_list) < 3:
                raise AttributeError()
            if len(my_list) < 4:
                raise ValueError()
            v = objects[key]
            try:
                v.__dict__[my_list[2]] = eval(my_list[3])
            except Exception:
                v.__dict__[my_list[2]] = my_list[3]
                v.save()
        except SyntaxError:
            print("** class name missing **")
        except NameError:
            print("** class doesn't exist **")
        except IndexError:
            print("** instance id missing **")
        except KeyError:
            print("** no instance found **")
        except AttributeError:
            print("** attribute name missing **")
        except ValueError:
            print("** value missing **")

    def help_update(self) -> None:
        """Updates the help for update"""
        print("")
        print("The `update` command update a specified instance of a", end="")
        print(" using the class name and the ID of the instance, and", end="")
        print(" and the specifying the attribute to update or adding", end="")
        print(" a new attribute plus the value.\n")
        print("Usage:\n(hbnb) update User 1234-5678 email 'test@oop.com'\n")

    def count(self, line) -> None:
        """Public instance method that counts the number of instances of a
        class"""
        counter = 0
        try:
            my_list = split(line, " ")
            if my_list[0] not in self.__classes:
                raise NameError()
            objects = storage.all()
            for key in objects:
                name = key.split('.')
                if name[0] == my_list[0]:
                    counter += 1
            print(counter)
        except NameError:
            print("** class doesn't exist **")

    def help_count(self) -> None:
        """Updates the help for count"""
        print("")
        print("The `count` command displays the number of instances", end="")
        print(" of a specified class found in the json file.", end="\n")
        print("Usage:\n(hbnb) count User'\nor\n(hbnb) User.count()\n")

    def strip_clean(self, args):
        """strips the argument and return a string of command
        Args:
            args: input list of args
        Return:
            returns string of argumetns
        """
        new_list = []
        new_list.append(args[0])
        try:
            my_dict = eval(
                args[1][args[1].find('{'):args[1].find('}')+1])
        except Exception:
            my_dict = None
        if isinstance(my_dict, dict):
            new_str = args[1][args[1].find('(')+1:args[1].find(')')]
            new_list.append(((new_str.split(", "))[0]).strip('"'))
            new_list.append(my_dict)
            return new_list
        new_str = args[1][args[1].find('(')+1:args[1].find(')')]
        new_list.append(" ".join(new_str.split(", ")))
        return " ".join(i for i in new_list)

    def default(self, line):
        """This public instance method is called when an invalid command is
        given. If this is not overwritten, it displays an error, but we will
        be handling invalid commands before returning False if command not
        found."""
        my_list = line.split('.')
        if len(my_list) >= 2:
            if my_list[1] == "all()":
                self.do_all(my_list[0])
            elif my_list[1] == "count()":
                self.count(my_list[0])
            elif my_list[1][:4] == "show":
                self.do_show(self.strip_clean(my_list))
            elif my_list[1][:7] == "destroy":
                self.do_destroy(self.strip_clean(my_list))
            elif my_list[1][:6] == "update":
                args = self.strip_clean(my_list)
                if isinstance(args, list):
                    obj = storage.all()
                    key = args[0] + ' ' + args[1]
                    for k, v in args[2].items():
                        self.do_update(key + ' "{}" "{}"'.format(k, v))
                else:
                    self.do_update(args)
        else:
            cmd.Cmd.default(self, line)


if __name__ == '__main__':
    commnd = HBNBCommand()
    commnd.cmdloop()
