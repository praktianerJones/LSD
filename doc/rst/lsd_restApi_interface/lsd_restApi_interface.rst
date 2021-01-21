.. _lsd_restApi_interface:

RestApi_Interface
=================
The restApi interface with the LBS has a certain HTTP Structure, this part of the documentation is an overview of HTTP Requests, 
it will explain what assumption's were made beforehand, how the URI's look and explain there functions, it shall answer the question
what is important for the LBS to connect to the LSD.

Assumption
----------

HTTP-Methods
~~~~~~~~~~~~
The Interface uses HTTP-Methods. 
HTTP-Methods consist out of four methods: 

	    #. GET requests the given resource from the server
	    #. POST create a new resource acts on entire resource
	    #. PUT  updates the resource with the given ID -> acts on a single resource
	    #. DELETE delets user with ID 
		
URI
~~~
Every resource is adressable through a Uniform Resource Identifier(URI)
A URI consist out of four important parts 

    URI: https://software.luetze.int/software/t9107_sw1000_lsd?status=Draft
	
        #. scheme       -> http, https etc. 
        #. authority    -> //software.luetze.int, //127.0.0.1
        #. path		    -> /software/t9107_sw1000_lsd
        #. query        -> ?status=Draft
		
	URI to enter the rest_api: 
	https://software.luetze.int/rest_api/<resource>
		
Resource adresses
-----------------
Products
~~~~~~~~

software.luetze.int/rest_api/products
	
+------------------+-------------------+---------------------------+-----------------------+
| Method           | Input(body)       | Output                    |Comment                |
+==================+===================+===========================+=======================+
| GET              | none              | list of all products(json)|                       |
+------------------+-------------------+---------------------------+-----------------------+
| POST             | new product (json)| redirect products/new id  |by verified user       |
+------------------+-------------------+---------------------------+-----------------------+

software.luetze.int/rest_api/products/<str:article_number>
	
+------------------+-------------------+----------------------------------+
| Method           | Input(body)       | Output                           |
+==================+===================+==================================+
| GET              | none              | product with article_number(json)|
+------------------+-------------------+----------------------------------+

software.luetze.int/rest_api/products/<str:article_number>/latest
	
+------------------+-------------------+---------------------------+
| Method           | Input(body)       | Output                    |
+==================+===================+===========================+
| GET              | none              | list of all releases(json)|
+------------------+-------------------+---------------------------+

software.luetze.int/rest_api/products/<str:article_number>/revisions/<int:article_revision>
	
+------------------+-------------------+---------------------------+
| Method           | Input(body)       | Output                    |
+==================+===================+===========================+
| GET              | none              | list of revisions(json),  |
|                  |                   | assosiated with product   |
+------------------+-------------------+---------------------------+


Releases
~~~~~~~~
partly implemented

software.luetze.int/rest_api/releases

	
+------------------+-------------------+---------------------------+
| Method           | Input(body)       | Output                    |
+==================+===================+===========================+
| GET              | none              | list of all releases(json)|
+------------------+-------------------+---------------------------+

software.luetze.int/rest_api/releases/<str:Release_title>/licenses/<str:license_title>
	
+------------------+-------------------+---------------------------+
| Method           | Input(body)       | Output                    |
+==================+===================+===========================+
| GET              | none              | list of licenses(json),   |
|                  |                   | assosiated with release   |
+------------------+-------------------+---------------------------+

Licenses
~~~~~~~~
not implemented yet
software.luetze.int/rest_api/licenses


+------------------+-------------------+---------------------------+-----------------------+
| Method           | Input(body)       | Output                    |Comment                |
+==================+===================+===========================+=======================+
| GET              | none              | list of all products(json)|                       |
+------------------+-------------------+---------------------------+-----------------------+
| POST             | new product (json)| redirect licenses/lic_id  |by verified user       |
+------------------+-------------------+---------------------------+-----------------------+
	
software.luetze.int/rest_api/licenses/<str:title>

+------------------+-------------------+---------------------------+
| Method           | Input(body)       | Output                    |
+==================+===================+===========================+
| GET              | none              |license(json) by title     |
+------------------+-------------------+---------------------------+

software.luetze.int/rest_api/licenses/<str:license_title>/releases/<str:release_title>
	
+------------------+-------------------+---------------------------+
| Method           | Input(body)       | Output                    |
+==================+===================+===========================+
| GET              | none              | list of releases(json),   |
|                  |                   | assosiated with license   |
+------------------+-------------------+---------------------------+


Tools
~~~~~
not implemented yet


List of all routes
------------------
generated by django_extensions 


/	lsd.views.home	lsd-home
/about/	lsd.views.about	lsd-about

Products:

/products/	products.views.product_list	product-list
/products/<str:article_number>/	products.views.product_details	product-detail
/products/<str:article_number>/<str:article_revision>/	products.views.product_details_revision	product-details-revision
/products/<str:article_number>/latest/	products.views.product_details_latest	product-details-latest


RestApi:

/rest_api/api-auth/login/	django.contrib.auth.views.LoginView	rest_framework:login
/rest_api/api-auth/logout/	django.contrib.auth.views.LogoutView	rest_framework:logout
/rest_api/products/	rest_api.views.product_list
/rest_api/products/<str:article_number>/	rest_api.views.product_by_number
/rest_api/products/<str:article_number>/<int:article_revision>/	rest_api.views.product
/rest_api/products/<str:article_number>/latest/	rest_api.views.product_latest
/rest_api/releases/	rest_api.views.release_list

Software:

/software/	software.views.software_list	software-list
/software/<str:software_name>/	software.views.software_details	software-detail
/software/<str:software_name>/<str:software_version>/	software.views.software_details_version	software-detail-version
/software/<str:software_name>/<str:software_version>/release/	software.views.software_details_version_release	software-detail-version-release
/software/<str:software_name>/<str:software_version>/withdraw/	software.views.software_details_version_withdraw	software-detail-version-withdraw
/software/<str:software_name>/latest/	software.views.software_details_latest	software-datail-latest
/software/<str:software_name>/nightly/	software.views.software_details_nightly	software-detail-nightly


Tools:

/tools/	tools.views.tools_list	tools-list
/tools/<str:tool_name>/	tools.views.tool_version_list	tool-version-list
/tools/<str:tool_name>/<str:tool_version>/	tools.views.tool_details	tool-details

Va:

/va/	lsd.views.va	lsd-va
/va/<str:branch_type>/	lsd.views.va_branch	lsd-va-branch-type
/va/<str:branch_type>/<str:branch_name>/	lsd.views.va_branch_name	lsd-va-branch-type-name
/va/latest/	lsd.views.va_details_latest	lsd-va-latest
/va/latest/doc/	lsd.views.va_details_latest_doc	lsd-va-latest-doc
/va/latest/sw/	lsd.views.va_details_latest_sw	lsd-va-latest-sw
/va/nightly/	lsd.views.va_details_nightly	lsd-va-nightly
/va/nightly/doc/	lsd.views.va_details_nightly_doc	lsd-va-nightly-doc
/va/nightly/sw/	lsd.views.va_details_nightly_sw	lsd-va-nightly-sw	




Auto generated

/admin/	django.contrib.admin.sites.index	admin:index
/admin/<app_label>/	django.contrib.admin.sites.app_index	admin:app_list
/admin/auth/group/	django.contrib.admin.options.changelist_view	admin:auth_group_changelist
/admin/auth/group/<path:object_id>/	django.views.generic.base.RedirectView
/admin/auth/group/<path:object_id>/change/	django.contrib.admin.options.change_view	admin:auth_group_change
/admin/auth/group/<path:object_id>/delete/	django.contrib.admin.options.delete_view	admin:auth_group_delete
/admin/auth/group/<path:object_id>/history/	django.contrib.admin.options.history_view	admin:auth_group_history
/admin/auth/group/autocomplete/	django.contrib.admin.options.autocomplete_view	admin:auth_group_autocomplete
/admin/auth/user/	django.contrib.admin.options.changelist_view	admin:auth_user_changelist
/admin/auth/user/<id>/password/	django.contrib.auth.admin.user_change_password	admin:auth_user_password_change
/admin/auth/user/<path:object_id>/	django.views.generic.base.RedirectView
/admin/auth/user/<path:object_id>/change/	django.contrib.admin.options.change_view	admin:auth_user_change
/admin/auth/user/<path:object_id>/delete/	django.contrib.admin.options.delete_view	admin:auth_user_delete
/admin/auth/user/<path:object_id>/history/	django.contrib.admin.options.history_view	admin:auth_user_history
/admin/auth/user/add/	django.contrib.auth.admin.add_view	admin:auth_user_add
/admin/auth/user/autocomplete/	django.contrib.admin.options.autocomplete_view	admin:auth_user_autocomplete
/admin/jsi18n/	django.contrib.admin.sites.i18n_javascript	admin:jsi18n
/admin/login/	django.contrib.admin.sites.login	admin:login
/admin/logout/	django.contrib.admin.sites.logout	admin:logout
/admin/password_change/	django.contrib.admin.sites.password_change	admin:password_change
/admin/password_change/done/	django.contrib.admin.sites.password_change_done	admin:password_change_done
/admin/products/family/	django.contrib.admin.options.changelist_view	admin:products_family_changelist
/admin/products/family/<path:object_id>/	django.views.generic.base.RedirectView
/admin/products/family/<path:object_id>/change/	django.contrib.admin.options.change_view	admin:products_family_change
/admin/products/family/<path:object_id>/delete/	django.contrib.admin.options.delete_view	admin:products_family_delete
/admin/products/family/<path:object_id>/history/	django.contrib.admin.options.history_view	admin:products_family_history
/admin/products/family/add/	django.contrib.admin.options.add_view	admin:products_family_add
/admin/products/family/autocomplete/	django.contrib.admin.options.autocomplete_view	admin:products_family_autocomplete
/admin/products/product/	django.contrib.admin.options.changelist_view	admin:products_product_changelist
/admin/products/product/<path:object_id>/	django.views.generic.base.RedirectView
/admin/products/product/<path:object_id>/change/	django.contrib.admin.options.change_view	admin:products_product_change
/admin/products/product/<path:object_id>/delete/	django.contrib.admin.options.delete_view	admin:products_product_delete
/admin/products/product/<path:object_id>/history/	django.contrib.admin.options.history_view	admin:products_product_history
/admin/products/product/add/	django.contrib.admin.options.add_view	admin:products_product_add
/admin/products/product/autocomplete/	django.contrib.admin.options.autocomplete_view	admin:products_product_autocomplete
/admin/products/productgroup/	django.contrib.admin.options.changelist_view	admin:products_productgroup_changelist
/admin/products/productgroup/<path:object_id>/	django.views.generic.base.RedirectView
/admin/products/productgroup/<path:object_id>/change/	django.contrib.admin.options.change_view	admin:products_productgroup_change
/admin/products/productgroup/<path:object_id>/delete/	django.contrib.admin.options.delete_view	admin:products_productgroup_delete
/admin/products/productgroup/<path:object_id>/history/	django.contrib.admin.options.history_view	admin:products_productgroup_history
/admin/products/productgroup/add/	django.contrib.admin.options.add_view	admin:products_productgroup_add
/admin/products/productgroup/autocomplete/	django.contrib.admin.options.autocomplete_view	admin:products_productgroup_autocomplete
/admin/r/<int:content_type_id>/<path:object_id>/	django.contrib.contenttypes.views.shortcut	admin:view_on_site
/admin/software/release/	django.contrib.admin.options.changelist_view	admin:software_release_changelist
/admin/software/release/<path:object_id>/	django.views.generic.base.RedirectView
/admin/software/release/<path:object_id>/change/	django.contrib.admin.options.change_view	admin:software_release_change
/admin/software/release/<path:object_id>/delete/	django.contrib.admin.options.delete_view	admin:software_release_delete
/admin/software/release/<path:object_id>/history/	django.contrib.admin.options.history_view	admin:software_release_history
/admin/software/release/add/	django.contrib.admin.options.add_view	admin:software_release_add
/admin/software/release/autocomplete/	django.contrib.admin.options.autocomplete_view	admin:software_release_autocomplete
/admin/tools/tool/	django.contrib.admin.options.changelist_view	admin:tools_tool_changelist
/admin/tools/tool/<path:object_id>/	django.views.generic.base.RedirectView
/admin/tools/tool/<path:object_id>/change/	django.contrib.admin.options.change_view	admin:tools_tool_change
/admin/tools/tool/<path:object_id>/delete/	django.contrib.admin.options.delete_view	admin:tools_tool_delete
/admin/tools/tool/<path:object_id>/history/	django.contrib.admin.options.history_view	admin:tools_tool_history
/admin/tools/tool/add/	django.contrib.admin.options.add_view	admin:tools_tool_add
/admin/tools/tool/autocomplete/	django.contrib.admin.options.autocomplete_view	admin:tools_tool_autocomplete

/login/	django.contrib.auth.views.LoginView	login
/logout/	django.contrib.auth.views.LogoutView	logout