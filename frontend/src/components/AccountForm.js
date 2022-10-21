import axios from "./axiosFactory";
import htmx from "htmx.org/dist/htmx";
import iziToast from 'izitoast/dist/js/iziToast.min.js';  // you have access to iziToast now


function sleep(ms) {
    return new window.Promise(resolve => setTimeout(resolve, ms));
}

function validateField(formElement, fieldElement) {
    let formData = new FormData(formElement);
    formData.append("__field_name__", fieldElement.name);

    axios.post(formElement.action, formData).then(function (response) {
      let errors = response.data.errors;
      let errorsWrapperElement = document.getElementById(`error-wrapper-${fieldElement.name}`);
      if (errors.length === 0) {
        document.getElementById('submitForm').classList.remove('hidden');
        errorsWrapperElement.classList.add('hidden');
        if (errorsWrapperElement) {
          errorsWrapperElement.innerHTML = "";
        }
      } else {
        document.getElementById('submitForm').classList.add('hidden');
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
                        // console.info("RESPONSE DATA: ", response);

                        if (response.status === 200 || response.status === 201) {
                            div.innerHTML = `
                            ${formElement}
                            `;
                            iziToast.success({
                                title: response.data.title,
                                balloon: true,
                                position: "topRight",
                                animateInside: true,
                                message: response.data.message
                            });
                            sleep(3500); //wait 1 sec and then htmx redirect get
                            htmx.ajax('GET', redirect, {target:'main', swap:'outerHTML'});
                            // sleep(3500); //wait 1 sec and then htmx redirect get
                            // location.reload();
                        } else if (response.status === 403) {
                            iziToast.error({
                                title: response.data.title,
                                balloon: true,
                                position: "topRight",
                                animateInside: true,
                                message: response.data.message
                            });
                            // sleep(3500); //wait 1 sec and then htmx redirect get
                            htmx.ajax('GET', response.data.success_url, {target:'main', swap:'outerHTML'});
                        }else {
                            iziToast.error({
                                title: response.data.title,
                                balloon: true,
                                position: "topRight",
                                animateInside: true,
                                message: response.data.message
                            });
                        }

                        console.log(response);
                    }).catch(function (error) {
                        if (error.response.status === 403) {
                            iziToast.error({
                                title: error.response.data.title,
                                balloon: true,
                                position: "topRight",
                                animateInside: true,
                                message: error.response.data.message
                            });
                            // sleep(3500); //wait 1 sec and then htmx redirect get
                            return htmx.ajax('GET', error.response.data.success_url, {target:'body', swap:'outerHTML'});
                        }
                        iziToast.error({
                            title: "Form Error",
                            balloon: true,
                            position: "topRight",
                            animateInside: true,
                            message: `Something wrong happened: ${error}`
                        });
                    });
                    // .finally(function () {
                    //     console.log("finally");
                    // });

                this.processing = false;
            } else {
                iziToast.error({
                    title: "Form Sending Incomplete",
                    balloon: true,
                    position: "topRight",
                    animateInside: true,
                    message: `Form data is not valid. Ensure you have filled all fields accurately! ${formElement.reportValidity()}`
                });
                sleep(2500); //wait 2.5 sec and then htmx redirect get
                this.processing = false;
                htmx.ajax('GET', redirect, {target:'main', swap:'outerHTML'});
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
            var x = document.getElementById("id_password");
            if (x.type === "password") {
              x.type = "text";
            } else {
              x.type = "password";
            }
        },

        async submitFileForm() {
            this.processing = true;

            const formElement = this.$refs.form;
            const div = document.getElementById('form');
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
                        // console.info("RESPONSE DATA: ", response);

                        if (response.status === 200 || response.status === 201) {
                            div.innerHTML = `
                            ${formElement}
                            `;
                            iziToast.success({
                                title: response.data.title,
                                balloon: true,
                                position: "topRight",
                                animateInside: true,
                                message: response.data.message
                            });
                            sleep(3500); //wait 1 sec and then htmx redirect get
                            htmx.ajax('GET', redirect, {target:'body', swap:'outerHTML'});
                            // sleep(3500); //wait 1 sec and then htmx redirect get
                            // location.reload();
                        } else {
                            iziToast.error({
                                title: response.data.title,
                                balloon: true,
                                position: "topRight",
                                animateInside: true,
                                message: response.data.message
                            });
                        }

                        console.log(response);
                    }).catch(function (error) {
                        iziToast.error({
                            title: "Form Error",
                            balloon: true,
                            position: "topRight",
                            animateInside: true,
                            message: `Something wrong happened: ${error}`
                        });
                    });
                    // .finally(function () {
                    //     console.log("finally");
                    // });

                this.processing = false;
            } else {
                iziToast.error({
                    title: "Form Sending Incomplete",
                    balloon: true,
                    position: "topRight",
                    animateInside: true,
                    message: `Form data is not valid. Ensure you have filled all fields accurately! ${formElement.reportValidity()}`
                });
                sleep(2500); //wait 2.5 sec and then htmx redirect get
                this.processing = false;
                htmx.ajax('GET', redirect, {target:'main', swap:'outerHTML'});
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
