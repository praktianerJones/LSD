# Installation guide

For the development of the LSD the following third-party software must be installed before its used:

|Software name|Version|Function|
|--|--|--|
|Django|2.1.7|WebFramework|
|Django_extensions|3.0.3|Collection of custom extensions|
|Django_python3_ldap|0.11.3|3-Clause-BSD|Web Framework|
|Djangorestframework|3.10.3|Framework for REST API|
|Crispy_forms|1.8.1|Helps to format templates|
|Json|Unknown|Lightweight data-interchange format|
|Python|3.6.9|Programming language|

To make the installation easier, we included a requirments file in our repo, so just hit:
```
pip-compile
pip-sync
```
to install the required packages. 


### credentials
The passwords and the django secret key are held by a json file outside of this repository.
The file needs to be in the same directory as the repository.
The filename has to be ``config.json``
The file has to provide these variables:
```
{
    "lsd_secret_key": "<django secret key - used for security features>",
    "lsd_dbpass": "<password of the db or "" in case of internal sqlite db>",
    "lsd_ldappass": "<password of the user>",
    "lsd_testserver": true/false, (optional - true: django uses an internal sqlite db - for test/develop purpose)
    "lsd_debug": true/false (optional - if not set it will be set through the lsd_testserver)
}
```

If this file is not found the LSD defaults to testserver state without LDAP
access and uses the internal sqlite dummy database.

For more information check the readme.md in the repository folder LSD. 


