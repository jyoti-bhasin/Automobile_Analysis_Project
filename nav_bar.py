import streamlit as st
import pandas as pd
from streamlit_option_menu import option_menu

def navigation_options():
    selected_option = option_menu(
        menu_title=None,
        options=['Home', 'Explore', 'About'],
        icons=['house', 'book',''],
        menu_icon='cast',
        default_index=0,
        orientation='horizontal',
    )
    return selected_option
