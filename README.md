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
When you want to get started please have a look on our (how to install)[https://github.com/praktianerJones/LSD/blob/main/How_To_Install.md] for more information about the LSD, please visit our wiki. 

### What Apps are implemented in the LSD?

1. LSD-App

   The LSD App serves as a base-app. Every other app uses the base-app’s functions. Within the LSD app a base template is integrated, which sets the view of the whole website. 
The rest of the templates are nested into a block of a base template. No data is saved through the LSD app. The LSD app manages base functions like the authentica-tion 
administration of the system, which is provided by Django. Django’s administration systems allow an admin to delete, create, update and view table entries.  

2. REST_API-App

   The REST_API-App is the gateway to the LBS. It communicates through HTTP requests and responses. It allows the LBS to get products and POST or GET releases. No data is saved   
   within the REST_API-App. 
   
3. User-App

   The LSD provides sensitive functions and information, the user app’s main task is to limit access to certain pages. The user app is provided by Django and has interfaces to 
   most apps. Beside its main task, the user app allows the system to distribute responsibilities of other apps (e.g. being creator of a model instance).  
   
4. Software-App

   The Software-App represents the used software which is developed. The App has a table release, which represents the software in a certain release state with a version number. 
   Release interacts with the table user. Every release has several conditions for users, these are responsible for different tasks (developing, testing, verifying and being 
   responsible).  
   
5. Tool-App

   The Tool-App represents the tools used by software and hardware developers. They relate to the class release of the software-app. One software can use several tools.  
   
6. Products-App

   The Products-App represents the finished product. Every product is linked to the soft-ware-release it used for development. A product can be part of a family, which is a 
   cluster of product groups.
   
7. Package-App

   The Package-App represents the packages which are used from software releases. They distinguish themselves from releases, because they can be third-party software. The  
   Package-App is used mostly by the LBS. The LBS must check if all used packages by a release are within a legal usability.
   

8. License-App

   The License-Module within the License-App represents the licenses used by certain soft-ware releases or packages. Every package can have multiple optional licenses, but it 
   must be clear which license is used through a foreign key attribute, which sets the license which is used. The permission level of a license is represented by a “traffic 
   light system”, which indicates if the usage is recommended (GREEN), the usage is not recommended (YELLOW) or the usage is forbidden (RED). If a user has the right 
   permissions, they can upload a new license. Due to legal issues a license must be accepted through a user in the User-Group “Lawyer”. The modules section and paragraph are 
   implemented for fur-ther usage.  


### About the company behind the LSD
The LSD is developed and maintained through the Friedrich Lütze GmbH. The Friedrich Lütze GmbH works in the fields transportation and automation, with the specifications cable, cabinet, connectivity and control. 
[Please visit our Website for more information about the Friedrich Lütze GmbH.](https://www.luetze.com/de-de/)

### License
The LSD through the 3-Clause-BSD, a copy of this license is provided in this Repo. 
