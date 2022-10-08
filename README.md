# mysql-selfmanaged
HHA 504 // Week 6 // Assignment 5

## This repo focuses on spinning up virtual machines, creating databases with mysql within those vms, and then connecting to those virtual machines via python and subsequently inserting data into the databases.

## For this example we choose to use Azure. Azure's ssh connection process is tedious at first but actually becomes quite routine with frequent use. In addition, it's convenient to have the environment within the user's native Terminal or Cmd Prmpt. Lastly, Azure's process for creating rules for opening ports for connection (specifically 3306 for mysql) is decidedly simpler than GCP's process.

## There are a few ways to go about starting the process but we choose to create the virtual machine and set up mysql there first.

## When creating a machine suitable for this exercise and similar mysql purposes, it's important to keep a few parameters in mind. We prefer our operating size to be Linux (Ubuntu). We want size to be a little larger than our typical test or scratch environments created up till now. As opposed to a micro machine size, we want to select a more mid-tier size (in this case we choose Standard B2). A good rule of thumb is to look for a size with 2 vcpus. We can leave port traffic rules as default, as we will be creating a custom rule afterwards.

## after creating our machine and starting it, we can turn our attention to creating a custom traffic rule so that we can properly connect to the vm from other machines via mysql to populate databases within that vm. Within Azure, having navigated to the virtual machines section, we can click on the machine we intend to use for the exercise. Within the left side bar that appears, we navigate to networking under settings. We can then simply click Add Inbound Port Rule. For source, we can keep Any. For source port ranges, we type '*' to signify All. For destination port ranges, we type '3306' for mysql access specifically. The rest of the parameters can be kept as default values. Now our vm is ready for inbound connections through port 3306.

## Next we prep the vm for table insertion. Before we can remotely insert a table via mysql, we first need to create a database in mysql with an empty table. Let's access our vm. For Azure we connect via ssh. We can open our terminals and cd into our .ssh directory. From there, we can use 'ls -l' to view available files. We can then chmod 400 the appropriate .pem or .cer file. From there, we can connect with the appropriate command line.

## We changed port rules for inbound traffic on Azure web, and now we must do the same in the vm. In this case we must modify both the bind address and mysql bind address. We can view bind addresses with 'sudo nano /etc/mysql/mysql.conf.d/mysqld.cnf'. Once we are in nano, we can edit the bind address and mysql bind address to 0.0.0.0 to simply account for all incoming ip addresses. We can use ctrl + O to save  and ctrl + X to exit nano text editor.

## Let's install mysql. As best practice, we run 'sudo apt-get update' to ensure all packages are up-to-date. Then, we can use 'sudo apt-get install mysql-server mysql-client' to acquire mysql.

## Now that we have acquired mysql, we can go ahead and access it. Because there are no accessible user accounts by default, we will have to use root user account initially. we can access mysql via root with 'sudo mysql'. From here, we'll want to create a new user. For the purposes of this exercise, we can grant this user all the permissions of a root user without restrictions. we can use command CREATE USER to create a new user. the parameters are username followed by @ followed with domain address. In this case we can use '%' for wild card address values to simplify the process. Following the parameters is IDENTIFIED BY followed by a password. Command structure would look like: 'CREATE USER 'user'@'%' IDENTIFIED BY 'password';'. Commands are not case sensitive. 

## To check that we have successfully created a user, we can perform query: 'SELECT user FROM mysql.user;'

## From there, we want to grant the new user we have created with root privileges. This can be accomplished with 'GRANT ALL PRIVILEGES on *.* to 'user'@'%' WITH GRANT PRIVILEGES.' *.* signifies that the user in question will be granted all privileges regarding any and all future databases existing within the mysql. WITH GRANT PRIVILEGES allows the user in question to grant privileges to other users as well.

## To check that we have properly elevated the new user, we can use 'SELECT * FROM mysql.user \G'
## Here we use \G instead of ; or \g to end the query because \G will present the information in an orderly list-like format. We can simply search through the users and find the desired ones and view privilege statuses.

## Now let's create a database to populate with an empty table. First let's log into the account we've just created and elevated. We can type 'exit' or '\q' in mysql to exit back out to the base vm if necessary. To log into an account we can follow structure: 'mysql -u user -p'. -u stands for username and -p stands for password. After entering command, we will be prompted to enter the appropriate password.

## Once we have access to the account, we can check existing databases with: 'show databases;' There should be a few default databases. Let's create one of our own. We have accomplished this with 'CREATE DATABASE cybersalaries;' as the name is relevant to the csv we will use to populate it. We can check that our command went through with 'SHOW DATABASES;'

## We have to be using our new database to create a table within it. Our command will reflect that: 'USE cybersalaries' to shift into it. To create a table, we need to define at least a single column. We have chosen to use:
## 'CREATE TABLE salaries (
##    year int,
##    salary varchar(255)
## );

## The columns we have chosen to define are not too relevant as they will be populated by information we pull from the csv.

## For pushing csv data into the database remotely, refer to the dbconnect.py file.

## NOTE: requirements.txt contains all necessary components for this exercise, including pymysql, sqlalchemy and dotenv