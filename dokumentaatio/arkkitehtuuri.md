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

### Päätoiminnallisuudet

#### Käyttäjä kirjoittaa tekstiä

```mermaid
sequenceDiagram
    participant U as User
    participant UI as UI/MainApplication
    participant DN as DrawNode
    participant N as Node

    U->>UI: Klikataan canvasta
    UI->>DN: on_canvas_click(event)
    DN->>DN: get_node(canvas, root_node, x, y, width, height, click_x, click_y)
    DN->>N: Määritellään active_node
    N-->>DN: Palautetaan noden tiedot
    DN-->>UI: Määrätään active_node

    U->>UI: Kirjoitetaan tekstiä kenttään ja painetaan enter
    UI->>DN: on_entry_return(event)
    DN->>N: Update node text, font and style
    DN->>DN: draw_tree()
    DN->>UI: Piirretään uudestaan päivitetty puu
    UI-->>U: Näytetään päivitetty puu
```

- Käyttäjä klikkaa jotakin solmua canvaksella: DrawNode-luokassa käynnistyy on_canvas_click-tapahtumankäsittelijä.
- Määritellään aktiivinen solmu: Klikkauksen sijainnin perusteella DrawNode saa selville aktiivisen solmun get_node-metodilla.
- Päivitetään solmun tiedot: Kun käyttäjä kirjoittaa tekstiä ja painaa enter, kutsutaan on_entry_return-metodia, joka päivittää aktiivisen solmun tiedot.
- Piirretään puu uudelleen: Puu piirretään aina uudelleen päivitetyillä tiedoilla.
