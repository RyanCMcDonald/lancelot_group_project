########## Run this code in your terminal to have it hosted on your browser!  In Terminal: 'streamlit run 04_streamlit_code.py' ##########
########## Also hosted live @ https://food-ins-18.herokuapp.com/ ##########

## Code for embedding into in tableau from https://towardsdatascience.com/embedding-tableau-in-streamlit-a9ce290b932b
## Base code from streamlit lesson

import streamlit as st
import streamlit.components.v1 as components
import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st



st.set_page_config(
    page_icon='📖',
    initial_sidebar_state='expanded'
)



page = st.sidebar.selectbox(
    'Page',
    ('Feeding America Visualized', 'Predicting Food Insecurity', 'Food Insecurity Indicators', 'Food Insecurity Time Series Modeling')
)

if page == 'Feeding America Visualized':
    st.title('Feeding America Visualized')
    st.write('''
This website and applet are a representation of our exploration into Food Insecurity in America. In this and subsequent pages we portray Food Insecurity and several related socioeconomic variables at county and state levels for the USA. We also explain the features that have the
largest predictive power in our machine learning models (which can be found on our project's [GitHub](https://github.com/RyanCMcDonald/lancelot_group_project/tree/main).)
    ''')

    st.write('''
In the final page of this web app we display our timeseries
forecasts for Food Insecurity until 2026 which was developed with univariate Prophet and multivariate VAR models, both of which can be found at the project github.
    ''')

    st.subheader('Food Insecurity by County in the USA (2019)')
    st.write('''
Below is a map of Food Insecurity in the US. We can observe greater Food Insecurity values in counties located in the Deep South, parts of Appalachia, and counties in close proximity to Native American reservations.
    ''')

    def main():
        html_temp = """<div class='tableauPlaceholder' id='viz1616862765912' style='position: relative'><noscript><a href='#'><img alt='FI Dash ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Fo&#47;FoodInsecurityInAmerica_16167866065860&#47;FIDash&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='FoodInsecurityInAmerica_16167866065860&#47;FIDash' /><param name='tabs' value='no' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Fo&#47;FoodInsecurityInAmerica_16167866065860&#47;FIDash&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='en' /></object></div>                <script type='text/javascript'>                    var divElement = document.getElementById('viz1616862765912');                    var vizElement = divElement.getElementsByTagName('object')[0];                    if ( divElement.offsetWidth > 800 ) { vizElement.style.minWidth='420px';vizElement.style.maxWidth='1020px';vizElement.style.width='100%';vizElement.style.minHeight='587px';vizElement.style.maxHeight='787px';vizElement.style.height=(divElement.offsetWidth*0.75)+'px';} else if ( divElement.offsetWidth > 500 ) { vizElement.style.minWidth='420px';vizElement.style.maxWidth='1020px';vizElement.style.width='100%';vizElement.style.minHeight='587px';vizElement.style.maxHeight='787px';vizElement.style.height=(divElement.offsetWidth*0.75)+'px';} else { vizElement.style.width='100%';vizElement.style.height='727px';}                     var scriptElement = document.createElement('script');                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                </script>"""
        components.html(html_temp, height = 900, width= 900)
    if __name__ == "__main__":
        main()


    st.subheader('Percent Below Poverty Line by County (2019)')
    st.write('''
Below is a map of percent below the poverty line by county in the USA. Similar trends can be observed as in the above Food Insecurity map. However, areas of extreme proverty appear less widespread than Food Insecurity (zoom out for Alaska and Hawaii).''')

    def main():
        html_temp = """<div class='tableauPlaceholder' id='viz1616957234900' style='position: relative'><noscript><a href='#'><img alt='Pov Dash ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Fo&#47;FoodInsecurityInAmerica_16167866065860&#47;PovDash&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='FoodInsecurityInAmerica_16167866065860&#47;PovDash' /><param name='tabs' value='no' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Fo&#47;FoodInsecurityInAmerica_16167866065860&#47;PovDash&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='en' /><param name='filter' value='publish=yes' /></object></div>                <script type='text/javascript'>                    var divElement = document.getElementById('viz1616957234900');                    var vizElement = divElement.getElementsByTagName('object')[0];                    if ( divElement.offsetWidth > 800 ) { vizElement.style.minWidth='420px';vizElement.style.maxWidth='1020px';vizElement.style.width='100%';vizElement.style.minHeight='587px';vizElement.style.maxHeight='787px';vizElement.style.height=(divElement.offsetWidth*0.75)+'px';} else if ( divElement.offsetWidth > 500 ) { vizElement.style.minWidth='420px';vizElement.style.maxWidth='1020px';vizElement.style.width='100%';vizElement.style.minHeight='587px';vizElement.style.maxHeight='787px';vizElement.style.height=(divElement.offsetWidth*0.75)+'px';} else { vizElement.style.width='100%';vizElement.style.height='727px';}                     var scriptElement = document.createElement('script');                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                </script>"""
        components.html(html_temp, height = 900, width = 900)

    if __name__ == "__main__":
        main()


    st.subheader('Food Insecurity (General Rate and Child Rate) vs Various Factors (2019)')
    st.write('''
Below are plots of food insecurity rate by county in the USA. These scatter plots indicate the general food insecurity rates (in blue) and child food insecurity rates (in orange). The plots show a trend of child based food insecurity increasing at a faster rate than that of general food insecurity.  The data shows children are most at risk with the majority of factors included in our data (percent uninsured, minority, poverty and rural shown below).''')

    def main():
        html_temp = """<div class='tableauPlaceholder' id='viz1616889772153' style='position: relative'><noscript><a href='#'><img alt='Food Insecurity Rate (general and children) Against Various Factors ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Fo&#47;FoodInsecurtiyvsVariousFactors&#47;Dashboard1&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='FoodInsecurtiyvsVariousFactors&#47;Dashboard1' /><param name='tabs' value='no' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Fo&#47;FoodInsecurtiyvsVariousFactors&#47;Dashboard1&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='en' /><param name='filter' value='publish=yes' /></object></div>                <script type='text/javascript'>                    var divElement = document.getElementById('viz1616889772153');                    var vizElement = divElement.getElementsByTagName('object')[0];                    if ( divElement.offsetWidth > 800 ) { vizElement.style.minWidth='420px';vizElement.style.maxWidth='850px';vizElement.style.width='100%';vizElement.style.minHeight='587px';vizElement.style.maxHeight='1087px';vizElement.style.height=(divElement.offsetWidth*0.75)+'px';} else if ( divElement.offsetWidth > 500 ) { vizElement.style.minWidth='420px';vizElement.style.maxWidth='850px';vizElement.style.width='100%';vizElement.style.minHeight='587px';vizElement.style.maxHeight='1087px';vizElement.style.height=(divElement.offsetWidth*0.75)+'px';} else { vizElement.style.width='100%';vizElement.style.height='1277px';}                     var scriptElement = document.createElement('script');                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                </script>"""
        components.html(html_temp, height = 1100, width = 900)

    if __name__ == "__main__":
        main()

    st.subheader('Historical Food Insecurity by State')
    st.write('''
The below map displays actual average Food Insecurity by state through time. Covering a period of 2010-2019, we see a general trend of many southeastern US states having relatively higher food insecurity than other parts of the country (zoom out for Alaska and Hawaii).
    ''')

    def main():
        html_temp = """<div class='tableauPlaceholder' id='viz1616863130052' style='position: relative'><noscript><a href='#'><img alt='Dashboard 1 ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;K3&#47;K3M4KSW3R&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='path' value='shared&#47;K3M4KSW3R' /> <param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;K3&#47;K3M4KSW3R&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='en' /><param name='filter' value='publish=yes' /></object></div>                <script type='text/javascript'>                    var divElement = document.getElementById('viz1616863130052');                    var vizElement = divElement.getElementsByTagName('object')[0];                    if ( divElement.offsetWidth > 800 ) { vizElement.style.minWidth='420px';vizElement.style.maxWidth='1020px';vizElement.style.width='100%';vizElement.style.minHeight='587px';vizElement.style.maxHeight='787px';vizElement.style.height=(divElement.offsetWidth*0.75)+'px';} else if ( divElement.offsetWidth > 500 ) { vizElement.style.minWidth='420px';vizElement.style.maxWidth='1020px';vizElement.style.width='100%';vizElement.style.minHeight='587px';vizElement.style.maxHeight='787px';vizElement.style.height=(divElement.offsetWidth*0.75)+'px';} else { vizElement.style.width='100%';vizElement.style.height='727px';}                     var scriptElement = document.createElement('script');                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                </script>"""
        components.html(html_temp, height = 900, width = 900)
    if __name__ == "__main__":
        main()


elif page == 'Predicting Food Insecurity':
    st.title('Predicting Food Insecurity')
    st.subheader('Socioeconomic factors associated with Food Insecurity')
    st.write('''
Our production machine learning model, which employed over 50 features and captured 93.5% of the variability of the data, shows that, all else held equal,
a one-unit increase in each of these features would result in an increase in Food Insecurity of the amount indicated in the graph below.''')

    def main():
        html_temp = """<div class='tableauPlaceholder' id='viz1616866672368' style='position: relative'><noscript><a href='#'><img alt='Dashboard 1 ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;LR&#47;LRFeatureCoef&#47;Dashboard1&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='LRFeatureCoef&#47;Dashboard1' /><param name='tabs' value='no' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;LR&#47;LRFeatureCoef&#47;Dashboard1&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='en' /><param name='filter' value='publish=yes' /></object></div>                <script type='text/javascript'>                    var divElement = document.getElementById('viz1616866672368');                    var vizElement = divElement.getElementsByTagName('object')[0];                    vizElement.style.width='720px';vizElement.style.height='587px';                    var scriptElement = document.createElement('script');                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                </script>"""
        components.html(html_temp, height = 900, width = 900)
    if __name__ == "__main__":
        main()

elif page == 'Food Insecurity Indicators':
    st.title('Food Insecurity Indicators')
    st.subheader('Socioeconomic factors associated with Food Insecurity')
    st.write('''
A variety of factors contribute to food insecurity in a given community. Factors such as income, employment, access to healthcare, and education are just a few factors at play in affecting one's access to food. The below visualizations depict Food Insecurity vs. formal education for each state in the overlying map with median household income depicted in the bar graph below.
    ''')

    def main():
        html_temp = """<div class='tableauPlaceholder' id='viz1616967718434' style='position: relative'><noscript><a href='#'><img alt='Dashboard 1 ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;St&#47;State_Based_FI_Rate&#47;Dashboard1&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='State_Based_FI_Rate&#47;Dashboard1' /><param name='tabs' value='no' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;St&#47;State_Based_FI_Rate&#47;Dashboard1&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='en' /><param name='filter' value='publish=yes' /></object></div>                <script type='text/javascript'>                    var divElement = document.getElementById('viz1616967718434');                    var vizElement = divElement.getElementsByTagName('object')[0];                    vizElement.style.minWidth='420px';vizElement.style.maxWidth='1020px';vizElement.style.width='100%';vizElement.style.minHeight='587px';vizElement.style.maxHeight='787px';vizElement.style.height=(divElement.offsetWidth*0.75)+'px';                    var scriptElement = document.createElement('script');                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                </script>"""
        components.html(html_temp, height = 900, width = 900)
    if __name__ == "__main__":
        main()


elif page == 'Food Insecurity Time Series Modeling':
    st.title('Food Insecurity Time Series Modeling')
    st.subheader('Modeling Food Insecurity in the United States (2010-2026)')

    st.write('''
The Facebook Prophet univariate time series model was utilized to forecast Food Insecurity by state five years into the future.     ''')

    def main():
        html_temp = """<div class='tableauPlaceholder' id='viz1616870027946' style='position: relative'><noscript><a href='#'><img alt='Dashboard 2 ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;St&#47;StateFoodInsecurityPredictionsMap_ar&#47;Dashboard2&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='StateFoodInsecurityPredictionsMap_ar&#47;Dashboard2' /><param name='tabs' value='no' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;St&#47;StateFoodInsecurityPredictionsMap_ar&#47;Dashboard2&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='en' /><param name='filter' value='publish=yes' /></object></div>                <script type='text/javascript'>                    var divElement = document.getElementById('viz1616870027946');                    var vizElement = divElement.getElementsByTagName('object')[0];                    vizElement.style.minWidth='420px';vizElement.style.maxWidth='1020px';vizElement.style.width='100%';vizElement.style.minHeight='587px';vizElement.style.maxHeight='787px';vizElement.style.height=(divElement.offsetWidth*0.75)+'px';                    var scriptElement = document.createElement('script');                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                </script>"""
        components.html(html_temp, height = 900, width = 900)
    if __name__ == "__main__":
        main()


        st.subheader('Food Insecurity through Time')
        st.write('''
Below is a line graph of Food Insecurity. The upper line graph reflects the actual training data containing Food Insecurity values by state as provided by Feeding America. The lower line graph reflects the Facebook Prophet model used to forecast Food Insecurity five years into the future.    ''')

    def main():
        html_temp = """<div class='tableauPlaceholder' id='viz1616869802759' style='position: relative'><noscript><a href='#'><img alt='Dashboard 2 (2) ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;St&#47;StateFoodInsecurityPredictions_ar&#47;Dashboard22&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='StateFoodInsecurityPredictions_ar&#47;Dashboard22' /><param name='tabs' value='no' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;St&#47;StateFoodInsecurityPredictions_ar&#47;Dashboard22&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='en' /><param name='filter' value='publish=yes' /></object></div>                <script type='text/javascript'>                    var divElement = document.getElementById('viz1616869802759');                    var vizElement = divElement.getElementsByTagName('object')[0];                    vizElement.style.minWidth='420px';vizElement.style.maxWidth='1020px';vizElement.style.width='100%';vizElement.style.minHeight='587px';vizElement.style.maxHeight='787px';vizElement.style.height=(divElement.offsetWidth*0.75)+'px';                    var scriptElement = document.createElement('script');                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                </script>"""
        components.html(html_temp, height = 900, width = 900)
    if __name__ == "__main__":
        main()

        st.subheader('Multivariate Timeseries Model of Food Insecurity')
        st.write('''
The map below reflects a multivariate time series model forecasting Food Insecurity utilizing time, historic Food Insecurity rates, and historic poverty rates by state.     ''')

    def main():
        html_temp = """<div class='tableauPlaceholder' id='viz1616876252569' style='position: relative'><noscript><a href='#'><img alt='Dashboard 3 ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;St&#47;StateFoodInsecurityPredictionsMap_ar&#47;Dashboard3&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='StateFoodInsecurityPredictionsMap_ar&#47;Dashboard3' /><param name='tabs' value='no' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;St&#47;StateFoodInsecurityPredictionsMap_ar&#47;Dashboard3&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='en' /><param name='filter' value='publish=yes' /></object></div>                <script type='text/javascript'>                    var divElement = document.getElementById('viz1616876252569');                    var vizElement = divElement.getElementsByTagName('object')[0];                    vizElement.style.minWidth='420px';vizElement.style.maxWidth='1020px';vizElement.style.width='100%';vizElement.style.minHeight='587px';vizElement.style.maxHeight='787px';vizElement.style.height=(divElement.offsetWidth*0.75)+'px';                    var scriptElement = document.createElement('script');                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                </script>"""
        components.html(html_temp, height = 900, width = 900)
    if __name__ == "__main__":
        main()
