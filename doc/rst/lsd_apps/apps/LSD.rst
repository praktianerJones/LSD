LSD
---

Description
:::::::::::

The LSD App serves as a base-app. Every other app uses the base-app’s functions. 
Within the LSD app a base template is integrated, which sets the view of the whole website.
The rest of the templates are nested into a block of a base template. 
No data is saved through the LSD app. The LSD app manages base functions like the authentication
administration of the system, which is provided by Django. 
Django’s administration systems allow an admin to delete, create, update and view table entries.

List of Interfaces
:::::::::::::::::: 
	#. If the user clicks 'Home' on the navigation bar, they are forwarded to a software release list view.
	#. If the user clicks 'VA' (short for "Verfahrensanweisung") on the navigation bar, they are forwarded to an overview of links to different versions of the procedural instructions.
	#. If the user clicks 'Login' on the navigation bar, they will be forwarded to a login screen.
	#. If a logged in user clicks 'Logout' on the navigation bar, they will be logged out.