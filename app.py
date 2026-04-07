from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)
app.config["SECRET_KEY"] = "amicuscc-site-secret"


COMPANY_PROFILE = {
    "name_zh": "銓群實業有限公司",
    "name_en": "AMICUSCC MACHINE CO. LTD",
    "address_zh": "新北市三重區興德路111-1號7樓",
    "address_en": "7 F., No. 111-1, Xingde Rd., Sanchong Dist., New Taipei City 241458, Taiwan (R.O.C.)",
    "phone": "+886 2 85123280",
    "tel_link": "+886285123280",
    "email": "amicuscc@ms46.hinet.net",
    "map_link": "https://maps.google.com/?q=7+F.,+No.+111-1,+Xingde+Rd.,+Sanchong+Dist.,+New+Taipei+City+241458,+Taiwan",
}


@app.route("/")
def index():
    product_lines = [
        {
            "name": "DC 無刷風扇",
            "desc": "適用伺服器、工控與通訊設備，提供高可靠長壽命散熱。",
            "spec": "40mm - 172mm / 5V-48V",
        },
        {
            "name": "EC 智慧節能風機",
            "desc": "高效率驅動架構，兼顧低噪音與高風量，滿足綠能需求。",
            "spec": "80mm - 250mm / PWM 調速",
        },
        {
            "name": "軸流與鼓風模組",
            "desc": "針對高靜壓與導流需求設計，適合醫療與精密儀器。",
            "spec": "客製葉型 / IP55 選配",
        },
    ]

    applications = [
        "AI 伺服器與資料中心",
        "車用電子與充電設備",
        "醫療設備與空氣淨化",
        "工業自動化與電力控制",
    ]

    contact_status = request.args.get("contact_status", "")

    return render_template(
        "index.html",
        product_lines=product_lines,
        applications=applications,
        company=COMPANY_PROFILE,
        contact_status=contact_status,
    )


@app.route("/about")
def about():
    return render_template("about.html", company=COMPANY_PROFILE)


@app.post("/contact")
def contact_submit():
    name = request.form.get("name", "").strip()
    company_name = request.form.get("company_name", "").strip()
    requirement = request.form.get("requirement", "").strip()

    if not name or not company_name or not requirement:
        return redirect(url_for("index", contact_status="error", _anchor="contact-form"))

    return redirect(url_for("index", contact_status="ok", _anchor="contact-form"))


if __name__ == "__main__":
    app.run(debug=True)
