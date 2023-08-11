import csv

# Check my interpreter works
# print("Hello World!")

# Import .csv from same folder this script is in
path = "./car_.csv"
file = open(path, newline="")
reader = csv.reader(file)

# Separate Header from rows (only needed sometimes)
header = next(reader)

## need to convert reader output to correct format
list_of_strings = []
for i in reader:
    counter = i[0]
    output = (
        "{"
        + f'"value": "{counter}", "synonyms": ["{counter}"], "languageCode": "en"'
        + "},"
    )
    list_of_strings.append(output)

# print(list_of_strings)

# This is a list of list, need to change into a .txt file to be able to copy and paste in one
conv_string = ""
for i in list_of_strings:
    add_to = str(i)
    entity = f"{add_to}"
    conv_string = conv_string + entity + "\n"
    # print(conv_string)

# To keep things tidy
final = conv_string

with open("./cars_final.txt", "w") as f:
    f.write(final)
