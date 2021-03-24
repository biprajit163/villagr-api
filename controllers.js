
const express = require('express');
const router = express.Router();
const Business = require('./models.js');


router.get('/', (req, res) => {
    const page = parseInt(req.query.page);
    const limit = parseInt(req.query.limit);
    const startIndex = (page - 1) * limit;
    const endIndex = page * limit;

    Business.find({})
        .then(data => {
            let resData = {
                results: data.length,
                data: Array
            };

            resData.data = data.slice(startIndex, endIndex);
            res.json(resData)
        })
        .catch(err => console.log(err));
});


module.exports = router;