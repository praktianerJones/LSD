User
----

Description
:::::::::::

The LSD provides sensitive functions and information, the user app’s main task is to limit access to certain pages.
The user app is provided by Django and has interfaces to most apps. 
Beside its main task, the user app allows the system to distribute responsibilities of other apps (e.g. being creator of a model instance).
(e.g. beeing a creater of a module instance). The User module is provided by django. 


List of Interfaces
:::::::::::::::::: 
Please note that "user" descripes in that context the physical user of the Programm and "User" descripes the User module
	#. If an unauthenticated user clicks ‘Login’ on the navigation bar, they are forwarded to a Login-Form.
	#. If an unauthenticated user fills in the login-form with a valid username and pass-word, they are authenticated.
	#. If the authenticated user clicks 'Licenses' on the navigation bar  they are able to see a hidden 'Add a new license' button(see License module for more information).

Class Diagramm
::::::::::::::

.. graphviz:: /dot/user.dot

User groups
:::::::::::

Django provides user groups. User groups are used to establish an authentication sys-tem at the backend.
Every model has four authentication states, which a user group can hold.
The four states on every model are add, change, delete and view.
On a client re-quest the server checks if the user is authenticated and has the right permissions to en-ter the side.
A user can have multiple user groups.

The following user groups exist: 
	
	#. Admin | can access all states of every model
	#. Software Team Member | can access the states add, change, view but not delete
	#. License Reviewer | can access a special fifth state, implemented to recognice a review
	#. PG | mostly view 
	#. Production | mostly view

Admin
:::::
The Admin is an implemented User, he can access the Admin-Page and view the LogEntry, admin and Admin-Page are provided by django. 

.. graphviz:: /dot/admin.dot

At the Admin-Page he can: 

	#. Logout
	#. Change his password
	#. View his recent actions
	#. View, Add, Update and Delete every Module including the User module