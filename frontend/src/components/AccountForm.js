import axios from "./axiosFactory";
import htmx from "htmx.org/dist/htmx";
import iziToast from 'izitoast/dist/js/iziToast.min.js';  // you have access to iziToast now
import {isValid, isExpirationDateValid, getCreditCardNameByNumber} from 'creditcard.js';

function sleep(ms) {
    return new window.Promise(resolve => setTimeout(resolve, ms));
}

function validateField(formElement, fieldElement) {
    let formData = new FormData(formElement);
    formData.append("__field_name__", fieldElement.name);

    if(document.getElementById('id_card_provider')) {
        var providerN = document.getElementById('id_card_provider');
        providerN.readOnly = true;
    }

    axios.post(formElement.action, formData).then(function (response) {
      let errors = response.data.errors;
      let errorsWrapperElement = document.getElementById(`error-wrapper-${fieldElement.name}`);
      if (errors.length === 0) {
        if (document.getElementById('submitForm')) document.getElementById('submitForm').classList.remove('hidden');
        if (document.getElementById('subscribeDriver')) document.getElementById('subscribeDriver').classList.remove('hidden');
        if (document.getElementById('subscribeCompany')) document.getElementById('subscribeCompany').classList.remove('hidden');
        errorsWrapperElement.classList.add('hidden');
        if (errorsWrapperElement) {
          errorsWrapperElement.innerHTML = "";
        }
      } else {
        if (document.getElementById('submitForm')) document.getElementById('submitForm').classList.add('hidden');
        if (document.getElementById('subscribeDriver')) document.getElementById('subscribeDriver').classList.add('hidden');
        if (document.getElementById('subscribeCompany')) document.getElementById('subscribeCompany').classList.add('hidden');
        errorsWrapperElement.classList.remove('hidden');
        errorsWrapperElement.classList.add('flex');
        if (errorsWrapperElement) {
          let errorsHtml = '';
          for (let i = 0; i < errors.length; i++) {
            errorsHtml += `${errors[i]}`;
          }
          errorsWrapperElement.innerHTML = errorsHtml;
        }


      }

        //   cc validator
      if(document.getElementById("id_card_exp_month") || document.getElementById("id_card_exp_year") || document.getElementById("id_card_no")) {
        var month = document.getElementById("id_card_exp_month");
        var year = document.getElementById("id_card_exp_year");
        var number = document.getElementById("id_card_no");
        var valid = document.getElementById(`error-wrapper-card_exp_year`);
        var card_no = document.getElementById(`error-wrapper-card_no`);
        var img = document.getElementById(`provider`);
        console.log(number.value);
        console.log(year.value);
        var expired = isExpirationDateValid(`${month.value}`, `${year.value}`);
        var provider = getCreditCardNameByNumber(`${number.value}`);
        var vcard = isValid(`${number.value}`);

        if(expired == true) {
            valid.classList.remove('hidden', 'bg-red-200', 'text-red-600');
            valid.classList.add('flex', 'bg-green-200', 'text-green-600');
            valid.innerHTML = "Not yet expired";
            if (document.getElementById('submitForm')) document.getElementById('submitForm').classList.remove('hidden');
        } else {
            valid.classList.add('hidden', 'bg-red-200', 'text-red-600');
            valid.classList.remove('flex', 'bg-green-200', 'text-green-600');
            valid.innerHTML = "Card has expired";
            if (document.getElementById('submitForm')) document.getElementById('submitForm').classList.add('hidden');
        }

        if(vcard == true) {
            card_no.classList.remove('hidden', 'bg-red-200', 'text-red-600');
            card_no.classList.add('flex', 'bg-green-200', 'text-green-600');
            card_no.innerHTML = "Valid Card Number";
            if (document.getElementById('submitForm')) document.getElementById('submitForm').classList.remove('hidden');
        } else {
            card_no.classList.add('hidden', 'bg-red-200', 'text-red-600');
            card_no.classList.remove('flex', 'bg-green-200', 'text-green-600');
            card_no.innerHTML = "Not A Valid Card Number";
            if (document.getElementById('submitForm')) document.getElementById('submitForm').classList.add('hidden');
        }

        if(provider === 'Visa') {
            img.src = "https://upload.wikimedia.org/wikipedia/commons/thumb/5/5e/Visa_Inc._logo.svg/800px-Visa_Inc._logo.svg.png?20170118154621";
        } else if (provider === 'Mastercard') {
            img.src = 'https://upload.wikimedia.org/wikipedia/commons/thumb/2/2a/Mastercard-logo.svg/772px-Mastercard-logo.svg.png?20210817144358';
        }


        providerN.value = provider;
      }

      if(response.data.avatar){
        document.getElementById('avatar').src = response.data.avatar;
      }
    });
  }


export default function AccountForm() {
    return {
        processing: false,

        async submitForm() {
            this.processing = true;

            const formElement = this.$refs.form;
            const div = document.getElementById('form');
            const action = formElement.action;
            const redirect = formElement.dataset.errorurl || formElement.dataset.redirect;
            const csrf = formElement.dataset.csrf;
            let data = new FormData(formElement);
            formElement.querySelectorAll("[name]").forEach(fieldElement => {
                if (fieldElement.type === "textarea") {
                    let textarea = fieldElement.id;
                    console.log('textarea content: ', window.parent.tinymce.get(textarea).getContent());
                    data.append(fieldElement.name, window.parent.tinymce.get(textarea).getContent());
                }

                if (fieldElement.type !== "textarea"){
                    data.append(fieldElement.name, fieldElement.value);
                }
            });

            if (formElement.checkValidity()) {
                await axios.post(action, data, {
                    headers: {
                      'X-CSRFToken': csrf,
                    }})
                    .then(function (response) {

                        div.appendChild(formElement);
                        sleep(4500); //wait 1 sec and then htmx redirect get
                        if (response.status === 200 || response.status === 201) {
                            iziToast.success({
                                title: response.data.title,
                                balloon: true,
                                position: "topRight",
                                animateInside: true,
                                message: response.data.message
                            });
                            // location.reload();
                        }

                        if(response.data.username) {
                            return window.location.replace(`${window.location.origin}/users/${response.data.username}/`);
                        }

                        if (redirect) {
                            return window.location.replace(redirect); // htmx.ajax('GET', redirect, {target:'body', swap:'outerHTML'});
                        }

                    }).catch(function (error) {

                        if (error.response && error.response.status === 403) {
                            return iziToast.error({
                                title: error.response.data.title,
                                balloon: true,
                                position: "topRight",
                                animateInside: true,
                                message: error.response.data.message
                            });
                        }

                        return iziToast.error({
                            title: "Form Error",
                            balloon: true,
                            position: "topRight",
                            animateInside: true,
                            message: `Something wrong happened: ${error}`
                        });

                        // sleep(7500); //wait 1 sec and then htmx redirect get
                        // return window.location.reload();
                    });

                this.processing = false;
            }

        },

        async submitSignupForm() {
            this.processing = true;

            const formElement = this.$refs.form;
            const action = formElement.action;
            const redirect = formElement.dataset.errorurl || formElement.dataset.redirect;
            const csrf = formElement.dataset.csrf;
            let data = new FormData(formElement);
            formElement.querySelectorAll("[name]").forEach(fieldElement => {
                if (fieldElement.type === "textarea") {
                    let textarea = fieldElement.id;
                    console.log('textarea content: ', window.parent.tinymce.get(textarea).getContent());
                    data.append(fieldElement.name, window.parent.tinymce.get(textarea).getContent());
                }

                if (fieldElement.type !== "textarea"){
                    data.append(fieldElement.name, fieldElement.value);
                }
            });

            if (formElement.checkValidity()) {
                await axios.post(action, data, {
                    headers: {
                      'X-CSRFToken': csrf,
                    }})
                    .then(function (response) {
                        iziToast.success({
                            title: "SINGUP SUCCESSFUL",
                            balloon: true,
                            position: "topRight",
                            animateInside: true,
                            message: "You have successfully registered a new account" + response
                        });
                        sleep(7500); //wait 1 sec and then htmx redirect get
                        return window.location.replace(redirect);

                    }).catch(function (error) {

                        return iziToast.error({
                            title: "SIGNUP FORM ERROR",
                            balloon: true,
                            position: "topRight",
                            animateInside: true,
                            message: `Something wrong happened: ${error}`
                        });
                    });

                this.processing = false;
            }

        },

        async submitCodeForm() {
            const formElement = this.$refs.form;
            const action = formElement.action;
            const el = document.getElementById('code');
            const redirect = formElement.dataset.redirect;
            const csrf = formElement.dataset.csrf;
            let data = new FormData(formElement);
            formElement.querySelectorAll("[name]").forEach(fieldElement => {
                if (fieldElement.type === "textarea") {
                    let textarea = fieldElement.id;
                    console.log('textarea content: ', window.parent.tinymce.get(textarea).getContent());
                    data.append(fieldElement.name, window.parent.tinymce.get(textarea).getContent());
                }

                if (fieldElement.type !== "textarea"){
                    data.append(fieldElement.name, fieldElement.value);
                }
            });

            if (formElement.checkValidity()) {
                await axios.get(action, data, {
                    headers: {
                      'X-CSRFToken': csrf,
                    }})
                    .then(function (response) {
                        if (response.status === 200) {
                            iziToast.success({
                                title: response.data.title,
                                balloon: true,
                                position: "topRight",
                                animateInside: true,
                                message: response.data.message
                            });
                            el.classList.add('hidden');
                            sleep(7500); //wait 1 sec and then htmx redirect get
                            return window.location.replace(redirect);
                        }

                    }).catch(function (error) {

                        return iziToast.error({
                            title: error.response.data.title,
                            balloon: true,
                            position: "topRight",
                            animateInside: true,
                            message: error.response.data.message
                        });
                    });
            }

        },

        async deleteForm() {
            this.processing = true;
            const formElement = this.$refs.form;
            const csrf = formElement.dataset.csrf;
            const action = formElement.action;
            const redirect = formElement.dataset.redirect;
            let data = new FormData(formElement);
            formElement.querySelectorAll("[name]").forEach(fieldElement => {
                if (fieldElement.type === "textarea") {
                    let textarea = fieldElement.id;
                    console.log('textarea content: ', window.parent.tinymce.get(textarea).getContent());
                    data.append(fieldElement.name, window.parent.tinymce.get(textarea).getContent());
                }

                if (fieldElement.type !== "textarea"){
                    data.append(fieldElement.name, fieldElement.value);
                }
            });

            if (formElement.checkValidity()) {
                await axios.post(action, data, {
                    headers: {
                      'X-CSRFToken': csrf,
                    }})
                    .then(function (response) {
                        if (response.status === 200) {
                            iziToast.success({
                                title: response.data.title,
                                balloon: true,
                                position: "topRight",
                                animateInside: true,
                                message: response.data.message
                            });
                            sleep(7500); //wait 1 sec and then htmx redirect get
                            return location.replace(redirect);
                        }

                    }).catch(function (error) {

                        return iziToast.error({
                            title: error.response.data.title,
                            balloon: true,
                            position: "topRight",
                            animateInside: true,
                            message: error.response.data.message
                        });
                    });
            }
            this.processing = true;
        },

        async submitUpdateForm() {
            this.processing = true;
            const formElement = this.$refs.form;
            const action = formElement.action;
            const redirect = formElement.dataset.redirect;
            const csrf = formElement.dataset.csrf;
            let data = new FormData(formElement);
            formElement.querySelectorAll("[name]").forEach(fieldElement => {
                if (fieldElement.type === "textarea") {
                    let textarea = fieldElement.id;
                    console.log('textarea content: ', window.parent.tinymce.get(textarea).getContent());
                    data.append(fieldElement.name, window.parent.tinymce.get(textarea).getContent());
                }

                if (fieldElement.type !== "textarea"){
                    data.append(fieldElement.name, fieldElement.value);
                }
            });

            if (formElement.checkValidity()) {
                await axios.post(action, data, {
                    headers: {
                      'X-CSRFToken': csrf,
                      'Content-Type':'multipart/form-data'
                    }})
                    .then(function (response) {
                        if (response.status === 200 || response.status == 201) {
                            iziToast.success({
                                title: response.data.title,
                                balloon: true,
                                position: "topRight",
                                animateInside: true,
                                message: response.data.message
                            });
                            sleep(7500); //wait 1 sec and then htmx redirect get
                            return htmx.ajax('GET', redirect, {target:'body', swap:'outerHTML'});
                        }

                    }).catch(function (error) {

                        return iziToast.error({
                            title: error.response.data.title,
                            balloon: true,
                            position: "topRight",
                            animateInside: true,
                            message: error.response.data.message
                        });
                    });
            }
            this.processing = true;
        },

        async submitEmailConfirmForm() {
            this.processing = true;

            const formElement = this.$refs.form;
            const action = formElement.action;
            const redirect = formElement.dataset.redirect;
            const csrf = formElement.dataset.csrf;
            let data = new FormData(formElement);
            formElement.querySelectorAll("[name]").forEach(fieldElement => {
                if (fieldElement.type === "textarea") {
                    let textarea = fieldElement.id;
                    console.log('textarea content: ', window.parent.tinymce.get(textarea).getContent());
                    data.append(fieldElement.name, window.parent.tinymce.get(textarea).getContent());
                }

                if (fieldElement.type !== "textarea"){
                    data.append(fieldElement.name, fieldElement.value);
                }
            });

            if (formElement.checkValidity()) {
                await axios.post(action, data, {
                    headers: {
                      'X-CSRFToken': csrf,
                    }})
                    .then(function (response) {

                        iziToast.success({
                            title: "EMAIL CONFIRMATION  SUCCESSFUL",
                            balloon: true,
                            position: "topRight",
                            animateInside: true,
                            message: "You have successfully confirmed your email address" + response.data.message
                        });
                        sleep(7500); //wait 1 sec and then htmx redirect get
                        if(response.data.redirect) return window.location.replace(response.data.redirect);

                        window.location.replace(redirect);
                    }).catch(function (error) {

                        return iziToast.error({
                            title: "EMAIL CONFIRMATION ERROR",
                            balloon: true,
                            position: "topRight",
                            animateInside: true,
                            message: `Something wrong happened: ${error}`
                        });
                    });

                this.processing = false;
            }

        },

        async submitLoginForm() {
            this.processing = true;

            const formElement = this.$refs.form;
            const action = formElement.action;
            const redirect = formElement.dataset.errorurl || formElement.dataset.redirect;
            const csrf = formElement.dataset.csrf;
            let data = new FormData(formElement);
            formElement.querySelectorAll("[name]").forEach(fieldElement => {
                if (fieldElement.type === "textarea") {
                    let textarea = fieldElement.id;
                    console.log('textarea content: ', window.parent.tinymce.get(textarea).getContent());
                    data.append(fieldElement.name, window.parent.tinymce.get(textarea).getContent());
                }

                if (fieldElement.type !== "textarea"){
                    data.append(fieldElement.name, fieldElement.value);
                }
            });

            if (formElement.checkValidity()) {
                await axios.post(action, data, {
                    headers: {
                      'X-CSRFToken': csrf,
                    }})
                    .then(function (response) {
                        iziToast.success({
                            title: "LOGIN SUCCESSFUL",
                            balloon: true,
                            position: "topRight",
                            animateInside: true,
                            message: "You have successfully logged into your account" + response
                        });
                        sleep(7500); //wait 1 sec and then htmx redirect get
                        return window.location.replace(redirect);

                    }).catch(function (error) {

                        return iziToast.error({
                            title: "LOGIN FORM ERROR",
                            balloon: true,
                            position: "topRight",
                            animateInside: true,
                            message: `Something wrong happened: ${error}`
                        });
                    });

                this.processing = false;
            }

        },

        async submitPasswordForm() {
            this.processing = true;

            const formElement = this.$refs.form;
            const action = formElement.action;
            const redirect = formElement.dataset.redirect;
            // const eredirect = formElement.dataset.errorurl;
            const csrf = formElement.dataset.csrf;
            let data = new FormData(formElement);
            formElement.querySelectorAll("[name]").forEach(fieldElement => {
                if (fieldElement.type === "textarea") {
                    let textarea = fieldElement.id;
                    console.log('textarea content: ', window.parent.tinymce.get(textarea).getContent());
                    data.append(fieldElement.name, window.parent.tinymce.get(textarea).getContent());
                }

                if (fieldElement.type !== "textarea"){
                    data.append(fieldElement.name, fieldElement.value);
                }
            });

            if (formElement.checkValidity()) {
                await axios.post(action, data, {
                    headers: {
                      'X-CSRFToken': csrf,
                    }})
                    .then(function (response) {
                        iziToast.success({
                            title: "PASSWORD SUCCESSFULLY UPDATED",
                            balloon: true,
                            position: "topRight",
                            animateInside: true,
                            message: response
                        });
                        sleep(7500); //wait 1 sec and then htmx redirect get
                        return window.location.replace(redirect);


                    }).catch(function (error) {

                        return iziToast.error({
                            title: "PASSWORD FORM ERROR",
                            balloon: true,
                            position: "topRight",
                            animateInside: true,
                            message: `Something wrong happened: ${error}`
                        });
                    });

                this.processing = false;
            }

        },

        async showPassword() {
            var x = document.getElementById("id_password");
            if (x.type === "password") {
              x.type = "text";
            } else {
              x.type = "password";
            }
        },

        async showSingupPassword() {
            var x = document.getElementById("id_password1");
            var y = document.getElementById("id_password2");
            if (x.type === "password" && y.type === "password") {
              x.type = "text";
              y.type = "text";
            } else {
              x.type = "password";
              y.type = "password";
            }
        },

        async submitFileForm() {
            this.processing = true;

            const formElement = this.$refs.form;
            const div = document.getElementById('form');
            const action = formElement.action || window.location;
            const redirect = formElement.dataset.redirect;
            const csrf = formElement.dataset.csrf;
            let data = new FormData(formElement);
            formElement.querySelectorAll("[name]").forEach(fieldElement => {
                if (fieldElement.type === "textarea") {
                    let textarea = fieldElement.id;
                    console.log('textarea content: ', window.parent.tinymce.get(textarea).getContent());
                    data.append(fieldElement.name, window.parent.tinymce.get(textarea).getContent());
                }

                if (fieldElement.type !== "textarea"){
                    data.append(fieldElement.name, fieldElement.value);
                }
            });

            if (formElement.checkValidity()) {
                await axios.post(action, data, {
                    headers: {
                      'X-CSRFToken': csrf,
                      'Content-Type':'multipart/form-data'
                    }})
                    .then(function (response) {
                        div.appendChild(formElement);
                        if (response.status === 200 || response.status === 201) {
                            iziToast.success({
                                title: response.data.title,
                                balloon: true,
                                position: "topRight",
                                animateInside: true,
                                message: response.data.message
                            });
                            sleep(4500); //wait 1 sec and then htmx redirect get
                            if (redirect) {
                                return htmx.ajax('GET', redirect, {target:'body', swap:'outerHTML'});
                            }
                            return;
                        }
                    }).catch(function (error) {
                        if (error.response && error.response.status === 403) {
                            iziToast.error({
                                title: error.response.data.title,
                                balloon: true,
                                position: "topRight",
                                animateInside: true,
                                message: error.response.data.message
                            });
                        }
                        iziToast.error({
                            title: "Form Error",
                            balloon: true,
                            position: "topRight",
                            animateInside: true,
                            message: `Something wrong happened: ${error}`
                        });
                    });

                this.processing = false;
            } else {
                iziToast.error({
                    title: "Form Sending Incomplete",
                    balloon: true,
                    position: "topRight",
                    animateInside: true,
                    message: `Form data is not valid. Ensure you have filled all fields accurately! ${formElement.reportValidity()}`
                });
                sleep(5500); //wait 2.5 sec and then htmx redirect get
                this.processing = false;
                htmx.ajax('GET', redirect, {target:'body', swap:'outerHTML'});
            }

        },

        async checkValidity() {
            const formElement = this.$refs.form;
            formElement.querySelectorAll('[name]').forEach(fieldElement => {
                fieldElement.addEventListener('change', event => {
                    console.log(event);
                    validateField(formElement, fieldElement);
                });
            });
        },

        getBtnText() {
            return this.processing ? 'Processing...' : 'Submit';
        }
    };
}
