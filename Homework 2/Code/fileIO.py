def read_input(inputFileName):
    inputFile = open(inputFileName)
    lines = inputFile.readlines()
    A = []
    for line in lines:
        A.append(map(int, line.split()))
    inputFile.close()
    return A


def write_output(outputFileName, ans):
    outputFile = open(outputFileName)
    outputFile.write(ans)
    outputFile.close()