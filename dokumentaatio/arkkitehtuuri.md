## Rakenne

Koodin pakkausrakenne näyttää tältä:

```mermaid
graph TD;
    subgraph services ["services"]
        DrawNode[("DrawNode")]
        TreeBuilder[("TreeBuilder")]
        HtmlBuilder[("HtmlBuilder")]
    end

    ui[("ui")]
    repositories[("repositories")]
    entities[("entities")]

    ui -.-> services
    services -.-> repositories
    services -.-> entities
    repositories -.-> entities

    DrawNode -.-> TreeBuilder
    HtmlBuilder -.-> DrawNode
```

- Pakkaus _ui_ sisältää käyttöliittymästä vastaavat luokat, eli käyttäjälle näkyvän sovelluksen osan.
- Pakkaus _services_ tarjoaa sovelluslogiikan, jota käyttöliittymä käyttää.
- Pakkaus _repositories_ sisältää tietojen pysyväistallennuksesta vastaavat luokat.
- Pakkaus _entities_ sisältää sovelluksen datamalleista vastaavat luokat.

### Sovelluslogiikka

- Luokka [DrawNode](/src/services/draw_node.py) kuvaa solmun eli div-elementin piirtämistä.
- Luokka [TreeBuilder](/src/services/tree_builder.py) kuvaa puun rakentamista eli layoutin luomista.
- Luokka [HtmlBuilder](/src/services/html_builder.py) kuvaa puun muuntamista html-tiedostoksi. 
