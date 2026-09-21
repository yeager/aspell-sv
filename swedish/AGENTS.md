# Svenska språkregler

Använd alltid Språkrådet (Isof) som förstahandskälla vid nya eller ändrade
svenska språkregler och skrivregler. Följ `docs/sprakpolicy.md`: kontrollera
aktuellt källstöd, dokumentera direkta hänvisningar och bevara accepterade
varianter. SAOL kompletterar för enskilda ord enligt Språkrådets hänvisningar.

Gör inte kontextberoende skrivråd till generella stavningsförbud. Uppdatera
regelunderlag och relevanta regressioner tillsammans. Kör `make check` före
inlämning. Håll `tools/check_language_policy.py`, `tests/test_language_policy.py`
och regelunderlaget synkroniserade med hunspell-sv; dokumentera källrevisionen
i README. Lexikala källrevisioner i stats.json/source-sha256.json beskriver
ordlistans ursprung och ska inte ändras när endast policyn uppdateras.
