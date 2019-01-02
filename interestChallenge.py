import pandas as pd
import matplotlib.pyplot as plt

#Accessing and treating data
data = pd.read_csv("data.csv")
grouped = data.groupby('purpose')['int_rate'].mean().sort_values(ascending=False)

#Printing grouped data to console
print(grouped)

#Creating plot from grouped data
grouped.plot.bar(rot=90)

#Adding labels
plt.gcf().canvas.set_window_title('Mean interest rate by loan purpose')
plt.title('Mean interest rate by loan purpose')
plt.ylabel('Mean Interest rate (%)')
plt.xlabel('Loan purpose')


#Adjusting chart spacing
plt.tight_layout()

#Displaying plot
plt.show()
