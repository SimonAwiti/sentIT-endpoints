[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Coverage Status](https://coveralls.io/repos/github/SimonAwiti/sentIT-endpoints/badge.svg)](https://coveralls.io/github/SimonAwiti/sentIT-endpoints)
# sentIT Application
# sentIT application endpoints

## The following are API endpoints enabling one to: 
* Create account and log in
* Create a parcel delivery order
* Change the destination of the parcel through editing 
* View the made parcel orders details 
* Delete a made parcel order 
* View all parcel orders created
## Here is a list of the functioning endpoints

| EndPoint                      | Functionality                    |  Actual routes                |
| :---                          |     :---:                        |    :---:                      |
| GET /parcel order             | Get all available orders         |  /api/v1/orders/              |
| GET /parcel order/<orderId>   | Fetch a single order details     |  /api/v1/orders/<orderid>     |
| Edit /parcel order/<orderId>  | Changin the details of the order |  /api/v1/orders/<orderid>     |
| PUT /parcel order/<orderId>   | Cancel a single parcel order     |  /api/v1/orders/<orderid>     |
| POST /parcel order            | Create a parcel order            |  /api/v1/orders/              |
| POST /users                   | User log in                      |  /api/v1/users/login          |
| POST /users                   | User registration                |  /api/v1/users/register       |

  
## Extra endpoints include 
* Admin can be able to add another admin

## Testing the endpoints

* Install python then using pip install .. install flask
* clone the repo
* Ensure that postman is installed
* From your terminal locate the repo and run: python run.py
* open postman and test the endpoints
* Use unittest to run the the tests

## Setting up and how to start the application

* Install python then using pip instal .. install flask
* clone the repo
* From your terminal Ensure that the virtual environment is activated
* From the terminal locate the repo and run: python run.py

## Technology used

* Python 3.6
* Flask framework
* Unittest for testing

## Background context 

Published POSTMAN documentation
[Documentation](https://documenter.getpostman.com/view/5353857/RWgtTwtr#intro)

# Written by: Simon Awiti
#### Copyright © Andela 2018 

