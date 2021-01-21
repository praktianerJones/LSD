Products
--------

Description 
:::::::::::
The Products-App represents the finished product.
Every product is linked to the software-release it used for development.
A product can be part of a family, which is a cluster of product groups.

Class Diagramm
::::::::::::::

.. graphviz:: /dot/products.dot

List of Interfaces
::::::::::::::::::::::::::::::::::::::::::::::::::

	#.	If the user clicks ‘Products’ on the navigation bar, they are forwarded to a list of all products.
	#.	If the user clicks one of the products of the list, they can view a detail-page of the product.
	#.	If they click one of the used releases, they are is linked to the release detail view of the module software.
