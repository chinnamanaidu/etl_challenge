# Guidelines for ETL Project

This document contains guidelines, requirements, and suggestions for Project 1.

## Team Effort
# The team members for this project Ravi Chinnamanaidu, Ashni Dattani and Richard

The main purpose of the project is to get the data from web, and do necessary transformation and cleaning and upload into the DB table.

Initially some of the websites are taken for analysis like https://data.world  and https://kaggle.com , most of the data files they provided are downloadable, the same data could also be obtained through web scrapping., there are different sets of data available on various sectors and industries and we downloaded the files that are required.
The SandP 500 file and Bitcoin file downloaded from data.world and analyzed.

After analysis, notebook file developed to read the csv file, transform the data, clean the data and load into the DB table.  This part completed successfully, there are no issues.

The other action item taken was to get the real time data from https://finance.yahoo.com , initially we went through the most active symbols,  trending symbols and cryptocurrencies.

After more analysis of the html file, we came with plan to get the data of the symbol and its other attributes like name, open price, close price, day high, day low, volume, 
average volume and market capital..,

Then model developed to render the data from the yahoo site, to also make it capable of getting the next page of data, so program is built so it could iterate through all the pages to get the required data and append the arraylist,  this arraylist has the list of json objects.

After parsing through all the pages the arraylist is converted to dataframe object,  the DB create engines are initialized to the postgres DB instance and the data from dataframe is loaded into the table.

After loading the data it is also verified it si loaded and no records are skipped.

There are more challenges in loading the data, some time data is alphanumeric, this needs to be converted to numeric, it has "," in it, this needs to be removed, the M comes for millions, this needs to be converted and B comes for Billion.. and so on all the corrections are updated on price, volume, market capital, average volume and other data sets.

These are the SQLs for the DB 

create table btc_usd (
	trans_date date,
	price float,
	openvalue float,
	dayhighvalue float,
	daylowvalue float,
	volume_btc integer,
	volume_currency integer,
	weighted_price float
)

create table yahoo_most_active (
	trans_date date,
	symbol text,
	company_name text,
	price float,
	day_change text,
	percent_change text,
	volume float,
	avg_volume float,
	market_cap float
)

create table yahoo_most_trending (
	trans_date date,
	symbol text,
	company_name text,
	price float,
	day_change text,
	percent_change text,
	volume float,
	avg_volume float,
	market_cap float
)

create table yahoo_btc_coin (
	trans_date date,
	symbol text,
	company_name text,
	price float,
	day_change text,
	percent_change text,
	total_volume float,
	currency_supply float,
	market_cap float,
	currency_value float,
	currency_value_old float
)   

create table sandp (
	trans_date date,
	price float,
	openvalue float,
	dayhighvalue float,
	daylowvalue float,
	percent_change text
)

The file Bitcoin_data.ipynb  used to read the bitcoin_data.csv file from data.world website, it has the date, and other attributes for btc_usd symbol.

The file dta_etl.ipynb used to read the sp.csv file to prepare Standard and Poor 500 stats data into the sandp table.

The file web_etl.ipynb used to prepare the most active symbols on yahoo website, get data for top 200 and uploads into the DB table.

The file web_etl_trending.ipynb used to get the trending symbol from yahoo website

The file web_etl_btc_coin.ipynb used to get the crypto currency data from yahoo website and upload in the DB table.

## Data Cleanup & Analysis

Once you have identified your datasets, perform ETL on the data. Make sure to plan and document the following:

* The sources of data that you will extract from.

* The type of transformation needed for this data (cleaning, joining, filtering, aggregating, etc).

* The type of final production database to load the data into (relational or non-relational).

* The final tables or collections that will be used in the production database.

You will be required to submit a final technical report with the above information and steps required to reproduce your ETL process.

## Project Report

At the end of the week, your team will submit a Final Report that describes the following:

* **E**xtract: your original data sources and how the data was formatted (CSV, JSON, pgAdmin 4, etc).
In yahoo web scrapping notebook you could see data is extracted on various pages and formatted.

* **T**ransform: what data cleaning or transformation was required.
The data is transformed when doing the screen scrapping to remove "," from numerics and transform M and B to Million and Billion data.

* **L**oad: the final database, tables/collections, and why this was chosen.
The json object loaded into the DB table.
Please upload the report to Github and submit a link to Bootcampspot.

- - -

### Copyright

Coding Boot Camp © 2019. All Rights Reserved.
