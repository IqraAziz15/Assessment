1. For running the server following command will be used:
	python server.py

2. For running the API in Postman and in the browser following are the GET API:
	First API: 'http://127.0.0.1:5000/api/fetchapidata'
	Second API: 'http://127.0.0.1:5000/api/fetchapi2data'
	Third API: 'http://127.0.0.1:5000/api/fetchapi3data'
	Cumulative List: 'http://127.0.0.1:5000/api/getdatafromdb'

3. For Migration, following commands will be used:
	1. Through 'cd' enter into the folder 'api'.
	2. Run 'python coronaapiroutes.py db init'.
	3. Then for migrating, run command 'python coronaapiroutes.py db migrate'.
	4. For upgrading db, run command 'python coronaapiroutes.py db upgrade'.

4. Commands for MYSQL Command Line:
	1. Enter password: qwerty12
	2. For Databases use command: 'show databases;'
	3. For creating db: 'CREATE DATABASE flasktask;'
	4. For using db: 'use flasktask;'
	5. For all the tables: 'show tables;'
	6. For seeing tables columns: 'describe tablename;'
	7. For table data: 'SELECT * from tablename;'
	8. For dropping tables: 'DROP TABLE tablename;'
	9. For altering table: 'ALTER TABLE query;'
	10. Write 'quit' for quitting MYSQL Command Line
