from flask import Flask, render_template,request
import joblib
import numpy as np

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("home.html")

@app.route("/tahmin", methods = ["POST"])

def tahmin_et():

    model = open("NB_gazete_model.pkl","rb")
    clf = joblib.load(model)
    classes = np.array(["Magazin","Dünya","Spor","Siyaset","Kültür-Sanat","Teknoloji"])
    if request.method == "POST":
        text = request.form["haber_metni"]
        data = [text]
        sonuc = clf.predict(data).astype(int)
    return render_template("result.html", prediction = classes[sonuc])

if __name__ == '__main__':
    app.run()
