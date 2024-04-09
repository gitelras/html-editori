# HTML-editori

Sovellusta käytetään **HTML- ja CSS-dokumentin** tekemiseen. Käyttäjä voi luoda graafisella käyttöliittymällä mieleisensä _staattisen nettisivun_. 

- [Vaatimusmäärittely](/dokumentaatio/vaatimusmaarittely.md)
- [Changelog](/dokumentaatio/changelog.md)
- [Tuntikirjanpito](/dokumentaatio/tuntikirjanpito.md)

## Käynnistä sovellus näin

Asenna projektin riippuvuudet

```bash
poetry install
```

Suorita alustustoimenpiteet

```bash
poetry run invoke build
```

Käynnistä

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

Avaa testikattavuusraportti

```bash
poetry run invoke show-report
```





