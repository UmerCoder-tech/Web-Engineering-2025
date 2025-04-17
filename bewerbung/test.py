import MySQLdb

db = MySQLdb.connect(
    host="localhost",
    user="root",
    passwd="12345",
    db="bewerbungsdatenbank"
)
print("Verbindung erfolgreich!")
db.close()
