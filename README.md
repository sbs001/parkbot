# Parkbot :robot:

In this application you can get parking spaces according to location and hourly price.

## Enviroment

The application requires to have installed Python.
You can downolad it in https://www.python.org

## Install instructions

To use Parkbot, clone this repository into your directory.

Use the next command in your console:
````
$ git clone https://github.com/sbs001/parkbot.git
````
Now, get into parkbot directory

````
$ cd parkbot
````

## How to use

Format:
```
$python3 parkbot airgarage-data.json [command] [argument]
```

### Allowed Commands 

`locate`: This command will return a list of spot names by location (state only). Example: `locate AZ` will return spots in Arizona 

`find_price_hourly_lte`.  This command will return a list of spot names where the hourly price is less than or equal to the query price. (Note: the price is in cents).
 Example: `find_price_hourly_lte 200` will return spots that are less than or equal to $2 per hour.
 
 `find_price_hourly_gt`.  This command will return a list of spot names where the price is greater than the query price. (Note: the price is in cents).
 Example: `find_price_hourly_gt 200`  will return spots that are greater than $2.00 per hour.
 
 
 ### Example output

```
$ python3 parkbot airgarage-data.json locate AZ
Tempe Beach Park, Safeway, Azusa Ramen
```
```
$ python3 parkbot airgarage-data.json find_price_hourly_lte 200
Church of 8 Wheels, Tempe Beach Park, AirGarage HQ, Safeway, Walgreens, Goldilocks Pizza, The Salon, Archer Salon
```
```
$ python3 parkbot airgarage-data.json find_price_hourly_gt 200
Sweetgreen, Sandwiches n More, Azusa Ramen
```

### DEMO

![Peek 27-07-2021 11-57](https://user-images.githubusercontent.com/50562395/127177801-634e248e-bc16-4c42-b258-685e034338a7.gif)

