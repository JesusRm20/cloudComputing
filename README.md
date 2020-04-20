<center><h1>ECS781P: CLOUD COMPUTING  </h1></center>
<center><h3>Mini-Project</h3></center>
<center> <h4>Jesus Sicairos – 190717845</h4></center>

This document describes the resources that make up the project. The project consists of a web app that uses the Police API to retrieve info about crimes that happened in a specific date and in a specific location. This data is then save in a postgres database instance and manipulated with the API built for this project.

<h2>Structure:</h2>

<table>
    <tr>
        <td rowspan=8 width=40%> <img src='C:\Users\Jesus Sicairos\Desktop\Structure.png' width=100% /></td>
        <td>* db/ <br>
            in this folder we can find a .sql file which has the script to create the tables used for this app.
        </td>
    </tr>
    <tr>
		<td>
            * static/ <br>
            in this folder we can find all the static files used in the app. By static file it is meant to all files that do not change at all in the app like script files.
        </td>
    </tr>
    <tr>
		<td>
            * templates/ <br>
            here we find all the html files used to mark up the pages used in the web page.
        </td>
    </tr>
    <tr>
		<td>
            * crimeClasses.py <br>
            this file contains all the classes needed to create requests to the database. Basically this classes are used to help sqlalchemy to recreate the schema of the table in the database to which we are querying to.
        </td>
    </tr>
    <tr>
		<td>
            * main.py <br>
            this is the main executeble file. Here we find all the functions declared with its route and the method to be used with.
        </td>
    </tr>
    <tr>
		<td>
            * passwordHash.py <br>
            this is used to work with the user authentication, it helps to hass the password that is save in the database when a user creates an account and it also helps to verify the user when logging in.
        </td>
    </tr>
    <tr>
		<td>
            * task.py <br>
            this file contains auxiliary functions that help to manipulate crimes related data.
        </td>
    </tr>
    <tr>
		<td>
            * userClasses.py <br>
            this file contains clases and auxiliary functions that help to manipulate users related data.
        </td>
    </tr>
</table>

<h2>Requirements:</h2>

In order for the project to run smoothly the following elements are require:

```
* EC2 medium size intance 
* This instance should have install the folling packages:
	* pip
	* docker.io
	* awscli
	* docker postgres image
```

<h2>Functionality:</h2>

The app consists of 5 different forms. Each of which is in charge of performing a specific task.

<h4>Log In Form:</h4>

This is the firs form that loads when the someone access to my app through a web browser.

<img src="C:\Users\Jesus Sicairos\Desktop\webApp\logIn.png" style="zoom:70%;" />

Here the users have to authenticate themselves in order to gain access to the rest of the app. In case that they do not have a user account they have the option to create one just by going to the sign up page.

<h4>Sign Up Form:</h4>

When a user wants to create an account they just need to go to the sign up page fill in the details asked for in the form and click the sign up button.

<img src="C:\Users\Jesus Sicairos\Desktop\webApp\signUp.png" style="zoom:70%;" />

<h4>List Crimes Form:</h4>

This form will show a list of crimes to the user in case that there are some loaded to the database, once it logs in. In case that there are no crimes loaded in the database there is an option where a user can go to load crimes. In this form we have a search bar that helps us to search for crimes of a specific date. Just as a note all dates in the app are worked in the format of YYYY-MM. Here we also have an option to view the details of a specific crime. If we press the details button the server will take us to the form where the details of that crime are shown.

<img src="C:\Users\Jesus Sicairos\Desktop\webApp\listOfCrimes.png" style="zoom:70%;" />

<h4>Load Crimes Form:</h4>

This form allows the user to load crimes that happened in a certain date to the database, as long as they are not already store in the database. If the user inputs a date that already exists in the database the form will let the user that those crimes are already loaded and will let they try another date.

<img src="C:\Users\Jesus Sicairos\Desktop\webApp\loadCrimes.png" style="zoom:70%;" />

<h4>Edit Crime Form:</h4>

In this form the user will be able to visualize the details of a specific crime as well as the outcomes that this crime has had. In this form the user has an option to edit the crime's detail and even delete outcomes for this crime. Once the user presses the edit button all the fields that can be modified will be enable letting the user change their values. When the user has finished changing everything they only have to press the save button and the changes will be applied in the database.

<img src="C:\Users\Jesus Sicairos\Desktop\webApp\editCrime.png" style="zoom:70%;" />

<h2>Descriptions of Methods Implemented:</h2>

<h4>Sign Up:</h4>

```python
@app.route('/signup', methods=['GET', 'POST'])
def signup():
```

This function works with the two requests specified in the methods variable. Every time that the server gets a 'GET' request to this path, what it does is loads the resources require to visualize the sign up form. After the user fill in all the inputs and press the sign up button a 'POST' request is issue to the same path. In this part the method takes all the values sent with the request and save them in the database as a new user entry. After all this it redirects the user to the login method.

<h4>Load Crimes:</h4>

```python
@app.route('/load', methods=['GET','POST'])
def loadCrimes():
```

This function works the same way as the signup function. Here when the server gets a 'GET' request to this path, it loads the resources to show the load form. And when the user presses the load button a 'POST' request will be issue to this path. Here the function will make use of the selectCrimeByDate() function contained in the task.py file. This function makes a request to the police API for all the crimes that happened in the date given by the user and returns that to the loadCrimes() function. Then this function takes this rows retuned and save them in the table streetLevelCrimes contained in the database.

<h4>Log In:</h4>

```python
@app.route('/login', methods=['GET', 'POST'])
@app.route('/login/<name>', methods=['GET', 'POST'])
def login(name=None):
```

This function is being reach from the two different paths specified in the route function.  The first route is always reach when the user loads the log in page to log in to the system. Once it enters the credentials and presses the Log in button it will issue the post request. In this part a call to the database is made to retrieve the info about the user and check if it has provided the right credentials. The second path is always reach every time the user logs out from the system.

<h4>Home:</h4>

```python
@app.route('/', methods=['GET', 'POST'])
def home():
```

Once again this function uses 'GET' and 'POST' requests. When a 'GET' request is recieved the server loads the listCrimes form and lists all the crimes. These crimes are retrieves from the database with the help of the getStreestLevelCrimes() function contained within the task.py file. And a 'POST' request is executed whenever a user searches for crime for a certain date from the search box provided in the form.

<h4>Edit Crime:</h4>

```python
@app.route('/edit/<id>', methods=['GET','POST'])
def editCrime(id):
```

This function as well as the others work with 'GET' and 'POST', but in contrast with the others this function works as a bridge to the 'PUT' and 'DELETE' methods. The 'GET' request to this path will load the edit crime form, will retrieve the details of the given crime from the database as well as the outcomes and display them to the user. Then the when the users edits any of the details for the crime and presses the save button, the 'POST' request will be executed. After this the function will call the 'PUT' method to update the details of the crime in the database. After doing this it will reload the form showing the details updated.

Also when the user presses the delete button for an outcome, the 'POST' request will be executed, but this time it will call the 'DELETE' method, which will then delete that specific outcome from the database.

<h4>PUT:</h4>

```python
@app.route('/put', methods=['PUT'])
def put():
```

This function will be call from the editCrime() function. This function looks for the specified crime in the database and updates the details of it with the new details given in the request.

<h4>DELETE:</h4>

```python
@app.route('/delete', methods=['DELETE'])
def delete():
```

 Finally, this function will also be call from the editCrime() function. In this case what it will do is look for the the outcome with the persistent_id given in the request and it will delete it from the database. 

<h2>Setting up and Running the APP</h2>

After having all the above specified requirements met we proceed to the creation of the docker container that will contain the database that will be using in the APP. Assuming that we have successfully made an ssh connection to the ec2 instance shell, we just need to run the following command:

```shell
sudo docker run -p 5432:5432 --name=postgres-db postgres:latest
```

Once done that a new container with the name postgresDB will be running in our system. We can verify that the newly created is in fact running just by running the following command:

![](C:\Users\Jesus Sicairos\Desktop\webApp\dockerps.png)

Next we proceed to create the database, as well as the tables needed for our APP to run.

Once we have our database up and running, now we can create the image that will contain all the required tools to run our web app. To do this we just need to run the following command:

```
sudo docker build . --tag=cloudproject:v3
```

in the tag flag we specify the name we want to give to our image. This time we assume that we already have the Dockerfile in the working directory. In my case my Dockerfile looks as follows:

```shell
FROM python:3.7-alpine 
WORKDIR /cloudProject 
COPY . /cloudProject
RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev
Run pip install psycopg2-binary
Run pip install -U -r requirements.txt 
EXPOSE 8080 9042 
CMD ["python" , "main.py"]
```

One more thing that we need to be sure of is that we also have our requirements.txt file in the same directory. In this file we specify all the packages that need to be installed in our image.

After we run the command we can check that our image has been created by running the following command:

![](C:\Users\Jesus Sicairos\Desktop\webApp\dockerImages.png)

Once we have the image ready, we proceed to start a new container running the image that we just created. To do that we just run the following command:

```shell
sudo docker run -d -p 80:80 --name=cloudFinal cloudproject:v3
```

Here in the --name flag we specify the name we want our container to have. And we can check that our new container is running in parallel with our database container by running the following command:

![](C:\Users\Jesus Sicairos\Desktop\webApp\dockerps2.png)

After verifying that our two containers are up and running, our APP is ready. We just need to go to the browser and go to the following URL:

```html
http://ec2-54-166-176-148.compute-1.amazonaws.com/
```

