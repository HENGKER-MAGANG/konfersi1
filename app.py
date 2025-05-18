from flask import Flask, render_template, request
import os

app = Flask(__name__)

# Data mata uang
mata_uang = ["USD", "EUR", "MYR", "CNY", "KRW", "JPY"]
kurs = [15500, 17000, 3300, 2200, 12, 110]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/mata-uang', methods=['GET', 'POST'])
def mata_uang_converter():
    hasil_text = None
    if request.method == 'POST':
        mode = request.form.get('mode')
        pilih = int(request.form.get('pilih'))
        jumlah = float(request.form.get('jumlah'))

        if mode == '1':
            hasil = jumlah * kurs[pilih]
            hasil_text = f"{jumlah} {mata_uang[pilih]} = {hasil:.2f} IDR"
        elif mode == '2':
            hasil = jumlah / kurs[pilih]
            hasil_text = f"{jumlah} IDR = {hasil:.2f} {mata_uang[pilih]}"
        else:
            hasil_text = "Mode tidak valid."

    return render_template('mata_uang.html', mata_uang=mata_uang, hasil=hasil_text)

@app.route('/suhu', methods=['GET', 'POST'])
def suhu_converter():
    suhu_list = ["Celsius", "Fahrenheit", "Kelvin"]
    result = None

    if request.method == 'POST':
        try:
            suhu_awal = int(request.form["suhu_awal"])
            suhu_tujuan = int(request.form["suhu_tujuan"])
            nilai_suhu = float(request.form["nilai_suhu"])

            if suhu_awal == 1 and suhu_tujuan == 2:
                hasil = (nilai_suhu * 9/5) + 32
            elif suhu_awal == 1 and suhu_tujuan == 3:
                hasil = nilai_suhu + 273.15
            elif suhu_awal == 2 and suhu_tujuan == 1:
                hasil = (nilai_suhu - 32) * 5/9
            elif suhu_awal == 2 and suhu_tujuan == 3:
                hasil = (nilai_suhu - 32) * 5/9 + 273.15
            elif suhu_awal == 3 and suhu_tujuan == 1:
                hasil = nilai_suhu - 273.15
            elif suhu_awal == 3 and suhu_tujuan == 2:
                hasil = (nilai_suhu - 273.15) * 9/5 + 32
            elif suhu_awal == suhu_tujuan:
                hasil = nilai_suhu

            result = {
                "dari": suhu_list[suhu_awal - 1],
                "ke": suhu_list[suhu_tujuan - 1],
                "nilai": nilai_suhu,
                "hasil": round(hasil, 2)
            }
        except:
            result = {"error": "Input tidak valid."}

    return render_template("suhu.html", suhu_list=suhu_list, result=result)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 3000))
    app.run(debug=False, host='0.0.0.0', port=port)
