#AWARDS

#### By **Canssidle** 

## Description

This web-app allows a user to create a Profile,Category,Country,Technology,Color and Projects that are all under his username allowing other users to vote for them and visit the particular projects site.

## Behaviour Driven Development

| Behavior our program should handle | Input description |  Output description
| --- | --- | --- |
| `Register/Sign up` | Fill in the required details | The user will recieve an activation email
| `Login` |Enter the reqired details |  The user will be redirected to the homepage
| `Upload project` | The user user can upload a project and give the details about the project | Displays the created project
| `View`| The user can click on a project which has been already uploaded | The user will be able to see the details about the project


### prerequisites
First clone the project to your camputer. 
* git clone https://github.com/canssidle/Awards.git
Ensure python3 is installed.
Install virtual environment by running 
* pip3 install virtualenv
Create a virtualenvironment by running  
* virtualenv <name of environment>on the terminal and once its activated by running  *source <name of environment>/bin/activate then install all the packages by running 
* pip3 install -r requirements.txt

Create .env file and paste the following.
* SECRET_KEY = '<Secret_key>'
* DBNAME = 'name-of-app-database'
* USER = '<Username>'
* PASSWORD = '<password>'
* DEBUG = True

* EMAIL_USE_TLS = True
* EMAIL_HOST = 'smtp.gmail.com'
* EMAIL_PORT = 587
* EMAIL_HOST_USER = '<your-email>'
Then start the server by running 
* python3 manage.py runserver.
Copy the link and paste in any browser 
* http://localhost:8000



## Technology and Tools Used

 Python3.6 - Programming language
 Django - Django framework
 Git - Version control
 Visual Studio - Code editor
 Postgresql
 Heroku
 Bootstrap4

 

## Further help
+ To get Further help you can read the Django Documentation.

## Licence
MIT (c) 2019 canssidle (https://github.com/canssidle)