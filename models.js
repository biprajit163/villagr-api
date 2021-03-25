
const mongoose = require('./connection.js')

const businessSchema = {
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
    lat_long: [Number],
    loan_size_rank_by_state: Number,
    loan_amount_by_zip_percentile: Number,
    loan_amount_by_type_percentile: Number,
    loan_amount_by_city_percentile: Number,
    zipcode_urgency: String,
    typ_urgency: String,
    city_urgency: String,
    loan_size_urgency: String
}

const Business = mongoose.model("Business", businessSchema);

module.exports = Business;
