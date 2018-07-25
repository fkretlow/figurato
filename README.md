# Figurato
A figured bass font for Dorico  
(Figurato works more or less as expected in Finale 25 as well.)  
**Tested only on Windows!**  
Version 0.2 (2018–07–25)

Use the font in text objects, in playing techniques or with the lyrics popover.  

#### Characters
`n` = natural  
`b` = flat  
`#` = `s` = sharp  
`bb` = double flat  
`x` = double sharp  
`/` = combining slash  
`+` = plus  
`-` = `d` = dash  
`,` = separator

#### Layers
Figures are automatically stacked from bottom to top. If you need to skip a layer, type `,` (comma): `3,7n`

#### Accidentals
By default accidentals are placed *to the right of the preceding number.* If you want accidentals to be placed to the left of the following number, separate the first accidental from the preceding number with `,` (comma): `3,b5`.

You cannot place accidentals both to the left and to the right of numbers in the same figure.

In figures with only two characters the accidental is automatically placed to the left or the right of the number according to the string you type: `b7` or `7b`.

If you need a single accidental in the bottommost layer, separate it with `,` (comma): `b,5`

#### Slashed numbers and dashes
If you need a slashed number, type `/` (slash) or `+` (plus) after the number: `6/` or `6+`

If you need a dash type `-` (hyphen, doesn't work in Dorico's lyrics popover) or `d`.

#### Parentheses and Brackets
Rudimentary support for parentheses and brackets has been added. You can put a whole layer or an accidental in parentheses or brackets. Currently this works only with accidentals to the right of the numbers: `(4)` or `[6b]` or `24(b)`

#### Italic numbers
Numbers preceded by `i` are printed in italic: `2i4i6`
