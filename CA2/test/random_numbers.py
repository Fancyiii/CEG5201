import json
import random

lsize = [64, 128, 256, 512, 1024, 2048, 4096, 8192]

# Create 10 groups of 8 sets of random integers (arrays)
data = [[random.choices(range(256), k=ele) for ele in lsize] for _ in range(10)]

# Save the data to a JSON file
with open('integer_data.json', 'w') as file:
    json.dump(data, file)
