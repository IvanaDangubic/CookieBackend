from model import Korisnik,Kategorija,Kolac
from pony.orm import db_session, select
from uuid import uuid4 as gid


class Kolaci:  
    @db_session()
    def listaj():
        q = select(s for s in Kolac) 
        data = [x.to_dict() for x in q]
        return data,

    @db_session
    def dodaj(s):
        try:
            s["id"] = str(gid())
            s = Kolac(**s)
            return True, None
        except Exception as e: 
            return False, str(e)
  
class Korisnici:
    @db_session()
    def listaj():
        q = select(s for s in Korisnik) 
        data = [x.to_dict() for x in q]
        return data,

    @db_session
    def dodaj(s):
        try:
            s["id"] = str(gid())
            s = Korisnik(**s)
            return True, None
        except Exception as e:
            return False, str(e)

class Kategorije:
    @db_session()
    def listaj():
        q = select(s for s in Kategorija)
        data = [x.to_dict() for x in q]
        return data,



