## Figurato

[Figurato](../README.md) > Changelog  

#### Changelog

- Latest (1.0)
    - Added non-breaking space.
- 0.6.1
    - **Warning! Not fully backwards compatible:** cleaned up and finally consistent key bindings for modified numbers:
        - dashed numbers: `2/` and `2//`
        - "ticked" numbers: `2'` and `2''`
        - ligatures with plus: `2+`
    - Added support for the numbers 13 and 14.
    - Added two sets of dashed numbers.
    - Added `6\`, `i6\` and `7\`, `i7\`.
    - The italic set is now complete.
    - Better outlines for parentheses.
    - Much work on spacing between parentheses, accidentals, modified numbers and brackets.
- 0.5
    - Added FiguratoMac, a version of the font that bypasses the OpenType bug in Dorico on Mac by using precomposed figures instead of positioning rules.
- 0.4
    - Added support for the numbers 11 and 12.
    - Typing `|` (bar) registers an invisible opening or closing parenthesis or bracket.
    - Another version of the font, FiguratoB, has been added for figured bass indications above the staff. It works in the same way as Figurato, except that the figures are vertically aligned to the bottommost row.
- 0.3.2
    - Missing glyphs for parentheses that enclose three or more layers have been added.
    - Single accidentals in inner layers do no longer collide with numbers in adjacent layers.
    - The outlines of the italic numbers have been overhauled.
    - Slashed italic numbers have been added.
    - Accidentals in parentheses do no longer collide with the numbers they modify.
    - Parentheses and brackets that enclose up to three layers do now automatically avoid collisions with accidentals and slashed figures in almost all cases.
    - The kerning tables for accidentals (natural, flat, sharp) in up to three adjacent layers are now complete. As double flat and double sharp are rarely ever used for figured bass I consider working them into the tables not worth the (considerable) effort.
- 0.3
    - The stacking order has been inverted. Figures are now automatically stacked top-down. **Figures in documents that were created with a version prior to 0.3 will look different when you install the latest version.**
    - Accidentals can now be placed both to the left and to the right of the numbers in the same figure.
    - Support for parentheses has been expanded (still limited).
    - Minor enhancements to the glyph outlines.

- 0.2.1
    - The line height has been reduced. Change the font size in documents that were created with a version prior to 0.2.1 to 50%.  

[Back to the top](changelog.md#figurato)