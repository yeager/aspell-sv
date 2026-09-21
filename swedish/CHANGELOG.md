# Changes

## 2026.09.21-rc2

- Apply 17 sourced spelling corrections to both modern and legacy inputs.
- Correct the enspann inflections inherited from Hunspell.
- Include reviewed compounds and accepted variants from the Swedish rule audit.
- Test whole words through libaspell, including punctuation, without hiding
  rejected spellings through command-line tokenization.
- Retain exact equality checks for every compiled word form.

Free compounds remain disabled; this is a dictionary preview.
The sourced rule catalogue is maintained in yeager/hunspell-sv under docs/.
