# FastApiServer
First step in FastApi

#Install dependens

1. Install modules from "requirements.txt"
2. The work was done on a database with the parameters host= "0.0.0.0", port=27017
3. If you want to change the database connection settings in the project depending on the approach you have chosen for the demonstration (mongoengine or pymongo) , you need to edit the settings file data modules_for_working/db_modules/mongoengine_chouse/settings_db.py or modules_for_working/db_modules/pymongo_chouse/settings_db.py
4. Use backup of the users "collection.json" in the database under the name "test"
5. If you want to change the application settings edit the file "modules_for_working/server/settings_server.py"

#Run application for demonstation

1. Run database server by MongoDB on localhost port=27017(default)
2. Run manage_application.py
3. Run three test-server-app from far_server: server1.py, server2.py, server3.py on ports 3001, 3002, 3003
4. For view works routings go to localhost:5000/docs in your browser

#Info data to login

User with extended rights-login:admin, pass:1234

User without extended rights-login:test1, pass:1234
