create database finance_db

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