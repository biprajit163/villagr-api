
# Villagr API

## API Description
This API connects with COVID-19 Economic Injury Disaster Loans dataset, which is hosted on the cloud platform MongoDb Atlas. the API then uses Express, a node.js framework, to make a REST API that can call to the database and get back business data with API routing endpoints. The API is hosted on heroku (https://villagr.herokuapp.com/api), and the API calls allows the frontend team to fetch all the business data available in the database. The database consists of businesses data from Virgina, Washington DC, businesses that recieved the most COVID-19 aid, and the different business types. The API utalizes a limit function to its routing calls that allow the programers to decide how much data they want to call in order to make rendering easier on the frontend. 


## Team memmbers
#### User Experience Designers
- Diana Kao = https://www.linkedin.com/in/dianakao1/ 
- Eileen Ward = https://www.linkedin.com/in/eileentward/

#### Software Engineers
- Biprajit Majumder = https://github.com/biprajit163
- Ben Ritter = https://github.com/benritter522
- David Tersoff = https://github.com/dtersoff

#### Data Scientists
- Aaron Hume = https://github.com/1aaronh
- Song May = https://github.com/SingingCat717


## Technologies used
- Express.js, Mongoose, MongoDB 
- Python, Pandas, GeoPy


## Framework 
![backend-framework - Copy](https://user-images.githubusercontent.com/14338321/112692687-b5e54d00-8e55-11eb-8685-45eb54c976cc.png)

 
### Credit
- Data Source = https://www.sba.gov/funding-programs/loans/covid-19-relief-options/covid-19-economic-injury-disaster-loan#section-header-12


## Future Plans and Implementations
We were limited with the resources given to us, we hosted our database on MongoDB Atlas the free version has a storage capacity of 512 MB but our nationwide datae would take up 2GB of storage. We could have arguably gotten data for multiple states but since we were hosting our API on Heroku, the Heroku servers has a set timeout of 30 sec before it
crashes. So to resolve the issues we settled on Virginia and DC data so the API can make HTTP requests to the backend without crashing. If given the appropriate resources we would like to implement data from more states and use this Yelp data set we have premade to match businesses with customer ratings. This way the user can get more information about which businesses provide the best services and they can still help their favorite business.    