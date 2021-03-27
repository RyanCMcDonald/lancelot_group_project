## Code for embedding into in tableau from https://towardsdatascience.com/embedding-tableau-in-streamlit-a9ce290b932b
## Base code from streamlit lesson

import streamlit as st
import streamlit.components.v1 as components
import matplotlib.pyplot as plt
import pandas as pd
import pickle
import streamlit as st
from nltk.sentiment.vader import SentimentIntensityAnalyzer


st.set_page_config(
    page_icon='📖',
    initial_sidebar_state='expanded'
)

st.title('Food Insecurity in the USA')

st.write('Use the sidebar to select a page to view.')

page = st.sidebar.selectbox(
    'Page',
    ('About our Project', 'Data 2018', 'Time Series Data')
)

if page == 'About our Project':
    st.subheader('Food Insecurity in the USA')
    st.write('''
This is where we describe the project and motivation for exploring food insecurity.
    ''')

    def main():
        html_temp = """<div class='tableauPlaceholder' id='viz1616344445485' style='position: relative'><noscript><a href='#'><img alt=' ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Fo&#47;FoodInsecurityInAmerica&#47;FoodInsecurity&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='path' value='views&#47;FoodInsecurityInAmerica&#47;FoodInsecurity?:language=en&amp;:embed=y&amp;:display_count=y' /> <param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Fo&#47;FoodInsecurityInAmerica&#47;FoodInsecurity&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='en' /></object></div>                <script type='text/javascript'>                    var divElement = document.getElementById('viz1616344445485');                    var vizElement = divElement.getElementsByTagName('object')[0];                    vizElement.style.width='100%';vizElement.style.height=(divElement.offsetWidth*0.75)+'px';                    var scriptElement = document.createElement('script');                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                </script>"""
        components.html(html_temp, height = 700)
    if __name__ == "__main__":    
        main()

    st.subheader('Poverty in the USA')
    st.write('''
And here is another incredibly interesting visualization.
    ''')

    def main():
        html_temp = """<div class='tableauPlaceholder' id='viz1616344445485' style='position: relative'><noscript><a href='#'><img alt=' ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Fo&#47;FoodInsecurityInAmerica&#47;FoodInsecurity&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='path' value='views&#47;FoodInsecurityInAmerica&#47;FoodInsecurity?:language=en&amp;:embed=y&amp;:display_count=y' /> <param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Fo&#47;FoodInsecurityInAmerica&#47;FoodInsecurity&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='en' /></object></div>                <script type='text/javascript'>                    var divElement = document.getElementById('viz1616344445485');                    var vizElement = divElement.getElementsByTagName('object')[0];                    vizElement.style.width='100%';vizElement.style.height=(divElement.offsetWidth*0.75)+'px';                    var scriptElement = document.createElement('script');                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                </script>"""
        components.html(html_temp, height = 700)
    if __name__ == "__main__":    
        main()


elif page == 'Data 2018':
    st.subheader('Data 2018: Visualizing Socio-Economics and Health in the USA')

    st.write('''
Below you'll find interactive visualizations of many different socio-economic and health features on a county-by-bounty basis for the USA.
    ''')

    def main():
        html_temp = """<div class='tableauPlaceholder' id='viz1616344445485' style='position: relative'><noscript><a href='#'><img alt=' ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Fo&#47;FoodInsecurityInAmerica&#47;FoodInsecurity&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='path' value='views&#47;FoodInsecurityInAmerica&#47;FoodInsecurity?:language=en&amp;:embed=y&amp;:display_count=y' /> <param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Fo&#47;FoodInsecurityInAmerica&#47;FoodInsecurity&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='en' /></object></div>                <script type='text/javascript'>                    var divElement = document.getElementById('viz1616344445485');                    var vizElement = divElement.getElementsByTagName('object')[0];                    vizElement.style.width='100%';vizElement.style.height=(divElement.offsetWidth*0.75)+'px';                    var scriptElement = document.createElement('script');                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                </script>"""
        components.html(html_temp, height = 700)
    if __name__ == "__main__":    
        main()

elif page == 'Time Series Data':
    st.subheader('Data through the ages')

    st.write('''
Interact with the visualizations below to get a better sense of data through the ages.
    ''')

    def main():
        html_temp = """<div class='tableauPlaceholder' id='viz1616344445485' style='position: relative'><noscript><a href='#'><img alt=' ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Fo&#47;FoodInsecurityInAmerica&#47;FoodInsecurity&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='path' value='views&#47;FoodInsecurityInAmerica&#47;FoodInsecurity?:language=en&amp;:embed=y&amp;:display_count=y' /> <param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Fo&#47;FoodInsecurityInAmerica&#47;FoodInsecurity&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='en' /></object></div>                <script type='text/javascript'>                    var divElement = document.getElementById('viz1616344445485');                    var vizElement = divElement.getElementsByTagName('object')[0];                    vizElement.style.width='100%';vizElement.style.height=(divElement.offsetWidth*0.75)+'px';                    var scriptElement = document.createElement('script');                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                </script>"""
        components.html(html_temp, height = 700)
    if __name__ == "__main__":    
        main()