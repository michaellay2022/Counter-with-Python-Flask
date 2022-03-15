from flask import Flask, render_template, redirect, request, session
app = Flask(__name__)
app.secret_key = "keyforcounter"

# // ========Root route - render the html==//


@app.route("/")
def index():
    if 'counter' in session:
        session["counter"] = session["counter"]+1
        # print('key exists!')
    else:
        # print("key 'key_name' does NOT exist")
        session["counter"] = 0

    return render_template("index.html", counter=session["counter"])

# // ====Process the counter
# @app.route("/counting")
# def counting():
#     session["counter"] = session["counter"]+1
#     return render_template("index.html", counter=session["counter"])
# #// ====Reset =======


@app.route("/increase_by2")
def increase():
    session["counter"] = session["counter"]+2
    return render_template("index.html", counter=session["counter"])


@app.route("/destroy_session")
def reset():
    session.clear()
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)
