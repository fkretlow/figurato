## FiguratoMac
FiguratoMac uses precomposed figures instead of OpenType positioning features to bypass [a bug in the Qt framework](https://bugreports.qt.io/browse/QTBUG-69803) that Dorico is built upon. That bug prevents the positioning code of the normal version from working correctly. **Don't use Figurato or FiguratoB with Dorico on Mac. Do use FiguratoMac instead.**

#### Portability
As for how to input figures, FiguratoMac works exactly like Figurato. Therefore Dorico projects that were created with FiguratoMac will look the same on Windows if you replace FiguratoMac with Figurato (which you don't need to do because FiguratoMac works on Windows). The reverse is not completely true, because FiguratoMac comes with a few limitations:

- Parentheses and brackets are not supported.
- Italic figures are not supported.
- A vast, but limited number of figures is supported.

Dorico projects that were created with Figurato on Windows will look the same on Mac if you replace Figurato with FiguratoMac, except for figures that contain italic numbers, parentheses, or brackets, and for figures that are not yet added as ligatures in FiguratoMac.

*If you want to be sure right from the start, there's no reason not to use FiguratoMac with Dorico on Windows in projects that must be accessible on both platforms.*

#### Supported figures
The initial version of FiguratoMac contains about 2900 precomposed ligatures. Most of the commonly used figures should be supported. If you come across a figure that does not work as expected, please do notify me so I can add it. You can open an issue here in the repository. If you came here by following a link on the Dorico user forum, you could also post a request in that thread or shoot me a P.M.  
(At some point I might upload the bundle of python scripts that I use to generate the composites so you can easily fork this repository and add figures yourself.)
