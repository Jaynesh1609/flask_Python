from flask import Flask, render_template
import os
import subprocess

#for class u need to give __init__
app = Flask("myapp")   

#for the experiment 

@app.route("/date")
def date():
    data = subprocess.getoutput("<h3>date /t </h3>")
    return(data)

#page for form only
@app.route("/form")
def form():
    return  render_template("myform.html" )   #when we don't need to change the name
   
#page for new file
@app.route("/menu", methods= ['GET'] )   #fetching value from form.html
def menu():
    Name = request.args.get("x")    #upadating the name accdingly
    c    = request.args.get("y")    # from get we take value from y its args of class request
    #myname = 'jack'
    menu = render_template("menu.html",   myname = Name ,  cname = c  )
    return menu

#we have to sue decortaor over here
@app.route("/search")
def mysearch():
    #we can also put full html code here
    return("<b>search</b>")     #return over here soo msg reach to clients
    #print("search")

@app.route("/email")
def myeamil():
    return  render_template("menu.html")
