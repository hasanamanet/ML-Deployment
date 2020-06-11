from flask import Flask, render_template,request
import joblib
import numpy as np

import pyodbc
from config.db import cursor
import re


app = Flask(__name__)


@app.route('/')
def home():
    return render_template("home.html")

@app.route("/tahmin", methods = ["POST"])
def tahmin_et():

    model = open("NB_gazete_model.pkl","rb")
    clf = joblib.load(model)
    classes = np.array(["Magazin","Dünya","Spor","Siyaset","Kültür-Sanat","Teknoloji"])

    # veritabanı işleri
    cursor.execute("SELECT icerik FROM haber_metinleri")
    haber_icerik = list(cursor.fetchall())

    tahmin = ""
    for i in range(0,len(haber_icerik)):
        tahmin = clf.predict([str(haber_icerik[i])]).astype(int)
        tahmin = re.sub(r"[\"\'\]\[]", '', str(classes[tahmin]))
        icerik = re.sub(r"[\"()]", '', str(haber_icerik[i]))
        cursor.execute("INSERT INTO haber_kategori_tahmin (metin, kategori_tahmini) VALUES (?, ?)", (icerik), (tahmin)) 
        cursor.commit()
    #conx_string_b = "driver={SQL SERVER}; server=DESKTOP-S5L3657\SQLEXPRESS; database=metin_analizi; trusted_connection=YES;"
    #conx = pyodbc.connect(conx_string_b)
    #cursor = conx.cursor()
    
    mesaj = "yazıldıı"
    #for icerik in haber_icerik:tahmin = str(clf.predict([str(icerik)]))
    


    
    """if request.method == "POST":
        text = request.form["haber_metni"]
        data = [text]
        sonuc = clf.predict(data).astype(int)"""
    return render_template("result.html", prediction = mesaj)

if __name__ == '__main__':
    app.run()
