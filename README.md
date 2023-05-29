# phonePe Pulse - Data

Phonepe-data is a data app to help visualize user and transaction details of the app. It is inspired by [phonepe pulse](https://www.phonepe.com/pulse/explore/transaction/2022/4/).<br/>
Find the data [here](https://github.com/PhonePe/pulse#readme)<br />

stack : python, mysql, streamlit, plotly.

# Guide #

<h3>Install the dependencies</h3>
pandas : <code> pip install pandas </code> <br/>
streamlit : <code> pip install streamlit </code> <br/>
pysql : <code> pip install pysql </code> <br/>
plotly : <code> pip install plotly </code> <br/>

<h3>Data Folder Structure </h3>

```json
data
|___ aggregated
    |___ transactions
        |___ country
            |___ india
                |___ 2018
                |    1.json
                |    2.json
                |    3.json
                |    4.json
                
                |___ 2019
                |    ...
                |___ 2019
                |___ state 
                    |___ andaman-&-nicobar-islands
                        |___2018
                        |   1.json
                        |   2.json
                        |   3.json
                        |   4.json

                    |___ andhra-pradesh
                    |    ...
                    |    ...
```

<h3>Data JSON Structure / Syntax</h3>

<h4>1. Aggregated</h4>
1.1 data/aggregated/transaction/country/india/2018/1.json
Transaction data broken down by type of payment at country level.

For complete details on syntax find the comments in below code

NOTE: Similar syntax is followed for state level too. Ex: data/aggregated/transaction/country/india/state/delhi/2018/1.json

```json
{
    "success": true, //Ignore. For internal use only
    "code": "SUCCESS", //Ignore. For internal use only
    "data": {
        "from": 1514745000000, //Data duration
        "to": 1522175400000,
        "transactionData": [
            {
                "name": "Recharge & bill payments", //Type of payment category
                "paymentInstruments": [
                    {
                        "type": "TOTAL",
                        "count": 72550406, //Total number of transactions for the above payment category
                        "amount": 1.4472713558652578E10 //Total value
                    }
                ]
            },
            
            ...,

            ...,
                        
            {
                "name": "Others",
                "paymentInstruments": [
                    {
                        "type": "TOTAL",
                        "count": 5761576,
                        "amount": 4.643217301269438E9
                    }
                ]
            }
        ]
    },
    "responseTimestamp": 1630346628866 //Ignore. For internal use only.
}
```
1.2 data/aggregated/user/country/india/2021/1.json
Users data broken down by devices at country level.

For complete details on syntax find the comments in below code

NOTE: Similar syntax is followed for state level too. Ex: data/aggregated/user/country/india/state/delhi/2021/1.json
```json
{
    "success": true, //Ignore. For internal use only.
    "code": "SUCCESS", //Ignore. For internal use only.
    "data": {
        "aggregated": {
            "registeredUsers": 284985430, //Total number of registered users for the selected quarter.
            "appOpens": 8635508502 //Number of app opens by users for the selected quarter
        },
        "usersByDevice": [ //Users by individual device
            {
                "brand": "Xiaomi", //Brand name of the device
                "count": 71553154, //Number of registered users by this brand.
                "percentage": 0.2510765339828075 //Percentage of share of current device type compared to all devices.
            },
            
            ...,

            ...,

            {
                "brand": "Others", //All unrecognized device types grouped here. 
                "count": 23564639, //Number of registered users by all unrecognized device types.
                "percentage": 0.08268717105993804 //Percentage of share of all unrecognized device types compared to overall devices that users are registered with.
            }
        ]
    },
    "responseTimestamp": 1630346630074 //Ignore. For internal use only.
}
```

<h4>2. Map</h4>
2.1 data/map/transaction/hover/country/india/2021/1.json
Total number of transactions and total value of all transactions at the state level.

For complete details on syntax find the comments in below code

NOTE: Similar syntax is followed for district level too. Ex: data/map/transaction/hover/country/india/state/delhi/2021/1.json
```json
{
    "success": true, //Ignore. For internal use only.
    "code": "SUCCESS", //Ignore. For internal use only.
    "data": {
        "hoverDataList": [ //Internally, this being used to show state/district level data whenever a user hovers on a particular state/district.
            {
                "name": "puducherry", //State / district name
                "metric": [
                    {
                        "type": "TOTAL", 
                        "count": 3309432, //Total number of transactions done within the selected year-quarter for the current state/district.
                        "amount": 5.899309571743641E9 //Total transaction value within the selected year-quarter for the current state/district.
                    }
                ]
            },

            ...,

            ...,

            {
                "name": "tamil nadu",
                "metric": [
                    {
                        "type": "TOTAL",
                        "count": 136556674,
                        "amount": 2.4866814387365314E11
                    }
                ]
            }            
        ]
    },
    "responseTimestamp": 1630346628834 //Ignore. For internal use only.
}
```

2.2 data/map/user/hover/country/india/2021/1.json
Total number of registered users and number of app opens by these registered users at the state level.

For complete details on syntax find the comments in below code

NOTE: Similar syntax is followed for district level too. Ex: data/map/user/hover/country/india/state/delhi/2021/1.json
```json
{
    "success": true, //Ignore. For internal use only.
    "code": "SUCCESS", //Ignore. For internal use only.
    "data": {
        "hoverData": { //Internally, this being used to show state/district level data whenever a user hovers on a particular state/district.
            "puducherry": {
                "registeredUsers": 346279, //Total number of registered users for the selected state/district
                "appOpens": 7914507 //Total number of app opens by the registered users for the selected state/district
            },

            ...,

            ...,

            "tamil nadu": {
                "registeredUsers": 16632608,
                "appOpens": 348801714
            }
        }
    },
    "responseTimestamp": 1630346628866 //Ignore. For internal use only.
}
```
<h3>Table Schema</h3>

<h4>1.Transaction</h4>
1.1 Aggregate Transactions</br>
| transaction_type | year | quarter | transactions_M | amount_cr |</br>
</br>
1.2 Map Transactions</br>
| state | year | quarter | transactions_M | amount_cr |</br>

<h4>2.User</h4>
2.1 Aggregate Users</br>
| brand | transactions_M | percentage | year | quarter |</br>
</br>
2.2 Aggregate Transactions</br>
| year | quarter | state | users_registered_M | appOpens_M |</br>

<h3>Run the application</h3>
Run the application: <code> streamlit run main.py </code>
