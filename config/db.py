import pyodbc as db

server = 'DESKTOP-S5L3657\SQLEXPRESS'
database = 'metin_analizi'
username = 'root'
password = '1234'
port = 1433
driver = '{SQL SERVER}'


connectionstring = f'DRIVER={driver};SERVER={server};PORT={port};DATABASE={database};UID={username};PWD={password}; trusted_connection=YES'

connection = db.connect(connectionstring)
cursor = connection.cursor()