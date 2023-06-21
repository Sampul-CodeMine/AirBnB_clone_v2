<center> <h1>HBNB - The Console</h1> </center>

This repository contains the initial stage of a student project to build a clone of the AirBnB website. This stage implements a backend interface, or console, to manage program data. Console commands allow the user to create, update, and destroy objects, as well as manage file storage. Using a system of JSON serialization/deserialization, storage is persistent between sessions.

---

<center><h3>Repository Contents by Project Task</h3> </center>

| Tasks | Files | Description |
| ----- | ----- | ------ |
| 0: Authors/README File | [AUTHORS](https://github.com/Sampul-CodeMine/AirBnB_clone_v2/blob/dev/AUTHORS) | Project authors |
| 1: Pep8 | N/A | All code is pep8 compliant|
| 2: Unit Testing | [/tests](https://github.com/Sampul-CodeMine/AirBnB_clone_v2/tree/dev/tests) | All class-defining modules are unittested |
| 3. Make BaseModel | [/models/base_model.py](https://github.com/Sampul-CodeMine/AirBnB_clone_v2/blob/dev/models/base_model.py) | Defines a parent class to be inherited by all model classes|
| 4. Update BaseModel w/ kwargs | [/models/base_model.py](https://github.com/Sampul-CodeMine/AirBnB_clone_v2/blob/dev/models/base_model.py) | Add functionality to recreate an instance of a class from a dictionary representation|
| 5. Create FileStorage class | [/models/engine/file_storage.py](https://github.com/Sampul-CodeMine/AirBnB_clone_v2/blob/dev/models/engine/file_storage.py) [/models/_ _init_ _.py](https://github.com/Sampul-CodeMine/AirBnB_clone_v2/blob/dev/models/__init__.py) [/models/base_model.py](https://github.com/Sampul-CodeMine/AirBnB_clone_v2/blob/dev/models/base_model.py) | Defines a class to manage persistent file storage system|
| 6. Console 0.0.1 | [console.py](https://github.com/Sampul-CodeMine/AirBnB_clone_v2/blob/dev/console.py) | Add basic functionality to console program, allowing it to quit, handle empty lines and ^D |
| 7. Console 0.1 | [console.py](https://github.com/Sampul-CodeMine/AirBnB_clone_v2/blob/dev/console.py) | Update the console with methods allowing the user to create, destroy, show, and update stored data |
| 8. Create User class | [console.py](https://github.com/Sampul-CodeMine/AirBnB_clone_v2/blob/dev/console.py) [/models/engine/file_storage.py](https://github.com/Sampul-CodeMine/AirBnB_clone_v2/blob/dev/models/engine/file_storage.py) [/models/user.py](https://github.com/Sampul-CodeMine/AirBnB_clone_v2/blob/dev/models/user.py) | Dynamically implements a user class |
| 9. More Classes | [/models/user.py](https://github.com/Sampul-CodeMine/AirBnB_clone_v2/blob/dev/models/user.py) [/models/place.py](https://github.com/Sampul-CodeMine/AirBnB_clone_v2/blob/dev/models/place.py) [/models/city.py](https://github.com/Sampul-CodeMine/AirBnB_clone_v2/blob/dev/models/city.py) [/models/amenity.py](https://github.com/Sampul-CodeMine/AirBnB_clone_v2/blob/dev/models/amenity.py) [/models/state.py](https://github.com/Sampul-CodeMine/AirBnB_clone_v2/blob/dev/models/state.py) [/models/review.py](https://github.com/Sampul-CodeMine/AirBnB_clone_v2/blob/dev/models/review.py) | Dynamically implements more classes |
| 10. Console 1.0 | [console.py](https://github.com/Sampul-CodeMine/AirBnB_clone_v2/blob/dev/console.py) [/models/engine/file_storage.py](https://github.com/Sampul-CodeMine/AirBnB_clone_v2/blob/dev/models/engine/file_storage.py) | Update the console and file storage system to work dynamically with all  classes update file storage |
<br>

We are aspiring to be Web developers and Software Engineers. At **ALX SE Programme**, one of the requirements that makes you standout and become a formidable Software Engineer, is to create an _AirBnB Clone_. You do not just roll out these solutions but rather, approach it one at a time. Our first step to developing this web application is to create a Command Line Interpreter  (CLI) to help us manage our projects' objects. This step is very important because we will be building and including static and dynamic contents: HTML/CSS/JS templates, DB storage, File Storage, API (Application Proramming Interface) and Front-End Integration.

## What is a CLI (Command Line Interpreter)?

A `CLI` is a text-based User-Interface (`UI`) that runs commands and programes. It manages  computer files and interact with the computer. Do you remember the `Shell`? It’s exactly the same but limited to a specific use-case. In our case, we want to be able to manage the objects of our project:

- Create a new object (ex: a new User or a new Place)
- Retrieve an object from a file, a database etc…
- Do operations on objects (count, compute stats, etc…)
- Update attributes of an object
- Destroy an object

## Learning Objectives

During and after the cause of this project, we will be able to do the following:

- Know how to create a Python package
- Know how to create a CLI in Python using the `cmd module`
- Know what is `Unit testing` and how to implement it in a large project
- Know how to `serialize` and `deserialize` a Class
- Know how to write and read a `JSON` file
- Know how to manage `datetime`
- Know what is an `UUID`
- Know what is `*args` and how to use it
- Know what is `**kwargs` and how to use it
- Know how to handle named arguments in a function

## Requirements

### Python Scripts

- Allowed editors: `vi`, `vim`, `emacs`
- All your files will be interpreted/compiled on `Ubuntu 20.04 LTS` using `python3 (version 3.8.5)`
- All your files should end with a new line
- The first line of all your files should be exactly `#!/usr/bin/python3`
- A `README.md` file, at the root of the folder of the project, is mandatory
- Your code should use the `pycodestyle (version 2.8.*)`
- All your files must be executable
- The length of your files will be tested using wc
- All your modules should have a documentation `(python3 -c 'print(__import__("my_module").__doc__)')`
- All your classes should have a documentation `(python3 -c 'print(__import__("my_module").MyClass.__doc__)')`
- All your functions (inside and outside a class) should have a documentation `(python3 -c 'print(__import__("my_module").my_function.__doc__)'` and `python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)')`
- A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)

### Python Unit Tests

- Allowed editors: `vi`, `vim`, `emacs`
- All your files should end with a new line
- All your test files should be inside a folder `./tests`
- You have to use the `unittest` module
- All your test files should be python files `(extension: .py)`
- All your test files and folders should start by `test_`
- Your file organization in the tests folder should be the same as your project
- > e.g., For `models/base_model.py`, unit tests must be in: `tests/test_models/test_base_model.py`
- > e.g., For `models/user.py`, unit tests must be in: `tests/test_models/test_user.py`
- All your tests should be executed by using this command: `python3 -m unittest discover tests`
- You can also test file by file by using this command: `python3 -m unittest tests/test_models/test_base_model.py`
- All your modules should have a documentation `(python3 -c 'print(__import__("my_module").__doc__)')`
- All your classes should have a documentation `(python3 -c 'print(__import__("my_module").MyClass.__doc__)')`
- All your functions (inside and outside a class) should have a documentation `(python3 -c 'print(__import__("my_module").my_function.__doc__)'` and `python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)')`

## Program Build-up

We will be building this **AirBnB Clone** web application phase by phase using the **SDLC (Software Development Life Cycle)**

- Problem Definition / Plan
- Solution Requirements and Analysis
- Solution Design using algorithms, flowcharts, and pseudocodes
- Implementation using a choice Programming Language
- Solution Testing
- Deployment
- Maintenance

> _Note: The problem definition, requirements are already done for us. We only need to design a clone of the original using our own design, implement our code with our choice programming language which in this project is **Python Programming Language** and test our implementations using **Python's unittest module**._

## Classes Needed in this Project

|   Classes -->  | BaseModel | User | State | City | Amenity | Place | Review | FileStorage |
| --- | --------- | ----------- | -----| ----- | -----| ------- | ----- | ------ |
| **Public Instance Attributes** | `id`<br>`created_at`<br>`updated_at` | Inherits from `BaseModel` | Inherits from `BaseModel` | Inherits from `BaseModel` | Inherits from `BaseModel` | Inherits from `BaseModel` | Inherits from `BaseModel` | --- |
| **Public Instance Methods** |`save()`<br>`to_dict()` | --- | --- | --- | --- | --- | --- | `all()`<br>`new()`<br>`save()`<br>`reload()` |
| **Public Class Attributes** | --- | `email`<br>`first_name`<br>`last_name`<br>`password`| `name` | `name`<br>`state_id` | `name` | `city_id`<br>`user_id`<br>`name`<br>`description`<br>`number_rooms`<br>`number_bathrooms`<br>`max_guest`<br>`price_by_night`<br>`latitude`<br>`longitude`<br>`amenity_ids` | `place_id`<br>`user_id`<br>`text` | --- |
| **Private Class Attributes** | --- | --- | --- | --- | --- | --- | --- | `__file_path`<br>`__objects` |

<br>

<center> <h2>General Use</h2> </center>

1. First clone this repository.

3. Once the repository is cloned locate the "console.py" file and run it as follows:
```
/AirBnB_clone_v2$ ./console.py
```
4. When this command is run the following prompt should appear:
```
(hbnb)
```
5. This prompt designates you are in the "HBnB" console. There are a variety of commands available within the console program.

##### Commands
    * create - Creates an instance based on given class

    * destroy - Destroys an object based on class and UUID

    * show - Shows an object based on class and UUID

    * all - Shows all objects the program has access to, or all objects of a given class

    * update - Updates existing attributes an object based on class name and UUID

    * quit - Exits the program (EOF will as well)


##### Alternative Syntax
Users are able to issue a number of console command using an alternative syntax:

	Usage: <class_name>.<command>([<id>[name_arg value_arg]|[kwargs]])
Advanced syntax is implemented for the following commands: 

    * all - Shows all objects the program has access to, or all objects of a given class

	* count - Return number of object instances by class

    * show - Shows an object based on class and UUID

	* destroy - Destroys an object based on class and UUID

    * update - Updates existing attributes an object based on class name and UUID

<br>
<br>
<center> <h2>Examples</h2> </center>
<h3>Primary Command Syntax</h3>

###### Example 0: Create an object
Usage: create <class_name>
```
(hbnb) create BaseModel
```
```
(hbnb) create BaseModel
3aa5babc-efb6-4041-bfe9-3cc9727588f8
(hbnb)                   
```
###### Example 1: Show an object
Usage: show <class_name> <_id>

```
(hbnb) show BaseModel 3aa5babc-efb6-4041-bfe9-3cc9727588f8
[BaseModel] (3aa5babc-efb6-4041-bfe9-3cc9727588f8) {'id': '3aa5babc-efb6-4041-bfe9-3cc9727588f8', 'created_at': datetime.datetime(2020, 2, 18, 14, 21, 12, 96959), 
'updated_at': datetime.datetime(2020, 2, 18, 14, 21, 12, 96971)}
(hbnb)  
```
###### Example 2: Destroy an object
Usage: destroy <class_name> <_id>
```
(hbnb) destroy BaseModel 3aa5babc-efb6-4041-bfe9-3cc9727588f8
(hbnb) show BaseModel 3aa5babc-efb6-4041-bfe9-3cc9727588f8
** no instance found **
(hbnb)   
```
###### Example 3: Update an object
Usage: update <class_name> <_id>
```
(hbnb) update BaseModel b405fc64-9724-498f-b405-e4071c3d857f first_name "person"
(hbnb) show BaseModel b405fc64-9724-498f-b405-e4071c3d857f
[BaseModel] (b405fc64-9724-498f-b405-e4071c3d857f) {'id': 'b405fc64-9724-498f-b405-e4071c3d857f', 'created_at': datetime.datetime(2020, 2, 18, 14, 33, 45, 729889), 
'updated_at': datetime.datetime(2020, 2, 18, 14, 33, 45, 729907), 'first_name': 'person'}
(hbnb)
```
<h3>Alternative Syntax</h3>

###### Example 0: Show all User objects
Usage: <class_name>.all()
```
(hbnb) User.all()
["[User] (99f45908-1d17-46d1-9dd2-b7571128115b) {'updated_at': datetime.datetime(2020, 2, 19, 21, 47, 34, 92071), 'id': '99f45908-1d17-46d1-9dd2-b7571128115b', 'created_at': datetime.datetime(2020, 2, 19, 21, 47, 34, 92056)}", "[User] (98bea5de-9cb0-4d78-8a9d-c4de03521c30) {'updated_at': datetime.datetime(2020, 2, 19, 21, 47, 29, 134362), 'id': '98bea5de-9cb0-4d78-8a9d-c4de03521c30', 'created_at': datetime.datetime(2020, 2, 19, 21, 47, 29, 134343)}"]
```

###### Example 1: Destroy a User
Usage: <class_name>.destroy(<_id>)
```
(hbnb) User.destroy("99f45908-1d17-46d1-9dd2-b7571128115b")
(hbnb)
(hbnb) User.all()
(hbnb) ["[User] (98bea5de-9cb0-4d78-8a9d-c4de03521c30) {'updated_at': datetime.datetime(2020, 2, 19, 21, 47, 29, 134362), 'id': '98bea5de-9cb0-4d78-8a9d-c4de03521c30', 'created_at': datetime.datetime(2020, 2, 19, 21, 47, 29, 134343)}"]
```
###### Example 2: Update User (by attribute)
Usage: <class_name>.update(<_id>, <attribute_name>, <attribute_value>)
```
(hbnb) User.update("98bea5de-9cb0-4d78-8a9d-c4de03521c30", name "Todd the Toad")
(hbnb)
(hbnb) User.all()
(hbnb) ["[User] (98bea5de-9cb0-4d78-8a9d-c4de03521c30) {'updated_at': datetime.datetime(2020, 2, 19, 21, 47, 29, 134362), 'id': '98bea5de-9cb0-4d78-8a9d-c4de03521c30', 'name': 'Todd the Toad', 'created_at': datetime.datetime(2020, 2, 19, 21, 47, 29, 134343)}"]
```
###### Example 3: Update User (by dictionary)
Usage: <class_name>.update(<_id>, <dictionary>)
```
(hbnb) User.update("98bea5de-9cb0-4d78-8a9d-c4de03521c30", {'name': 'Fred the Frog', 'age': 9})
(hbnb)
(hbnb) User.all()
(hbnb) ["[User] (98bea5de-9cb0-4d78-8a9d-c4de03521c30) {'updated_at': datetime.datetime(2020, 2, 19, 21, 47, 29, 134362), 'name': 'Fred the Frog', 'age': 9, 'id': '98bea5de-9cb0-4d78-8a9d-c4de03521c30', 'created_at': datetime.datetime(2020, 2, 19, 21, 47, 29, 134343)}"]
```
<br>

## How Program is Executed

### Your shell should work like this in interactive mode

```bash
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$
```

### But also in non-interactive mode: (like the Shell project in C)

```bash
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
```

## AirBnB Clone Console Usage

### How to Start The Console

The AirBnB Clone console can be run both interactively and non-interactively.

**Running in the Non-Interactive Mode**

```shell
$ echo "help" | python3 console.py
(hbnb)
Documented commands (type help <topic>):
========================================
EOF  all  create  destroy  help  quit  show  update

(hbnb)
$
```

or

```shell
$ echo "help" | ./console.py
(hbnb)
Documented commands (type help <topic>):
========================================
EOF  all  create  destroy  help  quit  show  update

(hbnb)
$
```

Alternatively, it can be run in interactive mode, run the file `console.py` by itself:

**Running in the Interactive Mode**

```shell
$ ./console.py
(hbnb)

```

or

```shell
$ python3 console.py
(hbnb)

```

In this README or guide, we will be making most of the documentation with the interactive mode.<br> When you execute the above command, it displays a prompt `(hbnb)`. This is the prompt required of the project and it awaits inputs from the user.

### **Quiting the Console**

To quit the console, you can type in any of the following:

- EOF
- quit

or do the following key combinations on your keyboard

- CMD+D (Unix) / CRTL+C (Windows)

```shell
(hbnb) quit
$

```

or

```shell
(hbnb) EOF
$

```

or

```shell
(hbnb) (CTRL+C)
$

```

### **Getting Help**

#### **To get help generally**

```shell

(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  all  create  destroy  help  quit  show  update

(hbnb)
```

#### **To get help for a particular command**

```shell

(hbnb) help all

The `all` command displays the string representation of all class instances present in the storage.

Usage:
(hbnb) all User
```

```shell
(hbnb) help update

The `update` command update a specified instance of a using the class name and the ID of the instance, and and the specifying the attribute to update or adding a new attribute plus the value.

Usage:
(hbnb) update User 1234-5678 email 'test@oop.com'

(hbnb)
```

Presently, we have nothing in the flat file database, We will create a New User and a BaseModel

```shell
(hbnb) all
[]
(hbnb)

```

Firstly, we have to get help on how to create an instance of a model and what models are available

```shell
$ ./console.py
(hbnb) help create

The `create` command creates an instance of a class, saves it to the storage and prints out the ID of the instance created.

Models available includes:

        Amenity
        BaseModel
        City
        Place
        Review
        State
        User

Usage:
(hbnb) create User

(hbnb)
```

To create a New User model, we type `create User` and it returns the ID of the User model created

 ```shell
 (hbnb) create User
97bf8455-58aa-4d65-a83e-32699de58bbb
(hbnb)
```

To display the details of the User model that was created, 

```shell
(hbnb) show User 97bf8455-58aa-4d65-a83e-32699de58bbb
[User] (97bf8455-58aa-4d65-a83e-32699de58bbb) {'id': '97bf8455-58aa-4d65-a83e-32699de58bbb', 'created_at': datetime.datetime(2023, 5, 13, 13, 16, 37, 181187), 'updated_at': datetime.datetime(2023, 5, 13, 13, 16, 37, 181187)}
(hbnb)
```

To update the details of the User model created, we can specify a new attribute and supply a value for the new attribute or specify an existing attribute and give a new value to replace the previous value. 

```shell
(hbnb) update User 97bf8455-58aa-4d65-a83e-32699de58bbb nationality "Nigerian"
(hbnb)

(hbnb) show User 97bf8455-58aa-4d65-a83e-32699de58bbb
[User] (97bf8455-58aa-4d65-a83e-32699de58bbb) {'id': '97bf8455-58aa-4d65-a83e-32699de58bbb', 'created_at': datetime.datetime(2023, 5, 13, 13, 16, 37, 181187), 'updated_at': datetime.datetime(2023, 5, 13, 13, 21, 11, 714225), 'nationality': 'Nigerian'}
(hbnb)

(hbnb) update User 97bf8455-58aa-4d65-a83e-32699de58bbb email "test.user@email.com"
(hbnb) show User 97bf8455-58aa-4d65-a83e-32699de58bbb
[User] (97bf8455-58aa-4d65-a83e-32699de58bbb) {'id': '97bf8455-58aa-4d65-a83e-32699de58bbb', 'created_at': datetime.datetime(2023, 5, 13, 13, 16, 37, 181187), 'updated_at': datetime.datetime(2023, 5, 13, 13, 24, 24, 386540), 'nationality': 'Nigerian', 'email': 'test.user@email.com'}
(hbnb)
```

To remove a model from the flat file database,

```shell
(hbnb) destroy User 97bf8455-58aa-4d65-a83e-32699de58bbb
(hbnb) all
[]
(hbnb) all User
[]
(hbnb) show User 97bf8455-58aa-4d65-a83e-32699de58bbb
** no instance found **
(hbnb)
```
---


<p>The program is interactive and the documentation from the help file is leading enough.</p>
