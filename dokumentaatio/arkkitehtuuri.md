
```mermaid
graph TD;
    ui["ui"]
    services["services"]
    repositories["repositories"]
    entities["entities"]

    ui -.-> services
    services -.-> repositories
    services -.-> entities
    repositories -.-> entities

