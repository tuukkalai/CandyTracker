# CandyTracker
> Sovellus on luotu osana Helsingin yliopiston tietojenkäsittelutieteen kurssia "Aineopintojen harjoitustyö: Tietokantasovellus"

Sovellus löytyy osoitteesta https://candytracker.herokuapp.com/

Uuden käyttäjän saa luotua klikkaamalla 'Sign up' tai sisäänkirjaus onnistuu myös testikäyttäjällä `testduudyksi` (ja salasanalla `salasana`).

## What?

CandyTracker on makeisten syönnin seurantaan soveltuva päiväkirja. Sovellus saattaa toimia apuna hillitsemään omaa sokerinkulutusta, tai esittämään kulutetun sokerin määrän.

CandyTrackerissä voit muodostaa kavereiden, tai vaikka tuntemattomien kanssa ryhmiä, ja kilpailla haasteissa muita ryhmiä vastaan.

### Teknologiat

- [Python](https://www.python.org/)
- [Flask](https://flask.palletsprojects.com/en/1.1.x/)
- [PostgreSQL](https://www.postgresql.org/)
- [Bootstrap](https://getbootstrap.com/)
  - jonka osana mm. [jQuery](https://jquery.com/)
- [Chart.js](https://www.chartjs.org/)
- [Select2](https://select2.org/)
- [Duet Date Picker](https://github.com/duetds/date-picker)
- [Teenyicons](https://teenyicons.com/)

### Käyttäjän toiminnot

#### Perustoiminnot
- [x] Vierailija voi rekisteröityä
- [x] Käyttäjä voi kirjautua sisään ja ulos
- [x] Käyttäjä voi hakea makeisia valmistajan nimellä tai makeisen nimellä
- [x] Käyttäjä voi lisätä puuttuvan makeisen listaan
- [x] Käyttäjä voi lisätä omaan kulutushistoriaansa makeisen
- [x] Käyttäjä voi tarkastella omaa sokerin/makeisten kulutuksta

#### Ryhmätoiminnot
- [x] Käyttäjä voi luoda ryhmän
- [x] Käyttäjä voi pyytää liittymistä avoimeen ryhmään
- [x] Käyttäjä voi poistua ryhmästä
- [x] Käyttäjä voi aktivoida haasteen/tavoitteen ryhmässä
- [x] Käyttäjä voi lähettää viestin ryhmässä

Ryhmien ensimmäinen käyttäjä (luoja) on admin, ja hän näkee hieman enemmän ryhmissä kuin muut.
Jos admin poistaa itsensä ryhmästä, toiseksi vanhimmasta ryhmäläisestä tulee admin.

## Sovelluksen suorittaminen

Ensimmäisellä kerralla

```bash
$ cd CandyTracker
$ python3 -m venv venv
$ source venv/bin/activate
(venv) $ pip install -r requirements.txt
(venv) $ flask run
```

Seuraavilla kerroilla

```bash
$ source venv/bin/activate
(venv) $ flask run
```

## Kurssiin liittyvät vaatimukset

### Yleiskuva
- [x] Sovellus toimii, kun käyttäjä testaa sitä
- [x] Sovellusta on mukavaa käyttää ja on selvää, mitä toiminnot tekevät
- [x] Jos käyttäjä antaa väärää tietoa, tästä tulee selkeä ilmoitus
- [x] Sovelluksen käyttöliittymä ja ulkoasu ovat viimeisteltyjä
- [x] Tiedosto README.md antaa hyvän kuvan sovelluksesta
### Tekninen toteutus
- [x] Koodia on helppo lukea ja muuttujien, funktioiden, jne. nimet on valittu hyvin
- [-] Koodi on tiivistä ja suoraviivaista
- [x] Koodi on jaettu järkevästi osiin tiedostoiksi ja funktioiksi
- [x] Koodin tyyli on yhdenmukainen kaikissa sovelluksen osissa
- [x] Versionhallinnassa commitit ja niiden viestit on tehty hyvin
### Tietokanta-asiat
- [x] Tietokanta on suunniteltu järkevästi sovelluksen vaatimusten mukaisesti
- [x] Taulut ja sarakkeet on nimetty selkeästi ja yhdenmukaisesti
- [x] Tauluissa on käytetty viiteavaimia ja tarvittaessa muita määreitä
- [x] SQL-kyselyt on toteutettu suoraviivaisesti eikä haeta turhaa tietoa
- [x] Jos tiedot voi hakea järkevästi yhdellä kyselyllä, ei suoriteta useita kyselyjä
### Tietoturva
- [x] Käyttäjät pääsevät näkemään vain tietoja, joihin heillä on oikeus
- [x] Käyttäjän syöte tarkastetaan ennen tietokantakomentoja
- [x] Sovelluksessa ei ole SQL-injektion mahdollisuutta eikä XSS- ja CSRF-haavoittuvuuksia
- [x] Salasanat tallennetaan tietokantaan asianmukaisesti
- [x] Versionhallinnassa ei ole salaista tietoa (kuten .env-tiedostoa)