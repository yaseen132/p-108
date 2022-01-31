import pandas as pd 
import plotly.figure_factory as ff 

df=pd.read_csv('data1.csv')

figure=ff.create_distplot([df['Avg Rating'].tolist()],['Rating'],show_hist=False)
figure.show()
