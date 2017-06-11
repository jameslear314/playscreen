import FileTools

def parenMismatch(file):
    mismatches = []
    paragraph = ""
    line = ""
    blankLines = 0

    lines = file.readlines()
    for i in range(len(lines)):
        if lines[i] == "\n":
            if line != "\n":
                paragraph = paragraph + line
                if not checkQuotations(paragraph):
                    mismatches.append(paragraph)
            paragraph = line = lines[i]
        else:
            paragraph += line
            line = lines[i]

    return mismatches

def checkQuotations(paragraph):
    openQuote = 0
    closeQuote = 0
    quote = 0

    for i in range(len(paragraph)):
        char = paragraph[i]
        if char == '“':
            openQuote += 1
        elif char == '”':
            closeQuote += 1
        elif char == '"':
            quote += 1

    balanced =  openQuote + closeQuote + quote % 2 == 0 or \
               (openQuote == closeQuote and \
               quote % 2 == 0)

    return balanced

def PridePrejudiceLetters():
    name = FileTools.getOpenFileName()
    file = FileTools.openFile(name)
    mismatches = parenMismatch(file)
    return mismatches
    
