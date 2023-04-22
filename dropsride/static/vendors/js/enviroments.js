const GOOGLE_API_KEY = process.env.GOOGLE_API_KEY;
const GOOGLE_CAPTCHA_SITE_KEY = process.env.GOOGLE_CAPTCHA_SITE_KEY;
const GOOGLE_CAPTCHA_SECRET_KEY = process.env.GOOGLE_CAPTCHA_SECRET_KEY;
const TINYMCE_KEY = process.env.TINYMCE_KEY;
const PAYSTACK_LIVE_SK = process.env.PAYSTACK_LIVE_SK;
const PAYSTACK_LIVE_PK = process.env.PAYSTACK_LIVE_PK;
const PAYSTACK_TEST_SK = process.env.PAYSTACK_TEST_SK;
const PAYSTACK_TEST_PK = process.env.PAYSTACK_TEST_PK;

export{
    GOOGLE_API_KEY,
    GOOGLE_CAPTCHA_SITE_KEY,
    GOOGLE_CAPTCHA_SECRET_KEY,
    TINYMCE_KEY,
    PAYSTACK_LIVE_SK,
    PAYSTACK_LIVE_PK,
    PAYSTACK_TEST_SK,
    PAYSTACK_TEST_PK,
};

// import {GOOGLE_API_KEY} from ./enviroments.js to use the enviroment variables where necessary
