
def  fileReader(address) : 
    finalList = []
   
    file = open(address)
    lines = file.readlines()
    for i in lines :
        finalList.append(i.split(','))
    file.close()
    return finalList
def  isLarge(num,criteria) :
    if(num>criteria) : 
        return 'Large'
    return 'Small'
def  GCPercentage(line) :
    return (100 * (line.count('G') + line.count('C'))/len(line))
def  averageCalculator(finalData, LOF) : #calculates the averaage of GC percentage due to the LOF(large or small)
    temp = 0
    count = 0
    for i in finalData : 
        if i[1] == LOF :
            temp = temp + i[2]
            count = count + 1
    return (temp/count)
def  csvExporter(data,address) :
    f = open(address,'w')
    string = ''
    
    for i in data :
        string = i[0] +','+ i[1]+',' + str(i[2]) + '\n'
        f.write(string)



data = fileReader('02-basic python 2/houseelf_earlength_dna_data.csv')
finalData = []
for i in data : 
    finalData.append([i[0], isLarge(float(i[1]),10), GCPercentage(i[2])])
print('Large ears GC average : ',averageCalculator(finalData,'Large'))
print('Small ears GC average : ',averageCalculator(finalData,'Small'))
csvExporter(finalData,'02-basic python 2/grangers_analysis.csv');
csvExporter(finalData,'02-basic python 2/grangers_analysis.txt')