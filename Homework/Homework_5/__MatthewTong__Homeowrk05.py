import numpy as np

# csv file path
file_path = "vgsales-2.csv"

# loadtxt() loads the csv file as string
year_sorted_data = np.loadtxt(file_path, delimiter=",", dtype=str, usecols = (0, 1, 4), skiprows=1, encoding='utf-8')

# Show the data sorted by year
print(year_sorted_data)