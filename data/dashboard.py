import plotly.express as px
from data import mysql

def generate_dashboard(category, year, quarter):
        if category == "transaction":
                try:
                        aggregate_transactions = mysql.read("aggregate_transactions") 
                        map_transactions = mysql.read("map_transactions") 
                        aggregate_transactions = aggregate_transactions[(aggregate_transactions["year"]==(year)) & (aggregate_transactions["quarter"]==quarter)]
                        map_transactions = map_transactions[(map_transactions["year"] == year) & (map_transactions["quarter"] == quarter)]
                        return [generate_map(map_transactions,"transaction"),map_transactions, aggregate_transactions]
                except:
                        return None
                            
        elif category == "user":
                try:
                        aggregate_users = mysql.read("aggregate_users")     
                        map_users = mysql.read("map_users")     
                        aggregate_users = aggregate_users[(aggregate_users["year"]==year) & (aggregate_users["quarter"] == quarter)]
                        map_users = map_users[(map_users["year"]==year) & (map_users["quarter"]==quarter)]
                        return [generate_map(map_users, "user"), map_users, aggregate_users]
                except:
                        return None

def generate_map(data, category):
        if category == "transaction":
                fig = px.choropleth(
                data,
                geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
                featureidkey='properties.ST_NM',
                locations='state',
                hover_data=['transactions_M','amount_cr'],
                color='transactions_M',
                color_continuous_scale='Reds',
                projection='mercator',
                basemap_visible=True,
                range_color=(0,data["transactions_M"].max())
                )                
                fig.update_geos(fitbounds="locations", visible=False)
                return fig
                
        elif category == "user":
                fig = px.choropleth(
                data,
                geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
                featureidkey='properties.ST_NM',
                locations='state',
                hover_data=['users_registered_M','appOpens_M'],
                color='users_registered_M',
                color_continuous_scale='Reds',
                projection='mercator',
                basemap_visible=True,
                range_color=(0,data["users_registered_M"].max())
                )
                fig.update_geos(fitbounds="locations", visible=False)
                return fig  