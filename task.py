from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
@app.route("/main/")
def main():
    context = {"title" : "Главная"}
    return render_template("new_main.html", **context)

@app.route("/clothes/")
def clothes():
    context = {"title" : "Одежда"}
    return render_template("new_clothes.html", **context)

@app.route("/shoes/")
def shoes():
    context = {"title" : "Обувь"}
    return render_template("new_shoes.html", **context)

@app.route("/coat/")
def coat():
    context = {"title" : "Куртка"}
    return render_template("new_coat.html", **context)

if __name__ == "__main__":
    app.run()

