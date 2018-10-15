# Python Flask Hello World Example
This is the Static Void Academy example repository for a Hello World Python Flask web server. This is meant as a simple introduction to web servers.

Find the companion article [here](???) and the companion YouTube video [here](???).

## Installation / Prerequisites
You will need:
- Python3
- Pip3
- Pipenv

### Python3 / Pip3

#### Mac
For Mac users, we recommend using Homebrew to install all of your libraries and packages. Follow instructions on [Homebrew's site](https://brew.sh/#install) to install brew first.

Then, install Python3
```
brew install python
```

This will install Python 3.7 and pip 3. You can automatically alias/set up your `python` and `pip` commands to point to `python3` and `pip3` if you'd like, but we recommend against it just so you can keep track of which versions you're using. If you're using Homebrew and your OS is up-to-date, then it should automatically install the latest versions of Python and Pip for you.

#### Linux
Use your distribution's package manager to install Python 3
```
# Debian/Ubuntu
sudo apt-get update && sudo apt-get install python3.7

# CentOS/RedHat
sudo yum update && sudo yum install centos-release-scl
sudo yum install rh-python36

# Fedora
sudo dnf install python3
```

#### Windows
Download the installer from the [python website](https://www.python.org/downloads/release/python-370/) and install it from there. We recommend the `Windows x86-64 web-based installer` if you have decently fast Internet.

Python 3.4 and later include pip by default. If your package manager installed Python 3.3 or below, then you'll need to find separate instructions to install pip3, because this README is getting huge.


### Pipenv
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

## Running
Once you have confirmed that the virtual environment has been activated, use the following commands to launch the Flask service.
```
FLASK_APP=main.py flask run --port=<desired port number>
```

