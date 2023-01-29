
from flask import Flask,render_template,request,session, redirect, url_for, flash
import mysql.connector
from flask_fontawesome import FontAwesome
import hashlib
from datetime import datetime
from werkzeug.utils import secure_filename
import os

PRODUCT_IMAGES_UPLOAD_FOLDER = os.path.abspath('static\\images\\product_images\\')
USER_IMAGES_UPLOAD_FOLDER = os.path.abspath('static\\images\\user_images\\')
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

app = Flask(__name__)
fa = FontAwesome(app)
app.config['UPLOAD_PRODUCTS'] = PRODUCT_IMAGES_UPLOAD_FOLDER
app.config['UPLOAD_USERS'] = USER_IMAGES_UPLOAD_FOLDER
app.config['SECRET_KEY'] = "RAF2021-2022"
mydb = mysql.connector.connect(
	host="localhost",
	user="root",
	password="", # ako niste nista menjali u phpmyadminu ovo su standardni
    # username i password
	database="flask_eprod" # iz phpmyadmin 
    )


class Proizvod:
	__id : int
	__naziv : str
	__cena : float
	__opis : str	
	__url_slike : str
	__prodaja : str
	__id_prodavac : int
	__broj_prodatih : int

	def __init__(self, id, naziv, cena, opis, url_slike, prodaja, id_prodavac, broj_prodatih):
		self.__id = id
		self.__naziv = naziv
		self.__cena = cena
		self.__opis = opis		
		self.__url_slike = url_slike
		self.__prodaja = prodaja
		self.__id_prodavac = id_prodavac
		self.__broj_prodatih = broj_prodatih

	def get_id(self):
		return self.__id
		
	def get_naziv(self):
		return self.__naziv

	def get_cena(self):
		return self.__cena

	def get_opis(self):
		return self.__opis

	def get_url_slike(self):
		return self.__url_slike

	def get_u_prodaji(self):
		return self.__prodaja	

	def get_prodavac(self):
		return self.__id_prodavac

	def get_broj_prodatih(self):
		return self.__broj_prodatih

	@staticmethod
	def izvuci_sve_proizvode():
		cursor = mydb.cursor(prepared=True)
		sql = "SELECT * FROM proizvod"
		cursor.execute(sql)
		rez = cursor.fetchall()
		lista_objekata = []
		for i in range(len(rez)):
			proiz_kao_lista = ukini_bytearray(rez[i])
			p1 = Proizvod(
				proiz_kao_lista[0],
				proiz_kao_lista[1],
				proiz_kao_lista[2],
				proiz_kao_lista[3],
				proiz_kao_lista[4],
				proiz_kao_lista[5],
				proiz_kao_lista[6],
				proiz_kao_lista[7]		
			)
			lista_objekata.append(p1)

		return lista_objekata

	@staticmethod
	def izvuci_jedan_proizvod(id):
		cursor = mydb.cursor(prepared=True)
		sql = '''
			 	 SELECT * 
				 FROM proizvod
				 WHERE idProizvod=?
			 '''
		sql_param = (id, )
		cursor.execute(sql, sql_param)
		rez = cursor.fetchone()
		rez = ukini_bytearray(rez)
		p1 = Proizvod(
			rez[0],
			rez[1],
			rez[2],
			rez[3],
			rez[4],
			rez[5],
			rez[6],
			rez[7]
		)
		return p1

	@staticmethod
	def proveri_stanje_velicine(proizvod_id, velicina):
		cursor = mydb.cursor(prepared=True)
		sql = '''
			SELECT *
			FROM lager
			INNER JOIN proizvod
			ON proizvod.idProizvod=lager.idProizvod
			INNER JOIN velicina
			ON velicina.idVelicina=lager.idVelicina
			WHERE velicina.oznaka_velicine=? AND proizvod.idProizvod=?
		'''
		parametri = (velicina, proizvod_id)

		cursor.execute(sql, parametri)
		rez = cursor.fetchall()

		return rez

	@staticmethod
	def update_proizvod(proizvod):
		cursor = mydb.cursor(prepared=True)
		sql = '''
				UPDATE proizvod
				SET
					idProizvod=?,
					naziv_proizvoda=?,
					proizvod_cena=?,
					opis_proizvoda=?,
					url_slike=?,
					u_prodaji=?
				WHERE idProizvod=?
				'''

		parametri = (proizvod.get_id(), proizvod.get_naziv(), proizvod.get_cena(),
					proizvod.get_opis(), proizvod.get_url_slike(), proizvod.get_u_prodaji(),
					proizvod.get_id())
				
		cursor.execute(sql, parametri)
		mydb.commit()

	@staticmethod
	def skini_sa_lagera(proizvod_id, velicina_id, kolicina):
		cursor = mydb.cursor(prepared=True)
		sql = "SELECT * FROM lager WHERE idProizvod=? AND idVelicina=?"
		parametri = (proizvod_id, velicina_id)		

		cursor.execute(sql, parametri)
		lager_proizvoda = cursor.fetchall()
		
		parametri = (kolicina, proizvod_id, velicina_id)
		sql = '''
			UPDATE lager SET
			kolicina=kolicina-? 
			WHERE lager.idProizvod=?
			AND lager.idVelicina=?
		'''										

		cursor.execute(sql, parametri)
		mydb.commit()

	@staticmethod
	def dodaj_na_lager(proizvod_id, velicina_id, kolicina):
		cursor = mydb.cursor(prepared=True)
		sql = "SELECT * FROM lager WHERE idProizvod=? AND idVelicina=?"
		parametri = (proizvod_id, velicina_id)		
		
		cursor.execute(sql, parametri)
		lager_proizvoda = cursor.fetchall()

		cursor = mydb.cursor(prepared=True)
		if lager_proizvoda:
			parametri = (kolicina, proizvod_id, velicina_id)
			sql = '''
				UPDATE lager SET
				kolicina=kolicina+? 
				WHERE lager.idProizvod=?
				AND lager.idVelicina=?
			'''										

		else:
			parametri = (velicina_id, proizvod_id, kolicina)
			sql = '''
				INSERT INTO lager
				VALUES (?, ?, ?)
			'''

		cursor.execute(sql, parametri)
		mydb.commit()
	
	@staticmethod 
	def dodaj_broj_prodatih(proizvod_id, kolicina):
		cursor = mydb.cursor(prepared=True)
		sql = '''
			UPDATE proizvod 
			SET
				broj_prodatih=broj_prodatih+?
			WHERE idProizvod=?
		'''
		parametri = (kolicina, proizvod_id)
		cursor.execute(sql, parametri)
		mydb.commit()

	def top_lista_proizvoda():
		cursor = mydb.cursor(buffered=True)
		sql = '''
			SELECT * 
			FROM proizvod
			WHERE proizvod.u_prodaji='da'
			ORDER BY proizvod.broj_prodatih DESC
			LIMIT 6
		'''
		lista_proizvoda = []
		cursor.execute(sql)
		rez = cursor.fetchall()
		for i in range(len(rez)):
			proizvod_lista = ukini_bytearray(rez[i])
			p = Proizvod(
							proizvod_lista[0],
							proizvod_lista[1],
							proizvod_lista[2],
							proizvod_lista[3],
							proizvod_lista[4],
							proizvod_lista[5],
							proizvod_lista[6],
							proizvod_lista[7]
						)
			lista_proizvoda.append(p)
		cursor.close()
		return lista_proizvoda

class Korisnik:
	id : int
	username : str
	lozinka : str
	ime_prezime : str
	datum_registracije : str
	adresa : str
	broj_telefona : str
	email : str
	url_profilna : str
	stanje : float

	def __init__(self, id, username, lozinka, ime_prezime, datum_reg,
				 adresa, broj_telefona, email, url_profilna, stanje):
		self.id = id
		self.username = username
		self.lozinka = lozinka
		self.ime_prezime = ime_prezime
		self.datum_registracije = datum_reg
		self.adresa = adresa
		self.broj_telefona = broj_telefona
		self.email = email
		self.url_profilna = url_profilna
		self.stanje = stanje

	def select_svi_korisnici():
		cursor = mydb.cursor(prepared=True)
		sql = "SELECT * FROM korisnik"
		cursor.execute(sql)
		rez = cursor.fetchall()
		for i in range (len(rez)):
			rez[i] = ukini_bytearray(rez[i])
		
		return rez

	def korisnik_register(username, email, password, confirm_password, ime_prezime, adresa, broj_telefona, url_slike):

		cursor = mydb.cursor(prepared=True)
		sql = "SELECT * FROM korisnik WHERE korisnicko_ime=?"
		parametri = (username, )
		cursor.execute(sql, parametri)
		korisnik = cursor.fetchall()
		
		password = password.encode()
		password = hashlib.sha256(password).hexdigest()

		datum = datetime.today()
		
		tip_korisnika = '3'
		trenutno_stanje = 0
		sql_insert = "INSERT INTO korisnik VALUES (null, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
		parametri_insert = (username, password, ime_prezime, datum, adresa, broj_telefona, email, tip_korisnika, url_slike, trenutno_stanje)
		cursor.execute(sql_insert, parametri_insert)	
		
		mydb.commit()							
		    
	def kreiraj_korpu(id):
		cursor = mydb.cursor(prepared=True)
		sql = "INSERT INTO porudzbina VALUES(null, ?, ?, ?)"
		parametri = (id, datetime.now(), "korpa")
		cursor.execute(sql, parametri)
		mydb.commit()
		sql = "SELECT * FROM porudzbina WHERE porudzbina.Korisnik_iDkorisnik=? AND porudzbina.stanje_porudzbine='korpa'"
		parametri = (id, )
		cursor.execute(sql, parametri)
		rez = cursor.fetchone()
		rez = ukini_bytearray(rez)
		return rez[0]

	def kreiraj_stavku_korpe(proizvod_id, korpa_id, velicina):
		cursor = mydb.cursor(prepared=True)	
		sql = '''
			SELECT idVelicina
			FROM velicina 
			WHERE oznaka_velicine=?
		'''
		parametri=(velicina, )
		cursor.execute(sql, parametri)
		id_velicina = cursor.fetchone()

		sql = "INSERT INTO stavkaporudzbine VALUES(?, ?, ?, ?)"
		kolicina = 1		
		parametri = (korpa_id, proizvod_id, kolicina, id_velicina[0])
		cursor.execute(sql, parametri)
		mydb.commit()


	def korisnik_login(username, password):
		cursor = mydb.cursor(prepared=True)
		sql_check_korisnik = "SELECT * FROM korisnik WHERE korisnicko_ime=?"
		parametri_check_korisnik = (username, )
		cursor.execute(sql_check_korisnik, parametri_check_korisnik)
		korisnik = cursor.fetchone()
		
		if not korisnik:
			return False		
		
		korisnik = ukini_bytearray(korisnik)		
		password = password.encode()
		password = hashlib.sha256(password).hexdigest()

		if password != korisnik[2]:
			return False
		
		session['korisnik_id'] = korisnik[0]
		session['username'] = korisnik[1]
		session['privilegija'] = korisnik[8]		

		return True		

	@staticmethod
	def korisnik_dodaj_racun(id, kolicina):
		kolicina = float(kolicina)
		
		if kolicina > 0:
			cursor = mydb.cursor(prepared=True)
			sql = "UPDATE korisnik SET stanje=stanje+? WHERE iDkorisnik=?"
			parametri = (kolicina, id)
			cursor.execute(sql, parametri)
			mydb.commit()

		else:
			return False

	@staticmethod
	def validiraj_username_register(username):
		cursor = mydb.cursor(prepared=True)
		sql = '''
			SELECT * FROM korisnik WHERE korisnicko_ime=?
		'''
		parametri = (username, )
		cursor.execute(sql, parametri)
		postojeci_korisnik = cursor.fetchall()
		if postojeci_korisnik:
			return True
		else:
			return False

class Komentar:
	__id_korisnik : int
	__id_proizvod : int
	__tekst_komentara : str

	def __init__(self, id_korisnik, id_proizvod, tekst_komentara):
		self.__id_korisnik = id_korisnik
		self.__id_proizvod = id_proizvod
		self.__tekst_komentara = tekst_komentara

	def get_id_korisnik(self):
		return self.__id_korisnik
	
	def get_id_proizvod(self):
		return self.__id_proizvod

	def get_tekst_komentara(self):
		return self.__tekst_komentara

	@staticmethod
	def izvuci_komentare(id_proizvod):
		cursor = mydb.cursor(prepared=True)
		sql = '''
			SELECT korisnik.korisnicko_ime, korisnik.url_profilna_slika, komentar.tekst_komentara
			FROM komentar
			INNER JOIN korisnik
			ON komentar.idKorisnik = korisnik.iDkorisnik
			INNER JOIN proizvod
			ON proizvod.idProizvod = komentar.idProizvod
			WHERE proizvod.idProizvod = ?
		'''

		parametri = (id_proizvod)
		cursor.execute(sql, parametri)
		rez = cursor.fetchall()

		for i in range (len(rez)):
			rez[i] = ukini_bytearray(rez[i])			

		return rez

	@staticmethod
	def insert_komentar(korisnik_id, proizvod_id, tekst_komentara):
		cursor = mydb.cursor(prepared=True)
		sql = '''
			INSERT INTO komentar
			VALUES (?, ?, ?)
		'''
		
		parametri = (korisnik_id, proizvod_id, tekst_komentara)
		cursor.execute(sql, parametri)
		mydb.commit()

@app.route('/')
def index():
	proizvodi = Proizvod.top_lista_proizvoda()
	return render_template("index.html", proizvodi=proizvodi)

@app.route('/register', methods=['POST', 'GET'])
def register():
	if request.method == 'GET':
		return render_template('register.html')
	
	if request.method == 'POST':

		username = request.form['username']
		email = request.form['email']
		confirm_lozinka = request.form['confirm_password']
		lozinka = request.form['password']
		ime_prezime = request.form['ime_prezime']
		adresa = request.form['adresa']
		broj_telefona = request.form['broj_telefona']
		slika = request.files['slika']

		if Korisnik.validiraj_username_register(username):
			return render_template("register.html", greska="Uneto korisnicko ime je zauzeto")

		if len(lozinka) < 8:
			return render_template("register.html", greska="Lozinka mora imati barem 8 karaktera")

		if lozinka != confirm_lozinka:
			return render_template("register.html", greska="Lozinke se ne poklapaju")

		if len(ime_prezime.split(" ")) < 2:
			return render_template("register.html", greska="Unesite i ime i prezime")

		if not broj_telefona.isnumeric():
			return render_template("register.html", greska="Unesite ispravan broj telefona")

		putanja_cuvanje = os.path.join(app.config['UPLOAD_USERS'], slika.filename)
		putanja_baza = os.path.join('images/user_images/', slika.filename)

		if not slika:
			putanja_baza = 'images/user_images/basic.webp'
			Korisnik.korisnik_register(username, email, lozinka, confirm_lozinka, ime_prezime, adresa, broj_telefona, putanja_baza)
			return redirect('/login')

		Korisnik.korisnik_register(username, email, lozinka, confirm_lozinka, ime_prezime, adresa, broj_telefona, putanja_baza)

		slika.save(putanja_cuvanje)

		return redirect(url_for('login'))

@app.route('/login', methods=['POST', 'GET'])
def login():
	if request.method == "GET":
		return render_template("login.html")

	if request.method == "POST":
		username = request.form['username']
		password = request.form['password']

		if Korisnik.korisnik_login(username, password):			
			return redirect('/')
		
		else:
			return render_template('login.html', greska="Netacno korisnicko ime ili lozinka")

@app.route('/logout')
def logout():
	session.clear()
	return redirect('/login')



@app.route('/user_profile')
def user_profile():
	if 'username' not in session:
		flash("Niste ulogovani")
		return redirect('/login')	

	username = session['username']

	cursor = mydb.cursor(prepared=True)
	sql = "SELECT * FROM korisnik WHERE korisnicko_ime=?"
	parametri = (username, )
	cursor.execute(sql, parametri)
	korisnik = cursor.fetchall()
	
	try:
		korisnik = ukini_bytearray(korisnik[0])
	
		k1 = Korisnik(korisnik[0], korisnik[1], korisnik[2], korisnik[3], korisnik[4], 
					korisnik[5], korisnik[6], korisnik[7],  korisnik[9], korisnik[10])		

	except:
		return redirect('/')
	
	return render_template('user_profile.html', korisnik=k1)

@app.route('/update_korisnik/<korisnik_id>', methods=['POST', 'GET'])
def update_korisnik(korisnik_id):
	cursor = mydb.cursor(prepared=True)
	sql = "SELECT * FROM korisnik WHERE iDkorisnik=?"
	parametri=(korisnik_id, )
	cursor.execute(sql, parametri)
	korisnik = cursor.fetchone()
	korisnik = ukini_bytearray(korisnik)
	k = Korisnik(korisnik[0], korisnik[1], korisnik[2], korisnik[3], korisnik[4],
				 korisnik[5], korisnik[6], korisnik[7], korisnik[9], korisnik[10])

	if request.method == 'GET':

		return render_template("update_korisnik.html", korisnik=k)

	if request.method == 'POST':
		username = request.form['username']
		lozinka = request.form['lozinka']

		confirm_lozinka = request.form['confirm-lozinka']

		if lozinka != confirm_lozinka:
			return render_template("greska.html", greska="Lozinke se ne poklapaju")		


		ime_prezime = request.form['ime_prezime']
		adresa = request.form['adresa']
		broj_telefona = request.form['broj_telefona']
		url_profilna = request.files['url_profilna']


		# if len(lozinka) < 8:
		# 	return render_template("greska.html", greska="Lozinka mora imati barem 8 karaktera")		

		if len(ime_prezime.split(" ")) < 2:
			return render_template("greska.html", greska="Unesite i ime i prezime")

		if not broj_telefona.isnumeric():
			return render_template("greska.html", greska="Unesite ispravan broj telefona")

		putanja_baza = ""
		if url_profilna:

			putanja_cuvanje = os.path.join(app.config['UPLOAD_USERS'], url_profilna.filename)
			putanja_baza = os.path.join('images/user_images/', url_profilna.filename)
			url_profilna.save(putanja_cuvanje)

		if not url_profilna or url_profilna.filename == '':
			putanja_baza = k.url_profilna

		if lozinka:
			lozinka = lozinka.encode()
			lozinka = hashlib.sha256(lozinka).hexdigest()

		if not lozinka:
			lozinka = korisnik[2]

		sql_update = '''UPDATE korisnik
					 SET						
						korisnicko_ime=?, 
						lozinka=?, 
						ime_prezime=?,
						adresa=?,
						broj_telefona=?,
						url_profilna_slika=?
						 
					 WHERE iDkorisnik=?
					 '''
		parametri_update = (username, lozinka, ime_prezime, adresa, broj_telefona, putanja_baza, korisnik_id)
		cursor.execute(sql_update, parametri_update)
		mydb.commit()		
		cursor.close()
		return redirect('/')

@app.route('/products_all', methods=['POST', 'GET'])
def products_all():
	if request.method == "GET":
		all_products_db = Proizvod.izvuci_sve_proizvode()		
		proizvodi_prodaja = []
		for product in all_products_db:
			if product.get_u_prodaji() == 'da':
				proizvodi_prodaja.append(product)

		return render_template('products.html', all_products=proizvodi_prodaja)
	
	if request.method == 'POST':
		kriterijum_sortiranja = request.form['kriterijum']

		all_products_db = Proizvod.izvuci_sve_proizvode()		
		proizvodi_prodaja = []
		for product in all_products_db:
			if product.get_u_prodaji() == 'da':
				proizvodi_prodaja.append(product)


		if kriterijum_sortiranja == 'cena-rastuca':
			proizvodi_prodaja = sorted(proizvodi_prodaja, key=lambda x : x.get_cena())			

		elif kriterijum_sortiranja == 'cena-opadajuca':
			proizvodi_prodaja = sorted(proizvodi_prodaja, key=lambda x : x.get_cena(), reverse=True)
			
		elif kriterijum_sortiranja == 'naziv-rastuci':
			proizvodi_prodaja = sorted(proizvodi_prodaja, key=lambda x : x.get_naziv())			

		elif kriterijum_sortiranja == 'naziv-opadajuci':
			proizvodi_prodaja = sorted(proizvodi_prodaja, key=lambda x : x.get_naziv(), reverse=True)

		else:
			proizvodi_prodaja = proizvodi_prodaja

		return render_template('products.html', all_products=proizvodi_prodaja)

def ukini_bytearray(bytearray_tuple):	
	bytearray_tuple = list(bytearray_tuple)	
	for i in range (len(bytearray_tuple)):
		if isinstance(bytearray_tuple[i], bytearray):
			bytearray_tuple[i] = bytearray_tuple[i].decode()
			
	return bytearray_tuple


@app.route('/proizvod/<proizvod_id>')
def render_proizvod(proizvod_id):
	if request.method == 'GET':
		proizvod = Proizvod.izvuci_jedan_proizvod(proizvod_id)
		
		try:
			komentar = Komentar.izvuci_komentare(proizvod_id)
			if komentar:
				return render_template("product.html", product=proizvod, komentar=komentar)
		
		except:
			return render_template("product.html", product=proizvod)


@app.route('/dodaj_u_korpu', methods=['POST'])
def dodaj_u_korpu():

	proizvod_id = request.form['proizvod_id']
	velicina = request.form['velicina']	

	if not Proizvod.proveri_stanje_velicine(proizvod_id, velicina):		
		return render_template("greska.html", greska="Nema trazene velicine")
	
	if 'username' in session and 'korisnik_id' in session: 
		user_id = session['korisnik_id']
		username = session['username']	


	cursor = mydb.cursor(prepared=True)
	sql = "SELECT * FROM korisnik WHERE korisnicko_ime=?"
	parametri = (username, )
	cursor.execute(sql, parametri)
	user = cursor.fetchall()	

	if user:
		user = ukini_bytearray(user)
		user_id = user[0][0]

		sql = '''SELECT porudzbina.Korisnik_idKorisnik , porudzbina.idKorpa
				FROM porudzbina 				
				WHERE Korisnik_idKorisnik=? AND porudzbina.stanje_porudzbine="korpa"'''
		parametri = (user_id, )
		cursor.execute(sql, parametri)
		korpa = cursor.fetchone()

		if korpa:			
			try:

				Korisnik.kreiraj_stavku_korpe(proizvod_id, korpa[1], velicina)				
			except:
				return render_template("greska.html")
			
		else:			
			try:
				korpa_id = Korisnik.kreiraj_korpu(user[0][0])				
				Korisnik.kreiraj_stavku_korpe(proizvod_id, korpa_id, velicina)
			except:
				return render_template("greska.html")
		#korpa = ukini_bytearray(korpa)
		#Korisnik.kreiraj_stavku_korpe(proizvod_id, korpa[0])
				
	return redirect('/render_korpa')


@app.route('/render_korpa')
def render_korpa():
	if 'username' not in session:
		return redirect('/login')
	username = session['username']

	cursor = mydb.cursor(prepared=True)

	sql = '''SELECT korisnik.korisnicko_ime, proizvod.naziv_proizvoda, stavkaporudzbine.kolicina, 
			proizvod.idProizvod, stavkaporudzbine.Korpa_idKorpa, porudzbina.stanje_porudzbine,
			korisnik.iDkorisnik, proizvod.url_slike, velicina.oznaka_velicine
			FROM stavkaporudzbine 
			INNER JOIN porudzbina
			ON stavkaporudzbine.Korpa_idKorpa=porudzbina.idKorpa
			INNER JOIN korisnik 
			ON porudzbina.Korisnik_iDkorisnik=korisnik.iDkorisnik
			INNER JOIN proizvod
			ON proizvod.idProizvod=stavkaporudzbine.Proizvod_idProizvod
			INNER JOIN velicina
			ON velicina.idVelicina=stavkaporudzbine.idVelicina
			WHERE korisnik.korisnicko_ime=? AND porudzbina.stanje_porudzbine="korpa"'''

	parametri = (username, )
	cursor.execute(sql, parametri)
	stavke = cursor.fetchall()	
	
	try:			
		if stavke:		
			stavke = list(stavke)
			for i in range (len(stavke)):			
				stavke[i] = ukini_bytearray(stavke[i])
			
			return render_template('korpa.html', stavke=stavke)
		else:
			return render_template("korpa.html")
	except:
		return render_template("greska.html", greska="GRESKA PRILIKOM RENDEROVANJA KORPE")
	
	
@app.route('/delete_stavka_korpe')
def delete_stavka_korpe():
	korpa_id = request.args.get('korpa_id', None)
	proizvod_id = request.args.get('proizvod_id', None)
	
	cursor = mydb.cursor(prepared=True)
	sql = "DELETE FROM `stavkaporudzbine` WHERE stavkaporudzbine.Korpa_idKorpa=? AND Proizvod_idProizvod=?"
	parametri = (korpa_id, proizvod_id)
	cursor.execute(sql, parametri)
	mydb.commit()

	return redirect('/render_korpa')
	#return redirect('/render_korpa')

@app.route('/kolicina_plus')
def kolicina_plus():
	korpa_id = request.args.get('korpa_id', None)
	proizvod_id = request.args.get('proizvod_id', None)	

	cursor = mydb.cursor(buffered=True)
	sql = "SELECT * FROM stavkaporudzbine WHERE Proizvod_idProizvod=%s AND Korpa_idKorpa=%s"
	parametri = (proizvod_id, korpa_id)
	cursor.execute(sql, parametri)
	stavka = cursor.fetchone()

	stavka = ukini_bytearray(stavka)
	kolicina = int(stavka[2])
	kolicina += 1

	sql = "UPDATE stavkaporudzbine SET kolicina=%s WHERE Proizvod_idProizvod=%s AND Korpa_idKorpa=%s"
	parametri = (kolicina, proizvod_id, korpa_id )
	cursor.execute(sql, parametri)
	mydb.commit()

	return redirect('/render_korpa')

@app.route('/kolicina_minus')
def kolicina_minus():
	korpa_id = request.args.get('korpa_id', None)
	proizvod_id = request.args.get('proizvod_id', None)	

	cursor = mydb.cursor(prepared=True)
	sql = "SELECT * FROM stavkaporudzbine WHERE Proizvod_idProizvod=? AND Korpa_idKorpa=?"
	parametri = (proizvod_id, korpa_id)
	cursor.execute(sql, parametri)
	stavka = cursor.fetchone()
	
	stavka = ukini_bytearray(stavka)
	kolicina = int(stavka[2])
	kolicina -= 1
	if kolicina >= 1:
		sql = "UPDATE stavkaporudzbine SET kolicina=? WHERE Proizvod_idProizvod=? AND Korpa_idKorpa=?"
		parametri = (kolicina, proizvod_id, korpa_id)

	else:
		sql = "DELETE FROM `stavkaporudzbine` WHERE stavkaporudzbine.Korpa_idKorpa=? AND Proizvod_idProizvod=?"
		parametri=(proizvod_id, korpa_id)
	
	cursor.execute(sql, parametri)
	mydb.commit()
	
	return redirect('/render_korpa')

@app.route('/kupi')
def kupi():
	korpa_id = request.args.get('korpa_id', None)
	korisnik_id = request.args.get('korisnik_id', None)	
	cursor = mydb.cursor(buffered=True)

	sql = '''
		SELECT proizvod.proizvod_cena, stavkaporudzbine.kolicina, proizvod.idProdavac, proizvod.idProizvod, stavkaporudzbine.idVelicina
		FROM stavkaporudzbine  
		INNER JOIN proizvod
		ON proizvod.idProizvod = stavkaporudzbine.Proizvod_idProizvod
		INNER JOIN porudzbina
		ON porudzbina.idKorpa = stavkaporudzbine.Korpa_idKorpa
		WHERE porudzbina.Korisnik_iDkorisnik=%s AND porudzbina.idKorpa=%s
	'''

	
	parametri = (korisnik_id, korpa_id)
	cursor.execute(sql, parametri)
	stavke_korpe = cursor.fetchall()
	
	ukupno_para = 0
	for i in range(len(stavke_korpe)):
		stavke_korpe[i] = ukini_bytearray(stavke_korpe[i])
		ukupno_para = ukupno_para + (stavke_korpe[i][0] * stavke_korpe[0][1])



	for stavka in stavke_korpe:
		c = stavka[0]
		k = stavka[1]		
		prodavac = stavka[2]
		proizvod_id = stavka[3]
		velicina_id = stavka[4]

		cursor = mydb.cursor(prepared=True)	
		sql = "SELECT stanje FROM korisnik WHERE iDkorisnik=?"
		parametri = (korisnik_id, )
		cursor.execute(sql, parametri)
		pare = cursor.fetchone()	
				
		pare = ukini_bytearray(pare)
		pare = float(pare[0])

		if pare > (ukupno_para):
			pare = pare - (c * k)

			sql = '''
				UPDATE porudzbina
				SET porudzbina.stanje_porudzbine="izvrsena"
				WHERE porudzbina.Korisnik_iDkorisnik=? AND porudzbina.idKorpa=?
			'''
			parametri = (korisnik_id, korpa_id)
			cursor.execute(sql, parametri)
			mydb.commit()
			sql = "UPDATE korisnik SET stanje=? WHERE korisnik.iDkorisnik=?"
			parametri = (pare, korisnik_id)
			cursor.execute(sql, parametri)
			mydb.commit()
			sql = "UPDATE korisnik SET stanje=stanje+? WHERE korisnik.iDkorisnik=?"
			parametri = ((c*k), prodavac)
			cursor.execute(sql, parametri)
			Proizvod.skini_sa_lagera(proizvod_id, velicina_id, k)
			Proizvod.dodaj_broj_prodatih(proizvod_id, k)
		else:
			return render_template("greska.html", greska="Nemate dovoljno para")

	return redirect('/render_korpa')

@app.route('/dodaj_eracun', methods=['POST', 'GET'])
def dodaj_raucn():
	if request.method == 'GET':
		return render_template('racun_dodaj.html')
	
	if request.method == 'POST':
		if 'korisnik_id' not in session:
			return redirect('/login')

		korisnik_id = session['korisnik_id']
		kolicina = request.form['kolicina']		
		kolicina = str(kolicina)

		Korisnik.korisnik_dodaj_racun(korisnik_id, kolicina)

		return redirect('/user_profile')

@app.route('/admin_panel')
def admin_panel():
	
	if session['privilegija'] != 1 or 'privilegija' not in session:
		return render_template('greska.html', greska="Zabranjen pristup")

	if session['privilegija'] == 1:
		return render_template('admin_panel.html')	

@app.route('/istorija_kupovine/<korisnik_id>')
def istorija_kupovine(korisnik_id):

	if str(session['korisnik_id']) == korisnik_id or session['privilegija'] == '1':
	
		cursor = mydb.cursor(prepared=True)
		sql = "SELECT * FROM porudzbina WHERE Korisnik_iDkorisnik=?"
		parametri = (korisnik_id, )
		cursor.execute(sql, parametri)
		
		korpe_korisnika = cursor.fetchall()
		for korpa in korpe_korisnika:
			korpa = ukini_bytearray(korpa)

		sql = '''
				SELECT proizvod.url_slike, proizvod.naziv_proizvoda, proizvod.proizvod_cena, porudzbina.datum_porudzbine,
					stavkaporudzbine.kolicina, porudzbina.idKorpa
				FROM porudzbina
				INNER JOIN korisnik
				ON korisnik.iDkorisnik=porudzbina.Korisnik_iDkorisnik
				INNER JOIN stavkaporudzbine 
				ON stavkaporudzbine.Korpa_idKorpa=porudzbina.idKorpa
				INNER JOIN proizvod
				ON proizvod.idProizvod=stavkaporudzbine.Proizvod_idProizvod
				WHERE porudzbina.Korisnik_iDkorisnik=? AND porudzbina.stanje_porudzbine = 'izvrsena'
				'''
		parametri = (korisnik_id, )
		cursor.execute(sql, parametri)
		istorija = cursor.fetchall()
		
		for i in range (len(istorija)):
			istorija[i] = ukini_bytearray(istorija[i])


		return render_template('istorija_kupovine.html', korpe=istorija)
	else:
		return render_template('greska.html', greska="Nemate pravo pristupa")


@app.route('/admin_svi_korisnici')
def svi_korisnici():
	svi_korisnici = Korisnik.select_svi_korisnici()
	return render_template("all_users.html", svi_korisnici=svi_korisnici)


@app.route('/dodaj_proizvod', methods=['POST', 'GET'])
def dodaj_proizvod():
	if request.method == 'GET':
		return render_template("add_proizvod.html")
	
	if request.method == 'POST':
		naziv = request.form['naziv_proizvoda']
		cena = request.form['cena']
		opis = request.form['opis']		
		slika = request.files['slika']	
		u_prodaji = request.form['u_prodaji']	

		fajl = slika.filename
		fajl = secure_filename(fajl)
		putanja = os.path.join(app.config['UPLOAD_PRODUCTS'], fajl)
		putanja_baza = os.path.join('images/product_images/', fajl)

		prodavac = session['korisnik_id']
		broj_prodatih = 0
		cursor = mydb.cursor(prepared=True)
		sql = "INSERT INTO proizvod VALUES (null, ?, ?, ?, ?, ?, ?, ?)"
		parametri = (naziv, cena, opis, putanja_baza, u_prodaji, prodavac, broj_prodatih)
		cursor.execute(sql, parametri)
		mydb.commit()	
		slika.save(putanja)
		return redirect('/dodaj_proizvod')

@app.route('/dodeli_prava', methods=['POST', 'GET'])
def dodeli_prava():	
	korisnik_id = request.form['korisnik_id']
	prava = request.form['prava']

	cursor = mydb.cursor(prepared=True)
	sql = "UPDATE korisnik SET TipKorisnika_idTipKorisnika=? WHERE iDkorisnik=?"
	parametri = (prava, korisnik_id)
	cursor.execute(sql, parametri)
	mydb.commit()

	return redirect('/admin_svi_korisnici')


@app.route('/admin_svi_proizvodi')
def admin_svi_proizvodi():
	if 'privilegija' in session and session['privilegija'] == 1:
		svi_proizvodi = Proizvod.izvuci_sve_proizvode()
		return render_template('all_products_admin.html', svi_proizvodi=svi_proizvodi)
	else:
		return render_template("greska.html", greska="Zabranjen pristup")


@app.route('/update_proizvod/<proizvod_id>', methods=['POST', 'GET'])
def update_proizvod(proizvod_id):
	if 'privilegija' in session:
		proizvod = Proizvod.izvuci_jedan_proizvod(proizvod_id)
		if request.method == "GET" and 'privilegija' in session:
			proizvod = Proizvod.izvuci_jedan_proizvod(proizvod_id)
			return render_template("update_proizvod.html", proizvod=proizvod)
		
		if request.method == "POST":
			naziv = request.form['naziv']
			cena = request.form['cena']
			opis = request.form['opis']
			slika = request.files['slika']
			u_prodaji = request.form['prodaja']
			broj_prodatih = request.form['broj_prodatih']

			slika_baza = "images/product_images/" + slika.filename
			slika_os = os.path.join(app.config['UPLOAD_PRODUCTS'], slika.filename)

			if not slika or slika.filename == '':
				slika_baza = proizvod.get_url_slike()
			
			prodavac_id = session['korisnik_id']
			p = Proizvod(proizvod.get_id(), naziv, cena, opis, slika_baza, u_prodaji, prodavac_id, broj_prodatih)			
			Proizvod.update_proizvod(p)
			if slika:
				slika.save(slika_os)
			return redirect('/admin_svi_proizvodi')


@app.route('/dodaj_komentar', methods=['POST'])
def dodaj_komentar():
	korisnik_id = request.form['korisnik_id']
	proizvod_id = request.form['proizvod_id']
	tekst_komentara = request.form['komentar']


	Komentar.insert_komentar(korisnik_id, proizvod_id, tekst_komentara)
	return redirect(f'/proizvod/{proizvod_id}')


@app.route('/lager_forma', methods=['POST'])
def lager_forma():
	proizvod_id = request.form['proizvod_id']	
	proizvod = Proizvod.izvuci_jedan_proizvod(proizvod_id)
	return render_template("lager_forma.html", proizvod=proizvod)


@app.route('/lager_dodaj', methods=['POST'])
def lager_dodaj():
	proizvod_id = request.form['proizvod_id']
	velicina = request.form['velicina']
	kolicina = request.form['kolicina']

	cursor = mydb.cursor(prepared=True)
	sql = "SELECT idVelicina FROM velicina WHERE velicina.oznaka_velicine=?"
	parametri = (velicina, )
	cursor.execute(sql, parametri)
	id = cursor.fetchone()
	id = ukini_bytearray(id)
	id = id[0]

	Proizvod.dodaj_na_lager(proizvod_id, id, kolicina)

	return redirect("/admin_svi_proizvodi")


@app.route('/zaposleni_panel')
def zaposleni_panel():
	if 'korisnik_id' in session and session['privilegija'] == 2:
		return render_template("zaposleni_panel.html")
	else:
		redirect('/')

@app.route('/moji_proizvodi')
def moji_proizvodi():
	if 'korisnik_id' in session and session['privilegija'] == 2:
		prodavac_id = session['korisnik_id']
		cursor = mydb.cursor(prepared=True)
		sql = '''
			SELECT * 
			FROM proizvod
			WHERE proizvod.idProdavac=?
		'''
		parametri = (prodavac_id, )
		cursor.execute(sql, parametri)
		moji_proizvodi_baza = cursor.fetchall()
		lista_proizvoda = []

		for i in range (len(moji_proizvodi_baza)):
			moji_proizvodi_baza[i] = ukini_bytearray(moji_proizvodi_baza[i])
			p = Proizvod(
				moji_proizvodi_baza[i][0],
				moji_proizvodi_baza[i][1],
				moji_proizvodi_baza[i][2],
				moji_proizvodi_baza[i][3],
				moji_proizvodi_baza[i][4],
				moji_proizvodi_baza[i][5],
				moji_proizvodi_baza[i][6],
				moji_proizvodi_baza[i][7]
			)
			lista_proizvoda.append(p)



		return render_template("all_products_admin.html", svi_proizvodi=lista_proizvoda)

	return redirect('/')


app.run(debug=True)
