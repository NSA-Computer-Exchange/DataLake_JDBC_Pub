# DataLake_JDBC_Pub
Data Lake connection using the JDBC driver

NSA Professional Services
Rob Thayer - rob.thayer@nsacom.com


## Steps to configure and run a query:
1. Create a directory on your system to hold the JDBC Driver and the IONAPI credential file. 
2. Download the Infor Compass JDBC driver from your tenant.  `IONDesk > Configuration > Downloads > Compass JDBC Driver` to the directory created in step 1.
3. Create a backend service in Infor ION API. `Infor ION API > Authorized Apps > Non-Infor New Authorized App > Backend Service` 
4. Save your ION API credentials to the directory created in step 1 and name it exactly as shown: **`Infor Compass JDBC Driver.ionapi`**
