import sqlite3 as sql

# connect to SQLite
con = sql.connect('db_tokens.db')

# Create a Connection
cur = con.cursor()

# Drop users table if already exist.
cur.execute("DROP TABLE IF EXISTS tokens")

# Create users table  in db_web database
sql = 'CREATE TABLE "tokens" ("uid"	INTEGER PRIMARY KEY AUTOINCREMENT, "token_name" TEXT, "secret"	TEXT, "delta" INT)'
cur.execute(sql)

# commit changes
con.commit()

# close the connection
con.close()
