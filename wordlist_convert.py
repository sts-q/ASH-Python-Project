import csv

infile  = "wordlist_1000_1.csv"
outfile = "wordlist_1000_ash.csv"

def printHeadline ():  
    print ("----------------------------------------------------------------------------") 
    print (f"{'de':26} {'en':26} {'importance':10} {' fun':5} {'score':4}")
    pass

def printLine (l):
    print (f"{l[0]:26} {l[1]:26} {l[2]:10d} {l[3]:4d} {l[4]:6d}")

def printLines(ls):
    printHeadline()
    for l in ls:
        printLine (l)
    printHeadline()

# convert a wordlist from external to ASHcards format
def import_wordlist():
    print ()
    print ("============  wordlist_convert")
    print ("reading from: " + infile)
    print ("writing to:   " + outfile)
    newLines = []
    # read lines from infile, delimiter is tab character '\t'
    # append integers for: importance, fun-factor, score
    # as we want to have in ASHcards
    with open (infile) as fdin:
        csvReader = csv.reader (fdin, delimiter='\t')
        for row in csvReader:
            newLines.append ([row[0], row[1], 0,0,0])

    # print what we have so far
    # printLines (newLines)
    
    # write data back to a new csv-file
    with open (outfile, "w") as fdout:
        csvWriter = csv.writer (fdout, delimiter = ';' )
        for l in newLines:
            csvWriter.writerow (l)
        
    print (f"{len (newLines):8d} lines found")

    print ("============  done")
    print ()

def main():
    import_wordlist()
    pass


if __name__ == "__main__":
    main()



