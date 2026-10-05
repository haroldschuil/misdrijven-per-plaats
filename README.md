# Misdrijven per plaats

Een eenvoudige webapp die politiecijfers van [data.politie.nl](https://data.politie.nl) ontsluit. Kies een woonplaats of gemeente, een soort misdrijf en een tijdsspanne en zie hoeveel misdrijven de politie heeft geregistreerd, of er sprake is van groei of afname en hoe twee plaatsen zich tot elkaar verhouden. Op gemeenteniveau ook misdrijven met aangifte, internetaangiften en cijfers per 1.000 inwoners.

## Starten

Download of clone de repository en voer in de map uit:

```
python3 server.py
```

Op Windows: `py server.py`. De app opent op http://localhost:8000. Stoppen met Ctrl+C.

`server.py` haalt de cijfers op bij de politie-API en geeft ze door aan de app. Dat is nodig omdat browsers rechtstreekse verzoeken naar de API kunnen blokkeren (CORS). Het script gebruikt alleen standaard Python en laat alleen de drie brontabellen door.

Zonder `server.py` (bijvoorbeeld via GitHub Pages) probeert de app de API rechtstreeks. Of dat werkt, hangt af van de CORS-instellingen van de API en is niet getest.

## Online zetten (klikbare link)

GitHub Pages werkt niet goed voor deze app, omdat server.py daar niet draait en de browser de politie-API dan rechtstreeks moet aanroepen. Netlify kan de doorgeefrol van server.py overnemen; de instellingen staan in `netlify.toml`.

1. Ga naar https://app.netlify.com en log in met je GitHub-account.
2. Kies *Add new site* > *Import an existing project* > *GitHub* en selecteer deze repository.
3. Laat alle instellingen leeg en klik *Deploy*.
4. Pas eventueel de naam aan via *Site configuration* > *Change site name*, bijvoorbeeld `misdrijven-per-plaats`. De app staat dan op https://misdrijven-per-plaats.netlify.app.

Elke push naar `main` zet Netlify automatisch opnieuw online.

## Bron

- Woonplaats: tabel 47015NED, *Geregistreerde misdrijven; soort misdrijf, plaats*: https://data.politie.nl/#/Politie/nl/dataset/47015NED/table
- Gemeente: tabel 47013NED, *Geregistreerde misdrijven en aangiften; soort misdrijf, gemeente 2026*: https://data.politie.nl/#/Politie/nl/dataset/47013NED/table
- Inwoners: CBS-tabel 03759ned, *Bevolking op 1 januari en gemiddeld; geslacht, leeftijd en regio*: https://opendata.cbs.nl/statline/#/CBS/nl/dataset/03759ned/table
- API's: `https://dataderden.cbs.nl/ODataApi/OData/` (politie) en `https://opendata.cbs.nl/ODataApi/OData/` (CBS)
- Definities: https://www.politie.nl/algemeen/dataportaal/dataportaal-definities.html
- Licentie van de politiedata: CC-BY 4.0, © Politie

## Wat de cijfers wel en niet zeggen

- **Geregistreerde misdrijven, geen aangiften.** Een misdrijf telt als de politie het heeft vastgelegd in een proces-verbaal van aangifte of een ambtshalve proces-verbaal. Pogingen tellen mee.
- **Misdrijven met aangifte** (in de tabel: Aangiften) zijn geregistreerde misdrijven waarvoor een proces-verbaal van aangifte is opgesteld. Per misdrijf kunnen meerdere aangiften gedaan zijn; het cijfer telt misdrijven, niet aangiften. Alleen op gemeenteniveau.
- **Aangiften lopen achter.** Bij een controle in oktober 2026 (gemeente Wageningen) liepen de aangiftecijfers twee maanden achter op de misdrijfcijfers. Of dat voor alle gemeenten geldt, is niet gecontroleerd. De app gebruikt per meetwaarde de laatste beschikbare maand.
- **Alleen maandcijfers.** De politie publiceert per maand, rond de 15e van de volgende maand. Weekcijfers bestaan niet.
- **Groei of afname** wordt vergeleken met dezelfde periode een jaar eerder (geen seizoenseffect) en, bij 1 en 3 maanden, met de voorgaande periode.
- **Toevalsindicatie:** z = (A − B) / √(A + B), een benadering voor het verschil tussen twee telgetallen (Poisson). Bij |z| < 2 is het verschil goed verklaarbaar door toeval. Dit is een vuistregel, geen formele toets.
- **Per 1.000 inwoners** (alleen gemeenten): bij een kalenderjaar gedeeld door de gemiddelde bevolking van dat jaar, bij een maandperiode door het aantal inwoners op 1 januari van het jaar waarin de periode eindigt. Voor woonplaatsen is geen inwonertal beschikbaar in deze bron.
- **Verborgen delicten:** zedendelicten, kinderporno, kinderprostitutie en maatschappelijke integriteit (overig) staan niet per maand in de tabellen. Op gemeenteniveau zijn jaarcijfers beschikbaar.
- **Cijfers worden achteraf bijgewerkt.** Recente maanden kunnen nog veranderen.
