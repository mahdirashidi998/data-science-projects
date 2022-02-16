data = [['A1', 28], ['A2', 32], ['A3', 1], ['A4', 0],
        ['A5', 10], ['A6', 22], ['A7', 30], ['A8', 19],
		['B1', 145], ['B2', 27], ['B3', 36], ['B4', 25],
		['B5', 9], ['B6', 38], ['B7', 21], ['B8', 12],
		['C1', 122], ['C2', 87], ['C3', 36], ['C4', 3],
		['D1', 0], ['D2', 5], ['D3', 55], ['D4', 62],
		['D5', 98], ['D6', 32]]
def  totalBirds(data) :
	tot = 0
	for i in data :
		tot = tot + i[1]
	return tot
def  averageBirds(data) :
	return totalBirds(data)/len(data)
def siteBirdNumWithChar(data,char) : 
	tot = 0
	for i in data :
		if i[0][0] == char :
			tot = tot + i[1]
	return tot;


print('number of sites : ',len(data))
print('7th site birds : ',data[6][1])
print('last site birds :', data[-1][1])
print('Number of all birds : ',totalBirds(data))
print('averageNumOfBirds : ',averageBirds(data))
print('birds number of sites starts with c : ', siteBirdNumWithChar(data,'C'))


