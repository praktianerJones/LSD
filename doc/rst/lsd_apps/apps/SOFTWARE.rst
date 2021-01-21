Software
--------

Description
::::::::::::::::::::::::::::::::::::::::::::

The Software-App represents the used software which is developed.
The App has a ta-ble release, which represents the software in a certain release state with a version number.
Release interacts with the table user. Every release has several conditions for users,
these are responsible for different tasks (developing, testing, verifying and being responsible).

Class Diagramm
::::::::::::::

.. graphviz:: /dot/software.dot


List of Interfaces
:::::::::::::::::: 
	#.	If the user clicks ‘Software’ on the navigation bar, they are forwarded to a list of all releases.
	#.	If the user clicks one of the releases on the list, they can view a detail-page of the release.
	#.	If they click show doc, they get forwarded on a page, where they can view the documentation.
	#.	If they click download software, on the detail-page, they can download the soft-ware’s latest release.
	#.	If they click on one version of the detailed release page, they are forwarded to the version page of the release.
	#.	If a user is logged in, they can change the releases status to ‘released’ or to ‘withdrawn’.
