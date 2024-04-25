# HTML-editori

Sovellusta käytetään **HTML-dokumentin** tekemiseen. Käyttäjä voi luoda graafisella käyttöliittymällä mieleisensä _staattisen nettisivun_. 

- [Vaatimusmäärittely](/dokumentaatio/vaatimusmaarittely.md)
- [Changelog](/dokumentaatio/changelog.md)
- [Tuntikirjanpito](/dokumentaatio/tuntikirjanpito.md)
- [Arkkitehtuurikuvaus](/dokumentaatio/arkkitehtuuri.md)
- [Release](https://github.com/gitelras/ot-harjoitustyo/releases/tag/viikko5)
  
## Käynnistä sovellus

Asenna projektin riippuvuudet

```bash
poetry install
```

Suorita alustustoimenpiteet

```bash
poetry run invoke build
```

Käynnistä sovellus

```bash
poetry run invoke start
```

## Testaa sovellusta

Suorita testit

```bash
poetry run invoke test
```

Generoi halutessasi testikattavuusraportti

```bash
poetry run invoke coverage-report
```

Avaa testikattavuusraportti selaimessa

```bash
poetry run invoke show-report
```

## Pylint

Suorita tiedoston [.pylintrc](./.pylintrc) tarkistukset

```bash
poetry run invoke lint
```




