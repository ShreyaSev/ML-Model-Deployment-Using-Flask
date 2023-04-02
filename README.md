# MLT-CIA2-Model-Deployment-Using-Flask
This repository contains the files for a simple web app using html and css for a machine learning model.

## Contents
# Login
### index.html and index.css
The html and css files for the first login page. The user is prompted to enter their username and password, which is authenticated using the mysql database. If the credentials are valid, the user is taken to the next page. If it is invalid, a message is printed stating that the username or password is invalid and they can try again. 

There is also a link to a page where a new user can create an account. 

## Registration
### registration.html and registration.css
The user is prompted to enter their username, password and email. If the username already exists, a message is printed saying this user already exists. If all the details are entered correctly, the user is added to the database and a Success message is printed. There is also a link to return back to the login page. 

## Entering details into the model
### home.html and home.css
This page contains a header which welcomes the current user based on their username. It also has a logout button which terminates the current session. 
A html form collects all the required data from the user.
On clicking the predict button, the prediction is displayed below the button itself. 
The collected data is passed to the model which is saved as a .pkl file. 

## Database Management
flask_mysql db is used to connect MySQL to the flask app. 
