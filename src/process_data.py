import pandas as pd
from refiner import Refinery

# Load the raw data
df = pd.read_csv('data/raw_data.csv')

# Initialize the refinery
refinery = Refinery()

# Apply refiner to the dataframe (it will handle missing values)
# We'll use the default recipe which includes imputation for numeric columns
refined_df = refinery.refine(df)

# Save the refined data
refined_df.to_csv('data/refined_data.csv', index=False)

print("Refinement complete. Saved to data/refined_data.csv")