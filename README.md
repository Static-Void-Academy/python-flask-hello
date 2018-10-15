
# Python Flask Hello World Example

## Installing / Getting started

In order to launch the Flask instance, ensure that you have Python 3.7 installed. If it is not installed it can be downloaded from the link provided [here](https://www.python.org/downloads/release/python-370/):

https://www.python.org/downloads/

Next, use the pip3 package manager to install the pipenv module

```
sudo pip3 install pipenv
``` 


After installing _pipenv_, the _pipenv install_ command can be used to install of the modules listed within the Pipfile contained in the directory.

```
pipenv install 
```

After installing the required dependencies, the virtual environment created by _pipenv_ during the installation must now be activated.

```
pipenv shell
```


You can confirm that you have successfully activated the virtual environment if the name of the project appears in parentheses to the left of the command line. 

Once you have confirmed that the virtual environment has been activated, use the following commands to launch the Flask service.

```
FLASK_APP=main.py flask run --port=<desired port number>
```


