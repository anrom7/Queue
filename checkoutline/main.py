
from marketmodel import MarketModel

print("Welcome the Market Simulator")
lengthOfSimulation = int(input("Enter the total running time: "))
averageTimePerCus = int(input("Enter the average time per customer: "))
probabilityOfNewArrival = float(input("Enter the probability of a new arrival: "))

model = MarketModel(lengthOfSimulation, averageTimePerCus, probabilityOfNewArrival)

model.runSimulation()
print(model)
