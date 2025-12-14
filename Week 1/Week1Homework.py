import pandas as pd
import matplotlib.pyplot as plt

def question_1():
    # Read the dataset (file is in the same folder as this script)
    df = pd.read_excel("Seattle Bikes.xlsx")

    # (a) Rename columns
    df = df.rename(columns={
        "Date": "Date",
        "Fremont Bridge Total": "Total",
        "Fremont Bridge East Sidewalk": "East",
        "Fremont Bridge West Sidewalk": "West"
    })

    # (b) Average counts by year
    df["Date"] = pd.to_datetime(df["Date"])
    df["Year"] = pd.DatetimeIndex(df["Date"]).year
    avg_counts = df.groupby("Year")[["Total", "East", "West"]].mean()

    print("Average counts by year:")
    print(avg_counts)

    # (c) Plot
    avg_counts.plot(kind="bar", figsize=(10, 6))
    plt.title("Average Bicycle Counts by Year")
    plt.ylabel("Average Count")
    plt.xlabel("Year")
    plt.legend(title="Counts")
    plt.tight_layout()
    plt.show()

    return avg_counts

def question_2():
    # Read the dataset (Excel) from the current folder
    df = pd.read_excel("BreastCancer.xlsx")

    # Ensure numeric types (usually already numeric)
    df["Year"] = pd.to_numeric(df["Year"])
    df["BC Rate"] = pd.to_numeric(df["BC Rate"])

    # (a) Average BC rate for each country
    avg_by_country = df.groupby("Country")["BC Rate"].mean()
    print("Average BC Rate by country:")
    print(avg_by_country)

    # (b) Average BC rate for each year
    avg_by_year = df.groupby("Year")["BC Rate"].mean()
    print("\nAverage BC Rate by year:")
    print(avg_by_year)

    # (c) Plot USA rates from 2000 to 2012
    usa = df[(df["Country"] == "USA") & (df["Year"].between(2000, 2012))].sort_values("Year")
    plt.plot(usa["Year"], usa["BC Rate"], marker="o")
    plt.title("Breast Cancer Rates in USA (2000–2012)")
    plt.xlabel("Year")
    plt.ylabel("BC Rate")
    plt.grid(True)
    plt.tight_layout()
    plt.show()

    return avg_by_country, avg_by_year, usa

def question_3():
    # (a) Create the first DataFrame
    df1 = pd.DataFrame({
        "Name": ["Jack", "Mary", "Kate", "Tom"],
        "Gender": ["M", "F", "F", "M"],
        "Midterm": [80, 76, 71, 91],
        "Final": [85, 62, 83, 90],
        "Birth Date": ["1992-7-8", "1990-3-6", "1992-1-5", "1994-2-7"]
    })

    print("DataFrame a):")
    print(df1, "\n")

    # (b) Create the second DataFrame
    df2 = pd.DataFrame({
        "Name": ["Kevin", "David"],
        "Gender": ["M", "M"],
        "Midterm": [95, 98],
        "Final": [93, 99],
        "Birth Date": ["1991-9-5", "1981-7-3"]
    })

    print("DataFrame b):")
    print(df2, "\n")

    # Append df2 to df1
    df_combined = pd.concat([df1, df2], ignore_index=True)

    print("Combined DataFrame:")
    print(df_combined)

    return df1, df2, df_combined

# Run it
results = question_1()
results = question_2()
results = question_3()

