# CandyTracker
> Sovellus on luotu osana Helsingin yliopiston tietojenkäsittelutieteen kurssia "Aineopintojen harjoitustyö: Tietokantasovellus"

Sovellus löytyy osoitteesta https://candytracker.herokuapp.com/

Käyttäjänimellä `user` ja salasanalla `asdf1234` pääsee kirjautumaan sisään.

Uuden käyttäjän voi luoda valitsemalla 'Sign up'.

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
- [https://select2.org/](Select2)
- [Duet Date Picker](https://github.com/duetds/date-picker)
- [Teenyicons](https://teenyicons.com/)

### Käyttäjän toiminnot

#### Perustoiminnot
- [x] Vierailija voi rekisteröityä
- [x] Käyttäjä voi kirjautua sisään ja ulos
- [x] Käyttäjä voi hakea makeisia valmistajan nimellä tai makeisen nimellä
- [x] Käyttäjä voi lisätä puuttuvan makeisen listaan
- [x] Käyttäjä voi lisätä omaan kulutushistoriaansa makeisen
- [ ] Käyttäjä voi tarkastella omaa sokerin/makeisten kulutuksta

#### Ryhmätoiminnot
- [ ] Käyttäjä voi luoda ryhmän
- [ ] Käyttäjä voi etsiä ryhmiä
- [ ] Käyttäjä voi liittyä ryhmään
- [ ] Käyttäjä voi poistua ryhmästä
- [ ] Käyttäjä voi luoda haasteen/tavoitteen ryhmässä

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
- [ ] Sovellus toimii, kun käyttäjä testaa sitä
- [ ] Sovellusta on mukavaa käyttää ja on selvää, mitä toiminnot tekevät
- [ ] Jos käyttäjä antaa väärää tietoa, tästä tulee selkeä ilmoitus
- [ ] Sovelluksen käyttöliittymä ja ulkoasu ovat viimeisteltyjä
- [ ] Tiedosto README.md antaa hyvän kuvan sovelluksesta
### Tekninen toteutus
- [ ] Koodia on helppo lukea ja muuttujien, funktioiden, jne. nimet on valittu hyvin
- [ ] Koodi on tiivistä ja suoraviivaista
- [ ] Koodi on jaettu järkevästi osiin tiedostoiksi ja funktioiksi
- [ ] Koodin tyyli on yhdenmukainen kaikissa sovelluksen osissa
- [ ] Versionhallinnassa commitit ja niiden viestit on tehty hyvin
### Tietokanta-asiat
- [ ] Tietokanta on suunniteltu järkevästi sovelluksen vaatimusten mukaisesti
- [ ] Taulut ja sarakkeet on nimetty selkeästi ja yhdenmukaisesti
- [ ] Tauluissa on käytetty viiteavaimia ja tarvittaessa muita määreitä
- [ ] SQL-kyselyt on toteutettu suoraviivaisesti eikä haeta turhaa tietoa
- [ ] Jos tiedot voi hakea järkevästi yhdellä kyselyllä, ei suoriteta useita kyselyjä
### Tietoturva
- [ ] Käyttäjät pääsevät näkemään vain tietoja, joihin heillä on oikeus
- [ ] Käyttäjän syöte tarkastetaan ennen tietokantakomentoja
- [ ] Sovelluksessa ei ole SQL-injektion mahdollisuutta eikä XSS- ja CSRF-haavoittuvuuksia
- [ ] Salasanat tallennetaan tietokantaan asianmukaisesti
- [ ] Versionhallinnassa ei ole salaista tietoa (kuten .env-tiedostoa)