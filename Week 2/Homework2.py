import re
import pandas as pd
from pathlib import Path
from plotnine import ggplot, aes, geom_bar, labs, theme_minimal, position_dodge, coord_flip

def Question_1():
    # Load the dataset
    file_path = "/Users/peytonhall/Desktop/DATA 499/Week 2/COVID-19-Vaccine.xlsx"
    df = pd.read_excel(file_path)

    # a) Keep only three columns
    df_selected = df[["ProductCategory", "StageDevelopment", "ProductDescription"]]

    # b) Find the number of vaccines by stage of development
    stage_counts = df_selected["StageDevelopment"].value_counts().reset_index()
    stage_counts.columns = ["StageDevelopment", "Count"]
    print("Number of vaccines by stage of development:")
    print(stage_counts)

    # c) Plot using ggplot
    plot = (
        ggplot(stage_counts, aes(x="StageDevelopment", y="Count"))
        + geom_bar(stat="identity", fill="skyblue")
        + labs(title="Number of Vaccines by Stage of Development",
               x="Stage of Development",
               y="Number of Vaccines")
        + theme_minimal()
    )

    print(plot)
    return stage_counts, plot

def Question_2():
    # Load the vaccine development data (adjust path if needed)
    file_path = "/Users/peytonhall/Desktop/DATA 499/Week 2/COVID-19-Vaccine.xlsx"
    df = pd.read_excel(file_path)

    # a) Keep only the specified product categories
    keep_categories = [
        "DNA-based",
        "Inactivated virus",
        "Protein subunit",
        "RNA-based vaccine",
        "Virus-like particle"
    ]
    df_keep = (
        df[df["ProductCategory"].isin(keep_categories)]
        [["ProductCategory", "StageDevelopment", "ProductDescription"]]
        .copy()
    )

    # b) Counts by stage of development AND product category
    counts = (
        df_keep
        .groupby(["StageDevelopment", "ProductCategory"])
        .size()
        .reset_index(name = "Count")
    )

    # optional: order stages nicely if present
    stage_order = ["Pre-clinical", "Phase I", "Phase I/II", "Phase II", "Phase II/III", "Phase III", "Authorized", "Approved"]
    counts["StageDevelopment"] = pd.Categorical(
        counts['StageDevelopment'],
        categories=[s for s in stage_order if s in counts["StageDevelopment"].unique()],
        ordered=True
    )
    counts = counts.sort_values(["StageDevelopment", "ProductCategory"]).reset_index(drop=True)

    print("Counts by StageDevelopment and ProductCategory:")
    print(counts)

    # c) Plot the counts (grouped bars by stage, grouped by product category)
    p = (
        ggplot(counts, aes(x = 'StageDevelopment', y = 'Count', fill = "ProductCategory"))
        + geom_bar(stat='identity', position=position_dodge(width = 0.8))
        + labs(
            title="Vaccines by Stage of Development and Product Category",
            x="Stage of Development",
            y="Number of Vaccines"
        )
        + theme_minimal()
        + coord_flip()  # flip for readable labels; remove if you prefer vertical bars
    )

    print(p)
    # save a copy for submission
    p.save("q2_vaccines_by_stage_and_category.png", dpi = 150, verbose = False)
    print("Saved plot to q2_vaccines_by_stage_and_category.png")

    return df_keep, counts, p

def Question_3():
    """
    Scrape store names and last-updated dates from the UPCItemDB page.
    Saves q3_store_updates.csv and returns the DataFrame.
    """
    import requests
    from bs4 import BeautifulSoup

    url = "https://www.upcitemdb.com/upc/888633483151"
    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
            "AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Safari/605.1.15"
        )
    }
    r = requests.get(url, headers = headers, timeout = 30)
    r.raise_for_status()

    soup = BeautifulSoup(r.text, "lxml")

    # grab all HTML tables and try them
    target_df = None
    for tbl in soup.find_all("table"):
        try:
            df_try = pd.read_html(str(tbl), flavor = "lxml")[0]
        except Exception:
            continue

        # normalize header text
        df_try.columns = [re.sub(r"\s+", " ", str(c)).strip() for c in df_try.columns]

        headers_lower = [c.lower() for c in df_try.columns]

        # need one column that looks like a store/seller name
        store_candidates = [c for c in df_try.columns
                            if re.search(r"(store|seller|merchant|retailer)", c, re.I)]
        # need one column that looks like "updated"
        updated_candidates = [c for c in df_try.columns
                              if re.search(r"updated", c, re.I)]

        if store_candidates and updated_candidates:
            target_df = df_try
            store_col = store_candidates[0]
            updated_col = updated_candidates[0]
            break

    if target_df is None:
        raise RuntimeError("Could not find a table with store/seller and updated columns.")

    # Reduce to the two fields and clean
    result = (
        target_df[[store_col, updated_col]]
        .rename(columns={store_col: "Store", updated_col: "Last Updated"})
        .copy()
    )
    result["Store"] = result["Store"].astype(str).str.strip()
    result["Last Updated"] = result["Last Updated"].astype(str).str.replace(r"\s+", " ", regex=True).str.strip()

    # drop empty rows
    result = result[(result["Store"] != "") & (result["Last Updated"] != "")]
    result = result.reset_index(drop=True)

    # save for submission
    out = Path("q3_store_updates.csv")
    result.to_csv(out, index = False)
    print(f"Saved {out.resolve()}")
    print(result.head(10))

    return result

if __name__ == "__main__":
    Question_1()
    Question_2()
    Question_3()
