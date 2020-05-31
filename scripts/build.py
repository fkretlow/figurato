import fontforge

def generateWithFeatures(font, fea, dest):
    # make sure no old lookups remain
    for l in font.gpos_lookups:
        f.removeLookup(l)
    for l in font.gsub_lookups:
        f.removeLookup(l)
    font.mergeFeature(fea)
    font.generate(dest)


if __name__ == "__main__":
    f = fontforge.open("./src/Figurato.sfd")

    print("generating FiguratoT.otf")
    generateWithFeatures(f, "./src/figurato_T.fea", "./redist/FiguratoT.otf")
    print("generating FiguratoB.otf")
    generateWithFeatures(f, "./src/figurato_B.fea", "./redist/FiguratoB.otf")

    f.close()
