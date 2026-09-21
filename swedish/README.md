# Swedish Aspell dictionary preview

This directory is a standalone dictionary distribution. The parent repository
is a fork of GNU Aspell; dictionary releases use the system Aspell engine.

The list contains 943,340 explicit forms from aspell-sv-0.51-0 and the pinned
hunspell-sv revision recorded in stats.json. Free compound joining is disabled
because it accepted known misspellings. Valid unseen compounds can therefore
be rejected; this preview is not equivalent to Hunspell's compound grammar.
4,379 candidates were excluded for character/format reasons.

## Build and test

Requires Aspell 0.60 and Python 3; the runtime dictionary needs only Aspell.

    make
    make check
    sudo make install

Use `aspell --lang=sv --encoding=utf-8 list` after installation. To test without
installation, run `make check`. Override ASPELL, DESTDIR, dictdir or datadir as
needed. RWS files are architecture-dependent: compile on the destination
platform or install a matching RPM. The Debian package compiles its hash on
installation and is Architecture: all.

## Reproduce the lexical conversion

Obtain https://ftp.gnu.org/gnu/aspell/dict/sv/aspell-sv-0.51-0.tar.bz2 and
https://github.com/yeager/hunspell-sv at commit
6cd0c2d1796f97ac260011a9859ce89926f20eb8. Verify source-sha256.json, unpack,
and run:

    python3 tools/convert.py /path/to/hunspell-sv /path/to/aspell-sv-0.51-0 /tmp/converted
    python3 tools/validate.py /path/to/hunspell-sv /tmp/converted

The exported merged.txt is this distribution's sv.wl. The package's sv.dat
additionally declares data-encoding utf-8 for install-time hash generation.
The old FSF postal address in the phonetic-file comment is updated.
No network access or regeneration of lexical data occurs during package builds.

## Packaging

Debian/Ubuntu: `dpkg-buildpackage -b -us -uc` with debhelper-compat 13,
dictionaries-common-dev, aspell, make and Python 3 installed.

RPM/Fedora: use packaging/rpm/aspell-sv.spec with a tarball of this directory
named aspell-sv-2026.09.21.tar.gz. The native-architecture RPM depends on
Aspell and installs in its dictionary directory. An SRPM permits other
architectures to rebuild the same source.

## Provenance and licenses

COPYING.aspell and Copyright.aspell retain the original LGPL 2.1 terms with
updated FSF address information. sv_phonet.dat has a separate GPL-2.0-or-later
notice by Martin Norbäck; COPYING.GPL2 supplies that license text.
LICENSE.hunspell preserves the modern source's LGPL 3 declaration; COPYING
and COPYING.LESSER contain GPL 3 and LGPL 3. The conversion/build contributions
are provided under LGPL 3. The source inventories do not establish a complete
rights audit for every lexical input, nor resolve combined redistribution
terms. Formal distribution acceptance requires that separate review.

This is an unsigned third-party preview, not an official GNU or distribution
release. Upstream review: https://github.com/GNUAspell/aspell/issues/692

## Swedish consonant deletion

Tests cover reduced compounds such as äggula, glasstrut, nattåg and tillåta,
and reject their triple-consonant misspellings. Hyphenated spellings such as
ägg-gula, till-låta and glass-skål are included as explicit reviewed forms.
This checks spellings; it does not implement automatic line breaking.
See https://frageladan.isof.se/faqs/31080 and
https://frageladan.isof.se/faqs/30528. The rule concerns consonants, not vowels.

## Reviewed Swedish rules

The conversion applies the 17 entries in lexical-corrections.json to both
source lists, removing nine misspellings from the legacy input. These are
reviewed word-level corrections, not a general character replacement rule.
The source catalogue covers 35 linguistic and writing-rule topics:
https://github.com/yeager/hunspell-sv/blob/6cd0c2d1796f97ac260011a9859ce89926f20eb8/docs/svenska-regler.md

Package checks use libaspell directly for 201 accepted and 49 rejected whole
words and compare every compiled form with sv.wl. Grammar and style examples
are documented separately; word acceptance does not validate a sentence.
