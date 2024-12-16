# Automated Analysis Report

## Summary
### Dataset Overview

- **Shape**: (2363, 11)  *(Rows: 2363, Columns: 11)*

#### Columns and Data Types

| Column Name                      | Data Type   |
|----------------------------------|-------------|
| Country name                     | object      |
| year                             | int64       |
| Life Ladder                      | float64     |
| Log GDP per capita               | float64     |
| Social support                   | float64     |
| Healthy life expectancy at birth | float64     |
| Freedom to make life choices     | float64     |
| Generosity                       | float64     |
| Perceptions of corruption        | float64     |
| Positive affect                  | float64     |
| Negative affect                  | float64     |

#### Missing Values

| Column Name                      |   Missing Count |
|----------------------------------|-----------------|
| Log GDP per capita               |              28 |
| Social support                   |              13 |
| Healthy life expectancy at birth |              63 |
| Freedom to make life choices     |              36 |
| Generosity                       |              81 |
| Perceptions of corruption        |             125 |
| Positive affect                  |              24 |
| Negative affect                  |              16 |

#### Summary Statistics (Numeric Columns)

| Column                           |   Count |           Mean |     Std Dev |      Min |       25% |       50% |        75% |      Max |
|----------------------------------|---------|----------------|-------------|----------|-----------|-----------|------------|----------|
| Country name                     |    2363 |  nan           | nan         |  nan     |  nan      |  nan      |  nan       |  nan     |
| year                             |    2363 | 2014.76        |   5.05944   | 2005     | 2011      | 2015      | 2019       | 2023     |
| Life Ladder                      |    2363 |    5.48357     |   1.12552   |    1.281 |    4.647  |    5.449  |    6.3235  |    8.019 |
| Log GDP per capita               |    2335 |    9.39967     |   1.15207   |    5.527 |    8.5065 |    9.503  |   10.3925  |   11.676 |
| Social support                   |    2350 |    0.809369    |   0.121212  |    0.228 |    0.744  |    0.8345 |    0.904   |    0.987 |
| Healthy life expectancy at birth |    2300 |   63.4018      |   6.84264   |    6.72  |   59.195  |   65.1    |   68.5525  |   74.6   |
| Freedom to make life choices     |    2327 |    0.750282    |   0.139357  |    0.228 |    0.661  |    0.771  |    0.862   |    0.985 |
| Generosity                       |    2282 |    9.77213e-05 |   0.161388  |   -0.34  |   -0.112  |   -0.022  |    0.09375 |    0.7   |
| Perceptions of corruption        |    2238 |    0.743971    |   0.184865  |    0.035 |    0.687  |    0.7985 |    0.86775 |    0.983 |
| Positive affect                  |    2339 |    0.651882    |   0.10624   |    0.179 |    0.572  |    0.663  |    0.737   |    0.884 |
| Negative affect                  |    2347 |    0.273151    |   0.0871311 |    0.083 |    0.209  |    0.262  |    0.326   |    0.705 |

#### Summary Statistics (Categorical Columns)

| Column                           |   Count |   Unique | Top       |   Frequency of Top |
|----------------------------------|---------|----------|-----------|--------------------|
| Country name                     |    2363 |      165 | Argentina |                 18 |
| year                             |    2363 |      nan | nan       |                nan |
| Life Ladder                      |    2363 |      nan | nan       |                nan |
| Log GDP per capita               |    2335 |      nan | nan       |                nan |
| Social support                   |    2350 |      nan | nan       |                nan |
| Healthy life expectancy at birth |    2300 |      nan | nan       |                nan |
| Freedom to make life choices     |    2327 |      nan | nan       |                nan |
| Generosity                       |    2282 |      nan | nan       |                nan |
| Perceptions of corruption        |    2238 |      nan | nan       |                nan |
| Positive affect                  |    2339 |      nan | nan       |                nan |
| Negative affect                  |    2347 |      nan | nan       |                nan |

#### Date/Time Columns

| Column Name   | Min Date   | Max Date   |
|---------------|------------|------------|



## Story
### Narrative Overview of the Dataset

The dataset consists of a total of 2,363 rows and 11 columns, reflecting various metrics related to well-being and socio-economic conditions of different countries over a range of years. Key columns include various indicators such as Life Ladder (life satisfaction), Log GDP per capita, and measures of social support and generational well-being. 

#### Data Type and Characteristics

The dataset holds primarily numerical data, such as integers for the year and floating-point numbers for metrics. The categorical variable is 'Country name', with a total of 165 unique countries represented within the dataset. The year spans from 2005 to 2023, indicating the data records various socio-economic conditions over a considerable timeframe.

### Summary Statistics

**Numerical Columns:** 
- **Life Ladder**: The mean life satisfaction score is about 5.48, with a standard deviation of 1.12, suggesting a relatively wide distribution of perceived life satisfaction across countries.
- **Log GDP Per Capita**: The average logarithmic GDP per capita is approximately 9.40, reflecting considerable economic variability, with a standard deviation of 1.15.
- **Social Support**: This measure averages 0.81, indicating that respondents generally feel supported; however, a standard deviation of 0.12 shows there's variability in social support perceptions.
- **Negative and Positive Affect**: These scores average around 0.27 and 0.65, respectively. While the average positive affect score suggests a generally positive outlook, the negative affect scores indicate some level of negative emotional experiences.

**Missing Values**: 
- The dataset contains several missing values across multiple columns. The number of missing entries ranges from 13 in social support to 125 in perceptions of corruption, potentially skewing analyses if not addressed properly.

### Insights from Statistical Summary

1. **Life Satisfaction**: The average Life Ladder score of 5.48 suggests that global life satisfaction is moderate, but with a one-standard deviation spread, it underscores felt disparities among different national contexts.
  
2. **GDP Contribution**: A mean log GDP per capita of 9.40 corresponds with an average GDP of approximately 12,186 (using the exponential function), hinting at significant economic variation across countries.

3. **Social Measures**: High average social support levels (0.81) contrast with relatively low generosity scores (mean = 0.0000977), prompting a discussion on societal welfare priorities versus altruistic behaviors.

4. **Corruption's Impact**: The low average score for perceptions of corruption (0.74) suggests many view their countries as relatively free from corruption, although with substantial variability that requires further investigation.

### Time Series Analysis

Given the presence of a 'year' column, a time series analysis can be performed focusing on certain key metrics:

1. **Trend Analysis**: Analyzing the change over time in the Life Ladder, Log GDP per capita, and Social Support can reveal socio-economic trends. For instance:
   - If we graphed Life Ladder scores over years, one might observe potential improvements or declines in life satisfaction.
   - Similarly, GDP growth rates may be evaluated to see how economic improvements relate to life satisfaction changes.

2. **Seasonality and Cyclic Patterns**: The impact of global events (e.g., economic crises or public health emergencies) may show visible effects on these metrics over years. Observational patterns, possibly aligning with historical events, might suggest if economies and societies recover post-crises.

3. **Correlation Analysis**: One could compute correlations between metrics, for instance, between Log GDP per capita and Life Ladder scores, revealing how economic reality translates into life satisfaction across different countries.

### Conclusion and Recommendations

The dataset provides valuable insights into socio-economic indicators affecting life satisfaction and well-being across 165 countries. However, the presence of missing values necessitates careful preprocessing to ensure accuracy in statistical outputs. 

Future studies would benefit from:
- **Handling Missing Data**: Techniques such as imputation or removal could enhance data quality.
- **Causal Analysis**: Exploring causal relationships between socio-economic indicators using advanced statistical methods could provide deeper insights into the factors influencing life satisfaction.
- **Comparative Analysis**: Comparisons between regions or groups may unearth critical insights into how cultural and geographical factors influence well-being metrics.

Overall, this dataset presents a robust starting point for understanding complex interactions between socio-economic conditions and perceived well-being on a global scale.

## Visualizations
![Visualization](happiness\heatmap.png)
![Box Plot](happiness\boxplot.png)
# Statistical Analysis Report
+----+----------------------------------+----------------+-----------------------------------------------------------------------------------------------------+----------------+-----------+
|    | Column                           | Distribution   | Params                                                                                              |   KS Statistic |   P-value |
+====+==================================+================+=====================================================================================================+================+===========+
|  0 | year                             | norm           | (np.float64(2014.7638595006347), np.float64(5.0583658012739825))                                    |         0.0777 |    0      |
+----+----------------------------------+----------------+-----------------------------------------------------------------------------------------------------+----------------+-----------+
|  1 | year                             | expon          | (2005.0, 9.76385950063468)                                                                          |         0.2196 |    0      |
+----+----------------------------------+----------------+-----------------------------------------------------------------------------------------------------+----------------+-----------+
|  2 | year                             | lognorm        | (np.float64(4.905342163702797e-06), -1029180.7023343472, np.float64(1031195.4661814413))            |         0.0777 |    0      |
+----+----------------------------------+----------------+-----------------------------------------------------------------------------------------------------+----------------+-----------+
|  3 | year                             | chi2           | (np.float64(0.5317103439208279), np.float64(2004.9999999999998), np.float64(3.030983199702571))     |         0.7424 |    0      |
+----+----------------------------------+----------------+-----------------------------------------------------------------------------------------------------+----------------+-----------+
|  4 | Life Ladder                      | norm           | (np.float64(5.483565806178587), np.float64(1.125283332829534))                                      |         0.0284 |    0.0438 |
+----+----------------------------------+----------------+-----------------------------------------------------------------------------------------------------+----------------+-----------+
|  5 | Life Ladder                      | expon          | (1.281, 4.202565806178587)                                                                          |         0.3846 |    0      |
+----+----------------------------------+----------------+-----------------------------------------------------------------------------------------------------+----------------+-----------+
|  6 | Life Ladder                      | lognorm        | (np.float64(2.026312231667982e-05), -55528.107398573935, np.float64(55533.59095297922))             |         0.0284 |    0.0438 |
+----+----------------------------------+----------------+-----------------------------------------------------------------------------------------------------+----------------+-----------+
|  7 | Life Ladder                      | chi2           | (np.float64(252.6766206197169), np.float64(-7.263741416460022), np.float64(0.050409743562686654))   |         0.0334 |    0.0099 |
+----+----------------------------------+----------------+-----------------------------------------------------------------------------------------------------+----------------+-----------+
|  8 | Log GDP per capita               | norm           | (np.float64(9.399671092077087), np.float64(1.1518227222400157))                                     |         0.0584 |    0      |
+----+----------------------------------+----------------+-----------------------------------------------------------------------------------------------------+----------------+-----------+
|  9 | Log GDP per capita               | expon          | (5.527, 3.872671092077087)                                                                          |         0.3355 |    0      |
+----+----------------------------------+----------------+-----------------------------------------------------------------------------------------------------+----------------+-----------+
| 10 | Log GDP per capita               | lognorm        | (np.float64(1.0788592803768132e-06), -1067620.9690362012, np.float64(1067630.3687066722))           |         0.0584 |    0      |
+----+----------------------------------+----------------+-----------------------------------------------------------------------------------------------------+----------------+-----------+
| 11 | Log GDP per capita               | chi2           | (np.float64(240.94793065025402), np.float64(-3.571104407317352), np.float64(0.053783014920145096))  |         0.0625 |    0      |
+----+----------------------------------+----------------+-----------------------------------------------------------------------------------------------------+----------------+-----------+
| 12 | Social support                   | norm           | (np.float64(0.8093693617021277), np.float64(0.12118597172175403))                                   |         0.0939 |    0      |
+----+----------------------------------+----------------+-----------------------------------------------------------------------------------------------------+----------------+-----------+
| 13 | Social support                   | expon          | (0.228, 0.5813693617021277)                                                                         |         0.4044 |    0      |
+----+----------------------------------+----------------+-----------------------------------------------------------------------------------------------------+----------------+-----------+
| 14 | Social support                   | lognorm        | (np.float64(9.47604775027982e-06), -12787.919799347554, np.float64(12788.729168135065))             |         0.0939 |    0      |
+----+----------------------------------+----------------+-----------------------------------------------------------------------------------------------------+----------------+-----------+
| 15 | Social support                   | chi2           | (np.float64(566.9482129284302), np.float64(-1.3004663258640763), np.float64(0.0037188680212272797)) |         0.1054 |    0      |
+----+----------------------------------+----------------+-----------------------------------------------------------------------------------------------------+----------------+-----------+
| 16 | Healthy life expectancy at birth | norm           | (np.float64(63.40182826086956), np.float64(6.841156658723825))                                      |         0.108  |    0      |
+----+----------------------------------+----------------+-----------------------------------------------------------------------------------------------------+----------------+-----------+
| 17 | Healthy life expectancy at birth | expon          | (6.72, 56.68182826086956)                                                                           |         0.5006 |    0      |
+----+----------------------------------+----------------+-----------------------------------------------------------------------------------------------------+----------------+-----------+
| 18 | Healthy life expectancy at birth | lognorm        | (np.float64(6.5239067730242576e-06), -1048569.2799999991, np.float64(1048632.6818059443))           |         0.108  |    0      |
+----+----------------------------------+----------------+-----------------------------------------------------------------------------------------------------+----------------+-----------+
| 19 | Healthy life expectancy at birth | chi2           | (np.float64(491.9210235719588), np.float64(-51.09586576357333), np.float64(0.2328305204870042))     |         0.113  |    0      |
+----+----------------------------------+----------------+-----------------------------------------------------------------------------------------------------+----------------+-----------+
| 20 | Freedom to make life choices     | norm           | (np.float64(0.750281908036098), np.float64(0.1393270878779754))                                     |         0.0618 |    0      |
+----+----------------------------------+----------------+-----------------------------------------------------------------------------------------------------+----------------+-----------+
| 21 | Freedom to make life choices     | expon          | (0.228, 0.522281908036098)                                                                          |         0.3666 |    0      |
+----+----------------------------------+----------------+-----------------------------------------------------------------------------------------------------+----------------+-----------+
| 22 | Freedom to make life choices     | lognorm        | (np.float64(8.503604794052661e-06), -16383.772, np.float64(16384.52228131564))                      |         0.0618 |    0      |
+----+----------------------------------+----------------+-----------------------------------------------------------------------------------------------------+----------------+-----------+
| 23 | Freedom to make life choices     | chi2           | (np.float64(374.49523755461473), np.float64(-1.2095260439227289), np.float64(0.005232300454395284)) |         0.0709 |    0      |
+----+----------------------------------+----------------+-----------------------------------------------------------------------------------------------------+----------------+-----------+
| 24 | Generosity                       | norm           | (np.float64(9.772129710779973e-05), np.float64(0.16135223825174483))                                |         0.0652 |    0      |
+----+----------------------------------+----------------+-----------------------------------------------------------------------------------------------------+----------------+-----------+
| 25 | Generosity                       | expon          | (-0.34, 0.3400977212971078)                                                                         |         0.2647 |    0      |
+----+----------------------------------+----------------+-----------------------------------------------------------------------------------------------------+----------------+-----------+
| 26 | Generosity                       | lognorm        | (np.float64(0.27663079510429456), np.float64(-0.5755934700591047), np.float64(0.5541383767680862))  |         0.0121 |    0.8866 |
+----+----------------------------------+----------------+-----------------------------------------------------------------------------------------------------+----------------+-----------+
| 27 | Generosity                       | chi2           | (np.float64(0.9266232261106886), np.float64(-0.3400000000000001), np.float64(0.9294721091405682))   |         0.337  |    0      |
+----+----------------------------------+----------------+-----------------------------------------------------------------------------------------------------+----------------+-----------+
| 28 | Perceptions of corruption        | norm           | (np.float64(0.7439709562109026), np.float64(0.18482417448645486))                                   |         0.1501 |    0      |
+----+----------------------------------+----------------+-----------------------------------------------------------------------------------------------------+----------------+-----------+
| 29 | Perceptions of corruption        | expon          | (0.035, 0.7089709562109026)                                                                         |         0.3888 |    0      |
+----+----------------------------------+----------------+-----------------------------------------------------------------------------------------------------+----------------+-----------+
| 30 | Perceptions of corruption        | lognorm        | (np.float64(1.128037870147264e-05), -16383.965, np.float64(16384.708969913743))                     |         0.1501 |    0      |
+----+----------------------------------+----------------+-----------------------------------------------------------------------------------------------------+----------------+-----------+
| 31 | Perceptions of corruption        | chi2           | (np.float64(239.8859554557386), np.float64(-1.5229030060705315), np.float64(0.009429718125157915))  |         0.1724 |    0      |
+----+----------------------------------+----------------+-----------------------------------------------------------------------------------------------------+----------------+-----------+
| 32 | Positive affect                  | norm           | (np.float64(0.6518820008550662), np.float64(0.1062169918191322))                                    |         0.0664 |    0      |
+----+----------------------------------+----------------+-----------------------------------------------------------------------------------------------------+----------------+-----------+
| 33 | Positive affect                  | expon          | (0.179, 0.4728820008550662)                                                                         |         0.4178 |    0      |
+----+----------------------------------+----------------+-----------------------------------------------------------------------------------------------------+----------------+-----------+
| 34 | Positive affect                  | lognorm        | (np.float64(1.2965231520830616e-05), -8191.820999999995, np.float64(8192.47288131228))              |         0.0664 |    0      |
+----+----------------------------------+----------------+-----------------------------------------------------------------------------------------------------+----------------+-----------+
| 35 | Positive affect                  | chi2           | (np.float64(295.0679926377616), np.float64(-0.6688153086286702), np.float64(0.004471771381193882))  |         0.075  |    0      |
+----+----------------------------------+----------------+-----------------------------------------------------------------------------------------------------+----------------+-----------+
| 36 | Negative affect                  | norm           | (np.float64(0.27315083084789094), np.float64(0.08711250825779107))                                  |         0.0567 |    0      |
+----+----------------------------------+----------------+-----------------------------------------------------------------------------------------------------+----------------+-----------+
| 37 | Negative affect                  | expon          | (0.083, 0.19015083084789092)                                                                        |         0.2756 |    0      |
+----+----------------------------------+----------------+-----------------------------------------------------------------------------------------------------+----------------+-----------+
| 38 | Negative affect                  | lognorm        | (np.float64(0.2540152360969511), -0.06600390595331716, np.float64(0.32840962519117206))             |         0.0124 |    0.8576 |
+----+----------------------------------+----------------+-----------------------------------------------------------------------------------------------------+----------------+-----------+
| 39 | Negative affect                  | chi2           | (np.float64(15.273272766724382), np.float64(0.03214360399168904), np.float64(0.0157796723736474))   |         0.0108 |    0.9426 |
+----+----------------------------------+----------------+-----------------------------------------------------------------------------------------------------+----------------+-----------+
# Sentiment Analysis Report
     Country name  year  Life Ladder  Log GDP per capita  ...  Generosity  Perceptions of corruption  Positive affect  Negative affect
0     Afghanistan  2008        3.724               7.350  ...       0.164                      0.882            0.414            0.258
1     Afghanistan  2009        4.402               7.509  ...       0.187                      0.850            0.481            0.237
2     Afghanistan  2010        4.758               7.614  ...       0.118                      0.707            0.517            0.275
3     Afghanistan  2011        3.832               7.581  ...       0.160                      0.731            0.480            0.267
4     Afghanistan  2012        3.783               7.661  ...       0.234                      0.776            0.614            0.268
...           ...   ...          ...                 ...  ...         ...                        ...              ...              ...
2358     Zimbabwe  2019        2.694               7.698  ...      -0.051                      0.831            0.658            0.235
2359     Zimbabwe  2020        3.160               7.596  ...       0.003                      0.789            0.661            0.346
2360     Zimbabwe  2021        3.155               7.657  ...      -0.079                      0.757            0.610            0.242
2361     Zimbabwe  2022        3.296               7.670  ...      -0.073                      0.753            0.641            0.191
2362     Zimbabwe  2023        3.572               7.679  ...      -0.069                      0.757            0.610            0.179

[2363 rows x 11 columns]
