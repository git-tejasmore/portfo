import email
from pdb import post_mortem
from statistics import mode
from flask import Flask,render_template, request, redirect
import csv

apps = Flask(__name__)

@apps.route("/")
def my_home():
    return render_template('index.html')

@apps.route("/index.html")
def my_home2():
    return render_template('index.html')

@apps.route("/<string:page_name>")
def html(page_name):
    return render_template(page_name)


#@apps.route("/favicon")
#def about():
 #   return 

@apps.route("/blog")
def blog():
    return "<p>This is a blog post</p>"

@apps.route("/blog/2022-Billionare-Born")
def b2b():
    return "<p>Soon my life will be changing and I will have 10 Billion US Dollars</p>"

def write_to_file(data):
    with open('database.txt', mode='a') as database:
        email = data["email"]
        subject = data["subject"]
        msg = data["message"]
        file = database.write(f'\n{email},{subject},{msg}')

def write_to_csv(data):
    with open('database.csv', mode='a') as database2:
        email = data["email"]
        subject = data["subject"]
        msg = data["message"]
        csv_writer = csv.writer(database2, delimiter = ',', quotechar='"',quoting= csv.QUOTE_MINIMAL)
        csv_writer.writerow([email,subject,msg])

@apps.route('/contact_form', methods=['POST', 'GET'])
def contact_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        write_to_csv(data)
        return redirect('/thankyou.html')
    else:
        return 'something went wrong'