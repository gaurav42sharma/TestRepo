# Project TestRepo

# Challenge 1

AWS three-tier architecture setup using Terraform code. 

**Provider.tf** : To setup AWS provider in terraform code

**Main.tf** : Complete terraform code to deploy VPC, Internet gateway, Appication Load balancer, Public subnets, Private subnets EC2 instances, Security groups, RDS database

**Variables.tf** : To store variables used in main.tf code

**Outputs.tf** : To print ALB DNS output after infrasctructure is deployed using terraform

**AWS_three_tier_architecture_diagram.png** : Visual representation of three-tier architecture

**Note** : This code can also be broken into terraform modules for simplification and code management for reusability. However above code is also reusable since we are using variables.tf file to save variable values which is only required to change in case reusing this code.

# Challenge 2

**script.py** : Python script to traverse through Instance metadata and print the same in JSON format (see JPG file for real time output)

**script_result.jpg** : Output for script.py on local EC2 instance

**pyscr.py** : Python script to retrieve output based on key value provided (see JPG file for real time output)

**pyscr.jpg** : Output for pyscr.py providing key value and return data based on key value

# Challenge 3

**python_dict_func.py** : Python script to traverse through nested object. 

Code logic: Creating function to traverse through nested object using for loop. For example, if input is provided as {'a':{'b':{'c':'d'}}}, this function will traverse from 1st key to 2nd key to 3rd key and so on. This will print key next to which input is provided. For e.g in above example, if you give ['a','b','c'] value returned will be 'd' and if there is no value then it will print 'none' as default value. Please see JPG file attached for real time output.

**python_dict_func.jpg** : Output of python_dict_func.py script for sample values
