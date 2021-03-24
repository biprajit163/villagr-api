
const Business = require('./models.js');
const seedData = require('./test-data.json');


Business.deleteMany({})
    .then(() => {
        return Business.insertMany(seedData);
    })
    .then(() => console.log('data seeded'))
    .catch(err => console.log(`Something went wrong ${err}`))
    .finally(() => process.exit())
