# phonepe-data

Phonepe-data is a data app to help visualize user and transaction details of the app. It is inspired by [phonepe pulse](https://www.phonepe.com/pulse/explore/transaction/2022/4/).<br/>
Find the data [here](https://github.com/PhonePe/pulse#readme)<br />

This app is built using python and streamlit, and uses mysql database to store and fetch the available data.


<h2>dependencies</h2>
pandas : <code> pip install pandas </code> <br/>
streamlit : <code> pip install streamlit </code> <br/>
pysql : <code> pip install pysql </code> <br/>
plotly : <code> pip install plotly </code> <br/>

<h2>Loading the data</h2>

set the connection parameters in .config file <br/>
Load the data into the database using: <code> python load_data.py </code>


<h2>Run the application</h2>

Run the application: <code> streamlit run main.py </code>
