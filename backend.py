import sqlite3

class DataBase:
    """docstring for DataBase."""
    def __init__(self,db):
        self.conn=sqlite3.connect("vehicles.db")
        self.cur=self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS vehicle (id INTEGER PRIMARY KEY, make text, model text, year integer, vehicleID char(8))")
        self.conn.commit()

    def insert(self,make,model,year,vehicleID):
        self.cur.execute("INSERT INTO vehicle VALUES (NULL,?,?,?,?)",(make,model,year,vehicleID))
        self.conn.commit()

    def view(self):
        self.cur.execute("SELECT * FROM vehicle")
        rows=self.cur.fetchall()
        return rows

    def search(self,make="",model="",year="",vehicleID=""):
        self.cur.execute("SELECT * FROM vehicle WHERE make=? OR model=? OR year=? OR vehicleID=?", (make,model,year,vehicleID))
        rows=self.cur.fetchall()
        return rows

    def delete(self,id):
        self.cur.execute("DELETE FROM vehicle WHERE id=?",(id,))
        self.conn.commit()

    def update(self,id,make,model,year,vehicleID):
        self.cur.execute("UPDATE vehicle SET make=?, model=?, year=?, vehicleID=? WHERE id=?",(make,model,year,vehicleID,id))
        self.conn.commit()

    def __del__(self):
        self.conn.close()
