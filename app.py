from xml.dom.minidom import Element
from flask import Flask,request,redirect
import requests

app = Flask(__name__)



@app.route("/",methods=["GET"])
def index():
    output = []
    while (len(output) < 25):
        element = requests.get("https://api.chucknorris.io/jokes/random").json()
        has_in_list = False
        for item in output:
            if element["id"] == item["id"]:
                 has_in_list = True
        if not has_in_list:
            output.append(element)
            
    return output

