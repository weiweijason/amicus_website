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

PRODUCTS = {
    "ac": [
        {
            "name": "AC 長版風扇",
            "code": "Series AC-L",
            "image": "jpg/long_AC.jpg",
            "desc": "長版交流風扇，適合需要較長風道的機櫃與通道型導流設備，提供高靜壓、穩定連續的送風能力，適用於工業排氣與通風換氣場合。",
            "spec": "AC 100 ~ 240V",
            "badge": "長版",
        },
        {
            "name": "AC 短版風扇",
            "code": "Series AC-S",
            "image": "jpg/shortAC.jpg",
            "desc": "短版緊湊型交流風扇，空間利用效率高，尺寸精簡不失風量，適合機箱嵌入式、面板安裝及各類家電散熱排氣需求。",
            "spec": "AC 100 ~ 240V",
            "badge": "短版",
        },
    ],
    "dc": [
        {
            "name": "DC 大型風扇",
            "code": "Series DC-XL",
            "image": "jpg/big_DC.jpg",
            "desc": "大型 DC 無刷風扇，高風量高靜壓輸出，專為伺服器機房、資料中心及大型工控設備打造，支援 PWM 智慧調速，壽命長、可靠性高。",
            "spec": "12V / 24V / 48V DC",
            "badge": "大型",
        },
        {
            "name": "DC 中型風扇",
            "code": "Series DC-M",
            "image": "jpg/medium_DC.jpg",
            "desc": "中型 DC 無刷風扇，風量與靜壓均衡，廣泛應用於工業自動化、醫療設備、通訊機箱及精密儀器的散熱整合方案。",
            "spec": "12V / 24V DC",
            "badge": "中型",
        },
        {
            "name": "DC 小型風扇",
            "code": "Series DC-S",
            "image": "jpg/small_DC.jpg",
            "desc": "小型 DC 無刷風扇，輕量緊湊設計，適合嵌入式系統、IoT 裝置、車用電子及各類需要低功耗精密散熱的應用場景。",
            "spec": "5V / 12V DC",
            "badge": "小型",
        },
    ],
    "accessory": {
        "name": "防護網罩",
        "code": "Guard Mesh",
        "image": "jpg/bonus.jpg",
        "desc": "可選配加裝於全系列 AC / DC 風扇，有效防止異物與手指接觸旋轉葉片，大幅提升設備安全性。採用高強度金屬網格製成，不影響整體風量表現，並可依客戶需求提供客製規格服務。",
    },
}

APPLICATIONS = [
    {"name": "AI 伺服器與資料中心", "icon": "🖥️"},
    {"name": "車用電子與充電設備", "icon": "🚗"},
    {"name": "醫療設備與空氣淨化", "icon": "🏥"},
    {"name": "工業自動化與電力控制", "icon": "⚙️"},
    {"name": "通訊基站與網路設備", "icon": "📡"},
    {"name": "精密儀器與嵌入式系統", "icon": "🔬"},
]

# ---------- English versions ----------

PRODUCTS_EN = {
    "ac": [
        {
            "name": "AC Long Fan",
            "code": "Series AC-L",
            "image": "jpg/long_AC.jpg",
            "desc": "Long-form AC fan engineered for cabinets and ducted airflow systems. Delivers sustained high static pressure for industrial ventilation and exhaust applications.",
            "spec": "AC 100 ~ 240V",
            "badge": "Long",
        },
        {
            "name": "AC Short Fan",
            "code": "Series AC-S",
            "image": "jpg/shortAC.jpg",
            "desc": "Compact AC fan with maximum space efficiency. Perfect for chassis-embedded or panel-mount installations in appliances and industrial enclosures.",
            "spec": "AC 100 ~ 240V",
            "badge": "Short",
        },
    ],
    "dc": [
        {
            "name": "DC Fan — Large",
            "code": "Series DC-XL",
            "image": "jpg/big_DC.jpg",
            "desc": "Heavy-duty DC brushless fan delivering high airflow and static pressure. Built for server rooms, data centers, and large industrial equipment. PWM speed control supported.",
            "spec": "12V / 24V / 48V DC",
            "badge": "Large",
        },
        {
            "name": "DC Fan — Medium",
            "code": "Series DC-M",
            "image": "jpg/medium_DC.jpg",
            "desc": "Mid-size DC brushless fan with balanced airflow and pressure. Widely deployed in industrial automation, medical devices, telecom enclosures, and precision instruments.",
            "spec": "12V / 24V DC",
            "badge": "Medium",
        },
        {
            "name": "DC Fan — Small",
            "code": "Series DC-S",
            "image": "jpg/small_DC.jpg",
            "desc": "Compact DC brushless fan with lightweight design. Ideal for embedded systems, IoT devices, automotive electronics, and low-power precision cooling applications.",
            "spec": "5V / 12V DC",
            "badge": "Small",
        },
    ],
    "accessory": {
        "name": "Protective Guard Mesh",
        "code": "Guard Mesh",
        "image": "jpg/bonus.jpg",
        "desc": "Optional add-on compatible with all AC and DC fan series. Prevents foreign objects and fingers from contacting rotating blades, significantly improving equipment safety. Manufactured from high-strength metal mesh with minimal impact on airflow performance. Custom sizes available upon request.",
    },
}

APPLICATIONS_EN = [
    {"name": "AI Servers & Data Centers", "icon": "🖥️"},
    {"name": "Automotive Electronics & EV Chargers", "icon": "🚗"},
    {"name": "Medical Equipment & Air Purification", "icon": "🏥"},
    {"name": "Industrial Automation & Power Control", "icon": "⚙️"},
    {"name": "Telecom Base Stations & Network Devices", "icon": "📡"},
    {"name": "Precision Instruments & Embedded Systems", "icon": "🔬"},
]


@app.route("/")
def index() -> str:
    """Render the main landing page (Chinese).

    Returns:
        Rendered HTML string for the index page.
    """
    contact_status = request.args.get("contact_status", "")

    return render_template(
        "index.html",
        products=PRODUCTS,
        applications=APPLICATIONS,
        company=COMPANY_PROFILE,
        contact_status=contact_status,
    )


@app.route("/en/")
def index_en() -> str:
    """Render the English landing page.

    Returns:
        Rendered HTML string for the English index page.
    """
    contact_status = request.args.get("contact_status", "")

    return render_template(
        "index_en.html",
        products=PRODUCTS_EN,
        applications=APPLICATIONS_EN,
        company=COMPANY_PROFILE,
        contact_status=contact_status,
    )


@app.route("/en/about")
def about_en() -> str:
    """Render the English about page.

    Returns:
        Rendered HTML string for the English about page.
    """
    return render_template("about_en.html", company=COMPANY_PROFILE)


@app.route("/about")
def about() -> str:
    """Render the about page (Chinese).

    Returns:
        Rendered HTML string for the about page.
    """
    return render_template("about.html", company=COMPANY_PROFILE)


@app.post("/contact")
def contact_submit():
    """Handle contact form submission (Chinese).

    Returns:
        Redirect response to the index page with contact status.
    """
    name = request.form.get("name", "").strip()
    company_name = request.form.get("company_name", "").strip()
    requirement = request.form.get("requirement", "").strip()

    if not name or not company_name or not requirement:
        return redirect(url_for("index", contact_status="error", _anchor="contact"))

    return redirect(url_for("index", contact_status="ok", _anchor="contact"))


@app.post("/en/contact")
def contact_submit_en():
    """Handle contact form submission (English).

    Returns:
        Redirect response to the English index page with contact status.
    """
    name = request.form.get("name", "").strip()
    company_name = request.form.get("company_name", "").strip()
    requirement = request.form.get("requirement", "").strip()

    if not name or not company_name or not requirement:
        return redirect(url_for("index_en", contact_status="error", _anchor="contact"))

    return redirect(url_for("index_en", contact_status="ok", _anchor="contact"))


if __name__ == "__main__":
    app.run(debug=True)
