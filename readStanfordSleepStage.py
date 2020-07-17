import sys
import os

folderpath="C:\\PSG\\0 standford - edit\\docunmentation\\"
filename="Sleep profile.txt"
filepath=folderpath+filename

with open(filepath) as fp:
    line=fp.read().splitlines() #splitlines removes \n end of the line
    #print("the whole file of txt is")

    del line[0:7]  #only in this file, others has to be reassessed
    #print(line)
    splitted = []
    montageCount=0

    # split string into time and stage
    for element in line:
        #print(element)
        splitted.append(element.split("; "))
        #print(element.split("; "))

    # change times into start time in seconds
    for element in splitted:
        element[0]=montageCount*30
        montageCount = montageCount + 1
        #cut time minus
        #print(element[0])
    #print(splitted)

    splitted2 = []
    splitted2.append(splitted[0]) #put first element into splitted2
    n=1
    #print(len(splitted))

    #if the sleep stage is the same as the previous, then do not append the stage, otherwise do.
    while n<len(splitted):
        if splitted[n][1]!=splitted2[-1][1]:
            splitted2.append(splitted[n])
        n=n+1
    #result is that we have a list of time when the sleep phase changes

    #change sleep stages into sleepwareG3 compilable names
    n=0
    while n<len(splitted2):
        if splitted2[n][1]=='N1':
            splitted2[n][1]="NonREM1"
        if splitted2[n][1]=='N2':
            splitted2[n][1]="NonREM2"
        if splitted[ n][1]=='N3':
            splitted[n][1]="NonREM3"
        n=n+1
    #print(splitted)
    #print(splitted2)

    #generate <XML> tags for the sleep stage
    # <Stage Type="NonREM1" Start="24330" />
    XMLlist=[]
    for record in splitted2:
        XMLlist.append("<Stage Type=\""+str(record[1])+"\" Start=\""+str(record[0])+"\" />")

    #print(XMLlist)

    #save at output
with open(folderpath+"outputSleepStage.txt", 'w') as f:
    for item in XMLlist:
        f.write("%s\n" % item)