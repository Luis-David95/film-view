# Film review app

## Summary

**Film review app** is a simple web application for writing film reviews. Every user account is either a regular *user* or an *admin* with additional privileges. Administrators may add new films to the database and ban/unban or promote regular users. The application was developed using the [Flask](https://palletsprojects.com/p/flask/) web application framework. A [PostgreSQL](https://www.postgresql.org/) database is used to store all relevant information needed by the application. Also, a demo version of the app is hosted on [Heroku](https://www.heroku.com/home).

## Testaaminen

Sovellusta voi testata osoitteessa https://rvr-fra.herokuapp.com/

Sovelluksessa on yksi julkinen pääkäyttäjä, jonka tunnus on **admin** ja salasana **password**. Tälle käyttäjälle on näkyvissä etusivulla "admin-paneeli", jonka kautta voidaan lisätä uusia elokuvia sovellukseen, hallinnoida elokuvia ja käyttäjiä sekä generoida [tiedostosta](https://github.com/rvrauhala/film-review-app/blob/main/data/countries.csv) maalistaus sovelluksen käyttöön. Ylläpitäjätunnuksella voi testata vain ylläpitäjälle tarkoitettuja toimintoja. Huomaathan, että maalistauksen generoiva painike ei toimi Herokussa enää toista kertaa, sillä sitä on jo painettu.

Rekisteröitymis- ja kirjautumistoimintojen testaamista varten sekä uusien elokuva-arvosteluiden lisäämistä varten kannattaa luoda uusi käyttäjätunnus, joka on oletuksena tavallinen käyttäjä.

## Ominaisuudet

- Käyttäjä voi kirjautua sisään ja ulos sekä luoda uuden tunnuksen
- Käyttäjä on joko tavallinen käyttäjä tai ylläpitäjä
- Tavallinen käyttäjä voi kirjoittaa elokuva-arvosteluita
- Ylläpitäjä voi hallinnoida elokuvia:
  - Uuden elokuvan lisääminen
  - Elokuvan poistaminen näkyvistä
  - Poistetun elokuvan palauttaminen näkyville
- Ylläpitäjä voi hallinnoida käyttäjiä:
  - Tavallinen käyttäjä voidaan ylentää ylläpitäjäksi
  - Tavallinen käyttäjä voidaan asettaa porttikieltoon
    - Porttikiellon saanut käyttäjä ei voi enää kirjautua sisään
    - Porttikiellon saaneen käyttäjän kirjoittamat arvostelut poistuvat näkyviltä eivätkä enää vaikuta tilastoihin
    - Käyttäjän saama porttikielto voidaan myös perua
- Ylläpitäjä voi generoida listan maista ja maanosista
  - Maalistausta käytetään kotimaan asettamiseksi käyttäjille, elokuville, ohjaajille ja käsikirjoittajille
- Sivustolla on tilastosivu, johon kootaan tietokannasta keskeisiä tietoja
- Etusivulla listataan tietokannasta löytyvät elokuvat
- Elokuvan nimeä klikkaamalla saadaan näkyviin lisää tietoa elokuvasta:
  - Nimi (name)
  - Kuvaus (description)
  - Julkaisuvuosi (year)
  - Julkaisumaa (country)
  - Kieli (language)
  - Lajityyppi (genre)
  - Ohjaaja (director)
  - Käsikirjoittaja (screenwriter)
- Käyttäjä voi antaa arvion elokuvasta ja lukea muiden antamia arvioita
  - Numeroarvosana 1-10
    - Numeroarvosanoista lasketaan keskiarvo, joka on elokuvan "arvosana" sivustolla
  - Sanallinen arvostelu
- Etusivun elokuvalistaus on mahdollista laittaa järjestykseen:
  - Aakkosjärjestyksessä (oletus)
  - Arvosanan perusteella parhaimmasta huonoimpaan
  - Arvosanan perusteella huonoimmasta parhaimpaan
  - Vuoden perusteella uusimmasta vanhimpaan
  - Vuoden perusteella vanhimmasta uusimpaan
- Elokuvia voi hakea:
  - Nimen perusteella

## Data
- Valtioiden tiedot: [un.org](https://www.un.org/en/about-us/member-states)
- Valtioiden liput: [countryflags.io](https://www.countryflags.io/)
- Favicon: [favicon.io](https://favicon.io/)