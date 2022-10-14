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
/* harmony import */ var ethers__WEBPACK_IMPORTED_MODULE_13__ = __webpack_require__(/*! ethers */ "./node_modules/ethers/lib.esm/ethers.js");
/* harmony import */ var _components_axiosFactory__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! ../components/axiosFactory */ "./src/components/axiosFactory.js");
/* harmony import */ var _components_StickyNav__WEBPACK_IMPORTED_MODULE_4__ = __webpack_require__(/*! ../components/StickyNav */ "./src/components/StickyNav.js");
/* harmony import */ var swiper__WEBPACK_IMPORTED_MODULE_5__ = __webpack_require__(/*! swiper */ "./node_modules/swiper/swiper.esm.js");
/* harmony import */ var detect_browser__WEBPACK_IMPORTED_MODULE_14__ = __webpack_require__(/*! detect-browser */ "./node_modules/detect-browser/es/index.js");
/* harmony import */ var izitoast_dist_css_iziToast_min_css__WEBPACK_IMPORTED_MODULE_6__ = __webpack_require__(/*! izitoast/dist/css/iziToast.min.css */ "./node_modules/izitoast/dist/css/iziToast.min.css");
/* harmony import */ var _lottiefiles_lottie_player__WEBPACK_IMPORTED_MODULE_7__ = __webpack_require__(/*! @lottiefiles/lottie-player */ "./node_modules/@lottiefiles/lottie-player/dist/lottie-player.esm.js");
/* harmony import */ var izitoast_dist_js_iziToast_min_js__WEBPACK_IMPORTED_MODULE_8__ = __webpack_require__(/*! izitoast/dist/js/iziToast.min.js */ "./node_modules/izitoast/dist/js/iziToast.min.js");
/* harmony import */ var izitoast_dist_js_iziToast_min_js__WEBPACK_IMPORTED_MODULE_8___default = /*#__PURE__*/__webpack_require__.n(izitoast_dist_js_iziToast_min_js__WEBPACK_IMPORTED_MODULE_8__);
/* harmony import */ var animejs_lib_anime_es_js__WEBPACK_IMPORTED_MODULE_9__ = __webpack_require__(/*! animejs/lib/anime.es.js */ "./node_modules/animejs/lib/anime.es.js");
/* harmony import */ var scrollmagic__WEBPACK_IMPORTED_MODULE_10__ = __webpack_require__(/*! scrollmagic */ "./node_modules/scrollmagic/scrollmagic/uncompressed/ScrollMagic.js");
/* harmony import */ var scrollmagic__WEBPACK_IMPORTED_MODULE_10___default = /*#__PURE__*/__webpack_require__.n(scrollmagic__WEBPACK_IMPORTED_MODULE_10__);
/* harmony import */ var _components_ContactForm__WEBPACK_IMPORTED_MODULE_11__ = __webpack_require__(/*! ../components/ContactForm */ "./src/components/ContactForm.js");
/* harmony import */ var lottie_web__WEBPACK_IMPORTED_MODULE_12__ = __webpack_require__(/*! lottie-web */ "./node_modules/lottie-web/build/player/lottie.js");
/* harmony import */ var lottie_web__WEBPACK_IMPORTED_MODULE_12___default = /*#__PURE__*/__webpack_require__.n(lottie_web__WEBPACK_IMPORTED_MODULE_12__);
// This is global imports for css and javascripts //
//----------------------------------------------------------














 // import { initializeApp } from "firebase/app";
// import { getAnalytics } from "firebase/analytics";
//----------------------------------------------------------
// Global Initializations for importedlibraries //
//----------------------------------------------------------
// initialize htmx

window.htmx = (htmx_org_dist_htmx__WEBPACK_IMPORTED_MODULE_1___default()); // initialize lottie web and lottie player

window.lottieweb = (lottie_web__WEBPACK_IMPORTED_MODULE_12___default()); // initialize animejs

window.anime = animejs_lib_anime_es_js__WEBPACK_IMPORTED_MODULE_9__["default"];
window.scrollMagic = (scrollmagic__WEBPACK_IMPORTED_MODULE_10___default()); // initialize ether js for crypto payment

window.ethers = ethers__WEBPACK_IMPORTED_MODULE_13__; // initialize axios async post|get request

window.axios = _components_axiosFactory__WEBPACK_IMPORTED_MODULE_3__["default"]; // initialize swiper.js

window.Swiper = swiper__WEBPACK_IMPORTED_MODULE_5__["default"]; // initiailize izitoast alerts

window.izitoast = (izitoast_dist_js_iziToast_min_js__WEBPACK_IMPORTED_MODULE_8___default()); // Alpine JS Scripts

window.Alpine = alpinejs__WEBPACK_IMPORTED_MODULE_2__["default"];
alpinejs__WEBPACK_IMPORTED_MODULE_2__["default"].data("StickyNav", _components_StickyNav__WEBPACK_IMPORTED_MODULE_4__["default"]);
alpinejs__WEBPACK_IMPORTED_MODULE_2__["default"].data("ContactForm", _components_ContactForm__WEBPACK_IMPORTED_MODULE_11__["default"]);
alpinejs__WEBPACK_IMPORTED_MODULE_2__["default"].start(); //----------------------------------------------------------
// set service worker link and scope start link
//----------------------------------------------------------

const sw = "/sw.js";
const home = "/"; // detect browser type

const browser = (0,detect_browser__WEBPACK_IMPORTED_MODULE_14__.detect)(); //----------------------------------------------------------
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
// if app is installed, thank the user for installing the app
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
              target: 'body',
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
          target: 'body',
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
//# sourceMappingURL=data:application/json;charset=utf-8;base64,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QUdqTCxNQUFNLENBQUNrTCxXQUEzQjs7TUFDQSxJQUFJRCxhQUFhLElBQUksQ0FBckIsRUFBd0I7UUFDcEIsS0FBS1QsT0FBTCxHQUFlLElBQWY7UUFDQSxLQUFLQyxNQUFMLEdBQWMsSUFBZDtNQUNIOztNQUVELElBQUlRLGFBQWEsR0FBRyxLQUFLUCxVQUFyQixJQUFtQyxLQUFLRixPQUFMLEtBQWlCLEtBQXhELEVBQStEO1FBQzNELEtBQUtBLE9BQUwsR0FBZSxJQUFmO1FBQ0EsS0FBS0MsTUFBTCxHQUFjLEtBQWQ7TUFDSCxDQUhELE1BR08sSUFBSVEsYUFBYSxHQUFHLEtBQUtQLFVBQXJCLElBQW1DLEtBQUtGLE9BQUwsS0FBaUIsSUFBeEQsRUFBOEQ7UUFDakUsS0FBS0EsT0FBTCxHQUFlLEtBQWY7UUFDQSxLQUFLQyxNQUFMLEdBQWMsSUFBZDtNQUNIOztNQUNELEtBQUtDLFVBQUwsR0FBa0JPLGFBQWxCO0lBQ0g7O0VBaENFLENBQVA7QUFrQ0g7Ozs7Ozs7Ozs7Ozs7Ozs7O0FDbkNEO0FBRUExTCx1RUFBQSxHQUFpQyxJQUFqQztBQUNBQSxzRUFBQSxHQUFnQyxXQUFoQztBQUNBQSxzRUFBQSxHQUFnQyxhQUFoQyxFQUNBOztBQUNBQSwrREFBQSxHQUF5QixLQUF6QjtBQUVBLGlFQUFlQSw4Q0FBZjs7Ozs7Ozs7Ozs7O0FDUkE7Ozs7Ozs7Ozs7O0FDQUEiLCJzb3VyY2VzIjpbIndlYnBhY2s6Ly9weXRob24td2VicGFjay1ib2lsZXJwbGF0ZS8uL3NyYy9hcHBsaWNhdGlvbi9hcHAuanMiLCJ3ZWJwYWNrOi8vcHl0aG9uLXdlYnBhY2stYm9pbGVycGxhdGUvLi9zcmMvY29tcG9uZW50cy9Db250YWN0Rm9ybS5qcyIsIndlYnBhY2s6Ly9weXRob24td2VicGFjay1ib2lsZXJwbGF0ZS8uL3NyYy9jb21wb25lbnRzL1N0aWNreU5hdi5qcyIsIndlYnBhY2s6Ly9weXRob24td2VicGFjay1ib2lsZXJwbGF0ZS8uL3NyYy9jb21wb25lbnRzL2F4aW9zRmFjdG9yeS5qcyIsIndlYnBhY2s6Ly9weXRob24td2VicGFjay1ib2lsZXJwbGF0ZS8uL3NyYy9zdHlsZXMvaW5kZXguc2Nzcz8wYjg4Iiwid2VicGFjazovL3B5dGhvbi13ZWJwYWNrLWJvaWxlcnBsYXRlL2lnbm9yZWR8L2hvbWUvZGFya2NvZHIvd3d3L2Rhcmtjb2RyL2Ryb3BzcmlkZS9mcm9udGVuZC9ub2RlX21vZHVsZXMvYm4uanMvbGlifGJ1ZmZlciJdLCJzb3VyY2VzQ29udGVudCI6WyIvLyBUaGlzIGlzIGdsb2JhbCBpbXBvcnRzIGZvciBjc3MgYW5kIGphdmFzY3JpcHRzIC8vXG4vLy0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS1cbmltcG9ydCBcIi4uL3N0eWxlcy9pbmRleC5zY3NzXCI7XG5pbXBvcnQgaHRteCBmcm9tIFwiaHRteC5vcmcvZGlzdC9odG14XCI7XG5pbXBvcnQgQWxwaW5lIGZyb20gXCJhbHBpbmVqc1wiO1xuaW1wb3J0IHsgZXRoZXJzIH0gZnJvbSBcImV0aGVyc1wiO1xuaW1wb3J0IGF4aW9zIGZyb20gXCIuLi9jb21wb25lbnRzL2F4aW9zRmFjdG9yeVwiO1xuaW1wb3J0IFN0aWNreU5hdiBmcm9tIFwiLi4vY29tcG9uZW50cy9TdGlja3lOYXZcIjtcbmltcG9ydCBTd2lwZXIgZnJvbSBcInN3aXBlclwiO1xuaW1wb3J0IHsgZGV0ZWN0IH0gZnJvbSBcImRldGVjdC1icm93c2VyXCI7XG5pbXBvcnQgXCJpeml0b2FzdC9kaXN0L2Nzcy9pemlUb2FzdC5taW4uY3NzXCI7XG5pbXBvcnQgXCJAbG90dGllZmlsZXMvbG90dGllLXBsYXllclwiO1xuaW1wb3J0IGl6aVRvYXN0IGZyb20gXCJpeml0b2FzdC9kaXN0L2pzL2l6aVRvYXN0Lm1pbi5qc1wiO1xuaW1wb3J0IGFuaW1lIGZyb20gXCJhbmltZWpzL2xpYi9hbmltZS5lcy5qc1wiO1xuaW1wb3J0IFNjcm9sbE1hZ2ljIGZyb20gXCJzY3JvbGxtYWdpY1wiO1xuaW1wb3J0IENvbnRhY3RGb3JtIGZyb20gXCIuLi9jb21wb25lbnRzL0NvbnRhY3RGb3JtXCI7XG5pbXBvcnQgbG90dGlld2ViIGZyb20gXCJsb3R0aWUtd2ViXCI7XG5cbi8vIGltcG9ydCB7IGluaXRpYWxpemVBcHAgfSBmcm9tIFwiZmlyZWJhc2UvYXBwXCI7XG4vLyBpbXBvcnQgeyBnZXRBbmFseXRpY3MgfSBmcm9tIFwiZmlyZWJhc2UvYW5hbHl0aWNzXCI7XG4vLy0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS1cblxuLy8gR2xvYmFsIEluaXRpYWxpemF0aW9ucyBmb3IgaW1wb3J0ZWRsaWJyYXJpZXMgLy9cbi8vLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLVxuLy8gaW5pdGlhbGl6ZSBodG14XG53aW5kb3cuaHRteCA9IGh0bXg7XG4vLyBpbml0aWFsaXplIGxvdHRpZSB3ZWIgYW5kIGxvdHRpZSBwbGF5ZXJcbndpbmRvdy5sb3R0aWV3ZWIgPSBsb3R0aWV3ZWI7XG4vLyBpbml0aWFsaXplIGFuaW1lanNcbndpbmRvdy5hbmltZSA9IGFuaW1lO1xud2luZG93LnNjcm9sbE1hZ2ljID0gU2Nyb2xsTWFnaWM7XG4vLyBpbml0aWFsaXplIGV0aGVyIGpzIGZvciBjcnlwdG8gcGF5bWVudFxud2luZG93LmV0aGVycyA9IGV0aGVycztcbi8vIGluaXRpYWxpemUgYXhpb3MgYXN5bmMgcG9zdHxnZXQgcmVxdWVzdFxud2luZG93LmF4aW9zID0gYXhpb3M7XG4vLyBpbml0aWFsaXplIHN3aXBlci5qc1xud2luZG93LlN3aXBlciA9IFN3aXBlcjtcbi8vIGluaXRpYWlsaXplIGl6aXRvYXN0IGFsZXJ0c1xud2luZG93Lml6aXRvYXN0ID0gaXppVG9hc3Q7XG4vLyBBbHBpbmUgSlMgU2NyaXB0c1xud2luZG93LkFscGluZSA9IEFscGluZTtcbkFscGluZS5kYXRhKFwiU3RpY2t5TmF2XCIsIFN0aWNreU5hdik7XG5BbHBpbmUuZGF0YShcIkNvbnRhY3RGb3JtXCIsIENvbnRhY3RGb3JtKTtcbkFscGluZS5zdGFydCgpO1xuLy8tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tXG5cbi8vIHNldCBzZXJ2aWNlIHdvcmtlciBsaW5rIGFuZCBzY29wZSBzdGFydCBsaW5rXG4vLy0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS1cbmNvbnN0IHN3ID0gXCIvc3cuanNcIjtcbmNvbnN0IGhvbWUgPSBcIi9cIjtcbi8vIGRldGVjdCBicm93c2VyIHR5cGVcbmNvbnN0IGJyb3dzZXIgPSBkZXRlY3QoKTtcbi8vLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLVxuXG4vLyBjb25zdCBmaXJlYmFzZUNvbmZpZyA9IHtcbi8vICAgYXBpS2V5OiBcIkFJemFTeUNDOWoycXdxaDFSZ0U3UVMyUTJMb1dCRVZ1X3AtU3dtc1wiLFxuLy8gICBhdXRoRG9tYWluOiBcImRyb3BzcmlkZS5maXJlYmFzZWFwcC5jb21cIixcbi8vICAgcHJvamVjdElkOiBcImRyb3BzcmlkZVwiLFxuLy8gICBzdG9yYWdlQnVja2V0OiBcImRyb3BzcmlkZS5hcHBzcG90LmNvbVwiLFxuLy8gICBtZXNzYWdpbmdTZW5kZXJJZDogXCI3MDgyMTgxMDQxNzBcIixcbi8vICAgYXBwSWQ6IFwiMTo3MDgyMTgxMDQxNzA6d2ViOmM4MmJkOTZjNjdkZjZkZjdhMzVkMTNcIixcbi8vICAgbWVhc3VyZW1lbnRJZDogXCJHLTFaRkVTR01WTjZcIixcbi8vIH07XG4vLyAvLyBJbml0aWFsaXplIEZpcmViYXNlXG5cbi8vIGNvbnN0IGFwcCA9IGluaXRpYWxpemVBcHAoZmlyZWJhc2VDb25maWcpO1xuLy8gY29uc3QgYW5hbHl0aWNzID0gZ2V0QW5hbHl0aWNzKGFwcCk7XG5cbi8vIGdldCBnbG9iYWwgdmFyaWFibGVzIGZyb20gdGhlIGJhc2UuaHRtbCBmaWxlIGZvclxuLy8gcHVzaCBub3RpZmljYXRpb24gYW5kIHB3YSBpbnN0YWxsIGJ1dHRvblxuLy8tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tXG5jb25zdCB7IEFQUExJQ0FUSU9OX1NFUlZFUl9LRVksIENSRUFURV9XUF9ERVZJQ0UsIFNFTkRfTk9USUZJQ0FUSU9OIH0gPVxuICB3aW5kb3cuV0VCX1BVU0hfQ0ZHO1xuLy8tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tXG5cbi8vIGdlbmVyYXRlIGtleSBmb3IgcHVzaCBub3RpZmljYXRpb25zXG4vLy0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS1cbmZ1bmN0aW9uIHVybEJhc2U2NFRvVWludDhBcnJheShiYXNlNjRTdHJpbmcpIHtcbiAgLy8gaHR0cHM6Ly9naXN0LmdpdGh1Yi5jb20vS2xlcml0aC84MGFiZDc0MmQ3MjZkZDU4N2Y0YmQ1ZDZhMGFiMjZiNiNmaWxlLXVybGJhc2U2NHRvdWludDhhcnJheS1qc1xuICB2YXIgcGFkZGluZyA9IFwiPVwiLnJlcGVhdCgoNCAtIChiYXNlNjRTdHJpbmcubGVuZ3RoICUgNCkpICUgNCk7XG4gIHZhciBiYXNlNjQgPSAoYmFzZTY0U3RyaW5nICsgcGFkZGluZykucmVwbGFjZSgvXFwtL2csIFwiK1wiKS5yZXBsYWNlKC9fL2csIFwiL1wiKTtcblxuICB2YXIgcmF3RGF0YSA9IHdpbmRvdy5hdG9iKGJhc2U2NCk7XG4gIHZhciBvdXRwdXRBcnJheSA9IG5ldyBVaW50OEFycmF5KHJhd0RhdGEubGVuZ3RoKTtcblxuICBmb3IgKHZhciBpID0gMDsgaSA8IHJhd0RhdGEubGVuZ3RoOyArK2kpIHtcbiAgICBvdXRwdXRBcnJheVtpXSA9IHJhd0RhdGEuY2hhckNvZGVBdChpKTtcbiAgfVxuICByZXR1cm4gb3V0cHV0QXJyYXk7XG5cbiAgLy8gY29uc3Qgb3V0cHV0RGF0YSA9IG91dHB1dEFycmF5Lm1hcCgob3V0cHV0LCBpbmRleCkgPT5cbiAgLy8gICByYXdEYXRhLmNoYXJDb2RlQXQoaW5kZXgpXG4gIC8vICk7XG4gIC8vIHJldHVybiBvdXRwdXREYXRhO1xufVxuLy8tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tXG5cbi8vIHRoaXMgaXMgdG8gc3Vic2NyaWJlIHRvIHB1c2ggbm90aWZpY2F0aW9uIGZyb20gdGhlIGJyb3dzZXIgdG8gdGhlIHNlcnZlclxuLy8tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tXG5mdW5jdGlvbiBzYXZlU3Vic2NyaWJlT2JqKHN1YnNjcmlwdGlvbikge1xuICAvLyBzYXZlIHN1YnNjcmlwdGlvbiB0byB0aGUgc2VydmVyXG4gIGNvbnN0IHN1YnNjcmlwdGlvbkpzb24gPSBzdWJzY3JpcHRpb24udG9KU09OKCk7XG4gIGNvbnN0IGVuZHBvaW50UGFydHMgPSBzdWJzY3JpcHRpb25Kc29uLmVuZHBvaW50LnNwbGl0KFwiL1wiKTtcbiAgY29uc3QgcmVnaXN0cmF0aW9uSWQgPSBlbmRwb2ludFBhcnRzW2VuZHBvaW50UGFydHMubGVuZ3RoIC0gMV07XG5cbiAgY29uc3QgcHJlZGF0YSA9IHtcbiAgICBzdGF0dXNfdHlwZTogXCJzdWJzY3JpYmVcIixcbiAgICBzdWJzY3JpcHRpb246IHN1YnNjcmlwdGlvbkpzb24sXG4gICAgYnJvd3NlcjogYnJvd3Nlci5uYW1lLnRvTG93ZXJDYXNlKCksXG4gICAgcDI1NmRoOiBzdWJzY3JpcHRpb25Kc29uLmtleXMucDI1NmRoLFxuICAgIGF1dGg6IHN1YnNjcmlwdGlvbkpzb24ua2V5cy5hdXRoLFxuICAgIHVzZXJfYWdlbnQ6IG5hdmlnYXRvci5nZXRVc2VyQWdlbnQsXG4gICAgcmVnaXN0cmF0aW9uX2lkOiByZWdpc3RyYXRpb25JZCxcbiAgICBncm91cDogXCJ1c2Vyc1wiLFxuICB9O1xuXG4gIGNvbnN0IGRhdGEgPSBKU09OLnN0cmluZ2lmeShwcmVkYXRhKTtcblxuICBheGlvc1xuICAgIC5wb3N0KENSRUFURV9XUF9ERVZJQ0UsIGRhdGEsIHtcbiAgICAgIGhlYWRlcnM6IHtcbiAgICAgICAgXCJDb250ZW50LVR5cGVcIjogXCJhcHBsaWNhdGlvbi9qc29uXCIsXG4gICAgICB9LFxuICAgIH0pXG4gICAgLnRoZW4oZnVuY3Rpb24gKHJlc3BvbnNlKSB7XG4gICAgICBpZiAocHJvY2Vzcy5lbnYuTk9ERV9FTlYgPT09IFwiZGV2ZWxvcG1lbnRcIikge1xuICAgICAgICBjb25zb2xlLmxvZyhyZXNwb25zZSk7XG4gICAgICAgIGl6aVRvYXN0LnN1Y2Nlc3Moe1xuICAgICAgICAgIHRpdGxlOiBcIltQVVNIIE5PVElGSUNBVElPTiBTRVJWRVJdXCIsXG4gICAgICAgICAgYmFsbG9vbjogdHJ1ZSxcbiAgICAgICAgICBwb3NpdGlvbjogXCJ0b3BSaWdodFwiLFxuICAgICAgICAgIGFuaW1hdGVJbnNpZGU6IHRydWUsXG4gICAgICAgICAgbWVzc2FnZTogYE5vdGlmaWNhdGlvbiBTdWJzY3JpcHRpb24gJHtyZXNwb25zZS5zdGF0dXNUZXh0fWAsXG4gICAgICAgIH0pO1xuICAgICAgfVxuICAgIH0pXG4gICAgLmNhdGNoKGZ1bmN0aW9uIChlcnJvcikge1xuICAgICAgaWYgKHByb2Nlc3MuZW52Lk5PREVfRU5WID09PSBcImRldmVsb3BtZW50XCIpIHtcbiAgICAgICAgY29uc29sZS5sb2coZXJyb3IpO1xuICAgICAgICBpemlUb2FzdC5lcnJvcih7XG4gICAgICAgICAgdGl0bGU6IFwiW1BVU0ggTk9USUZJQ0FUSU9OIFNFUlZFUl1cIixcbiAgICAgICAgICBiYWxsb29uOiB0cnVlLFxuICAgICAgICAgIHBvc2l0aW9uOiBcInRvcFJpZ2h0XCIsXG4gICAgICAgICAgYW5pbWF0ZUluc2lkZTogdHJ1ZSxcbiAgICAgICAgICBtZXNzYWdlOiBgTm90aWZpY2F0aW9uIFN1YnNjcmlwdGlvbiAke2Vycm9yLm1lc3NhZ2V9YCxcbiAgICAgICAgfSk7XG4gICAgICB9XG4gICAgfSk7XG59XG4vLy0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS1cblxuLy8gdGhpcyBmdW5jdGlvbiBpcyB0byBzZW5kIHN1YnNjcmlwdGlvbiBub3RpZmljYXRpb24gdG8gdGhlIHNlcnZlclxuLy8tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tXG5mdW5jdGlvbiBzdWJzY3JpYmUocmVnaXN0cmF0aW9uKSB7XG4gIHJlZ2lzdHJhdGlvbi5wdXNoTWFuYWdlci5nZXRTdWJzY3JpcHRpb24oKS50aGVuKGZ1bmN0aW9uIChzdWJzY3JpcHRpb24pIHtcbiAgICBpZiAoc3Vic2NyaXB0aW9uKSB7XG4gICAgICBjb25zb2xlLmxvZyhcInN1YnNjcmlwdGlvbiBleGlzdHNcIik7XG4gICAgICBzYXZlU3Vic2NyaWJlT2JqKHN1YnNjcmlwdGlvbik7XG4gICAgICBzZXR1cFRyaWdnZXJCdXR0b24oc3Vic2NyaXB0aW9uKTtcbiAgICAgIHJldHVybjtcbiAgICB9XG4gIH0pO1xuXG4gIGNvbnN0IG9wdGlvbnMgPSB7XG4gICAgdXNlclZpc2libGVPbmx5OiB0cnVlLCAvLyByZXF1aXJlZCBieSBjaHJvbWVcbiAgICBhcHBsaWNhdGlvblNlcnZlcktleTogdXJsQmFzZTY0VG9VaW50OEFycmF5KEFQUExJQ0FUSU9OX1NFUlZFUl9LRVkpLFxuICB9O1xuXG4gIHJlZ2lzdHJhdGlvbi5wdXNoTWFuYWdlci5zdWJzY3JpYmUob3B0aW9ucykudGhlbihcbiAgICAvLyByZXF1ZXN0aW5nIHRvIHN1YnNjcmliZSBmcm9tIHRoZSBzZXJ2ZXJcbiAgICBmdW5jdGlvbiAoc3Vic2NyaXB0aW9uKSB7XG4gICAgICBpZiAocHJvY2Vzcy5lbnYuTk9ERV9FTlYgPT09IFwiZGV2ZWxvcG1lbnRcIikge1xuICAgICAgICBjb25zb2xlLmxvZyhgc3Vic2NyaXB0aW9uOiBgLCBzdWJzY3JpcHRpb24pO1xuICAgICAgICBjb25zb2xlLmxvZyhzdWJzY3JpcHRpb24uZW5kcG9pbnQpO1xuICAgICAgfVxuXG4gICAgICAvLyBzdWJzY3JpcHRpb24gaXMgbm93IHNhdmVkIHRvIHRoZSBzZXJ2ZXJcbiAgICAgIHNhdmVTdWJzY3JpYmVPYmooc3Vic2NyaXB0aW9uKTtcblxuICAgICAgLy8gaWYgc3Vic2NyaXB0aW9uIGlzIHN1Y2Nlc3NmdWxseSBzYXZlZCB0byB0aGUgc2VydmVyXG4gICAgICAvLyB0aGVuIGVuYWJsZSB0aGUgdGVzdCBub3RpZmljYXRpb24gcHVzaCBidXR0b24gdG8gYmUgdmlzaWJsZVxuICAgICAgc2V0dXBUcmlnZ2VyQnV0dG9uKHN1YnNjcmlwdGlvbik7XG5cbiAgICAgIGl6aVRvYXN0LnN1Y2Nlc3Moe1xuICAgICAgICB0aXRsZTogXCJbUFVTSCBOT1RJRklDQVRJT04gU1VCU0NSSVBUSU9OXVwiLFxuICAgICAgICBiYWxsb29uOiB0cnVlLFxuICAgICAgICBwb3NpdGlvbjogXCJ0b3BSaWdodFwiLFxuICAgICAgICBhbmltYXRlSW5zaWRlOiB0cnVlLFxuICAgICAgICBtZXNzYWdlOiBgU3Vic2NyaXB0aW9uIFNlbnQgU3VjY2Vzc2Z1bGx5YCxcbiAgICAgIH0pO1xuICAgIH0sXG5cbiAgICAvLyBpZiB0aGVyZSBpcyBhbiBlcnJvciBmaWd1cmUgdGhlIGVycm9yIGFuZCB0aHJvdyBhbiBhcHByb3ByYWl0ZSBlcnJvciBtZXNzYWdlIHRvXG4gICAgLy8gdGhlIHVzZXIgc28gaGUga25vd3MgZXhhY3RseSB3aGF0IGlzIHdyb25nIGFuZCBjYW4gbW92ZSBmb3J3YXJkIG9yIGFkanVzdCBmb3IgYVxuICAgIC8vIGRldmljZS5cbiAgICBmdW5jdGlvbiAoZXJyb3IpIHtcbiAgICAgIGlmIChwcm9jZXNzLmVudi5OT0RFX0VOViA9PT0gXCJkZXZlbG9wbWVudFwiKSB7XG4gICAgICAgIGNvbnNvbGUubG9nKGVycm9yKTtcbiAgICAgIH1cblxuICAgICAgaXppVG9hc3QuZXJyb3Ioe1xuICAgICAgICB0aXRsZTogXCJbUFVTSCBOT1RJRklDQVRJT04gU1VCU0NSSVBUSU9OXVwiLFxuICAgICAgICBiYWxsb29uOiB0cnVlLFxuICAgICAgICBwb3NpdGlvbjogXCJ0b3BSaWdodFwiLFxuICAgICAgICBhbmltYXRlSW5zaWRlOiB0cnVlLFxuICAgICAgICBtZXNzYWdlOiBgJHtlcnJvcn1gLFxuICAgICAgfSk7XG4gICAgfVxuICApO1xufVxuLy8tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tXG5cbi8vIFRoZSBmdW5jdGlvbiB0byB0cmlnZ2VyIHRoZSBwdXNoIG5vdGlmaWNhdGlvbiBmcm9tIHRoZSBicm93c2VyXG4vLy0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS1cbmZ1bmN0aW9uIHNldHVwVHJpZ2dlckJ1dHRvbihzdWJzY3JpcHRpb24pIHtcbiAgY29uc3QgdHJpZ2dlck5vdGlmaWNhdGlvbkJ1dHRvbiA9IGRvY3VtZW50LmdldEVsZW1lbnRCeUlkKFxuICAgIFwidHJpZ2dlck5vdGlmaWNhdGlvbkJ1dHRvblwiXG4gICk7XG4gIHRyaWdnZXJOb3RpZmljYXRpb25CdXR0b24uY2xhc3NMaXN0LnRvZ2dsZShcImhpZGRlblwiLCBmYWxzZSk7XG5cbiAgdHJpZ2dlck5vdGlmaWNhdGlvbkJ1dHRvbi5hZGRFdmVudExpc3RlbmVyKFwiY2xpY2tcIiwgKCkgPT4ge1xuICAgIGNvbnN0IHN1Ykpzb24gPSBzdWJzY3JpcHRpb24udG9KU09OKCk7XG4gICAgY29uc3QgZW5kcG9pbnRQYXJ0cyA9IHN1Ykpzb24uZW5kcG9pbnQuc3BsaXQoXCIvXCIpO1xuICAgIGNvbnN0IHJlZ2lzdHJhdGlvbklkID0gZW5kcG9pbnRQYXJ0c1tlbmRwb2ludFBhcnRzLmxlbmd0aCAtIDFdO1xuICAgIGNvbnN0IHByZWRhdGEgPSB7XG4gICAgICByZWdpc3RyYXRpb25faWQ6IHJlZ2lzdHJhdGlvbklkLFxuICAgICAgYXV0aDogc3ViSnNvbi5rZXlzLmF1dGgsXG4gICAgICBncm91cDogXCJ1c2Vyc1wiLFxuICAgICAgaGVhZDogXCJUcmlnZ2VyIFRlc3QgTm90aWZpY2F0aW9uXCIsXG4gICAgICBib2R5OiBcIlRoaXMgaXMgYSB0ZXN0IG5vdGlmaWNhdGlvblwiLFxuICAgIH07XG5cbiAgICBjb25zdCBkYXRhID0gSlNPTi5zdHJpbmdpZnkocHJlZGF0YSk7XG5cbiAgICBheGlvc1xuICAgICAgLnBvc3QoU0VORF9OT1RJRklDQVRJT04sIGRhdGEsIHtcbiAgICAgICAgaGVhZGVyczoge1xuICAgICAgICAgIFwiQ29udGVudC1UeXBlXCI6IFwiYXBwbGljYXRpb24vanNvblwiLFxuICAgICAgICB9LFxuICAgICAgfSlcbiAgICAgIC50aGVuKGZ1bmN0aW9uIChyZXNwb25zZSkge1xuICAgICAgICBpemlUb2FzdC5zdWNjZXNzKHtcbiAgICAgICAgICB0aXRsZTogXCJbUFVTSCBOT1RJRklDQVRJT04gVEVTVCBTVUNDRVNTRlVMXVwiLFxuICAgICAgICAgIGJhbGxvb246IHRydWUsXG4gICAgICAgICAgcG9zaXRpb246IFwidG9wUmlnaHRcIixcbiAgICAgICAgICBhbmltYXRlSW5zaWRlOiB0cnVlLFxuICAgICAgICAgIG1lc3NhZ2U6IHJlc3BvbnNlLmRhdGEubWVzc2FnZSxcbiAgICAgICAgfSk7XG4gICAgICB9KVxuICAgICAgLmNhdGNoKGZ1bmN0aW9uIChlcnJvcikge1xuICAgICAgICBpemlUb2FzdC5lcnJvcih7XG4gICAgICAgICAgdGl0bGU6IFwiW1BVU0ggTk9USUZJQ0FUSU9OIFRFU1QgRVJST1JdXCIsXG4gICAgICAgICAgYmFsbG9vbjogdHJ1ZSxcbiAgICAgICAgICBwb3NpdGlvbjogXCJ0b3BSaWdodFwiLFxuICAgICAgICAgIGFuaW1hdGVJbnNpZGU6IHRydWUsXG4gICAgICAgICAgbWVzc2FnZTogZXJyb3IucmVzcG9uc2UuZGF0YS5kZXRhaWwsXG4gICAgICAgIH0pO1xuICAgICAgfSk7XG4gIH0pO1xufVxuLy8tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tXG5cbi8vIGVuYWJsZSBzZXJ2aWNlIHdvcmtlciwgdGhlbiB3aGVuIHNlcnZpY2Ugd29ya2VyIGlzIGVuYWJsZWQgcmVxdWVzdFxuLy8gcGVybWlzc2lvbiBmb3IgcHVzaCBub3RpZmljYXRpb24gYW5kIGxvY2F0aW9uIHNlcnZpY2VzIGZyb20gdGhlIGJyb3dzZXJcbi8vLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLVxuaWYgKFwic2VydmljZVdvcmtlclwiIGluIG5hdmlnYXRvcikge1xuICB3aW5kb3cuYWRkRXZlbnRMaXN0ZW5lcihcImxvYWRcIiwgKCkgPT4ge1xuICAgIG5hdmlnYXRvci5zZXJ2aWNlV29ya2VyXG4gICAgICAucmVnaXN0ZXIoc3csIHsgc2NvcGU6IGhvbWUgfSlcbiAgICAgIC50aGVuKChyZWdpc3RyYXRpb24pID0+IHtcbiAgICAgICAgaWYgKHByb2Nlc3MuZW52Lk5PREVfRU5WID09PSBcImRldmVsb3BtZW50XCIpIHtcbiAgICAgICAgICBjb25zb2xlLmxvZyhcIlNlcnZpY2Ugd29ya2VyIHJlZ2lzdGVyYXRpb24gc3VjY2VlZGVkOiBcIiwgcmVnaXN0cmF0aW9uKTtcbiAgICAgICAgfVxuXG4gICAgICAgIG5hdmlnYXRvci5zZXJ2aWNlV29ya2VyLnJlYWR5LnRoZW4oZnVuY3Rpb24gKHJlZ2lzdHJhdGlvbikge1xuICAgICAgICAgIGlmIChwcm9jZXNzLmVudi5OT0RFX0VOViA9PT0gXCJkZXZlbG9wbWVudFwiKSB7XG4gICAgICAgICAgICBjb25zb2xlLmxvZyhcIlNlcnZpY2Ugd29ya2VyIGlzIGFjdGl2ZTogXCIsIHJlZ2lzdHJhdGlvbi5hY3RpdmUpO1xuICAgICAgICAgIH1cblxuICAgICAgICAgIGluaXRpYWxpc2VTdGF0ZShyZWdpc3RyYXRpb24pO1xuICAgICAgICB9KTtcbiAgICAgIH0pXG4gICAgICAuY2F0Y2goKGVycikgPT4ge1xuICAgICAgICBpemlUb2FzdC5lcnJvcih7XG4gICAgICAgICAgdGl0bGU6IFwiW1NFUlZJQ0UgV09SS0VSXVwiLFxuICAgICAgICAgIGJhbGxvb246IHRydWUsXG4gICAgICAgICAgcG9zaXRpb246IFwidG9wUmlnaHRcIixcbiAgICAgICAgICBhbmltYXRlSW5zaWRlOiB0cnVlLFxuICAgICAgICAgIG1lc3NhZ2U6IFwiU2VydmljZSBXb3JrZXIgRmFpbGVkIHRvIFJlZ2lzdGVyXCIsXG4gICAgICAgIH0pO1xuXG4gICAgICAgIGlmIChwcm9jZXNzLmVudi5OT0RFX0VOViA9PT0gXCJkZXZlbG9wbWVudFwiKSB7XG4gICAgICAgICAgY29uc29sZS5sb2coZXJyKTtcbiAgICAgICAgfVxuICAgICAgfSk7XG4gIH0pO1xufVxuXG5jb25zdCBpbml0aWFsaXNlU3RhdGUgPSAocmVnKSA9PiB7XG4gIGlmICghcmVnLnNob3dOb3RpZmljYXRpb24pIHtcbiAgICBpemlUb2FzdC5lcnJvcih7XG4gICAgICB0aXRsZTogXCJbUFVTSCBVTlNVUFBPUlRFRF1cIixcbiAgICAgIGJhbGxvb246IHRydWUsXG4gICAgICBwb3NpdGlvbjogXCJ0b3BSaWdodFwiLFxuICAgICAgYW5pbWF0ZUluc2lkZTogdHJ1ZSxcbiAgICAgIG1lc3NhZ2U6IFwiU2hvd2luZyA8c3Ryb25nPlBVU0ggTk9USUZJQ0FUSU9OUzwvc3Ryb25nPiBpcyB1bnN1cHBvcnRlZFwiLFxuICAgIH0pO1xuICAgIHJldHVybjtcbiAgfVxuXG4gIGlmIChOb3RpZmljYXRpb24ucGVybWlzc2lvbiA9PT0gXCJkZW5pZWRcIikge1xuICAgIGl6aVRvYXN0Lndhcm5pbmcoe1xuICAgICAgdGl0bGU6IFwiW1BVU0ggREVOSUVEXVwiLFxuICAgICAgYmFsbG9vbjogdHJ1ZSxcbiAgICAgIHBvc2l0aW9uOiBcInRvcFJpZ2h0XCIsXG4gICAgICBhbmltYXRlSW5zaWRlOiB0cnVlLFxuICAgICAgbWVzc2FnZTpcbiAgICAgICAgXCJZb3UgcHJldmVudGVkIHVzIGZyb20gc2h3b2luZyBub3RpZmljYXRpb25zLiBNYW51YWxseSBjaGVjayBpZiB5b3UgaGF2ZSBwcmV2ZW50ZWQgcHVzaCBub3RpZmNhdGlvbiBmcm9tIHVzLlwiLFxuICAgIH0pO1xuICAgIHJldHVybjtcbiAgfVxuXG4gIGlmICghKFwiUHVzaE1hbmFnZXJcIiBpbiB3aW5kb3cpKSB7XG4gICAgaXppVG9hc3QuaW5mbyh7XG4gICAgICB0aXRsZTogXCJbUFVTSCBCUk9XU0VSIFVOQVZBSUxCQUxFXVwiLFxuICAgICAgYmFsbG9vbjogdHJ1ZSxcbiAgICAgIHBvc2l0aW9uOiBcInRvcFJpZ2h0XCIsXG4gICAgICBhbmltYXRlSW5zaWRlOiB0cnVlLFxuICAgICAgbWVzc2FnZTogXCJQdXNoIG5vdGlmaWNhdGlvbiBpcyBub3QgYWxsb3dlZCBpbiB5b3VyIGJyb3dzZXIuXCIsXG4gICAgfSk7XG4gICAgcmV0dXJuO1xuICB9XG5cbiAgcmVnLnB1c2hNYW5hZ2VyLmdldFN1YnNjcmlwdGlvbigpLnRoZW4oKHN1YikgPT4ge1xuICAgIGlmICghc3ViKSB7XG4gICAgICBzdWJzY3JpYmUocmVnKTtcbiAgICB9IGVsc2Uge1xuICAgICAgc2V0dXBUcmlnZ2VyQnV0dG9uKHN1Yik7XG4gICAgICBpemlUb2FzdC5pbmZvKHtcbiAgICAgICAgdGl0bGU6IFwiW1NFUlZJQ0UgV09SS0VSXVwiLFxuICAgICAgICBiYWxsb29uOiB0cnVlLFxuICAgICAgICBwb3NpdGlvbjogXCJ0b3BSaWdodFwiLFxuICAgICAgICBhbmltYXRlSW5zaWRlOiB0cnVlLFxuICAgICAgICBtZXNzYWdlOiBcIlB1c2ggbm90aWZpY2F0aW9uIGhhcyBhbHJlYWR5IGJlZW4gc3Vic2NyaWJlZCB0b1wiLFxuICAgICAgfSk7XG4gICAgfVxuICB9KTtcbn07XG5cbi8vLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLVxuXG4vLyAtLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLVxuLy8gSU5TVEFMTCBCVVRUT04gRk9SIFBST0dSRVNTSVZFIFdFQiBBUFBMSUNBVElPTlxuLy8gLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tXG5jb25zdCBpbnN0YWxsQnV0dG9uID0gZG9jdW1lbnQuZ2V0RWxlbWVudEJ5SWQoXCJpbnN0YWxsQnV0dG9uXCIpO1xuLy8gd2hlbiBwYWdlIGxvYWRzIGZvciB0aGUgZmlyc3QgdGltZSwgaW5zdGFsbCBidXR0b24gd2lsbCBiZSB2aXNpYmxlXG4vLyBpZiB0aGUgdXNlciBoYXMgbm90IGluc3RhbGxlZCB0aGUgYXBwIG9yIFBXQS5cbndpbmRvdy5hZGRFdmVudExpc3RlbmVyKFwiYmVmb3JlaW5zdGFsbHByb21wdFwiLCAoZXZlbnQpID0+IHtcbiAgaWYgKHByb2Nlc3MuZW52Lk5PREVfRU5WID09PSBcImRldmVsb3BtZW50XCIpIHtcbiAgICBjb25zb2xlLmxvZyhcIvCfkY1bUFdBXVwiLCBcImJlZm9yZWluc3RhbGxwcm9tcHRcIiwgZXZlbnQpO1xuICB9XG4gIC8vIFN0YXNoIHRoZSBldmVudCBzbyBpdCBjYW4gYmUgdHJpZ2dlcmVkIGxhdGVyLlxuICB3aW5kb3cuZGVmZXJyZWRQcm9tcHQgPSBldmVudDtcbiAgLy8gUmVtb3ZlIHRoZSAnaGlkZGVuJyBjbGFzcyBmcm9tIHRoZSBpbnN0YWxsIGJ1dHRvbiBjb250YWluZXJcbiAgLy8gaWYgdGhlIFBXQSBoYXMgYmVlbiBpbnN0YWxsZWQsIGhpZGUgdGhlIGluc3RhbGwgYnV0dG9uIG9yIGlmIGl0IGhhcyBub3RcbiAgLy8gdGhlbiBhbGxvdyBmb3IgY2xpY2tcbiAgaW5zdGFsbEJ1dHRvbi5jbGFzc0xpc3QudG9nZ2xlKFwiaGlkZGVuXCIsIGZhbHNlKTtcbn0pO1xuXG5pbnN0YWxsQnV0dG9uLmFkZEV2ZW50TGlzdGVuZXIoXCJjbGlja1wiLCAoKSA9PiB7XG4gIGlmIChwcm9jZXNzLmVudi5OT0RFX0VOViA9PT0gXCJkZXZlbG9wbWVudFwiKSB7XG4gICAgY29uc29sZS5sb2coXCLwn5GNW1BXQV0gSW5zdGFsbCBCdXR0b24gQ2xpY2tlZFwiKTtcbiAgfVxuXG4gIGNvbnN0IHByb21wdEV2ZW50ID0gd2luZG93LmRlZmVycmVkUHJvbXB0O1xuICBpZiAoIXByb21wdEV2ZW50KSB7XG4gICAgLy8gVGhlIGRlZmVycmVkIHByb21wdCBpc24ndCBhdmFpbGFibGUuIHNvIHJldHVybiBub3RoaW5nXG4gICAgcmV0dXJuO1xuICB9XG4gIHByb21wdEV2ZW50LnByb21wdCgpO1xuICBwcm9tcHRFdmVudC51c2VyQ2hvaWNlLnRoZW4oKGNob2ljZSkgPT4ge1xuICAgIGlmIChwcm9jZXNzLmVudi5OT0RFX0VOViA9PT0gXCJkZXZlbG9wbWVudFwiKSB7XG4gICAgICBjb25zb2xlLmxvZyhcIvCfkY1bUFdBXSBVc2VyIENob2ljZTogXCIsIGNob2ljZSk7XG4gICAgfVxuICAgIC8vIGl6aVRvYXN0LnN1Y2Nlc3Moe1xuICAgIC8vICAgdGl0bGU6IGBbUFdBOiAke2Nob2ljZX1dYCxcbiAgICAvLyAgIG1lc3NhZ2U6ICfwn5GNIFlvdSBoYXZlIHN1Y2Nlc3NmdWxseSBpbnN0YWxsZWQgdGhlIHJlYWR2aWxsZSBhcHAnLFxuICAgIC8vIH0pO1xuICAgIC8vIFJlc2V0IHRoZSBkZWZlcnJlZCBwcm9tcHQgdmFyaWFibGUsIHNpbmNlXG4gICAgLy8gcHJvbXB0KCkgY2FuIG9ubHkgYmUgY2FsbGVkIG9uY2UuXG4gICAgd2luZG93LmRlZmVycmVkUHJvbXB0ID0gbnVsbDtcbiAgICAvLyBIaWRlIHRoZSBpbnN0YWxsIGJ1dHRvbiBvbmNlIHRoZSBQV0EgaGFzIGJlZW4gaW5zdGFsbGVkXG4gICAgaW5zdGFsbEJ1dHRvbi5jbGFzc0xpc3QudG9nZ2xlKFwiaGlkZGVuXCIsIHRydWUpO1xuICB9KTtcbn0pO1xuLy8tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tXG5cbi8vIGlmIGFwcCBpcyBpbnN0YWxsZWQsIHRoYW5rIHRoZSB1c2VyIGZvciBpbnN0YWxsaW5nIHRoZSBhcHBcbi8vLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLVxud2luZG93LmFkZEV2ZW50TGlzdGVuZXIoXCJhcHBpbnN0YWxsZWRcIiwgKGV2ZW50KSA9PiB7XG4gIGlmIChwcm9jZXNzLmVudi5OT0RFX0VOViA9PT0gXCJkZXZlbG9wbWVudFwiKSB7XG4gICAgY29uc29sZS5sb2coXCLwn5GNW1BXQV0gSW5zdGFsbGVkIFN0YXRlOiBcIiwgZXZlbnQpO1xuICB9XG5cbiAgaXppVG9hc3QuaW5mbyh7XG4gICAgdGl0bGU6IGBbU0VSVklDRSBXT1JLRVJdYCxcbiAgICBiYWxsb29uOiB0cnVlLFxuICAgIHBvc2l0aW9uOiBcInRvcFJpZ2h0XCIsXG4gICAgYW5pbWF0ZUluc2lkZTogdHJ1ZSxcbiAgICBtZXNzYWdlOiBcIkRyb3BzcmlkZSBBcHByZWNpYXRlcyBZb3VyIFN1cHBvcnQuXCIsXG4gIH0pO1xufSk7XG4vLy0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS1cblxuLy8gSFRNWCBDb25zb2xlIGxvZ3NcbmlmIChwcm9jZXNzLmVudi5OT0RFX0VOViA9PT0gXCJkZXZlbG9wbWVudFwiKSB7XG4gIC8vIGVuYWJsZSBsb2dnaW5nIGZvciBodG14IGluIGRldmVsb3BtZW50IHNlcnZlciBvbmx5XG4gIHdpbmRvdy5odG14LmxvZ0FsbCgpO1xufVxuXG5bXG4gIFwiaHRteDpvbkxvYWRcIixcbiAgXCJodG14OmxvYWRcIixcbiAgXCJsb2FkXCIsXG4gIFwiaHRteDphZnRlclN3YXBcIixcbiAgXCJodG14OmFmdGVyT25Mb2FkXCIsXG4gIFwiaHRteDphZnRlclJlcXVlc3RcIixcbl0uZm9yRWFjaCgoZXZ0KSA9PiB7XG4gIHdpbmRvdy5hZGRFdmVudExpc3RlbmVyKGV2dCwgZnVuY3Rpb24gKCkge1xuICAgIGNvbnN0IGNvdW50ZXJzID0gZG9jdW1lbnQucXVlcnlTZWxlY3RvckFsbChcIi5jb3VudGVyXCIpO1xuICAgIGNvbnN0IGNhciA9IGRvY3VtZW50LmdldEVsZW1lbnRCeUlkKCdjYXInKTtcblxuICAgIGNvbnN0IGNvbnRyb2xsZXIgPSBuZXcgU2Nyb2xsTWFnaWMuQ29udHJvbGxlcigpO1xuXG4gICAgLy8gaWYoZG9jdW1lbnQuZ2V0RWxlbWVudEJ5SWQoJ2NvbnN0Jykpe1xuICAgIC8vICAgbG90dGlld2ViLmxvYWRBbmltYXRpb24oe1xuICAgIC8vICAgICBjb250YWluZXI6IGRvY3VtZW50LmdldEVsZW1lbnRCeUlkKCdjb25zdCcpLFxuICAgIC8vICAgICBwYXRoOiBcIi9zdGF0aWMvdmVuZG9ycy9pbWFnZXMvbG90dGllL3VuZGVyLWNvbnN0cnVjdGlvbi5qc29uXCIsXG4gICAgLy8gICAgIHJlbmRlcmVyOiAnc3ZnJyxcbiAgICAvLyAgICAgbG9vcDogdHJ1ZSxcbiAgICAvLyAgICAgYXV0b1BsYXk6IHRydWUsXG4gICAgLy8gICAgIG5hbWU6ICdVbmRlciBDb25zdHJ1Y3Rpb24nXG4gICAgLy8gICB9KTtcbiAgICAvLyB9XG5cbiAgICBmdW5jdGlvbiBzdGFydENvdW50aW5nKCkge1xuICAgICAgaWYgKGNvdW50ZXJzKSB7XG4gICAgICAgIGNvdW50ZXJzLmZvckVhY2goKGNvdW50ZXIpID0+IHtcbiAgICAgICAgICBhbmltZSh7XG4gICAgICAgICAgICB0YXJnZXRzOiBjb3VudGVyLFxuICAgICAgICAgICAgaW5uZXJIVE1MOiBbMCwgY291bnRlci5nZXRBdHRyaWJ1dGUoXCJkYXRhLWNvdW50XCIpXSxcbiAgICAgICAgICAgIGVhc2luZzogXCJlYXNlSW5PdXRTaW5lXCIsXG4gICAgICAgICAgICByb3VuZDogMSxcbiAgICAgICAgICAgIGR1cmF0aW9uOiA0MDAwLFxuICAgICAgICAgIH0pO1xuICAgICAgICB9KTtcbiAgICAgIH1cbiAgICB9XG5cbiAgICBmdW5jdGlvbiBhbmltYXRlSG93cygpIHtcbiAgICAgIGlmIChkb2N1bWVudC5xdWVyeVNlbGVjdG9yQWxsKCcuaG93JykpIHtcbiAgICAgICAgYW5pbWUoe1xuICAgICAgICAgIHRhcmdldHM6IFwiLmhvd1wiLFxuICAgICAgICAgIHRyYW5zbGF0ZVg6IDU2LFxuICAgICAgICAgIGVhc2luZzogXCJlYXNlSW5PdXRTaW5lXCIsXG4gICAgICAgICAgZHVyYXRpb246IDgwMCxcbiAgICAgICAgICBvcGFjaXR5OiAxLFxuICAgICAgICAgIGRlbGF5OiBhbmltZS5zdGFnZ2VyKDIwMCwgeyBzdGFydDogNTAwIH0pLFxuICAgICAgICB9KTtcbiAgICAgIH1cbiAgICB9XG5cbiAgICBpZihkb2N1bWVudC5nZXRFbGVtZW50QnlJZCgnY291bnRUcmlnZ2VyJykpIHtcbiAgICAgIG5ldyBTY3JvbGxNYWdpYy5TY2VuZSh7XG4gICAgICAgIHRyaWdnZXJFbGVtZW50OiAnI2NvdW50VHJpZ2dlcicsXG4gICAgICAgIHRyaWdnZXJIb29rOiAnb25FbnRlcicsXG4gICAgICAgIGR1cmF0aW9uOiAnMTAwJScsXG4gICAgICAgIHJldmVyc2U6IGZhbHNlLFxuICAgICAgICBvZmZzZXQ6IDUwXG4gICAgICB9KS5vbignZW50ZXInLCBmdW5jdGlvbigpIHtcbiAgICAgICAgc3RhcnRDb3VudGluZygpO1xuICAgICAgfSkuYWRkVG8oY29udHJvbGxlcik7XG4gICAgfVxuXG4gICAgaWYoZG9jdW1lbnQuZ2V0RWxlbWVudEJ5SWQoJ3RyYWNrJykpIHtcbiAgICAgICAgbmV3IFNjcm9sbE1hZ2ljLlNjZW5lKHtcbiAgICAgICAgdHJpZ2dlckVsZW1lbnQ6ICcjdHJhY2snLFxuICAgICAgICB0cmlnZ2VySG9vazogJ29uRW50ZXInLFxuICAgICAgICBkdXJhdGlvbjogJzEwMCUnLFxuICAgICAgICByZXZlcnNlOiB0cnVlLFxuICAgICAgICBvZmZzZXQ6IDUwXG4gICAgICB9KS5vbignZW50ZXInLCBmdW5jdGlvbigpIHtcbiAgICAgICAgY2FyRHJpdmUoKTtcbiAgICAgIH0pLmFkZFRvKGNvbnRyb2xsZXIpO1xuICAgIH1cblxuXG4gICAgaWYoZG9jdW1lbnQuZ2V0RWxlbWVudEJ5SWQoJ2hvd3MnKSkge1xuICAgICAgbmV3IFNjcm9sbE1hZ2ljLlNjZW5lKHtcbiAgICAgICAgdHJpZ2dlckVsZW1lbnQ6ICcjaG93cycsXG4gICAgICAgIHRyaWdnZXJIb29rOiAnb25FbnRlcicsXG4gICAgICAgIGR1cmF0aW9uOiAnMTAwJScsXG4gICAgICAgIHJldmVyc2U6IGZhbHNlLFxuICAgICAgICBvZmZzZXQ6IDEwMFxuICAgICAgfSkub24oJ2VudGVyJywgZnVuY3Rpb24oKSB7XG4gICAgICAgIGFuaW1hdGVIb3dzKCk7XG4gICAgICB9KS5hZGRUbyhjb250cm9sbGVyKTtcbiAgICB9XG5cbiAgICBpZihkb2N1bWVudC5xdWVyeVNlbGVjdG9yQWxsKCcuaW50cm8nKSkge1xuICAgICAgYW5pbWUoe1xuICAgICAgICB0YXJnZXRzOiBcIi5pbnRyb1wiLFxuICAgICAgICB0cmFuc2xhdGVYOiAtNTYsXG4gICAgICAgIGVhc2luZzogXCJlYXNlSW5PdXRTaW5lXCIsXG4gICAgICAgIGR1cmF0aW9uOiA4MDAsXG4gICAgICAgIG9wYWNpdHk6IDEsXG4gICAgICAgIGRlbGF5OiBhbmltZS5zdGFnZ2VyKDIwMCwgeyBzdGFydDogNTAwIH0pLFxuICAgICAgfSk7XG4gICAgfVxuXG5cbiAgICBmdW5jdGlvbiBjYXJEcml2ZSgpIHtcbiAgICAgIGlmIChjYXIpIHtcbiAgICAgICAgYW5pbWUoe1xuICAgICAgICAgIHRhcmdldHM6IFwiI2NhclwiLFxuICAgICAgICAgIHRyYW5zbGF0ZVg6IHtcbiAgICAgICAgICAgIHZhbHVlOiBcIi0xMDB2d1wiLFxuICAgICAgICAgICAgZHVyYXRpb246IDUwMDAsXG4gICAgICAgICAgfSxcbiAgICAgICAgICBlYXNpbmc6IFwiZWFzZUluT3V0U2luZVwiLFxuICAgICAgICAgIG9wYWNpdHk6IDEsXG4gICAgICAgICAgZGVsYXk6IGFuaW1lLnN0YWdnZXIoMjAwLCB7IHN0YXJ0OiA1MDAgfSksXG4gICAgICAgICAgZGlyZWN0aW9uOiBcIm5vcm1hbFwiLFxuICAgICAgICAgIGxvb3A6IGZhbHNlLFxuICAgICAgICB9KTtcbiAgICAgIH1cbiAgICB9XG4gIH0pO1xufSk7XG4iLCJpbXBvcnQgYXhpb3MgZnJvbSBcIi4vYXhpb3NGYWN0b3J5XCI7XG5pbXBvcnQgaHRteCBmcm9tIFwiaHRteC5vcmcvZGlzdC9odG14XCI7XG5pbXBvcnQgaXppVG9hc3QgZnJvbSAnaXppdG9hc3QvZGlzdC9qcy9pemlUb2FzdC5taW4uanMnOyAgLy8geW91IGhhdmUgYWNjZXNzIHRvIGl6aVRvYXN0IG5vd1xuXG4vLyBmdW5jdGlvbiBzZXJpYWxpemUoZGF0YSkge1xuLy8gICAgIGxldCBvYmogPSB7fTtcbi8vICAgICBmb3IgKGxldCBba2V5LCB2YWx1ZV0gb2YgZGF0YSkge1xuLy8gICAgICAgaWYgKG9ialtrZXldICE9PSB1bmRlZmluZWQpIHtcbi8vICAgICAgICAgaWYgKCFBcnJheS5pc0FycmF5KG9ialtrZXldKSkge1xuLy8gICAgICAgICAgIG9ialtrZXldID0gW29ialtrZXldXTtcbi8vICAgICAgICAgfVxuLy8gICAgICAgICBvYmpba2V5XS5wdXNoKHZhbHVlKTtcbi8vICAgICAgIH0gZWxzZSB7XG4vLyAgICAgICAgIG9ialtrZXldID0gdmFsdWU7XG4vLyAgICAgICB9XG4vLyAgICAgfVxuLy8gICAgIHJldHVybiBvYmo7XG4vLyB9XG5cblxuZnVuY3Rpb24gc2xlZXAobXMpIHtcbiAgICByZXR1cm4gbmV3IHdpbmRvdy5Qcm9taXNlKHJlc29sdmUgPT4gc2V0VGltZW91dChyZXNvbHZlLCBtcykpO1xufVxuXG5mdW5jdGlvbiB2YWxpZGF0ZUZpZWxkKGZvcm1FbGVtZW50LCBmaWVsZEVsZW1lbnQpIHtcbiAgICBsZXQgZm9ybURhdGEgPSBuZXcgRm9ybURhdGEoZm9ybUVsZW1lbnQpO1xuICAgIGZvcm1EYXRhLmFwcGVuZChcIl9fZmllbGRfbmFtZV9fXCIsIGZpZWxkRWxlbWVudC5uYW1lKTtcblxuICAgIGF4aW9zLnBvc3QoZm9ybUVsZW1lbnQuYWN0aW9uLCBmb3JtRGF0YSkudGhlbihmdW5jdGlvbiAocmVzcG9uc2UpIHtcbiAgICAgIGxldCBlcnJvcnMgPSByZXNwb25zZS5kYXRhLmVycm9ycztcbiAgICAgIGxldCBlcnJvcnNXcmFwcGVyRWxlbWVudCA9IGRvY3VtZW50LmdldEVsZW1lbnRCeUlkKGBlcnJvci13cmFwcGVyLSR7ZmllbGRFbGVtZW50Lm5hbWV9YCk7XG4gICAgICBpZiAoZXJyb3JzLmxlbmd0aCA9PT0gMCkge1xuICAgICAgICBkb2N1bWVudC5nZXRFbGVtZW50QnlJZCgnc3VibWl0JykuY2xhc3NMaXN0LnJlbW92ZSgnaGlkZGVuJyk7XG4gICAgICAgIGVycm9yc1dyYXBwZXJFbGVtZW50LmNsYXNzTGlzdC5hZGQoJ2hpZGRlbicpO1xuICAgICAgICBpZiAoZXJyb3JzV3JhcHBlckVsZW1lbnQpIHtcbiAgICAgICAgICBlcnJvcnNXcmFwcGVyRWxlbWVudC5pbm5lckhUTUwgPSBcIlwiO1xuICAgICAgICB9XG4gICAgICB9IGVsc2Uge1xuICAgICAgICBkb2N1bWVudC5nZXRFbGVtZW50QnlJZCgnc3VibWl0JykuY2xhc3NMaXN0LmFkZCgnaGlkZGVuJyk7XG4gICAgICAgIGVycm9yc1dyYXBwZXJFbGVtZW50LmNsYXNzTGlzdC5yZW1vdmUoJ2hpZGRlbicpO1xuICAgICAgICBlcnJvcnNXcmFwcGVyRWxlbWVudC5jbGFzc0xpc3QuYWRkKCdmbGV4Jyk7XG4gICAgICAgIGlmIChlcnJvcnNXcmFwcGVyRWxlbWVudCkge1xuICAgICAgICAgIGxldCBlcnJvcnNIdG1sID0gJyc7XG4gICAgICAgICAgZm9yIChsZXQgaSA9IDA7IGkgPCBlcnJvcnMubGVuZ3RoOyBpKyspIHtcbiAgICAgICAgICAgIGVycm9yc0h0bWwgKz0gYCR7ZXJyb3JzW2ldfWA7XG4gICAgICAgICAgfVxuICAgICAgICAgIGVycm9yc1dyYXBwZXJFbGVtZW50LmlubmVySFRNTCA9IGVycm9yc0h0bWw7XG4gICAgICAgIH1cbiAgICAgIH1cbiAgICB9KTtcbiAgfVxuXG5cbmV4cG9ydCBkZWZhdWx0IGZ1bmN0aW9uIENvbnRhY3RGb3JtKCkge1xuICAgIHJldHVybiB7XG4gICAgICAgIHByb2Nlc3Npbmc6IGZhbHNlLFxuXG4gICAgICAgIGFzeW5jIHN1Ym1pdEZvcm0oKSB7XG4gICAgICAgICAgICB0aGlzLnByb2Nlc3NpbmcgPSB0cnVlO1xuXG4gICAgICAgICAgICBjb25zdCBmb3JtRWxlbWVudCA9IHRoaXMuJHJlZnMuY29udGFjdEZvcm07XG4gICAgICAgICAgICBjb25zdCBkaXYgPSBkb2N1bWVudC5nZXRFbGVtZW50QnlJZCgnY29udGFjdCcpO1xuICAgICAgICAgICAgY29uc3QgcmVkaXJlY3QgPSBmb3JtRWxlbWVudC5hY3Rpb247XG4gICAgICAgICAgICBjb25zdCBjc3JmID0gZm9ybUVsZW1lbnQuZGF0YXNldC5jc3JmO1xuICAgICAgICAgICAgbGV0IGRhdGEgPSBuZXcgRm9ybURhdGEoZm9ybUVsZW1lbnQpO1xuICAgICAgICAgICAgZm9ybUVsZW1lbnQucXVlcnlTZWxlY3RvckFsbChcIltuYW1lXVwiKS5mb3JFYWNoKGZpZWxkRWxlbWVudCA9PiB7XG4gICAgICAgICAgICAgICAgZGF0YS5hcHBlbmQoZmllbGRFbGVtZW50Lm5hbWUsIGZpZWxkRWxlbWVudC52YWx1ZSk7XG4gICAgICAgICAgICB9KTtcblxuICAgICAgICAgICAgY29uc29sZS5sb2coZGF0YSk7XG4gICAgICAgICAgICAvLyBkYXRhLmFwcGVuZCgnY3NyZm1pZGRsZXdhcmV0b2tlbicsIGNzcmYpO1xuICAgICAgICAgICAgLy8gZGF0YS5hcHBlbmQoJ25hbWUnLCBkb2N1bWVudC5nZXRFbGVtZW50QnlJZCgnaWRfbmFtZScpLnZhbHVlKTtcbiAgICAgICAgICAgIC8vIGRhdGEuYXBwZW5kKCdlbWFpbCcsIGRvY3VtZW50LmdldEVsZW1lbnRCeUlkKCdpZF9lbWFpbCcpLnZhbHVlKTtcbiAgICAgICAgICAgIC8vIGRhdGEuYXBwZW5kKCdtZXNzYWdlJywgZG9jdW1lbnQuZ2V0RWxlbWVudEJ5SWQoJ2lkX21lc3NhZ2UnKS52YWx1ZSk7XG5cbiAgICAgICAgICAgIC8vIGNvbnNvbGUuaW5mbyhcIkZPUk0gREFUQTogXCIsIGRhdGEpO1xuXG4gICAgICAgICAgICAvLyBsZXQgZm9ybURhdGEgPSBzZXJpYWxpemUoZGF0YSk7XG4gICAgICAgICAgICAvLyBjb25zb2xlLmluZm8oXCJTRVJJQUxJWkVEIEZPUk0gREFUQTogXCIsIGZvcm1EYXRhKTtcblxuXG4gICAgICAgICAgICBpZiAoZm9ybUVsZW1lbnQuY2hlY2tWYWxpZGl0eSgpKSB7XG4gICAgICAgICAgICAgICAgYXdhaXQgYXhpb3MucG9zdChyZWRpcmVjdCwgZGF0YSwge1xuICAgICAgICAgICAgICAgICAgICBoZWFkZXJzOiB7XG4gICAgICAgICAgICAgICAgICAgICAgJ1gtQ1NSRlRva2VuJzogY3NyZlxuICAgICAgICAgICAgICAgICAgICB9fSlcbiAgICAgICAgICAgICAgICAgICAgLnRoZW4oZnVuY3Rpb24gKHJlc3BvbnNlKSB7XG4gICAgICAgICAgICAgICAgICAgICAgICAvLyBjb25zb2xlLmluZm8oXCJSRVNQT05TRSBEQVRBOiBcIiwgcmVzcG9uc2UpO1xuXG4gICAgICAgICAgICAgICAgICAgICAgICBpZiAocmVzcG9uc2Uuc3RhdHVzID09PSAyMDAgfHwgcmVzcG9uc2UuZGF0YS5tZXNzYWdlID09PSBcIlN1cHBvcnQgTWFpbCBTdWNjZXNzZnVsbHkgU2VudFwiKSB7XG4gICAgICAgICAgICAgICAgICAgICAgICAgICAgZGl2LmlubmVySFRNTCA9IGBcbiAgICAgICAgICAgICAgICAgICAgICAgICAgICA8ZGl2IGNsYXNzPVwidy1mdWxsIHRleHQtZ3JlZW4tMzAwIHNwYWNlLXktOCBmbGV4IGZsZXgtY29sIGp1c3RpZnktY2VudGVyIHB5LTI0XCI+XG4gICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIDxzdmcgeG1sbnM9XCJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2Z1wiIGZpbGw9XCJub25lXCIgdmlld0JveD1cIjAgMCAyNCAyNFwiIHN0cm9rZS13aWR0aD1cIjEuNVwiIHN0cm9rZT1cImN1cnJlbnRDb2xvclwiIGNsYXNzPVwiYmxvY2sgdy0xNCBoLTE0IGJsb2NrIG14LWF1dG8gYW5pbWF0ZS1ib3VuY2UgdGV4dC1ncmVlbi0zMDBcIj5cbiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIDxwYXRoIHN0cm9rZS1saW5lY2FwPVwicm91bmRcIiBzdHJva2UtbGluZWpvaW49XCJyb3VuZFwiIGQ9XCJNMjEuNzUgNi43NXYxMC41YTIuMjUgMi4yNSAwIDAxLTIuMjUgMi4yNWgtMTVhMi4yNSAyLjI1IDAgMDEtMi4yNS0yLjI1VjYuNzVtMTkuNSAwQTIuMjUgMi4yNSAwIDAwMTkuNSA0LjVoLTE1YTIuMjUgMi4yNSAwIDAwLTIuMjUgMi4yNW0xOS41IDB2LjI0M2EyLjI1IDIuMjUgMCAwMS0xLjA3IDEuOTE2bC03LjUgNC42MTVhMi4yNSAyLjI1IDAgMDEtMi4zNiAwTDMuMzIgOC45MWEyLjI1IDIuMjUgMCAwMS0xLjA3LTEuOTE2VjYuNzVcIiAvPlxuICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICA8L3N2Zz5cbiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgPGRpdiBjbGFzcz1cInctZnVsbCBtZDp3LTMvNSB0ZXh0LWNlbnRlciBzcGFjZS15LTMgbXgtYXV0b1wiPlxuICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgPGg0IGNsYXNzPVwidGV4dC1ncmVlbi01MDAgZm9udC1zZW1pYm9sZCB0ZXh0LTJ4bCBtZDp0ZXh0LTR4bFwiPk1haWwgU2VudCBTdWNjZXNzZnVsbHk8L2g0PlxuICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgPHA+JHtyZXNwb25zZS5kYXRhLm1lc3NhZ2V9PC9wPlxuICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICA8L2Rpdj5cbiAgICAgICAgICAgICAgICAgICAgICAgICAgICA8L2Rpdj5cbiAgICAgICAgICAgICAgICAgICAgICAgICAgICBgO1xuICAgICAgICAgICAgICAgICAgICAgICAgICAgIGl6aVRvYXN0LnN1Y2Nlc3Moe1xuICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICB0aXRsZTogXCJFbWFpbCBTZW50IFN1Y2Nlc3NmdWxcIixcbiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgYmFsbG9vbjogdHJ1ZSxcbiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgcG9zaXRpb246IFwidG9wUmlnaHRcIixcbiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgYW5pbWF0ZUluc2lkZTogdHJ1ZSxcbiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgbWVzc2FnZTogcmVzcG9uc2UuZGF0YS5tZXNzYWdlXG4gICAgICAgICAgICAgICAgICAgICAgICAgICAgfSk7XG4gICAgICAgICAgICAgICAgICAgICAgICAgICAgc2xlZXAoMzUwMCk7IC8vd2FpdCAxIHNlYyBhbmQgdGhlbiBodG14IHJlZGlyZWN0IGdldFxuICAgICAgICAgICAgICAgICAgICAgICAgICAgIGh0bXguYWpheCgnR0VUJywgcmVkaXJlY3QsIHt0YXJnZXQ6J2JvZHknLCBzd2FwOidvdXRlckhUTUwnfSk7XG4gICAgICAgICAgICAgICAgICAgICAgICAgICAgLy8gc2xlZXAoMzUwMCk7IC8vd2FpdCAxIHNlYyBhbmQgdGhlbiBodG14IHJlZGlyZWN0IGdldFxuICAgICAgICAgICAgICAgICAgICAgICAgICAgIC8vIGxvY2F0aW9uLnJlbG9hZCgpO1xuICAgICAgICAgICAgICAgICAgICAgICAgfVxuXG4gICAgICAgICAgICAgICAgICAgICAgICBjb25zb2xlLmxvZyhyZXNwb25zZSk7XG4gICAgICAgICAgICAgICAgICAgIH0pLmNhdGNoKGZ1bmN0aW9uIChlcnJvcikge1xuICAgICAgICAgICAgICAgICAgICAgICAgaXppVG9hc3QuZXJyb3Ioe1xuICAgICAgICAgICAgICAgICAgICAgICAgICAgIHRpdGxlOiBcIkVtYWlsIFNlbmRpbmcgSW5jb21wbGV0ZVwiLFxuICAgICAgICAgICAgICAgICAgICAgICAgICAgIGJhbGxvb246IHRydWUsXG4gICAgICAgICAgICAgICAgICAgICAgICAgICAgcG9zaXRpb246IFwidG9wUmlnaHRcIixcbiAgICAgICAgICAgICAgICAgICAgICAgICAgICBhbmltYXRlSW5zaWRlOiB0cnVlLFxuICAgICAgICAgICAgICAgICAgICAgICAgICAgIG1lc3NhZ2U6IGBTb21ldGhpbmcgd3JvbmcgaGFwcGVuZWQ6ICR7ZXJyb3J9YFxuICAgICAgICAgICAgICAgICAgICAgICAgfSk7XG4gICAgICAgICAgICAgICAgICAgIH0pO1xuICAgICAgICAgICAgICAgICAgICAvLyAuZmluYWxseShmdW5jdGlvbiAoKSB7XG4gICAgICAgICAgICAgICAgICAgIC8vICAgICBjb25zb2xlLmxvZyhcImZpbmFsbHlcIik7XG4gICAgICAgICAgICAgICAgICAgIC8vIH0pO1xuXG4gICAgICAgICAgICAgICAgdGhpcy5wcm9jZXNzaW5nID0gZmFsc2U7XG4gICAgICAgICAgICB9IGVsc2Uge1xuICAgICAgICAgICAgICAgIGl6aVRvYXN0LmVycm9yKHtcbiAgICAgICAgICAgICAgICAgICAgdGl0bGU6IFwiU2VuZGluZyBFbWFpbCBJbmNvbXBsZXRlXCIsXG4gICAgICAgICAgICAgICAgICAgIGJhbGxvb246IHRydWUsXG4gICAgICAgICAgICAgICAgICAgIHBvc2l0aW9uOiBcInRvcFJpZ2h0XCIsXG4gICAgICAgICAgICAgICAgICAgIGFuaW1hdGVJbnNpZGU6IHRydWUsXG4gICAgICAgICAgICAgICAgICAgIG1lc3NhZ2U6IGBGb3JtIGRhdGEgaXMgbm90IHZhbGlkLiBFbnN1cmUgeW91IGhhdmUgZmlsbGVkIGFsbCBmaWVsZHMgYWNjdXJhdGVseSEgJHtmb3JtRWxlbWVudC5yZXBvcnRWYWxpZGl0eSgpfWBcbiAgICAgICAgICAgICAgICB9KTtcbiAgICAgICAgICAgICAgICBzbGVlcCgyNTAwKTsgLy93YWl0IDIuNSBzZWMgYW5kIHRoZW4gaHRteCByZWRpcmVjdCBnZXRcbiAgICAgICAgICAgICAgICB0aGlzLnByb2Nlc3NpbmcgPSBmYWxzZTtcbiAgICAgICAgICAgICAgICBodG14LmFqYXgoJ0dFVCcsIHJlZGlyZWN0LCB7dGFyZ2V0Oidib2R5Jywgc3dhcDonb3V0ZXJIVE1MJ30pO1xuICAgICAgICAgICAgfVxuXG4gICAgICAgIH0sXG5cbiAgICAgICAgYXN5bmMgY2hlY2tWYWxpZGl0eSgpIHtcbiAgICAgICAgICAgIGNvbnN0IGZvcm1FbGVtZW50ID0gdGhpcy4kcmVmcy5jb250YWN0Rm9ybTtcbiAgICAgICAgICAgIGZvcm1FbGVtZW50LnF1ZXJ5U2VsZWN0b3JBbGwoJ1tuYW1lXScpLmZvckVhY2goZmllbGRFbGVtZW50ID0+IHtcbiAgICAgICAgICAgICAgICBmaWVsZEVsZW1lbnQuYWRkRXZlbnRMaXN0ZW5lcignY2hhbmdlJywgZXZlbnQgPT4ge1xuICAgICAgICAgICAgICAgICAgICBjb25zb2xlLmxvZyhldmVudCk7XG4gICAgICAgICAgICAgICAgICAgIHZhbGlkYXRlRmllbGQoZm9ybUVsZW1lbnQsIGZpZWxkRWxlbWVudCk7XG4gICAgICAgICAgICAgICAgfSk7XG4gICAgICAgICAgICB9KTtcbiAgICAgICAgfSxcblxuICAgICAgICBnZXRCdG5UZXh0KCkge1xuICAgICAgICAgICAgcmV0dXJuIHRoaXMucHJvY2Vzc2luZyA/ICdQcm9jZXNzaW5nLi4uJyA6ICdTdWJtaXQnO1xuICAgICAgICB9XG4gICAgfTtcbn1cbiIsImV4cG9ydCBkZWZhdWx0IGZ1bmN0aW9uIFN0aWNreU5hdigpIHtcbiAgICByZXR1cm4ge1xuICAgICAgICBzaG93TmF2OiB0cnVlLFxuICAgICAgICBuYXZUb3A6IGZhbHNlLFxuICAgICAgICBsYXN0U2Nyb2xsOiAwLFxuXG4gICAgICAgIGluaXRTdGF0ZSgpIHtcbiAgICAgICAgICAgIGNvbnN0IG1haW4gPSBkb2N1bWVudC5nZXRFbGVtZW50QnlJZCgnbWFpbicpO1xuICAgICAgICAgICAgY29uc3QgbmF2YmFyID0gZG9jdW1lbnQuZ2V0RWxlbWVudEJ5SWQoJ25hdmJhcicpO1xuXG4gICAgICAgICAgICAvLyBnZXQgdGhlIGhlaWdodCBvZiB0aGUgbmF2YmFyIGFuZCB0aGVuIGFkZCBpdCB0byB0aGUgdG9wIHBhZGRpbmcgb2YgdGhlIG1haW4gY29udGVudFxuICAgICAgICAgICAgY29uc3QgaGVhZGVyX2ggPSBuYXZiYXIub2Zmc2V0SGVpZ2h0ICsgMTA7XG5cbiAgICAgICAgICAgIG1haW4uY2xhc3NMaXN0LmFkZChgcHQtWyR7aGVhZGVyX2h9cHhdYCk7XG4gICAgICAgICAgICB0aGlzLm5hdlRvcCA9IHRydWU7XG4gICAgICAgICAgICB0aGlzLnNob3dOYXYgPSBmYWxzZTtcbiAgICAgICAgfSxcblxuICAgICAgICBzY3JvbGxOYXYoKSB7XG4gICAgICAgICAgICBsZXQgY3VycmVudFNjcm9sbCA9IHdpbmRvdy5wYWdlWU9mZnNldDtcbiAgICAgICAgICAgIGlmIChjdXJyZW50U2Nyb2xsIDw9IDApIHtcbiAgICAgICAgICAgICAgICB0aGlzLnNob3dOYXYgPSB0cnVlO1xuICAgICAgICAgICAgICAgIHRoaXMubmF2VG9wID0gdHJ1ZTtcbiAgICAgICAgICAgIH1cblxuICAgICAgICAgICAgaWYgKGN1cnJlbnRTY3JvbGwgPiB0aGlzLmxhc3RTY3JvbGwgJiYgdGhpcy5zaG93TmF2ID09PSBmYWxzZSkge1xuICAgICAgICAgICAgICAgIHRoaXMuc2hvd05hdiA9IHRydWU7XG4gICAgICAgICAgICAgICAgdGhpcy5uYXZUb3AgPSBmYWxzZTtcbiAgICAgICAgICAgIH0gZWxzZSBpZiAoY3VycmVudFNjcm9sbCA8IHRoaXMubGFzdFNjcm9sbCAmJiB0aGlzLnNob3dOYXYgPT09IHRydWUpIHtcbiAgICAgICAgICAgICAgICB0aGlzLnNob3dOYXYgPSBmYWxzZTtcbiAgICAgICAgICAgICAgICB0aGlzLm5hdlRvcCA9IHRydWU7XG4gICAgICAgICAgICB9XG4gICAgICAgICAgICB0aGlzLmxhc3RTY3JvbGwgPSBjdXJyZW50U2Nyb2xsO1xuICAgICAgICB9XG4gICAgfTtcbn1cbiIsImltcG9ydCBheGlvcyBmcm9tIFwiYXhpb3NcIjtcblxuYXhpb3MuZGVmYXVsdHMud2l0aENyZWRlbnRpYWxzID0gdHJ1ZTtcbmF4aW9zLmRlZmF1bHRzLnhzcmZDb29raWVOYW1lID0gJ2NzcmZ0b2tlbic7XG5heGlvcy5kZWZhdWx0cy54c3JmSGVhZGVyTmFtZSA9IFwiWC1DU1JGVE9LRU5cIjtcbi8vIGF4aW9zLmRlZmF1bHRzLmhlYWRlcnNbJ1gtQ1NSRlRva2VuJ10gPSBkb2N1bWVudC5oZWFkLnF1ZXJ5U2VsZWN0b3IoJ21ldGFbbmFtZT1cImNzcmYtdG9rZW5cIl0nKS5nZXRBdHRyaWJ1dGUoJ2NvbnRlbnQnKTtcbmF4aW9zLmRlZmF1bHRzLnRpbWVvdXQgPSAxNTAwMDtcblxuZXhwb3J0IGRlZmF1bHQgYXhpb3M7XG4iLCIvLyBleHRyYWN0ZWQgYnkgbWluaS1jc3MtZXh0cmFjdC1wbHVnaW5cbmV4cG9ydCB7fTsiLCIvKiAoaWdub3JlZCkgKi8iXSwibmFtZXMiOlsiaHRteCIsIkFscGluZSIsImV0aGVycyIsImF4aW9zIiwiU3RpY2t5TmF2IiwiU3dpcGVyIiwiZGV0ZWN0IiwiaXppVG9hc3QiLCJhbmltZSIsIlNjcm9sbE1hZ2ljIiwiQ29udGFjdEZvcm0iLCJsb3R0aWV3ZWIiLCJ3aW5kb3ciLCJzY3JvbGxNYWdpYyIsIml6aXRvYXN0IiwiZGF0YSIsInN0YXJ0Iiwic3ciLCJob21lIiwiYnJvd3NlciIsIkFQUExJQ0FUSU9OX1NFUlZFUl9LRVkiLCJDUkVBVEVfV1BfREVWSUNFIiwiU0VORF9OT1RJRklDQVRJT04iLCJXRUJfUFVTSF9DRkciLCJ1cmxCYXNlNjRUb1VpbnQ4QXJyYXkiLCJiYXNlNjRTdHJpbmciLCJwYWRkaW5nIiwicmVwZWF0IiwibGVuZ3RoIiwiYmFzZTY0IiwicmVwbGFjZSIsInJhd0RhdGEiLCJhdG9iIiwib3V0cHV0QXJyYXkiLCJVaW50OEFycmF5IiwiaSIsImNoYXJDb2RlQXQiLCJzYXZlU3Vic2NyaWJlT2JqIiwic3Vic2NyaXB0aW9uIiwic3Vic2NyaXB0aW9uSnNvbiIsInRvSlNPTiIsImVuZHBvaW50UGFydHMiLCJlbmRwb2ludCIsInNwbGl0IiwicmVnaXN0cmF0aW9uSWQiLCJwcmVkYXRhIiwic3RhdHVzX3R5cGUiLCJuYW1lIiwidG9Mb3dlckNhc2UiLCJwMjU2ZGgiLCJrZXlzIiwiYXV0aCIsInVzZXJfYWdlbnQiLCJuYXZpZ2F0b3IiLCJnZXRVc2VyQWdlbnQiLCJyZWdpc3RyYXRpb25faWQiLCJncm91cCIsIkpTT04iLCJzdHJpbmdpZnkiLCJwb3N0IiwiaGVhZGVycyIsInRoZW4iLCJyZXNwb25zZSIsInByb2Nlc3MiLCJlbnYiLCJOT0RFX0VOViIsImNvbnNvbGUiLCJsb2ciLCJzdWNjZXNzIiwidGl0bGUiLCJiYWxsb29uIiwicG9zaXRpb24iLCJhbmltYXRlSW5zaWRlIiwibWVzc2FnZSIsInN0YXR1c1RleHQiLCJjYXRjaCIsImVycm9yIiwic3Vic2NyaWJlIiwicmVnaXN0cmF0aW9uIiwicHVzaE1hbmFnZXIiLCJnZXRTdWJzY3JpcHRpb24iLCJzZXR1cFRyaWdnZXJCdXR0b24iLCJvcHRpb25zIiwidXNlclZpc2libGVPbmx5IiwiYXBwbGljYXRpb25TZXJ2ZXJLZXkiLCJ0cmlnZ2VyTm90aWZpY2F0aW9uQnV0dG9uIiwiZG9jdW1lbnQiLCJnZXRFbGVtZW50QnlJZCIsImNsYXNzTGlzdCIsInRvZ2dsZSIsImFkZEV2ZW50TGlzdGVuZXIiLCJzdWJKc29uIiwiaGVhZCIsImJvZHkiLCJkZXRhaWwiLCJzZXJ2aWNlV29ya2VyIiwicmVnaXN0ZXIiLCJzY29wZSIsInJlYWR5IiwiYWN0aXZlIiwiaW5pdGlhbGlzZVN0YXRlIiwiZXJyIiwicmVnIiwic2hvd05vdGlmaWNhdGlvbiIsIk5vdGlmaWNhdGlvbiIsInBlcm1pc3Npb24iLCJ3YXJuaW5nIiwiaW5mbyIsInN1YiIsImluc3RhbGxCdXR0b24iLCJldmVudCIsImRlZmVycmVkUHJvbXB0IiwicHJvbXB0RXZlbnQiLCJwcm9tcHQiLCJ1c2VyQ2hvaWNlIiwiY2hvaWNlIiwibG9nQWxsIiwiZm9yRWFjaCIsImV2dCIsImNvdW50ZXJzIiwicXVlcnlTZWxlY3RvckFsbCIsImNhciIsImNvbnRyb2xsZXIiLCJDb250cm9sbGVyIiwic3RhcnRDb3VudGluZyIsImNvdW50ZXIiLCJ0YXJnZXRzIiwiaW5uZXJIVE1MIiwiZ2V0QXR0cmlidXRlIiwiZWFzaW5nIiwicm91bmQiLCJkdXJhdGlvbiIsImFuaW1hdGVIb3dzIiwidHJhbnNsYXRlWCIsIm9wYWNpdHkiLCJkZWxheSIsInN0YWdnZXIiLCJTY2VuZSIsInRyaWdnZXJFbGVtZW50IiwidHJpZ2dlckhvb2siLCJyZXZlcnNlIiwib2Zmc2V0Iiwib24iLCJhZGRUbyIsImNhckRyaXZlIiwidmFsdWUiLCJkaXJlY3Rpb24iLCJsb29wIiwic2xlZXAiLCJtcyIsIlByb21pc2UiLCJyZXNvbHZlIiwic2V0VGltZW91dCIsInZhbGlkYXRlRmllbGQiLCJmb3JtRWxlbWVudCIsImZpZWxkRWxlbWVudCIsImZvcm1EYXRhIiwiRm9ybURhdGEiLCJhcHBlbmQiLCJhY3Rpb24iLCJlcnJvcnMiLCJlcnJvcnNXcmFwcGVyRWxlbWVudCIsInJlbW92ZSIsImFkZCIsImVycm9yc0h0bWwiLCJwcm9jZXNzaW5nIiwic3VibWl0Rm9ybSIsIiRyZWZzIiwiY29udGFjdEZvcm0iLCJkaXYiLCJyZWRpcmVjdCIsImNzcmYiLCJkYXRhc2V0IiwiY2hlY2tWYWxpZGl0eSIsInN0YXR1cyIsImFqYXgiLCJ0YXJnZXQiLCJzd2FwIiwicmVwb3J0VmFsaWRpdHkiLCJnZXRCdG5UZXh0Iiwic2hvd05hdiIsIm5hdlRvcCIsImxhc3RTY3JvbGwiLCJpbml0U3RhdGUiLCJtYWluIiwibmF2YmFyIiwiaGVhZGVyX2giLCJvZmZzZXRIZWlnaHQiLCJzY3JvbGxOYXYiLCJjdXJyZW50U2Nyb2xsIiwicGFnZVlPZmZzZXQiLCJkZWZhdWx0cyIsIndpdGhDcmVkZW50aWFscyIsInhzcmZDb29raWVOYW1lIiwieHNyZkhlYWRlck5hbWUiLCJ0aW1lb3V0Il0sInNvdXJjZVJvb3QiOiIifQ==