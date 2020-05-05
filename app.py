import fitz
from flask import Flask, render_template,request
app = Flask(__name__)
@app.route("/")
def index():
    return render_template("files.html")

@app.route("/files",methods=["POST"])
def pdf():
    f=request.form.get("myfile")
    pdfReader = fitz.open(f)
    
    pageObj = pdfReader.loadPage(0)
    data=pageObj.getText()
    return render_template("files.html",data=data)

#PyMuPDF
