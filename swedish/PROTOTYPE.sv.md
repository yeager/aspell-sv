# Svensk Aspell – lokal konverteringsprototyp

Hunspell-ordlistan kan användas för att utöka Aspells svenska ordbok.
Den här prototypen innehåller **943 338 ordformer**, varav **823 757** saknas
som explicita poster i Aspell-paketet från 2004. Det är antal ordformer,
inte antal grundord eller ett mått på språklig kvalitet.

## Källor och byggmetod

- Aspell: https://ftp.gnu.org/gnu/aspell/dict/sv/aspell-sv-0.51-0.tar.bz2
- Hunspell: https://github.com/yeager/hunspell-sv
- Hunspell-källrevision: `e7e8828fa986aaf16a69f47d8b5a4450c29b8883`.
- Aspell 0.60.8.2 och systemets libhunspell 1.7 användes lokalt.

`convert.py` läser huvudordlistan och genererar dess enkla suffixformer.
Projektets testord tas också med som explicita kandidater, så att exempelvis
`applikationsserver` bevaras utan fri sammansättning.
Varje kandidat kontrolleras med libhunspell innan den förenas med den gamla
Aspell-listan. Poster med ONLYINCOMPOUND, NOSUGGEST eller FORCEUCASE hoppas
konservativt över; NEEDAFFIX-stammar exporteras inte ensamma. Explicita
FORBIDDENWORD-poster tas bort även ur den gamla listan (10 gamla poster).
Inga nya dynamiska sammansättningar genereras.

```bash
python3 convert.py /path/to/hunspell-sv /path/to/aspell-sv-0.51-0 /path/to/output
```

Skriptet kräver Python 3, `aspell`, `word-list-compress` och libhunspell 1.7.
Det avbryter vid prefixregler, alternativa flaggformat eller kedjade suffix
som det inte stöder. Det är anpassat till den undersökta revisionen, inte
en generell Hunspell-konverterare.

## Testa utan systeminstallation

Kör från den här katalogen:

```bash
printf '%s\n' meddelandekö symlänk filbläddrare Kubernetes stavvningskontroll |
  aspell --lang=sv --encoding=utf-8 \
    --local-data-dir="$PWD" --dict-dir="$PWD" --master=sv.rws list
```

Endast `stavvningskontroll` ska skrivas ut. För jämförelse kan du använda
`--master=sv-baseline.rws`. Originalet känner inte igen de fyra första
orden i detta test. `verification.json` redovisar 59 korrekta ord och 16
felstavningar, samt en exakt jämförelse av alla kompilerade ordformer med exporten.
Kör `python3 validate.py /path/to/hunspell-sv` för att upprepa valideringen.

## Begränsningar

- Hunspells sammansättningsregler har **inte** porterats. Aspells gamla
  `run-together` är avstängd eftersom den annars accepterar bland annat
  `översätning` och `säkerhett`. Korrekt sammansatta ord som inte finns bland
  de exporterade formerna kan därför flaggas som fel. Detta är ett medvetet
  val för att undvika fri sammansättnings falska godkännanden.
- Aspells gamla svenska ISO-8859-1-alfabet används. 4 379 förenade kandidater
  uteslöts på grund av tecken eller format; alla finns i `excluded.txt`.
- NOSUGGEST och andra specialflaggor har inte fullständiga Aspell-motsvarigheter
  i exporten. En äldre Aspell-post kan finnas kvar även om en Hunspell-post
  med samma stavning utesluts, utom vid explicit FORBIDDENWORD.
- Hunspell-godkännande är inte en språkgranskning. Befintliga lexikala fel
  kan följa med, och de små stavningstesterna mäter inte generell kvalitet.
- RWS-filerna är byggda i den här Linuxmiljön. Bygg om dem på målsystemet.
- Detta är ett tekniskt lokalt prov, inte en färdig upstream-utgåva.
  Båda källornas licensfiler medföljer separat; inget gemensamt licensval
  eller någon bedömning av rättigheterna till alla underkällor har gjorts.

## Filer

- `merged.txt`: exporterade ordformer i UTF-8.
- `sv.rws`, `sv.multi`, `sv.dat`, `sv_phonet.dat`: lokal Aspell-ordbok.
- `sv-baseline.rws`: originalet för jämförelser.
- `convert.py`: reproducerbar konvertering med externa källkataloger.
- `validate.py`: lokal integrationskontroll, inklusive affixreglernas antal.
- `stats.json`, `verification.json`: mätvärden och testresultat.
- `excluded.txt`: uteslutna ordformer.
- `COPYING.aspell`, `Copyright.aspell`, `LICENSE.hunspell`: källornas licenstexter.
