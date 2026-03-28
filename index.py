from flask import Flask, render_template,request
from datetime import datetime
import math
app = Flask(__name__)

@app.route("/")
def index():
    link = "<h1>資訊管理導論(馬崇恩)</h1>"
    link += "<a href=/mis>課程</a><hr>"
    link += "<a href=/today>現在日期時間</a><hr>"
    link += "<a href=/welcome?u=崇恩&=靜宜資管&=資訊管理導論>Get傳</a><hr>"
    link += "<a href=/me>關於我</a><hr>"
    link += "<a href=/math>次方與根號計算</a><hr>" 
    return link
@app.route("/math", methods=["GET", "POST"])
def math_calc():
    if request.method == "POST":
        try:
            x = float(request.form["x"])
            y = float(request.form["y"])
            opt = request.form["opt"]
            
            if opt == "pow":
                res = math.pow(x, y)
                result = f"{x} 的 {y} 次方為：{res}"
            elif opt == "root":
                # 根號即為 x 的 (1/y) 次方
                res = math.pow(x, 1/y)
                result = f"{x} 的 {y} 次方根為：{res}"
            else:
                result = "未知運算"
        except Exception as e:
            result = "輸入錯誤，請確保輸入的是數字。"
            
        return result
    else:
        return render_template("math.html")
@app.route("/mis")
def course():
    return "<h1>資訊管理導論</h1>"

@app.route("/today")
def today():
    now = datetime.now()
    return render_template("today.html",datetime = str(now))
@app.route("/me")
def me():
    now = datetime.now()
    return render_template("mis2026 B.html")
@app.route("/welcome", methods=["GET"])
def welcome():
    user = request.values.get("nick")
    return render_template("welcome.html", name=user)
@app.route("/account", methods=["GET", "POST"])
def account():
    if request.method == "POST":
        user = request.form["user"]
        pwd = request.form["pwd"]
        result = "您輸入的帳號是：" + user + "; 密碼為：" + pwd 
        return result
    else:
        return render_template("account.html")


if __name__ == "__main__":
    app.run(debug=True)
