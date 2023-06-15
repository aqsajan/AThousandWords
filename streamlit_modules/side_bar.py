# sidebar.py
import streamlit as st

def show_sidebar(page_options):
    # Add a title to the sidebar
    st.sidebar.title("Thousand Words")

    # Add navigation
    page = st.sidebar.selectbox("Go to", page_options, key="sidebar_selectbox")

    return page

def show_sidebar_1():
    st.sidebar.title("Thousand Words - Page 1")
    # Add a button
    button = st.sidebar.button('Button 1')
    # Add a slider
    slider = st.sidebar.slider('Model Slider', min_value=0, max_value=100, value=50)
    # Add a selectbox
    selectbox = st.sidebar.selectbox('Select Me', ['Option 1', 'Option 2', 'Option 3'])
    return button, slider, selectbox

def show_sidebar_2():
    st.sidebar.title("Thousand Words - Page 2")
    # Add a slider
    slider = st.sidebar.slider('Model Slider', min_value=0, max_value=100, value=50)
    # Add a selectbox
    selectbox = st.sidebar.selectbox('Select Me', ['Option 1', 'Option 2', 'Option 3'])
    return slider, selectbox

def show_sidebar_3():
    st.sidebar.title("Thousand Words - Page 3")
    # Add a button
    button = st.sidebar.button('Button 1')
    return button