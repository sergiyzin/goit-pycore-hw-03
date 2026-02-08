import re
import math

text = "Temperatures: 18.5, 20.1, 22.3, 24.5, 24.8, 23.0, 19.5"


#1, get all temps
pattern = r"\d{2}\.\d{1}"
matches = re.findall(pattern, text)
print(matches)

#2, set to floan(numeric)
float_numbers = [float(match) for match in matches]
print(float_numbers)

average = math.fsum(float_numbers) / len(float_numbers)
minimum = min(float_numbers)
maximum = max(float_numbers)


print("Average termperature is", average)
print("Minimum termperature is", minimum)
print("Maximum termperature is", maximum)
print("Round up termperature is", math.ceil(average))
print("Round down termperature is", math.floor(average))