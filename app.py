import numpy

from collections import Counter
import nav_bar
# for mathematical computation
import streamlit as st
import numpy as np
import pandas as pd

st.set_page_config(page_title="Analysis")

#for price_prediction
import price_prediction
from price_prediction import get_linear_prediction
import price_prediction3
from price_prediction3 import get_svm_prediction

#for news
import getting_news
from getting_news import get_news

#for web scraping
import web_scrap

import pickle
import pickle_mixin

# for data visualization

import seaborn as sns
import matplotlib.pyplot as plt
import plotly
import plotly.express as px
from matplotlib.pyplot import figure

#testing login

hide_menu_style = """
        <style>
        #MainMenu {visibility: hidden; }
        footer {visibility: hidden; }
        </style>
        """
st.markdown(hide_menu_style,unsafe_allow_html=True)


dt = pd.read_csv(r"Book2.csv")
pd.set_option('display.max_rows', None)
print(dt.head())
# print(dt[dt.isnull()].count())
# print(dt[dt.duplicated()].count())
dt = dt.replace(' ', '')

#customer segment commands
import customer_seg
from customer_seg import get_customer_seg

print(type(dt))
import plost


from nav_bar import navigation_options

a1 = navigation_options()


if a1 == 'Home':
    st.markdown(f"<h1 style='background-color:#F6CEEC;'> 📊 AUTOMOBILE DATA ANALYSIS </h1>", unsafe_allow_html=True)
    st.image("pexels-pixabay-164634.jpg", width=400)
    st.markdown("All those companies and activities involved in the manufacture of motor vehicles,"
            " including most components, such as engines and bodies, but excluding tires, batteries, and fuel. "
            " The industry’s principal products are passenger automobiles and light trucks, including pickups, vans, and sport utility vehicles."
            " The history of the automobile industry, though brief compared with that of many other industries, has exceptional interest because of its effects on history from the 20th century."
            "\n\n Lets analyze the automotive industry and grow.")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown(f"<h4> Do some Visual Representation of automobile features ...</h4>", unsafe_allow_html=True)
        st.write("\n")
        st.write("\n")
        st.image("pexels-pixabay-248747.jpg", width=180)
        st.markdown(f"<h4> Analyze customer segmentation ,for various automobile features ... </h4>",
                    unsafe_allow_html=True)
        st.write("\n")
        st.image("pexels-suzy-hazelwood-5010877.jpg", width=180)
        st.markdown(f"<h4> And much more ... </h4>", unsafe_allow_html=True)

    with col2:
        st.image("pexels-energepiccom-159888.jpg", width=180)
        st.markdown(f"<h4>Make some predictions ... </h4> ", unsafe_allow_html=True)
        st.write("\n")
        st.write("\n")
        st.image("pexels-vitaly-vlasov-1342460.jpg", width=180)
        st.markdown(f"<h4> Check out latest news related to automobiles ... </h4>", unsafe_allow_html=True)

if a1 == 'Explore':

    st.sidebar.title("Lets do some Representation and Analysis !")
    st.sidebar.image("download.png", width=100)

    b1 = st.sidebar.radio("select option :",('📈 Visual Representation','📉 Dependency & Analysis','📋 Price Prediction','📰 Automobile News','🔎 Resolve Queries','📊 Web Scraping'))

    options_to_choose = ['symboling','normalized_losses','wheel_base','engine_size', 'length', 'width','height','curb_weight', 'bore', 'stroke', 'compression_ratio', 'horsepower', 'peak_rpm',
                         'city_mpg', 'highway_mpg', 'num_doors', 'num_cylinders', 'engine_size_cc',
                         'power2weight_ratio']
    size_of_options = len(options_to_choose)


    if b1 == '📈 Visual Representation':
        st.markdown(f"<h1 style='background-color:#F3F781;'> 📈 Visual Representation & Analysis </h1>", unsafe_allow_html=True)
        #st.title("Visual Representation & Analysis")
        selected_option2 = st.multiselect(
            '👉 Choose the feature for representation :',
            options=options_to_choose,
            default=(options_to_choose[0], options_to_choose[1], options_to_choose[3])
        )
        size_of_selected_option = len(selected_option2)

        graphs_to_choose = (
            'Bar Graph', 'Line Graph', 'Area Graph', 'Scatter Chart', 'Donut Chart', 'Pie Chart',)

        if size_of_selected_option == 0:
            st.warning("Select an option.")

        elif size_of_selected_option == size_of_options:
            type_of_graph = st.radio('👉 Choose the type of graph to display : ', graphs_to_choose)

            if type_of_graph == 'Pie Chart':  # need to be handled

                st.warning("Please select only one parameter of feature to view this chart.")

            if type_of_graph == 'Donut Chart':
                st.warning("Please select only one parameter of feature to view this chart.")

            if type_of_graph == 'Scatter Chart':
                st.warning("Please select only one parameter of feature to view this chart.")

            if type_of_graph == 'Line Graph':
                plost.line_chart(
                    dt,
                    x='make',
                    y=selected_option2,
                    height=500,
                    # 👈 This is magic!
                )

            if type_of_graph == 'Area Graph':
                plost.area_chart(
                    data=dt,
                    x='make',
                    y=selected_option2,
                    opacity=1,
                    height=500,
                    stack=False)

            if type_of_graph == 'Bar Graph':
                which_form = st.selectbox("Direction of Bar Chart : ", ('vertical', 'horizontal'))
                plost.bar_chart(
                    data=dt,
                    bar='make',
                    value=selected_option2,
                    direction=which_form,
                    group='value',
                    color='make',
                    height=500,
                    legend=None)

        elif size_of_selected_option < size_of_options and size_of_selected_option != 1:
            type_of_graph = st.radio('👉 Choose the type of graph to display : ', graphs_to_choose)

            if type_of_graph == 'Pie Chart':  # need to be handled

                st.warning("Please select only one parameter of feature to view this chart.")

            if type_of_graph == 'Donut Chart':
                st.warning("Please select only one parameter of feature to view this chart.")

            if type_of_graph == 'Scatter Chart':
                st.warning("Please select only one parameter of feature to view this chart.")

            if type_of_graph == 'Line Graph':
                plost.line_chart(
                    dt,
                    x='make',
                    y=selected_option2,
                    height=500,
                    # 👈 This is magic!
                )

            if type_of_graph == 'Area Graph':
                plost.area_chart(
                    data=dt,
                    x='make',
                    y=selected_option2,
                    opacity=1,
                    height=500,
                    stack=False)

            if type_of_graph == 'Bar Graph':
                which_form = st.selectbox("Direction of Bar Chart : ", ('vertical', 'horizontal'))
                plost.bar_chart(
                    data=dt,
                    bar='make',
                    value=selected_option2,
                    direction=which_form,
                    group='value',
                    color='make',
                    height=500,
                    legend=None)

        elif size_of_selected_option == 1:

            type_of_graph = st.radio('👉 Choose the type of graph to display : ', graphs_to_choose)

            if type_of_graph == 'Pie Chart':  # need to be handled
                selected = selected_option2[0]
                st.subheader(selected)
                plost.pie_chart(
                    data=dt,
                    theta=selected,  # can take single value only
                    color='make',
                    height=500, )

            if type_of_graph == 'Donut Chart':
                selected = selected_option2[0]
                st.subheader(selected)
                plost.donut_chart(
                    data=dt,
                    theta=selected,
                    height=500,  # can take single value only
                    color='make')

            if type_of_graph == 'Scatter Chart':
                plost.scatter_chart(
                    data=dt,
                    x='make',
                    y='engine-size',  # for one value
                    size=150,
                    opacity='engine-size',
                    height=500)

            if type_of_graph == 'Line Graph':
                plost.line_chart(
                    dt,
                    x='make',
                    y=selected_option2,
                    height=500,
                    # 👈 This is magic!
                )

            if type_of_graph == 'Area Graph':
                plost.area_chart(
                    data=dt,
                    x='make',
                    y=selected_option2,
                    opacity=1,
                    height=500,
                    stack=False)

            if type_of_graph == 'Bar Graph':
                which_form = st.selectbox("Direction of Bar Chart : ", ('vertical', 'horizontal'))
                plost.bar_chart(
                    data=dt,
                    bar='make',
                    value=selected_option2,
                    direction=which_form,
                    group='value',
                    color='make',
                    height=500,
                    legend=None)

    elif b1 == '📉 Dependency & Analysis':
        st.markdown(f"<h1 style='background-color:#F3F781;'> 📉 Dependency & Analysis </h1>",
                    unsafe_allow_html=True)

        y_axis_dependent = st.multiselect(
            "👉 Choose the features you wanna analyze for dependency: ",
            options=options_to_choose,
            default=(options_to_choose[0], options_to_choose[1]))

        res = list((Counter(options_to_choose) - Counter(y_axis_dependent)).elements())

        x_axis_dependent = st.selectbox("👉 Choose the feature with respect to which you want to see analysis : ",
                                        res)

        type_of_graph2 = st.selectbox("👉 Select type of Chart :", ('Area Chart', 'Line Chart'))

        if y_axis_dependent != x_axis_dependent and len(y_axis_dependent) != 0:

            if type_of_graph2 == 'Line Chart':
                plost.line_chart(
                    dt,
                    x=x_axis_dependent,
                    y=y_axis_dependent,
                    height=500,
                    # 👈 This is magic!
                )

            if type_of_graph2 == 'Area Chart':
                plost.area_chart(
                    data=dt,
                    x=x_axis_dependent,
                    y=y_axis_dependent,
                    opacity=1,
                    height=500,
                    stack=False)

        else:

            st.warning("Choose atleast 1 option for analysis.")

    elif b1 == '📋 Price Prediction':
        st.markdown(f"<h1 style='background-color:#E2A9F3;'> 📋 Price Prediction </h1>",
                    unsafe_allow_html=True)

        options_to_choose2 = ['width', 'bore', 'stroke', 'horsepower', 'num_doors', 'num_cylinders',
                              'engine_size_cc', 'power2weight_ratio']
        get_linear_prediction(dt, options_to_choose2)
        # get_rf_prediction(dt, options_to_choose2)
        get_svm_prediction(dt, options_to_choose2)
        model = pickle.load(open('model.sav', 'rb'))
        # model2 = pickle.load(open('model2.sav', 'rb'))
        model3 = pickle.load(open('model3.sav', 'rb'))


        def user_report():
            width = st.number_input("🙌 Enter width of the car.", value=66.0, min_value=50.0, max_value=350.0, key=1,
                                    step=0.1)
            bore = st.number_input("🙌 Enter bore of the car.", key=2, step=0.1, value=3.0)
            stroke = st.number_input("🙌 Enter stroke of the car.", key=3, step=0.1, value=3.0)
            horsepower = st.number_input("🙌 Enter horsepower of the car.", key=5, step=10.0, value=102.0)
            num_doors = st.number_input("🙌 Enter number of doors of the car.", key=8, step=1.0, value=4.0)
            num_cylinders = st.number_input("🙌 Enter number of cylinders of the car.", key=9, step=1.0, value=4.0)
            engine_size_cc = st.number_input("🙌 Enter Engine size in cc of the car.", key=10, step=10.0, value=1786.0)
            power2weight_ratio = st.number_input("🙌 Enter power to weight ratio of the car.", key=11, step=0.001,
                                                 value=0.0)

            user_report_data = {
                'width': width,
                'bore': bore,
                'stroke': stroke,
                'horsepower': horsepower,
                'num_doors': num_doors,
                'num_cylinders': num_cylinders,
                'engine_size_cc': engine_size_cc,
                'power2weight_ratio': power2weight_ratio

            }
            report_data = pd.DataFrame(user_report_data, index=[0])
            return report_data


        user_data = user_report()

        selected_model = st.selectbox("👉 Choose model", ('Linear Regression', 'SVM Regression'))
        if selected_model == 'Linear Regression':
            price_pred = model.predict(user_data)
            st.write("\n")
            st.subheader("✍ The  predicted  price  of  the  car  is: ")
            st.subheader("Rs. " + str(np.round(price_pred[0], 2)))

        if selected_model == 'SVM Regression':
            price_pred = model3.predict(user_data)
            st.write("\n")
            st.subheader("✍ The  predicted  price  of  the  car  is: ")
            st.subheader("Rs. " + str(np.round(price_pred[0], 2)))

    elif b1 == '📰 Automobile News':
        st.markdown(f"<h1 style='background-color:#A9BCF5;'> 📰 Automobile News </h1>",
                    unsafe_allow_html=True)

        get_news()

    elif b1 == '🔎 Resolve Queries':
        st.markdown(f"<h1 style='background-color:#A9BCF5;'> 🔎 Resolve Queries</h1>",
                    unsafe_allow_html=True)

        selected_query = st.selectbox("👉 Your query is related to",('📝 Find cars with an input value of a feature',
                                                                  '📝 Highest/Lowest values of features',
                                                                     '📝 Segmentation & Grouping'))

        if selected_query == '📝 Find cars with an input value of a feature':
            selected_feature = st.selectbox("Choose an option", (
            'symboling', 'normalized_losses', 'wheel_base', 'engine_size', 'length', 'width', 'height', 'curb_weight',
            'bore', 'stroke', 'compression_ratio', 'horsepower', 'peak_rpm',
            'city_mpg', 'highway_mpg', 'num_doors', 'num_cylinders', 'engine_size_cc',
            'power2weight_ratio'))

            selected_car = st.number_input("Enter value ", key=1, step=0.1)
            selected_car = float(selected_car)

            if st.checkbox("Equal to input value"):
                model_list = dt[dt[selected_feature] == selected_car].make
                final_model_list = model_list.unique()
                st.write("The cars having " + selected_feature + " equal to " + str(selected_car) + " are :")
                for i in final_model_list:
                    st.write(i.capitalize())

            if st.checkbox("More than input value"):
                model_list = dt[dt[selected_feature] > selected_car].make
                final_model_list = model_list.unique()
                st.write("The cars having " + selected_feature + " greater than " + str(selected_car) + " are :")
                for i in final_model_list:
                    st.write(i.capitalize())

            if st.checkbox("Less than input value"):
                model_list = dt[dt[selected_feature] < selected_car].make
                final_model_list = model_list.unique()
                st.write("The cars having " + selected_feature + " smaller than " + str(selected_car) + " are :")
                for i in final_model_list:
                    st.write(i.capitalize())

        if selected_query == '📝 Highest/Lowest values of features':
            selected_feature = st.selectbox("Choose an option", (
                'symboling', 'normalized_losses', 'wheel_base', 'engine_size', 'length', 'width', 'height',
                'curb_weight',
                'bore', 'stroke', 'compression_ratio', 'horsepower', 'peak_rpm',
                'city_mpg', 'highway_mpg', 'num_doors', 'num_cylinders', 'engine_size_cc',
                'power2weight_ratio'))

            column = dt[selected_feature]
            max_value = column.max()
            max_value_model = dt[column == max_value].make
            final_max_model = max_value_model.unique()
            st.write("The maximum value of " + selected_feature + " is " + str(max_value) + " and present in these cars : ")
            for i in final_max_model:
                st.write(i.capitalize())

            min_value = column.min()
            min_value_model = dt[column == min_value].make
            final_min_model = min_value_model.unique()
            st.write(
                "The minimum value of " + selected_feature + " is " + str(min_value) + " and present in these cars : ")
            for i in final_min_model:
                st.write(i.capitalize())

        if selected_query == '📝 Segmentation & Grouping':
            feature_for_segment = st.selectbox(
                "👉 Select the first feature to show grouping and segmentation: ", options_to_choose,
                key=1)
            Dict = {'symboling': 1, 'normalized_losses': 2, 'wheel_base': 10, 'length': 11, 'width': 12, 'height': 13,
                    'curb_weight': 14, 'engine_size': 17, 'horsepower': 22, 'peak_rpm': 23, 'bore': 19, 'stroke': 20,
                    'compression_ratio': 21,
                    'city_mpg': 24, 'highway_mpg': 25, 'num_doors': 28, 'num_cylinders': 29, 'engine_size_cc': 30,
                    'power2weight_ratio': 31}
            selected_segment = Dict[feature_for_segment]
            res = list((Counter(options_to_choose) - Counter([feature_for_segment])).elements())
            feature_for_segment2 = st.selectbox(
                "👉 Select the second feature to show grouping and segmentation: ", res,
                key=2)
            Dict2 = {'symboling': 1, 'normalized_losses': 2, 'wheel_base': 10, 'length': 11, 'width': 12, 'height': 13,
                     'curb_weight': 14, 'engine_size': 17, 'horsepower': 22, 'peak_rpm': 23, 'bore': 19, 'stroke': 20,
                     'compression_ratio': 21,
                     'city_mpg': 24, 'highway_mpg': 25, 'num_doors': 28, 'num_cylinders': 29, 'engine_size_cc': 30,
                     'power2weight_ratio': 31}
            selected_segment2 = Dict[feature_for_segment2]
            if st.button("📊 Get representation for these features "):
                st.write(
                    "The customer segmentation graph given below shows the most popular " + feature_for_segment + " and " + feature_for_segment2 + " combination which are preferred by people.")
                get_customer_seg(dt, selected_segment, selected_segment2)
                st.write(
                    "Red , yellow and green dots depict 3 different groups, which show how the " + feature_for_segment + " and the " + feature_for_segment2 + " are available in different cars.")



    elif b1 == '📊 Web Scraping':

        st.markdown(f"<h1 style='background-color:#F3F781;'> 📉 Web Scraping </h1>",
                    unsafe_allow_html=True)
        df = pd.read_excel('car_extracted_data.xlsx')

        st.subheader("Extracted data : ")
        st.write(df)
        plost.bar_chart(
            data=df,
            bar='Name',
            value='Rating',
            group='value',
            color='Name',
            height=500,
            legend=None)

        car_options = df["Name"].unique().tolist()

        car_selected = st.selectbox("select the car to get details : ",car_options)

        car_rating = df[df['Name'] == car_selected].Rating
        car_price = df[df['Name'] == car_selected].Price
        car_mileage = df[df['Name'] == car_selected].Mileage

        st.subheader("Mileage - " + car_mileage.values[0])
        st.subheader("Rating - " + str(car_rating.values[0]))
        car_rate= car_rating.values[0]
        average_rating = round(car_rate, 1)
        star_rating = ":star:" * int(round(average_rating, 0))
        st.subheader(star_rating)
        st.subheader("Price - " + str(car_price.values[0]))






