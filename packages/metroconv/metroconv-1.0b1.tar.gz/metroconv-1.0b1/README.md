# Metro Bank CSV to FreeAgent CSV converter

## The Problem
FreeAgent supports multiple well documented formats for importing bank account transactions into the accounting system. Metro Bank however only provides for download their own CSV format or force you to use their partner accounting systems to interface with your Business Bank Accounts.

## The Solution
This tiny piece of software tries to mitigate this by converting from the CSV format Metro Bank provides to the CSV format FreeAgent accepts.

## Building it
This piece of software is Python 3 compatible and also runs fine on Windows/mac/linux. It comes with a small utility that uses the code provided in the metroconv library. Once installed into a python environment the tool metroconv will be available on the PATH assuming the python environment, in which it is installed is the main python on the system or a python virtual environment that is activated.

### Build using setup.py
You can do
```bash
python setup.py bdist_egg
```
or if you have the wheel packager installed
```bash
python setup.py bdist_wheel
```

after which there will be an installation artefact in the dist directory that looks like one of these:
```bash
30/01/2019  15:01             3,563 metroconv-1.0-py3-none-any.whl
30/01/2019  15:01             7,170 metroconv-1.0-py3.7.egg
```
Then any of the 2 can be used by pip to install it.
```bash
pip install metroconv-1.0-py3-none-any.whl

Processing metroconv-1.0-py3-none-any.whl
Installing collected packages: metroconv
Successfully installed metroconv-1.0
```

### Installing from pypi (if it ever gets in there)
```bash
pip install metroconv
```
