import jaydebeapi
import csv

query = input("Type your query:")
query_file = input("Enter a file name to save your query to:")

conn = jaydebeapi.connect("com.infor.idl.jdbc.Driver",
                          "jdbc:infordatalake://NSACOM_DEM:.",
                          {'user':'','pass':''},
                          "C:/Users/compu/OneDrive/Code/VisualStudio/python/DataLake_Conn/infor-compass-jdbc-2020-05.jar",
                          "C:/Users/compu/OneDrive/Code/VisualStudio/python/DataLake_Conn/",
                          )


curs = conn.cursor()

#curs.execute("select * from apsv")
curs.execute(query)

headers = [i[0] for i in curs.description]

result = curs.fetchall()
curs.close()
conn.close()

with open("results/" + query_file + ".csv", "w", newline="", encoding='utf-8') as f:
    csv_writer = csv.writer(f)
    csv_writer.writerow(headers)
    csv_writer.writerows(result)

print(result[0]) 
f.close()


