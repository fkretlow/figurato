## Figurato

### FiguratoMac

**Don't use Figurato or FiguratoB with Dorico on Mac. Do use FiguratoMac instead.**  
There is no need to use FiguratoMac with Finale or Sibelius (greater than 2018.11) on Mac.

FiguratoMac uses precomposed figures instead of OpenType positioning features to bypass [a bug in the Qt framework](https://bugreports.qt.io/browse/QTBUG-69803) that Dorico is built upon. That bug prevents the positioning code of the normal version from working correctly. Meanwhile the bug has been fixed by the Qt developers, but the fix won’t be ported into Dorico until the next major release (probably 3.0 in mid 2019).

**Additions to Figurato after version 0.5 (see [changelog](changelog.md)) have not been and will not be ported to FiguratoMac.** (I’m sorry, this would just be too much work.)

#### Portability
As for how to input figures, FiguratoMac works exactly like Figurato 0.5. Therefore Dorico projects that were created with FiguratoMac will look the same on Windows if you replace FiguratoMac with Figurato (which you don't need to do because FiguratoMac works on Windows).

The reverse is not completely true, because FiguratoMac comes with a few limitations:

- Parentheses and brackets are not supported.
- Italic figures are not supported.
- A vast, but limited number of figures is supported.

Dorico projects that were created with Figurato on Windows will look the same on Mac if you replace Figurato with FiguratoMac, except for figures that contain italic numbers, parentheses, or brackets, and for figures that have not been added as ligatures in FiguratoMac yet.

If you want to be sure right from the start, there's no reason not to use FiguratoMac with Dorico on Windows in projects that must be accessible on both platforms.

#### Supported figures
FiguratoMac contains about 3.000 precomposed ligatures. Most of the commonly used figures should be supported. If you come across a figure that does not work as expected, please do notify me so I can add it. You can open an issue here in the repository. If you came here by following a link on the Dorico user forum, you could also post a request in that thread or shoot me a P.M.

[Back to the main manual](manual.md)