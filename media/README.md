# Automated Analysis Report

## Summary
### Dataset Overview

- **Shape**: (2652, 8)  *(Rows: 2652, Columns: 8)*

#### Columns and Data Types

| Column Name   | Data Type   |
|---------------|-------------|
| date          | object      |
| language      | object      |
| type          | object      |
| title         | object      |
| by            | object      |
| overall       | int64       |
| quality       | int64       |
| repeatability | int64       |

#### Missing Values

| Column Name   |   Missing Count |
|---------------|-----------------|
| date          |              99 |
| by            |             262 |

#### Summary Statistics (Numeric Columns)

| Column        |   Count |      Mean |    Std Dev |   Min |   25% |   50% |   75% |   Max |
|---------------|---------|-----------|------------|-------|-------|-------|-------|-------|
| date          |    2553 | nan       | nan        |   nan |   nan |   nan |   nan |   nan |
| language      |    2652 | nan       | nan        |   nan |   nan |   nan |   nan |   nan |
| type          |    2652 | nan       | nan        |   nan |   nan |   nan |   nan |   nan |
| title         |    2652 | nan       | nan        |   nan |   nan |   nan |   nan |   nan |
| by            |    2390 | nan       | nan        |   nan |   nan |   nan |   nan |   nan |
| overall       |    2652 |   3.04751 |   0.76218  |     1 |     3 |     3 |     3 |     5 |
| quality       |    2652 |   3.20928 |   0.796743 |     1 |     3 |     3 |     4 |     5 |
| repeatability |    2652 |   1.49472 |   0.598289 |     1 |     1 |     1 |     2 |     3 |

#### Summary Statistics (Categorical Columns)

| Column        |   Count |   Unique | Top               |   Frequency of Top |
|---------------|---------|----------|-------------------|--------------------|
| date          |    2553 |     2055 | 21-May-06         |                  8 |
| language      |    2652 |       11 | English           |               1306 |
| type          |    2652 |        8 | movie             |               2211 |
| title         |    2652 |     2312 | Kanda Naal Mudhal |                  9 |
| by            |    2390 |     1528 | Kiefer Sutherland |                 48 |
| overall       |    2652 |      nan | nan               |                nan |
| quality       |    2652 |      nan | nan               |                nan |
| repeatability |    2652 |      nan | nan               |                nan |

#### Date/Time Columns

| Column Name   | Min Date   | Max Date   |
|---------------|------------|------------|



## Story
Based on the analysis of the dataset with 2652 rows and 8 columns, the following structured narrative summarizes the findings and insights:

### Dataset Overview

The dataset consists of entries related to movies, with eight key columns capturing various attributes of each entry. Notably, the dataset includes metadata that ranges from qualitative ratings to categorical attributes such as language and movie titles.

### Column Details

1. **Date**: Represented in the `date` column, this field has 99 missing values, indicating that 99 entries lack associated dates. The dates span various movies, potentially allowing for time-based analyses.
  
2. **Language**: The `language` column indicates the language of the movies listed, with a predominance of the English language (1306 occurrences), suggesting a global focus with respect to English-speaking audiences.

3. **Type**: All entries are categorized under 'movie', suggesting a singular thematic approach of the dataset.

4. **Title**: The dataset consists of 2312 unique movie titles, with “Kanda Naal Mudhal” being the most frequently mentioned film at 9 occurrences, indicating possible repeat representations or a dataset that focuses on both popular and niche titles.

5. **By**: This column features the names of actors or directors associated with the movies, but it has a considerable missing value count (262), emphasizing a need for further investigation into the popularity or representation of certain figures in the film industry.

6. **Overall Rating**: The `overall` rating column reflects a mean value of approximately 3.05 on a scale presumably up to 5, with a notable standard deviation of about 0.76. The ratings seem to be concentrated around the moderate range, indicating a general trend of middling quality perceptions.

7. **Quality Rating**: Similar to the overall rating, the `quality` rating averages at 3.21 with a slightly higher standard deviation of 0.80, indicating that the quality of the movies perceived by the subjects in the dataset varies more broadly than the overall ratings.

8. **Repeatability**: This column has a mean value of 1.49, which may suggest that many of the movies listed are either single-view experiences or that movies have limited audiences or repeated viewings.

### Statistical Insights

- There are missing values primarily in the `date` and `by` columns, suggesting that data cleaning efforts could enhance analysis fidelity.
- The `overall` and `quality` ratings are minutely negatively skewed, presenting a general tendency towards more favorable ratings. This implies that while there are lower-rated films, the bulk falls into a more praise-oriented category.
- The `repeatability` score indicates that movies in this dataset tend to be one-time watch experiences, with limited repeated engagement.

### Time Series Analysis

Given the presence of the `date` column, we can conduct a time-series analysis:

- **Date Coverage**: The date column captures a wide range of movie release dates. To perform a robust time series analysis, it's essential first to convert the `date` column from an object type to a datetime format.
  
- **Frequency Analysis**: Once transformed, chronological trends such as the volume of movies released per month or year can be evaluated across the dataset. Additionally, it would be beneficial to examine how the overall ratings and quality ratings have changed over time, potentially revealing shifts in audience reception or industry standards.

### Conclusion and Recommendations

1. **Data Cleaning**: Addressing missing values, especially in the `date` and `by` columns, is paramount for any further analysis.
  
2. **Expanded Analysis**: Further exploration into how the ratings correlate with language or type could provide insights into audience preferences across different demographics.
  
3. **Time Series Visualization**: Once the `date` column is prepared, visualizing trends over time can yield valuable insights about the film industry’s evolution as perceived by viewers.
  
4. **Actor/Director Influence**: Investigating the correlation between the `by` column and the ratings may reveal how associated talent influences viewer reception, guiding future casting decisions.

This structured narrative provides a comprehensive overview of the dataset, elucidating key insights and guiding where future analyses could delve deeper to yield impactful findings.

## Visualizations
![Visualization](media\heatmap.png)
![Box Plot](media\boxplot.png)
# Statistical Analysis Report
+----+---------------+----------------+------------------------------------------------------------------------------------------------------+----------------+-----------+
|    | Column        | Distribution   | Params                                                                                               |   KS Statistic |   P-value |
+====+===============+================+======================================================================================================+================+===========+
|  0 | overall       | norm           | (np.float64(3.0475113122171944), np.float64(0.7620360454980117))                                     |         0.2805 |         0 |
+----+---------------+----------------+------------------------------------------------------------------------------------------------------+----------------+-----------+
|  1 | overall       | expon          | (1.0, 2.0475113122171944)                                                                            |         0.4093 |         0 |
+----+---------------+----------------+------------------------------------------------------------------------------------------------------+----------------+-----------+
|  2 | overall       | lognorm        | (np.float64(0.04813877686055134), -12.771183779336704, np.float64(15.800375982004649))               |         0.271  |         0 |
+----+---------------+----------------+------------------------------------------------------------------------------------------------------+----------------+-----------+
|  3 | overall       | chi2           | (np.float64(189.45326014484965), np.float64(-4.390915878282385), np.float64(0.039250450248671104))   |         0.2758 |         0 |
+----+---------------+----------------+------------------------------------------------------------------------------------------------------+----------------+-----------+
|  4 | quality       | norm           | (np.float64(3.2092760180995477), np.float64(0.7965924340690917))                                     |         0.2571 |         0 |
+----+---------------+----------------+------------------------------------------------------------------------------------------------------+----------------+-----------+
|  5 | quality       | expon          | (1.0, 2.2092760180995477)                                                                            |         0.4232 |         0 |
+----+---------------+----------------+------------------------------------------------------------------------------------------------------+----------------+-----------+
|  6 | quality       | lognorm        | (np.float64(0.008943289704754368), -85.86103037886036, np.float64(89.06674444793252))                |         0.2555 |         0 |
+----+---------------+----------------+------------------------------------------------------------------------------------------------------+----------------+-----------+
|  7 | quality       | chi2           | (np.float64(220.77630128059013), np.float64(-5.245954246519208), np.float64(0.0382756278472344))     |         0.2423 |         0 |
+----+---------------+----------------+------------------------------------------------------------------------------------------------------+----------------+-----------+
|  8 | repeatability | norm           | (np.float64(1.4947209653092006), np.float64(0.598176620278355))                                      |         0.3551 |         0 |
+----+---------------+----------------+------------------------------------------------------------------------------------------------------+----------------+-----------+
|  9 | repeatability | expon          | (1.0, 0.4947209653092006)                                                                            |         0.5592 |         0 |
+----+---------------+----------------+------------------------------------------------------------------------------------------------------+----------------+-----------+
| 10 | repeatability | lognorm        | (np.float64(17.937789054236266), np.float64(0.9999999999999998), np.float64(1.8312681394276613e-09)) |         0.3719 |         0 |
+----+---------------+----------------+------------------------------------------------------------------------------------------------------+----------------+-----------+
| 11 | repeatability | chi2           | (np.float64(1.0177295870092673), np.float64(0.9999999999999999), np.float64(0.8744412368094363))     |         0.5592 |         0 |
+----+---------------+----------------+------------------------------------------------------------------------------------------------------+----------------+-----------+
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
