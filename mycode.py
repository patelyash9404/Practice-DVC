import pandas as pd
import os

data = {
    'name': ['Alice', 'Bob', 'Charlie'],
    'age': [25, 30, 35],
    'city': ['New York', 'Los Angeles', 'Chicago']
}

df = pd.DataFrame(data)
# # Adding new row to df for V2
new_row_loc = {'name': 'GF1', 'age': 20, 'city': 'City1'}
df.loc[len(df.index)] = new_row_loc

new_row_loc = {'name': 'GF2', 'age': 20, 'city': 'City1'}
df.loc[len(df.index)] = new_row_loc
# Absolute path of this file
CURRENT_FILE_DIR = os.path.dirname(os.path.abspath(__file__))

# Practice-DVC root directory
PROJECT_ROOT = CURRENT_FILE_DIR  # because mycode.py is inside Practice-DVC

# Correct data folder inside Practice-DVC
data_dir = os.path.join(PROJECT_ROOT, "data")
os.makedirs(data_dir, exist_ok=True)

file_path = os.path.join(data_dir, "sample_data.csv")

df.to_csv(file_path, index=False)

print(f"CSV file saved to: {file_path}")