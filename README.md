# AirBnB Clone - The Console

![This is an image](https://docs.github.com/assets/cb-319648/images/help/writing/image-rendered.png)

## Description of the Project

This is the first out of a four part project assigned by Holberton School
that recreates a simple copy of the Airbnb website. The Console is a
command interpreter that manipulates data without a visual interface.

## Description of the Command Interpreter

The Command Interpreter allows us to manage objects while also storing them to a JSON file.
This means we will be creating, updating, or even destroying objects and when we close and run
the program again, the data will reload as it was in the previous session.

  * **How to start it:**  run the executable file console.py
```
./console.py
```
  * **How to use its commands:**

     | Command       |  Description                                                       |
     |     :---:     | -----------------------------------------------------------------  |
     | all           | prints string representation of all objects of a certain class     |
     | create        | creates a new instance of class provided as argument               |
     | destroy       | deletes an instance based on class name and id                     |
     | help          | shows list of commands and how to use help command                 |
     | help \<topic\>  | provides info on specific command                                  |
     | quit or EOF   | exits the program                                                  |
     | show          | prints string representation of an instance from class name and id |

## Examples

#### all command:
```
(hbnb) all
["[BaseModel] (b15e3b32-6b22-4645-83be-aa7cdb5869e6) {'id': 'b15e3b32-6b22-4645-83be-aa7cdb5869e6',
'created_at': datetime.datetime(2022, 3, 6, 0, 44, 18, 116779), 'updated_at':
datetime.datetime(2022, 3, 6, 0, 44, 18, 116786), 'name': 'My_First_Model', 'my_number': 89}",
"[BaseModel] (eff2456c-1afc-4627-83d0-e97b97adb066) {'id': 'eff2456c-1afc-4627-83d0-e97b97adb066',
'created_at': datetime.datetime(2022, 3, 6, 0, 44, 44, 58993), 'updated_at': 
datetime.datetime(2022, 3, 6, 0, 44, 44, 58996), 'name': 'My_First_Model', 'my_number': 89}"]
```
#### create command:
```
(hbnb) create User
378b55e1-8a4d-4ea3-9b23-06bfdb24a0af
```

#### destroy command:
```
(hbnb) destroy User 378b55e1-8a4d-4ea3-9b23-06bfdb24a0af
```
#### help command:
```
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  all  create  destroy  help  quit  show

Undocumented commands:
======================
printkey  showall
```
####  help \<topic\> command:
```
(hbnb) help all
 prints string representation of all objects
        from a certain class (or all objects if no class
        is specified
```
####  quit or EOF command:
```
(hbnb) quit
vagrant@ubuntu-focal:~/AirBnB_clone$
```
####  show command:
```
(hbnb) show User 378b55e1-8a4d-4ea3-9b23-06bfdb24a0af
[User] (378b55e1-8a4d-4ea3-9b23-06bfdb24a0af) {'id': '378b55e1-8a4d-4ea3-9b23-06bfdb24a0af',
'created_at': datetime.datetime(2022, 3, 6, 0, 49, 55, 811711), 'updated_at':
datetime.datetime(2022, 3, 6, 0, 49, 55, 811711)}
```
