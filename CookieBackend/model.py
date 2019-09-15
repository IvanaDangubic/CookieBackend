from pony.orm import Database, PrimaryKey, Required, Set, db_session
from uuid import uuid4 as gid


db = Database()



db.bind(provider='sqlite', filename='db.sqlite', create_db=True)

class Korisnik(db.Entity):
    id= PrimaryKey(str)
    Ime = Required(str)
    Prezime = Required(str)
    Username = Required(str)
    Lozinka = Required(str)
    kolaci = Set("Kolac") 

class Kategorija(db.Entity):
    id = PrimaryKey(str)
    Naziv = Required(str)
    kolaci = Set("Kolac") 
class Kolac(db.Entity):
    id= PrimaryKey(str)
    Naziv_kolaca = Required(str)
    sastojci=Required(str)
    priprema=Required(str)
    fotografija=Required(str)
    korisnici = Required(Korisnik)
    kategorije = Required(Kategorija)

db.generate_mapping(check_tables=True, create_tables=True) 


        
