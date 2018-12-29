import pandas as pd
import matplotlib.pyplot as plt

#Accessing and treating data
data = pd.read_csv("data.csv")
grouped = data.groupby('purpose')['int_rate'].mean()

#Creating plot from grouped data
grouped.plot.bar()

#Adding labels
plt.title('Mean interest rate by loan purpose')
plt.ylabel('Mean Interest rate (%)')
plt.xlabel('Loan purpose')

#Adjusting chart spacing
plt.subplots_adjust(bottom=0.35)

#Displaying plot
plt.show()