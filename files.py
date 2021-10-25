def openEncoded(filename, mode="r"):
    return open(f"txtSrc/{filename}.txt", mode=mode, encoding="utf-8")


def getFileContents(filename):
    file = openEncoded(filename)
    contents = file.readlines()
    file.close()

    return contents


def printFile(filename):
    for line in getFileContents(filename):
        print(line, end="")


def inputFile(filename, newValue):
    with open(f"txtSrc/{filename}.txt", mode="w", encoding="utf-8") as file:
        file.write(newValue)
