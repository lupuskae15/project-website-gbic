from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/profil')
def profil():
    return render_template('profil.html')

@app.route('/jadwal')
def jadwal():
    return render_template('jadwal.html')

@app.route('/berita')
def berita():
    return render_template('berita.html')

@app.route('/renungan')
def renungan():
    return render_template('renungan.html')

@app.route('/khotbah')
def khotbah():
    return render_template('khotbah.html')

@app.route('/kalender')
def kalender():
    return render_template('kalender.html')

@app.route('/pendaftaran', methods=['GET', 'POST'])
def pendaftaran():
    if request.method == 'POST':
        # Logika menerima data formulir pendaftaran jemaat/baptisan
        nama = request.form.get('nama')
        return render_template('pendaftaran.html', success=True, nama=nama)
    return render_template('pendaftaran.html', success=False)

@app.route('/doa', methods=['GET', 'POST'])
def doa():
    # Fitur pokok doa jemaat
    return render_template('doa.html')

@app.route('/galeri')
def galeri():
    return render_template('galeri.html')

@app.route('/kontak')
def kontak():
    return render_template('kontak.html')

if __name__ == '__main__':
    app.run(debug=True)