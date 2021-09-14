# DataLake_JDBC_Pub
Data Lake connection using the JDBC driver

NSA Professional Services
Rob Thayer - rob.thayer@nsacom.com

### Requirements:
1. Python 3.x (may work with Python 2.x but not tested)
2. jaydebeapi library
3. Infor Compass JDBC Driver
4. Infor IONAPI OAuth 2.0 Credentials


### Steps to configure and run a query:
1. Create a directory on your system to hold the JDBC Driver and the IONAPI credential file. 
2. Download the Infor Compass JDBC driver from your tenant.  `IONDesk > Configuration > Downloads > Compass JDBC Driver` to the directory created in step 1.
3. Create a backend service in Infor ION API. `Infor ION API > Authorized Apps > Non-Infor New Authorized App > Backend Service` 
4. Save your ION API credentials to the directory created in step 1 and name it exactly as shown: **`Infor Compass JDBC Driver.ionapi`**
5. Edit the `DataLake_Conn.py` python script and change the `<your_tenant>` and `<driver_path>` sections shown in the `conn` object. 


        conn = jaydebeapi.connect("com.infor.idl.jdbc.Driver",\
                          "jdbc:infordatalake://<your_tenant>:.",\
                          {'user':'','pass':''},\
                          "<driver_path>/infor-compass-jdbc-2020-05.jar",\
                          "<driver_path>/",\
                          )

### Example:

     conn = jaydebeapi.connect("com.infor.idl.jdbc.Driver",\
                          "jdbc:infordatalake://NSACOM_DEM:.",\
                          {'user':'','pass':''},\
                          "/code/datalake/infor-compass-jdbc-2020-05.jar",\
                          "/code/datalake/",\
                          )
6. Leave `user:` & `pass:` blank       

### Running the code
1. Make sure to import the `jaydebeapi` library into your python environment or virtual environment
2. python3 DataLake_Conn.py 
3. You will be prompted to type your query: IE: `SELECT TOP 100 cono, name, custno FROM arsc` 
4. Hit enter
5. Type a name for you results file (minus the extension, the code already assumes the file will be saved as a CSV.)
6. Once the process is complete you will find the results saved in the file you indicated in step 5. in the results/ directory.
