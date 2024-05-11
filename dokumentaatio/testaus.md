# Testausdokumentti

Ohjelman testaus koostuu automatisoidusta yksikkö- ja integraatiotestauksesta sekä manuaalisesta järjestelmätason testauksesta. Automatisoidut testit on toteutettu Pythonin unittest-kirjastolla.

## Yksikkötestaus

### Sovelluslogiikka

- HtmlBuilder-luokkaa testataan [TestHtmlBuilder](/src/tests/html_builder_test.py)-testiluokalla.
- DrawNode-luokkaa testataan [TestDrawnode](/src/tests/test_draw_node.py)-testiluokalla.
- TreeBuilder-luokkaa testataan [TestTreeBuilder](/src/tests/tree_builder_test.py)-testiluokalla. 
