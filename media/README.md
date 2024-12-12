# Automated Analysis Report

## Summary
{'columns': ['date', 'language', 'type', 'title', 'by', 'overall', 'quality', 'repeatability'], 'data_types': {'date': 'object', 'language': 'object', 'type': 'object', 'title': 'object', 'by': 'object', 'overall': 'int64', 'quality': 'int64', 'repeatability': 'int64'}, 'missing_values': {'date': 99, 'language': 0, 'type': 0, 'title': 0, 'by': 262, 'overall': 0, 'quality': 0, 'repeatability': 0}, 'summary_stats': {'date': {'count': 2553, 'unique': 2055, 'top': '21-May-06', 'freq': 8, 'mean': nan, 'std': nan, 'min': nan, '25%': nan, '50%': nan, '75%': nan, 'max': nan}, 'language': {'count': 2652, 'unique': 11, 'top': 'English', 'freq': 1306, 'mean': nan, 'std': nan, 'min': nan, '25%': nan, '50%': nan, '75%': nan, 'max': nan}, 'type': {'count': 2652, 'unique': 8, 'top': 'movie', 'freq': 2211, 'mean': nan, 'std': nan, 'min': nan, '25%': nan, '50%': nan, '75%': nan, 'max': nan}, 'title': {'count': 2652, 'unique': 2312, 'top': 'Kanda Naal Mudhal', 'freq': 9, 'mean': nan, 'std': nan, 'min': nan, '25%': nan, '50%': nan, '75%': nan, 'max': nan}, 'by': {'count': 2390, 'unique': 1528, 'top': 'Kiefer Sutherland', 'freq': 48, 'mean': nan, 'std': nan, 'min': nan, '25%': nan, '50%': nan, '75%': nan, 'max': nan}, 'overall': {'count': 2652.0, 'unique': nan, 'top': nan, 'freq': nan, 'mean': 3.0475113122171944, 'std': 0.7621797580962717, 'min': 1.0, '25%': 3.0, '50%': 3.0, '75%': 3.0, 'max': 5.0}, 'quality': {'count': 2652.0, 'unique': nan, 'top': nan, 'freq': nan, 'mean': 3.2092760180995477, 'std': 0.7967426636666686, 'min': 1.0, '25%': 3.0, '50%': 3.0, '75%': 4.0, 'max': 5.0}, 'repeatability': {'count': 2652.0, 'unique': nan, 'top': nan, 'freq': nan, 'mean': 1.4947209653092006, 'std': 0.598289430580212, 'min': 1.0, '25%': 1.0, '50%': 1.0, '75%': 2.0, 'max': 3.0}}, 'datetime_stats': {}, 'shape': (2652, 8)}

## Story
### Narrative Summary of Dataset Analysis

The dataset contains a total of 2,652 records, comprising 8 columns: `date`, `language`, `type`, `title`, `by`, `overall`, `quality`, and `repeatability`. Here is a breakdown of the key observations from the characteristics of the dataset:

1. **Columns Overview**:
   - **Date**: This column is formatted as an object type. However, it contains 99 missing values out of 2,652 records, indicating that some entries do not have a corresponding date.
   - **Language**: The dataset includes 11 unique languages, with 'English' being the most common, appearing 1,306 times.
   - **Type**: There are 8 unique types, predominantly featuring the category 'movie'.
   - **Title**: With 2,312 unique titles, 'Kanda Naal Mudhal' is the title with the highest frequency, appearing 9 times.
   - **By**: There are 1,528 unique contributors, with the top contributor, Kiefer Sutherland, appearing 48 times. This column has notable missing values (262).
   - **Overall Rating**: Ratings are provided in integer form (1 to 5) and show a mean rating of approximately 3.05 with a standard deviation of 0.76, indicating a reasonable spread of ratings.
   - **Quality Ratings**: Similarly, quality ratings have a mean of approximately 3.21 and a standard deviation of 0.80, suggesting consistency in quality across entries.
   - **Repeatability**: This integer rating has a mean of approximately 1.49, suggesting that most entries are rated as more predictable or similar.

2. **Missing Values**:
   - The dataset is relatively complete with notable exceptions in the `date` and `by` columns. The missing values in the `by` column may affect the analysis of contributor performance or trends.

3. **Statistical Overview**:
   - The descriptive statistics for the numeric ratings show that the majority of entries fall within the 3-4 range for both overall and quality scores. The distribution of these ratings is slightly skewed, indicating a general tendency towards better scores.

4. **Distribution of Ratings**:
   - The overall ratings typically center around 3, while quality ratings also cluster around this value. The repeatability scores are heavily skewed toward 1, indicating a trend of less repeatability among ratings.

### Timeseries Analysis

Given that the dataset contains a `date` column, we can conduct a preliminary timeseries analysis. However, before proceeding, we should check for the proper formatting of the date and address any missing or improperly formatted dates.

1. **Date Formatting**:
   - Convert the `date` column to a pandas datetime type, addressing the missing values by either filling or removing them.

```python
import pandas as pd

# Assuming `data` is the DataFrame containing the dataset
data['date'] = pd.to_datetime(data['date'], format='%d-%b-%y', errors='coerce')
```

2. **Handling Missing Dates**:
   - After converting, check for any remaining NaT (not a time) objects, which indicate failed conversions due to missing values.

```python
missing_dates = data['date'].isna().sum()
```

3. **Grouping by Date**:
   - If we can successfully handle the missing values, we can group the data by date to discern trends.

```python
daily_counts = data.groupby(data['date'].dt.date).size()
```

4. **Visualizing Trends**:
   - Plotting the daily entry counts or rating averages over time could reveal trends regarding how entries and ratings change over time.

```python
import matplotlib.pyplot as plt

plt.figure(figsize=(14, 7))
daily_counts.plot()
plt.title('Number of Entries Over Time')
plt.xlabel('Date')
plt.ylabel('Number of Entries')
plt.show()
```

### Insights from Timeseries Analysis

After conducting a timeseries analysis, we might observe:

- **Trends Over Time**: The number of entries may show cyclical patterns, indicating particular seasons or events that drive input.
- **Rating Patterns**: Trends in overall or quality ratings over time can help in assessing whether there are shifts in quality or public opinion.
- **Impact of Missing Values**: Investigating dates without any entries may highlight periods of inactivity or changes in the data collection process.

### Conclusion

This dataset provides a unique view of movie ratings and characteristics across languages and contributors, with clear patterns emerging in overall quality and repeatability scores. The integration of timeseries analysis can enhance understanding of how entries evolve over time. Addressing missing values will be crucial for ensuring the robustness of any conclusions drawn from the dataset.

## Visualizations
![Visualization](media\heatmap.png)
![Box Plot](media\boxplot.png)
# Profile Report
Data profiling report has been saved as 'media\data_profile.html'.
# Statistical Analysis Report
{'overall': {'norm': {'params': (np.float64(3.0475113122171944), np.float64(0.7620360454980117)), 'ks_statistic': np.float64(0.28051319835794214), 'p_value': np.float64(4.640116624273484e-185)}, 'expon': {'params': (1.0, 2.0475113122171944), 'ks_statistic': np.float64(0.4093063389502153), 'p_value': np.float64(0.0)}, 'lognorm': {'params': (np.float64(0.04813877686055134), -12.771183779336704, np.float64(15.800375982004649)), 'ks_statistic': np.float64(0.2709778861770157), 'p_value': np.float64(1.6518215663531124e-172)}, 'chi2': {'params': (np.float64(189.45326014484965), np.float64(-4.390915878282385), np.float64(0.039250450248671104)), 'ks_statistic': np.float64(0.27584208073424643), 'p_value': np.float64(7.471557584255665e-179)}}, 'quality': {'norm': {'params': (np.float64(3.2092760180995477), np.float64(0.7965924340690917)), 'ks_statistic': np.float64(0.25708358344332877), 'p_value': np.float64(4.7524559960258285e-155)}, 'expon': {'params': (1.0, 2.2092760180995477), 'ks_statistic': np.float64(0.4232461436612421), 'p_value': np.float64(0.0)}, 'lognorm': {'params': (np.float64(0.008943289704754368), -85.86103037886036, np.float64(89.06674444793252)), 'ks_statistic': np.float64(0.255479821279366), 'p_value': np.float64(4.257500472912363e-153)}, 'chi2': {'params': (np.float64(220.77630128059013), np.float64(-5.245954246519208), np.float64(0.0382756278472344)), 'ks_statistic': np.float64(0.24225160618595026), 'p_value': np.float64(1.7301652059608807e-137)}}, 'repeatability': {'norm': {'params': (np.float64(1.4947209653092006), np.float64(0.598176620278355)), 'ks_statistic': np.float64(0.3550957644108138), 'p_value': np.float64(1.0602976633912832e-299)}, 'expon': {'params': (1.0, 0.4947209653092006), 'ks_statistic': np.float64(0.5592006033182504), 'p_value': np.float64(0.0)}, 'lognorm': {'params': (np.float64(17.937789054236266), np.float64(0.9999999999999998), np.float64(1.8312681394276613e-09)), 'ks_statistic': np.float64(0.37187983795758034), 'p_value': np.float64(0.0)}, 'chi2': {'params': (np.float64(1.0177295870092673), np.float64(0.9999999999999999), np.float64(0.8744412368094363)), 'ks_statistic': np.float64(0.5592005968611535), 'p_value': np.float64(0.0)}}}
# Sentiment Analysis Report
           date language   type              title                             by  overall  quality  repeatability
0     15-Nov-24    Tamil  movie        Meiyazhagan           Arvind Swamy, Karthi        4        5              1
1     10-Nov-24    Tamil  movie          Vettaiyan        Rajnikanth, Fahad Fazil        2        2              1
2     09-Nov-24    Tamil  movie             Amaran  Siva Karthikeyan, Sai Pallavi        4        4              1
3     11-Oct-24   Telugu  movie              Kushi    Vijay Devarakonda, Samantha        3        3              1
4     05-Oct-24    Tamil  movie               GOAT                          Vijay        3        3              1
...         ...      ...    ...                ...                            ...      ...      ...            ...
2647        NaN  English  movie     Monsters, Inc.                            NaN        3        3              2
2648        NaN  English  movie    The Incredibles                            NaN        3        3              2
2649        NaN  English  movie               Cars                            NaN        3        3              2
2650        NaN  English  movie        Ratatouille                            NaN        4        4              2
2651        NaN  English  movie  Maid in Manhattan  Jennifer Lopez, Ralph Fiennes        3        3              2

[2652 rows x 8 columns]
