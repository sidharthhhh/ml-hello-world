# visualize.py
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
import pandas as pd

# 1. SETUP DATA
# Load the raw data again
iris = load_iris()
# Convert to a Table (DataFrame) for easier handling
df = pd.DataFrame(iris.data, columns=iris.feature_names)
# Add the species names (0,1,2 -> 'setosa', etc.)
df['species'] = iris.target_names[iris.target]

# 2. CREATE PLOT
# Create a figure (canvas)
plt.figure(figsize=(10, 6))

# Define colors for the 3 species
colors = ['red', 'green', 'blue']
species_names = ['setosa', 'versicolor', 'virginica']

# Loop through each species and plot its dots
for i in range(3):
    species_name = species_names[i]
    # Filter: Get only the rows for this specific flower
    subset = df[df['species'] == species_name]
    
    # Plot: X=Petal Length, Y=Petal Width
    plt.scatter(
        subset['petal length (cm)'], 
        subset['petal width (cm)'], 
        c=colors[i], 
        label=species_name,
        alpha=0.7 # Transparency
    )

# 3. LABELING
plt.title('Iris Data: Petal Length vs Width')
plt.xlabel('Petal Length (cm)')
plt.ylabel('Petal Width (cm)')
plt.legend() # Show the color key
plt.grid(True) # Add grid lines

# 4. SAVE TO DISK
output_file = 'iris_plot.png'
plt.savefig(output_file)
print(f"✅ Visualization saved as: {output_file}")