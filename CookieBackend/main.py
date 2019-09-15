from flask import Flask, Response, jsonify, request
from domain import Korisnici,Kolaci,Kategorije
from  flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/korisnici', methods=['GET', 'POST']) 
def handle_korisnici():
    if request.method == 'GET':
        korisnici = Korisnici.listaj() 
        return jsonify({"korisnici":korisnici}) 
    elif request.method == 'POST':
        status, greske = Korisnici.dodaj(request.get_json()) 
        if status:
            return Response(status=201)
        else:
            r = Response(status=500)
            r.set_data(greske)
            return r

@app.route("/kolaci", methods=['GET', 'POST',])
def handle_kolaci():
    if request.method == 'GET':
        kolaci = Kolaci.listaj()
        return jsonify({"kolaci": kolaci})
        
    elif request.method == 'POST':
        print("ovo sam dobila" , request.get_json())
        status, greske = Kolaci.dodaj(request.get_json())  
        if status:
         return Response(status=201)
    else:
        r = Response(status=500)
        r.set_data(greske)
        return r
    


@app.route("/kategorije", methods=['GET'])
def handle_kategorije():
    if request.method == 'GET':
        kategorije = Kategorije.listaj()
        return jsonify({"kategorije": kategorije})
    else:
        r = Response(status=500)
        r.set_data(greske)
        return r

if __name__ == '__main__':
    app.debug = True
    app.run()