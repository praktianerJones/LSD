.. _lsd_development:

LSD Development
===============

The LSD shall be integrated into the Luetze Build System and present structures and dependencies between aspects of the
software development process. 


:TODO - Sections about these aspects shall be documented:

    #.  Setup of development system
    #.  general technology discussion
    #.  UML of DB Structure
    #.  Test and production databases
    #.  How to use a dump of production to test migrations
    #.  proposed structure of apps
    #.  how to implement a new app
    #.  how to develop a REST-interface / serializer
    #.  how to use the REST interface
    #.  usage of manage.py


Software Requirements
----------------------
This system is developed in an virtual environment (VEnv), which has to be set up as follows:

Source the virtual Environment:

``source ~/pythonVEnv/bin/activate``

Switch to the VEnv you want to work on (generates a new VEnv if <VEnvName> is unknown):

``workon <VEnvName>``

The package pip-tools is used for package management. First, all included pakages are frozen using:

``pip freeze > requirements.in``

This .in file can now be compiled into an requirements.txt file, which does show all required packages and
if applicable, which package does require it. This is achived using:

``pip-compile``

The resulting requirements.txt file can now be used to install the exact versions used on the production system.
This is achived using:

``pip-sync``

Migrations
-----------
	:TODO - Further explanation regarding Migrations:
	
Define new classes which will be migrated in models.py.

Build the migration file:

``python ./djangoProject/manage.py makemigrations``

Print sql commands which will be executed with given migration id:

``python ./djangoProject/manage.py sqlmigrate <AppName> <migrationID>``

Migrate the changes to the: DB

``python ./djangoProject/manage.py migrate``

Show all migrations in db:

``python ./djangoProject/manage.py showmigrations``

Unapply migrations:

``python ./djangoproject/manage.py migrate <appName> <migrationName>``

Further useful commands
-----------------------

Deactivate virtual environments:

``deactivate``

Get django command list:

``django-admin``

Run the server

``python ./djangoProject/manage.py runserver``

.. include:: development_Sections/testing.rst