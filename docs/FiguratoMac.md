## Figurato

[Figurato](../README.md) > [Manual](manual.md) > [Dorico](dorico.md)  > FiguratoMac

### FiguratoMac

**Don't use Figurato or FiguratoB with Dorico 1 or 2 on Mac. Use FiguratoMac instead.**
There is no need to use FiguratoMac with Dorico 3, Finale or Sibelius (greater than 2018.11).

FiguratoMac uses precomposed figures instead of OpenType positioning features to bypass [a bug in the Qt framework](https://bugreports.qt.io/browse/QTBUG-69803) that Dorico is built upon. That bug prevents the positioning code of the normal version from working correctly in Dorico versions prior to 3. **The bug is fixed in Dorico 3.**

#### Limitations
**Additions to Figurato after version 0.5 (see [changelog](changelog.md)) have not been and will not be ported to FiguratoMac.**

- Don’t refer to the Special Characters section of the main manual. FiguratoMac only contains one variant of each augmented figure (2, 4, 5, 6, 7 and 9), accessible by typinng `/` or `+` after the number.
- Parentheses and brackets are not supported.
- Italic figures are not supported.
- A vast, but limited number of figures is supported.

#### Portability
As for how to input figures, FiguratoMac works exactly like Figurato. Therefore Dorico projects that were created with FiguratoMac will look the same on Windows if you replace FiguratoMac with Figurato, except for augmented/slashed figures. (You don't need to switch to Figurato because FiguratoMac works on Windows).

Dorico projects that were created with Figurato on Windows will look the same on Mac if you replace Figurato with FiguratoMac, except for augmented/slashed figures, figures that contain italic numbers, parentheses, or brackets, and for figures that have not been added as ligatures in FiguratoMac yet.

If you want to be sure right from the start, there's no reason not to use FiguratoMac with Dorico on Windows in projects that must be accessible on both platforms.

#### Supported figures
FiguratoMac contains about 3.000 precomposed ligatures. Most of the commonly used figures should be supported. If you come across a figure that does not work as expected, please do notify me so I can add it. You can open an issue here in the repository. If you came here by following a link on the Dorico user forum, you could also post a request in that thread or shoot me a P.M.

[Back to the top](FiguratoMac.md#figurato)