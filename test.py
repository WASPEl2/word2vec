import pandas as pd

# Load the variable from the file
data = pd.read_csv("assets/files/spotify_taylorswift.csv", usecols=["name", "link"])

# Access the variable
print(data)
