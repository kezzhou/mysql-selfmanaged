# mysql-selfmanaged
HHA 504 // Week 6 // Assignment 5

## This repo focuses on spinning up virtual machines, creating databases with mysql within those vms, and then connecting to those virtual machines via python and subsequently inserting data into the databases.

## For this example we choose to use Azure. Azure's ssh connection process is tedious at first but actually becomes quite routine with frequent use. In addition, it's convenient to have the environment within the user's native Terminal or Cmd Prmpt. Lastly, Azure's process for creating rules for opening ports for connection (specifically 3306 for mysql) is decidedly simpler than GCP's process.

## There are a few ways to go about starting the process but we choose to create the virtual machine and set up mysql there first.

## When creating a machine suitable for this exercise and similar mysql purposes, it's important to keep a few parameters in mind. We prefer our operating size to be Linux (Ubuntu). We want size to be a little larger than our typical test or scratch environments created up till now. As opposed to a micro machine size, we want to select a more mid-tier size (in this case we choose Standard B2). A good rule of thumb is to look for a size with 2 vcpus. We can leave port traffic rules as default, as we will be creating a custom rule afterwards.

## after creating our machine and starting it, we can turn our attention to creating a custom traffic rule so that we can properly connect to the vm from other machines via mysql to populate databases within that vm. Within Azure, having navigated to the virtual machines section, we can click on the machine we intend to use for the exercise. Within the left side bar that appears, we navigate to networking under settings. We can then simply click Add Inbound Port Rule. For source, we can keep Any. For source port ranges, we type '*' to signify All. For destination port ranges, we type '3306' for mysql access specifically. The rest of the parameters can be kept as default values. Now our vm is ready for inbound connections through port 3306.

