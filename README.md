# CandyTracker
> HY Tsoha 2020 - tuukkala

## Viikon 2 päivitykset

Sovellus löytyy osoitteesta https://candytracker.herokuapp.com/

Käyttäjänimellä `user` ja salasanalla `asdf1234` pääsee kirjautumaan sisään.

Uuden käyttäjän voi luoda valitsemalla 'Sign up'.

~~Reksiteröinnissä on vielä jokin bugi, samoin päiväkirjasyötteiden lisäämisessä.~~

~~Lokaalisti toimii rekisteröinti ja syötteiden lisääminen.~~


## What?

CandyTracker on makeisten syönnin seurantaan soveltuva päiväkirja. Sovellus saattaa toimia apuna hillitsemään omaa sokerinkulutusta, tai vaan esittämään kulutetun sokerin määrän.

### Käyttäjän toiminnot *- PLAN*

- [ ] Vierailija voi rekisteröityä
- [ ] Käyttäjä voi kirjautua sisään ja ulos
- [ ] Käyttäjä voi hakea makeisia valmistajan nimellä tai makeisen nimellä
- [ ] Käyttäjä voi lisätä puuttuvan makeisen listaan
  - Tulisiko olla Premium-käyttäjä, jottei ihan jokainen trolli pääse täyttämään tietokantaa?
  - Joku muu tarkistusrajoitus? Admin?
- [ ] Käyttäjä voi lisätä omaan kulutushistoriaansa makeisen
- [ ] Käyttäjä voi tarkastella omaa sokerin/makeisten kulutuksen

### Jatkokehitys / Brainstorming
> Hajatelmia mahdollisista laajennuksista

- Sosiaalinen aspekti
  - Käyttäjä voi julkaista oman kulutussyötteensä
  - Käyttäjä voi kommentoida muiden käyttäjien syötettä / kirjauksia

- Pelillistämis-osa
  - Saavutuksia / merkkejä
  - Käyttäjä voi kilpailla muiden käyttäjien kanssa

## Sovelluksen suorittaminen

Ensimmäisellä kerralla

```bash
$ cd CandyTracker
$ python3 -m venv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
$ flask run
```

Seuraavilla kerroilla
```bash
$ flask run
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

## ToDo

### Views
- [x] Frontpage (with login)
- [ ] Profile page / Dashboard
- [ ] Add entry to diary
- [ ] Add candy
- [x] 404
- [ ] Feed (?)
