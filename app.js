const express = require('express');
const cors = require('cors');

const app = express();


app.use(express.json());
app.use(express.urlencoded({ 
    extended: true
}))
app.use(cors());


// Database connection

const mongoURI = 
    process.env.NODE_ENV === 'production' 
    ? process.env.DB_URI 
    : 'mongodb://localhost:27017/business-data';




// Routers
app.use('/', (req, res) => {
    res.send('We are on Home page');
});

// Listen port
const PORT = process.env.PORT || 4040;

app.listen(PORT, () => {
    if (PORT === process.env.PORT) {
        console.log(`App is running on => ${PORT}`)
    } else {
        console.log(`App is running on => http://localhost:${PORT}`);
    }
});
