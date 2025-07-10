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