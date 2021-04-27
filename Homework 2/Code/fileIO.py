def read_input(inputFileName):
    inputFile = open(inputFileName, "r")
    lines = inputFile.readlines()
    A = []
    for line in lines:
        L = list(map(int, line.split()))
        if len(L) > 0:
            A.append(L)
    inputFile.close()
    return A


def write_output(outputFileName, ans):
    outputFile = open(outputFileName, "w")
    outputFile.write(str(ans) + '\n')
    outputFile.close()