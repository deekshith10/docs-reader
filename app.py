import PyPDF2
from flask import Flask, render_template,request
app = Flask(__name__)
@app.route("/")
def index():
    return render_template("files.html")

@app.route("/files",methods=["POST"])
def pdf():
    f=request.form.get("myfile")
    pdfReader = PyPDF2.PdfFileReader(f)
    pageObj = pdfReader.getPage(1)
    data=pageObj.extractText()
    return render_template("files.html",data=data)
