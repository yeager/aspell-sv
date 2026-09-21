# Changes

## Unreleased

- Adopt Språkrådet as the primary authority for language and writing rules.
- Bundle the reviewed rule catalogue and validate source evidence before
  conversion; reject context-only rules used as word corrections.
- Add policy regressions and the sourced word cases to `make check`.
- Use contextual numeric style advice without a fixed digit cutoff.
  Lexical contents and their original source pins are unchanged.

## 2026.09.21-rc2

- Apply 17 sourced spelling corrections to both modern and legacy inputs.
- Correct the enspann inflections inherited from Hunspell.
- Include reviewed compounds and accepted variants from the Swedish rule audit.
- Test whole words through libaspell, including punctuation, without hiding
  rejected spellings through command-line tokenization.
- Retain exact equality checks for every compiled word form.

Free compounds remain disabled; this is a dictionary preview.
The sourced rule catalogue is maintained in yeager/hunspell-sv under docs/
and copied here with its policy checks.
