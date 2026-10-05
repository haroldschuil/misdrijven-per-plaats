# Misdrijven per plaats

Een eenvoudige webapp die politiecijfers van [data.politie.nl](https://data.politie.nl) ontsluit. Kies een woonplaats, een soort misdrijf en een tijdsspanne en zie hoeveel misdrijven de politie heeft geregistreerd, of er sprake is van groei of afname en hoe twee plaatsen zich tot elkaar verhouden.

## Starten

Download of clone de repository en voer in de map uit:

```
python3 server.py
```

Op Windows: `py server.py`. De app opent op http://localhost:8000. Stoppen met Ctrl+C.

`server.py` haalt de cijfers op bij de politie-API en geeft ze door aan de app. Dat is nodig omdat browsers rechtstreekse verzoeken naar de API kunnen blokkeren (CORS). Het script gebruikt alleen standaard Python en laat alleen tabel 47015NED door.

Zonder `server.py` (bijvoorbeeld via GitHub Pages) probeert de app de API rechtstreeks. Of dat werkt, hangt af van de CORS-instellingen van de API en is niet getest.

## Bron

- Tabel 47015NED, *Geregistreerde misdrijven; soort misdrijf, plaats*: https://data.politie.nl/#/Politie/nl/dataset/47015NED/table
- API: `https://dataderden.cbs.nl/ODataApi/OData/47015NED`
- Definities: https://www.politie.nl/algemeen/dataportaal/dataportaal-definities.html
- Licentie van de data: CC-BY 4.0, © Politie

## Wat de cijfers wel en niet zeggen

- **Geregistreerde misdrijven, geen aangiften.** Een misdrijf telt als de politie het heeft vastgelegd in een proces-verbaal van aangifte of een ambtshalve proces-verbaal. Pogingen tellen mee.
- **Alleen maandcijfers.** De politie publiceert per maand, rond de 15e van de volgende maand. Weekcijfers bestaan niet.
- **Groei of afname** wordt vergeleken met dezelfde periode een jaar eerder (geen seizoenseffect) en, bij 1 en 3 maanden, met de voorgaande periode.
- **Toevalsindicatie:** z = (A − B) / √(A + B), een benadering voor het verschil tussen twee telgetallen (Poisson). Bij |z| < 2 is het verschil goed verklaarbaar door toeval. Dit is een vuistregel, geen formele toets.
- **Geen inwonertallen.** Absolute aantallen van plaatsen met verschillende omvang zijn niet één op één vergelijkbaar.
- **Verborgen delicten:** zedendelicten, kinderporno, kinderprostitutie en maatschappelijke integriteit (overig) staan niet per maand in deze tabel.
- **Cijfers worden achteraf bijgewerkt.** Recente maanden kunnen nog veranderen.
