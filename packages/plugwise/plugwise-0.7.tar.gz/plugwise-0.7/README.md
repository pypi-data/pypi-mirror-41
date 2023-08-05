This is a library and a simple command line utility for communicating with Plugwise smartplugs.

# Install
To install run the following command as root:
```
python3 setup.py install
```
# Usage
You can use plugwise_util to test some simple things. For example, to get power usage from a specific Circle use:
```
plugwise_util -m <MAC ADDRESS> -p
```
To get overview of the supported options use:
```
plugwise_util -h
```
This script also serves as an example usage of the library functionality. 
See the docstrings of the plugwise module for better documentation.
