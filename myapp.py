from flask import Flask, render_template, url_for

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html", title="Home Page", 
    Page="My home Page", 
    Stuff="This is my home page content for now ") 

@app.route("/about")
def about():
    return render_template("about.html", title="About Page", 
    Page="My About Page", 
    Stuff=" This is my about page stuff for now")

@app.route("/contact")
def contact():
    return render_template("contact.html", title="Contact Page", 
    Page="My Contact Page", 
    Stuff="I'm passing stuff to this Contact page, from the base and app files for now.")

@app.route("/advert")
def advert():
    return render_template("advert.html", title="Advert Page", 
    Page="My Advert Page", Stuff=" Adverts page for now")

@app.route("/test")
def test():
    return render_template("test.html", title="Test Page", 
    Page="My Test Page", Stuff=" My test page stuff for now")

if __name__ == "__main__":
   #app.run()
   app.run(debug=True, host="192.168.1.50", port=5000)
