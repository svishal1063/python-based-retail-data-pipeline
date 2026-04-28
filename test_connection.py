from sqlalchemy import create_engine

DB_URI = "postgresql://postgres:Elijah%40123@localhost:5432/retail_db"

try:
	engine = create_engine(DB_URI)
	connection = engine.connect()
	print("Connection successful")
except Exception as e:
	print("Connection failed")
	print(e)
