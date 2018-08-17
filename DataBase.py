import sqlite3

class Data_Base():
    def __init__(self):      
        self.conn = sqlite3.connect('emails_data.db')
        self.cur = self.conn.cursor()

    def create_tabel(self):
        with self.conn:
            self.cur.execute("""CREATE TABLE emaildata (
                        Pers_nr integer,
                        Achternaam text,
                        Voornaam text,
                        Adres text,
                        Woonplaats text,
                        Vervoer text,
                        Opmerkingen text,
                        Opdrachtgever text,
                        Woonplaats_werkgever text,
                        Start_tijd text,
                        email text,
                        nationaliteit text
                        )""")

    def insert_transport_data(self,tup):
        with self.conn:
            self.cur.execute("""INSERT INTO emaildata \
            (Pers_nr,Achternaam,Voornaam,Adres,Woonplaats,Vervoer,Opmerkingen,Opdrachtgever,\
            Woonplaats_werkgever,Start_tijd)\
            VALUES (?,?,?,?,?,?,?,?,?,?)""",tup)
    
    def update_transport_data(self,Pers_nr,email,nationaliteit):
        with self.conn:
            self.cur.execute("""UPDATE emaildata SET email = :email , nationaliteit = :nationaliteit\
                             WHERE Pers_nr = :Pers_nr""",\
                             {'Pers_nr' : Pers_nr,'email': email,'nationaliteit' : nationaliteit})
        
    def print_data(self):
        with self.conn:
            self.cur.execute("""SELECT * FROM emaildata """)
            print(self.cur.fetchone)
            
    
    def clear_table(self):
        with self.conn:
            self.cur.execute("""DELETE FROM emaildata""")
            
    def get_data(self):
        with self.conn:
            self.cur.execute("""SELECT * FROM emaildata""")
            return self.cur.fetchall()
        
DB = Data_Base()
try:
    DB.create_tabel()
except:
    pass