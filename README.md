# Elokuva-arvostelusovellus

Sovelluksessa listataan tietoa elokuvista, joille käyttäjät voivat kirjoittaa arvosteluita. Jokainen käyttäjätunnus on tavallinen käyttäjä (user) tai ylläpitäjä (admin). Ylläpitäjällä on oikeus hallinnoida käyttäjätilejä ja elokuvia sekä niiden tietoja. Sovelluksen käyttöliittymä on englanninkielinen ja sen nimi on yksinkertaisesti Film review app tai lyhennettynä FRA. Katso tarkempi ominaisuuslista alempana.

## Testaaminen

Sovellusta voi testata osoitteessa https://rvr-fra.herokuapp.com/

Sovelluksessa on yksi julkinen pääkäyttäjä, jonka tunnus on **admin** ja salasana **password**. Tälle käyttäjälle on näkyvissä etusivulla "admin-paneeli", jonka kautta voidaan lisätä uusia elokuvia sovellukseen, hallinnoida elokuvia ja käyttäjiä sekä generoida [tiedostosta](https://github.com/rvrauhala/tsoha-elokuvasovellus/blob/main/data/countries.csv) maalistaus sovelluksen käyttöön. Ylläpitäjätunnuksella voi testata vain ylläpitäjälle tarkoitettuja toimintoja. Huomaathan, että maalistauksen generoiva painike ei toimi Herokussa enää toista kertaa, sillä sitä on jo painettu.

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