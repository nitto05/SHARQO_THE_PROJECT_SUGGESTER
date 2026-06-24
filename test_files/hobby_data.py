import os
import sys

tools_dir = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__),
        "..",
        "dataset"
    )
)

sys.path.insert(0, tools_dir)

import pandas as pd
from collections import Counter ##### why counter...
import matplotlib.pyplot as plt

df = pd.read_excel("HOBBIES (Responses).xlsx")

# hobbies_column = list(df["Hobbies"])

# print(list(df.columns))

# attributes = list(df.columns)[1:]
# print(attributes)

df = df.drop("Timestamp", axis = 1)
df = df.drop("Email Address", axis = 1)


# print(df.columns)

# df.rename (
#     columns = {
#         "1. Which of the following hobbies/interests do you actively pursue?" : "hobbies",
#         "2. How long have you been pursuing this hobby/interest?" : "experience",
#         "3. Have you ever created, built, organized, or contributed to something related to your hobby?" : "built",
#         ""
#     }
# )

df.columns = [
    "hobbies",
    "experience",
    "built",
    "what",
    "interested"
]

print(df.columns)

print(df["hobbies"][0]) 
## here it may look like hobbies has many attributes in itself.. 
#but no, it has all the selected answers all concatenated into a string separated by commas
h1 = df["hobbies"][0].split(", ")
print(h1)

set1 = set()

for i in range(0, len(df)):
    h = df["hobbies"][i].split(", ") # each row hobbies separated
    set_h = set(h)

    set1.update(set_h)
    # for j in range (0, len(h)):
    #     if (h[j] not in set1):
    #         set1.add()
print(set1)
ind = 0

dict1 = dict()
for i in range(0, len(df)):
    h = df["hobbies"][i].split(", ") # each row hobbies separated
    # set_h = set(h)

    for j in h:
        if (j not in dict1.keys()):
            dict1[j] = 1
        else : 
            dict1[j] += 1
    # set1.update(set_h)
    # for j in range (0, len(h)):
    #     if (h[j] not in set1):
    #         set1.add()

print(dict1)
dict1.pop("Kuch nhi")
dict1.pop("For 2nd qn I am answering for dance")

dict1 = dict(sorted(dict1.items(), key = lambda x : x[1], reverse = True))

labels = list(dict1.keys())
values = list(dict1.values())

plt.figure(figsize = (12,6))
plt.bar(labels, values)
plt.xlabel("Hobbies")
plt.ylabel("Number of Responses")
plt.title("Popularity of Hobbies")

plt.xticks(rotation = 90)
    
# plt.bar (labels, values)

plt.show()

