#a simple bar chart drawing using python
from matplotlib import pyplot as plt
movies = ["Annie Hall", "Ben-Hur", "Casablanca", "Gandhi", "West Side Story"]
num_oscars = [5, 11, 3, 8, 10]plt.bar(movies,num_oscars)plt.title('oscarWinners')plt.ylabel('numberOfOscars')plt.show()