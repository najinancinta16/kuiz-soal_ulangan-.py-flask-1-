from flask import Flask, render_template

app = Flask(__name__)   

data={
    "nama": "Najinan Cinta Luqyana G",
    "alamat": "PayaBedi",
    "jenis_kelamin": "Perempuan",
    "pekerjaan": "Siswa",
    "tempat_lahir": "Langsa",
    "tanggal_lahir": "16 December 2008",
}
@app.route('/')
def index():
    return render_template('index.html',tittle="Halaman Index", isi="Selamat Datang di website flask")

@app.route('/about')
def about():
    return render_template('about.html',tittle="Halaman About", isi="Selamat Datang di Halaman About")

@app.route('/biodata')
def biodata():
    return render_template('biodata.html', tittle="Biodata", isi=data)
    

if __name__ == '__main__':
    app.run(debug=True)