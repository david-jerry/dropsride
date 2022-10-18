(self["webpackChunkpython_webpack_boilerplate"] = self["webpackChunkpython_webpack_boilerplate"] || []).push([["app"],{

/***/ "./src/application/app.js":
/*!********************************!*\
  !*** ./src/application/app.js ***!
  \********************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

"use strict";
__webpack_require__.r(__webpack_exports__);
/* harmony import */ var _styles_index_scss__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! ../styles/index.scss */ "./src/styles/index.scss");
/* harmony import */ var htmx_org_dist_htmx__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! htmx.org/dist/htmx */ "./node_modules/htmx.org/dist/htmx.js");
/* harmony import */ var htmx_org_dist_htmx__WEBPACK_IMPORTED_MODULE_1___default = /*#__PURE__*/__webpack_require__.n(htmx_org_dist_htmx__WEBPACK_IMPORTED_MODULE_1__);
/* harmony import */ var alpinejs__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! alpinejs */ "./node_modules/alpinejs/dist/module.esm.js");
/* harmony import */ var ethers__WEBPACK_IMPORTED_MODULE_14__ = __webpack_require__(/*! ethers */ "./node_modules/ethers/lib.esm/ethers.js");
/* harmony import */ var _components_axiosFactory__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! ../components/axiosFactory */ "./src/components/axiosFactory.js");
/* harmony import */ var _components_StickyNav__WEBPACK_IMPORTED_MODULE_4__ = __webpack_require__(/*! ../components/StickyNav */ "./src/components/StickyNav.js");
/* harmony import */ var swiper__WEBPACK_IMPORTED_MODULE_5__ = __webpack_require__(/*! swiper */ "./node_modules/swiper/swiper.esm.js");
/* harmony import */ var detect_browser__WEBPACK_IMPORTED_MODULE_15__ = __webpack_require__(/*! detect-browser */ "./node_modules/detect-browser/es/index.js");
/* harmony import */ var izitoast_dist_css_iziToast_min_css__WEBPACK_IMPORTED_MODULE_6__ = __webpack_require__(/*! izitoast/dist/css/iziToast.min.css */ "./node_modules/izitoast/dist/css/iziToast.min.css");
/* harmony import */ var _lottiefiles_lottie_player__WEBPACK_IMPORTED_MODULE_7__ = __webpack_require__(/*! @lottiefiles/lottie-player */ "./node_modules/@lottiefiles/lottie-player/dist/lottie-player.esm.js");
/* harmony import */ var izitoast_dist_js_iziToast_min_js__WEBPACK_IMPORTED_MODULE_8__ = __webpack_require__(/*! izitoast/dist/js/iziToast.min.js */ "./node_modules/izitoast/dist/js/iziToast.min.js");
/* harmony import */ var izitoast_dist_js_iziToast_min_js__WEBPACK_IMPORTED_MODULE_8___default = /*#__PURE__*/__webpack_require__.n(izitoast_dist_js_iziToast_min_js__WEBPACK_IMPORTED_MODULE_8__);
/* harmony import */ var animejs_lib_anime_es_js__WEBPACK_IMPORTED_MODULE_9__ = __webpack_require__(/*! animejs/lib/anime.es.js */ "./node_modules/animejs/lib/anime.es.js");
/* harmony import */ var scrollmagic__WEBPACK_IMPORTED_MODULE_10__ = __webpack_require__(/*! scrollmagic */ "./node_modules/scrollmagic/scrollmagic/uncompressed/ScrollMagic.js");
/* harmony import */ var scrollmagic__WEBPACK_IMPORTED_MODULE_10___default = /*#__PURE__*/__webpack_require__.n(scrollmagic__WEBPACK_IMPORTED_MODULE_10__);
/* harmony import */ var _components_ContactForm__WEBPACK_IMPORTED_MODULE_11__ = __webpack_require__(/*! ../components/ContactForm */ "./src/components/ContactForm.js");
/* harmony import */ var _components_AccountForm__WEBPACK_IMPORTED_MODULE_12__ = __webpack_require__(/*! ../components/AccountForm */ "./src/components/AccountForm.js");
/* harmony import */ var lottie_web__WEBPACK_IMPORTED_MODULE_13__ = __webpack_require__(/*! lottie-web */ "./node_modules/lottie-web/build/player/lottie.js");
/* harmony import */ var lottie_web__WEBPACK_IMPORTED_MODULE_13___default = /*#__PURE__*/__webpack_require__.n(lottie_web__WEBPACK_IMPORTED_MODULE_13__);
// This is global imports for css and javascripts //
//----------------------------------------------------------















 // import { initializeApp } from "firebase/app";
// import { getAnalytics } from "firebase/analytics";
//----------------------------------------------------------
// Global Initializations for importedlibraries //
//----------------------------------------------------------
// initialize htmx

window.htmx = (htmx_org_dist_htmx__WEBPACK_IMPORTED_MODULE_1___default()); // initialize lottie web and lottie player

window.lottieweb = (lottie_web__WEBPACK_IMPORTED_MODULE_13___default()); // initialize animejs

window.anime = animejs_lib_anime_es_js__WEBPACK_IMPORTED_MODULE_9__["default"];
window.scrollMagic = (scrollmagic__WEBPACK_IMPORTED_MODULE_10___default()); // initialize ether js for crypto payment

window.ethers = ethers__WEBPACK_IMPORTED_MODULE_14__; // initialize axios async post|get request

window.axios = _components_axiosFactory__WEBPACK_IMPORTED_MODULE_3__["default"]; // initialize swiper.js

window.Swiper = swiper__WEBPACK_IMPORTED_MODULE_5__["default"]; // initiailize izitoast alerts

window.izitoast = (izitoast_dist_js_iziToast_min_js__WEBPACK_IMPORTED_MODULE_8___default()); // Alpine JS Scripts

window.Alpine = alpinejs__WEBPACK_IMPORTED_MODULE_2__["default"];
alpinejs__WEBPACK_IMPORTED_MODULE_2__["default"].data("StickyNav", _components_StickyNav__WEBPACK_IMPORTED_MODULE_4__["default"]);
alpinejs__WEBPACK_IMPORTED_MODULE_2__["default"].data("ContactForm", _components_ContactForm__WEBPACK_IMPORTED_MODULE_11__["default"]);
alpinejs__WEBPACK_IMPORTED_MODULE_2__["default"].data("AccountForm", _components_AccountForm__WEBPACK_IMPORTED_MODULE_12__["default"]);
alpinejs__WEBPACK_IMPORTED_MODULE_2__["default"].start(); //----------------------------------------------------------
// set service worker link and scope start link
//----------------------------------------------------------

const sw = "/sw.js";
const home = "/"; // detect browser type

const browser = (0,detect_browser__WEBPACK_IMPORTED_MODULE_15__.detect)(); //----------------------------------------------------------
// const firebaseConfig = {
//   apiKey: "AIzaSyCC9j2qwqh1RgE7QS2Q2LoWBEVu_p-Swms",
//   authDomain: "dropsride.firebaseapp.com",
//   projectId: "dropsride",
//   storageBucket: "dropsride.appspot.com",
//   messagingSenderId: "708218104170",
//   appId: "1:708218104170:web:c82bd96c67df6df7a35d13",
//   measurementId: "G-1ZFESGMVN6",
// };
// // Initialize Firebase
// const app = initializeApp(firebaseConfig);
// const analytics = getAnalytics(app);
// get global variables from the base.html file for
// push notification and pwa install button
//----------------------------------------------------------

const {
  APPLICATION_SERVER_KEY,
  CREATE_WP_DEVICE,
  SEND_NOTIFICATION
} = window.WEB_PUSH_CFG; //----------------------------------------------------------
// generate key for push notifications
//----------------------------------------------------------

function urlBase64ToUint8Array(base64String) {
  // https://gist.github.com/Klerith/80abd742d726dd587f4bd5d6a0ab26b6#file-urlbase64touint8array-js
  var padding = "=".repeat((4 - base64String.length % 4) % 4);
  var base64 = (base64String + padding).replace(/\-/g, "+").replace(/_/g, "/");
  var rawData = window.atob(base64);
  var outputArray = new Uint8Array(rawData.length);

  for (var i = 0; i < rawData.length; ++i) {
    outputArray[i] = rawData.charCodeAt(i);
  }

  return outputArray; // const outputData = outputArray.map((output, index) =>
  //   rawData.charCodeAt(index)
  // );
  // return outputData;
} //----------------------------------------------------------
// this is to subscribe to push notification from the browser to the server
//----------------------------------------------------------


function saveSubscribeObj(subscription) {
  // save subscription to the server
  const subscriptionJson = subscription.toJSON();
  const endpointParts = subscriptionJson.endpoint.split("/");
  const registrationId = endpointParts[endpointParts.length - 1];
  const predata = {
    status_type: "subscribe",
    subscription: subscriptionJson,
    browser: browser.name.toLowerCase(),
    p256dh: subscriptionJson.keys.p256dh,
    auth: subscriptionJson.keys.auth,
    user_agent: navigator.getUserAgent,
    registration_id: registrationId,
    group: "users"
  };
  const data = JSON.stringify(predata);
  _components_axiosFactory__WEBPACK_IMPORTED_MODULE_3__["default"].post(CREATE_WP_DEVICE, data, {
    headers: {
      "Content-Type": "application/json"
    }
  }).then(function (response) {
    if (true) {
      console.log(response);
      izitoast_dist_js_iziToast_min_js__WEBPACK_IMPORTED_MODULE_8___default().success({
        title: "[PUSH NOTIFICATION SERVER]",
        balloon: true,
        position: "topRight",
        animateInside: true,
        message: `Notification Subscription ${response.statusText}`
      });
    }
  }).catch(function (error) {
    if (true) {
      console.log(error);
      izitoast_dist_js_iziToast_min_js__WEBPACK_IMPORTED_MODULE_8___default().error({
        title: "[PUSH NOTIFICATION SERVER]",
        balloon: true,
        position: "topRight",
        animateInside: true,
        message: `Notification Subscription ${error.message}`
      });
    }
  });
} //----------------------------------------------------------
// this function is to send subscription notification to the server
//----------------------------------------------------------


function subscribe(registration) {
  registration.pushManager.getSubscription().then(function (subscription) {
    if (subscription) {
      console.log("subscription exists");
      saveSubscribeObj(subscription);
      setupTriggerButton(subscription);
      return;
    }
  });
  const options = {
    userVisibleOnly: true,
    // required by chrome
    applicationServerKey: urlBase64ToUint8Array(APPLICATION_SERVER_KEY)
  };
  registration.pushManager.subscribe(options).then( // requesting to subscribe from the server
  function (subscription) {
    if (true) {
      console.log(`subscription: `, subscription);
      console.log(subscription.endpoint);
    } // subscription is now saved to the server


    saveSubscribeObj(subscription); // if subscription is successfully saved to the server
    // then enable the test notification push button to be visible

    setupTriggerButton(subscription);
    izitoast_dist_js_iziToast_min_js__WEBPACK_IMPORTED_MODULE_8___default().success({
      title: "[PUSH NOTIFICATION SUBSCRIPTION]",
      balloon: true,
      position: "topRight",
      animateInside: true,
      message: `Subscription Sent Successfully`
    });
  }, // if there is an error figure the error and throw an appropraite error message to
  // the user so he knows exactly what is wrong and can move forward or adjust for a
  // device.
  function (error) {
    if (true) {
      console.log(error);
    }

    izitoast_dist_js_iziToast_min_js__WEBPACK_IMPORTED_MODULE_8___default().error({
      title: "[PUSH NOTIFICATION SUBSCRIPTION]",
      balloon: true,
      position: "topRight",
      animateInside: true,
      message: `${error}`
    });
  });
} //----------------------------------------------------------
// The function to trigger the push notification from the browser
//----------------------------------------------------------


function setupTriggerButton(subscription) {
  if (document.getElementById("triggerNotificationButton")) {
    const triggerNotificationButton = document.getElementById("triggerNotificationButton");
    triggerNotificationButton.classList.toggle("hidden", false);
    triggerNotificationButton.addEventListener("click", () => {
      const subJson = subscription.toJSON();
      const endpointParts = subJson.endpoint.split("/");
      const registrationId = endpointParts[endpointParts.length - 1];
      const predata = {
        registration_id: registrationId,
        auth: subJson.keys.auth,
        group: "users",
        head: "Trigger Test Notification",
        body: "This is a test notification"
      };
      const data = JSON.stringify(predata);
      _components_axiosFactory__WEBPACK_IMPORTED_MODULE_3__["default"].post(SEND_NOTIFICATION, data, {
        headers: {
          "Content-Type": "application/json"
        }
      }).then(function (response) {
        izitoast_dist_js_iziToast_min_js__WEBPACK_IMPORTED_MODULE_8___default().success({
          title: "[PUSH NOTIFICATION TEST SUCCESSFUL]",
          balloon: true,
          position: "topRight",
          animateInside: true,
          message: response.data.message
        });
      }).catch(function (error) {
        izitoast_dist_js_iziToast_min_js__WEBPACK_IMPORTED_MODULE_8___default().error({
          title: "[PUSH NOTIFICATION TEST ERROR]",
          balloon: true,
          position: "topRight",
          animateInside: true,
          message: error.response.data.detail
        });
      });
    });
  }

  return;
} //----------------------------------------------------------
// enable service worker, then when service worker is enabled request
// permission for push notification and location services from the browser
//----------------------------------------------------------


if ("serviceWorker" in navigator) {
  window.addEventListener("load", () => {
    navigator.serviceWorker.register(sw, {
      scope: home
    }).then(registration => {
      if (true) {
        console.log("Service worker registeration succeeded: ", registration);
      }

      navigator.serviceWorker.ready.then(function (registration) {
        if (true) {
          console.log("Service worker is active: ", registration.active);
        }

        initialiseState(registration);
      });
    }).catch(err => {
      izitoast_dist_js_iziToast_min_js__WEBPACK_IMPORTED_MODULE_8___default().error({
        title: "[SERVICE WORKER]",
        balloon: true,
        position: "topRight",
        animateInside: true,
        message: "Service Worker Failed to Register"
      });

      if (true) {
        console.log(err);
      }
    });
  });
}

const initialiseState = reg => {
  if (!reg.showNotification) {
    izitoast_dist_js_iziToast_min_js__WEBPACK_IMPORTED_MODULE_8___default().error({
      title: "[PUSH UNSUPPORTED]",
      balloon: true,
      position: "topRight",
      animateInside: true,
      message: "Showing <strong>PUSH NOTIFICATIONS</strong> is unsupported"
    });
    return;
  }

  if (Notification.permission === "denied") {
    izitoast_dist_js_iziToast_min_js__WEBPACK_IMPORTED_MODULE_8___default().warning({
      title: "[PUSH DENIED]",
      balloon: true,
      position: "topRight",
      animateInside: true,
      message: "You prevented us from shwoing notifications. Manually check if you have prevented push notifcation from us."
    });
    return;
  }

  if (!("PushManager" in window)) {
    izitoast_dist_js_iziToast_min_js__WEBPACK_IMPORTED_MODULE_8___default().info({
      title: "[PUSH BROWSER UNAVAILBALE]",
      balloon: true,
      position: "topRight",
      animateInside: true,
      message: "Push notification is not allowed in your browser."
    });
    return;
  }

  reg.pushManager.getSubscription().then(sub => {
    if (!sub) {
      subscribe(reg);
    } else {
      setupTriggerButton(sub);
      izitoast_dist_js_iziToast_min_js__WEBPACK_IMPORTED_MODULE_8___default().info({
        title: "[SERVICE WORKER]",
        balloon: true,
        position: "topRight",
        animateInside: true,
        message: "Push notification has already been subscribed to"
      });
    }
  });
}; //----------------------------------------------------------
// -----------------------------------------------------------------
// INSTALL BUTTON FOR PROGRESSIVE WEB APPLICATION
// ------------------------------------------------------------------


if (document.getElementById("installButton")) {
  const installButton = document.getElementById("installButton"); // when page loads for the first time, install button will be visible
  // if the user has not installed the app or PWA.

  window.addEventListener("beforeinstallprompt", event => {
    if (true) {
      console.log("👍[PWA]", "beforeinstallprompt", event);
    } // Stash the event so it can be triggered later.


    window.deferredPrompt = event; // Remove the 'hidden' class from the install button container
    // if the PWA has been installed, hide the install button or if it has not
    // then allow for click

    installButton.classList.toggle("hidden", false);
  });
  installButton.addEventListener("click", () => {
    if (true) {
      console.log("👍[PWA] Install Button Clicked");
    }

    const promptEvent = window.deferredPrompt;

    if (!promptEvent) {
      // The deferred prompt isn't available. so return nothing
      return;
    }

    promptEvent.prompt();
    promptEvent.userChoice.then(choice => {
      if (true) {
        console.log("👍[PWA] User Choice: ", choice);
      } // iziToast.success({
      //   title: `[PWA: ${choice}]`,
      //   message: '👍 You have successfully installed the readville app',
      // });
      // Reset the deferred prompt variable, since
      // prompt() can only be called once.


      window.deferredPrompt = null; // Hide the install button once the PWA has been installed

      installButton.classList.toggle("hidden", true);
    });
  }); //----------------------------------------------------------
} // if app is installed, thank the user for installing the app
//----------------------------------------------------------


window.addEventListener("appinstalled", event => {
  if (true) {
    console.log("👍[PWA] Installed State: ", event);
  }

  izitoast_dist_js_iziToast_min_js__WEBPACK_IMPORTED_MODULE_8___default().info({
    title: `[SERVICE WORKER]`,
    balloon: true,
    position: "topRight",
    animateInside: true,
    message: "Dropsride Appreciates Your Support."
  });
}); //----------------------------------------------------------
// HTMX Console logs

if (true) {
  // enable logging for htmx in development server only
  window.htmx.logAll();
}

["htmx:onLoad", "htmx:load", "load", "htmx:afterSwap", "htmx:afterOnLoad", "htmx:afterRequest"].forEach(evt => {
  window.addEventListener(evt, function () {
    const counters = document.querySelectorAll(".counter");
    const car = document.getElementById('car');
    const controller = new (scrollmagic__WEBPACK_IMPORTED_MODULE_10___default().Controller)(); // if(document.getElementById('const')){
    //   lottieweb.loadAnimation({
    //     container: document.getElementById('const'),
    //     path: "/static/vendors/images/lottie/under-construction.json",
    //     renderer: 'svg',
    //     loop: true,
    //     autoPlay: true,
    //     name: 'Under Construction'
    //   });
    // }

    function startCounting() {
      if (counters) {
        counters.forEach(counter => {
          (0,animejs_lib_anime_es_js__WEBPACK_IMPORTED_MODULE_9__["default"])({
            targets: counter,
            innerHTML: [0, counter.getAttribute("data-count")],
            easing: "easeInOutSine",
            round: 1,
            duration: 4000
          });
        });
      }
    }

    function animateHows() {
      if (document.querySelectorAll('.how')) {
        (0,animejs_lib_anime_es_js__WEBPACK_IMPORTED_MODULE_9__["default"])({
          targets: ".how",
          translateX: 56,
          easing: "easeInOutSine",
          duration: 800,
          opacity: 1,
          delay: animejs_lib_anime_es_js__WEBPACK_IMPORTED_MODULE_9__["default"].stagger(200, {
            start: 500
          })
        });
      }
    }

    if (document.getElementById('countTrigger')) {
      new (scrollmagic__WEBPACK_IMPORTED_MODULE_10___default().Scene)({
        triggerElement: '#countTrigger',
        triggerHook: 'onEnter',
        duration: '100%',
        reverse: false,
        offset: 50
      }).on('enter', function () {
        startCounting();
      }).addTo(controller);
    }

    if (document.getElementById('track')) {
      new (scrollmagic__WEBPACK_IMPORTED_MODULE_10___default().Scene)({
        triggerElement: '#track',
        triggerHook: 'onEnter',
        duration: '100%',
        reverse: true,
        offset: 50
      }).on('enter', function () {
        carDrive();
      }).addTo(controller);
    }

    if (document.getElementById('hows')) {
      new (scrollmagic__WEBPACK_IMPORTED_MODULE_10___default().Scene)({
        triggerElement: '#hows',
        triggerHook: 'onEnter',
        duration: '100%',
        reverse: false,
        offset: 100
      }).on('enter', function () {
        animateHows();
      }).addTo(controller);
    }

    if (document.querySelectorAll('.intro')) {
      (0,animejs_lib_anime_es_js__WEBPACK_IMPORTED_MODULE_9__["default"])({
        targets: ".intro",
        translateX: -56,
        easing: "easeInOutSine",
        duration: 800,
        opacity: 1,
        delay: animejs_lib_anime_es_js__WEBPACK_IMPORTED_MODULE_9__["default"].stagger(200, {
          start: 500
        })
      });
    }

    function carDrive() {
      if (car) {
        (0,animejs_lib_anime_es_js__WEBPACK_IMPORTED_MODULE_9__["default"])({
          targets: "#car",
          translateX: {
            value: "-100vw",
            duration: 5000
          },
          easing: "easeInOutSine",
          opacity: 1,
          delay: animejs_lib_anime_es_js__WEBPACK_IMPORTED_MODULE_9__["default"].stagger(200, {
            start: 500
          }),
          direction: "normal",
          loop: false
        });
      }
    }
  });
});

/***/ }),

/***/ "./src/components/AccountForm.js":
/*!***************************************!*\
  !*** ./src/components/AccountForm.js ***!
  \***************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

"use strict";
__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "default": () => (/* binding */ AccountForm)
/* harmony export */ });
/* harmony import */ var _axiosFactory__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! ./axiosFactory */ "./src/components/axiosFactory.js");
/* harmony import */ var htmx_org_dist_htmx__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! htmx.org/dist/htmx */ "./node_modules/htmx.org/dist/htmx.js");
/* harmony import */ var htmx_org_dist_htmx__WEBPACK_IMPORTED_MODULE_1___default = /*#__PURE__*/__webpack_require__.n(htmx_org_dist_htmx__WEBPACK_IMPORTED_MODULE_1__);
/* harmony import */ var izitoast_dist_js_iziToast_min_js__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! izitoast/dist/js/iziToast.min.js */ "./node_modules/izitoast/dist/js/iziToast.min.js");
/* harmony import */ var izitoast_dist_js_iziToast_min_js__WEBPACK_IMPORTED_MODULE_2___default = /*#__PURE__*/__webpack_require__.n(izitoast_dist_js_iziToast_min_js__WEBPACK_IMPORTED_MODULE_2__);


 // you have access to iziToast now

function sleep(ms) {
  return new window.Promise(resolve => setTimeout(resolve, ms));
}

function validateField(formElement, fieldElement) {
  let formData = new FormData(formElement);
  formData.append("__field_name__", fieldElement.name);
  _axiosFactory__WEBPACK_IMPORTED_MODULE_0__["default"].post(formElement.action, formData).then(function (response) {
    let errors = response.data.errors;
    let errorsWrapperElement = document.getElementById(`error-wrapper-${fieldElement.name}`);

    if (errors.length === 0) {
      document.getElementById('submit').classList.remove('hidden');
      errorsWrapperElement.classList.add('hidden');

      if (errorsWrapperElement) {
        errorsWrapperElement.innerHTML = "";
      }
    } else {
      document.getElementById('submit').classList.add('hidden');
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
  });
}

function AccountForm() {
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
        data.append(fieldElement.name, fieldElement.value);
      });

      if (formElement.checkValidity()) {
        await _axiosFactory__WEBPACK_IMPORTED_MODULE_0__["default"].post(action, data, {
          headers: {
            'X-CSRFToken': csrf
          }
        }).then(function (response) {
          // console.info("RESPONSE DATA: ", response);
          if (response.status === 200 || response.status === 201) {
            div.innerHTML = `
                            ${formElement}
                            `;
            izitoast_dist_js_iziToast_min_js__WEBPACK_IMPORTED_MODULE_2___default().success({
              title: response.data.title,
              balloon: true,
              position: "topRight",
              animateInside: true,
              message: response.data.message
            });
            sleep(3500); //wait 1 sec and then htmx redirect get

            htmx_org_dist_htmx__WEBPACK_IMPORTED_MODULE_1___default().ajax('GET', redirect, {
              target: 'main',
              swap: 'outerHTML'
            }); // sleep(3500); //wait 1 sec and then htmx redirect get
            // location.reload();
          } else {
            izitoast_dist_js_iziToast_min_js__WEBPACK_IMPORTED_MODULE_2___default().error({
              title: response.data.title,
              balloon: true,
              position: "topRight",
              animateInside: true,
              message: response.data.message
            });
          }

          console.log(response);
        }).catch(function (error) {
          izitoast_dist_js_iziToast_min_js__WEBPACK_IMPORTED_MODULE_2___default().error({
            title: "Form Error",
            balloon: true,
            position: "topRight",
            animateInside: true,
            message: `Something wrong happened: ${error}`
          });
        }); // .finally(function () {
        //     console.log("finally");
        // });

        this.processing = false;
      } else {
        izitoast_dist_js_iziToast_min_js__WEBPACK_IMPORTED_MODULE_2___default().error({
          title: "Form Sending Incomplete",
          balloon: true,
          position: "topRight",
          animateInside: true,
          message: `Form data is not valid. Ensure you have filled all fields accurately! ${formElement.reportValidity()}`
        });
        sleep(2500); //wait 2.5 sec and then htmx redirect get

        this.processing = false;
        htmx_org_dist_htmx__WEBPACK_IMPORTED_MODULE_1___default().ajax('GET', redirect, {
          target: 'main',
          swap: 'outerHTML'
        });
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
        data.append(fieldElement.name, fieldElement.value);
      });

      if (formElement.checkValidity()) {
        await _axiosFactory__WEBPACK_IMPORTED_MODULE_0__["default"].post(action, data, {
          headers: {
            'X-CSRFToken': csrf,
            'Content-Type': 'multipart/form-data'
          }
        }).then(function (response) {
          // console.info("RESPONSE DATA: ", response);
          if (response.status === 200 || response.status === 201) {
            div.innerHTML = `
                            ${formElement}
                            `;
            izitoast_dist_js_iziToast_min_js__WEBPACK_IMPORTED_MODULE_2___default().success({
              title: response.data.title,
              balloon: true,
              position: "topRight",
              animateInside: true,
              message: response.data.message
            });
            sleep(3500); //wait 1 sec and then htmx redirect get

            htmx_org_dist_htmx__WEBPACK_IMPORTED_MODULE_1___default().ajax('GET', redirect, {
              target: 'main',
              swap: 'outerHTML'
            }); // sleep(3500); //wait 1 sec and then htmx redirect get
            // location.reload();
          } else {
            izitoast_dist_js_iziToast_min_js__WEBPACK_IMPORTED_MODULE_2___default().error({
              title: response.data.title,
              balloon: true,
              position: "topRight",
              animateInside: true,
              message: response.data.message
            });
          }

          console.log(response);
        }).catch(function (error) {
          izitoast_dist_js_iziToast_min_js__WEBPACK_IMPORTED_MODULE_2___default().error({
            title: "Form Error",
            balloon: true,
            position: "topRight",
            animateInside: true,
            message: `Something wrong happened: ${error}`
          });
        }); // .finally(function () {
        //     console.log("finally");
        // });

        this.processing = false;
      } else {
        izitoast_dist_js_iziToast_min_js__WEBPACK_IMPORTED_MODULE_2___default().error({
          title: "Form Sending Incomplete",
          balloon: true,
          position: "topRight",
          animateInside: true,
          message: `Form data is not valid. Ensure you have filled all fields accurately! ${formElement.reportValidity()}`
        });
        sleep(2500); //wait 2.5 sec and then htmx redirect get

        this.processing = false;
        htmx_org_dist_htmx__WEBPACK_IMPORTED_MODULE_1___default().ajax('GET', redirect, {
          target: 'main',
          swap: 'outerHTML'
        });
      }
    },

    async checkValidity() {
      const formElement = this.$refs.contactForm;
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

/***/ }),

/***/ "./src/components/ContactForm.js":
/*!***************************************!*\
  !*** ./src/components/ContactForm.js ***!
  \***************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

"use strict";
__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "default": () => (/* binding */ ContactForm)
/* harmony export */ });
/* harmony import */ var _axiosFactory__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! ./axiosFactory */ "./src/components/axiosFactory.js");
/* harmony import */ var htmx_org_dist_htmx__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! htmx.org/dist/htmx */ "./node_modules/htmx.org/dist/htmx.js");
/* harmony import */ var htmx_org_dist_htmx__WEBPACK_IMPORTED_MODULE_1___default = /*#__PURE__*/__webpack_require__.n(htmx_org_dist_htmx__WEBPACK_IMPORTED_MODULE_1__);
/* harmony import */ var izitoast_dist_js_iziToast_min_js__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! izitoast/dist/js/iziToast.min.js */ "./node_modules/izitoast/dist/js/iziToast.min.js");
/* harmony import */ var izitoast_dist_js_iziToast_min_js__WEBPACK_IMPORTED_MODULE_2___default = /*#__PURE__*/__webpack_require__.n(izitoast_dist_js_iziToast_min_js__WEBPACK_IMPORTED_MODULE_2__);


 // you have access to iziToast now
// function serialize(data) {
//     let obj = {};
//     for (let [key, value] of data) {
//       if (obj[key] !== undefined) {
//         if (!Array.isArray(obj[key])) {
//           obj[key] = [obj[key]];
//         }
//         obj[key].push(value);
//       } else {
//         obj[key] = value;
//       }
//     }
//     return obj;
// }

function sleep(ms) {
  return new window.Promise(resolve => setTimeout(resolve, ms));
}

function validateField(formElement, fieldElement) {
  let formData = new FormData(formElement);
  formData.append("__field_name__", fieldElement.name);
  _axiosFactory__WEBPACK_IMPORTED_MODULE_0__["default"].post(formElement.action, formData).then(function (response) {
    let errors = response.data.errors;
    let errorsWrapperElement = document.getElementById(`error-wrapper-${fieldElement.name}`);

    if (errors.length === 0) {
      document.getElementById('submit').classList.remove('hidden');
      errorsWrapperElement.classList.add('hidden');

      if (errorsWrapperElement) {
        errorsWrapperElement.innerHTML = "";
      }
    } else {
      document.getElementById('submit').classList.add('hidden');
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
  });
}

function ContactForm() {
  return {
    processing: false,

    async submitForm() {
      this.processing = true;
      const formElement = this.$refs.contactForm;
      const div = document.getElementById('contact');
      const redirect = formElement.action;
      const csrf = formElement.dataset.csrf;
      let data = new FormData(formElement);
      formElement.querySelectorAll("[name]").forEach(fieldElement => {
        data.append(fieldElement.name, fieldElement.value);
      });
      console.log(data); // data.append('csrfmiddlewaretoken', csrf);
      // data.append('name', document.getElementById('id_name').value);
      // data.append('email', document.getElementById('id_email').value);
      // data.append('message', document.getElementById('id_message').value);
      // console.info("FORM DATA: ", data);
      // let formData = serialize(data);
      // console.info("SERIALIZED FORM DATA: ", formData);

      if (formElement.checkValidity()) {
        await _axiosFactory__WEBPACK_IMPORTED_MODULE_0__["default"].post(redirect, data, {
          headers: {
            'X-CSRFToken': csrf
          }
        }).then(function (response) {
          // console.info("RESPONSE DATA: ", response);
          if (response.status === 200 || response.data.message === "Support Mail Successfully Sent") {
            div.innerHTML = `
                            <div class="w-full text-green-300 space-y-8 flex flex-col justify-center py-24">
                                <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="block w-14 h-14 block mx-auto animate-bounce text-green-300">
                                    <path stroke-linecap="round" stroke-linejoin="round" d="M21.75 6.75v10.5a2.25 2.25 0 01-2.25 2.25h-15a2.25 2.25 0 01-2.25-2.25V6.75m19.5 0A2.25 2.25 0 0019.5 4.5h-15a2.25 2.25 0 00-2.25 2.25m19.5 0v.243a2.25 2.25 0 01-1.07 1.916l-7.5 4.615a2.25 2.25 0 01-2.36 0L3.32 8.91a2.25 2.25 0 01-1.07-1.916V6.75" />
                                </svg>
                                <div class="w-full md:w-3/5 text-center space-y-3 mx-auto">
                                    <h4 class="text-green-500 font-semibold text-2xl md:text-4xl">Mail Sent Successfully</h4>
                                    <p>${response.data.message}</p>
                                </div>
                            </div>
                            `;
            izitoast_dist_js_iziToast_min_js__WEBPACK_IMPORTED_MODULE_2___default().success({
              title: "Email Sent Successful",
              balloon: true,
              position: "topRight",
              animateInside: true,
              message: response.data.message
            });
            sleep(3500); //wait 1 sec and then htmx redirect get

            htmx_org_dist_htmx__WEBPACK_IMPORTED_MODULE_1___default().ajax('GET', redirect, {
              target: 'main',
              swap: 'outerHTML'
            }); // sleep(3500); //wait 1 sec and then htmx redirect get
            // location.reload();
          }

          console.log(response);
        }).catch(function (error) {
          izitoast_dist_js_iziToast_min_js__WEBPACK_IMPORTED_MODULE_2___default().error({
            title: "Email Sending Incomplete",
            balloon: true,
            position: "topRight",
            animateInside: true,
            message: `Something wrong happened: ${error}`
          });
        }); // .finally(function () {
        //     console.log("finally");
        // });

        this.processing = false;
      } else {
        izitoast_dist_js_iziToast_min_js__WEBPACK_IMPORTED_MODULE_2___default().error({
          title: "Sending Email Incomplete",
          balloon: true,
          position: "topRight",
          animateInside: true,
          message: `Form data is not valid. Ensure you have filled all fields accurately! ${formElement.reportValidity()}`
        });
        sleep(2500); //wait 2.5 sec and then htmx redirect get

        this.processing = false;
        htmx_org_dist_htmx__WEBPACK_IMPORTED_MODULE_1___default().ajax('GET', redirect, {
          target: 'main',
          swap: 'outerHTML'
        });
      }
    },

    async checkValidity() {
      const formElement = this.$refs.contactForm;
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

/***/ }),

/***/ "./src/components/StickyNav.js":
/*!*************************************!*\
  !*** ./src/components/StickyNav.js ***!
  \*************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

"use strict";
__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "default": () => (/* binding */ StickyNav)
/* harmony export */ });
function StickyNav() {
  return {
    showNav: true,
    navTop: false,
    lastScroll: 0,

    initState() {
      const main = document.getElementById('main');
      const navbar = document.getElementById('navbar'); // get the height of the navbar and then add it to the top padding of the main content

      const header_h = navbar.offsetHeight + 10;
      main.classList.add(`pt-[${header_h}px]`);
      this.navTop = true;
      this.showNav = false;
    },

    scrollNav() {
      let currentScroll = window.pageYOffset;

      if (currentScroll <= 0) {
        this.showNav = true;
        this.navTop = true;
      }

      if (currentScroll > this.lastScroll && this.showNav === false) {
        this.showNav = true;
        this.navTop = false;
      } else if (currentScroll < this.lastScroll && this.showNav === true) {
        this.showNav = false;
        this.navTop = true;
      }

      this.lastScroll = currentScroll;
    }

  };
}

/***/ }),

/***/ "./src/components/axiosFactory.js":
/*!****************************************!*\
  !*** ./src/components/axiosFactory.js ***!
  \****************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

"use strict";
__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "default": () => (__WEBPACK_DEFAULT_EXPORT__)
/* harmony export */ });
/* harmony import */ var axios__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! axios */ "./node_modules/axios/index.js");
/* harmony import */ var axios__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(axios__WEBPACK_IMPORTED_MODULE_0__);

(axios__WEBPACK_IMPORTED_MODULE_0___default().defaults.withCredentials) = true;
(axios__WEBPACK_IMPORTED_MODULE_0___default().defaults.xsrfCookieName) = 'csrftoken';
(axios__WEBPACK_IMPORTED_MODULE_0___default().defaults.xsrfHeaderName) = "X-CSRFTOKEN"; // axios.defaults.headers['X-CSRFToken'] = document.head.querySelector('meta[name="csrf-token"]').getAttribute('content');

(axios__WEBPACK_IMPORTED_MODULE_0___default().defaults.timeout) = 15000;
/* harmony default export */ const __WEBPACK_DEFAULT_EXPORT__ = ((axios__WEBPACK_IMPORTED_MODULE_0___default()));

/***/ }),

/***/ "./src/styles/index.scss":
/*!*******************************!*\
  !*** ./src/styles/index.scss ***!
  \*******************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

"use strict";
__webpack_require__.r(__webpack_exports__);
// extracted by mini-css-extract-plugin


/***/ }),

/***/ "?8131":
/*!************************!*\
  !*** buffer (ignored) ***!
  \************************/
/***/ (() => {

/* (ignored) */

/***/ })

},
/******/ __webpack_require__ => { // webpackRuntimeModules
/******/ var __webpack_exec__ = (moduleId) => (__webpack_require__(__webpack_require__.s = moduleId))
/******/ __webpack_require__.O(0, ["vendors-node_modules_lottiefiles_lottie-player_dist_lottie-player_esm_js-node_modules_alpinej-ab0a7b"], () => (__webpack_exec__("./src/application/app.js")));
/******/ var __webpack_exports__ = __webpack_require__.O();
/******/ }
]);
//# sourceMappingURL=data:application/json;charset=utf-8;base64,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QWxCO0lBQ0g7O0VBaENFLENBQVA7QUFrQ0g7Ozs7Ozs7Ozs7Ozs7Ozs7O0FDbkNEO0FBRUE3TCx1RUFBQSxHQUFpQyxJQUFqQztBQUNBQSxzRUFBQSxHQUFnQyxXQUFoQztBQUNBQSxzRUFBQSxHQUFnQyxhQUFoQyxFQUNBOztBQUNBQSwrREFBQSxHQUF5QixLQUF6QjtBQUVBLGlFQUFlQSw4Q0FBZjs7Ozs7Ozs7Ozs7O0FDUkE7Ozs7Ozs7Ozs7O0FDQUEiLCJzb3VyY2VzIjpbIndlYnBhY2s6Ly9weXRob24td2VicGFjay1ib2lsZXJwbGF0ZS8uL3NyYy9hcHBsaWNhdGlvbi9hcHAuanMiLCJ3ZWJwYWNrOi8vcHl0aG9uLXdlYnBhY2stYm9pbGVycGxhdGUvLi9zcmMvY29tcG9uZW50cy9BY2NvdW50Rm9ybS5qcyIsIndlYnBhY2s6Ly9weXRob24td2VicGFjay1ib2lsZXJwbGF0ZS8uL3NyYy9jb21wb25lbnRzL0NvbnRhY3RGb3JtLmpzIiwid2VicGFjazovL3B5dGhvbi13ZWJwYWNrLWJvaWxlcnBsYXRlLy4vc3JjL2NvbXBvbmVudHMvU3RpY2t5TmF2LmpzIiwid2VicGFjazovL3B5dGhvbi13ZWJwYWNrLWJvaWxlcnBsYXRlLy4vc3JjL2NvbXBvbmVudHMvYXhpb3NGYWN0b3J5LmpzIiwid2VicGFjazovL3B5dGhvbi13ZWJwYWNrLWJvaWxlcnBsYXRlLy4vc3JjL3N0eWxlcy9pbmRleC5zY3NzPzBiODgiLCJ3ZWJwYWNrOi8vcHl0aG9uLXdlYnBhY2stYm9pbGVycGxhdGUvaWdub3JlZHwvaG9tZS9kYXJrY29kci93d3cvZGFya2NvZHIvZHJvcHNyaWRlL2Zyb250ZW5kL25vZGVfbW9kdWxlcy9ibi5qcy9saWJ8YnVmZmVyIl0sInNvdXJjZXNDb250ZW50IjpbIi8vIFRoaXMgaXMgZ2xvYmFsIGltcG9ydHMgZm9yIGNzcyBhbmQgamF2YXNjcmlwdHMgLy9cbi8vLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLVxuaW1wb3J0IFwiLi4vc3R5bGVzL2luZGV4LnNjc3NcIjtcbmltcG9ydCBodG14IGZyb20gXCJodG14Lm9yZy9kaXN0L2h0bXhcIjtcbmltcG9ydCBBbHBpbmUgZnJvbSBcImFscGluZWpzXCI7XG5pbXBvcnQgeyBldGhlcnMgfSBmcm9tIFwiZXRoZXJzXCI7XG5pbXBvcnQgYXhpb3MgZnJvbSBcIi4uL2NvbXBvbmVudHMvYXhpb3NGYWN0b3J5XCI7XG5pbXBvcnQgU3RpY2t5TmF2IGZyb20gXCIuLi9jb21wb25lbnRzL1N0aWNreU5hdlwiO1xuaW1wb3J0IFN3aXBlciBmcm9tIFwic3dpcGVyXCI7XG5pbXBvcnQgeyBkZXRlY3QgfSBmcm9tIFwiZGV0ZWN0LWJyb3dzZXJcIjtcbmltcG9ydCBcIml6aXRvYXN0L2Rpc3QvY3NzL2l6aVRvYXN0Lm1pbi5jc3NcIjtcbmltcG9ydCBcIkBsb3R0aWVmaWxlcy9sb3R0aWUtcGxheWVyXCI7XG5pbXBvcnQgaXppVG9hc3QgZnJvbSBcIml6aXRvYXN0L2Rpc3QvanMvaXppVG9hc3QubWluLmpzXCI7XG5pbXBvcnQgYW5pbWUgZnJvbSBcImFuaW1lanMvbGliL2FuaW1lLmVzLmpzXCI7XG5pbXBvcnQgU2Nyb2xsTWFnaWMgZnJvbSBcInNjcm9sbG1hZ2ljXCI7XG5pbXBvcnQgQ29udGFjdEZvcm0gZnJvbSBcIi4uL2NvbXBvbmVudHMvQ29udGFjdEZvcm1cIjtcbmltcG9ydCBBY2NvdW50Rm9ybSBmcm9tIFwiLi4vY29tcG9uZW50cy9BY2NvdW50Rm9ybVwiO1xuaW1wb3J0IGxvdHRpZXdlYiBmcm9tIFwibG90dGllLXdlYlwiO1xuXG4vLyBpbXBvcnQgeyBpbml0aWFsaXplQXBwIH0gZnJvbSBcImZpcmViYXNlL2FwcFwiO1xuLy8gaW1wb3J0IHsgZ2V0QW5hbHl0aWNzIH0gZnJvbSBcImZpcmViYXNlL2FuYWx5dGljc1wiO1xuLy8tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tXG5cbi8vIEdsb2JhbCBJbml0aWFsaXphdGlvbnMgZm9yIGltcG9ydGVkbGlicmFyaWVzIC8vXG4vLy0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS1cbi8vIGluaXRpYWxpemUgaHRteFxud2luZG93Lmh0bXggPSBodG14O1xuLy8gaW5pdGlhbGl6ZSBsb3R0aWUgd2ViIGFuZCBsb3R0aWUgcGxheWVyXG53aW5kb3cubG90dGlld2ViID0gbG90dGlld2ViO1xuLy8gaW5pdGlhbGl6ZSBhbmltZWpzXG53aW5kb3cuYW5pbWUgPSBhbmltZTtcbndpbmRvdy5zY3JvbGxNYWdpYyA9IFNjcm9sbE1hZ2ljO1xuLy8gaW5pdGlhbGl6ZSBldGhlciBqcyBmb3IgY3J5cHRvIHBheW1lbnRcbndpbmRvdy5ldGhlcnMgPSBldGhlcnM7XG4vLyBpbml0aWFsaXplIGF4aW9zIGFzeW5jIHBvc3R8Z2V0IHJlcXVlc3RcbndpbmRvdy5heGlvcyA9IGF4aW9zO1xuLy8gaW5pdGlhbGl6ZSBzd2lwZXIuanNcbndpbmRvdy5Td2lwZXIgPSBTd2lwZXI7XG4vLyBpbml0aWFpbGl6ZSBpeml0b2FzdCBhbGVydHNcbndpbmRvdy5peml0b2FzdCA9IGl6aVRvYXN0O1xuLy8gQWxwaW5lIEpTIFNjcmlwdHNcbndpbmRvdy5BbHBpbmUgPSBBbHBpbmU7XG5BbHBpbmUuZGF0YShcIlN0aWNreU5hdlwiLCBTdGlja3lOYXYpO1xuQWxwaW5lLmRhdGEoXCJDb250YWN0Rm9ybVwiLCBDb250YWN0Rm9ybSk7XG5BbHBpbmUuZGF0YShcIkFjY291bnRGb3JtXCIsIEFjY291bnRGb3JtKTtcbkFscGluZS5zdGFydCgpO1xuLy8tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tXG5cbi8vIHNldCBzZXJ2aWNlIHdvcmtlciBsaW5rIGFuZCBzY29wZSBzdGFydCBsaW5rXG4vLy0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS1cbmNvbnN0IHN3ID0gXCIvc3cuanNcIjtcbmNvbnN0IGhvbWUgPSBcIi9cIjtcbi8vIGRldGVjdCBicm93c2VyIHR5cGVcbmNvbnN0IGJyb3dzZXIgPSBkZXRlY3QoKTtcbi8vLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLVxuXG4vLyBjb25zdCBmaXJlYmFzZUNvbmZpZyA9IHtcbi8vICAgYXBpS2V5OiBcIkFJemFTeUNDOWoycXdxaDFSZ0U3UVMyUTJMb1dCRVZ1X3AtU3dtc1wiLFxuLy8gICBhdXRoRG9tYWluOiBcImRyb3BzcmlkZS5maXJlYmFzZWFwcC5jb21cIixcbi8vICAgcHJvamVjdElkOiBcImRyb3BzcmlkZVwiLFxuLy8gICBzdG9yYWdlQnVja2V0OiBcImRyb3BzcmlkZS5hcHBzcG90LmNvbVwiLFxuLy8gICBtZXNzYWdpbmdTZW5kZXJJZDogXCI3MDgyMTgxMDQxNzBcIixcbi8vICAgYXBwSWQ6IFwiMTo3MDgyMTgxMDQxNzA6d2ViOmM4MmJkOTZjNjdkZjZkZjdhMzVkMTNcIixcbi8vICAgbWVhc3VyZW1lbnRJZDogXCJHLTFaRkVTR01WTjZcIixcbi8vIH07XG4vLyAvLyBJbml0aWFsaXplIEZpcmViYXNlXG5cbi8vIGNvbnN0IGFwcCA9IGluaXRpYWxpemVBcHAoZmlyZWJhc2VDb25maWcpO1xuLy8gY29uc3QgYW5hbHl0aWNzID0gZ2V0QW5hbHl0aWNzKGFwcCk7XG4gIC8vIGdldCBnbG9iYWwgdmFyaWFibGVzIGZyb20gdGhlIGJhc2UuaHRtbCBmaWxlIGZvclxuICAvLyBwdXNoIG5vdGlmaWNhdGlvbiBhbmQgcHdhIGluc3RhbGwgYnV0dG9uXG4gIC8vLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLVxuICBjb25zdCB7IEFQUExJQ0FUSU9OX1NFUlZFUl9LRVksIENSRUFURV9XUF9ERVZJQ0UsIFNFTkRfTk9USUZJQ0FUSU9OIH0gPVxuICAgIHdpbmRvdy5XRUJfUFVTSF9DRkc7XG4gIC8vLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLVxuXG4gIC8vIGdlbmVyYXRlIGtleSBmb3IgcHVzaCBub3RpZmljYXRpb25zXG4gIC8vLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLVxuICBmdW5jdGlvbiB1cmxCYXNlNjRUb1VpbnQ4QXJyYXkoYmFzZTY0U3RyaW5nKSB7XG4gICAgLy8gaHR0cHM6Ly9naXN0LmdpdGh1Yi5jb20vS2xlcml0aC84MGFiZDc0MmQ3MjZkZDU4N2Y0YmQ1ZDZhMGFiMjZiNiNmaWxlLXVybGJhc2U2NHRvdWludDhhcnJheS1qc1xuICAgIHZhciBwYWRkaW5nID0gXCI9XCIucmVwZWF0KCg0IC0gKGJhc2U2NFN0cmluZy5sZW5ndGggJSA0KSkgJSA0KTtcbiAgICB2YXIgYmFzZTY0ID0gKGJhc2U2NFN0cmluZyArIHBhZGRpbmcpLnJlcGxhY2UoL1xcLS9nLCBcIitcIikucmVwbGFjZSgvXy9nLCBcIi9cIik7XG5cbiAgICB2YXIgcmF3RGF0YSA9IHdpbmRvdy5hdG9iKGJhc2U2NCk7XG4gICAgdmFyIG91dHB1dEFycmF5ID0gbmV3IFVpbnQ4QXJyYXkocmF3RGF0YS5sZW5ndGgpO1xuXG4gICAgZm9yICh2YXIgaSA9IDA7IGkgPCByYXdEYXRhLmxlbmd0aDsgKytpKSB7XG4gICAgICBvdXRwdXRBcnJheVtpXSA9IHJhd0RhdGEuY2hhckNvZGVBdChpKTtcbiAgICB9XG4gICAgcmV0dXJuIG91dHB1dEFycmF5O1xuXG4gICAgLy8gY29uc3Qgb3V0cHV0RGF0YSA9IG91dHB1dEFycmF5Lm1hcCgob3V0cHV0LCBpbmRleCkgPT5cbiAgICAvLyAgIHJhd0RhdGEuY2hhckNvZGVBdChpbmRleClcbiAgICAvLyApO1xuICAgIC8vIHJldHVybiBvdXRwdXREYXRhO1xuICB9XG4gIC8vLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLVxuXG4gIC8vIHRoaXMgaXMgdG8gc3Vic2NyaWJlIHRvIHB1c2ggbm90aWZpY2F0aW9uIGZyb20gdGhlIGJyb3dzZXIgdG8gdGhlIHNlcnZlclxuICAvLy0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS1cbiAgZnVuY3Rpb24gc2F2ZVN1YnNjcmliZU9iaihzdWJzY3JpcHRpb24pIHtcbiAgICAvLyBzYXZlIHN1YnNjcmlwdGlvbiB0byB0aGUgc2VydmVyXG4gICAgY29uc3Qgc3Vic2NyaXB0aW9uSnNvbiA9IHN1YnNjcmlwdGlvbi50b0pTT04oKTtcbiAgICBjb25zdCBlbmRwb2ludFBhcnRzID0gc3Vic2NyaXB0aW9uSnNvbi5lbmRwb2ludC5zcGxpdChcIi9cIik7XG4gICAgY29uc3QgcmVnaXN0cmF0aW9uSWQgPSBlbmRwb2ludFBhcnRzW2VuZHBvaW50UGFydHMubGVuZ3RoIC0gMV07XG5cbiAgICBjb25zdCBwcmVkYXRhID0ge1xuICAgICAgc3RhdHVzX3R5cGU6IFwic3Vic2NyaWJlXCIsXG4gICAgICBzdWJzY3JpcHRpb246IHN1YnNjcmlwdGlvbkpzb24sXG4gICAgICBicm93c2VyOiBicm93c2VyLm5hbWUudG9Mb3dlckNhc2UoKSxcbiAgICAgIHAyNTZkaDogc3Vic2NyaXB0aW9uSnNvbi5rZXlzLnAyNTZkaCxcbiAgICAgIGF1dGg6IHN1YnNjcmlwdGlvbkpzb24ua2V5cy5hdXRoLFxuICAgICAgdXNlcl9hZ2VudDogbmF2aWdhdG9yLmdldFVzZXJBZ2VudCxcbiAgICAgIHJlZ2lzdHJhdGlvbl9pZDogcmVnaXN0cmF0aW9uSWQsXG4gICAgICBncm91cDogXCJ1c2Vyc1wiLFxuICAgIH07XG5cbiAgICBjb25zdCBkYXRhID0gSlNPTi5zdHJpbmdpZnkocHJlZGF0YSk7XG5cbiAgICBheGlvc1xuICAgICAgLnBvc3QoQ1JFQVRFX1dQX0RFVklDRSwgZGF0YSwge1xuICAgICAgICBoZWFkZXJzOiB7XG4gICAgICAgICAgXCJDb250ZW50LVR5cGVcIjogXCJhcHBsaWNhdGlvbi9qc29uXCIsXG4gICAgICAgIH0sXG4gICAgICB9KVxuICAgICAgLnRoZW4oZnVuY3Rpb24gKHJlc3BvbnNlKSB7XG4gICAgICAgIGlmIChwcm9jZXNzLmVudi5OT0RFX0VOViA9PT0gXCJkZXZlbG9wbWVudFwiKSB7XG4gICAgICAgICAgY29uc29sZS5sb2cocmVzcG9uc2UpO1xuICAgICAgICAgIGl6aVRvYXN0LnN1Y2Nlc3Moe1xuICAgICAgICAgICAgdGl0bGU6IFwiW1BVU0ggTk9USUZJQ0FUSU9OIFNFUlZFUl1cIixcbiAgICAgICAgICAgIGJhbGxvb246IHRydWUsXG4gICAgICAgICAgICBwb3NpdGlvbjogXCJ0b3BSaWdodFwiLFxuICAgICAgICAgICAgYW5pbWF0ZUluc2lkZTogdHJ1ZSxcbiAgICAgICAgICAgIG1lc3NhZ2U6IGBOb3RpZmljYXRpb24gU3Vic2NyaXB0aW9uICR7cmVzcG9uc2Uuc3RhdHVzVGV4dH1gLFxuICAgICAgICAgIH0pO1xuICAgICAgICB9XG4gICAgICB9KVxuICAgICAgLmNhdGNoKGZ1bmN0aW9uIChlcnJvcikge1xuICAgICAgICBpZiAocHJvY2Vzcy5lbnYuTk9ERV9FTlYgPT09IFwiZGV2ZWxvcG1lbnRcIikge1xuICAgICAgICAgIGNvbnNvbGUubG9nKGVycm9yKTtcbiAgICAgICAgICBpemlUb2FzdC5lcnJvcih7XG4gICAgICAgICAgICB0aXRsZTogXCJbUFVTSCBOT1RJRklDQVRJT04gU0VSVkVSXVwiLFxuICAgICAgICAgICAgYmFsbG9vbjogdHJ1ZSxcbiAgICAgICAgICAgIHBvc2l0aW9uOiBcInRvcFJpZ2h0XCIsXG4gICAgICAgICAgICBhbmltYXRlSW5zaWRlOiB0cnVlLFxuICAgICAgICAgICAgbWVzc2FnZTogYE5vdGlmaWNhdGlvbiBTdWJzY3JpcHRpb24gJHtlcnJvci5tZXNzYWdlfWAsXG4gICAgICAgICAgfSk7XG4gICAgICAgIH1cbiAgICAgIH0pO1xuICB9XG4gIC8vLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLVxuXG4gIC8vIHRoaXMgZnVuY3Rpb24gaXMgdG8gc2VuZCBzdWJzY3JpcHRpb24gbm90aWZpY2F0aW9uIHRvIHRoZSBzZXJ2ZXJcbiAgLy8tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tXG4gIGZ1bmN0aW9uIHN1YnNjcmliZShyZWdpc3RyYXRpb24pIHtcbiAgICByZWdpc3RyYXRpb24ucHVzaE1hbmFnZXIuZ2V0U3Vic2NyaXB0aW9uKCkudGhlbihmdW5jdGlvbiAoc3Vic2NyaXB0aW9uKSB7XG4gICAgICBpZiAoc3Vic2NyaXB0aW9uKSB7XG4gICAgICAgIGNvbnNvbGUubG9nKFwic3Vic2NyaXB0aW9uIGV4aXN0c1wiKTtcbiAgICAgICAgc2F2ZVN1YnNjcmliZU9iaihzdWJzY3JpcHRpb24pO1xuICAgICAgICBzZXR1cFRyaWdnZXJCdXR0b24oc3Vic2NyaXB0aW9uKTtcbiAgICAgICAgcmV0dXJuO1xuICAgICAgfVxuICAgIH0pO1xuXG4gICAgY29uc3Qgb3B0aW9ucyA9IHtcbiAgICAgIHVzZXJWaXNpYmxlT25seTogdHJ1ZSwgLy8gcmVxdWlyZWQgYnkgY2hyb21lXG4gICAgICBhcHBsaWNhdGlvblNlcnZlcktleTogdXJsQmFzZTY0VG9VaW50OEFycmF5KEFQUExJQ0FUSU9OX1NFUlZFUl9LRVkpLFxuICAgIH07XG5cbiAgICByZWdpc3RyYXRpb24ucHVzaE1hbmFnZXIuc3Vic2NyaWJlKG9wdGlvbnMpLnRoZW4oXG4gICAgICAvLyByZXF1ZXN0aW5nIHRvIHN1YnNjcmliZSBmcm9tIHRoZSBzZXJ2ZXJcbiAgICAgIGZ1bmN0aW9uIChzdWJzY3JpcHRpb24pIHtcbiAgICAgICAgaWYgKHByb2Nlc3MuZW52Lk5PREVfRU5WID09PSBcImRldmVsb3BtZW50XCIpIHtcbiAgICAgICAgICBjb25zb2xlLmxvZyhgc3Vic2NyaXB0aW9uOiBgLCBzdWJzY3JpcHRpb24pO1xuICAgICAgICAgIGNvbnNvbGUubG9nKHN1YnNjcmlwdGlvbi5lbmRwb2ludCk7XG4gICAgICAgIH1cblxuICAgICAgICAvLyBzdWJzY3JpcHRpb24gaXMgbm93IHNhdmVkIHRvIHRoZSBzZXJ2ZXJcbiAgICAgICAgc2F2ZVN1YnNjcmliZU9iaihzdWJzY3JpcHRpb24pO1xuXG4gICAgICAgIC8vIGlmIHN1YnNjcmlwdGlvbiBpcyBzdWNjZXNzZnVsbHkgc2F2ZWQgdG8gdGhlIHNlcnZlclxuICAgICAgICAvLyB0aGVuIGVuYWJsZSB0aGUgdGVzdCBub3RpZmljYXRpb24gcHVzaCBidXR0b24gdG8gYmUgdmlzaWJsZVxuICAgICAgICBzZXR1cFRyaWdnZXJCdXR0b24oc3Vic2NyaXB0aW9uKTtcblxuICAgICAgICBpemlUb2FzdC5zdWNjZXNzKHtcbiAgICAgICAgICB0aXRsZTogXCJbUFVTSCBOT1RJRklDQVRJT04gU1VCU0NSSVBUSU9OXVwiLFxuICAgICAgICAgIGJhbGxvb246IHRydWUsXG4gICAgICAgICAgcG9zaXRpb246IFwidG9wUmlnaHRcIixcbiAgICAgICAgICBhbmltYXRlSW5zaWRlOiB0cnVlLFxuICAgICAgICAgIG1lc3NhZ2U6IGBTdWJzY3JpcHRpb24gU2VudCBTdWNjZXNzZnVsbHlgLFxuICAgICAgICB9KTtcbiAgICAgIH0sXG5cbiAgICAgIC8vIGlmIHRoZXJlIGlzIGFuIGVycm9yIGZpZ3VyZSB0aGUgZXJyb3IgYW5kIHRocm93IGFuIGFwcHJvcHJhaXRlIGVycm9yIG1lc3NhZ2UgdG9cbiAgICAgIC8vIHRoZSB1c2VyIHNvIGhlIGtub3dzIGV4YWN0bHkgd2hhdCBpcyB3cm9uZyBhbmQgY2FuIG1vdmUgZm9yd2FyZCBvciBhZGp1c3QgZm9yIGFcbiAgICAgIC8vIGRldmljZS5cbiAgICAgIGZ1bmN0aW9uIChlcnJvcikge1xuICAgICAgICBpZiAocHJvY2Vzcy5lbnYuTk9ERV9FTlYgPT09IFwiZGV2ZWxvcG1lbnRcIikge1xuICAgICAgICAgIGNvbnNvbGUubG9nKGVycm9yKTtcbiAgICAgICAgfVxuXG4gICAgICAgIGl6aVRvYXN0LmVycm9yKHtcbiAgICAgICAgICB0aXRsZTogXCJbUFVTSCBOT1RJRklDQVRJT04gU1VCU0NSSVBUSU9OXVwiLFxuICAgICAgICAgIGJhbGxvb246IHRydWUsXG4gICAgICAgICAgcG9zaXRpb246IFwidG9wUmlnaHRcIixcbiAgICAgICAgICBhbmltYXRlSW5zaWRlOiB0cnVlLFxuICAgICAgICAgIG1lc3NhZ2U6IGAke2Vycm9yfWAsXG4gICAgICAgIH0pO1xuICAgICAgfVxuICAgICk7XG4gIH1cbiAgLy8tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tXG5cbiAgLy8gVGhlIGZ1bmN0aW9uIHRvIHRyaWdnZXIgdGhlIHB1c2ggbm90aWZpY2F0aW9uIGZyb20gdGhlIGJyb3dzZXJcbiAgLy8tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tXG5cbiAgZnVuY3Rpb24gc2V0dXBUcmlnZ2VyQnV0dG9uKHN1YnNjcmlwdGlvbikge1xuICAgIGlmIChkb2N1bWVudC5nZXRFbGVtZW50QnlJZChcbiAgICAgIFwidHJpZ2dlck5vdGlmaWNhdGlvbkJ1dHRvblwiXG4gICAgKSl7XG4gICAgICBjb25zdCB0cmlnZ2VyTm90aWZpY2F0aW9uQnV0dG9uID0gZG9jdW1lbnQuZ2V0RWxlbWVudEJ5SWQoXG4gICAgICAgIFwidHJpZ2dlck5vdGlmaWNhdGlvbkJ1dHRvblwiXG4gICAgICApO1xuICAgICAgdHJpZ2dlck5vdGlmaWNhdGlvbkJ1dHRvbi5jbGFzc0xpc3QudG9nZ2xlKFwiaGlkZGVuXCIsIGZhbHNlKTtcblxuICAgICAgdHJpZ2dlck5vdGlmaWNhdGlvbkJ1dHRvbi5hZGRFdmVudExpc3RlbmVyKFwiY2xpY2tcIiwgKCkgPT4ge1xuICAgICAgICBjb25zdCBzdWJKc29uID0gc3Vic2NyaXB0aW9uLnRvSlNPTigpO1xuICAgICAgICBjb25zdCBlbmRwb2ludFBhcnRzID0gc3ViSnNvbi5lbmRwb2ludC5zcGxpdChcIi9cIik7XG4gICAgICAgIGNvbnN0IHJlZ2lzdHJhdGlvbklkID0gZW5kcG9pbnRQYXJ0c1tlbmRwb2ludFBhcnRzLmxlbmd0aCAtIDFdO1xuICAgICAgICBjb25zdCBwcmVkYXRhID0ge1xuICAgICAgICAgIHJlZ2lzdHJhdGlvbl9pZDogcmVnaXN0cmF0aW9uSWQsXG4gICAgICAgICAgYXV0aDogc3ViSnNvbi5rZXlzLmF1dGgsXG4gICAgICAgICAgZ3JvdXA6IFwidXNlcnNcIixcbiAgICAgICAgICBoZWFkOiBcIlRyaWdnZXIgVGVzdCBOb3RpZmljYXRpb25cIixcbiAgICAgICAgICBib2R5OiBcIlRoaXMgaXMgYSB0ZXN0IG5vdGlmaWNhdGlvblwiLFxuICAgICAgICB9O1xuXG4gICAgICAgIGNvbnN0IGRhdGEgPSBKU09OLnN0cmluZ2lmeShwcmVkYXRhKTtcblxuICAgICAgICBheGlvc1xuICAgICAgICAgIC5wb3N0KFNFTkRfTk9USUZJQ0FUSU9OLCBkYXRhLCB7XG4gICAgICAgICAgICBoZWFkZXJzOiB7XG4gICAgICAgICAgICAgIFwiQ29udGVudC1UeXBlXCI6IFwiYXBwbGljYXRpb24vanNvblwiLFxuICAgICAgICAgICAgfSxcbiAgICAgICAgICB9KVxuICAgICAgICAgIC50aGVuKGZ1bmN0aW9uIChyZXNwb25zZSkge1xuICAgICAgICAgICAgaXppVG9hc3Quc3VjY2Vzcyh7XG4gICAgICAgICAgICAgIHRpdGxlOiBcIltQVVNIIE5PVElGSUNBVElPTiBURVNUIFNVQ0NFU1NGVUxdXCIsXG4gICAgICAgICAgICAgIGJhbGxvb246IHRydWUsXG4gICAgICAgICAgICAgIHBvc2l0aW9uOiBcInRvcFJpZ2h0XCIsXG4gICAgICAgICAgICAgIGFuaW1hdGVJbnNpZGU6IHRydWUsXG4gICAgICAgICAgICAgIG1lc3NhZ2U6IHJlc3BvbnNlLmRhdGEubWVzc2FnZSxcbiAgICAgICAgICAgIH0pO1xuICAgICAgICAgIH0pXG4gICAgICAgICAgLmNhdGNoKGZ1bmN0aW9uIChlcnJvcikge1xuICAgICAgICAgICAgaXppVG9hc3QuZXJyb3Ioe1xuICAgICAgICAgICAgICB0aXRsZTogXCJbUFVTSCBOT1RJRklDQVRJT04gVEVTVCBFUlJPUl1cIixcbiAgICAgICAgICAgICAgYmFsbG9vbjogdHJ1ZSxcbiAgICAgICAgICAgICAgcG9zaXRpb246IFwidG9wUmlnaHRcIixcbiAgICAgICAgICAgICAgYW5pbWF0ZUluc2lkZTogdHJ1ZSxcbiAgICAgICAgICAgICAgbWVzc2FnZTogZXJyb3IucmVzcG9uc2UuZGF0YS5kZXRhaWwsXG4gICAgICAgICAgICB9KTtcbiAgICAgICAgICB9KTtcbiAgICAgIH0pO1xuICAgIH1cbiAgICByZXR1cm47XG4gIH1cbiAgLy8tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tXG5cbiAgLy8gZW5hYmxlIHNlcnZpY2Ugd29ya2VyLCB0aGVuIHdoZW4gc2VydmljZSB3b3JrZXIgaXMgZW5hYmxlZCByZXF1ZXN0XG4gIC8vIHBlcm1pc3Npb24gZm9yIHB1c2ggbm90aWZpY2F0aW9uIGFuZCBsb2NhdGlvbiBzZXJ2aWNlcyBmcm9tIHRoZSBicm93c2VyXG4gIC8vLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLVxuICBpZiAoXCJzZXJ2aWNlV29ya2VyXCIgaW4gbmF2aWdhdG9yKSB7XG4gICAgd2luZG93LmFkZEV2ZW50TGlzdGVuZXIoXCJsb2FkXCIsICgpID0+IHtcbiAgICAgIG5hdmlnYXRvci5zZXJ2aWNlV29ya2VyXG4gICAgICAgIC5yZWdpc3RlcihzdywgeyBzY29wZTogaG9tZSB9KVxuICAgICAgICAudGhlbigocmVnaXN0cmF0aW9uKSA9PiB7XG4gICAgICAgICAgaWYgKHByb2Nlc3MuZW52Lk5PREVfRU5WID09PSBcImRldmVsb3BtZW50XCIpIHtcbiAgICAgICAgICAgIGNvbnNvbGUubG9nKFwiU2VydmljZSB3b3JrZXIgcmVnaXN0ZXJhdGlvbiBzdWNjZWVkZWQ6IFwiLCByZWdpc3RyYXRpb24pO1xuICAgICAgICAgIH1cblxuICAgICAgICAgIG5hdmlnYXRvci5zZXJ2aWNlV29ya2VyLnJlYWR5LnRoZW4oZnVuY3Rpb24gKHJlZ2lzdHJhdGlvbikge1xuICAgICAgICAgICAgaWYgKHByb2Nlc3MuZW52Lk5PREVfRU5WID09PSBcImRldmVsb3BtZW50XCIpIHtcbiAgICAgICAgICAgICAgY29uc29sZS5sb2coXCJTZXJ2aWNlIHdvcmtlciBpcyBhY3RpdmU6IFwiLCByZWdpc3RyYXRpb24uYWN0aXZlKTtcbiAgICAgICAgICAgIH1cblxuICAgICAgICAgICAgaW5pdGlhbGlzZVN0YXRlKHJlZ2lzdHJhdGlvbik7XG4gICAgICAgICAgfSk7XG4gICAgICAgIH0pXG4gICAgICAgIC5jYXRjaCgoZXJyKSA9PiB7XG4gICAgICAgICAgaXppVG9hc3QuZXJyb3Ioe1xuICAgICAgICAgICAgdGl0bGU6IFwiW1NFUlZJQ0UgV09SS0VSXVwiLFxuICAgICAgICAgICAgYmFsbG9vbjogdHJ1ZSxcbiAgICAgICAgICAgIHBvc2l0aW9uOiBcInRvcFJpZ2h0XCIsXG4gICAgICAgICAgICBhbmltYXRlSW5zaWRlOiB0cnVlLFxuICAgICAgICAgICAgbWVzc2FnZTogXCJTZXJ2aWNlIFdvcmtlciBGYWlsZWQgdG8gUmVnaXN0ZXJcIixcbiAgICAgICAgICB9KTtcblxuICAgICAgICAgIGlmIChwcm9jZXNzLmVudi5OT0RFX0VOViA9PT0gXCJkZXZlbG9wbWVudFwiKSB7XG4gICAgICAgICAgICBjb25zb2xlLmxvZyhlcnIpO1xuICAgICAgICAgIH1cbiAgICAgICAgfSk7XG4gICAgfSk7XG4gIH1cblxuICBjb25zdCBpbml0aWFsaXNlU3RhdGUgPSAocmVnKSA9PiB7XG4gICAgaWYgKCFyZWcuc2hvd05vdGlmaWNhdGlvbikge1xuICAgICAgaXppVG9hc3QuZXJyb3Ioe1xuICAgICAgICB0aXRsZTogXCJbUFVTSCBVTlNVUFBPUlRFRF1cIixcbiAgICAgICAgYmFsbG9vbjogdHJ1ZSxcbiAgICAgICAgcG9zaXRpb246IFwidG9wUmlnaHRcIixcbiAgICAgICAgYW5pbWF0ZUluc2lkZTogdHJ1ZSxcbiAgICAgICAgbWVzc2FnZTogXCJTaG93aW5nIDxzdHJvbmc+UFVTSCBOT1RJRklDQVRJT05TPC9zdHJvbmc+IGlzIHVuc3VwcG9ydGVkXCIsXG4gICAgICB9KTtcbiAgICAgIHJldHVybjtcbiAgICB9XG5cbiAgICBpZiAoTm90aWZpY2F0aW9uLnBlcm1pc3Npb24gPT09IFwiZGVuaWVkXCIpIHtcbiAgICAgIGl6aVRvYXN0Lndhcm5pbmcoe1xuICAgICAgICB0aXRsZTogXCJbUFVTSCBERU5JRURdXCIsXG4gICAgICAgIGJhbGxvb246IHRydWUsXG4gICAgICAgIHBvc2l0aW9uOiBcInRvcFJpZ2h0XCIsXG4gICAgICAgIGFuaW1hdGVJbnNpZGU6IHRydWUsXG4gICAgICAgIG1lc3NhZ2U6XG4gICAgICAgICAgXCJZb3UgcHJldmVudGVkIHVzIGZyb20gc2h3b2luZyBub3RpZmljYXRpb25zLiBNYW51YWxseSBjaGVjayBpZiB5b3UgaGF2ZSBwcmV2ZW50ZWQgcHVzaCBub3RpZmNhdGlvbiBmcm9tIHVzLlwiLFxuICAgICAgfSk7XG4gICAgICByZXR1cm47XG4gICAgfVxuXG4gICAgaWYgKCEoXCJQdXNoTWFuYWdlclwiIGluIHdpbmRvdykpIHtcbiAgICAgIGl6aVRvYXN0LmluZm8oe1xuICAgICAgICB0aXRsZTogXCJbUFVTSCBCUk9XU0VSIFVOQVZBSUxCQUxFXVwiLFxuICAgICAgICBiYWxsb29uOiB0cnVlLFxuICAgICAgICBwb3NpdGlvbjogXCJ0b3BSaWdodFwiLFxuICAgICAgICBhbmltYXRlSW5zaWRlOiB0cnVlLFxuICAgICAgICBtZXNzYWdlOiBcIlB1c2ggbm90aWZpY2F0aW9uIGlzIG5vdCBhbGxvd2VkIGluIHlvdXIgYnJvd3Nlci5cIixcbiAgICAgIH0pO1xuICAgICAgcmV0dXJuO1xuICAgIH1cblxuICAgIHJlZy5wdXNoTWFuYWdlci5nZXRTdWJzY3JpcHRpb24oKS50aGVuKChzdWIpID0+IHtcbiAgICAgIGlmICghc3ViKSB7XG4gICAgICAgIHN1YnNjcmliZShyZWcpO1xuICAgICAgfSBlbHNlIHtcbiAgICAgICAgc2V0dXBUcmlnZ2VyQnV0dG9uKHN1Yik7XG4gICAgICAgIGl6aVRvYXN0LmluZm8oe1xuICAgICAgICAgIHRpdGxlOiBcIltTRVJWSUNFIFdPUktFUl1cIixcbiAgICAgICAgICBiYWxsb29uOiB0cnVlLFxuICAgICAgICAgIHBvc2l0aW9uOiBcInRvcFJpZ2h0XCIsXG4gICAgICAgICAgYW5pbWF0ZUluc2lkZTogdHJ1ZSxcbiAgICAgICAgICBtZXNzYWdlOiBcIlB1c2ggbm90aWZpY2F0aW9uIGhhcyBhbHJlYWR5IGJlZW4gc3Vic2NyaWJlZCB0b1wiLFxuICAgICAgICB9KTtcbiAgICAgIH1cbiAgICB9KTtcbiAgfTtcblxuICAvLy0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS1cblxuICAvLyAtLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLVxuICAvLyBJTlNUQUxMIEJVVFRPTiBGT1IgUFJPR1JFU1NJVkUgV0VCIEFQUExJQ0FUSU9OXG4gIC8vIC0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLVxuICBpZiAoZG9jdW1lbnQuZ2V0RWxlbWVudEJ5SWQoXCJpbnN0YWxsQnV0dG9uXCIpKXtcbiAgICBjb25zdCBpbnN0YWxsQnV0dG9uID0gZG9jdW1lbnQuZ2V0RWxlbWVudEJ5SWQoXCJpbnN0YWxsQnV0dG9uXCIpO1xuICAvLyB3aGVuIHBhZ2UgbG9hZHMgZm9yIHRoZSBmaXJzdCB0aW1lLCBpbnN0YWxsIGJ1dHRvbiB3aWxsIGJlIHZpc2libGVcbiAgLy8gaWYgdGhlIHVzZXIgaGFzIG5vdCBpbnN0YWxsZWQgdGhlIGFwcCBvciBQV0EuXG4gIHdpbmRvdy5hZGRFdmVudExpc3RlbmVyKFwiYmVmb3JlaW5zdGFsbHByb21wdFwiLCAoZXZlbnQpID0+IHtcbiAgICBpZiAocHJvY2Vzcy5lbnYuTk9ERV9FTlYgPT09IFwiZGV2ZWxvcG1lbnRcIikge1xuICAgICAgY29uc29sZS5sb2coXCLwn5GNW1BXQV1cIiwgXCJiZWZvcmVpbnN0YWxscHJvbXB0XCIsIGV2ZW50KTtcbiAgICB9XG4gICAgLy8gU3Rhc2ggdGhlIGV2ZW50IHNvIGl0IGNhbiBiZSB0cmlnZ2VyZWQgbGF0ZXIuXG4gICAgd2luZG93LmRlZmVycmVkUHJvbXB0ID0gZXZlbnQ7XG4gICAgLy8gUmVtb3ZlIHRoZSAnaGlkZGVuJyBjbGFzcyBmcm9tIHRoZSBpbnN0YWxsIGJ1dHRvbiBjb250YWluZXJcbiAgICAvLyBpZiB0aGUgUFdBIGhhcyBiZWVuIGluc3RhbGxlZCwgaGlkZSB0aGUgaW5zdGFsbCBidXR0b24gb3IgaWYgaXQgaGFzIG5vdFxuICAgIC8vIHRoZW4gYWxsb3cgZm9yIGNsaWNrXG4gICAgaW5zdGFsbEJ1dHRvbi5jbGFzc0xpc3QudG9nZ2xlKFwiaGlkZGVuXCIsIGZhbHNlKTtcbiAgfSk7XG5cbiAgaW5zdGFsbEJ1dHRvbi5hZGRFdmVudExpc3RlbmVyKFwiY2xpY2tcIiwgKCkgPT4ge1xuICAgIGlmIChwcm9jZXNzLmVudi5OT0RFX0VOViA9PT0gXCJkZXZlbG9wbWVudFwiKSB7XG4gICAgICBjb25zb2xlLmxvZyhcIvCfkY1bUFdBXSBJbnN0YWxsIEJ1dHRvbiBDbGlja2VkXCIpO1xuICAgIH1cblxuICAgIGNvbnN0IHByb21wdEV2ZW50ID0gd2luZG93LmRlZmVycmVkUHJvbXB0O1xuICAgIGlmICghcHJvbXB0RXZlbnQpIHtcbiAgICAgIC8vIFRoZSBkZWZlcnJlZCBwcm9tcHQgaXNuJ3QgYXZhaWxhYmxlLiBzbyByZXR1cm4gbm90aGluZ1xuICAgICAgcmV0dXJuO1xuICAgIH1cbiAgICBwcm9tcHRFdmVudC5wcm9tcHQoKTtcbiAgICBwcm9tcHRFdmVudC51c2VyQ2hvaWNlLnRoZW4oKGNob2ljZSkgPT4ge1xuICAgICAgaWYgKHByb2Nlc3MuZW52Lk5PREVfRU5WID09PSBcImRldmVsb3BtZW50XCIpIHtcbiAgICAgICAgY29uc29sZS5sb2coXCLwn5GNW1BXQV0gVXNlciBDaG9pY2U6IFwiLCBjaG9pY2UpO1xuICAgICAgfVxuICAgICAgLy8gaXppVG9hc3Quc3VjY2Vzcyh7XG4gICAgICAvLyAgIHRpdGxlOiBgW1BXQTogJHtjaG9pY2V9XWAsXG4gICAgICAvLyAgIG1lc3NhZ2U6ICfwn5GNIFlvdSBoYXZlIHN1Y2Nlc3NmdWxseSBpbnN0YWxsZWQgdGhlIHJlYWR2aWxsZSBhcHAnLFxuICAgICAgLy8gfSk7XG4gICAgICAvLyBSZXNldCB0aGUgZGVmZXJyZWQgcHJvbXB0IHZhcmlhYmxlLCBzaW5jZVxuICAgICAgLy8gcHJvbXB0KCkgY2FuIG9ubHkgYmUgY2FsbGVkIG9uY2UuXG4gICAgICB3aW5kb3cuZGVmZXJyZWRQcm9tcHQgPSBudWxsO1xuICAgICAgLy8gSGlkZSB0aGUgaW5zdGFsbCBidXR0b24gb25jZSB0aGUgUFdBIGhhcyBiZWVuIGluc3RhbGxlZFxuICAgICAgaW5zdGFsbEJ1dHRvbi5jbGFzc0xpc3QudG9nZ2xlKFwiaGlkZGVuXCIsIHRydWUpO1xuICAgIH0pO1xuICB9KTtcbiAgLy8tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tXG4gIH1cblxuXG4gIC8vIGlmIGFwcCBpcyBpbnN0YWxsZWQsIHRoYW5rIHRoZSB1c2VyIGZvciBpbnN0YWxsaW5nIHRoZSBhcHBcbiAgLy8tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tXG4gIHdpbmRvdy5hZGRFdmVudExpc3RlbmVyKFwiYXBwaW5zdGFsbGVkXCIsIChldmVudCkgPT4ge1xuICAgIGlmIChwcm9jZXNzLmVudi5OT0RFX0VOViA9PT0gXCJkZXZlbG9wbWVudFwiKSB7XG4gICAgICBjb25zb2xlLmxvZyhcIvCfkY1bUFdBXSBJbnN0YWxsZWQgU3RhdGU6IFwiLCBldmVudCk7XG4gICAgfVxuXG4gICAgaXppVG9hc3QuaW5mbyh7XG4gICAgICB0aXRsZTogYFtTRVJWSUNFIFdPUktFUl1gLFxuICAgICAgYmFsbG9vbjogdHJ1ZSxcbiAgICAgIHBvc2l0aW9uOiBcInRvcFJpZ2h0XCIsXG4gICAgICBhbmltYXRlSW5zaWRlOiB0cnVlLFxuICAgICAgbWVzc2FnZTogXCJEcm9wc3JpZGUgQXBwcmVjaWF0ZXMgWW91ciBTdXBwb3J0LlwiLFxuICAgIH0pO1xuICB9KTtcbiAgLy8tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tXG5cblxuXG4gIC8vIEhUTVggQ29uc29sZSBsb2dzXG4gIGlmIChwcm9jZXNzLmVudi5OT0RFX0VOViA9PT0gXCJkZXZlbG9wbWVudFwiKSB7XG4gICAgLy8gZW5hYmxlIGxvZ2dpbmcgZm9yIGh0bXggaW4gZGV2ZWxvcG1lbnQgc2VydmVyIG9ubHlcbiAgICB3aW5kb3cuaHRteC5sb2dBbGwoKTtcbiAgfVxuXG4gIFtcbiAgICBcImh0bXg6b25Mb2FkXCIsXG4gICAgXCJodG14OmxvYWRcIixcbiAgICBcImxvYWRcIixcbiAgICBcImh0bXg6YWZ0ZXJTd2FwXCIsXG4gICAgXCJodG14OmFmdGVyT25Mb2FkXCIsXG4gICAgXCJodG14OmFmdGVyUmVxdWVzdFwiLFxuICBdLmZvckVhY2goKGV2dCkgPT4ge1xuICAgIHdpbmRvdy5hZGRFdmVudExpc3RlbmVyKGV2dCwgZnVuY3Rpb24gKCkge1xuXG4gICAgY29uc3QgY291bnRlcnMgPSBkb2N1bWVudC5xdWVyeVNlbGVjdG9yQWxsKFwiLmNvdW50ZXJcIik7XG4gICAgY29uc3QgY2FyID0gZG9jdW1lbnQuZ2V0RWxlbWVudEJ5SWQoJ2NhcicpO1xuXG4gICAgY29uc3QgY29udHJvbGxlciA9IG5ldyBTY3JvbGxNYWdpYy5Db250cm9sbGVyKCk7XG5cbiAgICAvLyBpZihkb2N1bWVudC5nZXRFbGVtZW50QnlJZCgnY29uc3QnKSl7XG4gICAgLy8gICBsb3R0aWV3ZWIubG9hZEFuaW1hdGlvbih7XG4gICAgLy8gICAgIGNvbnRhaW5lcjogZG9jdW1lbnQuZ2V0RWxlbWVudEJ5SWQoJ2NvbnN0JyksXG4gICAgLy8gICAgIHBhdGg6IFwiL3N0YXRpYy92ZW5kb3JzL2ltYWdlcy9sb3R0aWUvdW5kZXItY29uc3RydWN0aW9uLmpzb25cIixcbiAgICAvLyAgICAgcmVuZGVyZXI6ICdzdmcnLFxuICAgIC8vICAgICBsb29wOiB0cnVlLFxuICAgIC8vICAgICBhdXRvUGxheTogdHJ1ZSxcbiAgICAvLyAgICAgbmFtZTogJ1VuZGVyIENvbnN0cnVjdGlvbidcbiAgICAvLyAgIH0pO1xuICAgIC8vIH1cblxuICAgIGZ1bmN0aW9uIHN0YXJ0Q291bnRpbmcoKSB7XG4gICAgICBpZiAoY291bnRlcnMpIHtcbiAgICAgICAgY291bnRlcnMuZm9yRWFjaCgoY291bnRlcikgPT4ge1xuICAgICAgICAgIGFuaW1lKHtcbiAgICAgICAgICAgIHRhcmdldHM6IGNvdW50ZXIsXG4gICAgICAgICAgICBpbm5lckhUTUw6IFswLCBjb3VudGVyLmdldEF0dHJpYnV0ZShcImRhdGEtY291bnRcIildLFxuICAgICAgICAgICAgZWFzaW5nOiBcImVhc2VJbk91dFNpbmVcIixcbiAgICAgICAgICAgIHJvdW5kOiAxLFxuICAgICAgICAgICAgZHVyYXRpb246IDQwMDAsXG4gICAgICAgICAgfSk7XG4gICAgICAgIH0pO1xuICAgICAgfVxuICAgIH1cblxuICAgIGZ1bmN0aW9uIGFuaW1hdGVIb3dzKCkge1xuICAgICAgaWYgKGRvY3VtZW50LnF1ZXJ5U2VsZWN0b3JBbGwoJy5ob3cnKSkge1xuICAgICAgICBhbmltZSh7XG4gICAgICAgICAgdGFyZ2V0czogXCIuaG93XCIsXG4gICAgICAgICAgdHJhbnNsYXRlWDogNTYsXG4gICAgICAgICAgZWFzaW5nOiBcImVhc2VJbk91dFNpbmVcIixcbiAgICAgICAgICBkdXJhdGlvbjogODAwLFxuICAgICAgICAgIG9wYWNpdHk6IDEsXG4gICAgICAgICAgZGVsYXk6IGFuaW1lLnN0YWdnZXIoMjAwLCB7IHN0YXJ0OiA1MDAgfSksXG4gICAgICAgIH0pO1xuICAgICAgfVxuICAgIH1cblxuICAgIGlmKGRvY3VtZW50LmdldEVsZW1lbnRCeUlkKCdjb3VudFRyaWdnZXInKSkge1xuICAgICAgbmV3IFNjcm9sbE1hZ2ljLlNjZW5lKHtcbiAgICAgICAgdHJpZ2dlckVsZW1lbnQ6ICcjY291bnRUcmlnZ2VyJyxcbiAgICAgICAgdHJpZ2dlckhvb2s6ICdvbkVudGVyJyxcbiAgICAgICAgZHVyYXRpb246ICcxMDAlJyxcbiAgICAgICAgcmV2ZXJzZTogZmFsc2UsXG4gICAgICAgIG9mZnNldDogNTBcbiAgICAgIH0pLm9uKCdlbnRlcicsIGZ1bmN0aW9uKCkge1xuICAgICAgICBzdGFydENvdW50aW5nKCk7XG4gICAgICB9KS5hZGRUbyhjb250cm9sbGVyKTtcbiAgICB9XG5cbiAgICBpZihkb2N1bWVudC5nZXRFbGVtZW50QnlJZCgndHJhY2snKSkge1xuICAgICAgICBuZXcgU2Nyb2xsTWFnaWMuU2NlbmUoe1xuICAgICAgICB0cmlnZ2VyRWxlbWVudDogJyN0cmFjaycsXG4gICAgICAgIHRyaWdnZXJIb29rOiAnb25FbnRlcicsXG4gICAgICAgIGR1cmF0aW9uOiAnMTAwJScsXG4gICAgICAgIHJldmVyc2U6IHRydWUsXG4gICAgICAgIG9mZnNldDogNTBcbiAgICAgIH0pLm9uKCdlbnRlcicsIGZ1bmN0aW9uKCkge1xuICAgICAgICBjYXJEcml2ZSgpO1xuICAgICAgfSkuYWRkVG8oY29udHJvbGxlcik7XG4gICAgfVxuXG5cbiAgICBpZihkb2N1bWVudC5nZXRFbGVtZW50QnlJZCgnaG93cycpKSB7XG4gICAgICBuZXcgU2Nyb2xsTWFnaWMuU2NlbmUoe1xuICAgICAgICB0cmlnZ2VyRWxlbWVudDogJyNob3dzJyxcbiAgICAgICAgdHJpZ2dlckhvb2s6ICdvbkVudGVyJyxcbiAgICAgICAgZHVyYXRpb246ICcxMDAlJyxcbiAgICAgICAgcmV2ZXJzZTogZmFsc2UsXG4gICAgICAgIG9mZnNldDogMTAwXG4gICAgICB9KS5vbignZW50ZXInLCBmdW5jdGlvbigpIHtcbiAgICAgICAgYW5pbWF0ZUhvd3MoKTtcbiAgICAgIH0pLmFkZFRvKGNvbnRyb2xsZXIpO1xuICAgIH1cblxuICAgIGlmKGRvY3VtZW50LnF1ZXJ5U2VsZWN0b3JBbGwoJy5pbnRybycpKSB7XG4gICAgICBhbmltZSh7XG4gICAgICAgIHRhcmdldHM6IFwiLmludHJvXCIsXG4gICAgICAgIHRyYW5zbGF0ZVg6IC01NixcbiAgICAgICAgZWFzaW5nOiBcImVhc2VJbk91dFNpbmVcIixcbiAgICAgICAgZHVyYXRpb246IDgwMCxcbiAgICAgICAgb3BhY2l0eTogMSxcbiAgICAgICAgZGVsYXk6IGFuaW1lLnN0YWdnZXIoMjAwLCB7IHN0YXJ0OiA1MDAgfSksXG4gICAgICB9KTtcbiAgICB9XG5cblxuICAgIGZ1bmN0aW9uIGNhckRyaXZlKCkge1xuICAgICAgaWYgKGNhcikge1xuICAgICAgICBhbmltZSh7XG4gICAgICAgICAgdGFyZ2V0czogXCIjY2FyXCIsXG4gICAgICAgICAgdHJhbnNsYXRlWDoge1xuICAgICAgICAgICAgdmFsdWU6IFwiLTEwMHZ3XCIsXG4gICAgICAgICAgICBkdXJhdGlvbjogNTAwMCxcbiAgICAgICAgICB9LFxuICAgICAgICAgIGVhc2luZzogXCJlYXNlSW5PdXRTaW5lXCIsXG4gICAgICAgICAgb3BhY2l0eTogMSxcbiAgICAgICAgICBkZWxheTogYW5pbWUuc3RhZ2dlcigyMDAsIHsgc3RhcnQ6IDUwMCB9KSxcbiAgICAgICAgICBkaXJlY3Rpb246IFwibm9ybWFsXCIsXG4gICAgICAgICAgbG9vcDogZmFsc2UsXG4gICAgICAgIH0pO1xuICAgICAgfVxuICAgIH1cbiAgfSk7XG59KTtcbiIsImltcG9ydCBheGlvcyBmcm9tIFwiLi9heGlvc0ZhY3RvcnlcIjtcbmltcG9ydCBodG14IGZyb20gXCJodG14Lm9yZy9kaXN0L2h0bXhcIjtcbmltcG9ydCBpemlUb2FzdCBmcm9tICdpeml0b2FzdC9kaXN0L2pzL2l6aVRvYXN0Lm1pbi5qcyc7ICAvLyB5b3UgaGF2ZSBhY2Nlc3MgdG8gaXppVG9hc3Qgbm93XG5cblxuZnVuY3Rpb24gc2xlZXAobXMpIHtcbiAgICByZXR1cm4gbmV3IHdpbmRvdy5Qcm9taXNlKHJlc29sdmUgPT4gc2V0VGltZW91dChyZXNvbHZlLCBtcykpO1xufVxuXG5mdW5jdGlvbiB2YWxpZGF0ZUZpZWxkKGZvcm1FbGVtZW50LCBmaWVsZEVsZW1lbnQpIHtcbiAgICBsZXQgZm9ybURhdGEgPSBuZXcgRm9ybURhdGEoZm9ybUVsZW1lbnQpO1xuICAgIGZvcm1EYXRhLmFwcGVuZChcIl9fZmllbGRfbmFtZV9fXCIsIGZpZWxkRWxlbWVudC5uYW1lKTtcblxuICAgIGF4aW9zLnBvc3QoZm9ybUVsZW1lbnQuYWN0aW9uLCBmb3JtRGF0YSkudGhlbihmdW5jdGlvbiAocmVzcG9uc2UpIHtcbiAgICAgIGxldCBlcnJvcnMgPSByZXNwb25zZS5kYXRhLmVycm9ycztcbiAgICAgIGxldCBlcnJvcnNXcmFwcGVyRWxlbWVudCA9IGRvY3VtZW50LmdldEVsZW1lbnRCeUlkKGBlcnJvci13cmFwcGVyLSR7ZmllbGRFbGVtZW50Lm5hbWV9YCk7XG4gICAgICBpZiAoZXJyb3JzLmxlbmd0aCA9PT0gMCkge1xuICAgICAgICBkb2N1bWVudC5nZXRFbGVtZW50QnlJZCgnc3VibWl0JykuY2xhc3NMaXN0LnJlbW92ZSgnaGlkZGVuJyk7XG4gICAgICAgIGVycm9yc1dyYXBwZXJFbGVtZW50LmNsYXNzTGlzdC5hZGQoJ2hpZGRlbicpO1xuICAgICAgICBpZiAoZXJyb3JzV3JhcHBlckVsZW1lbnQpIHtcbiAgICAgICAgICBlcnJvcnNXcmFwcGVyRWxlbWVudC5pbm5lckhUTUwgPSBcIlwiO1xuICAgICAgICB9XG4gICAgICB9IGVsc2Uge1xuICAgICAgICBkb2N1bWVudC5nZXRFbGVtZW50QnlJZCgnc3VibWl0JykuY2xhc3NMaXN0LmFkZCgnaGlkZGVuJyk7XG4gICAgICAgIGVycm9yc1dyYXBwZXJFbGVtZW50LmNsYXNzTGlzdC5yZW1vdmUoJ2hpZGRlbicpO1xuICAgICAgICBlcnJvcnNXcmFwcGVyRWxlbWVudC5jbGFzc0xpc3QuYWRkKCdmbGV4Jyk7XG4gICAgICAgIGlmIChlcnJvcnNXcmFwcGVyRWxlbWVudCkge1xuICAgICAgICAgIGxldCBlcnJvcnNIdG1sID0gJyc7XG4gICAgICAgICAgZm9yIChsZXQgaSA9IDA7IGkgPCBlcnJvcnMubGVuZ3RoOyBpKyspIHtcbiAgICAgICAgICAgIGVycm9yc0h0bWwgKz0gYCR7ZXJyb3JzW2ldfWA7XG4gICAgICAgICAgfVxuICAgICAgICAgIGVycm9yc1dyYXBwZXJFbGVtZW50LmlubmVySFRNTCA9IGVycm9yc0h0bWw7XG4gICAgICAgIH1cbiAgICAgIH1cbiAgICB9KTtcbiAgfVxuXG5cbmV4cG9ydCBkZWZhdWx0IGZ1bmN0aW9uIEFjY291bnRGb3JtKCkge1xuICAgIHJldHVybiB7XG4gICAgICAgIHByb2Nlc3Npbmc6IGZhbHNlLFxuXG4gICAgICAgIGFzeW5jIHN1Ym1pdEZvcm0oKSB7XG4gICAgICAgICAgICB0aGlzLnByb2Nlc3NpbmcgPSB0cnVlO1xuXG4gICAgICAgICAgICBjb25zdCBmb3JtRWxlbWVudCA9IHRoaXMuJHJlZnMuZm9ybTtcbiAgICAgICAgICAgIGNvbnN0IGRpdiA9IGRvY3VtZW50LmdldEVsZW1lbnRCeUlkKCdmb3JtJyk7XG4gICAgICAgICAgICBjb25zdCBhY3Rpb24gPSBmb3JtRWxlbWVudC5hY3Rpb247XG4gICAgICAgICAgICBjb25zdCByZWRpcmVjdCA9IGZvcm1FbGVtZW50LmRhdGFzZXQucmVkaXJlY3Q7XG4gICAgICAgICAgICBjb25zdCBjc3JmID0gZm9ybUVsZW1lbnQuZGF0YXNldC5jc3JmO1xuICAgICAgICAgICAgbGV0IGRhdGEgPSBuZXcgRm9ybURhdGEoZm9ybUVsZW1lbnQpO1xuICAgICAgICAgICAgZm9ybUVsZW1lbnQucXVlcnlTZWxlY3RvckFsbChcIltuYW1lXVwiKS5mb3JFYWNoKGZpZWxkRWxlbWVudCA9PiB7XG4gICAgICAgICAgICAgICAgZGF0YS5hcHBlbmQoZmllbGRFbGVtZW50Lm5hbWUsIGZpZWxkRWxlbWVudC52YWx1ZSk7XG4gICAgICAgICAgICB9KTtcblxuICAgICAgICAgICAgaWYgKGZvcm1FbGVtZW50LmNoZWNrVmFsaWRpdHkoKSkge1xuICAgICAgICAgICAgICAgIGF3YWl0IGF4aW9zLnBvc3QoYWN0aW9uLCBkYXRhLCB7XG4gICAgICAgICAgICAgICAgICAgIGhlYWRlcnM6IHtcbiAgICAgICAgICAgICAgICAgICAgICAnWC1DU1JGVG9rZW4nOiBjc3JmLFxuICAgICAgICAgICAgICAgICAgICB9fSlcbiAgICAgICAgICAgICAgICAgICAgLnRoZW4oZnVuY3Rpb24gKHJlc3BvbnNlKSB7XG4gICAgICAgICAgICAgICAgICAgICAgICAvLyBjb25zb2xlLmluZm8oXCJSRVNQT05TRSBEQVRBOiBcIiwgcmVzcG9uc2UpO1xuXG4gICAgICAgICAgICAgICAgICAgICAgICBpZiAocmVzcG9uc2Uuc3RhdHVzID09PSAyMDAgfHwgcmVzcG9uc2Uuc3RhdHVzID09PSAyMDEpIHtcbiAgICAgICAgICAgICAgICAgICAgICAgICAgICBkaXYuaW5uZXJIVE1MID0gYFxuICAgICAgICAgICAgICAgICAgICAgICAgICAgICR7Zm9ybUVsZW1lbnR9XG4gICAgICAgICAgICAgICAgICAgICAgICAgICAgYDtcbiAgICAgICAgICAgICAgICAgICAgICAgICAgICBpemlUb2FzdC5zdWNjZXNzKHtcbiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgdGl0bGU6IHJlc3BvbnNlLmRhdGEudGl0bGUsXG4gICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIGJhbGxvb246IHRydWUsXG4gICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIHBvc2l0aW9uOiBcInRvcFJpZ2h0XCIsXG4gICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIGFuaW1hdGVJbnNpZGU6IHRydWUsXG4gICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIG1lc3NhZ2U6IHJlc3BvbnNlLmRhdGEubWVzc2FnZVxuICAgICAgICAgICAgICAgICAgICAgICAgICAgIH0pO1xuICAgICAgICAgICAgICAgICAgICAgICAgICAgIHNsZWVwKDM1MDApOyAvL3dhaXQgMSBzZWMgYW5kIHRoZW4gaHRteCByZWRpcmVjdCBnZXRcbiAgICAgICAgICAgICAgICAgICAgICAgICAgICBodG14LmFqYXgoJ0dFVCcsIHJlZGlyZWN0LCB7dGFyZ2V0OidtYWluJywgc3dhcDonb3V0ZXJIVE1MJ30pO1xuICAgICAgICAgICAgICAgICAgICAgICAgICAgIC8vIHNsZWVwKDM1MDApOyAvL3dhaXQgMSBzZWMgYW5kIHRoZW4gaHRteCByZWRpcmVjdCBnZXRcbiAgICAgICAgICAgICAgICAgICAgICAgICAgICAvLyBsb2NhdGlvbi5yZWxvYWQoKTtcbiAgICAgICAgICAgICAgICAgICAgICAgIH0gZWxzZSB7XG4gICAgICAgICAgICAgICAgICAgICAgICAgICAgaXppVG9hc3QuZXJyb3Ioe1xuICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICB0aXRsZTogcmVzcG9uc2UuZGF0YS50aXRsZSxcbiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgYmFsbG9vbjogdHJ1ZSxcbiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgcG9zaXRpb246IFwidG9wUmlnaHRcIixcbiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgYW5pbWF0ZUluc2lkZTogdHJ1ZSxcbiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgbWVzc2FnZTogcmVzcG9uc2UuZGF0YS5tZXNzYWdlXG4gICAgICAgICAgICAgICAgICAgICAgICAgICAgfSk7XG4gICAgICAgICAgICAgICAgICAgICAgICB9XG5cbiAgICAgICAgICAgICAgICAgICAgICAgIGNvbnNvbGUubG9nKHJlc3BvbnNlKTtcbiAgICAgICAgICAgICAgICAgICAgfSkuY2F0Y2goZnVuY3Rpb24gKGVycm9yKSB7XG4gICAgICAgICAgICAgICAgICAgICAgICBpemlUb2FzdC5lcnJvcih7XG4gICAgICAgICAgICAgICAgICAgICAgICAgICAgdGl0bGU6IFwiRm9ybSBFcnJvclwiLFxuICAgICAgICAgICAgICAgICAgICAgICAgICAgIGJhbGxvb246IHRydWUsXG4gICAgICAgICAgICAgICAgICAgICAgICAgICAgcG9zaXRpb246IFwidG9wUmlnaHRcIixcbiAgICAgICAgICAgICAgICAgICAgICAgICAgICBhbmltYXRlSW5zaWRlOiB0cnVlLFxuICAgICAgICAgICAgICAgICAgICAgICAgICAgIG1lc3NhZ2U6IGBTb21ldGhpbmcgd3JvbmcgaGFwcGVuZWQ6ICR7ZXJyb3J9YFxuICAgICAgICAgICAgICAgICAgICAgICAgfSk7XG4gICAgICAgICAgICAgICAgICAgIH0pO1xuICAgICAgICAgICAgICAgICAgICAvLyAuZmluYWxseShmdW5jdGlvbiAoKSB7XG4gICAgICAgICAgICAgICAgICAgIC8vICAgICBjb25zb2xlLmxvZyhcImZpbmFsbHlcIik7XG4gICAgICAgICAgICAgICAgICAgIC8vIH0pO1xuXG4gICAgICAgICAgICAgICAgdGhpcy5wcm9jZXNzaW5nID0gZmFsc2U7XG4gICAgICAgICAgICB9IGVsc2Uge1xuICAgICAgICAgICAgICAgIGl6aVRvYXN0LmVycm9yKHtcbiAgICAgICAgICAgICAgICAgICAgdGl0bGU6IFwiRm9ybSBTZW5kaW5nIEluY29tcGxldGVcIixcbiAgICAgICAgICAgICAgICAgICAgYmFsbG9vbjogdHJ1ZSxcbiAgICAgICAgICAgICAgICAgICAgcG9zaXRpb246IFwidG9wUmlnaHRcIixcbiAgICAgICAgICAgICAgICAgICAgYW5pbWF0ZUluc2lkZTogdHJ1ZSxcbiAgICAgICAgICAgICAgICAgICAgbWVzc2FnZTogYEZvcm0gZGF0YSBpcyBub3QgdmFsaWQuIEVuc3VyZSB5b3UgaGF2ZSBmaWxsZWQgYWxsIGZpZWxkcyBhY2N1cmF0ZWx5ISAke2Zvcm1FbGVtZW50LnJlcG9ydFZhbGlkaXR5KCl9YFxuICAgICAgICAgICAgICAgIH0pO1xuICAgICAgICAgICAgICAgIHNsZWVwKDI1MDApOyAvL3dhaXQgMi41IHNlYyBhbmQgdGhlbiBodG14IHJlZGlyZWN0IGdldFxuICAgICAgICAgICAgICAgIHRoaXMucHJvY2Vzc2luZyA9IGZhbHNlO1xuICAgICAgICAgICAgICAgIGh0bXguYWpheCgnR0VUJywgcmVkaXJlY3QsIHt0YXJnZXQ6J21haW4nLCBzd2FwOidvdXRlckhUTUwnfSk7XG4gICAgICAgICAgICB9XG5cbiAgICAgICAgfSxcblxuICAgICAgICBhc3luYyBzdWJtaXRGaWxlRm9ybSgpIHtcbiAgICAgICAgICAgIHRoaXMucHJvY2Vzc2luZyA9IHRydWU7XG5cbiAgICAgICAgICAgIGNvbnN0IGZvcm1FbGVtZW50ID0gdGhpcy4kcmVmcy5mb3JtO1xuICAgICAgICAgICAgY29uc3QgZGl2ID0gZG9jdW1lbnQuZ2V0RWxlbWVudEJ5SWQoJ2Zvcm0nKTtcbiAgICAgICAgICAgIGNvbnN0IGFjdGlvbiA9IGZvcm1FbGVtZW50LmFjdGlvbjtcbiAgICAgICAgICAgIGNvbnN0IHJlZGlyZWN0ID0gZm9ybUVsZW1lbnQuZGF0YXNldC5yZWRpcmVjdDtcbiAgICAgICAgICAgIGNvbnN0IGNzcmYgPSBmb3JtRWxlbWVudC5kYXRhc2V0LmNzcmY7XG4gICAgICAgICAgICBsZXQgZGF0YSA9IG5ldyBGb3JtRGF0YShmb3JtRWxlbWVudCk7XG4gICAgICAgICAgICBmb3JtRWxlbWVudC5xdWVyeVNlbGVjdG9yQWxsKFwiW25hbWVdXCIpLmZvckVhY2goZmllbGRFbGVtZW50ID0+IHtcbiAgICAgICAgICAgICAgICBkYXRhLmFwcGVuZChmaWVsZEVsZW1lbnQubmFtZSwgZmllbGRFbGVtZW50LnZhbHVlKTtcbiAgICAgICAgICAgIH0pO1xuXG4gICAgICAgICAgICBpZiAoZm9ybUVsZW1lbnQuY2hlY2tWYWxpZGl0eSgpKSB7XG4gICAgICAgICAgICAgICAgYXdhaXQgYXhpb3MucG9zdChhY3Rpb24sIGRhdGEsIHtcbiAgICAgICAgICAgICAgICAgICAgaGVhZGVyczoge1xuICAgICAgICAgICAgICAgICAgICAgICdYLUNTUkZUb2tlbic6IGNzcmYsXG4gICAgICAgICAgICAgICAgICAgICAgJ0NvbnRlbnQtVHlwZSc6J211bHRpcGFydC9mb3JtLWRhdGEnXG4gICAgICAgICAgICAgICAgICAgIH19KVxuICAgICAgICAgICAgICAgICAgICAudGhlbihmdW5jdGlvbiAocmVzcG9uc2UpIHtcbiAgICAgICAgICAgICAgICAgICAgICAgIC8vIGNvbnNvbGUuaW5mbyhcIlJFU1BPTlNFIERBVEE6IFwiLCByZXNwb25zZSk7XG5cbiAgICAgICAgICAgICAgICAgICAgICAgIGlmIChyZXNwb25zZS5zdGF0dXMgPT09IDIwMCB8fCByZXNwb25zZS5zdGF0dXMgPT09IDIwMSkge1xuICAgICAgICAgICAgICAgICAgICAgICAgICAgIGRpdi5pbm5lckhUTUwgPSBgXG4gICAgICAgICAgICAgICAgICAgICAgICAgICAgJHtmb3JtRWxlbWVudH1cbiAgICAgICAgICAgICAgICAgICAgICAgICAgICBgO1xuICAgICAgICAgICAgICAgICAgICAgICAgICAgIGl6aVRvYXN0LnN1Y2Nlc3Moe1xuICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICB0aXRsZTogcmVzcG9uc2UuZGF0YS50aXRsZSxcbiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgYmFsbG9vbjogdHJ1ZSxcbiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgcG9zaXRpb246IFwidG9wUmlnaHRcIixcbiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgYW5pbWF0ZUluc2lkZTogdHJ1ZSxcbiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgbWVzc2FnZTogcmVzcG9uc2UuZGF0YS5tZXNzYWdlXG4gICAgICAgICAgICAgICAgICAgICAgICAgICAgfSk7XG4gICAgICAgICAgICAgICAgICAgICAgICAgICAgc2xlZXAoMzUwMCk7IC8vd2FpdCAxIHNlYyBhbmQgdGhlbiBodG14IHJlZGlyZWN0IGdldFxuICAgICAgICAgICAgICAgICAgICAgICAgICAgIGh0bXguYWpheCgnR0VUJywgcmVkaXJlY3QsIHt0YXJnZXQ6J21haW4nLCBzd2FwOidvdXRlckhUTUwnfSk7XG4gICAgICAgICAgICAgICAgICAgICAgICAgICAgLy8gc2xlZXAoMzUwMCk7IC8vd2FpdCAxIHNlYyBhbmQgdGhlbiBodG14IHJlZGlyZWN0IGdldFxuICAgICAgICAgICAgICAgICAgICAgICAgICAgIC8vIGxvY2F0aW9uLnJlbG9hZCgpO1xuICAgICAgICAgICAgICAgICAgICAgICAgfSBlbHNlIHtcbiAgICAgICAgICAgICAgICAgICAgICAgICAgICBpemlUb2FzdC5lcnJvcih7XG4gICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIHRpdGxlOiByZXNwb25zZS5kYXRhLnRpdGxlLFxuICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICBiYWxsb29uOiB0cnVlLFxuICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICBwb3NpdGlvbjogXCJ0b3BSaWdodFwiLFxuICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICBhbmltYXRlSW5zaWRlOiB0cnVlLFxuICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICBtZXNzYWdlOiByZXNwb25zZS5kYXRhLm1lc3NhZ2VcbiAgICAgICAgICAgICAgICAgICAgICAgICAgICB9KTtcbiAgICAgICAgICAgICAgICAgICAgICAgIH1cblxuICAgICAgICAgICAgICAgICAgICAgICAgY29uc29sZS5sb2cocmVzcG9uc2UpO1xuICAgICAgICAgICAgICAgICAgICB9KS5jYXRjaChmdW5jdGlvbiAoZXJyb3IpIHtcbiAgICAgICAgICAgICAgICAgICAgICAgIGl6aVRvYXN0LmVycm9yKHtcbiAgICAgICAgICAgICAgICAgICAgICAgICAgICB0aXRsZTogXCJGb3JtIEVycm9yXCIsXG4gICAgICAgICAgICAgICAgICAgICAgICAgICAgYmFsbG9vbjogdHJ1ZSxcbiAgICAgICAgICAgICAgICAgICAgICAgICAgICBwb3NpdGlvbjogXCJ0b3BSaWdodFwiLFxuICAgICAgICAgICAgICAgICAgICAgICAgICAgIGFuaW1hdGVJbnNpZGU6IHRydWUsXG4gICAgICAgICAgICAgICAgICAgICAgICAgICAgbWVzc2FnZTogYFNvbWV0aGluZyB3cm9uZyBoYXBwZW5lZDogJHtlcnJvcn1gXG4gICAgICAgICAgICAgICAgICAgICAgICB9KTtcbiAgICAgICAgICAgICAgICAgICAgfSk7XG4gICAgICAgICAgICAgICAgICAgIC8vIC5maW5hbGx5KGZ1bmN0aW9uICgpIHtcbiAgICAgICAgICAgICAgICAgICAgLy8gICAgIGNvbnNvbGUubG9nKFwiZmluYWxseVwiKTtcbiAgICAgICAgICAgICAgICAgICAgLy8gfSk7XG5cbiAgICAgICAgICAgICAgICB0aGlzLnByb2Nlc3NpbmcgPSBmYWxzZTtcbiAgICAgICAgICAgIH0gZWxzZSB7XG4gICAgICAgICAgICAgICAgaXppVG9hc3QuZXJyb3Ioe1xuICAgICAgICAgICAgICAgICAgICB0aXRsZTogXCJGb3JtIFNlbmRpbmcgSW5jb21wbGV0ZVwiLFxuICAgICAgICAgICAgICAgICAgICBiYWxsb29uOiB0cnVlLFxuICAgICAgICAgICAgICAgICAgICBwb3NpdGlvbjogXCJ0b3BSaWdodFwiLFxuICAgICAgICAgICAgICAgICAgICBhbmltYXRlSW5zaWRlOiB0cnVlLFxuICAgICAgICAgICAgICAgICAgICBtZXNzYWdlOiBgRm9ybSBkYXRhIGlzIG5vdCB2YWxpZC4gRW5zdXJlIHlvdSBoYXZlIGZpbGxlZCBhbGwgZmllbGRzIGFjY3VyYXRlbHkhICR7Zm9ybUVsZW1lbnQucmVwb3J0VmFsaWRpdHkoKX1gXG4gICAgICAgICAgICAgICAgfSk7XG4gICAgICAgICAgICAgICAgc2xlZXAoMjUwMCk7IC8vd2FpdCAyLjUgc2VjIGFuZCB0aGVuIGh0bXggcmVkaXJlY3QgZ2V0XG4gICAgICAgICAgICAgICAgdGhpcy5wcm9jZXNzaW5nID0gZmFsc2U7XG4gICAgICAgICAgICAgICAgaHRteC5hamF4KCdHRVQnLCByZWRpcmVjdCwge3RhcmdldDonbWFpbicsIHN3YXA6J291dGVySFRNTCd9KTtcbiAgICAgICAgICAgIH1cblxuICAgICAgICB9LFxuXG4gICAgICAgIGFzeW5jIGNoZWNrVmFsaWRpdHkoKSB7XG4gICAgICAgICAgICBjb25zdCBmb3JtRWxlbWVudCA9IHRoaXMuJHJlZnMuY29udGFjdEZvcm07XG4gICAgICAgICAgICBmb3JtRWxlbWVudC5xdWVyeVNlbGVjdG9yQWxsKCdbbmFtZV0nKS5mb3JFYWNoKGZpZWxkRWxlbWVudCA9PiB7XG4gICAgICAgICAgICAgICAgZmllbGRFbGVtZW50LmFkZEV2ZW50TGlzdGVuZXIoJ2NoYW5nZScsIGV2ZW50ID0+IHtcbiAgICAgICAgICAgICAgICAgICAgY29uc29sZS5sb2coZXZlbnQpO1xuICAgICAgICAgICAgICAgICAgICB2YWxpZGF0ZUZpZWxkKGZvcm1FbGVtZW50LCBmaWVsZEVsZW1lbnQpO1xuICAgICAgICAgICAgICAgIH0pO1xuICAgICAgICAgICAgfSk7XG4gICAgICAgIH0sXG5cbiAgICAgICAgZ2V0QnRuVGV4dCgpIHtcbiAgICAgICAgICAgIHJldHVybiB0aGlzLnByb2Nlc3NpbmcgPyAnUHJvY2Vzc2luZy4uLicgOiAnU3VibWl0JztcbiAgICAgICAgfVxuICAgIH07XG59XG4iLCJpbXBvcnQgYXhpb3MgZnJvbSBcIi4vYXhpb3NGYWN0b3J5XCI7XG5pbXBvcnQgaHRteCBmcm9tIFwiaHRteC5vcmcvZGlzdC9odG14XCI7XG5pbXBvcnQgaXppVG9hc3QgZnJvbSAnaXppdG9hc3QvZGlzdC9qcy9pemlUb2FzdC5taW4uanMnOyAgLy8geW91IGhhdmUgYWNjZXNzIHRvIGl6aVRvYXN0IG5vd1xuXG4vLyBmdW5jdGlvbiBzZXJpYWxpemUoZGF0YSkge1xuLy8gICAgIGxldCBvYmogPSB7fTtcbi8vICAgICBmb3IgKGxldCBba2V5LCB2YWx1ZV0gb2YgZGF0YSkge1xuLy8gICAgICAgaWYgKG9ialtrZXldICE9PSB1bmRlZmluZWQpIHtcbi8vICAgICAgICAgaWYgKCFBcnJheS5pc0FycmF5KG9ialtrZXldKSkge1xuLy8gICAgICAgICAgIG9ialtrZXldID0gW29ialtrZXldXTtcbi8vICAgICAgICAgfVxuLy8gICAgICAgICBvYmpba2V5XS5wdXNoKHZhbHVlKTtcbi8vICAgICAgIH0gZWxzZSB7XG4vLyAgICAgICAgIG9ialtrZXldID0gdmFsdWU7XG4vLyAgICAgICB9XG4vLyAgICAgfVxuLy8gICAgIHJldHVybiBvYmo7XG4vLyB9XG5cblxuZnVuY3Rpb24gc2xlZXAobXMpIHtcbiAgICByZXR1cm4gbmV3IHdpbmRvdy5Qcm9taXNlKHJlc29sdmUgPT4gc2V0VGltZW91dChyZXNvbHZlLCBtcykpO1xufVxuXG5mdW5jdGlvbiB2YWxpZGF0ZUZpZWxkKGZvcm1FbGVtZW50LCBmaWVsZEVsZW1lbnQpIHtcbiAgICBsZXQgZm9ybURhdGEgPSBuZXcgRm9ybURhdGEoZm9ybUVsZW1lbnQpO1xuICAgIGZvcm1EYXRhLmFwcGVuZChcIl9fZmllbGRfbmFtZV9fXCIsIGZpZWxkRWxlbWVudC5uYW1lKTtcblxuICAgIGF4aW9zLnBvc3QoZm9ybUVsZW1lbnQuYWN0aW9uLCBmb3JtRGF0YSkudGhlbihmdW5jdGlvbiAocmVzcG9uc2UpIHtcbiAgICAgIGxldCBlcnJvcnMgPSByZXNwb25zZS5kYXRhLmVycm9ycztcbiAgICAgIGxldCBlcnJvcnNXcmFwcGVyRWxlbWVudCA9IGRvY3VtZW50LmdldEVsZW1lbnRCeUlkKGBlcnJvci13cmFwcGVyLSR7ZmllbGRFbGVtZW50Lm5hbWV9YCk7XG4gICAgICBpZiAoZXJyb3JzLmxlbmd0aCA9PT0gMCkge1xuICAgICAgICBkb2N1bWVudC5nZXRFbGVtZW50QnlJZCgnc3VibWl0JykuY2xhc3NMaXN0LnJlbW92ZSgnaGlkZGVuJyk7XG4gICAgICAgIGVycm9yc1dyYXBwZXJFbGVtZW50LmNsYXNzTGlzdC5hZGQoJ2hpZGRlbicpO1xuICAgICAgICBpZiAoZXJyb3JzV3JhcHBlckVsZW1lbnQpIHtcbiAgICAgICAgICBlcnJvcnNXcmFwcGVyRWxlbWVudC5pbm5lckhUTUwgPSBcIlwiO1xuICAgICAgICB9XG4gICAgICB9IGVsc2Uge1xuICAgICAgICBkb2N1bWVudC5nZXRFbGVtZW50QnlJZCgnc3VibWl0JykuY2xhc3NMaXN0LmFkZCgnaGlkZGVuJyk7XG4gICAgICAgIGVycm9yc1dyYXBwZXJFbGVtZW50LmNsYXNzTGlzdC5yZW1vdmUoJ2hpZGRlbicpO1xuICAgICAgICBlcnJvcnNXcmFwcGVyRWxlbWVudC5jbGFzc0xpc3QuYWRkKCdmbGV4Jyk7XG4gICAgICAgIGlmIChlcnJvcnNXcmFwcGVyRWxlbWVudCkge1xuICAgICAgICAgIGxldCBlcnJvcnNIdG1sID0gJyc7XG4gICAgICAgICAgZm9yIChsZXQgaSA9IDA7IGkgPCBlcnJvcnMubGVuZ3RoOyBpKyspIHtcbiAgICAgICAgICAgIGVycm9yc0h0bWwgKz0gYCR7ZXJyb3JzW2ldfWA7XG4gICAgICAgICAgfVxuICAgICAgICAgIGVycm9yc1dyYXBwZXJFbGVtZW50LmlubmVySFRNTCA9IGVycm9yc0h0bWw7XG4gICAgICAgIH1cbiAgICAgIH1cbiAgICB9KTtcbiAgfVxuXG5cbmV4cG9ydCBkZWZhdWx0IGZ1bmN0aW9uIENvbnRhY3RGb3JtKCkge1xuICAgIHJldHVybiB7XG4gICAgICAgIHByb2Nlc3Npbmc6IGZhbHNlLFxuXG4gICAgICAgIGFzeW5jIHN1Ym1pdEZvcm0oKSB7XG4gICAgICAgICAgICB0aGlzLnByb2Nlc3NpbmcgPSB0cnVlO1xuXG4gICAgICAgICAgICBjb25zdCBmb3JtRWxlbWVudCA9IHRoaXMuJHJlZnMuY29udGFjdEZvcm07XG4gICAgICAgICAgICBjb25zdCBkaXYgPSBkb2N1bWVudC5nZXRFbGVtZW50QnlJZCgnY29udGFjdCcpO1xuICAgICAgICAgICAgY29uc3QgcmVkaXJlY3QgPSBmb3JtRWxlbWVudC5hY3Rpb247XG4gICAgICAgICAgICBjb25zdCBjc3JmID0gZm9ybUVsZW1lbnQuZGF0YXNldC5jc3JmO1xuICAgICAgICAgICAgbGV0IGRhdGEgPSBuZXcgRm9ybURhdGEoZm9ybUVsZW1lbnQpO1xuICAgICAgICAgICAgZm9ybUVsZW1lbnQucXVlcnlTZWxlY3RvckFsbChcIltuYW1lXVwiKS5mb3JFYWNoKGZpZWxkRWxlbWVudCA9PiB7XG4gICAgICAgICAgICAgICAgZGF0YS5hcHBlbmQoZmllbGRFbGVtZW50Lm5hbWUsIGZpZWxkRWxlbWVudC52YWx1ZSk7XG4gICAgICAgICAgICB9KTtcblxuICAgICAgICAgICAgY29uc29sZS5sb2coZGF0YSk7XG4gICAgICAgICAgICAvLyBkYXRhLmFwcGVuZCgnY3NyZm1pZGRsZXdhcmV0b2tlbicsIGNzcmYpO1xuICAgICAgICAgICAgLy8gZGF0YS5hcHBlbmQoJ25hbWUnLCBkb2N1bWVudC5nZXRFbGVtZW50QnlJZCgnaWRfbmFtZScpLnZhbHVlKTtcbiAgICAgICAgICAgIC8vIGRhdGEuYXBwZW5kKCdlbWFpbCcsIGRvY3VtZW50LmdldEVsZW1lbnRCeUlkKCdpZF9lbWFpbCcpLnZhbHVlKTtcbiAgICAgICAgICAgIC8vIGRhdGEuYXBwZW5kKCdtZXNzYWdlJywgZG9jdW1lbnQuZ2V0RWxlbWVudEJ5SWQoJ2lkX21lc3NhZ2UnKS52YWx1ZSk7XG5cbiAgICAgICAgICAgIC8vIGNvbnNvbGUuaW5mbyhcIkZPUk0gREFUQTogXCIsIGRhdGEpO1xuXG4gICAgICAgICAgICAvLyBsZXQgZm9ybURhdGEgPSBzZXJpYWxpemUoZGF0YSk7XG4gICAgICAgICAgICAvLyBjb25zb2xlLmluZm8oXCJTRVJJQUxJWkVEIEZPUk0gREFUQTogXCIsIGZvcm1EYXRhKTtcblxuXG4gICAgICAgICAgICBpZiAoZm9ybUVsZW1lbnQuY2hlY2tWYWxpZGl0eSgpKSB7XG4gICAgICAgICAgICAgICAgYXdhaXQgYXhpb3MucG9zdChyZWRpcmVjdCwgZGF0YSwge1xuICAgICAgICAgICAgICAgICAgICBoZWFkZXJzOiB7XG4gICAgICAgICAgICAgICAgICAgICAgJ1gtQ1NSRlRva2VuJzogY3NyZlxuICAgICAgICAgICAgICAgICAgICB9fSlcbiAgICAgICAgICAgICAgICAgICAgLnRoZW4oZnVuY3Rpb24gKHJlc3BvbnNlKSB7XG4gICAgICAgICAgICAgICAgICAgICAgICAvLyBjb25zb2xlLmluZm8oXCJSRVNQT05TRSBEQVRBOiBcIiwgcmVzcG9uc2UpO1xuXG4gICAgICAgICAgICAgICAgICAgICAgICBpZiAocmVzcG9uc2Uuc3RhdHVzID09PSAyMDAgfHwgcmVzcG9uc2UuZGF0YS5tZXNzYWdlID09PSBcIlN1cHBvcnQgTWFpbCBTdWNjZXNzZnVsbHkgU2VudFwiKSB7XG4gICAgICAgICAgICAgICAgICAgICAgICAgICAgZGl2LmlubmVySFRNTCA9IGBcbiAgICAgICAgICAgICAgICAgICAgICAgICAgICA8ZGl2IGNsYXNzPVwidy1mdWxsIHRleHQtZ3JlZW4tMzAwIHNwYWNlLXktOCBmbGV4IGZsZXgtY29sIGp1c3RpZnktY2VudGVyIHB5LTI0XCI+XG4gICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIDxzdmcgeG1sbnM9XCJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2Z1wiIGZpbGw9XCJub25lXCIgdmlld0JveD1cIjAgMCAyNCAyNFwiIHN0cm9rZS13aWR0aD1cIjEuNVwiIHN0cm9rZT1cImN1cnJlbnRDb2xvclwiIGNsYXNzPVwiYmxvY2sgdy0xNCBoLTE0IGJsb2NrIG14LWF1dG8gYW5pbWF0ZS1ib3VuY2UgdGV4dC1ncmVlbi0zMDBcIj5cbiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIDxwYXRoIHN0cm9rZS1saW5lY2FwPVwicm91bmRcIiBzdHJva2UtbGluZWpvaW49XCJyb3VuZFwiIGQ9XCJNMjEuNzUgNi43NXYxMC41YTIuMjUgMi4yNSAwIDAxLTIuMjUgMi4yNWgtMTVhMi4yNSAyLjI1IDAgMDEtMi4yNS0yLjI1VjYuNzVtMTkuNSAwQTIuMjUgMi4yNSAwIDAwMTkuNSA0LjVoLTE1YTIuMjUgMi4yNSAwIDAwLTIuMjUgMi4yNW0xOS41IDB2LjI0M2EyLjI1IDIuMjUgMCAwMS0xLjA3IDEuOTE2bC03LjUgNC42MTVhMi4yNSAyLjI1IDAgMDEtMi4zNiAwTDMuMzIgOC45MWEyLjI1IDIuMjUgMCAwMS0xLjA3LTEuOTE2VjYuNzVcIiAvPlxuICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICA8L3N2Zz5cbiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgPGRpdiBjbGFzcz1cInctZnVsbCBtZDp3LTMvNSB0ZXh0LWNlbnRlciBzcGFjZS15LTMgbXgtYXV0b1wiPlxuICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgPGg0IGNsYXNzPVwidGV4dC1ncmVlbi01MDAgZm9udC1zZW1pYm9sZCB0ZXh0LTJ4bCBtZDp0ZXh0LTR4bFwiPk1haWwgU2VudCBTdWNjZXNzZnVsbHk8L2g0PlxuICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgPHA+JHtyZXNwb25zZS5kYXRhLm1lc3NhZ2V9PC9wPlxuICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICA8L2Rpdj5cbiAgICAgICAgICAgICAgICAgICAgICAgICAgICA8L2Rpdj5cbiAgICAgICAgICAgICAgICAgICAgICAgICAgICBgO1xuICAgICAgICAgICAgICAgICAgICAgICAgICAgIGl6aVRvYXN0LnN1Y2Nlc3Moe1xuICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICB0aXRsZTogXCJFbWFpbCBTZW50IFN1Y2Nlc3NmdWxcIixcbiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgYmFsbG9vbjogdHJ1ZSxcbiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgcG9zaXRpb246IFwidG9wUmlnaHRcIixcbiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgYW5pbWF0ZUluc2lkZTogdHJ1ZSxcbiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgbWVzc2FnZTogcmVzcG9uc2UuZGF0YS5tZXNzYWdlXG4gICAgICAgICAgICAgICAgICAgICAgICAgICAgfSk7XG4gICAgICAgICAgICAgICAgICAgICAgICAgICAgc2xlZXAoMzUwMCk7IC8vd2FpdCAxIHNlYyBhbmQgdGhlbiBodG14IHJlZGlyZWN0IGdldFxuICAgICAgICAgICAgICAgICAgICAgICAgICAgIGh0bXguYWpheCgnR0VUJywgcmVkaXJlY3QsIHt0YXJnZXQ6J21haW4nLCBzd2FwOidvdXRlckhUTUwnfSk7XG4gICAgICAgICAgICAgICAgICAgICAgICAgICAgLy8gc2xlZXAoMzUwMCk7IC8vd2FpdCAxIHNlYyBhbmQgdGhlbiBodG14IHJlZGlyZWN0IGdldFxuICAgICAgICAgICAgICAgICAgICAgICAgICAgIC8vIGxvY2F0aW9uLnJlbG9hZCgpO1xuICAgICAgICAgICAgICAgICAgICAgICAgfVxuXG4gICAgICAgICAgICAgICAgICAgICAgICBjb25zb2xlLmxvZyhyZXNwb25zZSk7XG4gICAgICAgICAgICAgICAgICAgIH0pLmNhdGNoKGZ1bmN0aW9uIChlcnJvcikge1xuICAgICAgICAgICAgICAgICAgICAgICAgaXppVG9hc3QuZXJyb3Ioe1xuICAgICAgICAgICAgICAgICAgICAgICAgICAgIHRpdGxlOiBcIkVtYWlsIFNlbmRpbmcgSW5jb21wbGV0ZVwiLFxuICAgICAgICAgICAgICAgICAgICAgICAgICAgIGJhbGxvb246IHRydWUsXG4gICAgICAgICAgICAgICAgICAgICAgICAgICAgcG9zaXRpb246IFwidG9wUmlnaHRcIixcbiAgICAgICAgICAgICAgICAgICAgICAgICAgICBhbmltYXRlSW5zaWRlOiB0cnVlLFxuICAgICAgICAgICAgICAgICAgICAgICAgICAgIG1lc3NhZ2U6IGBTb21ldGhpbmcgd3JvbmcgaGFwcGVuZWQ6ICR7ZXJyb3J9YFxuICAgICAgICAgICAgICAgICAgICAgICAgfSk7XG4gICAgICAgICAgICAgICAgICAgIH0pO1xuICAgICAgICAgICAgICAgICAgICAvLyAuZmluYWxseShmdW5jdGlvbiAoKSB7XG4gICAgICAgICAgICAgICAgICAgIC8vICAgICBjb25zb2xlLmxvZyhcImZpbmFsbHlcIik7XG4gICAgICAgICAgICAgICAgICAgIC8vIH0pO1xuXG4gICAgICAgICAgICAgICAgdGhpcy5wcm9jZXNzaW5nID0gZmFsc2U7XG4gICAgICAgICAgICB9IGVsc2Uge1xuICAgICAgICAgICAgICAgIGl6aVRvYXN0LmVycm9yKHtcbiAgICAgICAgICAgICAgICAgICAgdGl0bGU6IFwiU2VuZGluZyBFbWFpbCBJbmNvbXBsZXRlXCIsXG4gICAgICAgICAgICAgICAgICAgIGJhbGxvb246IHRydWUsXG4gICAgICAgICAgICAgICAgICAgIHBvc2l0aW9uOiBcInRvcFJpZ2h0XCIsXG4gICAgICAgICAgICAgICAgICAgIGFuaW1hdGVJbnNpZGU6IHRydWUsXG4gICAgICAgICAgICAgICAgICAgIG1lc3NhZ2U6IGBGb3JtIGRhdGEgaXMgbm90IHZhbGlkLiBFbnN1cmUgeW91IGhhdmUgZmlsbGVkIGFsbCBmaWVsZHMgYWNjdXJhdGVseSEgJHtmb3JtRWxlbWVudC5yZXBvcnRWYWxpZGl0eSgpfWBcbiAgICAgICAgICAgICAgICB9KTtcbiAgICAgICAgICAgICAgICBzbGVlcCgyNTAwKTsgLy93YWl0IDIuNSBzZWMgYW5kIHRoZW4gaHRteCByZWRpcmVjdCBnZXRcbiAgICAgICAgICAgICAgICB0aGlzLnByb2Nlc3NpbmcgPSBmYWxzZTtcbiAgICAgICAgICAgICAgICBodG14LmFqYXgoJ0dFVCcsIHJlZGlyZWN0LCB7dGFyZ2V0OidtYWluJywgc3dhcDonb3V0ZXJIVE1MJ30pO1xuICAgICAgICAgICAgfVxuXG4gICAgICAgIH0sXG5cbiAgICAgICAgYXN5bmMgY2hlY2tWYWxpZGl0eSgpIHtcbiAgICAgICAgICAgIGNvbnN0IGZvcm1FbGVtZW50ID0gdGhpcy4kcmVmcy5jb250YWN0Rm9ybTtcbiAgICAgICAgICAgIGZvcm1FbGVtZW50LnF1ZXJ5U2VsZWN0b3JBbGwoJ1tuYW1lXScpLmZvckVhY2goZmllbGRFbGVtZW50ID0+IHtcbiAgICAgICAgICAgICAgICBmaWVsZEVsZW1lbnQuYWRkRXZlbnRMaXN0ZW5lcignY2hhbmdlJywgZXZlbnQgPT4ge1xuICAgICAgICAgICAgICAgICAgICBjb25zb2xlLmxvZyhldmVudCk7XG4gICAgICAgICAgICAgICAgICAgIHZhbGlkYXRlRmllbGQoZm9ybUVsZW1lbnQsIGZpZWxkRWxlbWVudCk7XG4gICAgICAgICAgICAgICAgfSk7XG4gICAgICAgICAgICB9KTtcbiAgICAgICAgfSxcblxuICAgICAgICBnZXRCdG5UZXh0KCkge1xuICAgICAgICAgICAgcmV0dXJuIHRoaXMucHJvY2Vzc2luZyA/ICdQcm9jZXNzaW5nLi4uJyA6ICdTdWJtaXQnO1xuICAgICAgICB9XG4gICAgfTtcbn1cbiIsImV4cG9ydCBkZWZhdWx0IGZ1bmN0aW9uIFN0aWNreU5hdigpIHtcbiAgICByZXR1cm4ge1xuICAgICAgICBzaG93TmF2OiB0cnVlLFxuICAgICAgICBuYXZUb3A6IGZhbHNlLFxuICAgICAgICBsYXN0U2Nyb2xsOiAwLFxuXG4gICAgICAgIGluaXRTdGF0ZSgpIHtcbiAgICAgICAgICAgIGNvbnN0IG1haW4gPSBkb2N1bWVudC5nZXRFbGVtZW50QnlJZCgnbWFpbicpO1xuICAgICAgICAgICAgY29uc3QgbmF2YmFyID0gZG9jdW1lbnQuZ2V0RWxlbWVudEJ5SWQoJ25hdmJhcicpO1xuXG4gICAgICAgICAgICAvLyBnZXQgdGhlIGhlaWdodCBvZiB0aGUgbmF2YmFyIGFuZCB0aGVuIGFkZCBpdCB0byB0aGUgdG9wIHBhZGRpbmcgb2YgdGhlIG1haW4gY29udGVudFxuICAgICAgICAgICAgY29uc3QgaGVhZGVyX2ggPSBuYXZiYXIub2Zmc2V0SGVpZ2h0ICsgMTA7XG5cbiAgICAgICAgICAgIG1haW4uY2xhc3NMaXN0LmFkZChgcHQtWyR7aGVhZGVyX2h9cHhdYCk7XG4gICAgICAgICAgICB0aGlzLm5hdlRvcCA9IHRydWU7XG4gICAgICAgICAgICB0aGlzLnNob3dOYXYgPSBmYWxzZTtcbiAgICAgICAgfSxcblxuICAgICAgICBzY3JvbGxOYXYoKSB7XG4gICAgICAgICAgICBsZXQgY3VycmVudFNjcm9sbCA9IHdpbmRvdy5wYWdlWU9mZnNldDtcbiAgICAgICAgICAgIGlmIChjdXJyZW50U2Nyb2xsIDw9IDApIHtcbiAgICAgICAgICAgICAgICB0aGlzLnNob3dOYXYgPSB0cnVlO1xuICAgICAgICAgICAgICAgIHRoaXMubmF2VG9wID0gdHJ1ZTtcbiAgICAgICAgICAgIH1cblxuICAgICAgICAgICAgaWYgKGN1cnJlbnRTY3JvbGwgPiB0aGlzLmxhc3RTY3JvbGwgJiYgdGhpcy5zaG93TmF2ID09PSBmYWxzZSkge1xuICAgICAgICAgICAgICAgIHRoaXMuc2hvd05hdiA9IHRydWU7XG4gICAgICAgICAgICAgICAgdGhpcy5uYXZUb3AgPSBmYWxzZTtcbiAgICAgICAgICAgIH0gZWxzZSBpZiAoY3VycmVudFNjcm9sbCA8IHRoaXMubGFzdFNjcm9sbCAmJiB0aGlzLnNob3dOYXYgPT09IHRydWUpIHtcbiAgICAgICAgICAgICAgICB0aGlzLnNob3dOYXYgPSBmYWxzZTtcbiAgICAgICAgICAgICAgICB0aGlzLm5hdlRvcCA9IHRydWU7XG4gICAgICAgICAgICB9XG4gICAgICAgICAgICB0aGlzLmxhc3RTY3JvbGwgPSBjdXJyZW50U2Nyb2xsO1xuICAgICAgICB9XG4gICAgfTtcbn1cbiIsImltcG9ydCBheGlvcyBmcm9tIFwiYXhpb3NcIjtcblxuYXhpb3MuZGVmYXVsdHMud2l0aENyZWRlbnRpYWxzID0gdHJ1ZTtcbmF4aW9zLmRlZmF1bHRzLnhzcmZDb29raWVOYW1lID0gJ2NzcmZ0b2tlbic7XG5heGlvcy5kZWZhdWx0cy54c3JmSGVhZGVyTmFtZSA9IFwiWC1DU1JGVE9LRU5cIjtcbi8vIGF4aW9zLmRlZmF1bHRzLmhlYWRlcnNbJ1gtQ1NSRlRva2VuJ10gPSBkb2N1bWVudC5oZWFkLnF1ZXJ5U2VsZWN0b3IoJ21ldGFbbmFtZT1cImNzcmYtdG9rZW5cIl0nKS5nZXRBdHRyaWJ1dGUoJ2NvbnRlbnQnKTtcbmF4aW9zLmRlZmF1bHRzLnRpbWVvdXQgPSAxNTAwMDtcblxuZXhwb3J0IGRlZmF1bHQgYXhpb3M7XG4iLCIvLyBleHRyYWN0ZWQgYnkgbWluaS1jc3MtZXh0cmFjdC1wbHVnaW5cbmV4cG9ydCB7fTsiLCIvKiAoaWdub3JlZCkgKi8iXSwibmFtZXMiOlsiaHRteCIsIkFscGluZSIsImV0aGVycyIsImF4aW9zIiwiU3RpY2t5TmF2IiwiU3dpcGVyIiwiZGV0ZWN0IiwiaXppVG9hc3QiLCJhbmltZSIsIlNjcm9sbE1hZ2ljIiwiQ29udGFjdEZvcm0iLCJBY2NvdW50Rm9ybSIsImxvdHRpZXdlYiIsIndpbmRvdyIsInNjcm9sbE1hZ2ljIiwiaXppdG9hc3QiLCJkYXRhIiwic3RhcnQiLCJzdyIsImhvbWUiLCJicm93c2VyIiwiQVBQTElDQVRJT05fU0VSVkVSX0tFWSIsIkNSRUFURV9XUF9ERVZJQ0UiLCJTRU5EX05PVElGSUNBVElPTiIsIldFQl9QVVNIX0NGRyIsInVybEJhc2U2NFRvVWludDhBcnJheSIsImJhc2U2NFN0cmluZyIsInBhZGRpbmciLCJyZXBlYXQiLCJsZW5ndGgiLCJiYXNlNjQiLCJyZXBsYWNlIiwicmF3RGF0YSIsImF0b2IiLCJvdXRwdXRBcnJheSIsIlVpbnQ4QXJyYXkiLCJpIiwiY2hhckNvZGVBdCIsInNhdmVTdWJzY3JpYmVPYmoiLCJzdWJzY3JpcHRpb24iLCJzdWJzY3JpcHRpb25Kc29uIiwidG9KU09OIiwiZW5kcG9pbnRQYXJ0cyIsImVuZHBvaW50Iiwic3BsaXQiLCJyZWdpc3RyYXRpb25JZCIsInByZWRhdGEiLCJzdGF0dXNfdHlwZSIsIm5hbWUiLCJ0b0xvd2VyQ2FzZSIsInAyNTZkaCIsImtleXMiLCJhdXRoIiwidXNlcl9hZ2VudCIsIm5hdmlnYXRvciIsImdldFVzZXJBZ2VudCIsInJlZ2lzdHJhdGlvbl9pZCIsImdyb3VwIiwiSlNPTiIsInN0cmluZ2lmeSIsInBvc3QiLCJoZWFkZXJzIiwidGhlbiIsInJlc3BvbnNlIiwicHJvY2VzcyIsImVudiIsIk5PREVfRU5WIiwiY29uc29sZSIsImxvZyIsInN1Y2Nlc3MiLCJ0aXRsZSIsImJhbGxvb24iLCJwb3NpdGlvbiIsImFuaW1hdGVJbnNpZGUiLCJtZXNzYWdlIiwic3RhdHVzVGV4dCIsImNhdGNoIiwiZXJyb3IiLCJzdWJzY3JpYmUiLCJyZWdpc3RyYXRpb24iLCJwdXNoTWFuYWdlciIsImdldFN1YnNjcmlwdGlvbiIsInNldHVwVHJpZ2dlckJ1dHRvbiIsIm9wdGlvbnMiLCJ1c2VyVmlzaWJsZU9ubHkiLCJhcHBsaWNhdGlvblNlcnZlcktleSIsImRvY3VtZW50IiwiZ2V0RWxlbWVudEJ5SWQiLCJ0cmlnZ2VyTm90aWZpY2F0aW9uQnV0dG9uIiwiY2xhc3NMaXN0IiwidG9nZ2xlIiwiYWRkRXZlbnRMaXN0ZW5lciIsInN1Ykpzb24iLCJoZWFkIiwiYm9keSIsImRldGFpbCIsInNlcnZpY2VXb3JrZXIiLCJyZWdpc3RlciIsInNjb3BlIiwicmVhZHkiLCJhY3RpdmUiLCJpbml0aWFsaXNlU3RhdGUiLCJlcnIiLCJyZWciLCJzaG93Tm90aWZpY2F0aW9uIiwiTm90aWZpY2F0aW9uIiwicGVybWlzc2lvbiIsIndhcm5pbmciLCJpbmZvIiwic3ViIiwiaW5zdGFsbEJ1dHRvbiIsImV2ZW50IiwiZGVmZXJyZWRQcm9tcHQiLCJwcm9tcHRFdmVudCIsInByb21wdCIsInVzZXJDaG9pY2UiLCJjaG9pY2UiLCJsb2dBbGwiLCJmb3JFYWNoIiwiZXZ0IiwiY291bnRlcnMiLCJxdWVyeVNlbGVjdG9yQWxsIiwiY2FyIiwiY29udHJvbGxlciIsIkNvbnRyb2xsZXIiLCJzdGFydENvdW50aW5nIiwiY291bnRlciIsInRhcmdldHMiLCJpbm5lckhUTUwiLCJnZXRBdHRyaWJ1dGUiLCJlYXNpbmciLCJyb3VuZCIsImR1cmF0aW9uIiwiYW5pbWF0ZUhvd3MiLCJ0cmFuc2xhdGVYIiwib3BhY2l0eSIsImRlbGF5Iiwic3RhZ2dlciIsIlNjZW5lIiwidHJpZ2dlckVsZW1lbnQiLCJ0cmlnZ2VySG9vayIsInJldmVyc2UiLCJvZmZzZXQiLCJvbiIsImFkZFRvIiwiY2FyRHJpdmUiLCJ2YWx1ZSIsImRpcmVjdGlvbiIsImxvb3AiLCJzbGVlcCIsIm1zIiwiUHJvbWlzZSIsInJlc29sdmUiLCJzZXRUaW1lb3V0IiwidmFsaWRhdGVGaWVsZCIsImZvcm1FbGVtZW50IiwiZmllbGRFbGVtZW50IiwiZm9ybURhdGEiLCJGb3JtRGF0YSIsImFwcGVuZCIsImFjdGlvbiIsImVycm9ycyIsImVycm9yc1dyYXBwZXJFbGVtZW50IiwicmVtb3ZlIiwiYWRkIiwiZXJyb3JzSHRtbCIsInByb2Nlc3NpbmciLCJzdWJtaXRGb3JtIiwiJHJlZnMiLCJmb3JtIiwiZGl2IiwicmVkaXJlY3QiLCJkYXRhc2V0IiwiY3NyZiIsImNoZWNrVmFsaWRpdHkiLCJzdGF0dXMiLCJhamF4IiwidGFyZ2V0Iiwic3dhcCIsInJlcG9ydFZhbGlkaXR5Iiwic3VibWl0RmlsZUZvcm0iLCJjb250YWN0Rm9ybSIsImdldEJ0blRleHQiLCJzaG93TmF2IiwibmF2VG9wIiwibGFzdFNjcm9sbCIsImluaXRTdGF0ZSIsIm1haW4iLCJuYXZiYXIiLCJoZWFkZXJfaCIsIm9mZnNldEhlaWdodCIsInNjcm9sbE5hdiIsImN1cnJlbnRTY3JvbGwiLCJwYWdlWU9mZnNldCIsImRlZmF1bHRzIiwid2l0aENyZWRlbnRpYWxzIiwieHNyZkNvb2tpZU5hbWUiLCJ4c3JmSGVhZGVyTmFtZSIsInRpbWVvdXQiXSwic291cmNlUm9vdCI6IiJ9