# Elokuva-arvostelusovellus

Sovelluksessa listataan tietoa elokuvista, joille käyttäjät voivat kirjoittaa arvosteluita. Jokainen käyttäjätunnus on peruskäyttäjä (user) tai ylläpitäjä (admin). Ylläpitäjällä on oikeus hallinnoida käyttäjätilejä ja elokuvia sekä niiden tietoja. Sovelluksen käyttöliittymä on englanninkielinen ja sen nimi on yksinkertaisesti *Film review app*.

## Testaaminen

Sovellusta voi testata osoitteessa https://tsoha-elokuvasovellus.herokuapp.com/  
Heroku päivitetty tiistaina 4.5.

Sovelluksessa on yksi pääkäyttäjä, jonka tunnus on **admin** ja salasana **password**. Vain tälle käyttäjälle on näkyvissä etusivulla "admin-paneeli", jonka kautta voidaan lisätä uusia elokuvia sovellukseen. Ylläpitäjätunnuksella voi testata uuden elokuvan lisäämistä. Huomaathan, että maalistauksen generoiva painike ei toimi Herokussa enää toista kertaa, sillä sitä on jo painettu. Sen toimivuuden voi todeta uutta elokuvaa luodessa siitä, että valikosta löytyy lista maista, jotka on luettu tiedostosta [countries.csv](https://github.com/rvrauhala/tsoha-elokuvasovellus/blob/main/data/countries.csv). Katso myös tiedosto [countries.py](https://github.com/rvrauhala/tsoha-elokuvasovellus/blob/main/countries.py), josta löytyy listauksen generoiva koodi.

Sovelluksen testaamista ja elokuva-arvosteluiden lisäämistä varten kannattaa luoda uusi käyttäjätunnus, joka on oletuksena tavallinen käyttäjä.

## Ominaisuudet

Lista päivitetty perjantaina 7.5.

- Käyttäjä voi kirjautua sisään ja ulos sekä luoda uuden tunnuksen
- Käyttäjä on peruskäyttäjä tai ylläpitäjä
- Sivustolla on tilastosivu, johon kootaan tietokannasta keskeisiä tietoja
- Sivustolla listataan tietokannasta löytyvät elokuvat
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
- Elokuvalistaus on mahdollista laittaa järjestykseen:
  - Aakkosjärjestyksessä (oletus)
  - Arvosanan perusteella parhaimmasta huonoimpaan
  - Arvosanan perusteella huonoimmasta parhaimpaan
  - Vuoden perusteella uusimmasta vanhimpaan
  - Vuoden perusteella vanhimmasta uusimpaan
- Ylläpitäjä voi lisätä uuden elokuvan
- Ylläpitäjä voi hallinnoida elokuvia:
  - Ylläpitäjä voi poistaa elokuvan näkyvistä
  - Ylläpitäjä voi palauttaa poistetun elokuvan näkyviin
- Ylläpitäjä voi generoida listan maista ja maanosista

## To-do

- Hakutoiminto
- Elokuvan tietojen muokkaustoiminto
- Arvioiden muokkaus- ja/tai poistotoiminto
- Syötteiden validoinnin lisääminen ja tarkentaminen
- Ulkoasun ja käyttöliittymän parantelua

## Data
- Valtioiden tiedot: [un.org](https://www.un.org/en/about-us/member-states)
- Valtioiden liput: [countryflags.io](https://www.countryflags.io/)
- Favicon: [favicon.io](https://favicon.io/)