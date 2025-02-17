from altair import Axis
import streamlit as st
import pandas as pd
from  matplotlib import pyplot as plt

import seaborn as sns


@st.cache_data
def load_df():
    data = pd.read_csv("Jewelry_Dataset.csv")
   
    

    return data
data =  load_df()



def show_EDA():
    #st.title ('Exploratory Data Analysis')

    st.write ("""### Jewelry Price Optimization Analysis""")

    

    st.write("""##### Frequency By Gender""")
    
    # Create a figure and axes
    plt.figure(figsize = (12, 8))
    sns.countplot(data = data, x = "Target_Gender")
    plt.xlabel("Gender")
    plt.ylabel("Gender Subpopulation")
    plt.show(); plt.close()

    
     st.write("""##### Jewelry By Category""")
    
    # Category count plot
    plt.figure(figsize = (15, 8))
    sns.countplot(data = real_categories, x = "Category")
    plt.xlabel("Jewelry categories")
    plt.ylabel("Category frequency")
    plt.show(); plt.close()










