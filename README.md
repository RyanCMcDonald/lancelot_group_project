# <img src="./resources/GA.png" width="25" height="25" />   <span style="color:Purple">Project 5 :  Food Insecurity Regression Study</span> 
---
## <span style="color:Green">Group 1</span>      

#### Alec Edgecliffe-Johnson, Ryan McDonald, Andrew Roberts, Ira Seidman- General Assembly 

---
### Problem Statement
Food insecurity in the United States is a problem faced by communities from a broad spectrum of socioeconomic backgrounds across all fifty states. The present study aims to model a diverse assemblage of economic data collected at the county-level with the express purpose of predicting food insecurity based on these contributing factors. Understanding key economic indicators of food insecurity will help better identify areas in need of food assistance programs, such as food pantries and dietary education centers. Additionally, the modeling process will highlight contributing factors towards food insecurity, so that targeted action at the local level can be undertaken to alleviate the scourge of food insecurity.

   1. A web-app will be developed to allow anyone to access the data

---
## Executive Summary

**After extensive review, EDA, and preprocessing we were able to develop a linear regression model that could account for over 93% of variability in our data. This model was the starting point for our enhanced analysis.  In addition to the production model, a time series analysis was conducted in order to forecast food insecurity rate as well as poverty rates for each of the United States.** 

MORE MORE 
MORE MORE 
MORE MORE

We tested 8 additional models in an attempt to achieve a higher testing score. And, while some were very close or near identical in score, our production model could be run with less computational resources. 

As an added bonus, the link below shows several EDA-based plots and our time series plotted results deployed on our Streamlit Web App, hosted on Heroku!

[Streamlit WebApp Hosted on Herokuapp](https://food-ins-18.herokuapp.com/)


**Summary of methodolgy, production model**
   
   -  various attributes of discussion for model 
        
        -  other models tried...
        
        - something else
        


![a picture](./resources/gui_pic.PNG) 
           
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
|                                               |                                                     | ch_fi_rate_18                                                 | Percent                          |
|                                               |                                                     |                                                               |                                  |

**Data Sources**
###### $_{1}$https://www2.census.gov/programs-surveys/cps/techdocs/cpsmar20.pdf
###### $_{1}$https://map.feedingamerica.org/
###### $_{1}$https://www.countyhealthrankings.org/resources/2019-chr-national-statistics
###### $_{1}$https://www.cdc.gov/data.html

 
### The following databases were utilized in analysis:

| **Database Utilized**            | **Features Within Database**                                     | **Database Utilized**                            | **Features Within Database**           |
|------------------------------|--------------------------------------------------------------|----------------------------------------------|------------------------------------|
| Pandas                       |                                                              | SKLearn - Metrics                            | r2_score, mean_square_error        |
| Numpy                        |                                                              | SKLearn - Impute                             | SinpleImputer, KNNImputer          |
| Matplotlib                   | pyplot                                                       | SKLearn - Neighbors                          | KNeighborsRegressor                |
| Seaborn                      |                                                              | SKLearn - Decomposition                      | PCA                                |
| Copy                         | copy, deepcopy                                               | Tensorflow - Keras - Metris                  | RootMeanSquaredError               |
| pickle                       |                                                              | Tensorflow - Keras - Models                  | Sequential, load_model             |
| nltk - tokenize              | sent-tokenizer, Regexp                                       | Tensorflow - Keras - Layers                  | Dense, Dropout, BatchNormalization |
| nltk - sentiment             | SetimentIntensityAnalyzer                                    | Tensorflow - Keras - Regularizers            | l1, l2, l1_l2                      |
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
|                 |                                                     | FBProphet                                    | Prophet                            |
                                  
---      
### Analysis - TO BE UPDATED!

1. All utilized datasets were cleaned and modified to provide the needed information to complete the problem statement.

 
-

2.  Additional supporting analysis is provided in the code notebook for review, as well as additional insights. Indepth and detailed processing and review are featured throughout the code notebook within markdown and code- formatted lines. 

---
### Conclusions and Recommendations- TO BE UPDATED!!!
   
   