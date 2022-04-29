from flask import Flask,render_template
app=Flask(__name__)
@app.route("/")
def running():
    return render_template("index.html")

if __name__=="__main__":
    app.run(debug=True)
# you should end all the running of the terminal then you could run it.