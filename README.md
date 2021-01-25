# LSD 
### Introduction 
Documentation tool for metainformation, developed to fulfill certain transportation norms

LSD stands for Luetze Software Delievery. It was build with the python based Webframework Django. 
The LSD consists of different apps, which change the functionality. 
Apps can be activated and deactivated. 

### Usage of the LSD
We use the LSD as a filling system. Through the Web and RestApi Interface integrated in the LSD, our internal Buildtool saves information of software in the LSD. 

### How can you contribute? 
We welcome contributors, please inform yourself about our [code of conduct](https://github.com/praktianerJones/LSD/blob/main/CODE_OF_CONDUCT.md) .

This Repo is especially interessting for people and companies who wants to develop a continous integration system used by companies who have to fulfill certain norms. 
When you want to get started please have a look on our [how to install](https://github.com/praktianerJones/LSD/blob/main/How_To_Install.md) for more information about the LSD, please visit our wiki. 

### What Apps are implemented in the LSD?

1. The base app

   Within the base app the general settings for the system are set. It defines the look of the other apps through a CSS file and a base template, which should be imported in        other apps. Every app that should be available through their urls.py files must be included in the base files urls.py file.

2. REST_API-App

   The REST_API-App is the gateway to the LBS. It communicates through HTTP requests and responses. It allows the LBS to get products and POST or GET releases. No data is saved 
   within the REST_API-App. 
   
3. User-App

   The LSD provides sensitive functions and information, the user app’s main task is to limit access to certain pages. The user app is provided by Django and has interfaces to 
   most apps. Beside its main task, the user app allows the system to distribute responsibilities of other apps (e.g. being creator of a model instance).  
   
4. The software app

   The software app represents active or inactive software repositories developed through the Friedrich Lütze GmbH. A software can exist multiple times in different versions,      these versions are called releases. Every software release has a license and multiple users, which fulfill different roles (e.g. creator, maintainer etc.).
   
5. Tool-App

   The tools app manages the tools which are used by hardware or software developers. They are connected to the software app. One software can use multiple tools.

6. The products app

   The software app represents active or inactive software repositories developed through the Friedrich Lütze GmbH. A software can exist multiple times in different versions,      these versions are called releases. Every software release has a license and multiple users, which fulfill different roles (e.g. creator, maintainer etc.).
   
7. Package-App

   The package app is responsible to represent software build from multiple modules. Every package has a license and every software can have multiple packages.
   

8. License-App

   The License-Module within the License-App represents the licenses used by certain soft-ware releases or packages. Every package can have multiple optional licenses, but it 
   must be clear which license is used through a foreign key attribute, which sets the license which is used. The permission level of a license is represented by a “traffic 
   light system”, which indicates if the usage is recommended (GREEN), the usage is not recommended (YELLOW) or the usage is forbidden (RED). If a user has the right 
   permissions, they can upload a new license. Due to legal issues a license must be accepted through a user in the User-Group “Lawyer”. The modules section and paragraph are 
   implemented for further usage.  

9. The va app

   The acronym va stands for “Verfahrensanweisung”. Through the va app the internal work-ing instructions are described. 

### About the company behind the LSD
The LSD is developed and maintained through the Friedrich Lütze GmbH. The Friedrich Lütze GmbH works in the fields transportation and automation, with the specifications cable, cabinet, connectivity and control. 
[Please visit our Website for more information about the Friedrich Lütze GmbH.](https://www.luetze.com/de-de/)

### License
The LSD through the 3-Clause-BSD, a copy of this license is provided in this Repo. 
