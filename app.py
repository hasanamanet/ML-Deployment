from flask import Flask, render_template,request
import joblib


app = Flask(__name__)


@app.route('/')
def home():
    return render_template("home.html")

@app.route("/tahmin", methods = ["POST"])

def tahmin_et():

    model = open("NB_gazete_model.pkl","rb")
    clf = joblib.load(model)
    tahmin = ""

    if request.method == "POST":
        text = request.form["haber_metni"]
        data = [text]
        sonuc = clf.predict(data)
    if sonuc == [0]:
        tahmin = "Magazin"
    elif sonuc == [1]:
        tahmin = "Dünya"
    elif sonuc == [5]:
        tahmin = "Teknoloji"
    elif sonuc == [3]:
        tahmin = "Siyaset"
    elif sonuc == [4]:
        tahmin = "Kültür - Sanat"
    else:
        tahmin = "Spor"
    return render_template("result.html", prediction = tahmin)

if __name__ == '__main__':
    app.run()
