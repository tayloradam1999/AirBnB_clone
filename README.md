# AnA-BnB
## Adam and Adam's AirBnB

## Project Description
First step: Write a command interpreter to manage your AirBnB objects.
This is the first step towards building your first full web application: the AirBnB clone. This first step is very important because you will use what you build during this project with all other following projects: HTML/CSS templating, database storage, API, front-end integration…

## Description of the command interpreter
### What’s a command interpreter?
Do you remember the Shell? It’s exactly the same but limited to a specific use-case. In our case, we want to be able to manage the objects of our project:

* Create a new object (ex: a new User or a new Place)
* Retrieve an object from a file, a database etc…
* Do operations on objects (count, compute stats, etc…)
* Update attributes of an object
* Destroy an object

### Starting the command interpreter
You are able to start the command interpreter by running the following command:
```
./console
```

### Using the command interpereter
Once you have ran
```
./console
```
you are now able to run commands within the interpreter while using the following format!
```
create BaseModel
```
```
show BaseModel
```
```
help create
```

## File Structure
The file structure of this program is quite simple.

We have our console inside of the home directory, and within the home directory, there are two parent directories called 'models' and 'tests'.

'models' holds files for all of the classes that will be used within our program. Also, within this directory, there is another parent directory called 'engine'.

'engine' is a directory that holds 'file_storage.py' which holds a class that serializes instances to a JSON file and deserializes JSON files to instances.

Now, if we go back to our home directory, we can then go into 'tests' which is a directory that holds all of our unittesting files.Unittesting is important, never forget to unittest.
