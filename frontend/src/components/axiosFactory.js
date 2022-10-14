import axios from "axios";

axios.defaults.withCredentials = true;
axios.defaults.xsrfCookieName = 'csrftoken';
axios.defaults.xsrfHeaderName = "X-CSRFTOKEN";
// axios.defaults.headers['X-CSRFToken'] = document.head.querySelector('meta[name="csrf-token"]').getAttribute('content');
axios.defaults.timeout = 15000;

export default axios;
