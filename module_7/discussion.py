#%% 
import seaborn as sns
import pandas as pd

# Motorcycle data
data = {
    'Model': ['Model A', 'Model B', 'Model C', 'Model D'],
    'Engine Displacement (cc)': [600, 1000, 750, 1200],
    'Horsepower (hp)': [70, 120, 90, 140]
}

df = pd.DataFrame(data)

# Create a scatter plot using seaborn
sns.scatterplot(data=df, x='Engine Displacement (cc)', y='Horsepower (hp)', hue='Model', palette='viridis')

# %%
