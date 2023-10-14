#!/usr/bin/python3
import cmd
import re
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models import storage
from models.amenity import Amenity
from models.review import Review


class HBNBCommand(cmd.Cmd):
    '''class for a commandline interpreter'''

    prompt = '(hbnb) '
    valid_classes = ['BaseModel',
                     'User',
                     'City',
                     'State',
                     'Amenity',
                     'Place',
                     'Reviews'
                     ]

    def do_create(self, line):
        '''Usage: create class_name'''
        if not line:
            print('** class name missing **')
        else:
            class_name = line.strip()
            if class_name in self.valid_classes:
                new = eval(class_name)()
                new.save()
                print(new.id)
            else:
                print("** class doesn't exist **")

    def do_show(self, line):
        '''Usage: show class_name class_id
        eg show BaseModel 1234-1234-1234
        '''
        if not line:
            print('** class name missing **')
        else:
            args = line.split()
            if args[0] not in self.valid_classes:
                print("** class doesn't exist **")
            else:
                if len(args) < 2:
                    print('** instance id missing **')
                else:
                    key = f'{args[0]}.{args[1]}'
                    all_obj = storage.all()

                    if key in all_obj:
                        print(all_obj[key])
                    else:
                        print('** no instance found **')

    def do_destory(self, line):
        '''Usage destory class_name class_id
        destroy BaseModel 1234-1234-1234
        '''
        if not line:
            print('** class name missing **')
        else:
            args = line.split()
            if args[0] not in self.valid_classes:
                print("** class doesn't exist **")
            else:
                if len(args) < 2:
                    print("** instance id missing **")
                else:
                    key = f'{args[0]}.{args[1]}'
                    all_obj = storage.all()

                    if key in all_obj:
                        del all_obj[key]
                    else:
                        print('** no instance found **')
                    storage.save()

    def do_all(self, line):
        ''' Usage all [class_name]
        '''
        instances = []
        if not line:
            all_obj = storage.all()
            for value in all_obj.values():
                instances.append(value)
        else:
            class_name = line.strip()
            all_obj = storage.all()
            for key, value in all_obj.items():
                cls_name, cls_id = key.split('.')
                if class_name == cls_name:
                    instances.append(value)

        for instance in instances:
            print(instance)

    def do_count(self, line):
        count = 0

        if not line:
            for key in storage.all():
                count += 1

        else:
            class_name = line.strip()
            if class_name not in self.valid_classes:
                print("** class doesn't exist **")
                return
            for key in storage.all():
                cls_name, cls_id = key.split('.')
                if class_name == cls_name:
                    count += 1
        print(count)

    def do_update(self, line):
        '''update <class name> <id> <attribute name> "<attribute value>
        update BaseModel 1234-1234-1234 email "aibnb@mail.com"
        '''
        if not line:
            print('** class name missing **')
            return
        args = line.split()
        class_name = args[0]
        if class_name not in self.valid_classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        instance_id = args[1]
        key = f'{class_name}.{instance_id}'
        if key not in storage.all():
            print("** no instance found **")
            return

        instance = storage.all()[key]

        if len(args) < 3:
            print('** attribute name missing **')
            return
        attr_name = args[2]
        if len(args) < 4:
            print('** value missing **')
            return
        attr_value = args[3]

        # check if the instance has the specifies attribute
        if hasattr(instance, attr_name):
            attr_type = type(getattr(instance, attr_name))
            setattr(instance, attr_name, attr_type(attr_value))
            instance.save()
        else:
            print('** no attribute found **')

    def do_EOF(self, line):
        '''Exit the program using Ctrl-D (EOF)'''
        print()
        return True

    def default(self, line):
        '''handle User.all() command'''
        if re.match(r'^(\S+)\.all\(.*\)$', line):
            match = re.match(r'^(\S+)\.all\(.*\)$', line)
            class_name = match.group(1)
            self.do_all(class_name)
        elif re.match(r'^(\S+)\.count\(.*\)$', line):
            match = re.match(r'^(\S+)\.count\(.*\)$', line)
            class_name = match.group(1)
            self.do_count(class_name)
        elif re.match(r'^(\S+)\.show\((.*)\)$', line):
            match = re.match(r'^(\S+)\.show\((.*\))$', line)
            class_name = match.group(1)
            class_id = match.group(2)
            class_id = class_id.strip(" '\"()")
            args = class_name + ' ' + class_id
            self.do_show(args)
        elif re.match(r'^(\S+)\.destory\((.*)\)$', line):
            match = re.match(r'^(\S+)\.destory\((.*\))$', line)
            class_name = match.group(1)
            class_id = match.group(2)
            class_id = class_id.strip(" '\"()")
            args = class_name + ' ' + class_id
            self.do_destory(args)
        elif re.match(r'^(\S+)\.destory\((.*),(.*)\)$', line):
            match = re.match(r'^(\S+)\.destory\((.*\))$', line)
            class_name = match.group(1)
            class_id = match.group(2)
            args = match.group(3)
            inst_attr, inst_val = args.split()
            class_id = class_id.strip(" '\"()")
            inst_attr = inst_attr.strip(" '\"()")
            inst_val = inst_val.strip(" '\"()")
            args = class_name + ' ' + class_id + ' ' + inst_attr + inst_val
            self.do_destory(args)

    def do_quit(self, line):
        '''Quit the commandline'''
        return True

    def help_quit(self):
        '''Help for the quit command'''
        print('Quit command to exit the program')
        print()

    def emptyline(self):
        '''Do nothing on empty line'''
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
