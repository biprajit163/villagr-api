const express = require('express');
const cors = require('cors');
const app = express();
const routers = require('./controllers.js');


app.use(express.json());
app.use(express.urlencoded({ extended: true }))
app.use(cors());


// Routers
app.use('/api', routers);

app.use('/', (req, res) => {
    res.send('We are on Home page');
});





// Listen port

app.set("port", process.env.PORT || 4040);

app.listen(app.get("port"), () => {
  console.log(`App is running on PORT: ${app.get("port")}`);
});




