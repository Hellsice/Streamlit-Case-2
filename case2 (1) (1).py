#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Covid-vs-Gaming_Julius_Slobbe_500916116_Serhat_kokcu_500858425_Bart_Kombee_500914214


# In[2]:


import numpy as np
import pandas as pd

import plotly.express as px
import plotly.graph_objects as go

import streamlit as st


# In[3]:


st.title('Online gaming vs Covid-19')


# In[8]:


energy_usage = pd.read_csv('Energy usage.csv')
WC4 = pd.read_csv('Corona and steam.csv')
PS4_concurrent_players = pd.read_csv('PS4.csv')


# In[17]:


# Create a simple bar chart
fig1 = px.bar(data_frame=energy_usage, x='year', y='consumption')


# Create the buttons
my_buttons = [{'label': "Bar", 'method': "update", 'args': [{"type": "bar"}]},
  {'label': "Line-figure", 'method': "update", 'args': [{"type": "line", 'mode': 'line'}]}]



# Add buttons to the plot and show
fig1.update_layout(
    
    {'updatemenus': [{
      'type':'buttons','direction': 'down',
      'x': 1.3,'y': 0.5,
      'showactive': True, 'active': 0,
      'buttons': my_buttons}]},

)

fig1.update_layout(
    title="Energy usage (TWH)",
    xaxis_title="Time stamp",
    yaxis_title="Energy usage (TWH)",
    legend_title="Legend Title",
    font=dict(
        family="Arial",
        size=14,
        color="RebeccaPurple"
    )
)
fig1.show()



# In[18]:


# Create a simple bar chart
fig2 = px.bar(data_frame=WC4, x='Date', y='Steam users')

#annotations
value_annotations=[{'text': 'Peak #1 : 4-apr-2020' ,'showarrow': True, 'x': '2020-04-04', 'y': 24900000 },
                  {'text': 'Peak #2 : 5-apr-2021' ,'showarrow': True, 'x': '2021-04-05', 'y': 26900000 },
                  {'text': 'Peak #3 : 3-apr-2022' ,'showarrow': True, 'x': '2022-04-03', 'y': 30000000 }]
sign_clear=[{'text': 'Clear', 'showarrow': False, 'x': 'October', 'y': 24.53 }]



# Create the buttons
my_buttons = [{'label': "Bar", 'method': "update", 'args': [{"type": "bar"}]},
  {'label': "Line-figure", 'method': "update", 'args': [{"type": "line", 'mode': 'line'}]},
             {'label': "Peaks", 'method': "update", 'args': [{}, {"annotations": value_annotations}]},
             {'label': "Clear peaks", 'method': "update", 'args': [{}, {"annotations": sign_clear}]}]



# Add buttons to the plot and show
fig2.update_layout(
    
    {'updatemenus': [{
      'type':'buttons','direction': 'down',
      'x': 1.3,'y': 0.5,
      'showactive': True, 'active': 0,
      'buttons': my_buttons}]},

)

fig2.update_layout(
    title="Interactive plot displaying unique peaks regarding the Steam dataset",
    xaxis_title="Time stamp",
    yaxis_title="Active users (Millions)",
    legend_title="Legend Title",
    font=dict(
        family="Arial",
        size=14,
        color="RebeccaPurple"
    )
)
fig2.show()


my_chart = st.bar_chart(data=WC4, x='DateTime', y='Steam users')
my_chart.add_rows(PS4_concurrent_players)


# In[19]:


# Create a simple bar chart
fig3 = px.bar(data_frame=WC4, x='Date', y='Corona cases')

#annotations
sign_clear=[{'text': 'Clear', 'showarrow': False, 'x': 'October', 'y': 24.53 }]


# Create the buttons
my_buttons = [{'label': "Bar", 'method': "update", 'args': [{"type": "bar"}]},
  {'label': "Line-figure", 'method': "update", 'args': [{"type": "line", 'mode': 'line'}]},]




# Add buttons to the plot and show
fig3.update_layout(
    
    {'updatemenus': [{
      'type':'buttons','direction': 'down',
      'x': 1.3,'y': 0.5,
      'showactive': True, 'active': 0,
      'buttons': my_buttons}]},

)

fig3.update_layout(
    title="Confirmed COVID cases on a global scale",
    xaxis_title="Time stamp",
    yaxis_title="Confirmed COVID cases (Infectants in billions)",
    legend_title="Legend Title",
    font=dict(
        family="Arial",
        size=14,
        color="RebeccaPurple"
    )
)
fig3.show()




# In[20]:


# Create a simple bar chart
fig4 = px.bar(data_frame=PS4_concurrent_players, x='dates', y='Player count')

# Create the buttons
my_buttons = [{'label': "Bar", 'method': "update", 'args': [{"type": "bar"}]},
  {'label': "Line-figure", 'method': "update", 'args': [{"type": "line", 'mode': 'line'}]}]


# Add buttons to the plot and show
fig4.update_layout(
    
    {'updatemenus': [{
      'type':'buttons','direction': 'down',
      'x': 1.3,'y': 0.5,
      'showactive': True, 'active': 0,
      'buttons': my_buttons}]},

)

fig4.update_layout(
    title="Active PS players online",
    xaxis_title="Time stamp",
    yaxis_title="Active users",
    legend_title="Legend Title",
    font=dict(
        family="Arial",
        size=14,
        color="RebeccaPurple"
    )
)
fig4.show()


# In[21]:


#WC3 Houdt nu de combinatie van de 2 dataframes world_cases en Steam_players_corona in.
WC4.head(20)

# Correlation table met pearson methodiek
WC5= WC4[['Corona cases', 'Steam users']]
WC_corr= WC5.corr(method='pearson')

# Heat map instellen
fig5 = go.Figure(go.Heatmap(
        z=WC_corr.values.tolist(),
        x=WC_corr.columns,
        y=WC_corr.columns,
        colorscale='rdylgn', 
        zmin=-1, zmax=1))


fig5.update_layout(
    title="Correlation heatmap",
    xaxis_title=" 'users' = active steam users    |    'Cumulative_cases' = Infected patients ",
    legend_title="Legend Title",
    font=dict(
        family="Arial",
        size=14,
        color="RebeccaPurple"
    )
)

# Plot laten zien
fig5.show()


# In[22]:


fig6 = px.scatter(x=WC4["Corona cases"], y=WC4["Steam users"])


fig6.update_layout(
    title="Scatterplot",
    xaxis_title="Infected patients (millions)",
    yaxis_title="Active steam users (millions)",
    font=dict(
        family="Arial",
        size=14,
        color="RebeccaPurple"
    )
)

fig6.show()


# In[25]:


st.header('Our figures after analysing our 4 datasets')

st.write('Welcome to our presentation, the 4 datasets that we have used consist of Steam players, Power consumption globally, COVID Cases and playstation network users. With these 4 datasets we are trying to show if there is a correlation between the COVID cases and the remaining datasets mentioned above.')


st.plotly_chart(fig1, use_container_width=False, sharing="streamlit")

st.plotly_chart(fig2, use_container_width=False, sharing="streamlit")

st.plotly_chart(fig3, use_container_width=False, sharing="streamlit")

st.plotly_chart(fig4, use_container_width=False, sharing="streamlit")

st.plotly_chart(fig5, use_container_width=False, sharing="streamlit")

st.plotly_chart(fig6, use_container_width=False, sharing="streamlit")


# In[ ]:




