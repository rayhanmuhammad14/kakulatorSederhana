from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    hasil = None
    if request.method == "POST":
        try:
            hargaBeli = float(request.form["hargaBeli"])
            satuan = float(request.form["satuan"])

            hargaProses = hargaBeli * 11 /100

            harga_modal = hargaBeli + hargaProses

            hargaJual = harga_modal * 25/ 200

            hasilRaw = hargaJual / satuan

            hasil= int(hasilRaw*10)

        except ValueError:
            hasil = "Input tidak valid"

    return render_template("index.html", hasil=hasil)

if __name__ == "__main__":
    app.run(debug=True)
