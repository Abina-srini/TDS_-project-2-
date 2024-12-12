# Automated Analysis Report

## Summary
{'columns': ['Country name', 'year', 'Life Ladder', 'Log GDP per capita', 'Social support', 'Healthy life expectancy at birth', 'Freedom to make life choices', 'Generosity', 'Perceptions of corruption', 'Positive affect', 'Negative affect'], 'data_types': {'Country name': 'object', 'year': 'int64', 'Life Ladder': 'float64', 'Log GDP per capita': 'float64', 'Social support': 'float64', 'Healthy life expectancy at birth': 'float64', 'Freedom to make life choices': 'float64', 'Generosity': 'float64', 'Perceptions of corruption': 'float64', 'Positive affect': 'float64', 'Negative affect': 'float64'}, 'missing_values': {'Country name': 0, 'year': 0, 'Life Ladder': 0, 'Log GDP per capita': 28, 'Social support': 13, 'Healthy life expectancy at birth': 63, 'Freedom to make life choices': 36, 'Generosity': 81, 'Perceptions of corruption': 125, 'Positive affect': 24, 'Negative affect': 16}, 'summary_stats': {'Country name': {'count': 2363, 'unique': 165, 'top': 'Argentina', 'freq': 18, 'mean': nan, 'std': nan, 'min': nan, '25%': nan, '50%': nan, '75%': nan, 'max': nan}, 'year': {'count': 2363.0, 'unique': nan, 'top': nan, 'freq': nan, 'mean': 2014.7638595006347, 'std': 5.059436468192795, 'min': 2005.0, '25%': 2011.0, '50%': 2015.0, '75%': 2019.0, 'max': 2023.0}, 'Life Ladder': {'count': 2363.0, 'unique': nan, 'top': nan, 'freq': nan, 'mean': 5.483565806178587, 'std': 1.1255215132391925, 'min': 1.281, '25%': 4.647, '50%': 5.449, '75%': 6.3235, 'max': 8.019}, 'Log GDP per capita': {'count': 2335.0, 'unique': nan, 'top': nan, 'freq': nan, 'mean': 9.399671092077089, 'std': 1.1520694444710216, 'min': 5.527, '25%': 8.506499999999999, '50%': 9.503, '75%': 10.3925, 'max': 11.676}, 'Social support': {'count': 2350.0, 'unique': nan, 'top': nan, 'freq': nan, 'mean': 0.8093693617021277, 'std': 0.12121176420299144, 'min': 0.228, '25%': 0.744, '50%': 0.8345, '75%': 0.904, 'max': 0.987}, 'Healthy life expectancy at birth': {'count': 2300.0, 'unique': nan, 'top': nan, 'freq': nan, 'mean': 63.40182826086957, 'std': 6.842644351828009, 'min': 6.72, '25%': 59.195, '50%': 65.1, '75%': 68.5525, 'max': 74.6}, 'Freedom to make life choices': {'count': 2327.0, 'unique': nan, 'top': nan, 'freq': nan, 'mean': 0.750281908036098, 'std': 0.13935703459253465, 'min': 0.228, '25%': 0.661, '50%': 0.771, '75%': 0.862, 'max': 0.985}, 'Generosity': {'count': 2282.0, 'unique': nan, 'top': nan, 'freq': nan, 'mean': 9.772129710780206e-05, 'std': 0.16138760312630687, 'min': -0.34, '25%': -0.112, '50%': -0.022, '75%': 0.09375, 'max': 0.7}, 'Perceptions of corruption': {'count': 2238.0, 'unique': nan, 'top': nan, 'freq': nan, 'mean': 0.7439709562109026, 'std': 0.1848654805936834, 'min': 0.035, '25%': 0.687, '50%': 0.7985, '75%': 0.86775, 'max': 0.983}, 'Positive affect': {'count': 2339.0, 'unique': nan, 'top': nan, 'freq': nan, 'mean': 0.6518820008550662, 'std': 0.10623970474397627, 'min': 0.179, '25%': 0.572, '50%': 0.663, '75%': 0.737, 'max': 0.884}, 'Negative affect': {'count': 2347.0, 'unique': nan, 'top': nan, 'freq': nan, 'mean': 0.27315083084789094, 'std': 0.08713107245795021, 'min': 0.083, '25%': 0.209, '50%': 0.262, '75%': 0.326, 'max': 0.705}}, 'datetime_stats': {}, 'shape': (2363, 11)}

## Story
### Dataset Overview

The dataset consists of 2,363 entries across 11 columns, focusing on various indicators of well-being and quality of life across different countries and years. The columns include measures such as Life Ladder, Log GDP per capita, Social support, Healthy life expectancy at birth, and aspects of affective states, along with perceived corruption and freedom. The data spans from 2005 to 2023.

### Summary Statistics

1. **Life Ladder**:
   - Mean: 5.48
   - Standard Deviation: 1.12
   - Range: 1.281 to 8.019
   - This indicator, which reflects subjective well-being, shows moderate variability across countries and years, with a significant proportion reporting values exceeding the mean.

2. **Log GDP per capita**:
   - Mean: 9.40
   - Standard Deviation: 1.15
   - Range: 5.527 to 11.676
   - This moderately high GDP measure indicates substantial economic diversity, impacting life satisfaction levels.

3. **Social Support**:
   - Mean: 0.81
   - Standard Deviation: 0.12
   - Range: 0.228 to 0.987
   - This metric indicates social connectivity, crucial for individual well-being.

4. **Healthy Life Expectancy at Birth**:
   - Mean: 63.40 years
   - Standard Deviation: 6.84 years
   - Range: 6.72 to 74.6 years
   - This suggests health disparities across countries, reflecting different health systems and lifestyles.

5. **Freedom to Make Life Choices**:
   - Mean: 0.75
   - Standard Deviation: 0.14
   - Range: 0.228 to 0.985
   - This suggests varying degrees of autonomy and choice available to individuals in different countries.

6. **Generosity**:
   - Mean: 0.00009772
   - Standard Deviation: 0.161
   - Range: -0.34 to 0.7
   - This reflects a significant amount of missing data and may indicate variability in charitable actions or perceptions across the dataset.

7. **Perceptions of Corruption**:
   - Mean: 0.74
   - Standard Deviation: 0.18
   - Range: 0.035 to 0.983
   - Higher scores suggest extensive perceived corruption, affecting public satisfaction and governance.

8. **Positive and Negative Affect**:
   - Positive Affect: Mean: 0.65, Range: 0.179 to 0.884
   - Negative Affect: Mean: 0.27, Range: 0.083 to 0.705
   - These metrics gauge emotional states and well-being, showing generally positive moods prevailing against negative feelings.

### Missing Values
The dataset contains several missing values, particularly for Generosity (81), Perceptions of Corruption (125), and Healthy Life Expectancy (63). Careful treatment of these missing values is necessary, as they could bias results.

### Time Series Analysis

The column **year** is identified as a time series variable. Below are insights derived from analyzing the time component of the dataset:

1. **Trends Over Time**: 
   - Analyzing the mean for 'Life Ladder' over the years could indicate improvements in well-being across various nations. Similarly, examining trends for 'Log GDP per capita' might reflect economic growth.
  
2. **Visualizations**:
   - **Line Plot**: A time series plot for each of the metrics (e.g., Life Ladder, GDP per capita) against year would reveal trends, seasonality, or anomalies.
   - Trends may vary by country, and distinct groupings may emerge over time, suggesting differing socioeconomic developments.

3. **Example Findings**:
   - If plotted, one might observe an increasing trend in Life Ladder scores from 2005 to 2023, indicating a potential improvement in global happiness. 
   - An uptick in Log GDP per capita may correlate with increases in Life Ladder during the same years, affirming the relationship between economic stability and subjective well-being.

### Conclusion

The dataset offers intricate insights into the well-being of individuals across various countries and years. Basic analyses reveal the interconnectedness of economic factors and life satisfaction, while time series assessments could further elucidate trends in global development and happiness. Given the missing values, careful data handling and further analysis are advised to yield robust conclusions. Additional analyses like grouping by country or region, and assessing changes, can further guide interpretations and recommendations.

## Visualizations
![Visualization](happiness\happiness.csv_heatmap.png)
![Box Plot](happiness\happiness.csv_boxplot.png)
# Profile Report
Data profiling report has been saved as 'happiness\happiness.csv_data_profile.html'.
# Statistical Analysis Report
{'year': {'norm': {'params': (np.float64(2014.7638595006347), np.float64(5.0583658012739825)), 'ks_statistic': np.float64(0.077713610516844), 'p_value': np.float64(7.366045453363774e-13)}, 'expon': {'params': (2005.0, 9.76385950063468), 'ks_statistic': np.float64(0.21956869217007724), 'p_value': np.float64(1.6108392097120104e-100)}, 'lognorm': {'params': (np.float64(4.905342163702797e-06), -1029180.7023343472, np.float64(1031195.4661814413)), 'ks_statistic': np.float64(0.07771377920618272), 'p_value': np.float64(7.365129569722621e-13)}, 'chi2': {'params': (np.float64(0.5317103439208279), np.float64(2004.9999999999998), np.float64(3.030983199702571)), 'ks_statistic': np.float64(0.742375122894751), 'p_value': np.float64(0.0)}}, 'Life Ladder': {'norm': {'params': (np.float64(5.483565806178587), np.float64(1.125283332829534)), 'ks_statistic': np.float64(0.028366347255268987), 'p_value': np.float64(0.04376701977801023)}, 'expon': {'params': (1.281, 4.202565806178587), 'ks_statistic': np.float64(0.3846388967301102), 'p_value': np.float64(4.941531063e-315)}, 'lognorm': {'params': (np.float64(2.026312231667982e-05), -55528.107398573935, np.float64(55533.59095297922)), 'ks_statistic': np.float64(0.028365386876381016), 'p_value': np.float64(0.0437783215194143)}, 'chi2': {'params': (np.float64(252.6766206197169), np.float64(-7.263741416460022), np.float64(0.050409743562686654)), 'ks_statistic': np.float64(0.033430984974032185), 'p_value': np.float64(0.009933071848146282)}}, 'Log GDP per capita': {'norm': {'params': (np.float64(9.399671092077087), np.float64(1.1518227222400157)), 'ks_statistic': np.float64(0.058384170870676044), 'p_value': np.float64(2.323407732899753e-07)}, 'expon': {'params': (5.527, 3.872671092077087), 'ks_statistic': np.float64(0.3355246108663761), 'p_value': np.float64(6.54343994915213e-235)}, 'lognorm': {'params': (np.float64(1.0788592803768132e-06), -1067620.9690362012, np.float64(1067630.3687066722)), 'ks_statistic': np.float64(0.05838417993558087), 'p_value': np.float64(2.3233962174999797e-07)}, 'chi2': {'params': (np.float64(240.94793065025402), np.float64(-3.571104407317352), np.float64(0.053783014920145096)), 'ks_statistic': np.float64(0.062465980229519436), 'p_value': np.float64(2.3064383740633576e-08)}}, 'Social support': {'norm': {'params': (np.float64(0.8093693617021277), np.float64(0.12118597172175403)), 'ks_statistic': np.float64(0.09391983872489335), 'p_value': np.float64(1.7173484298512432e-18)}, 'expon': {'params': (0.228, 0.5813693617021277), 'ks_statistic': np.float64(0.4044358916868376), 'p_value': np.float64(0.0)}, 'lognorm': {'params': (np.float64(9.47604775027982e-06), -12787.919799347554, np.float64(12788.729168135065)), 'ks_statistic': np.float64(0.09392156572601412), 'p_value': np.float64(1.7147199357568643e-18)}, 'chi2': {'params': (np.float64(566.9482129284302), np.float64(-1.3004663258640763), np.float64(0.0037188680212272797)), 'ks_statistic': np.float64(0.10536157662091178), 'p_value': np.float64(3.606056160119035e-23)}}, 'Healthy life expectancy at birth': {'norm': {'params': (np.float64(63.40182826086956), np.float64(6.841156658723825)), 'ks_statistic': np.float64(0.10798890433884817), 'p_value': np.float64(8.206187105422143e-24)}, 'expon': {'params': (6.72, 56.68182826086956), 'ks_statistic': np.float64(0.5006472245863821), 'p_value': np.float64(0.0)}, 'lognorm': {'params': (np.float64(6.5239067730242576e-06), -1048569.2799999991, np.float64(1048632.6818059443)), 'ks_statistic': np.float64(0.10799011370046036), 'p_value': np.float64(8.196276011939746e-24)}, 'chi2': {'params': (np.float64(491.9210235719588), np.float64(-51.09586576357333), np.float64(0.2328305204870042)), 'ks_statistic': np.float64(0.11297137595360035), 'p_value': np.float64(5.0287223172772027e-26)}}, 'Freedom to make life choices': {'norm': {'params': (np.float64(0.750281908036098), np.float64(0.1393270878779754)), 'ks_statistic': np.float64(0.06181555429702984), 'p_value': np.float64(3.5803048946213744e-08)}, 'expon': {'params': (0.228, 0.522281908036098), 'ks_statistic': np.float64(0.36659671906246083), 'p_value': np.float64(6.710418334101788e-281)}, 'lognorm': {'params': (np.float64(8.503604794052661e-06), -16383.772, np.float64(16384.52228131564)), 'ks_statistic': np.float64(0.06181704699438745), 'p_value': np.float64(3.5772226600501636e-08)}, 'chi2': {'params': (np.float64(374.49523755461473), np.float64(-1.2095260439227289), np.float64(0.005232300454395284)), 'ks_statistic': np.float64(0.07086086446317419), 'p_value': np.float64(1.3215724685108224e-10)}}, 'Generosity': {'norm': {'params': (np.float64(9.772129710779973e-05), np.float64(0.16135223825174483)), 'ks_statistic': np.float64(0.06516451233318199), 'p_value': np.float64(7.212698133051416e-09)}, 'expon': {'params': (-0.34, 0.3400977212971078), 'ks_statistic': np.float64(0.2646724687019688), 'p_value': np.float64(1.3798916339442725e-141)}, 'lognorm': {'params': (np.float64(0.27663079510429456), np.float64(-0.5755934700591047), np.float64(0.5541383767680862)), 'ks_statistic': np.float64(0.012121542439426647), 'p_value': np.float64(0.8865834376621214)}, 'chi2': {'params': (np.float64(0.9266232261106886), np.float64(-0.3400000000000001), np.float64(0.9294721091405682)), 'ks_statistic': np.float64(0.3369626970349996), 'p_value': np.float64(1.2977585901106686e-231)}}, 'Perceptions of corruption': {'norm': {'params': (np.float64(0.7439709562109026), np.float64(0.18482417448645486)), 'ks_statistic': np.float64(0.15005313667044784), 'p_value': np.float64(1.8673208421101766e-44)}, 'expon': {'params': (0.035, 0.7089709562109026), 'ks_statistic': np.float64(0.38883815662487975), 'p_value': np.float64(3.459346655639357e-305)}, 'lognorm': {'params': (np.float64(1.128037870147264e-05), -16383.965, np.float64(16384.708969913743)), 'ks_statistic': np.float64(0.15005545701658413), 'p_value': np.float64(1.861448192123614e-44)}, 'chi2': {'params': (np.float64(239.8859554557386), np.float64(-1.5229030060705315), np.float64(0.009429718125157915)), 'ks_statistic': np.float64(0.17239936017602803), 'p_value': np.float64(1.2386485000192765e-58)}}, 'Positive affect': {'norm': {'params': (np.float64(0.6518820008550662), np.float64(0.1062169918191322)), 'ks_statistic': np.float64(0.06638442496908392), 'p_value': np.float64(2.0925500168646867e-09)}, 'expon': {'params': (0.179, 0.4728820008550662), 'ks_statistic': np.float64(0.41780236288874767), 'p_value': np.float64(0.0)}, 'lognorm': {'params': (np.float64(1.2965231520830616e-05), -8191.820999999995, np.float64(8192.47288131228)), 'ks_statistic': np.float64(0.06638586614739317), 'p_value': np.float64(2.0906722652079894e-09)}, 'chi2': {'params': (np.float64(295.0679926377616), np.float64(-0.6688153086286702), np.float64(0.004471771381193882)), 'ks_statistic': np.float64(0.0749971858391274), 'p_value': np.float64(6.902122968160337e-12)}}, 'Negative affect': {'norm': {'params': (np.float64(0.27315083084789094), np.float64(0.08711250825779107)), 'ks_statistic': np.float64(0.056728232537662016), 'p_value': np.float64(5.250236381485211e-07)}, 'expon': {'params': (0.083, 0.19015083084789092), 'ks_statistic': np.float64(0.2756072623667596), 'p_value': np.float64(4.5689965266252264e-158)}, 'lognorm': {'params': (np.float64(0.2540152360969511), -0.06600390595331716, np.float64(0.32840962519117206)), 'ks_statistic': np.float64(0.012418590836164478), 'p_value': np.float64(0.8575598170389285)}, 'chi2': {'params': (np.float64(15.273272766724382), np.float64(0.03214360399168904), np.float64(0.0157796723736474)), 'ks_statistic': np.float64(0.010843917550634241), 'p_value': np.float64(0.9425510045952572)}}}
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
