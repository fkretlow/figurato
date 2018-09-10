#### MAC USERS, PLEASE READ THIS:
**There is [a bug in the underlying Qt framework](https://bugreports.qt.io/browse/QTBUG-69803) that affects the automatic positioning in Dorico on Mac. Please be aware that if you export your score from Dorico on Mac as pdf, the positioning of the figures will be turned upside down in the pdf, and what's more, this will most likely cause collisions for pretty much every figure that consists of more than one layer.**

The reason for this is that – unlike Mac-Dorico itself – the pdf layout engine interprets the positioning code correctly, but of course Dorico has previously positioned the figures according to how its own layout engine renders them. There is nothing I can do about this from inside the font.

**Sadly, I must therefore discourage all Mac users from using the current version of Figurato.**

(For what it's worth, you should be able to use the figures without automatic positioning in text objects with carriage returns.)


# Figurato
A figured bass font for Dorico  (Figurato works more or less as expected in Finale 25 as well.)

Version 0.3.0.26 (2018–09–10)  

### Recent Changes

#### 0.3
* The stacking order has been inverted. Figures are now automatically stacked top-down. Figures in documents that were created with a version prior to 0.3 will look different when you install this version.
* Accidentals can now be placed both to the left and to the right of the numbers in one figure.
* Support for parentheses has been expanded (still limited).
* Minor enhancements to the glyph outlines.

#### 0.2.1
* The line height has been reduced. Change the font size in documents that were created with a version prior to 0.2.1 to 50%. I recommend 9pt absolute.

## How to use
Use the font in text objects, in playing techniques or with the lyrics popover.

#### Characters
`n` = natural  
`b` = flat  
`#` = `s` = sharp  
`bb` = double flat  
`x` = double sharp  
`/` = combining slash  
`+` = plus  
`-` = `–` (endash) = `d` = dash  
`,` = separator

#### Layers
Figures are automatically stacked from top to bottom. If you need to skip a layer, type `,` (comma): `7n,3`

#### Accidentals
By default accidentals are placed *to the right of the preceding number.* If you want an accidental to be placed to the left of the following number, separate it from the preceding number with `,` (comma): `5,b3`.

You can place accidentals both to the left and to the right of numbers in one figure. Just type away and if something doesn't look like you expect, insert a `,` (comma) to make things unambiguous.

If you need a single accidental in the bottommost layer, separate it with `,` (comma): `5,b`

#### Slashed numbers and dashes
If you need a slashed number, type `/` (slash) or `+` (plus) after the number: `6/` or `6+`

If you need a dash type `-` (hyphen, doesn't work in Dorico's lyrics popover) `–` (endash) or `d`.

#### Parentheses and Brackets
There's limited support for parentheses and brackets. You can put one or more layers in parentheses or brackets: `(4)` `[63]` `6(42)` This does not reliably work with accidentals yet.

#### Italic numbers
Numbers preceded by `i` are printed in italic: `6i4i2`
