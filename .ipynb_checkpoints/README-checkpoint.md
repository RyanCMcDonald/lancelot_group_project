<<<<<<< HEAD
# lancelot_group_project

We�ll figure this stuff out
UPDATING README FILE WITH RANDOM SENTENCE
=======
# <img src="./resources/GA.png" width="25" height="25" />   <span style="color:Purple">Project 5 :  Food Insecurity Regression Study</span> 
---
## <span style="color:Green">Group 1</span>      

#### Alec Edgecliffe-Johnson, Ryan McDonald, Andrew Roberts, Ira Seidman- General Assembly 

---
### Problem Statement
Food insecurity in the United States is a problem faced by communities from a broad spectrum of socioeconomic backgrounds across all fifty states. The present study aims to model a diverse assemblage of economic data collected at the county-level with the express purpose of predicting food insecurity based on these contributing factors. Understanding key economic indicators of food insecurity will help better identify areas in need of food assistance programs, such as food pantries and dietary education centers. Additionally, the modeling process will highlight contributing factors towards food insecurity, so that targeted action at the local level can be undertaken to alleviate the scourge of food insecurity.

A web-app will be developed to allow anyone to access the data

---
## Executive Summary

**After extensive review, EDA, and preprocessing we were able to develop a linear regression model that could account for over 93% of variability in our data. This model was the starting point for our enhanced analysis. In addition to the production model, a time series analysis was conducted in order to forecast food insecurity rate as well as poverty rates for each state in America.** 

The information gained from our analysis could be used to better allocate resources to the areas that need it most. Although overall our forecasts show food insecurity decreasing in the majority of states, areas of the deep south as well as New Mexico and Utah may face persistent problems in the years to come. 

We did extensive EDA work to understand the relationship between the 60+ features in our dataset. Some of the more intuitive relevant findings are the degree to which poverty and food insecurity are correlated and the ways in which other indicators of health and nutrition are related to food insecurity. We also found less intuitive connections, like the correlation between being black and having children with a lower birth weight. 

In our modeling phase, we tested eight models in addition to our production model in an attempt to achieve a higher testing score. And, while some were very close or near identical in score, our production model provided the best mix of testing score, fit and use of computational resources. According to the model, the three predictors with the highest coefficients were the percent of the population that was disabled, percent of children in poverty and percent with fair or poor health. 

Our initial univariate time series model was an Arima model developed on 10 years of state-level food insecurity data. The model basically predicted the mean for the next seven years. This was later enhanced with an Auto-Arima model and finally a Prophet model, the latter of which performed extremely well in comparison to the actual data over the period in question (2010-2019) and generated clear forecasts for the following seven years. 

Our multivariate time series model was a Vector Autoregressive model developed on 10 years of state-level food insecurity and 10 years of poverty data. The model performed very well in comparison to the actual data for the time period for both variables and generated predictions for the next seven years. The output of our time series models (univariate and multivariate) indicates persistent food insecurity issues in many states in the deep south as well as several states in the southwest/west including New Mexico and Utah.


The link below shows several EDA-based plots and the group's time series plotd deployed on a Streamlit Web App, hosted on Heroku!

[Streamlit WebApp Hosted on Herokuapp](https://food-ins-18.herokuapp.com/)


## Analysis

Initial exploratory data analysis was methodical.  Review of all features was conducted to better understand the data and which features contributed most to food insecurity.  Once the initial analysis was completed, modeling began. 
   
   - For some models, all features were utilized and for others,  only subsets of features (those deemed most influential to food insecurity) were used.  This helped us better understand the influences our features had on our results.
    
   - Our production model utilized all numerical features from our primary data set, netting our strongest results, while being the most interpretable. Quick run times also helped with out decision. 

The EDA shows that childhood food insecurity rates are much higher and that certain states in the south and west suffer from higher food insecurity than average. When investigating which indicators are the strongest predictors for food insecurity; income, employment, access to healthcare, and education are just a few of the leading features. Group One’s Tableau visualizations of Food Insecurity vs. Formal Education and Median Household Income show how education levels and income definitely correlate with food insecurity. Finally, the time series predictions show food insecurity rates generally decreasing through the USA, but certain states like Louisiana, Mississippi, Arkansas, New Mexico, and Utah will still have higher than average food insecurity in the coming years.

**A representation of our forcasted MultiVariate Time Series Model is shown below.**

![VAR excerpt](./resources/var_excerpt.png) 
           
---
### Data Description
Data utilized for the project analysis was obtained through a variety of sources, including the CDC, Feeding America, County Heath Rankings, Census.gov and others.  There were over a dozen different data sources that were reviewed, cleaned, and formatted in order to be combined into one primary data source for our project.  In addition to our primary dataset, many smaller ones were developed for various EDA and modeling needs through the notebook. 
Our primary dataset contained 60 features (of varying data types) and 3140 entries (representing each county in the United States).


**Data Dictionary created for datasets utilized in this analysis**

| Feature Name                                  | Description                                         | Feature Name                                                  | Description                      |
|-----------------------------------------------|-----------------------------------------------------|---------------------------------------------------------------|----------------------------------|
| fips                                          | Federal Information Processing Series Code          | percent_enrolled_in_free_or_reduced_lunch                     | Percent                          |
| state_name                                    | Name                                                | percent_homeowners                                            | Percent                          |
| county                                        | County Name                                         | percent_65_and_over                                           | Percent                          |
| lat                                           | Latitude Ordinate                                   | percent_black                                                 | Percent                          |
| lon                                           | Longitude Ordinate                                  | percent_american_indian_alaska_native                         | Percent                          |
| total_population                              | Number                                              | percent_asian                                                 | Percent                          |
| area_sqmi                                     | Sq-Mi Area of County                                | percent_native_hawaiian_other_pacific_islander                | Percent                          |
| population_density_per_sqmi                   | Number / SqMi                                       | percent_hispanic                                              | Percent                          |
| percent_fair_or_poor_health                   | Percentage                                          | percent_non_hispanic_white                                    | Percent                          |
| average_number_of_mentally_unhealthy_days     | Ave Days /Month of Stress/Depression/Etc.           | percent_not_proficient_in_english                             | Percent                          |
| percent_low_birthweight                       | Percent Less Than 5lb, 8oz at Birth                 | percent_female                                                | Percent                          |
| percent_smokers                               | Percent                                             | percent_rural                                                 | Percent                          |
| percent_adults_with_obesity                   | Percent Above BMI = 30                              | per_capita_income                                             | Number                           |
| food_environment_index                        | 0-10(best) Ability to and Access to Food            | percent_below_poverty                                         | Percent                          |
| percent_physically_inactive                   | Percent Not Participating in Leisure Activities     | percent_unemployed_CDC                                        | Percent                          |
| percent_with_access_to_exercise_opportunities | Percent Within Reasonable Proximity to Exercise     | percent_no_highschool_diploma                                 | Percent                          |
| percent_uninsured                             | Percent                                             | percent_age_17_and_younger                                    | Percent                          |
| primary_care_physicians_rate                  | Ratio (County Pop./# PCP)                           | percent_disabled                                              | Percent                          |
| high_school_graduation_rate                   | Ratio                                               | percent_minorities                                            | Percent                          |
| percent_children_in_poverty                   | Percent                                             | percent_limited_english_abilities                             | Percent                          |
| num_households_CHR                            | # Households in County                              | percentile_rank_social_vulnerability                          | Percentile Disaster Preparedness |
| percent_single_parent_households_CHR          | Percent                                             | pct_overall_pov_19                                            | Percent                          |
| violent_crime_rate                            | # Violent Crimes/100,000 Pop.                       | cpm_18                                                        | Average Cost Per Meal            |
| percent_severe_housing_problems               | Percent Without Adequate Housing Features           | state_abr                                                     | 2 Letter State Abbr.             |
| severe_housing_cost_burden                    | Percent Pop. With > 50% Income Utilized for Housing | percent_of_adults_with_less_than_high_school_diploma          | Percent                          |
| life_expectancy                               | Number                                              | percent_of_adults_with_high_school_diploma_only               | Percent                          |
| percent_adults_with_diabetes                  | Percent                                             | percent_of_adults_completing_some_college_or_associate_degree | Percent                          |
| percent_limited_access_to_healthy_foods       | Percent With Limited Access to Grocery Stores       | percent_of_adults_with_bachelor_degree_or_higher              | Percent                          |
| median_household_income                       | Number                                              | fi_rate_18                                                    | Percent                          |
| ch_fi_rate_18                                 | Percent                                             | 


**Data Sources**
###### https://www2.census.gov/programs-surveys/cps/techdocs/cpsmar20.pdf
###### https://map.feedingamerica.org/
###### https://www.countyhealthrankings.org/resources/2019-chr-national-statistics
###### https://www.cdc.gov/data.html

 
### The following databases were utilized in analysis:

| **Database Utilized**            | **Features Within Database**                                     | **Database Utilized**                            | **Features Within Database**           |
|------------------------------|--------------------------------------------------------------|----------------------------------------------|------------------------------------|
| Pandas                       |                                                              | SKLearn - Metrics                            | r2_score, mean_square_error        |
| Numpy                        |                                                              | SKLearn - Impute                             | SinpleImputer, KNNImputer          |
| Matplotlib                   | pyplot                                                       | SKLearn - Neighbors                          | KNeighborsRegressor                |
| Seaborn                      |                                                              | SKLearn - Decomposition                      | PCA                                |
| Copy                         | copy, deepcopy                                               | Tensorflow - Keras - Metris                  | RootMeanSquaredError               |
| FBProphet                    | Prophet                                                      | Tensorflow - Keras - Models                  | Sequential, load_model             |
| nltk - tokenize              | sent-tokenizer, Regexp                                       | Tensorflow - Keras - Layers                  | Dense, Dropout, BatchNormalization |
| nltk - sentiment             | SetimentIntensityAnalyzer                                    | Tensorflow - Keras - Regularizers            | l2                      |
| time                         |                                                              | Tensorflow - Keras - Callbacks               | EarlyStopping                      |
| xgboost                      | XGBClassifier                                                | Tensorflow - Keras - Wrappers - Scikit_learn | KerasRegressor                     |
| SKLearn - Model Selection    | train_test_split, GridSearchCV, corr_val_score               | Tensorflow - Keras - Utils                   | plot_model                         |
| SKLearn - Pipeline           | Pipeline                                                     | Streamlit                                    |                                    |
| SKLearn - Preprocessing         | StardardScalar, PolynomialFeatures                                   | Streamlit - Components - v1                  |                                    |
| SKLearn - Linear Model       | LogisticRegression, LassoCV                                  | Datetime                                     |                                    |
| SKLearn - SVM | LinearSVC                             | Statsmodels - TSA - ARIMA - Model            | ARIMA                              |
| SKLearn - Ensemble           | RandomForestRegressor,  AdaBoostRegressor, BaggingRegressor | Statsmodels - TSA - Vector_AR - Var_Model    | VAR                                |
| SKLearn - Tree               | DecisionTreeRegressor, plot_tree                             | PMARIMA                                      |                                    |
| SKLearn - SVR                | SVR                                                          | PMARIMA - Model_selection                    | train-test-split                   |

---
### Conclusions and Recommendations

Food insecurity is a challenge faced by many Americans due to a wide array of contributing factors. The above analysis incorporated a variety of machine learning algorithms to best capture the influence of these factors for predicting food insecurity at the county level across the United States. Ultimately, a linear regression was the best performing model and could account for 93% of the variability in our data. This production model identified disability rates, child poverty rates, fair/poor health rates, and housing-related issues as the greatest contributing factors towards food insecurity. To reduce food insecurity, it is our recommendation that public policy be framed such that these issues be alleviated to the greatest extent possible by targeting these areas of highest correlation and further exploring the extent of causative relationships.  

Additionally, time series modeling at the state level demonstrates the extent to which food insecurity will evolve going forward based on past trends. This enables the identification of locations where communities are at greatest risk of continued or worsening food insecurity. With this information in mind, policy can be guided to best allocate resources to areas in need of assistance. Our time series modeling suggests that areas in the Deep South and several states in the West, including New Mexico and Utah, will continue to experience food insecurity challenges, which warrants further investigation to better understand contributing causes and potential solutions.

   
>>>>>>> upstream/main
