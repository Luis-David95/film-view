# Elokuva-arvostelusovellus

Sovelluksessa listataan tietoa elokuvista, joille käyttäjät voivat kirjoittaa arvosteluita. Jokainen käyttäjätunnus on peruskäyttäjä (user) tai ylläpitäjä (admin). Ylläpitäjällä on oikeus hallinnoida käyttäjätilejä ja elokuvia sekä niiden tietoja. Sovelluksen käyttöliittymä on englanninkielinen ja sen nimi on yksinkertaisesti *Film review app*.

## Testaaminen

Sovellusta voi testata osoitteessa https://tsoha-elokuvasovellus.herokuapp.com/  

Sovelluksessa on yksi pääkäyttäjä, jonka tunnus on **admin** ja salasana **password**. Vain tälle käyttäjälle on näkyvissä etusivulla "admin-paneeli", jonka kautta voidaan lisätä uusia elokuvia sovellukseen. Ylläpitäjätunnuksella voi testata uuden elokuvan lisäämistä. Huomaathan, että maalistauksen generoiva painike ei toimi Herokussa enää toista kertaa, sillä sitä on jo painettu. Sen toimivuuden voi todeta uutta elokuvaa luodessa siitä, että valikosta löytyy lista maista, jotka on luettu tiedostosta [countries.csv](https://github.com/rvrauhala/tsoha-elokuvasovellus/blob/main/data/countries.csv). Katso myös tiedosto [countries.py](https://github.com/rvrauhala/tsoha-elokuvasovellus/blob/main/countries.py), josta löytyy listauksen generoiva koodi. 

Sovelluksen testaamista ja elokuva-arvosteluiden lisäämistä varten kannattaa luoda uusi käyttäjätunnus, joka on oletuksena tavallinen käyttäjä.

## Ominaisuudet

Toteutetut ja toimivat ominaisuudet on merkittu "✓"-tunnuksella.  
Lista päivitetty sunnuntaina 25.4.

- Käyttäjä voi kirjautua sisään ja ulos sekä luoda uuden tunnuksen ✓
- Käyttäjä on peruskäyttäjä tai ylläpitäjä ✓
- Sivustolla listataan tietokannasta löytyvät elokuvat ✓
- Elokuvan nimeä klikkaamalla saadaan näkyviin lisää tietoa elokuvasta:
  - Nimi (name) ✓
  - Kuvaus (description) ✓
  - Julkaisuvuosi (year) ✓
  - Julkaisumaa (country) ✓
  - Kieli (language)
  - Lajityyppi (genre)
  - Ohjaaja (director)
  - Käsikirjoittaja (screenwriter)
- Käyttäjä voi antaa arvion elokuvasta ja lukea muiden antamia arvioita ✓
  - Numeroarvosana esim. 1-10 ✓
    - Numeroarvosanoista lasketaan keskiarvo, joka on elokuvan "arvosana" sivustolla
  - Sanallinen arvostelu ✓
- Käyttäjä voi hakea elokuvia elokuvan nimen, kuvauksen tai lajityypin perusteella
- Elokuvalistaus on mahdollista ladata aakkosjärjestyksessä tai arvosanan perusteella parhaimmasta huonoimpaan
- Ylläpitäjä voi lisätä elokuvia ✓
- Ylläpitäjä voi poistaa elokuvan tietokannasta
- Ylläpitäjä voi generoida listan maista ja maanosista ✓
- Ylläpitäjä voi muokata käyttäjän tai elokuvan tietoja
- Ylläpitäjä voi tarvittaessa poistaa käyttäjän antaman arvion