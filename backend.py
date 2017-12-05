import sqlite3

def connect():
    conn=sqlite3.connect("vehicles.db")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS vehicle (id INTEGER PRIMARY KEY, make text, model text, year integer, vehicleID char(8))")
    conn.commit()
    conn.close()

def insert(make,model,year,vehicleID):
    conn=sqlite3.connect("vehicles.db")
    cur=conn.cursor()
    cur.execute("INSERT INTO vehicle VALUES (NULL,?,?,?,?)",(make,model,year,vehicleID))
    conn.commit()
    conn.close()

def view():
    conn=sqlite3.connect("vehicles.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM vehicle")
    rows=cur.fetchall()
    conn.close()
    return rows

def search(make="",model="",year="",vehicleID=""):
    conn=sqlite3.connect("vehicles.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM vehicle WHERE make=? OR model=? OR year=? OR vehicleID=?", (make,model,year,vehicleID))
    rows=cur.fetchall()
    conn.close()
    return rows

def delete(id):
    conn=sqlite3.connect("vehicles.db")
    cur=conn.cursor()
    cur.execute("DELETE FROM vehicle WHERE id=?",(id,))
    conn.commit()
    conn.close()

def update(id,make,model,year,vehicleID):
    conn=sqlite3.connect("vehicles.db")
    cur=conn.cursor()
    cur.execute("UPDATE vehicle SET make=?, model=?, year=?, vehicleID=? WHERE id=?",(make,model,year,vehicleID,id))
    conn.commit()
    conn.close()

connect()
