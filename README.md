# CandyTracker
> HY Tsoha 2020 - tuukkala

## What?

CandyTracker on makeisten syönnin seurantaan soveltuva päiväkirja. Sovellus saattaa toimia apuna hillitsemään omaa sokerinkulutusta, tai vaan esittämään kulutetun sokerin määrän.

Päiväkirjanomaisesti käyttäjä voi lisätä päivän/viikon aikana syömänsä makeiset, ja sovellus näyttää käyttäjälle dataa. Halutessaan käyttäjä voi näyttää julkisesti kulutetun sokerin määrän tai pitää oman profiilinsa privaattina. Julkiset profiilit voidaan lisätä ranking-tilastoihin ("Eniten vähentäneet", "Vähiten karkkipäiviä", ...).

Käyttäjän on mahdollista lisätä sovellukseen makeisia, jonka jälkeen myös muiden käyttäjien on mahdollista valita kyseinen tuote.

## Sovelluksen suorittaminen

```bash
$ cd CandyTracker
$ source venv/bin/activate
$ pip install flask
$ flask run
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

