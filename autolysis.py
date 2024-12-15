# /// script
# requires-python = ">=3.11"
# dependencies = [
#   "httpx",
#   "pandas",
#   "matplotlib",
#   "seaborn",
#   "requests",
#   "scipy",
#   "numpy",
#   "textblob",
# ]
# ///

import os
import sys
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import requests
import json
from scipy import stats
from scipy.stats import norm, expon, lognorm, chi2
import numpy as np
from textblob import TextBlob
import warnings
from charset_normalizer import detect

# Suppress warnings related to data fitting
warnings.filterwarnings("ignore")

# Print arguments passed to the script
print("Arguments passed:", sys.argv)
print("Starting analysis script")

# Directly set the token in os.environ (for temporary use only)
os.environ["AIPROXY_TOKEN"] = "eyJhbGciOiJIUzI1NiJ9.eyJlbWFpbCI6IjIzZjEwMDE3MDVAZHMuc3R1ZHkuaWl0bS5hYy5pbiJ9.38K6jer3VKplM-TfIzuiob-JB8jizvKZy72qJ_cDalM" # Replace with your token

# Retrieve the token
AIPROXY_TOKEN = os.environ.get("AIPROXY_TOKEN")

# Verify environment variable
if "AIPROXY_TOKEN" not in os.environ:
    print("Error: AIPROXY_TOKEN environment variable is not set.")
    sys.exit(1)

# Function to detect file encoding
def detect_encoding(file_path):
    with open(file_path, "rb") as file:
        raw_data = file.read()
        result = detect(raw_data)
        return result["encoding"]

# Function to load dataset
def load_dataset(file_path):
    try:
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"The file {file_path} does not exist.")
        if not file_path.lower().endswith(".csv"):
            raise ValueError(f"The file {file_path} is not a CSV file.")

        encoding = detect_encoding(file_path)
        print(f"Detected file encoding: {encoding}")
        df = pd.read_csv(file_path, encoding=encoding)
        return df
    except Exception as e:
        print(f"Error loading dataset: {e}")
        sys.exit(1)

# Function to analyze the dataset
def analyze_dataset(df):
    numeric_and_categorical = df.select_dtypes(include=["number", "object", "category", "bool"])
    datetime_columns = df.select_dtypes(include=["datetime"])
    summary_stats = numeric_and_categorical.describe(include="all").to_dict()
    datetime_stats = {col: {"min": df[col].min(), "max": df[col].max()} for col in datetime_columns.columns}

    summary = {
        "columns": list(df.columns),
        "data_types": df.dtypes.astype(str).to_dict(),
        "missing_values": df.isnull().sum().to_dict(),
        "summary_stats": summary_stats,
        "datetime_stats": datetime_stats,
        "shape": df.shape,
    }
    return summary


# Function to generate a profile report

# Function to visualize data
def visualize_data(df, output_folder):
    numeric_df = df.select_dtypes(include=["number"])
    chart_paths = []

    if not numeric_df.empty:
        plt.figure(figsize=(10, 8))
        sns.heatmap(numeric_df.corr(), annot=True, cmap="coolwarm")
        plt.title("Correlation Heatmap")
        heatmap_path = os.path.join(output_folder, "heatmap.png")
        plt.savefig(heatmap_path)
        plt.close()
        chart_paths.append(heatmap_path)
    else:
        print("No numeric data available for correlation analysis.")
    return chart_paths

# Function to fit distributions and plot
def fit_and_plot_distribution(df, output_folder):
    numeric_df = df.select_dtypes(include=["number"])
    if numeric_df.empty:
        print("No numeric data available for distribution fitting.")
        return {}

    results = {}
    for column in numeric_df.columns:
        data = numeric_df[column].dropna()
        distributions = [norm, expon, lognorm, chi2]
        column_results = {}

        for dist in distributions:
            try:
                params = dist.fit(data)
                D, p_value = stats.kstest(data, dist.cdf, args=params)
                column_results[dist.name] = {"params": params, "ks_statistic": D, "p_value": p_value}
            except Exception as e:
                print(f"Error fitting distribution {dist.name} for column {column}: {e}")

        results[column] = column_results
        x = np.linspace(data.min(), data.max(), 100)

        # Plot the fitted distributions
        plt.figure()
        plt.hist(data, bins=30, density=True, alpha=0.6, label="Data")
        for dist in distributions:
            try:
                params = dist.fit(data)
                plt.plot(x, dist.pdf(x, *params), label=dist.name)
            except Exception as e:
                print(f"Error plotting distribution {dist.name} for column {column}: {e}")
        plt.title(f"Distributions Fitted to {column}")
        plt.legend()

        # Save the plot
        dist_plot_path = os.path.join(output_folder, f"{column}_distributions.png")
        plt.savefig(dist_plot_path)
        plt.close()

    return results

# Function to perform sentiment analysis only on specified columns
def perform_sentiment_analysis(df, output_folder, keyword="review"):
    target_columns = [col for col in df.columns if keyword.lower() in col.lower()]
    for col in target_columns:
        if df[col].dtype == "object":
            sentiment_col = f"{col}_sentiment"
            df[sentiment_col] = df[col].apply(
                lambda text: TextBlob(str(text)).sentiment.polarity if pd.notnull(text) else None
            )
    sentiment_output_path = os.path.join(output_folder, "sentiment_analysis.csv")
    df.to_csv(sentiment_output_path, index=False)
    print(f"Sentiment analysis saved to {sentiment_output_path}")
    return df

# Function to plot boxplots
def plot_boxplot(df, output_folder):
    numeric_df = df.select_dtypes(include=["number"])
    if not numeric_df.empty:
        plt.figure(figsize=(10, 6))
        sns.boxplot(data=numeric_df)
        plt.title("Box Plot of Numeric Data")
        plt.xticks(rotation=45)
        boxplot_path = os.path.join(output_folder, "boxplot.png")
        plt.savefig(boxplot_path)
        plt.close()
        return boxplot_path
    else:
        print("No numeric data available to plot.")
        return None
def generate_narration(prompt):
    url = "https://aiproxy.sanand.workers.dev/openai/v1/chat/completions"
    headers = {"Content-Type": "application/json", "Authorization": f"Bearer {AIPROXY_TOKEN}"}
    data = {"model": "gpt-4o-mini", "messages": [{"role": "user", "content": prompt}]}

    try:
        response = requests.post(url, headers=headers, data=json.dumps(data))
        response.raise_for_status()
        return response.json()["choices"][0]["message"]["content"]
    except Exception as e:
        print(f"Error generating narration: {e}")
        sys.exit(1)
# Main function
def main():
    if len(sys.argv) != 2:
        print("Usage: python script.py dataset.csv")
        sys.exit(1)

    file_path = sys.argv[1]
    output_folder = os.path.splitext(file_path)[0]
    os.makedirs(output_folder, exist_ok=True)

    df = load_dataset(file_path)
    summary = analyze_dataset(df)
    chart_paths = visualize_data(df, output_folder)
    stat = fit_and_plot_distribution(df, output_folder)
    sentiment = perform_sentiment_analysis(df, output_folder)
    box_plot_path = plot_boxplot(df, output_folder)
    
    prompt = f"I analyzed the dataset with the following characteristics: {summary}, {stat},{df}. Provide a narrative.Also do timeseries analysis if you find any date column in my dataset"
    story = generate_narration(prompt)

    readme_path = os.path.join(output_folder, "README.md")
    with open(readme_path, "w") as f:
        f.write(f"# Automated Analysis Report\n\n## Summary\n{summary}\n\n")
        f.write(f"## Story\n{story}\n\n")
        f.write("## Visualizations\n")
        for chart in chart_paths:
            f.write(f"![Visualization]({chart})\n")
        if box_plot_path:
            f.write(f"![Box Plot]({box_plot_path})\n")
        f.write(f"# Statistical Analysis Report\n{stat}\n")
        f.write(f"# Sentiment Analysis Report\n{sentiment}\n")

    print("Analysis complete. Results saved in", output_folder)

if __name__ == "__main__":
    main()
