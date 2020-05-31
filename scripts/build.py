import fontforge

def generateWithFeatures(font, fea, name, dest="./redist/"):
    # make sure no old lookups remain
    for l in font.gpos_lookups:
        font.removeLookup(l)
    for l in font.gsub_lookups:
        font.removeLookup(l)
    font.mergeFeature(fea)
    font.familyname = name
    font.fontname = name
    font.generate(dest + name + ".otf")


if __name__ == "__main__":
    f = fontforge.open("./src/Figurato.sfd")

    print("generating Figurato.otf")
    generateWithFeatures(f, "./src/figurato_T.fea", "Figurato")
    print("generating FiguratoB.otf")
    generateWithFeatures(f, "./src/figurato_B.fea", "FiguratoB")

    f.close()
