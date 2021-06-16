# Film review app

## Summary

**Film review app** is a simple web application for writing film reviews. Every user account is either a regular *user* or an *admin* with additional privileges. Administrators may add new films to the database and ban/unban or promote regular users. The application was developed using the [Flask](https://palletsprojects.com/p/flask/) web application framework. A [PostgreSQL](https://www.postgresql.org/) database is used to store all relevant information needed by the application. Also, a demo version of the app is hosted on [Heroku](https://www.heroku.com/home).

## How to install

(To-do)

## How to test

A demo version of *Film review app* can be found on [Heroku](https://rvr-fra.herokuapp.com/). You may use it to see how the application works without installing it on your machine.

The application has one public administrator account for testing purposes. The username is **admin** and the password is **password**. After logging in, on the front page there should be an admin panel only visible to admin accounts. By using the admin panel you may perform administrative actions such as adding new films to the database, generating a country list (this only works once though) or managing user accounts.

To test regular user functionality, you may create a new account by clicking "Register" on the front page and choosing a username, password and your country.

Please do not submit any offensive content or sensitive data.

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