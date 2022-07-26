from flask import Flask, render_template

skkills_app = Flask(__name__)

@skkills_app.route("/")
def home_page():
    # return "Hello From Flask Fremwork "
    return render_template("home_page.html", page_title="Homa Page")

    
@skkills_app.route("/about_page")
def about_page():
    return render_template("/about_page.html", page_title="About Page")
    # return "About From Flask Fremwork "

if __name__ == "__main__":
    # skkills_app.run()
    skkills_app.run(debug=True, port=9000)



