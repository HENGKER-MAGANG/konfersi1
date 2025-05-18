from flask import Flask, render_template, request
import os

app = Flask(__name__)

mata_uang = ["USD", "EUR", "MYR", "CNY", "KRW", "JPY"]
kurs = [15500, 17000, 3300, 2200, 12, 110]

@app.route('/', methods=['GET', 'POST'])
def index():
    hasil_text = None
    selected_mode = "1"

    if request.method == 'POST':
        mode = request.form.get('mode')
        pilih = int(request.form.get('pilih'))
        jumlah = float(request.form.get('jumlah'))

        selected_mode = mode  # untuk tetap menampilkan mode terpilih

        if mode == '1':
            hasil = jumlah * kurs[pilih]
            hasil_text = f"{jumlah} {mata_uang[pilih]} = {hasil:,.2f} IDR"
        elif mode == '2':
            hasil = jumlah / kurs[pilih]
            hasil_text = f"{jumlah:,.2f} IDR = {hasil:.2f} {mata_uang[pilih]}"
        else:
            hasil_text = "⚠️ Mode tidak valid."

    return render_template('index.html', mata_uang=mata_uang, hasil=hasil_text, selected_mode=selected_mode)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # penting untuk Railway/Render
    app.run(host="0.0.0.0", port=port)
