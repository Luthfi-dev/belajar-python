import os
from flask import Flask, render_template, request
import cv2
from werkzeug.utils import secure_filename
import random

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/predic', methods=['GET', 'POST'])
def predic():
    return render_template("predic.html")

@app.route('/tescam')
def tes():
    return render_template("tescam.html")

@app.route('/tangkap', methods=['GET','POST'])
def tangkap():
    print(request.form.get('coba'))
    return render_template('tangkap.html')

@app.route('/tesdata', methods=['GET','POST'])
def tesdata():
    print(request.form.get('coba'))
    return "alhamdulillah"

@app.route('/proses', methods=['GET','POST'])
def proses():
    dataGambar = request.form.get('uriGambar') #url gambar hasil capture
    # simpan gambar ke folder
    file = request.files['file']
    filename = str(random.randrange(1,10000)) + ".jpg"
    g = dataGambar + ".jpg"
    file.save(os.path.join('gambar', g))
    print(filename) #file name ini dalah foto hasil gambar dari upload
    # ==================> KODE PROSES DISINI <=====================

    # ==================> END KODE PROSES <========================
    return render_template("proses.html", data=g)




if __name__ == "__main__":
    app.run(debug=True)

