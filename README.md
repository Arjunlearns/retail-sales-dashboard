# 📊 Retail Sales Analytics Dashboard

An end-to-end retail sales data analysis project using **Python, Pandas, Plotly, and Streamlit**. This project explores the UCI Online Retail dataset, identifies sales trends and top-performing products and countries, and presents the findings through an interactive web dashboard.

## 🔗 Project Links

- **Live Dashboard:** [View the Interactive Dashboard](https://arjun-retail-sales-dashboard.streamlit.app/)
- **GitHub Repository:** [View Source Code](https://github.com/Arjunlearns/retail-sales-dashboard)
- **Dataset:** [UCI Online Retail Dataset](https://archive.ics.uci.edu/dataset/352/online+retail)

## 📌 Project Overview

The goal of this project was to analyze historical online retail transactions to understand sales performance, identify business trends, and extract useful insights from transactional data.

The project began with exploratory data analysis and data cleaning in Google Colab. The analysis was then developed into an interactive Streamlit dashboard that allows users to explore key performance indicators and sales patterns.

The dataset contains transactions from **December 2010 to December 2011**, including invoice numbers, product descriptions, quantities, invoice dates, unit prices, customer identifiers, and countries.

## 🎯 Objectives

- Inspect and understand the structure and quality of the dataset.
- Identify missing values, duplicate records, cancelled invoices, and invalid transactions.
- Clean the data before performing analysis.
- Calculate revenue and key sales performance indicators.
- Analyze monthly sales trends.
- Identify top-performing products, countries, and customers.
- Build an interactive dashboard to communicate findings visually.
- Deploy the dashboard online so it can be accessed without running the notebook locally.

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python | Data processing and analysis |
| Google Colab | Exploratory data analysis and experimentation |
| Pandas | Data cleaning, transformation, grouping, and aggregation |
| Matplotlib / Seaborn | Exploratory visualizations, where used in the notebook |
| Plotly | Interactive dashboard charts |
| Streamlit | Dashboard development |
| Git and GitHub | Version control and source-code hosting |
| Streamlit Community Cloud | Dashboard deployment |

## 📂 Dataset

**Source:** UCI Machine Learning Repository — Online Retail

The dataset contains **541,909 transaction records** and 8 columns.

Important columns include:

- `InvoiceNo` — invoice identifier; invoice numbers beginning with `C` indicate cancellations.
- `StockCode` — product identifier.
- `Description` — product description.
- `Quantity` — quantity purchased in a transaction.
- `InvoiceDate` — date and time of the transaction.
- `UnitPrice` — price per unit in pounds sterling.
- `CustomerID` — customer identifier.
- `Country` — country associated with the transaction.

## 🔍 Data Analysis Workflow

### 1. Data loading and inspection

I loaded the original Excel dataset into a Pandas DataFrame in Google Colab and examined its structure using methods such as:

- `head()` to inspect sample records.
- `shape` to understand the dataset dimensions.
- `info()` to inspect column data types and non-null values.
- `isnull().sum()` to identify missing values.
- `duplicated().sum()` to identify duplicate records.
- `describe()` to inspect numerical distributions.

This initial inspection revealed data-quality issues that needed to be addressed before calculating sales metrics.

### 2. Data quality assessment

The initial dataset inspection identified:

| Data quality issue | Records identified |
|---|---:|
| Missing product descriptions | 1,454 |
| Missing customer IDs | 135,080 |
| Duplicate rows | 5,268 |
| Negative quantities | 10,624 |
| Negative unit prices | 2 |
| Zero unit prices | 2,515 |

These checks helped determine which records required cleaning and which transactions should be excluded from the positive-sales analysis.

### 3. Data cleaning and preparation

I created a separate working DataFrame to preserve the original data and applied the following transformations:

- Removed exact duplicate records.
- Replaced missing product descriptions with `"Unknown"`.
- Excluded cancelled invoices identified by invoice numbers beginning with `C`.
- Excluded transactions with zero or negative quantities.
- Excluded transactions with zero or negative unit prices.
- Converted invoice dates to datetime format.
- Created a revenue column by multiplying quantity by unit price.
- Extracted the year-month period for monthly sales analysis.

The key revenue calculation was:

`Revenue = Quantity × UnitPrice`

The main cleaning operations were implemented using Pandas filtering, string operations, missing-value handling, duplicate removal, and datetime functionality.

### 4. Cleaning results

| Stage | Number of rows |
|---|---:|
| Original dataset | 541,909 |
| After removing duplicates | 536,641 |
| After filtering to positive-sales transactions | 524,878 |

The cleaned dataset was then used for the subsequent sales analysis.

### 5. Exploratory data analysis in Google Colab

I used Pandas grouping and aggregation to investigate several business questions:

**Monthly sales trends**

Grouped transactions by month and calculated total revenue to identify changes in sales over time.

**Top products**

Aggregated revenue by product description to identify products or transaction descriptions generating the highest recorded revenue.

**Country-level sales**

Grouped transactions by country to understand the geographic distribution of revenue.

**Customer analysis**

Grouped transactions by customer ID to identify customers associated with the highest recorded revenue. This analysis included only transactions with an identified customer ID.

I also created charts to make these patterns easier to interpret.

## 📈 Key Performance Indicators

The final positive-sales dataset produced the following results:

| Metric | Result |
|---|---:|
| Positive sales revenue | £10,642,110.80 |
| Units sold | 5,572,420 |
| Unique invoices | 19,960 |
| Unique products | 3,922 |
| Identified customers | 4,338 |
| Best month by revenue | November 2011 |
| November 2011 revenue | £1,503,866.78 |
| Top country by revenue | United Kingdom |
| United Kingdom revenue | £9,001,744.09 |
| Top product description by revenue | DOTCOM POSTAGE |
| Revenue for top product description | £206,248.77 |
| Top identified customer ID | 14646 |
| Revenue for top identified customer | £280,206.02 |

*These figures reflect the cleaned positive-sales dataset, not net revenue after accounting for returns and refunds.*

## 💡 Key Insights

### 1. The United Kingdom was the dominant market

The United Kingdom generated £9.00 million in positive sales revenue, representing the largest share of revenue in the analyzed dataset.

### 2. November 2011 was the strongest month

November 2011 recorded approximately £1.50 million in positive sales revenue, making it the highest-revenue month in the analysis.

### 3. Product descriptions require business context

`DOTCOM POSTAGE` ranked first by recorded revenue among product descriptions. Because this is a postage-related description rather than a conventional merchandise item, the result should be interpreted separately from ordinary product performance.

### 4. Customer-level analysis can highlight valuable customers

Customer ID 14646 had the highest recorded revenue among identified customers, at approximately £280,206.02.

### 5. Data quality directly affects business conclusions

The original dataset contained duplicate rows, missing customer identifiers, cancellations, and invalid quantity or price values. Cleaning these records helped produce more consistent positive-sales metrics.

## 📊 Interactive Dashboard

The deployed Streamlit dashboard makes the analysis easier to explore without requiring users to run Python code.

Dashboard features include:

- KPI cards for key sales metrics.
- Monthly revenue trend visualization.
- Top 10 product descriptions by revenue.
- Top 10 countries by revenue.
- Top 10 identified customers by revenue.
- Country selection filters.
- A preview of the analyzed transaction data.

**[Open the Live Dashboard](PASTE_YOUR_STREAMLIT_DASHBOARD_URL_HERE)**

## 🧠 What I Learned

Through this project, I gained practical experience with:

- Loading and inspecting real-world datasets.
- Identifying and handling missing values and duplicate records.
- Filtering transactions using business rules.
- Performing data aggregation using Pandas `groupby()`.
- Working with dates and monthly time-series data.
- Calculating KPIs and interpreting sales patterns.
- Creating data visualizations.
- Building an interactive dashboard using Streamlit and Plotly.
- Managing project files with Git and GitHub.
- Deploying a Python application using Streamlit Community Cloud.
- Managing dependencies for a deployed application through `requirements.txt`.

## ⚠️ Limitations and Assumptions

- The analysis focuses on positive-sales transactions after removing cancellations and transactions with non-positive quantities or prices.
- The revenue values are not net revenue after subtracting returns or refunds.
- Customer analysis excludes transactions without a customer ID.
- The dataset ends in December 2011, and December may represent a partial reporting period.
- Product descriptions may include non-merchandise entries such as postage.
- The findings describe the available historical dataset and should not automatically be generalized to current retail performance.

## 🚀 Future Improvements

Potential extensions include:

- Adding product category analysis.
- Comparing monthly and year-over-year performance where suitable data is available.
- Adding country, date-range, and product filters.
- Analyzing cancellations and returns separately.
- Calculating average order value and repeat-purchase metrics.
- Adding customer segmentation and retention analysis.
- Improving dashboard layout and mobile responsiveness.

## ▶️ Run the Dashboard Locally

### Prerequisites

- Python installed on your computer.
- Git installed.
- An internet connection to download the source dataset.

### Installation

Clone the repository:

```bash
git clone https://github.com/Arjunlearns/retail-sales-dashboard.git
cd retail-sales-dashboard
```

Create and activate a virtual environment if desired, then install dependencies:

```bash
python -m pip install -r requirements.txt
```

Run the Streamlit application:

```bash
python -m streamlit run app.py
```

The terminal will display a local URL, usually `http://localhost:8501`, where you can open the dashboard.

The application downloads the original UCI dataset and performs the required cleaning steps, so the exported CSV does not need to be committed to the repository.

## 📁 Repository Structure

```text
retail-sales-dashboard/
├── app.py
├── requirements.txt
├── README.md
└── .gitignore
```

## 📚 References

- UCI Machine Learning Repository: [Online Retail Dataset](https://archive.ics.uci.edu/dataset/352/online+retail)
- [Pandas Documentation](https://pandas.pydata.org/docs/)
- [Plotly Documentation](https://plotly.com/python/)
- [Streamlit Documentation](https://docs.streamlit.io/)

---

**Author:** Arjun V Reddy

**Project:** Retail Sales Analytics Dashboard

**Focus Areas:** Data Analysis · Data Cleaning · Business Intelligence · Data Visualization · Dashboard Development
