# Whois

This small application print to console terminal nice foramted information about website from Whois XML API.

## Requirements:

- Python 3
- Pip

### Automatic installation with pip:

* pip install -r requirements.txt


### Non-automatic installation without pip:

* sudo apt-get install -y python3

* sudo apt install -y python3-pip

* pip install requests

* pip install colorama

* pip install pprint

## Usage:

### Basic usage

* python3 whois.py -d example.com

### Advanced usage parameters:

* #### -c
    Print contact info

* #### -o
    Print organization info
    
* #### -hn
    Print host names
    
* #### -a
    Print everything, except raw json
    
* #### -rj
    Print only raw json
    
* #### -rjr
    Print only raw json in readable form

* #### -sak
    Set your own API key

* #### -sdk
    Set default API key
    
* #### -uk
    Use your own API key

## Unit tests

### Function tests for profiq.com and other functions

* It is used for testing function of the code.