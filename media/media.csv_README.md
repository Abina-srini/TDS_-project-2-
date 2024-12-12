# Automated Analysis Report

## Summary
{'columns': ['date', 'language', 'type', 'title', 'by', 'overall', 'quality', 'repeatability'], 'data_types': {'date': 'object', 'language': 'object', 'type': 'object', 'title': 'object', 'by': 'object', 'overall': 'int64', 'quality': 'int64', 'repeatability': 'int64'}, 'missing_values': {'date': 99, 'language': 0, 'type': 0, 'title': 0, 'by': 262, 'overall': 0, 'quality': 0, 'repeatability': 0}, 'summary_stats': {'date': {'count': 2553, 'unique': 2055, 'top': '21-May-06', 'freq': 8, 'mean': nan, 'std': nan, 'min': nan, '25%': nan, '50%': nan, '75%': nan, 'max': nan}, 'language': {'count': 2652, 'unique': 11, 'top': 'English', 'freq': 1306, 'mean': nan, 'std': nan, 'min': nan, '25%': nan, '50%': nan, '75%': nan, 'max': nan}, 'type': {'count': 2652, 'unique': 8, 'top': 'movie', 'freq': 2211, 'mean': nan, 'std': nan, 'min': nan, '25%': nan, '50%': nan, '75%': nan, 'max': nan}, 'title': {'count': 2652, 'unique': 2312, 'top': 'Kanda Naal Mudhal', 'freq': 9, 'mean': nan, 'std': nan, 'min': nan, '25%': nan, '50%': nan, '75%': nan, 'max': nan}, 'by': {'count': 2390, 'unique': 1528, 'top': 'Kiefer Sutherland', 'freq': 48, 'mean': nan, 'std': nan, 'min': nan, '25%': nan, '50%': nan, '75%': nan, 'max': nan}, 'overall': {'count': 2652.0, 'unique': nan, 'top': nan, 'freq': nan, 'mean': 3.0475113122171944, 'std': 0.7621797580962717, 'min': 1.0, '25%': 3.0, '50%': 3.0, '75%': 3.0, 'max': 5.0}, 'quality': {'count': 2652.0, 'unique': nan, 'top': nan, 'freq': nan, 'mean': 3.2092760180995477, 'std': 0.7967426636666686, 'min': 1.0, '25%': 3.0, '50%': 3.0, '75%': 4.0, 'max': 5.0}, 'repeatability': {'count': 2652.0, 'unique': nan, 'top': nan, 'freq': nan, 'mean': 1.4947209653092006, 'std': 0.598289430580212, 'min': 1.0, '25%': 1.0, '50%': 1.0, '75%': 2.0, 'max': 3.0}}, 'datetime_stats': {}, 'shape': (2652, 8)}

## Story
Based on the dataset you've analyzed, here’s a comprehensive narrative about the `'by'` statistic along with a summary of the relevant aspects of the dataset, followed by a brief exploration of time series analysis based on the date column.

### Narrative About `'by'` Statistic

The `'by'` column in your dataset contains information about the creators or contributors associated with the titles, presumably films given the context of the dataset. In this column, there are 2390 recorded entries out of the total 2652 entries, indicating that there are 262 missing values for this attribute. Despite the missing data, a variety of unique contributors is present, with a total of 1528 distinct names noted.

The most frequently appearing contributor is **Kiefer Sutherland**, who appears 48 times. While this figure provides insight into some leading individuals or entities in your dataset, it is essential to consider the distribution of other creators as well. The sheer number of unique contributors suggests that the dataset captures a diverse array of creators, indicative of a rich ecosystem in content production.

Given the missing values for the `'by'` column, it would be prudent to evaluate how the presence or absence of this information influences ratings in the columns `'overall'`, `'quality'`, and `'repeatability'`. One might consider visualizing the average ratings across contributors, potentially identifying key players who contribute to highly rated films.

### Summary of the Dataset

The dataset encompasses a total of **2652 entries and 8 attributes**, with several characteristics:

- **Date**: The entries note dates related to the content, with a total of 2553 non-null entries; 99 entries are missing. There are **2055 unique dates**.
- **Language**: The dataset features films in **11 languages**, predominantly in **English** (1306 occurrences).
- **Type**: All entries categorize as **'movie'** with no variance.
- **Title**: There are **2312 unique titles** in the dataset, suggesting a broad range of content.
- **Ratings**: 
  - **Overall Ratings**: Mean score of approximately **3.05**, with a variety ranging from **1 to 5**.
  - **Quality Ratings**: Mean score stands at approximately **3.21**, also ranging from **1 to 5** indicating a generally favorable reception.
  - **Repeatability**: Average ratings around **1.49**, implying that most titles scored low on repeatability potential, with values dominated by scores of **1** or **2**.

There are no records with the type other than movie and the distribution of the dataset suggests that it may have potential for insightful analysis—particularly in aspects of creator influence (the `'by'` attribute) on the ratings and quality of the content.

### Time Series Analysis

Exploring the `'date'` column reveals opportunities for time series analysis. Although there are missing values for dates (99 entries), it still offers a pathway to evaluate trends over time.

1. **Data Processing**: Convert the `'date'` column from an object to a datetime format to facilitate time-related analysis. For entries with missing dates, you may ignore or fill those accordingly if necessary.
   
2. **Trend Analysis**:
   - Identify the number of movies released over time to spot trends—whether production rates are increasing or decreasing relative to certain timeframes.
   - Plotting these trends using a line chart could illustrate the number of movies released per month/year.

3. **Ratings Over Time**:
   - Calculate the mean rating for each month/year to see if there are significant shifts in overall or quality ratings. This may reveal patterns coinciding with events in the film industry or broader cultural phenomena.

As a result of this analysis, you can derive insights into how the landscape of film outputs and their reception have evolved, and potentially identify periods that were particularly fruitful or challenging for the film industry captured in this dataset.

### Conclusion

Your dataset presents a wealth of information regarding films, their contributors, and audience perceptions through ratings. By diving deeper into the `'by'` statistics and leveraging time series analysis with the `'date'` column, you can unveil compelling narratives regarding the evolution of films and the contributors behind them. Further analysis, particularly on the relationships between ratings and specific contributors, could yield additional insights into collaborations that lead to critical acclaim or popular films.

## Visualizations
![Visualization](media\media.csv_heatmap.png)
![Box Plot](media\media.csv_boxplot.png)
# Profile Report
Data profiling report has been saved as 'media\media.csv_data_profile.html'.
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
