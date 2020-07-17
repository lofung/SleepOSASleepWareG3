import sys
import os

folderpath="C:\\PSG\\0 standford - edit\\docunmentation\\"
filename="Position.txt"
filepath=folderpath+filename

with open(filepath) as fp:
    line=fp.read().splitlines() #splitlines removes \n end of the line
    #print("the whole file of txt is")

    del line[0:6]  #only in this file, others has to be reassessed
    #print(line)
    splitted = []

    # split string into time and stage
    for element in line:
        #print(element)
        splitted.append(element.split("; "))
        #print(element.split("; "))

    # change times into start time in seconds
    for element in splitted:
        #split time into HH,MM,SS
        element[0]=element[0][0:8].split(":")
        #make time into 24-36h format, with 1am=25:00 for calculation purposes
        if int(element[0][0])<13:
            element[0][0]=int(element[0][0])+24
        #covert into seconds
        element[0]=int(element[0][2])+int(element[0][1])*60+int(element[0][0])*60*60

    initialTime=splitted[0][0] #first element in first splitted data is the initial time,
        #previous loop is looping elements in splitted

    for element in splitted:
        element[0]=element[0]-initialTime

    #print(splitted)

    XMLlist=[]
    #result <BodyPositionItem Position="Right" Start="4676" />
    for element in splitted:
        XMLlist.append("<BodyPositionItem Position=\"" + element[1] +"\" Start=\""+ str(element[0]) +"\" />")

    #print(XMLlist)
    #save at output
with open(folderpath+"outputPosition.txt", 'w') as f:
    for item in XMLlist:
        f.write("%s\n" % item)