
const mongoose = require('./connection.js')

const businessSchema = {
    index: Number,
    business_name: String,
    street_address: String,
    city: String,
    state: String,
    zip_code_first5: String,
    zip_code_last4: Number,
    congressional_district: Number,
    business_type: String,
    loan_amount: Number, 
    loan_net_proceeds_UNSURE: Number,
    full_address: String,
    lat_long: [Number]
}

const Business = mongoose.model("Business", businessSchema);

module.exports = Business;
