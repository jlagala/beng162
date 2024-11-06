import matplotlib.pyplot as plt

# Your data
values = [137,138,123,124,21,41,79,131,204,241,11,73,194,146,143,144,136,244,107,235,147]
occurences = []
for i in values:
    occurences.append(1)

# Create the histogram with orange bars
plt.bar(values, occurences, width=2, color='orange', alpha=0.7)

# Adding vertical red lines at 112 and 131
plt.axvline(x=112, color='red', linestyle='--', linewidth=2)
plt.axvline(x=131, color='red', linestyle='--', linewidth=2)

#green lines
plt.axvline(x=132, color="green", linestyle="--", linewidth=2)
plt.axvline(x=150,color="green",linestyle="--",linewidth=2)

# Adding labels and title
plt.xlabel('Locus/BP')
plt.ylabel('# of Mutations')

# Add a legend
plt.legend()

# Show the plot
plt.axis(ymax = 5)
plt.show()
