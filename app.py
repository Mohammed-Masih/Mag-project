from flask import *
from database.sqlitedbmain import Qry, qry
import json
from werkzeug.datastructures import ImmutableMultiDict
from flask import Flask, render_template, url_for, request
import uuid
app = Flask(__name__)

app.config["TEMPLATE_AUTO_RELOAD"] = True
app.config["SECRET_KEY"] = "mag@1234"

@app.route('/admin')
def admin():
    return render_template('admin.html')

@app.route('/')
def home():
     return render_template('index.html')


@app.route('/bookings')
def bookings():
    return render_template('bookings.html')

@app.route('/about-us')
def about_us():
    return render_template('about-1.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/coming-soon')
def coming_soon():
    return render_template('coming-soon-1.html')

@app.route('/error-404')
def error_404():
    return render_template('error-404.html')

@app.route('/gallery')
def gallery():
    return render_template('gallery-grid-3.html')

@app.route('/privacy-policy')
def privacy_policy():
    return render_template('privacy-policy.html')

@app.route('/football')
def football():
    return render_template('football.html')

@app.route('/cricket')
def cricket():
    return render_template('cricket.html')

@app.errorhandler(404) 
def invalid_route(e): 
    return render_template("error-404.html", page='404')




def get_json(request):
    data = request.form.to_dict(flat=False)    
    return json.loads(list(data.keys())[0])




@app.route("/sign-in", methods=["GET", "POST"])
def sign_in():
    if request.method == "POST":
        json_data = get_json(request)
        fullname = json_data['fullname']
        email = json_data['email']
        phone = json_data['phone']
        address = json_data['address']
        city = json_data['city']
        username = json_data['username']
        password = json_data['password']

        userid = str(uuid.uuid1())
        qry.run(f"""
                INSERT into user ('userid', 'fullname', 'email', 'phone', 'address', 'city', 'username', 'password') values(
                    '{userid}',  '{fullname}', '{email}', '{phone}', '{address}', '{city}', '{username}', '{password}'
                )
        """)


        qry.commit()

        session['user'] = email
        session['userid'] = userid

        return redirect("/")


    return render_template("sign-in.html", page = "Sign In")




@app.route("/auth" , methods = ["GET", "POST"])
def auth():
    if request.method == "POST":
        print("=========data============")
        # data = request.form
        
        # data = data.to_dict(flat=False)
        # json_data = json.loads(list(data.keys())[0])
        # print(json_data)
        email = request.form['email']
        password = request.form['password']
        if len(qry.run(f"select * from user where email='{email}' and password='{password}';").getList()) >= 1:
            session['user'] = email
            return {"status" : "DONE"}
            # return redirect{"/"}
        else:
            return {"status" : "USERNAME OR PASSWORD IS INCORRECT"}
        














if __name__ == "__main__":
    app.run(debug=True, port=5000)