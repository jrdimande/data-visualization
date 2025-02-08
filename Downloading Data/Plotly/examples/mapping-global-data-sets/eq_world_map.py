from plotly.graph_objs import Scattergeo, Layout
from plotly import offline
from eq_explore_data import mags, lons, lats

# Map the earthquakes
data =[Scattergeo(lon=lons, lat=lats)]
my_layout = Layout(title='Global Earthquakes')

fig = {'data' : data, 'layout' : my_layout}
offline.plot(fig, filename='global_earthquakes.html')
