Rest_Api
--------

Description 
::::::::::::::::::::::::::::::::::::::::::::
The REST_API-App is the gateway to the LBS. 
It communicates through HTTP requests and responses.
It allows the LBS to get products and POST or GET releases. 
No data is saved within the REST_API-App.

List of Interfaces
:::::::::::::::::: 
The following interfaces can be found in the file  rest_api/urls.py 

	#. If the LBS sends a GET  request on '/releases', it gets a list of releases.
	#. If the LBS sends a GET  request on '/releases/<str:release_nr>', it gets a single release.
	#. If the LBS sends a GET  request on '/products', it gets a list of all products.
	#. If the LBS sends a GET  request on '/products/<str:article_number>', it gets a single product.
	#. If the LBS sends a GET  request on '/products/<str:article_number>/revisions/latest', he gets the latest revision of the product.
	#. If the LBS sends a GET  request on '/licenses', it gets a list of all licenses.
	#. If the LBS sends a GET  request on '/licenses/<str:titel>', it gets a single license.
	#. If the LBS sends a GET  request on '/licenses/<str:titel>/releases', he gets all releases which use licenses.
	#. If the LBS sends a GET  request on '/packages', it gets a list of all packages.
	#. If the LBS sends a GET  request on '/packages/<str:package_name>/versions/<str:package_version>', it gets a package filtered through name and version.	
	#. If the LBS sends a POST request on '/releases', with a list of releases, the list will be added to the database, if it is serializable.
	#. If the LBS sends a POST request on '/products', with the correct head and body it can add new products to the Database.
	#. If the LBS sends a POST request on '/packages', it can add a list of packages to the database and gets the list back, sorted into four sub lists, which will show him if the adding of every single package was sucessful and if not why it was not.

Sequence diagram: example on product_latest
:::::::::::::::::::::::::::::::::::::::::::

.. uml:: /uml/rest_api_Sequenzdiagram.uml