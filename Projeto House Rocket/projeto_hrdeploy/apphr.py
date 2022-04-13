# Imports
import streamlit as st
import pandas as pd
import numpy as np
import folium
from streamlit_folium import folium_static
from folium.plugins import MarkerCluster
import geopandas
import plotly.express as px
from datetime import datetime

st.set_page_config(layout = 'wide')

@st.cache(allow_output_mutation = True)

# Functio to read the dataset
def get_data(path):
    data = pd.read_csv(path)

    return data

# Function to get the coordinates of the map to draw the edges
@st.cache(allow_output_mutation = True)
def get_geofile(url):
    geofile = geopandas.read_file(url)

    return geofile


def set_attibutes(data):
    # Add attributes
    pass

def data_overview(data):
    # Filters
    f_attributes = st.sidebar.multiselect('Enter columns', data.columns)
    f_zipcode = st.sidebar.multiselect('Enter zipcode', data['zipcode'].unique())

    st.title('Data Overview')

    # Setting the display of the filters
    if (f_zipcode != []) & (f_attributes !=[]):
        data = data.loc[data['zipcode'].isin(f_zipcode), f_attributes]

    elif (f_zipcode != []) & (f_attributes == []):
        data = data.loc[data['zipcode'].isin(f_zipcode), : ]

    elif( f_zipcode == []) & (f_attributes != []):
        data = data.loc[: , f_attributes]

    else:
        data = data.copy()

    # Display the entire datafream without filters at the top of the page
    st.dataframe(data)

    # Setting one disply to show graphs side-by-side
    c1, c2 = st.columns((1, 1))

    # Average metrics
    df1 = data[['id', 'zipcode']].groupby('zipcode').count().reset_index()
    df2 = data[['price', 'zipcode']].groupby('zipcode').mean().reset_index()
    df3 = data[['sqft_living', 'zipcode']].groupby('zipcode').mean().reset_index()

    # Merging the dataframes
    m1 = pd.merge(df1, df2, on='zipcode', how = 'inner')
    df = pd.merge(m1, df3, on = 'zipcode', how = 'inner')

    # Rename the name of columns
    df.columns = ['zipcode', 'total houses', 'price', 'sqft_living']

    # Method to display a dataframe in streamlit app
    c1.header('Descriptive Statistics')
    c1.dataframe(df.describe().T, height = 600)

    return None

def region_overview(data, geofile):
    # Densidade de Portfolio
    st.title('Region Overview')

    c1, c2 = st.columns(2)
    c1.header('Portfolio Density')

    # Getting a sample of the original dataframe to can be able to test the code
    df = data.sample(10)

    # Base Map Folium
    density_map = folium.Map(location = [data['lat'].mean(), data['long'].mean()], default_zoom_start = 15)

    # Setting the markers to each house on the map
    marker_cluster = MarkerCluster().add_to(density_map)

    # Getting each lat and log from our dataframe
    for name, row in df.iterrows():
        folium.Marker( [row['lat'], row['long']],
        popup = 'Sold U${0} on: {1}. Features: {2} sqft, {3} bedrooms, {4} bathrooms, year built {5}'.format(row['price'], row['date'], row['sqft_living'], row['bedrooms'], row['bathrooms'], row['yr_built'])).add_to(marker_cluster)


    # Plotting the map
    with c1:
        folium_static(density_map)

    # Region Price map
    c2.header('Price Density')

    # Setting the map to show within mean, what's the high price per zipcode
    df = data[['price', 'zipcode']].groupby('zipcode').mean().reset_index()

    # Setting the geofile to show the correct color per region
    geofile = geofile[geofile['ZIP'].isin(df['zipcode'].tolist())]

    # Setting the plot for a base map
    region_map_price = folium.Map(location = [data['lat'].mean(),
    data['long'].mean()], default_zoom_start = 15)

    # Setting the map to show colored regions
    region_map_price.choropleth(data = df, geo_data = geofile, columns=['zipcode', 'price'],
    key_on = 'feature.properties.ZIP',
    fill_color = 'YlOrRd', # The code means, YellowOrangeRed
    fill_opacity = 0.7,
    line_opcatity = 0.2,
    legend_name = 'AVG Prices')

    # Plotting the map

    with c2:
        folium_static(region_map_price)

    return None

def set_commercial(data):
    # Distribuicao dos imoveis por categorias comerciais
    st.sidebar.title('Comemercial Options')
    st.title('Commercial Attributes')

    # Average price per Year
    min_year_built = int(data['yr_built'].min() )
    max_year_built = int(data['yr_built'].max() )

    # Setting filters
    st.sidebar.subheader('Select Max Year Built')
    f_year_built = st.sidebar.slider('Year Built', 
    min_year_built,
    max_year_built,
    min_year_built)

    st.header('Average Price Per Year Built')

    # Get Data
    data['date'] = pd.to_datetime(data['date']).dt.strftime('%Y-%m-%d')

    # Data Filtering
    data = data.loc[data['yr_built'] <= f_year_built ]
    df = data[['yr_built', 'price']].groupby('yr_built').mean().reset_index()

    # Plot
    fig = px.line(df, x = 'yr_built', y = 'price')
    st.plotly_chart(fig, use_container_width = True)

    # Average price per day
    st.header('Average price per day')
    st.sidebar.subheader('Select Max Data')

    # Load Data
    data = get_data(path = 'df_all.csv')
    data['date'] = pd.to_datetime(data['date']).dt.strftime('%Y-%m-%d')

    # Creagint filters
    min_date = datetime.strptime(data['date'].min(), '%Y-%m-%d')
    max_date = datetime.strptime(data['date'].max(), '%Y-%m-%d')
    f_date = st.sidebar.slider('Date', min_date, max_date, min_date)

    # Setting the filters
    data['date'] = pd.to_datetime(data['date'])
    data = data.loc[data['date'] <= f_date, : ]
    df = data[['date', 'price']].groupby('date').mean().reset_index()

    # Plot
    fig = px.line(df, x = 'date', y = 'price')
    st.plotly_chart(fig, use_container_width = True)


    # Histogram
    st.header('Price Distribuition')
    st.sidebar.subheader('Select Max Price')

    # Creating Filters
    min_price = int(data['price'].min())
    max_price = int(data['price'].max())
    avg_price = int(data['price'].mean())
    f_price = st.sidebar.slider('Price', min_price, max_price, avg_price)

    # Setting filter
    df = data[data['price'] < f_price]

    # Plot
    fig = px.histogram(df, x = 'price', nbins = 50)
    st.plotly_chart(fig, use_container_width = True)

    return None

def set_physical(data):
    
    # Distribuicao das casas por categorias fisicas
    st.sidebar.title('Attributes Options')
    st.title('House Attributes')

    # Data Transformation
    data['floors'] = data['floors'].astype('int64')
    data['bathrooms'] = data['bathrooms'].astype('int64')

    # Creating Filters
    f_bedrooms = st.sidebar.selectbox('Max number of bedrooms', sorted(set(data['bedrooms'].unique())))
    f_bathrooms = st.sidebar.selectbox('Max number of bathrooms', sorted(set(data['bathrooms'].unique())))

    # setting the layout of the plots
    c1, c2 = st.columns (2)

    # Houses per bedrooms
    c1.header('Houses per bedrooms')
    df = data[data['bedrooms'] <= f_bedrooms]
    fig = px.histogram(df, x = 'bedrooms', nbins = 19)
    c1.plotly_chart(fig, use_container_width = True)

    # Houses per bathrooms
    c2.header('Houses per bathrooms')
    df = data[data['bathrooms'] <= f_bathrooms]
    fig = px.histogram(df, x = 'bathrooms', nbins = 19)
    c2.plotly_chart(fig, use_container_width = True)

    # Creating the filters
    f_floors = st.sidebar.selectbox('Max number of floors', sorted(set(data['floors'].unique())))
    f_waterview = st.sidebar.checkbox('Only House with Waterview')

    c1, c2 = st.columns(2)

    # House per floors
    c1.header('Houses per floors')
    df = data[data['floors'] <= f_floors]
    fig = px.histogram(df, x = 'floors', nbins = 19)
    c1.plotly_chart(fig, use_container_width = True)

    # Houses per waterview
    if f_waterview:
        df = data[data['waterfront'] == 1]
    else:
        df = data.copy()

    fig = px.histogram(df, x = 'waterfront', nbins = 10)
    c2.header('Houses per waterview')
    c2.plotly_chart(fig, use_container_width = True)

    return None


if __name__ == '__main__':
    # ETL
    path = 'df_all.csv'
    url = 'https://opendata.arcgis.com/datasets/83fc2e72903343aabff6de8cb445b81c_2.geojson'

    # Load data
    data = get_data(path)
    geofile = get_geofile(url)

    # Transformation Data
    data_overview(data)

    region_overview(data, geofile)

    set_commercial(data)

    set_physical(data)
