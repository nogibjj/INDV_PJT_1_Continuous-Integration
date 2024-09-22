import pandas as pd
import matplotlib.pyplot as plt

# Load dataset using Pandas
ppl = pd.read_csv("HR.csv", encoding="utf-8")

# Explore data
full_desc = ppl.describe().T
print(full_desc)

# Calculate statistics for Age
age_mean = ppl["Age"].mean()
age_median = ppl["Age"].median()
age_std = ppl["Age"].std()

# Plot histogram for Age
plt.figure(figsize=(8, 6))
plt.hist(ppl["Age"], bins=10, edgecolor="black")
plt.title("Average age of employees")
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.show()

# Print descriptive statistics
print(f"Average age of employees is {round(age_mean, 1)}")
print(f"Median age of employees is {age_median}")
print(f"Standard Deviation age of employees is {age_std}")

# Employee Attrition rate
attrition_counts = ppl["Attrition"].value_counts()
plt.pie(
    attrition_counts,
    labels=attrition_counts.index,
    autopct="%1.1f%%",
    startangle=90,
)
plt.title("Employee Attrition")
plt.show()

# Employee Attrition by departments
def generate_frequency_graph(col_name):
    temp_grp = ppl.groupby([col_name, "Attrition"]).size().unstack(fill_value=0)
    temp_grp.columns = ["Attrition_No", "Attrition_Yes"]
    temp_grp["Percentage Attrition"] = (
        temp_grp["Attrition_Yes"]
        / (temp_grp["Attrition_Yes"] + temp_grp["Attrition_No"])
    ) * 100
    print(temp_grp)

    temp_grp[["Attrition_No", "Attrition_Yes"]].plot(
        kind="bar",
        stacked=False,
    )
    plt.xlabel(col_name)
    plt.ylabel("Count")
    plt.title(f"Attrition by {col_name}")
    plt.show()


generate_frequency_graph("Department")
