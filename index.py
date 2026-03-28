import math
from flask import Flask, render_template,request
from datetime import datetime
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
@app.route("/math", methods=["GET", "POST"])
def math_calc():
    if request.method == "POST":
        try:
            # 1. 抓取資料
            num_x = float(request.form.get("x"))
            num_y = float(request.form.get("y"))
            opt = request.form.get("opt")
            
            # 2. 判斷邏輯
            if opt == "pow":
                res = num_x ** num_y
                return f"計算結果：{num_x} 的 {num_y} 次方 = {res}"
            elif opt == "root":
                res = num_x ** (1/num_y)
                return f"計算結果：{num_x} 的 {num_y} 次根號 = {res}"
            
        except Exception as e:
            return f"發生錯誤：{e} (請檢查是否輸入正確數字)"
            
    # GET 請求時顯示網頁
    return render_template("math.html")

if __name__ == "__main__":
    app.run(debug=True)
