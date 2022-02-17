#a bar chart histogram visulazing every 10 grade and number of their repitition
from matplotlib import pyplot as plt
grades = [83,95,91,87,70,0,85,82,100,67,73,77,0]
decile = lambda grade: grade // 10 * 10
decileL = [decile(grade) for grade in grades]
print(decileL)
histogram = [decileL.count(i) for i in decileL ]
print(histogram)
sett = set(zip(decileL, histogram))
sett = sorted(sett, key = lambda tup: tup[0]) #sort by zero number
print(sett)
plt.bar([x[0] for x in sett],[y[1] for y in sett],8 )
plt.axis([-5,105,0,5])
plt.xticks([10 * i for i in range(11)]) # x-axis labels at 0, 10, ..., 100
plt.xlabel("Decile")
plt.ylabel("# of Students")
plt.title("Distribution of Exam 1 Grades")

plt.show()
