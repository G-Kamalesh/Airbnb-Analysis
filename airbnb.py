import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Airbnb",layout="wide",initial_sidebar_state='collapsed')

if 'key' not in st.session_state:
    st.session_state['key'] = 'Home'

def change():
    if st.session_state['key'] == 'Home':
        st.session_state['key'] = 'Dashboard'
    

options = ['Home','Dashboard']
s = st.sidebar.selectbox("select",options,key = 'key') 
if s == 'Home':

    # Layout using columns
    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("<h1 style='text-align: right; color: red;'>Airbnb</h1>", unsafe_allow_html=True)

    with col2:
        st.image('https://cdn.freebiesupply.com/logos/large/2x/airbnb-2-logo-png-transparent.png', use_column_width=True)

    with col3:
        st.title(":red[Analysis]")

    st.subheader("""Airbnb, Inc. is an American company operating an online marketplace for short- and long-term homestays and experiences.The company acts as a broker and charges a commission from each booking.""")

    st.header("Overview")       
    st.markdown("""This project aims to analyze Airbnb data to uncover insights into pricing variations, availability patterns, and location-based trends.
Using MongoDB Atlas for data storage, Python for data processing, and tools like Streamlit and Tableau for visualization, we will:

**:red[Retrieve and Clean Data]**: Establish a MongoDB connection, import the Airbnb dataset, and clean it by addressing missing values and
duplicates.
            
**:red[Interactive Web Application]**: Develop a Streamlit app with geospatial visualizations to explore listings based on prices, ratings,
and other factors.
            
**:red[Price and Availability Analysis]**: Analyze and visualize price variations and availability patterns across locations and seasons.
            
**:red[Location-Based Insights]**: Extract and visualize data for specific regions to understand neighborhood trends.
            
**:red[Comprehensive Dashboard]**: Create an interactive Tableau dashboard to present key insights.
            
The goal is to provide actionable insights for stakeholders in the travel and property management sectors, enabling data-driven 
decision-making.""")

    st.write("Check this out for Data Preprocessing [click me](https://colab.research.google.com/drive/1kQXaEAETMHD-QgAjQkErOrc4U-PynXQ_?usp=sharing)")


    st.button("Go To Dashboard",on_click=change)

if s == "Dashboard":

    tableau_html = """
<div class='tableauPlaceholder' id='viz1719898012030' style='position: relative'><noscript><a href='#'><img alt='AIRBNB  ANALYSIS  DASHBOARD ' 
src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Ai&#47;AirbnbAnalysis_17197403302300&#47;Dashboard1&#47;1_rss.png' 
style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' 
value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' 
value='3' /> <param name='site_root' value='' /><param name='name' value='AirbnbAnalysis_17197403302300&#47;Dashboard1' /><param name='tabs' 
value='no' /><param name='toolbar' value='yes' /><param name='static_image' 
value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Ai&#47;AirbnbAnalysis_17197403302300&#47;Dashboard1&#47;1.png' /> <param name='animate_transition' 
value='yes' /><param name='display_static_image' 
value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' 
value='yes' /><param name='language' value='en-US' /></object></div>                
<script type='text/javascript'>                    
var divElement = document.getElementById('viz1719898012030');                    
var vizElement = divElement.getElementsByTagName('object')[0];                    
if ( divElement.offsetWidth > 800 ) { vizElement.style.width='1200px';vizElement.style.height='527px';} else if ( divElement.offsetWidth > 500 ) { vizElement.style.width='1200px';vizElement.style.height='527px';} else { vizElement.style.width='100%';vizElement.style.height='1877px';}                     
var scriptElement = document.createElement('script');                    
scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    
vizElement.parentNode.insertBefore(scriptElement, vizElement);                
</script>
"""

    components.html(tableau_html, height=600,width=1400)



