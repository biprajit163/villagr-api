
const mongoose = require('mongoose');


const mongoURI = 
    process.env.NODE_ENV === 'production' 
    ? process.env.DB_URL 
    : 'mongodb://localhost:27017/business-data';



mongoose.connect(mongoURI, {
    useNewUrlParser: true,
    useCreateIndex: true,
    useUnifiedTopology: true,
    useFindAndModify: false,
})
.then(instance => {
console.log(instance.connections[0].name);
})
.catch(err => console.log('Connection Failed'));


module.exports = mongoose;
