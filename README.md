# s3_trigger_lambda_function_RDMs_project
This project triggers a lambda function that fetches data from s3 and loads it into Mysql database

![Workflow Diagram](https://github.com/kennethchinedu/s3_trigger_lambda_function_RDMs_project/assets/67561307/46da7c93-0335-43c6-a771-b95ecda7c22d)

The aim of this project is to show how data management and integration is seamless in AWS,  by combining Amazon RDS and Amazon S3,
with lambda function in the middle of it all. 


### Quick Recap of the process


1. Create an S3 Bucket: create an S3 bucket to store your data files. Ensure that the bucket's permissions are set correctly to allow access.

2. Configure Amazon RDS: Set up your Amazon RDS instance based on the database engine you're using, such as MySQL, PostgreSQL, or SQL Serverm whatever you want to use.

3. Work On Access Control: Make sure the RDS instance has the necessary permissions to access the S3 bucket. Using the  IAM role you created, with the required permissions and associating it with your RDS instance too.

4. Write The Right SQL Queries: Craft SQL queries to load the data from the S3 files into your Amazon RDS tables. 

5. Keep Eye On Security: Use secret keys or environmental variables where it is necessary to keep things safe.
6. Automate the Process: Sometimes you may require your code to execute within a timeframe, that is where amazon event bridge comes in, or triggers when you want them to execute per action. 
