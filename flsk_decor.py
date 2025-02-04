from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def films():
   return render_template("index.html", caption="Фильмы про Гарри", link="Посмотреть фильм")

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/shablon")
def films2():
    return render_template("index.html", caption="Гарри Поттер", link="Перейти в кинотеатр")

@app.route("/person/")
def person():
    return render_template("main.html")

if __name__ == "__main__":
    app.run()
