# Testausdokumentti

Ohjelman testaus koostuu automatisoidusta yksikkö- ja integraatiotestauksesta sekä manuaalisesta järjestelmätason testauksesta. Automatisoidut testit on toteutettu Pythonin unittest-kirjastolla.

## Yksikkötestaus

### Sovelluslogiikka

- HtmlBuilder-luokkaa testataan [TestHtmlBuilder](/src/tests/html_builder_test.py)- ja [TestHtmlRepository](/src/tests/html_repository_test.py) -testiluokalla.
- DrawNode-luokkaa testataan [TestDrawnode](/src/tests/test_draw_node.py)-testiluokalla.
- TreeBuilder-luokkaa testataan [TestTreeBuilder](/src/tests/tree_builder_test.py)-testiluokalla. 

### Integraatiotestaus

- Save-luokkaa testataan [TestHtmlRepository](/src/tests/html_repository_test.py)-testiluokalla. Käytössä on testitietokanta, jota käytetään vain testaukseen.

## Järjestelmätestaus

- Sovellus on käynnistetty ja sitä on käytetty [käyttöohjeen](/dokumentaatio/kayttohje.md) mukaisella tavalla macOS- ja Linux-ympäristössä. 

- Kaikki [vaatimussmäärittelyssä](/dokumentaatio/kayttohje.md) mainitut toiminnallisuudet on testattu erilaisilla skenaariolla.

- Sovellusta on testattu tilanteissa, missä käyttäjä on nimennyt html-dokumentin tai jättänyt sen nimeämättä. 

- Sovelluksen tietokantakonfiguraatiota on testattu.

## Testikattavuus

Sovelluksen haarautumiskattavuus on 76% käyttöliittymää lukuunottamatta. Testauksen ulkopuolelle jäi sisäkkäisten div-elementtien luonti ja aktiivisen alueen tietojen päivittäminen. 

![Raportin kuva](/report.png "Raportti")

