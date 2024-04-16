## Rakenne

Koodin pakkausrakenne näyttää tältä:

```mermaid
graph TD;
    subgraph services ["services"]
        DrawNode[("DrawNode")]
        HtmlBuilder[("TreeBuilder")]
        TreeBuilder[("HtmlBuilder")]
    end

    ui[("ui")]
    repositories[("repositories")]
    entities[("entities")]

    ui --> services
    services -->|uses| repositories
    services -->|uses| entities
    repositories -->|uses| entities
```

- Pakkaus _ui_ sisältää käyttöliittymästä vastaavat luokat, eli käyttäjälle näkyvän sovelluksen osan.
- Pakkaus _services_ tarjoaa sovelluslogiikan, jota käyttöliittymä käyttää.
- Pakkaus _repositories_ sisältää tietojen pysyväistallennuksesta vastaavat luokat.
- Pakkaus _entities_ sisältää sovelluksen datamalleista vastaavat luokat.

### Sovelluslogiikka

- Luokka DrawNode kuvaa solmun eli div-elementin piirtämistä.
- Luokka TreeBuilder kuvaa puun rakentamista eli layoutin luomista.
- Luokka HtmlBilder kuvaa puun muuntamista html-tiedostoksi. 
