import sys
import os

folderpath="C:\\PSG\\0 standford - edit\\docunmentation\\"
filename="Flow Events.txt"
filepath=folderpath+filename

with open(filepath) as fp:
    line=fp.read().splitlines() #splitlines removes \n end of the line
    #print("the whole file of txt is")
    #print(line[1][-8:]) #second line initial time
    initialTime = line[1][-8:].split(":")  # first element in first splitted data is the initial time,
    #print(initialTime)
    initialTime = int(initialTime[2]) + int(initialTime[1]) * 60 + int(initialTime[0]) * 60 * 60
    #print(initialTime)

    del line[0:5]  #only in this file, others has to be reassessed
    #print(line)
    splitted = []

    # split string into time and stage
    for element in line:
        #print(element)
        splitted.append(element.replace("-",";").split(";"))
        #split line into [start, end, duration, type], since the start-end is seperated with -, replace - with ;, then split
        #print(element.split("; "))
    #print(splitted)

    # change times into start time in seconds
    for element in splitted:
        # split time into HH,MM,SS
        element[0] = element[0][0:8].split(":")
        element[1] = element[1][0:8].split(":")
        element[2] = int(element[2])
        # make time into 24-36h format, with 1am=25:00 for calculation purposes
        if int(element[0][0]) < 13:
            element[0][0] = int(element[0][0]) + 24
        if int(element[1][0]) < 13:
            element[1][0] = int(element[1][0]) + 24

        # covert into seconds
        element[0] = int(element[0][2]) + int(element[0][1]) * 60 + int(element[0][0]) * 60 * 60
        element[1] = int(element[1][2]) + int(element[1][1]) * 60 + int(element[1][0]) * 60 * 60

    # previous loop is looping elements in splitted

    #linear transform against initialTime, for both start and the end time
    for element in splitted:
        element[0] = element[0] - initialTime
        element[1] = element[1] - initialTime

    #print(splitted)

    XMLlist=[]
    #result <Event Family="Respiratory" Type="ObstructiveApnea" Start="37.5" Duration="6.5" Machine="true">
    #need to add all the inside useless tags, may assign number as 0
    for element in splitted:
        XMLlist.append("<Event Family=\"User\" Type=\"Comment\" Start=\""+ str(element[0]) +"\" Duration=\"0\">")
        XMLlist.append("   <Comment>Stanford: " + str(element[1]) + "</Comment>")
        XMLlist.append("</Event>")