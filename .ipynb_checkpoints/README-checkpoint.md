# <img src="./resources/GA.png" width="25" height="25" />   <span style="color:Purple">Project 5 :  Food Insecurity Regression Study</span> 
---
## <span style="color:Green">Group 1</span>      

#### Alec Edgecliffe-Johnson, Ryan McDonald, Andrew Roberts, Ira Seidman- General Assembly 

---
### Problem Statement
Food insecurity in the United States is a problem faced by communities from a broad spectrum of socioeconomic backgrounds across all fifty states. The present study aims to model a diverse assemblage of economic data collected at the county-level with the express purpose of predicting food insecurity based on these contributing factors. Understanding key economic indicators of food insecurity will help better identify areas in need of food assistance programs, such as food pantries and dietary education centers. Additionally, the modeling process will highlight contributing factors towards food insecurity, so that targeted action at the local level can be undertaken alleviate the scourge of food insecurity.

   1. Some actionable use of the model
   2. Some other use/ application?
       * Try it for the UK? 
       * mention of an app/etc? 
###### $_{1}$https://sources
###### $_{1}$https://sources


 ---
## Executive Summary
**Sumamry of methodolgy, production model**
   
   -  various attributes of discussion for model 
        
        -  other models tried...
        
        - something else
        
**streamlit/ tabluea thingy?**

![a picture](./resources/gui_pic.PNG) 
           
---
### Data Description
Data utilized for the project analysis was obtained through.... a bunch of places.. 

Dataset contains X columns.  dataset size....

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

 
**(TO BE UPDATED) The following databases were utilized in analysis:**

| Database Utilized            | Features Within Database                                         |
|------------------------------|------------------------------------------------------------------|
| Pandas                       |                                                                  |
| Numpy                        |                                                                  |
| matplotlib                   | pyplot                                                           |
| pickle                       |                                                                  |
| nltk - tokenize              | sent-tokenizer, Regexp                                           |
| nltk - sentiment             | SetimentIntensityAnalyzer                                        |
| time                         |                                                                  |
| xgboost                      | XGBClassifier                                                    |
| SKLearn - Model Selection    | train_test_split, GridSearchCV, corr_val_score                   |
| SKLearn - Pipeline           | Pipeline                                                         |
| SKLearn - Naive-bayes        | MultinomialNB, BernoulliNB                                       |
| SKLearn - Linear Model       | LogisticRegression, LogisticRegressionCV                         |
| SKLearn - Feature Extraction | CountVectorizer, TfidfVectorizer                                 |
| SKLearn - Ensemble           | RandomForestClassifier, ExtraTreesClassifier, AdaBoostClassifier |
| SKLearn - Tree               | export_text, DecisionTreeClassifier, plot_tree                   |
| SKLearn - SVM                | LinearSVC                                                        |
| SKLearn - Metrics            | confusion_matrix, plot_confusion_matrix                          |
| tkinter                      | simpledialog                                                     |

---      
### Analysis - TO BE UPDATED!

1. All utilized datasets were cleaned and modified to provide the needed information to complete the problem statement.
2. Additional subreddits were utilized to further test our production model on unseen data.
  
  -  Sentiment Analysis was conducted as a precurser to modeling to help identify any correlations between the two intially chosen subreddits (r/VanLife and r/camping)
      ![another pic](./resources/sentiment_table.JPG)
  
  -  The variety of techniques utilized throughout our model preparations are shown below, with our Production Model parameters off on the side. Our production model baseline performance on r/VanLife and r/camping were 97% on training data, 87.6% on testing data.  An overfit model, but that was not our concern for this project, with testing results taking the win.
      ![another pic](./resources/model_params.JPG)

   -  Our model's performance on several different pairs of subreddits with varying similarities (low score indicates material within subreddits cannot be distiguished independantly... they are too similar.  High scoring results indicate subreddit pairs have very different content.)
      ![another pic](./resources/follow_up_performance.PNG) 


 
-

3.  Additional supporting analysis is provided in the code notebook for review, as well as additional insights. Indepth and detailed processing and review are featured throughout the code notebook within markdown and code- formatted lines. 

---
### Conclusions and Recommendations- TO BE UPDATED!!!
   
   -  Our Production Model is a success!  We, at Reddit, are looking forward to releasing this hijinks to unsuspecting Reddit users on April 1st. The model performed as well as we could have hoped, weeding out similar subreddits and promoting others as ‘unique’
 
     
   -  Although, lighthearted from the beginning, we understand this model can be utilized for many more great things here, at Reddit.  We look forward to applying classification modeling for better predictive advertising, product deals with merchants, and to enhance the user experience all together.  For now, though, we will be monitoring users on April Fools' to see how everyone reacts, and are looking forward to putting together our 2022 ideas to work soon!

  