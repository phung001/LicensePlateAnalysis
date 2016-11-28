#open files for reading
inFile = open("inFile.txt", "r")
inFile2 = open("stolen.txt", "r")

#initialize dictionary
D = {}

for line in inFile:
    #find lines with 7 characters for the license plates and store into dictionary
        #dictionary holds total percentage and total occurences
    if line[4] == '-':
        temp = line.split(" ")
        if len(temp[5]) == 8:
            #first instance of characters
            if D.get(temp[5]) == None:
                D[temp[5]] = [float(temp[7][:5]), 1]
            #every other instance found characters
            else:
                x = D[temp[5]]
                D[temp[5]][0] = x[0] + float(temp[7][:5])
                D[temp[5]][1] = x[1] + 1
        
#calculate the average percentage of each
finalList = []
for i in D.keys():
    finalList.append( [i, D[i][0]/D[i][1]] )


highOcc = 0
highPlates = '0'
highest = 0
j = 0
#find the highest occured plate
for i in D.keys():
    j = j+1
    if highOcc < D[i][1]:
        highOcc = D[i][1]
        highPlates = i
        highest = finalList[j][1]
    #if highest occured is the same, choose the highest average percentage
    elif highOcc == D[i][1]:
        if(finalList[j][1] > highest):
            highOcc = D[i][1]
            highPlates = i
            highest = finalList[j][1]

#look through the database and print if stolen plate is found
done = 0
for line in inFile2:
    if line[:7] == highPlates[:7]:
        print "STOLEN PLATE: " + highPlates[:7]
        done = 1
        break

if done == 0:
    print "NO STOLEN PLATE FOUND"

inFile.close()
inFile2.close()
