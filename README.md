#Projekat iz predmeta Web Sistemi i Tehnologije - Ecommerce

Ovo je studentski projekat i on predstavlja Internet prodavnicu sa funckionalnostima vezanim za kupovinu "novcem" kojeg korisnik sebi moze dodati koliko god zeli :). U nastavku su izlistane funkcionalnosti, pravila validacije u formama...

Kako bi sve radilo kako treba, potrebno je imati instalirane module:
	-flask
	-mysql-connector
	-flask-fontawesome
	-datetime
	-werkzeug.utils
	-os

SQL fajl sa bazom - flask_eprod.sql

prijava kao administrator:
	-username:administrator
	-password:administrator

##1. Pocetna stranica
	
	-navbar linkovi ka ponudi(spisak svih proizvoda koji su trenutno u prodaji)
	-link ka formama za prijavljivanje i registraciju
	-na manjim sirinama ekrana linkovi pocetna i ponuda se dobijaju u side-menu
	-u donjem delu stranice se nalaze najprodavaniji proizvodi (svaki put kada neko kupi odredjeni proizvod, tom proizvodu se dodaje jedan "bod")
	-footer


##2. Register

	-Forma za registraciju
	-ne moze se odabrati postojeci usename
	-email mora odgovarati izrazu
	-password mora imati barem 8 karaktera i mora se potvrditi
	-password se nakon validacije hash-iran unosi u bazu
	-ime i prezime moraju biti barem dve reci
	-broj telefona mora biti string koji se sastoji samo iz brojeva
	-ukoliko se slika ne unese, podrazumevano se uzima genericka

##3. Login

	-Sva polja moraju biti popunjena
	-korisnicko ime mora postojati i sifra mora biti ona koja odgovara tom korisniku
	-password se hash-ira i poredi sa vrednosti iz baze
	-ako je prijava uspesna u sessiju se dodaju korisnicko ime, id korisnika i oznaka njegove privilegije

##4. Ponuda 
	
	-Svi proizvodi koji su trenutno u prodaji, njihove slike i cene
	-klikom	na proizvod dobijamo njegovu pojedinacnu stranicu

##5. Stranica sa proizvodom
	
	-Podaci o proizvodu
	-opcija dodavanja zeljene velicine u korpu, velicina mora biti odabrana
	-prikaz komentara za dati proizvod i opcija unosa komentara ako je korisnik ulogovan
	-pritiskom na dugme "dodaj u korpu" se proizvod dodaje u korpu
	-ukoliko zelimo da dodamo u korpu proizvod kojeg trenutno nema na stanju, dobijamo odgovarajucu poruku
	
##6. Korpa

	-Prikazuju nam se svi proizvodi koje trenutno imamo u korpi
	-kolicinu mozemo menjati klikom na + i - 
	-opcija brisanja iz korpe
	-opcija kupovine sadrzaja korpe
	-ukoliko prijavljeni korisnik nema dovoljno novca, ispisuje mu se odgovarajuca poruka
	-sadrzaj korpe ostaje i kada napustimo stranicu sve dok se ne kupi ili obrise, mozemo se vracati i dodavati nove proizvode
	
##7. Korisnicki profil
	-Prikaz podataka o korisniku
	-Pregled istorije kupovine
	-izmene podataka na profilu klikom na "edit" ikonicu
	-dodavanje novca na racun korisnika

##8. Izmena podataka na profilu

	-pravila validacije su ista kao kod registracije
	-polje za password je podrazumevano prazno, ako se nista ne unese sifra ce ostati ista

##9. Prodavac

	-Kada prijavljeni korisnik ima privilegije prodavca, na svakoj stranici ima link "Upravljanje proizvodima"
	-Na toj stranici dobija linkove sa opcijama pregleda svih proizvoda koje je okacio i njihove izmene, kao i link za dodavanje novog proizvoda
	-Pri pregledu svih proizvoda, prodavac ih moze izmeniti, dodati odredjenu kolicinu na lager ili ih staviti ili povuci iz prodaje
	-kada neko kupi proizvod odredjenog prodavca, tom prodavcu se vrednost kupovine dodaje na racun

##10. Admin 

	-kada prijavljeni korisnik ima privilegije administratora, na svakoj stranici mu se prikzuje link "Admin panel"
	-na admin panelu se nalaze opcije pregleda korisnika, proizvoda i dodavanje proizvoda
	-pri pregledu korisnika, administrator im moze menjati podatke ili im dodeliti prava
	-pri pregledu proizvoda administrator moze raditi sve sto moze i prodavac, samo sto se administratoru prikazuju proizvodi svih prodavaca

##11. Logout

	-Klikom na dugme logout, brisu se podaci iz sesije i pojavljuje login forma
	
