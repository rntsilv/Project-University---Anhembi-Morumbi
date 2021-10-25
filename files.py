def openEncoded(filename, mode="r"):
    return open(f"txtSrc/{filename}.txt", mode=mode, encoding="utf-8")


def getFileLines(filename):
    file = openEncoded(filename)
    lines = file.readlines()
    file.close()

    return lines


def getFileContent(filename):
    file = openEncoded(filename)
    content = file.read()
    file.close()

    return content


def printFile(filename):
    for line in getFileContents(filename):
        print(line, end="")


def inputFile(filename, newValue):
    with open(f"txtSrc/{filename}.txt", mode="w", encoding="utf-8") as file:
        file.write(newValue)
