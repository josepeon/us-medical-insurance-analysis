import csv
import os
# This script reads a CSV file containing U.S. medical insurance data and prints each row.
# It also creates a README file with project details if it doesn't already exist.
with open('/Users/josepeon/Documents/ZEROZERO/AI Engineer Path/US Medical Insurance/python-portfolio-project-starter-files/insurance.csv', 'r') as insurances:
    reader = csv.reader(insurances)
    for row in reader:
        print(row)
with open('/Users/josepeon/Documents/ZEROZERO/AI Engineer Path/US Medical Insurance/python-portfolio-project-starter-files/README.md', 'w') as readme:
    readme.write("""# U.S. Medical Insurance Cost Analysis

This project explores a dataset of U.S. medical insurance costs to uncover basic insights using Python. The dataset includes demographic and personal health information such as age, BMI, smoking status, and number of children.

## 🥅 Project Goals
- Understand trends in medical insurance charges
- Explore potential correlations (e.g. smoking and cost)
- Practice data cleaning, transformation, and analysis

## 📊 Dataset
- Source: Codecademy’s "U.S. Medical Insurance" CSV file
- Columns include: `age`, `sex`, `bmi`, `children`, `smoker`, `region`, `charges`

## 🔍 Analysis Questions
- What is the average age of the patients?
- What regions are most represented?
- How do charges compare between smokers and non-smokers?
- What is the average age of individuals with at least one child?

## 🛠 Tools Used
- Python 3
- CSV module
- VS Code
- Git & GitHub

## 🚧 Status
Project in progress. Next step: exploring analysis functions and saving column data as variables.

---

Contributions or suggestions welcome!
""")

# Check if README.md exists, if not create it
if not os.path.exists('README.md'):
    with open('README.md', 'w') as readme:
        readme.write(""" ... """)
else:
    print("README.md already exists. Not overwriting.")

# Initialize lists to store column data
# These lists will be used to store the data from the CSV file for further analysis.
ages = []
sexes = []
bmis = []
children = []
smokers = []
regions = []
charges = []

# Read the CSV file again to populate the lists
with open('python-portfolio-project-starter-files/insurance.csv', 'r') as insurances:
    reader = csv.DictReader(insurances)
    for row in reader:
        ages.append(int(row['age']))
        sexes.append(row['sex'])
        bmis.append(float(row['bmi']))
        children.append(int(row['children']))
        smokers.append(row['smoker'])
        regions.append(row['region'])
        charges.append(float(row['charges']))
# Print the first few entries of each list to verify data loading
print("Age:", ages[:5])
print("Sex:", sexes[:5])
print("BMI:", bmis[:5])
print("Children:", children[:5])
print("Smoker:", smokers[:5])
print("Region:", regions[:5])
print("Charges:", charges[:5])          

# Calculate the average age using the function
age_average = 0
def average_age(ages):
    ages_sum = 0
    ages_count = len(ages)
    for age in ages:
        ages_sum += age
    if ages_count > 0:
        return ages_sum / ages_count  
    else: 0

age_average = average_age(ages)
print(age_average, .2)
