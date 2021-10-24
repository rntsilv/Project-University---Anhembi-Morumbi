def openEncoded(filename, mode="r"):
    return open(filename, mode=mode, encoding="utf-8")


def getFileContents(filename):
    file = openEncoded(filename)
    contents = file.readlines()
    file.close()

    return contents


def printFile(filename):
    for line in getFileContents(filename):
        print(line)
