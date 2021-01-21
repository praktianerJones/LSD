Licenses
--------

Description
::::::::::::::::::::::::::::::::::::::::::::

The License-Module within the License-App represents the licenses used by certain software releases or packages.
Every package can have multiple optional licenses, but it must be clear which license is used through a foreign key attribute,
which sets the license which is used. The permission level of a license is represented by a “traffic light system”,
which indicates if the usage is recommended (GREEN), the usage is not rec-ommended (YELLOW) or the usage is forbidden (RED).
If a user has the right permis-sions, they can upload a new license. Due to legal issues a license must be accepted through
a user in the User-Group “Lawyer”. The modules section and paragraph are im-plemented for further usage.

Class Diagramm
::::::::::::::

.. graphviz:: /dot/licenses.dot

List of Interfaces
:::::::::::::::::: 
	#.	If the user clicks “Licenses” on the navigation bar, they are forwarded to a list of all licenses.
	#.	If the user is on the list of all licenses and wants to filter the list, they can choose one or multiple of the following:
		*	Fill in the license title box and click the button “Search”, the list of licenses is filtered through the license title.
		*	Fill in the release title box and click the button “Search”, the list of licenses is filtered through the release title.
		*	Choose one of the permission levels and click the button “Search”, the list of licenses is filtered through the chosen permission level.
	#.	If a user is logged in and is in the right user-group, they can see a “add a new li-cense” link on the license list page.
	#.	If a user is logged in, is in the right user-group, and clicks the “add a new license link, they can add a new license through a form, a license is added with the sta-tus “requested”.
	#.	If a user is logged in and is in the user-group “Lawyer” and a license has the status “requested” they can view the license through the license page and decide to change the status of the new license to “approved”.
	#.	If the user clicks one of the licenses of the list of all licenses, they can view a de-tailed page of the license
		*	If the user clicks “View original text” they can view the original text on a different page.
		*	If the user clicks “Download Text” they can download the original license as a “.txt” file.
