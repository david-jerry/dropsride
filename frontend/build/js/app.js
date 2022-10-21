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
      // console.log(response);
      // iziToast.success({
      //   title: "[PUSH NOTIFICATION SERVER]",
      //   balloon: true,
      //   position: "topRight",
      //   animateInside: true,
      //   message: `Notification Subscription ${response.statusText}`,
      // });
      const subscribeNotificationButton = document.getElementById('subscribeNotificationButton');
      subscribeNotificationButton.classList.toggle('hidden', true);
      izitoast_dist_js_iziToast_min_js__WEBPACK_IMPORTED_MODULE_8___default().success({
        title: "[PUSH NOTIFICATION SUBSCRIPTION]",
        balloon: true,
        position: "topRight",
        animateInside: true,
        message: `Subscription Sent Successfully ${response.statusText}`
      }); // if subscription is successfully saved to the server
      // then enable the test notification push button to be visible

      setupTriggerButton(subscription);
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
}

function saveDriverSubscribeObj(subscription) {
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
    group: "drivers"
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
}

function saveCompanySubscribeObj(subscription) {
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
    group: "drivers"
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


    saveSubscribeObj(subscription);
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
}

function subscribeDriver(registration) {
  registration.pushManager.getSubscription().then(function (subscription) {
    if (subscription) {
      console.log("subscription exists");
      saveDriverSubscribeObj(subscription);
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


    saveDriverSubscribeObj(subscription);
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
}

function subscribeCompany(registration) {
  registration.pushManager.getSubscription().then(function (subscription) {
    if (subscription) {
      console.log("subscription exists");
      saveCompanySubscribeObj(subscription);
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


    saveCompanySubscribeObj(subscription);
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
// subscribe(reg);


function setupSubscribeButton(reg) {
  if (document.getElementById('subscribeNotificationButton')) {
    const subscribeNotificationButton = document.getElementById('subscribeNotificationButton');
    subscribeNotificationButton.classList.toggle('hidden', false);
    subscribeNotificationButton.addEventListener('click', () => {
      subscribe(reg);
      console.log("Subscribe Button Set");
    });
  }
}

function setupDriverSubscribeButton(reg) {
  if (document.getElementById('subscribeDriver')) {
    const subscribeDriverButton = document.getElementById('subscribeDriver');
    subscribeDriverButton.addEventListener('click', () => {
      subscribeDriver(reg);
    });
  }
}

function setupCompanySubscribeButton(reg) {
  if (document.getElementById('subscribeCompany')) {
    const subscribeCompanyButton = document.getElementById('subscribeCompany');
    subscribeCompanyButton.addEventListener('click', () => {
      subscribeCompany(reg);
    });
  }
} //----------------------------------------------------------
// This function is for a user to test the push notification
//----------------------------------------------------------


function setupTriggerButton(subscription) {
  const subJson = subscription.toJSON();
  const endpointParts = subJson.endpoint.split("/");
  const registrationId = endpointParts[endpointParts.length - 1];
  const predata = {
    registration_id: registrationId,
    auth: subJson.keys.auth,
    head: "Welcome to Dropsride",
    body: "This is how our push notifications shall be appearing on your device."
  };
  const data = JSON.stringify(predata);
  _components_axiosFactory__WEBPACK_IMPORTED_MODULE_3__["default"].post(SEND_NOTIFICATION, data, {
    headers: {
      "Content-Type": "application/json"
    }
  }).then(function (response) {
    izitoast_dist_js_iziToast_min_js__WEBPACK_IMPORTED_MODULE_8___default().info({
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
  return;
} //----------------------------------------------------------
// End push notification button
//----------------------------------------------------------


if (document.getElementById('shareUrl')) {
  const shareButton = document.getElementById('shareUrl');
  const url = shareButton.dataset.url;
  const title = document.title;
  shareButton.addEventListener('click', () => {
    if (navigator.share) {
      navigator.share({
        title: title,
        text: `Check out ${title.toUpperCase()}.`,
        url: url
      }).then(() => izitoast_dist_js_iziToast_min_js__WEBPACK_IMPORTED_MODULE_8___default().success({
        title: "[SHARE PAGE]",
        balloon: true,
        position: "topRight",
        animateInside: true,
        message: `Successfully share ${url}`
      })).catch(error => izitoast_dist_js_iziToast_min_js__WEBPACK_IMPORTED_MODULE_8___default().error({
        title: "[SHARE PAGE ERROR]",
        balloon: true,
        position: "topRight",
        animateInside: true,
        message: error
      }));
    }
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
    console.log("Registration Object", reg);

    if (!sub || sub === null) {
      setupSubscribeButton(reg);
    } else if (sub !== null) {
      console.log("Subscribe Already Done"); // setupTriggerButton(sub);

      izitoast_dist_js_iziToast_min_js__WEBPACK_IMPORTED_MODULE_8___default().info({
        title: "[SERVICE WORKER]",
        balloon: true,
        position: "topRight",
        animateInside: true,
        message: "Push notification has already been subscribed to"
      });
    }
  });
  setupDriverSubscribeButton(reg);
  setupCompanySubscribeButton(reg);
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
        if (fieldElement.type === "textarea") {
          let textarea = fieldElement.id;
          console.log('textarea content: ', window.parent.tinymce.get(textarea).getContent());
          data.append(fieldElement.name, window.parent.tinymce.get(textarea).getContent());
        }

        if (fieldElement.type !== "textarea") {
          data.append(fieldElement.name, fieldElement.value);
        }
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
        if (fieldElement.type === "textarea") {
          let textarea = fieldElement.id;
          console.log('textarea content: ', window.parent.tinymce.get(textarea).getContent());
          data.append(fieldElement.name, window.parent.tinymce.get(textarea).getContent());
        }

        if (fieldElement.type !== "textarea") {
          data.append(fieldElement.name, fieldElement.value);
        }
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
//# sourceMappingURL=data:application/json;charset=utf-8;base64,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Q0EsS0FBS0wsTUFBTCxHQUFjLElBQWQ7TUFDQSxLQUFLRCxPQUFMLEdBQWUsS0FBZjtJQUNILENBZkU7O0lBaUJIUSxTQUFTLEdBQUc7TUFDUixJQUFJQyxhQUFhLEdBQUd4TSxNQUFNLENBQUN5TSxXQUEzQjs7TUFDQSxJQUFJRCxhQUFhLElBQUksQ0FBckIsRUFBd0I7UUFDcEIsS0FBS1QsT0FBTCxHQUFlLElBQWY7UUFDQSxLQUFLQyxNQUFMLEdBQWMsSUFBZDtNQUNIOztNQUVELElBQUlRLGFBQWEsR0FBRyxLQUFLUCxVQUFyQixJQUFtQyxLQUFLRixPQUFMLEtBQWlCLEtBQXhELEVBQStEO1FBQzNELEtBQUtBLE9BQUwsR0FBZSxJQUFmO1FBQ0EsS0FBS0MsTUFBTCxHQUFjLEtBQWQ7TUFDSCxDQUhELE1BR08sSUFBSVEsYUFBYSxHQUFHLEtBQUtQLFVBQXJCLElBQW1DLEtBQUtGLE9BQUwsS0FBaUIsSUFBeEQsRUFBOEQ7UUFDakUsS0FBS0EsT0FBTCxHQUFlLEtBQWY7UUFDQSxLQUFLQyxNQUFMLEdBQWMsSUFBZDtNQUNIOztNQUNELEtBQUtDLFVBQUwsR0FBa0JPLGFBQWxCO0lBQ0g7O0VBaENFLENBQVA7QUFrQ0g7Ozs7Ozs7Ozs7Ozs7Ozs7O0FDbkNEO0FBRUFsTix1RUFBQSxHQUFpQyxJQUFqQztBQUNBQSxzRUFBQSxHQUFnQyxXQUFoQztBQUNBQSxzRUFBQSxHQUFnQyxhQUFoQyxFQUNBOztBQUNBQSwrREFBQSxHQUF5QixLQUF6QjtBQUVBLGlFQUFlQSw4Q0FBZjs7Ozs7Ozs7Ozs7O0FDUkE7Ozs7Ozs7Ozs7O0FDQUEiLCJzb3VyY2VzIjpbIndlYnBhY2s6Ly9weXRob24td2VicGFjay1ib2lsZXJwbGF0ZS8uL3NyYy9hcHBsaWNhdGlvbi9hcHAuanMiLCJ3ZWJwYWNrOi8vcHl0aG9uLXdlYnBhY2stYm9pbGVycGxhdGUvLi9zcmMvY29tcG9uZW50cy9BY2NvdW50Rm9ybS5qcyIsIndlYnBhY2s6Ly9weXRob24td2VicGFjay1ib2lsZXJwbGF0ZS8uL3NyYy9jb21wb25lbnRzL0NvbnRhY3RGb3JtLmpzIiwid2VicGFjazovL3B5dGhvbi13ZWJwYWNrLWJvaWxlcnBsYXRlLy4vc3JjL2NvbXBvbmVudHMvU3RpY2t5TmF2LmpzIiwid2VicGFjazovL3B5dGhvbi13ZWJwYWNrLWJvaWxlcnBsYXRlLy4vc3JjL2NvbXBvbmVudHMvYXhpb3NGYWN0b3J5LmpzIiwid2VicGFjazovL3B5dGhvbi13ZWJwYWNrLWJvaWxlcnBsYXRlLy4vc3JjL3N0eWxlcy9pbmRleC5zY3NzPzBiODgiLCJ3ZWJwYWNrOi8vcHl0aG9uLXdlYnBhY2stYm9pbGVycGxhdGUvaWdub3JlZHwvaG9tZS9kYXJrY29kci93d3cvZGFya2NvZHIvZHJvcHNyaWRlL2Zyb250ZW5kL25vZGVfbW9kdWxlcy9ibi5qcy9saWJ8YnVmZmVyIl0sInNvdXJjZXNDb250ZW50IjpbIi8vIFRoaXMgaXMgZ2xvYmFsIGltcG9ydHMgZm9yIGNzcyBhbmQgamF2YXNjcmlwdHMgLy9cbi8vLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLVxuaW1wb3J0IFwiLi4vc3R5bGVzL2luZGV4LnNjc3NcIjtcbmltcG9ydCBodG14IGZyb20gXCJodG14Lm9yZy9kaXN0L2h0bXhcIjtcbmltcG9ydCBBbHBpbmUgZnJvbSBcImFscGluZWpzXCI7XG5pbXBvcnQgeyBldGhlcnMgfSBmcm9tIFwiZXRoZXJzXCI7XG5pbXBvcnQgYXhpb3MgZnJvbSBcIi4uL2NvbXBvbmVudHMvYXhpb3NGYWN0b3J5XCI7XG5pbXBvcnQgU3RpY2t5TmF2IGZyb20gXCIuLi9jb21wb25lbnRzL1N0aWNreU5hdlwiO1xuaW1wb3J0IFN3aXBlciBmcm9tIFwic3dpcGVyXCI7XG5pbXBvcnQgeyBkZXRlY3QgfSBmcm9tIFwiZGV0ZWN0LWJyb3dzZXJcIjtcbmltcG9ydCBcIml6aXRvYXN0L2Rpc3QvY3NzL2l6aVRvYXN0Lm1pbi5jc3NcIjtcbmltcG9ydCBcIkBsb3R0aWVmaWxlcy9sb3R0aWUtcGxheWVyXCI7XG5pbXBvcnQgaXppVG9hc3QgZnJvbSBcIml6aXRvYXN0L2Rpc3QvanMvaXppVG9hc3QubWluLmpzXCI7XG5pbXBvcnQgYW5pbWUgZnJvbSBcImFuaW1lanMvbGliL2FuaW1lLmVzLmpzXCI7XG5pbXBvcnQgU2Nyb2xsTWFnaWMgZnJvbSBcInNjcm9sbG1hZ2ljXCI7XG5pbXBvcnQgQ29udGFjdEZvcm0gZnJvbSBcIi4uL2NvbXBvbmVudHMvQ29udGFjdEZvcm1cIjtcbmltcG9ydCBBY2NvdW50Rm9ybSBmcm9tIFwiLi4vY29tcG9uZW50cy9BY2NvdW50Rm9ybVwiO1xuaW1wb3J0IGxvdHRpZXdlYiBmcm9tIFwibG90dGllLXdlYlwiO1xuXG4vLyBpbXBvcnQgeyBpbml0aWFsaXplQXBwIH0gZnJvbSBcImZpcmViYXNlL2FwcFwiO1xuLy8gaW1wb3J0IHsgZ2V0QW5hbHl0aWNzIH0gZnJvbSBcImZpcmViYXNlL2FuYWx5dGljc1wiO1xuLy8tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tXG5cbi8vIEdsb2JhbCBJbml0aWFsaXphdGlvbnMgZm9yIGltcG9ydGVkbGlicmFyaWVzIC8vXG4vLy0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS1cbi8vIGluaXRpYWxpemUgaHRteFxud2luZG93Lmh0bXggPSBodG14O1xuLy8gaW5pdGlhbGl6ZSBsb3R0aWUgd2ViIGFuZCBsb3R0aWUgcGxheWVyXG53aW5kb3cubG90dGlld2ViID0gbG90dGlld2ViO1xuLy8gaW5pdGlhbGl6ZSBhbmltZWpzXG53aW5kb3cuYW5pbWUgPSBhbmltZTtcbndpbmRvdy5zY3JvbGxNYWdpYyA9IFNjcm9sbE1hZ2ljO1xuLy8gaW5pdGlhbGl6ZSBldGhlciBqcyBmb3IgY3J5cHRvIHBheW1lbnRcbndpbmRvdy5ldGhlcnMgPSBldGhlcnM7XG4vLyBpbml0aWFsaXplIGF4aW9zIGFzeW5jIHBvc3R8Z2V0IHJlcXVlc3RcbndpbmRvdy5heGlvcyA9IGF4aW9zO1xuLy8gaW5pdGlhbGl6ZSBzd2lwZXIuanNcbndpbmRvdy5Td2lwZXIgPSBTd2lwZXI7XG4vLyBpbml0aWFpbGl6ZSBpeml0b2FzdCBhbGVydHNcbndpbmRvdy5peml0b2FzdCA9IGl6aVRvYXN0O1xuLy8gQWxwaW5lIEpTIFNjcmlwdHNcbndpbmRvdy5BbHBpbmUgPSBBbHBpbmU7XG5BbHBpbmUuZGF0YShcIlN0aWNreU5hdlwiLCBTdGlja3lOYXYpO1xuQWxwaW5lLmRhdGEoXCJDb250YWN0Rm9ybVwiLCBDb250YWN0Rm9ybSk7XG5BbHBpbmUuZGF0YShcIkFjY291bnRGb3JtXCIsIEFjY291bnRGb3JtKTtcbkFscGluZS5zdGFydCgpO1xuLy8tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tXG5cbi8vIHNldCBzZXJ2aWNlIHdvcmtlciBsaW5rIGFuZCBzY29wZSBzdGFydCBsaW5rXG4vLy0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS1cbmNvbnN0IHN3ID0gXCIvc3cuanNcIjtcbmNvbnN0IGhvbWUgPSBcIi9cIjtcbi8vIGRldGVjdCBicm93c2VyIHR5cGVcbmNvbnN0IGJyb3dzZXIgPSBkZXRlY3QoKTtcbi8vLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLVxuXG4vLyBjb25zdCBmaXJlYmFzZUNvbmZpZyA9IHtcbi8vICAgYXBpS2V5OiBcIkFJemFTeUNDOWoycXdxaDFSZ0U3UVMyUTJMb1dCRVZ1X3AtU3dtc1wiLFxuLy8gICBhdXRoRG9tYWluOiBcImRyb3BzcmlkZS5maXJlYmFzZWFwcC5jb21cIixcbi8vICAgcHJvamVjdElkOiBcImRyb3BzcmlkZVwiLFxuLy8gICBzdG9yYWdlQnVja2V0OiBcImRyb3BzcmlkZS5hcHBzcG90LmNvbVwiLFxuLy8gICBtZXNzYWdpbmdTZW5kZXJJZDogXCI3MDgyMTgxMDQxNzBcIixcbi8vICAgYXBwSWQ6IFwiMTo3MDgyMTgxMDQxNzA6d2ViOmM4MmJkOTZjNjdkZjZkZjdhMzVkMTNcIixcbi8vICAgbWVhc3VyZW1lbnRJZDogXCJHLTFaRkVTR01WTjZcIixcbi8vIH07XG4vLyAvLyBJbml0aWFsaXplIEZpcmViYXNlXG5cbi8vIGNvbnN0IGFwcCA9IGluaXRpYWxpemVBcHAoZmlyZWJhc2VDb25maWcpO1xuLy8gY29uc3QgYW5hbHl0aWNzID0gZ2V0QW5hbHl0aWNzKGFwcCk7XG4vLyBnZXQgZ2xvYmFsIHZhcmlhYmxlcyBmcm9tIHRoZSBiYXNlLmh0bWwgZmlsZSBmb3Jcbi8vIHB1c2ggbm90aWZpY2F0aW9uIGFuZCBwd2EgaW5zdGFsbCBidXR0b25cbi8vLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLVxuY29uc3QgeyBBUFBMSUNBVElPTl9TRVJWRVJfS0VZLCBDUkVBVEVfV1BfREVWSUNFLCBTRU5EX05PVElGSUNBVElPTiB9ID0gd2luZG93LldFQl9QVVNIX0NGRztcbi8vLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLVxuXG4vLyBnZW5lcmF0ZSBrZXkgZm9yIHB1c2ggbm90aWZpY2F0aW9uc1xuLy8tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tXG5mdW5jdGlvbiB1cmxCYXNlNjRUb1VpbnQ4QXJyYXkoYmFzZTY0U3RyaW5nKSB7XG4gIC8vIGh0dHBzOi8vZ2lzdC5naXRodWIuY29tL0tsZXJpdGgvODBhYmQ3NDJkNzI2ZGQ1ODdmNGJkNWQ2YTBhYjI2YjYjZmlsZS11cmxiYXNlNjR0b3VpbnQ4YXJyYXktanNcbiAgdmFyIHBhZGRpbmcgPSBcIj1cIi5yZXBlYXQoKDQgLSAoYmFzZTY0U3RyaW5nLmxlbmd0aCAlIDQpKSAlIDQpO1xuICB2YXIgYmFzZTY0ID0gKGJhc2U2NFN0cmluZyArIHBhZGRpbmcpLnJlcGxhY2UoL1xcLS9nLCBcIitcIikucmVwbGFjZSgvXy9nLCBcIi9cIik7XG5cbiAgdmFyIHJhd0RhdGEgPSB3aW5kb3cuYXRvYihiYXNlNjQpO1xuICB2YXIgb3V0cHV0QXJyYXkgPSBuZXcgVWludDhBcnJheShyYXdEYXRhLmxlbmd0aCk7XG5cbiAgZm9yICh2YXIgaSA9IDA7IGkgPCByYXdEYXRhLmxlbmd0aDsgKytpKSB7XG4gICAgb3V0cHV0QXJyYXlbaV0gPSByYXdEYXRhLmNoYXJDb2RlQXQoaSk7XG4gIH1cbiAgcmV0dXJuIG91dHB1dEFycmF5O1xuXG4gIC8vIGNvbnN0IG91dHB1dERhdGEgPSBvdXRwdXRBcnJheS5tYXAoKG91dHB1dCwgaW5kZXgpID0+XG4gIC8vICAgcmF3RGF0YS5jaGFyQ29kZUF0KGluZGV4KVxuICAvLyApO1xuICAvLyByZXR1cm4gb3V0cHV0RGF0YTtcbn1cbi8vLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLVxuXG4vLyB0aGlzIGlzIHRvIHN1YnNjcmliZSB0byBwdXNoIG5vdGlmaWNhdGlvbiBmcm9tIHRoZSBicm93c2VyIHRvIHRoZSBzZXJ2ZXJcbi8vLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLVxuZnVuY3Rpb24gc2F2ZVN1YnNjcmliZU9iaihzdWJzY3JpcHRpb24pIHtcbiAgLy8gc2F2ZSBzdWJzY3JpcHRpb24gdG8gdGhlIHNlcnZlclxuICBjb25zdCBzdWJzY3JpcHRpb25Kc29uID0gc3Vic2NyaXB0aW9uLnRvSlNPTigpO1xuICBjb25zdCBlbmRwb2ludFBhcnRzID0gc3Vic2NyaXB0aW9uSnNvbi5lbmRwb2ludC5zcGxpdChcIi9cIik7XG4gIGNvbnN0IHJlZ2lzdHJhdGlvbklkID0gZW5kcG9pbnRQYXJ0c1tlbmRwb2ludFBhcnRzLmxlbmd0aCAtIDFdO1xuXG4gIGNvbnN0IHByZWRhdGEgPSB7XG4gICAgc3RhdHVzX3R5cGU6IFwic3Vic2NyaWJlXCIsXG4gICAgc3Vic2NyaXB0aW9uOiBzdWJzY3JpcHRpb25Kc29uLFxuICAgIGJyb3dzZXI6IGJyb3dzZXIubmFtZS50b0xvd2VyQ2FzZSgpLFxuICAgIHAyNTZkaDogc3Vic2NyaXB0aW9uSnNvbi5rZXlzLnAyNTZkaCxcbiAgICBhdXRoOiBzdWJzY3JpcHRpb25Kc29uLmtleXMuYXV0aCxcbiAgICB1c2VyX2FnZW50OiBuYXZpZ2F0b3IuZ2V0VXNlckFnZW50LFxuICAgIHJlZ2lzdHJhdGlvbl9pZDogcmVnaXN0cmF0aW9uSWQsXG4gICAgZ3JvdXA6IFwidXNlcnNcIixcbiAgfTtcblxuICBjb25zdCBkYXRhID0gSlNPTi5zdHJpbmdpZnkocHJlZGF0YSk7XG5cbiAgYXhpb3NcbiAgICAucG9zdChDUkVBVEVfV1BfREVWSUNFLCBkYXRhLCB7XG4gICAgICBoZWFkZXJzOiB7XG4gICAgICAgIFwiQ29udGVudC1UeXBlXCI6IFwiYXBwbGljYXRpb24vanNvblwiLFxuICAgICAgfSxcbiAgICB9KVxuICAgIC50aGVuKGZ1bmN0aW9uIChyZXNwb25zZSkge1xuICAgICAgaWYgKHByb2Nlc3MuZW52Lk5PREVfRU5WID09PSBcImRldmVsb3BtZW50XCIpIHtcbiAgICAgICAgLy8gY29uc29sZS5sb2cocmVzcG9uc2UpO1xuICAgICAgICAvLyBpemlUb2FzdC5zdWNjZXNzKHtcbiAgICAgICAgLy8gICB0aXRsZTogXCJbUFVTSCBOT1RJRklDQVRJT04gU0VSVkVSXVwiLFxuICAgICAgICAvLyAgIGJhbGxvb246IHRydWUsXG4gICAgICAgIC8vICAgcG9zaXRpb246IFwidG9wUmlnaHRcIixcbiAgICAgICAgLy8gICBhbmltYXRlSW5zaWRlOiB0cnVlLFxuICAgICAgICAvLyAgIG1lc3NhZ2U6IGBOb3RpZmljYXRpb24gU3Vic2NyaXB0aW9uICR7cmVzcG9uc2Uuc3RhdHVzVGV4dH1gLFxuICAgICAgICAvLyB9KTtcbiAgICAgICAgY29uc3Qgc3Vic2NyaWJlTm90aWZpY2F0aW9uQnV0dG9uID0gZG9jdW1lbnQuZ2V0RWxlbWVudEJ5SWQoJ3N1YnNjcmliZU5vdGlmaWNhdGlvbkJ1dHRvbicpO1xuICAgICAgICBzdWJzY3JpYmVOb3RpZmljYXRpb25CdXR0b24uY2xhc3NMaXN0LnRvZ2dsZSgnaGlkZGVuJywgdHJ1ZSk7XG5cbiAgICAgICAgaXppVG9hc3Quc3VjY2Vzcyh7XG4gICAgICAgICAgdGl0bGU6IFwiW1BVU0ggTk9USUZJQ0FUSU9OIFNVQlNDUklQVElPTl1cIixcbiAgICAgICAgICBiYWxsb29uOiB0cnVlLFxuICAgICAgICAgIHBvc2l0aW9uOiBcInRvcFJpZ2h0XCIsXG4gICAgICAgICAgYW5pbWF0ZUluc2lkZTogdHJ1ZSxcbiAgICAgICAgICBtZXNzYWdlOiBgU3Vic2NyaXB0aW9uIFNlbnQgU3VjY2Vzc2Z1bGx5ICR7cmVzcG9uc2Uuc3RhdHVzVGV4dH1gLFxuICAgICAgICB9KTtcblxuICAgICAgLy8gaWYgc3Vic2NyaXB0aW9uIGlzIHN1Y2Nlc3NmdWxseSBzYXZlZCB0byB0aGUgc2VydmVyXG4gICAgICAvLyB0aGVuIGVuYWJsZSB0aGUgdGVzdCBub3RpZmljYXRpb24gcHVzaCBidXR0b24gdG8gYmUgdmlzaWJsZVxuICAgICAgc2V0dXBUcmlnZ2VyQnV0dG9uKHN1YnNjcmlwdGlvbik7XG5cbiAgICAgIH1cbiAgICB9KVxuICAgIC5jYXRjaChmdW5jdGlvbiAoZXJyb3IpIHtcbiAgICAgIGlmIChwcm9jZXNzLmVudi5OT0RFX0VOViA9PT0gXCJkZXZlbG9wbWVudFwiKSB7XG4gICAgICAgIGNvbnNvbGUubG9nKGVycm9yKTtcbiAgICAgICAgaXppVG9hc3QuZXJyb3Ioe1xuICAgICAgICAgIHRpdGxlOiBcIltQVVNIIE5PVElGSUNBVElPTiBTRVJWRVJdXCIsXG4gICAgICAgICAgYmFsbG9vbjogdHJ1ZSxcbiAgICAgICAgICBwb3NpdGlvbjogXCJ0b3BSaWdodFwiLFxuICAgICAgICAgIGFuaW1hdGVJbnNpZGU6IHRydWUsXG4gICAgICAgICAgbWVzc2FnZTogYE5vdGlmaWNhdGlvbiBTdWJzY3JpcHRpb24gJHtlcnJvci5tZXNzYWdlfWAsXG4gICAgICAgIH0pO1xuICAgICAgfVxuICAgIH0pO1xufVxuXG5mdW5jdGlvbiBzYXZlRHJpdmVyU3Vic2NyaWJlT2JqKHN1YnNjcmlwdGlvbikge1xuICAvLyBzYXZlIHN1YnNjcmlwdGlvbiB0byB0aGUgc2VydmVyXG4gIGNvbnN0IHN1YnNjcmlwdGlvbkpzb24gPSBzdWJzY3JpcHRpb24udG9KU09OKCk7XG4gIGNvbnN0IGVuZHBvaW50UGFydHMgPSBzdWJzY3JpcHRpb25Kc29uLmVuZHBvaW50LnNwbGl0KFwiL1wiKTtcbiAgY29uc3QgcmVnaXN0cmF0aW9uSWQgPSBlbmRwb2ludFBhcnRzW2VuZHBvaW50UGFydHMubGVuZ3RoIC0gMV07XG5cbiAgY29uc3QgcHJlZGF0YSA9IHtcbiAgICBzdGF0dXNfdHlwZTogXCJzdWJzY3JpYmVcIixcbiAgICBzdWJzY3JpcHRpb246IHN1YnNjcmlwdGlvbkpzb24sXG4gICAgYnJvd3NlcjogYnJvd3Nlci5uYW1lLnRvTG93ZXJDYXNlKCksXG4gICAgcDI1NmRoOiBzdWJzY3JpcHRpb25Kc29uLmtleXMucDI1NmRoLFxuICAgIGF1dGg6IHN1YnNjcmlwdGlvbkpzb24ua2V5cy5hdXRoLFxuICAgIHVzZXJfYWdlbnQ6IG5hdmlnYXRvci5nZXRVc2VyQWdlbnQsXG4gICAgcmVnaXN0cmF0aW9uX2lkOiByZWdpc3RyYXRpb25JZCxcbiAgICBncm91cDogXCJkcml2ZXJzXCIsXG4gIH07XG5cbiAgY29uc3QgZGF0YSA9IEpTT04uc3RyaW5naWZ5KHByZWRhdGEpO1xuXG4gIGF4aW9zXG4gICAgLnBvc3QoQ1JFQVRFX1dQX0RFVklDRSwgZGF0YSwge1xuICAgICAgaGVhZGVyczoge1xuICAgICAgICBcIkNvbnRlbnQtVHlwZVwiOiBcImFwcGxpY2F0aW9uL2pzb25cIixcbiAgICAgIH0sXG4gICAgfSlcbiAgICAudGhlbihmdW5jdGlvbiAocmVzcG9uc2UpIHtcbiAgICAgIGlmIChwcm9jZXNzLmVudi5OT0RFX0VOViA9PT0gXCJkZXZlbG9wbWVudFwiKSB7XG4gICAgICAgIGNvbnNvbGUubG9nKHJlc3BvbnNlKTtcbiAgICAgICAgaXppVG9hc3Quc3VjY2Vzcyh7XG4gICAgICAgICAgdGl0bGU6IFwiW1BVU0ggTk9USUZJQ0FUSU9OIFNFUlZFUl1cIixcbiAgICAgICAgICBiYWxsb29uOiB0cnVlLFxuICAgICAgICAgIHBvc2l0aW9uOiBcInRvcFJpZ2h0XCIsXG4gICAgICAgICAgYW5pbWF0ZUluc2lkZTogdHJ1ZSxcbiAgICAgICAgICBtZXNzYWdlOiBgTm90aWZpY2F0aW9uIFN1YnNjcmlwdGlvbiAke3Jlc3BvbnNlLnN0YXR1c1RleHR9YCxcbiAgICAgICAgfSk7XG4gICAgICB9XG4gICAgfSlcbiAgICAuY2F0Y2goZnVuY3Rpb24gKGVycm9yKSB7XG4gICAgICBpZiAocHJvY2Vzcy5lbnYuTk9ERV9FTlYgPT09IFwiZGV2ZWxvcG1lbnRcIikge1xuICAgICAgICBjb25zb2xlLmxvZyhlcnJvcik7XG4gICAgICAgIGl6aVRvYXN0LmVycm9yKHtcbiAgICAgICAgICB0aXRsZTogXCJbUFVTSCBOT1RJRklDQVRJT04gU0VSVkVSXVwiLFxuICAgICAgICAgIGJhbGxvb246IHRydWUsXG4gICAgICAgICAgcG9zaXRpb246IFwidG9wUmlnaHRcIixcbiAgICAgICAgICBhbmltYXRlSW5zaWRlOiB0cnVlLFxuICAgICAgICAgIG1lc3NhZ2U6IGBOb3RpZmljYXRpb24gU3Vic2NyaXB0aW9uICR7ZXJyb3IubWVzc2FnZX1gLFxuICAgICAgICB9KTtcbiAgICAgIH1cbiAgICB9KTtcbn1cblxuZnVuY3Rpb24gc2F2ZUNvbXBhbnlTdWJzY3JpYmVPYmooc3Vic2NyaXB0aW9uKSB7XG4gIC8vIHNhdmUgc3Vic2NyaXB0aW9uIHRvIHRoZSBzZXJ2ZXJcbiAgY29uc3Qgc3Vic2NyaXB0aW9uSnNvbiA9IHN1YnNjcmlwdGlvbi50b0pTT04oKTtcbiAgY29uc3QgZW5kcG9pbnRQYXJ0cyA9IHN1YnNjcmlwdGlvbkpzb24uZW5kcG9pbnQuc3BsaXQoXCIvXCIpO1xuICBjb25zdCByZWdpc3RyYXRpb25JZCA9IGVuZHBvaW50UGFydHNbZW5kcG9pbnRQYXJ0cy5sZW5ndGggLSAxXTtcblxuICBjb25zdCBwcmVkYXRhID0ge1xuICAgIHN0YXR1c190eXBlOiBcInN1YnNjcmliZVwiLFxuICAgIHN1YnNjcmlwdGlvbjogc3Vic2NyaXB0aW9uSnNvbixcbiAgICBicm93c2VyOiBicm93c2VyLm5hbWUudG9Mb3dlckNhc2UoKSxcbiAgICBwMjU2ZGg6IHN1YnNjcmlwdGlvbkpzb24ua2V5cy5wMjU2ZGgsXG4gICAgYXV0aDogc3Vic2NyaXB0aW9uSnNvbi5rZXlzLmF1dGgsXG4gICAgdXNlcl9hZ2VudDogbmF2aWdhdG9yLmdldFVzZXJBZ2VudCxcbiAgICByZWdpc3RyYXRpb25faWQ6IHJlZ2lzdHJhdGlvbklkLFxuICAgIGdyb3VwOiBcImRyaXZlcnNcIixcbiAgfTtcblxuICBjb25zdCBkYXRhID0gSlNPTi5zdHJpbmdpZnkocHJlZGF0YSk7XG5cbiAgYXhpb3NcbiAgICAucG9zdChDUkVBVEVfV1BfREVWSUNFLCBkYXRhLCB7XG4gICAgICBoZWFkZXJzOiB7XG4gICAgICAgIFwiQ29udGVudC1UeXBlXCI6IFwiYXBwbGljYXRpb24vanNvblwiLFxuICAgICAgfSxcbiAgICB9KVxuICAgIC50aGVuKGZ1bmN0aW9uIChyZXNwb25zZSkge1xuICAgICAgaWYgKHByb2Nlc3MuZW52Lk5PREVfRU5WID09PSBcImRldmVsb3BtZW50XCIpIHtcbiAgICAgICAgY29uc29sZS5sb2cocmVzcG9uc2UpO1xuICAgICAgICBpemlUb2FzdC5zdWNjZXNzKHtcbiAgICAgICAgICB0aXRsZTogXCJbUFVTSCBOT1RJRklDQVRJT04gU0VSVkVSXVwiLFxuICAgICAgICAgIGJhbGxvb246IHRydWUsXG4gICAgICAgICAgcG9zaXRpb246IFwidG9wUmlnaHRcIixcbiAgICAgICAgICBhbmltYXRlSW5zaWRlOiB0cnVlLFxuICAgICAgICAgIG1lc3NhZ2U6IGBOb3RpZmljYXRpb24gU3Vic2NyaXB0aW9uICR7cmVzcG9uc2Uuc3RhdHVzVGV4dH1gLFxuICAgICAgICB9KTtcbiAgICAgIH1cbiAgICB9KVxuICAgIC5jYXRjaChmdW5jdGlvbiAoZXJyb3IpIHtcbiAgICAgIGlmIChwcm9jZXNzLmVudi5OT0RFX0VOViA9PT0gXCJkZXZlbG9wbWVudFwiKSB7XG4gICAgICAgIGNvbnNvbGUubG9nKGVycm9yKTtcbiAgICAgICAgaXppVG9hc3QuZXJyb3Ioe1xuICAgICAgICAgIHRpdGxlOiBcIltQVVNIIE5PVElGSUNBVElPTiBTRVJWRVJdXCIsXG4gICAgICAgICAgYmFsbG9vbjogdHJ1ZSxcbiAgICAgICAgICBwb3NpdGlvbjogXCJ0b3BSaWdodFwiLFxuICAgICAgICAgIGFuaW1hdGVJbnNpZGU6IHRydWUsXG4gICAgICAgICAgbWVzc2FnZTogYE5vdGlmaWNhdGlvbiBTdWJzY3JpcHRpb24gJHtlcnJvci5tZXNzYWdlfWAsXG4gICAgICAgIH0pO1xuICAgICAgfVxuICAgIH0pO1xufVxuLy8tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tXG5cbi8vIHRoaXMgZnVuY3Rpb24gaXMgdG8gc2VuZCBzdWJzY3JpcHRpb24gbm90aWZpY2F0aW9uIHRvIHRoZSBzZXJ2ZXJcbi8vLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLVxuZnVuY3Rpb24gc3Vic2NyaWJlKHJlZ2lzdHJhdGlvbikge1xuICByZWdpc3RyYXRpb24ucHVzaE1hbmFnZXIuZ2V0U3Vic2NyaXB0aW9uKCkudGhlbihmdW5jdGlvbiAoc3Vic2NyaXB0aW9uKSB7XG4gICAgaWYgKHN1YnNjcmlwdGlvbikge1xuICAgICAgY29uc29sZS5sb2coXCJzdWJzY3JpcHRpb24gZXhpc3RzXCIpO1xuICAgICAgc2F2ZVN1YnNjcmliZU9iaihzdWJzY3JpcHRpb24pO1xuICAgICAgc2V0dXBUcmlnZ2VyQnV0dG9uKHN1YnNjcmlwdGlvbik7XG4gICAgICByZXR1cm47XG4gICAgfVxuICB9KTtcblxuICBjb25zdCBvcHRpb25zID0ge1xuICAgIHVzZXJWaXNpYmxlT25seTogdHJ1ZSwgLy8gcmVxdWlyZWQgYnkgY2hyb21lXG4gICAgYXBwbGljYXRpb25TZXJ2ZXJLZXk6IHVybEJhc2U2NFRvVWludDhBcnJheShBUFBMSUNBVElPTl9TRVJWRVJfS0VZKSxcbiAgfTtcblxuICByZWdpc3RyYXRpb24ucHVzaE1hbmFnZXIuc3Vic2NyaWJlKG9wdGlvbnMpLnRoZW4oXG4gICAgLy8gcmVxdWVzdGluZyB0byBzdWJzY3JpYmUgZnJvbSB0aGUgc2VydmVyXG4gICAgZnVuY3Rpb24gKHN1YnNjcmlwdGlvbikge1xuICAgICAgaWYgKHByb2Nlc3MuZW52Lk5PREVfRU5WID09PSBcImRldmVsb3BtZW50XCIpIHtcbiAgICAgICAgY29uc29sZS5sb2coYHN1YnNjcmlwdGlvbjogYCwgc3Vic2NyaXB0aW9uKTtcbiAgICAgICAgY29uc29sZS5sb2coc3Vic2NyaXB0aW9uLmVuZHBvaW50KTtcbiAgICAgIH1cblxuICAgICAgLy8gc3Vic2NyaXB0aW9uIGlzIG5vdyBzYXZlZCB0byB0aGUgc2VydmVyXG4gICAgICBzYXZlU3Vic2NyaWJlT2JqKHN1YnNjcmlwdGlvbik7XG5cbiAgICB9LFxuXG4gICAgLy8gaWYgdGhlcmUgaXMgYW4gZXJyb3IgZmlndXJlIHRoZSBlcnJvciBhbmQgdGhyb3cgYW4gYXBwcm9wcmFpdGUgZXJyb3IgbWVzc2FnZSB0b1xuICAgIC8vIHRoZSB1c2VyIHNvIGhlIGtub3dzIGV4YWN0bHkgd2hhdCBpcyB3cm9uZyBhbmQgY2FuIG1vdmUgZm9yd2FyZCBvciBhZGp1c3QgZm9yIGFcbiAgICAvLyBkZXZpY2UuXG4gICAgZnVuY3Rpb24gKGVycm9yKSB7XG4gICAgICBpZiAocHJvY2Vzcy5lbnYuTk9ERV9FTlYgPT09IFwiZGV2ZWxvcG1lbnRcIikge1xuICAgICAgICBjb25zb2xlLmxvZyhlcnJvcik7XG4gICAgICB9XG5cbiAgICAgIGl6aVRvYXN0LmVycm9yKHtcbiAgICAgICAgdGl0bGU6IFwiW1BVU0ggTk9USUZJQ0FUSU9OIFNVQlNDUklQVElPTl1cIixcbiAgICAgICAgYmFsbG9vbjogdHJ1ZSxcbiAgICAgICAgcG9zaXRpb246IFwidG9wUmlnaHRcIixcbiAgICAgICAgYW5pbWF0ZUluc2lkZTogdHJ1ZSxcbiAgICAgICAgbWVzc2FnZTogYCR7ZXJyb3J9YCxcbiAgICAgIH0pO1xuICAgIH1cbiAgKTtcbn1cblxuZnVuY3Rpb24gc3Vic2NyaWJlRHJpdmVyKHJlZ2lzdHJhdGlvbikge1xuICByZWdpc3RyYXRpb24ucHVzaE1hbmFnZXIuZ2V0U3Vic2NyaXB0aW9uKCkudGhlbihmdW5jdGlvbiAoc3Vic2NyaXB0aW9uKSB7XG4gICAgaWYgKHN1YnNjcmlwdGlvbikge1xuICAgICAgY29uc29sZS5sb2coXCJzdWJzY3JpcHRpb24gZXhpc3RzXCIpO1xuICAgICAgc2F2ZURyaXZlclN1YnNjcmliZU9iaihzdWJzY3JpcHRpb24pO1xuICAgICAgcmV0dXJuO1xuICAgIH1cbiAgfSk7XG5cbiAgY29uc3Qgb3B0aW9ucyA9IHtcbiAgICB1c2VyVmlzaWJsZU9ubHk6IHRydWUsIC8vIHJlcXVpcmVkIGJ5IGNocm9tZVxuICAgIGFwcGxpY2F0aW9uU2VydmVyS2V5OiB1cmxCYXNlNjRUb1VpbnQ4QXJyYXkoQVBQTElDQVRJT05fU0VSVkVSX0tFWSksXG4gIH07XG5cbiAgcmVnaXN0cmF0aW9uLnB1c2hNYW5hZ2VyLnN1YnNjcmliZShvcHRpb25zKS50aGVuKFxuICAgIC8vIHJlcXVlc3RpbmcgdG8gc3Vic2NyaWJlIGZyb20gdGhlIHNlcnZlclxuICAgIGZ1bmN0aW9uIChzdWJzY3JpcHRpb24pIHtcbiAgICAgIGlmIChwcm9jZXNzLmVudi5OT0RFX0VOViA9PT0gXCJkZXZlbG9wbWVudFwiKSB7XG4gICAgICAgIGNvbnNvbGUubG9nKGBzdWJzY3JpcHRpb246IGAsIHN1YnNjcmlwdGlvbik7XG4gICAgICAgIGNvbnNvbGUubG9nKHN1YnNjcmlwdGlvbi5lbmRwb2ludCk7XG4gICAgICB9XG5cbiAgICAgIC8vIHN1YnNjcmlwdGlvbiBpcyBub3cgc2F2ZWQgdG8gdGhlIHNlcnZlclxuICAgICAgc2F2ZURyaXZlclN1YnNjcmliZU9iaihzdWJzY3JpcHRpb24pO1xuXG5cbiAgICAgIGl6aVRvYXN0LnN1Y2Nlc3Moe1xuICAgICAgICB0aXRsZTogXCJbUFVTSCBOT1RJRklDQVRJT04gU1VCU0NSSVBUSU9OXVwiLFxuICAgICAgICBiYWxsb29uOiB0cnVlLFxuICAgICAgICBwb3NpdGlvbjogXCJ0b3BSaWdodFwiLFxuICAgICAgICBhbmltYXRlSW5zaWRlOiB0cnVlLFxuICAgICAgICBtZXNzYWdlOiBgU3Vic2NyaXB0aW9uIFNlbnQgU3VjY2Vzc2Z1bGx5YCxcbiAgICAgIH0pO1xuICAgIH0sXG5cbiAgICAvLyBpZiB0aGVyZSBpcyBhbiBlcnJvciBmaWd1cmUgdGhlIGVycm9yIGFuZCB0aHJvdyBhbiBhcHByb3ByYWl0ZSBlcnJvciBtZXNzYWdlIHRvXG4gICAgLy8gdGhlIHVzZXIgc28gaGUga25vd3MgZXhhY3RseSB3aGF0IGlzIHdyb25nIGFuZCBjYW4gbW92ZSBmb3J3YXJkIG9yIGFkanVzdCBmb3IgYVxuICAgIC8vIGRldmljZS5cbiAgICBmdW5jdGlvbiAoZXJyb3IpIHtcbiAgICAgIGlmIChwcm9jZXNzLmVudi5OT0RFX0VOViA9PT0gXCJkZXZlbG9wbWVudFwiKSB7XG4gICAgICAgIGNvbnNvbGUubG9nKGVycm9yKTtcbiAgICAgIH1cblxuICAgICAgaXppVG9hc3QuZXJyb3Ioe1xuICAgICAgICB0aXRsZTogXCJbUFVTSCBOT1RJRklDQVRJT04gU1VCU0NSSVBUSU9OXVwiLFxuICAgICAgICBiYWxsb29uOiB0cnVlLFxuICAgICAgICBwb3NpdGlvbjogXCJ0b3BSaWdodFwiLFxuICAgICAgICBhbmltYXRlSW5zaWRlOiB0cnVlLFxuICAgICAgICBtZXNzYWdlOiBgJHtlcnJvcn1gLFxuICAgICAgfSk7XG4gICAgfVxuICApO1xufVxuXG5mdW5jdGlvbiBzdWJzY3JpYmVDb21wYW55KHJlZ2lzdHJhdGlvbikge1xuICByZWdpc3RyYXRpb24ucHVzaE1hbmFnZXIuZ2V0U3Vic2NyaXB0aW9uKCkudGhlbihmdW5jdGlvbiAoc3Vic2NyaXB0aW9uKSB7XG4gICAgaWYgKHN1YnNjcmlwdGlvbikge1xuICAgICAgY29uc29sZS5sb2coXCJzdWJzY3JpcHRpb24gZXhpc3RzXCIpO1xuICAgICAgc2F2ZUNvbXBhbnlTdWJzY3JpYmVPYmooc3Vic2NyaXB0aW9uKTtcbiAgICAgIHJldHVybjtcbiAgICB9XG4gIH0pO1xuXG4gIGNvbnN0IG9wdGlvbnMgPSB7XG4gICAgdXNlclZpc2libGVPbmx5OiB0cnVlLCAvLyByZXF1aXJlZCBieSBjaHJvbWVcbiAgICBhcHBsaWNhdGlvblNlcnZlcktleTogdXJsQmFzZTY0VG9VaW50OEFycmF5KEFQUExJQ0FUSU9OX1NFUlZFUl9LRVkpLFxuICB9O1xuXG4gIHJlZ2lzdHJhdGlvbi5wdXNoTWFuYWdlci5zdWJzY3JpYmUob3B0aW9ucykudGhlbihcbiAgICAvLyByZXF1ZXN0aW5nIHRvIHN1YnNjcmliZSBmcm9tIHRoZSBzZXJ2ZXJcbiAgICBmdW5jdGlvbiAoc3Vic2NyaXB0aW9uKSB7XG4gICAgICBpZiAocHJvY2Vzcy5lbnYuTk9ERV9FTlYgPT09IFwiZGV2ZWxvcG1lbnRcIikge1xuICAgICAgICBjb25zb2xlLmxvZyhgc3Vic2NyaXB0aW9uOiBgLCBzdWJzY3JpcHRpb24pO1xuICAgICAgICBjb25zb2xlLmxvZyhzdWJzY3JpcHRpb24uZW5kcG9pbnQpO1xuICAgICAgfVxuXG4gICAgICAvLyBzdWJzY3JpcHRpb24gaXMgbm93IHNhdmVkIHRvIHRoZSBzZXJ2ZXJcbiAgICAgIHNhdmVDb21wYW55U3Vic2NyaWJlT2JqKHN1YnNjcmlwdGlvbik7XG5cbiAgICAgIGl6aVRvYXN0LnN1Y2Nlc3Moe1xuICAgICAgICB0aXRsZTogXCJbUFVTSCBOT1RJRklDQVRJT04gU1VCU0NSSVBUSU9OXVwiLFxuICAgICAgICBiYWxsb29uOiB0cnVlLFxuICAgICAgICBwb3NpdGlvbjogXCJ0b3BSaWdodFwiLFxuICAgICAgICBhbmltYXRlSW5zaWRlOiB0cnVlLFxuICAgICAgICBtZXNzYWdlOiBgU3Vic2NyaXB0aW9uIFNlbnQgU3VjY2Vzc2Z1bGx5YCxcbiAgICAgIH0pO1xuICAgIH0sXG5cbiAgICAvLyBpZiB0aGVyZSBpcyBhbiBlcnJvciBmaWd1cmUgdGhlIGVycm9yIGFuZCB0aHJvdyBhbiBhcHByb3ByYWl0ZSBlcnJvciBtZXNzYWdlIHRvXG4gICAgLy8gdGhlIHVzZXIgc28gaGUga25vd3MgZXhhY3RseSB3aGF0IGlzIHdyb25nIGFuZCBjYW4gbW92ZSBmb3J3YXJkIG9yIGFkanVzdCBmb3IgYVxuICAgIC8vIGRldmljZS5cbiAgICBmdW5jdGlvbiAoZXJyb3IpIHtcbiAgICAgIGlmIChwcm9jZXNzLmVudi5OT0RFX0VOViA9PT0gXCJkZXZlbG9wbWVudFwiKSB7XG4gICAgICAgIGNvbnNvbGUubG9nKGVycm9yKTtcbiAgICAgIH1cblxuICAgICAgaXppVG9hc3QuZXJyb3Ioe1xuICAgICAgICB0aXRsZTogXCJbUFVTSCBOT1RJRklDQVRJT04gU1VCU0NSSVBUSU9OXVwiLFxuICAgICAgICBiYWxsb29uOiB0cnVlLFxuICAgICAgICBwb3NpdGlvbjogXCJ0b3BSaWdodFwiLFxuICAgICAgICBhbmltYXRlSW5zaWRlOiB0cnVlLFxuICAgICAgICBtZXNzYWdlOiBgJHtlcnJvcn1gLFxuICAgICAgfSk7XG4gICAgfVxuICApO1xufVxuLy8tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tXG5cbi8vIFRoZSBmdW5jdGlvbiB0byB0cmlnZ2VyIHRoZSBwdXNoIG5vdGlmaWNhdGlvbiBmcm9tIHRoZSBicm93c2VyXG4vLy0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS1cbi8vIHN1YnNjcmliZShyZWcpO1xuZnVuY3Rpb24gc2V0dXBTdWJzY3JpYmVCdXR0b24ocmVnKSB7XG4gIGlmIChkb2N1bWVudC5nZXRFbGVtZW50QnlJZCgnc3Vic2NyaWJlTm90aWZpY2F0aW9uQnV0dG9uJykpIHtcbiAgICBjb25zdCBzdWJzY3JpYmVOb3RpZmljYXRpb25CdXR0b24gPSBkb2N1bWVudC5nZXRFbGVtZW50QnlJZCgnc3Vic2NyaWJlTm90aWZpY2F0aW9uQnV0dG9uJyk7XG4gICAgc3Vic2NyaWJlTm90aWZpY2F0aW9uQnV0dG9uLmNsYXNzTGlzdC50b2dnbGUoJ2hpZGRlbicsIGZhbHNlKTtcbiAgICBzdWJzY3JpYmVOb3RpZmljYXRpb25CdXR0b24uYWRkRXZlbnRMaXN0ZW5lcignY2xpY2snLCAoKSA9PiB7XG4gICAgICBzdWJzY3JpYmUocmVnKTtcbiAgICAgIGNvbnNvbGUubG9nKFwiU3Vic2NyaWJlIEJ1dHRvbiBTZXRcIik7XG4gICAgfSk7XG4gIH1cbn1cblxuZnVuY3Rpb24gc2V0dXBEcml2ZXJTdWJzY3JpYmVCdXR0b24ocmVnKSB7XG4gIGlmIChkb2N1bWVudC5nZXRFbGVtZW50QnlJZCgnc3Vic2NyaWJlRHJpdmVyJykpIHtcbiAgICBjb25zdCBzdWJzY3JpYmVEcml2ZXJCdXR0b24gPSBkb2N1bWVudC5nZXRFbGVtZW50QnlJZCgnc3Vic2NyaWJlRHJpdmVyJyk7XG4gICAgc3Vic2NyaWJlRHJpdmVyQnV0dG9uLmFkZEV2ZW50TGlzdGVuZXIoJ2NsaWNrJywgKCkgPT4ge1xuICAgICAgc3Vic2NyaWJlRHJpdmVyKHJlZyk7XG4gICAgfSk7XG4gIH1cbn1cblxuZnVuY3Rpb24gc2V0dXBDb21wYW55U3Vic2NyaWJlQnV0dG9uKHJlZykge1xuICBpZiAoZG9jdW1lbnQuZ2V0RWxlbWVudEJ5SWQoJ3N1YnNjcmliZUNvbXBhbnknKSkge1xuICAgIGNvbnN0IHN1YnNjcmliZUNvbXBhbnlCdXR0b24gPSBkb2N1bWVudC5nZXRFbGVtZW50QnlJZCgnc3Vic2NyaWJlQ29tcGFueScpO1xuICAgIHN1YnNjcmliZUNvbXBhbnlCdXR0b24uYWRkRXZlbnRMaXN0ZW5lcignY2xpY2snLCAoKSA9PiB7XG4gICAgICBzdWJzY3JpYmVDb21wYW55KHJlZyk7XG4gICAgfSk7XG4gIH1cbn1cblxuLy8tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tXG4vLyBUaGlzIGZ1bmN0aW9uIGlzIGZvciBhIHVzZXIgdG8gdGVzdCB0aGUgcHVzaCBub3RpZmljYXRpb25cbi8vLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLVxuZnVuY3Rpb24gc2V0dXBUcmlnZ2VyQnV0dG9uKHN1YnNjcmlwdGlvbikge1xuICBjb25zdCBzdWJKc29uID0gc3Vic2NyaXB0aW9uLnRvSlNPTigpO1xuICBjb25zdCBlbmRwb2ludFBhcnRzID0gc3ViSnNvbi5lbmRwb2ludC5zcGxpdChcIi9cIik7XG4gIGNvbnN0IHJlZ2lzdHJhdGlvbklkID0gZW5kcG9pbnRQYXJ0c1tlbmRwb2ludFBhcnRzLmxlbmd0aCAtIDFdO1xuICBjb25zdCBwcmVkYXRhID0ge1xuICAgIHJlZ2lzdHJhdGlvbl9pZDogcmVnaXN0cmF0aW9uSWQsXG4gICAgYXV0aDogc3ViSnNvbi5rZXlzLmF1dGgsXG4gICAgaGVhZDogXCJXZWxjb21lIHRvIERyb3BzcmlkZVwiLFxuICAgIGJvZHk6IFwiVGhpcyBpcyBob3cgb3VyIHB1c2ggbm90aWZpY2F0aW9ucyBzaGFsbCBiZSBhcHBlYXJpbmcgb24geW91ciBkZXZpY2UuXCIsXG4gIH07XG5cbiAgY29uc3QgZGF0YSA9IEpTT04uc3RyaW5naWZ5KHByZWRhdGEpO1xuXG4gIGF4aW9zXG4gICAgLnBvc3QoU0VORF9OT1RJRklDQVRJT04sIGRhdGEsIHtcbiAgICAgIGhlYWRlcnM6IHtcbiAgICAgICAgXCJDb250ZW50LVR5cGVcIjogXCJhcHBsaWNhdGlvbi9qc29uXCIsXG4gICAgICB9LFxuICAgIH0pXG4gICAgLnRoZW4oZnVuY3Rpb24gKHJlc3BvbnNlKSB7XG4gICAgICBpemlUb2FzdC5pbmZvKHtcbiAgICAgICAgdGl0bGU6IFwiW1BVU0ggTk9USUZJQ0FUSU9OIFRFU1QgU1VDQ0VTU0ZVTF1cIixcbiAgICAgICAgYmFsbG9vbjogdHJ1ZSxcbiAgICAgICAgcG9zaXRpb246IFwidG9wUmlnaHRcIixcbiAgICAgICAgYW5pbWF0ZUluc2lkZTogdHJ1ZSxcbiAgICAgICAgbWVzc2FnZTogcmVzcG9uc2UuZGF0YS5tZXNzYWdlLFxuICAgICAgfSk7XG4gICAgfSlcbiAgICAuY2F0Y2goZnVuY3Rpb24gKGVycm9yKSB7XG4gICAgICBpemlUb2FzdC5lcnJvcih7XG4gICAgICAgIHRpdGxlOiBcIltQVVNIIE5PVElGSUNBVElPTiBURVNUIEVSUk9SXVwiLFxuICAgICAgICBiYWxsb29uOiB0cnVlLFxuICAgICAgICBwb3NpdGlvbjogXCJ0b3BSaWdodFwiLFxuICAgICAgICBhbmltYXRlSW5zaWRlOiB0cnVlLFxuICAgICAgICBtZXNzYWdlOiBlcnJvci5yZXNwb25zZS5kYXRhLmRldGFpbCxcbiAgICAgIH0pO1xuICAgIH0pO1xuICByZXR1cm47XG59XG4vLy0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS1cbi8vIEVuZCBwdXNoIG5vdGlmaWNhdGlvbiBidXR0b25cbi8vLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLVxuXG5pZiAoZG9jdW1lbnQuZ2V0RWxlbWVudEJ5SWQoJ3NoYXJlVXJsJykpIHtcbmNvbnN0IHNoYXJlQnV0dG9uID0gZG9jdW1lbnQuZ2V0RWxlbWVudEJ5SWQoJ3NoYXJlVXJsJyk7XG5jb25zdCB1cmwgPSBzaGFyZUJ1dHRvbi5kYXRhc2V0LnVybDtcbmNvbnN0IHRpdGxlID0gZG9jdW1lbnQudGl0bGU7XG5zaGFyZUJ1dHRvbi5hZGRFdmVudExpc3RlbmVyKCdjbGljaycsICgpID0+IHtcbiAgaWYgKG5hdmlnYXRvci5zaGFyZSkge1xuICAgIG5hdmlnYXRvci5zaGFyZSh7XG4gICAgICB0aXRsZTogdGl0bGUsXG4gICAgICB0ZXh0OiBgQ2hlY2sgb3V0ICR7dGl0bGUudG9VcHBlckNhc2UoKX0uYCxcbiAgICAgIHVybDogdXJsLFxuICAgIH0pXG4gICAgICAudGhlbigoKSA9PiBpemlUb2FzdC5zdWNjZXNzKHtcbiAgICAgICAgdGl0bGU6IFwiW1NIQVJFIFBBR0VdXCIsXG4gICAgICAgIGJhbGxvb246IHRydWUsXG4gICAgICAgIHBvc2l0aW9uOiBcInRvcFJpZ2h0XCIsXG4gICAgICAgIGFuaW1hdGVJbnNpZGU6IHRydWUsXG4gICAgICAgIG1lc3NhZ2U6IGBTdWNjZXNzZnVsbHkgc2hhcmUgJHt1cmx9YCxcbiAgICAgIH0pKVxuICAgICAgLmNhdGNoKChlcnJvcikgPT4gaXppVG9hc3QuZXJyb3Ioe1xuICAgICAgICB0aXRsZTogXCJbU0hBUkUgUEFHRSBFUlJPUl1cIixcbiAgICAgICAgYmFsbG9vbjogdHJ1ZSxcbiAgICAgICAgcG9zaXRpb246IFwidG9wUmlnaHRcIixcbiAgICAgICAgYW5pbWF0ZUluc2lkZTogdHJ1ZSxcbiAgICAgICAgbWVzc2FnZTogZXJyb3IsXG4gICAgICB9KSk7XG4gICAgfVxufSk7XG59XG5cbi8vLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLVxuXG4vLyBlbmFibGUgc2VydmljZSB3b3JrZXIsIHRoZW4gd2hlbiBzZXJ2aWNlIHdvcmtlciBpcyBlbmFibGVkIHJlcXVlc3Rcbi8vIHBlcm1pc3Npb24gZm9yIHB1c2ggbm90aWZpY2F0aW9uIGFuZCBsb2NhdGlvbiBzZXJ2aWNlcyBmcm9tIHRoZSBicm93c2VyXG4vLy0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS1cbmlmIChcInNlcnZpY2VXb3JrZXJcIiBpbiBuYXZpZ2F0b3IpIHtcbiAgd2luZG93LmFkZEV2ZW50TGlzdGVuZXIoXCJsb2FkXCIsICgpID0+IHtcbiAgICBuYXZpZ2F0b3Iuc2VydmljZVdvcmtlclxuICAgICAgLnJlZ2lzdGVyKHN3LCB7IHNjb3BlOiBob21lIH0pXG4gICAgICAudGhlbigocmVnaXN0cmF0aW9uKSA9PiB7XG4gICAgICAgIGlmIChwcm9jZXNzLmVudi5OT0RFX0VOViA9PT0gXCJkZXZlbG9wbWVudFwiKSB7XG4gICAgICAgICAgY29uc29sZS5sb2coXCJTZXJ2aWNlIHdvcmtlciByZWdpc3RlcmF0aW9uIHN1Y2NlZWRlZDogXCIsIHJlZ2lzdHJhdGlvbik7XG4gICAgICAgIH1cblxuICAgICAgICBuYXZpZ2F0b3Iuc2VydmljZVdvcmtlci5yZWFkeS50aGVuKGZ1bmN0aW9uIChyZWdpc3RyYXRpb24pIHtcbiAgICAgICAgICBpZiAocHJvY2Vzcy5lbnYuTk9ERV9FTlYgPT09IFwiZGV2ZWxvcG1lbnRcIikge1xuICAgICAgICAgICAgY29uc29sZS5sb2coXCJTZXJ2aWNlIHdvcmtlciBpcyBhY3RpdmU6IFwiLCByZWdpc3RyYXRpb24uYWN0aXZlKTtcbiAgICAgICAgICB9XG5cbiAgICAgICAgICBpbml0aWFsaXNlU3RhdGUocmVnaXN0cmF0aW9uKTtcbiAgICAgICAgfSk7XG4gICAgICB9KVxuICAgICAgLmNhdGNoKChlcnIpID0+IHtcbiAgICAgICAgaXppVG9hc3QuZXJyb3Ioe1xuICAgICAgICAgIHRpdGxlOiBcIltTRVJWSUNFIFdPUktFUl1cIixcbiAgICAgICAgICBiYWxsb29uOiB0cnVlLFxuICAgICAgICAgIHBvc2l0aW9uOiBcInRvcFJpZ2h0XCIsXG4gICAgICAgICAgYW5pbWF0ZUluc2lkZTogdHJ1ZSxcbiAgICAgICAgICBtZXNzYWdlOiBcIlNlcnZpY2UgV29ya2VyIEZhaWxlZCB0byBSZWdpc3RlclwiLFxuICAgICAgICB9KTtcblxuICAgICAgICBpZiAocHJvY2Vzcy5lbnYuTk9ERV9FTlYgPT09IFwiZGV2ZWxvcG1lbnRcIikge1xuICAgICAgICAgIGNvbnNvbGUubG9nKGVycik7XG4gICAgICAgIH1cbiAgICAgIH0pO1xuICB9KTtcbn1cblxuY29uc3QgaW5pdGlhbGlzZVN0YXRlID0gKHJlZykgPT4ge1xuICBpZiAoIXJlZy5zaG93Tm90aWZpY2F0aW9uKSB7XG4gICAgaXppVG9hc3QuZXJyb3Ioe1xuICAgICAgdGl0bGU6IFwiW1BVU0ggVU5TVVBQT1JURURdXCIsXG4gICAgICBiYWxsb29uOiB0cnVlLFxuICAgICAgcG9zaXRpb246IFwidG9wUmlnaHRcIixcbiAgICAgIGFuaW1hdGVJbnNpZGU6IHRydWUsXG4gICAgICBtZXNzYWdlOiBcIlNob3dpbmcgPHN0cm9uZz5QVVNIIE5PVElGSUNBVElPTlM8L3N0cm9uZz4gaXMgdW5zdXBwb3J0ZWRcIixcbiAgICB9KTtcbiAgICByZXR1cm47XG4gIH1cblxuICBpZiAoTm90aWZpY2F0aW9uLnBlcm1pc3Npb24gPT09IFwiZGVuaWVkXCIpIHtcbiAgICBpemlUb2FzdC53YXJuaW5nKHtcbiAgICAgIHRpdGxlOiBcIltQVVNIIERFTklFRF1cIixcbiAgICAgIGJhbGxvb246IHRydWUsXG4gICAgICBwb3NpdGlvbjogXCJ0b3BSaWdodFwiLFxuICAgICAgYW5pbWF0ZUluc2lkZTogdHJ1ZSxcbiAgICAgIG1lc3NhZ2U6XG4gICAgICAgIFwiWW91IHByZXZlbnRlZCB1cyBmcm9tIHNod29pbmcgbm90aWZpY2F0aW9ucy4gTWFudWFsbHkgY2hlY2sgaWYgeW91IGhhdmUgcHJldmVudGVkIHB1c2ggbm90aWZjYXRpb24gZnJvbSB1cy5cIixcbiAgICB9KTtcbiAgICByZXR1cm47XG4gIH1cblxuICBpZiAoIShcIlB1c2hNYW5hZ2VyXCIgaW4gd2luZG93KSkge1xuICAgIGl6aVRvYXN0LmluZm8oe1xuICAgICAgdGl0bGU6IFwiW1BVU0ggQlJPV1NFUiBVTkFWQUlMQkFMRV1cIixcbiAgICAgIGJhbGxvb246IHRydWUsXG4gICAgICBwb3NpdGlvbjogXCJ0b3BSaWdodFwiLFxuICAgICAgYW5pbWF0ZUluc2lkZTogdHJ1ZSxcbiAgICAgIG1lc3NhZ2U6IFwiUHVzaCBub3RpZmljYXRpb24gaXMgbm90IGFsbG93ZWQgaW4geW91ciBicm93c2VyLlwiLFxuICAgIH0pO1xuICAgIHJldHVybjtcbiAgfVxuXG4gIHJlZy5wdXNoTWFuYWdlci5nZXRTdWJzY3JpcHRpb24oKS50aGVuKChzdWIpID0+IHtcbiAgICBjb25zb2xlLmxvZyhcIlJlZ2lzdHJhdGlvbiBPYmplY3RcIiwgcmVnKTtcbiAgICBpZiAoIXN1YiB8fCBzdWIgPT09IG51bGwpIHtcbiAgICAgIHNldHVwU3Vic2NyaWJlQnV0dG9uKHJlZyk7XG4gICAgfSBlbHNlIGlmKHN1YiAhPT0gbnVsbCl7XG4gICAgICBjb25zb2xlLmxvZyhcIlN1YnNjcmliZSBBbHJlYWR5IERvbmVcIik7XG4gICAgICAvLyBzZXR1cFRyaWdnZXJCdXR0b24oc3ViKTtcbiAgICAgIGl6aVRvYXN0LmluZm8oe1xuICAgICAgICB0aXRsZTogXCJbU0VSVklDRSBXT1JLRVJdXCIsXG4gICAgICAgIGJhbGxvb246IHRydWUsXG4gICAgICAgIHBvc2l0aW9uOiBcInRvcFJpZ2h0XCIsXG4gICAgICAgIGFuaW1hdGVJbnNpZGU6IHRydWUsXG4gICAgICAgIG1lc3NhZ2U6IFwiUHVzaCBub3RpZmljYXRpb24gaGFzIGFscmVhZHkgYmVlbiBzdWJzY3JpYmVkIHRvXCIsXG4gICAgICB9KTtcbiAgICB9XG4gIH0pO1xuXG4gIHNldHVwRHJpdmVyU3Vic2NyaWJlQnV0dG9uKHJlZyk7XG4gIHNldHVwQ29tcGFueVN1YnNjcmliZUJ1dHRvbihyZWcpO1xufTtcblxuLy8tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tXG5cbi8vIC0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tXG4vLyBJTlNUQUxMIEJVVFRPTiBGT1IgUFJPR1JFU1NJVkUgV0VCIEFQUExJQ0FUSU9OXG4vLyAtLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS1cbmlmIChkb2N1bWVudC5nZXRFbGVtZW50QnlJZChcImluc3RhbGxCdXR0b25cIikpe1xuICBjb25zdCBpbnN0YWxsQnV0dG9uID0gZG9jdW1lbnQuZ2V0RWxlbWVudEJ5SWQoXCJpbnN0YWxsQnV0dG9uXCIpO1xuLy8gd2hlbiBwYWdlIGxvYWRzIGZvciB0aGUgZmlyc3QgdGltZSwgaW5zdGFsbCBidXR0b24gd2lsbCBiZSB2aXNpYmxlXG4vLyBpZiB0aGUgdXNlciBoYXMgbm90IGluc3RhbGxlZCB0aGUgYXBwIG9yIFBXQS5cbndpbmRvdy5hZGRFdmVudExpc3RlbmVyKFwiYmVmb3JlaW5zdGFsbHByb21wdFwiLCAoZXZlbnQpID0+IHtcbiAgaWYgKHByb2Nlc3MuZW52Lk5PREVfRU5WID09PSBcImRldmVsb3BtZW50XCIpIHtcbiAgICBjb25zb2xlLmxvZyhcIvCfkY1bUFdBXVwiLCBcImJlZm9yZWluc3RhbGxwcm9tcHRcIiwgZXZlbnQpO1xuICB9XG4gIC8vIFN0YXNoIHRoZSBldmVudCBzbyBpdCBjYW4gYmUgdHJpZ2dlcmVkIGxhdGVyLlxuICB3aW5kb3cuZGVmZXJyZWRQcm9tcHQgPSBldmVudDtcbiAgLy8gUmVtb3ZlIHRoZSAnaGlkZGVuJyBjbGFzcyBmcm9tIHRoZSBpbnN0YWxsIGJ1dHRvbiBjb250YWluZXJcbiAgLy8gaWYgdGhlIFBXQSBoYXMgYmVlbiBpbnN0YWxsZWQsIGhpZGUgdGhlIGluc3RhbGwgYnV0dG9uIG9yIGlmIGl0IGhhcyBub3RcbiAgLy8gdGhlbiBhbGxvdyBmb3IgY2xpY2tcbiAgaW5zdGFsbEJ1dHRvbi5jbGFzc0xpc3QudG9nZ2xlKFwiaGlkZGVuXCIsIGZhbHNlKTtcbn0pO1xuXG5pbnN0YWxsQnV0dG9uLmFkZEV2ZW50TGlzdGVuZXIoXCJjbGlja1wiLCAoKSA9PiB7XG4gIGlmIChwcm9jZXNzLmVudi5OT0RFX0VOViA9PT0gXCJkZXZlbG9wbWVudFwiKSB7XG4gICAgY29uc29sZS5sb2coXCLwn5GNW1BXQV0gSW5zdGFsbCBCdXR0b24gQ2xpY2tlZFwiKTtcbiAgfVxuXG4gIGNvbnN0IHByb21wdEV2ZW50ID0gd2luZG93LmRlZmVycmVkUHJvbXB0O1xuICBpZiAoIXByb21wdEV2ZW50KSB7XG4gICAgLy8gVGhlIGRlZmVycmVkIHByb21wdCBpc24ndCBhdmFpbGFibGUuIHNvIHJldHVybiBub3RoaW5nXG4gICAgcmV0dXJuO1xuICB9XG4gIHByb21wdEV2ZW50LnByb21wdCgpO1xuICBwcm9tcHRFdmVudC51c2VyQ2hvaWNlLnRoZW4oKGNob2ljZSkgPT4ge1xuICAgIGlmIChwcm9jZXNzLmVudi5OT0RFX0VOViA9PT0gXCJkZXZlbG9wbWVudFwiKSB7XG4gICAgICBjb25zb2xlLmxvZyhcIvCfkY1bUFdBXSBVc2VyIENob2ljZTogXCIsIGNob2ljZSk7XG4gICAgfVxuICAgIC8vIGl6aVRvYXN0LnN1Y2Nlc3Moe1xuICAgIC8vICAgdGl0bGU6IGBbUFdBOiAke2Nob2ljZX1dYCxcbiAgICAvLyAgIG1lc3NhZ2U6ICfwn5GNIFlvdSBoYXZlIHN1Y2Nlc3NmdWxseSBpbnN0YWxsZWQgdGhlIHJlYWR2aWxsZSBhcHAnLFxuICAgIC8vIH0pO1xuICAgIC8vIFJlc2V0IHRoZSBkZWZlcnJlZCBwcm9tcHQgdmFyaWFibGUsIHNpbmNlXG4gICAgLy8gcHJvbXB0KCkgY2FuIG9ubHkgYmUgY2FsbGVkIG9uY2UuXG4gICAgd2luZG93LmRlZmVycmVkUHJvbXB0ID0gbnVsbDtcbiAgICAvLyBIaWRlIHRoZSBpbnN0YWxsIGJ1dHRvbiBvbmNlIHRoZSBQV0EgaGFzIGJlZW4gaW5zdGFsbGVkXG4gICAgaW5zdGFsbEJ1dHRvbi5jbGFzc0xpc3QudG9nZ2xlKFwiaGlkZGVuXCIsIHRydWUpO1xuICB9KTtcbn0pO1xuLy8tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tXG59XG5cblxuLy8gaWYgYXBwIGlzIGluc3RhbGxlZCwgdGhhbmsgdGhlIHVzZXIgZm9yIGluc3RhbGxpbmcgdGhlIGFwcFxuLy8tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tXG53aW5kb3cuYWRkRXZlbnRMaXN0ZW5lcihcImFwcGluc3RhbGxlZFwiLCAoZXZlbnQpID0+IHtcbiAgaWYgKHByb2Nlc3MuZW52Lk5PREVfRU5WID09PSBcImRldmVsb3BtZW50XCIpIHtcbiAgICBjb25zb2xlLmxvZyhcIvCfkY1bUFdBXSBJbnN0YWxsZWQgU3RhdGU6IFwiLCBldmVudCk7XG4gIH1cblxuICBpemlUb2FzdC5pbmZvKHtcbiAgICB0aXRsZTogYFtTRVJWSUNFIFdPUktFUl1gLFxuICAgIGJhbGxvb246IHRydWUsXG4gICAgcG9zaXRpb246IFwidG9wUmlnaHRcIixcbiAgICBhbmltYXRlSW5zaWRlOiB0cnVlLFxuICAgIG1lc3NhZ2U6IFwiRHJvcHNyaWRlIEFwcHJlY2lhdGVzIFlvdXIgU3VwcG9ydC5cIixcbiAgfSk7XG59KTtcbi8vLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLVxuXG5cblxuLy8gSFRNWCBDb25zb2xlIGxvZ3NcbmlmIChwcm9jZXNzLmVudi5OT0RFX0VOViA9PT0gXCJkZXZlbG9wbWVudFwiKSB7XG4gIC8vIGVuYWJsZSBsb2dnaW5nIGZvciBodG14IGluIGRldmVsb3BtZW50IHNlcnZlciBvbmx5XG4gIHdpbmRvdy5odG14LmxvZ0FsbCgpO1xufVxuXG5bXG4gIFwiaHRteDpvbkxvYWRcIixcbiAgXCJodG14OmxvYWRcIixcbiAgXCJsb2FkXCIsXG4gIFwiaHRteDphZnRlclN3YXBcIixcbiAgXCJodG14OmFmdGVyT25Mb2FkXCIsXG4gIFwiaHRteDphZnRlclJlcXVlc3RcIixcbl0uZm9yRWFjaCgoZXZ0KSA9PiB7XG4gIHdpbmRvdy5hZGRFdmVudExpc3RlbmVyKGV2dCwgZnVuY3Rpb24gKCkge1xuXG4gICAgY29uc3QgY291bnRlcnMgPSBkb2N1bWVudC5xdWVyeVNlbGVjdG9yQWxsKFwiLmNvdW50ZXJcIik7XG4gICAgY29uc3QgY2FyID0gZG9jdW1lbnQuZ2V0RWxlbWVudEJ5SWQoJ2NhcicpO1xuXG4gICAgY29uc3QgY29udHJvbGxlciA9IG5ldyBTY3JvbGxNYWdpYy5Db250cm9sbGVyKCk7XG5cbiAgICAvLyBpZihkb2N1bWVudC5nZXRFbGVtZW50QnlJZCgnY29uc3QnKSl7XG4gICAgLy8gICBsb3R0aWV3ZWIubG9hZEFuaW1hdGlvbih7XG4gICAgLy8gICAgIGNvbnRhaW5lcjogZG9jdW1lbnQuZ2V0RWxlbWVudEJ5SWQoJ2NvbnN0JyksXG4gICAgLy8gICAgIHBhdGg6IFwiL3N0YXRpYy92ZW5kb3JzL2ltYWdlcy9sb3R0aWUvdW5kZXItY29uc3RydWN0aW9uLmpzb25cIixcbiAgICAvLyAgICAgcmVuZGVyZXI6ICdzdmcnLFxuICAgIC8vICAgICBsb29wOiB0cnVlLFxuICAgIC8vICAgICBhdXRvUGxheTogdHJ1ZSxcbiAgICAvLyAgICAgbmFtZTogJ1VuZGVyIENvbnN0cnVjdGlvbidcbiAgICAvLyAgIH0pO1xuICAgIC8vIH1cblxuICAgIGZ1bmN0aW9uIHN0YXJ0Q291bnRpbmcoKSB7XG4gICAgICBpZiAoY291bnRlcnMpIHtcbiAgICAgICAgY291bnRlcnMuZm9yRWFjaCgoY291bnRlcikgPT4ge1xuICAgICAgICAgIGFuaW1lKHtcbiAgICAgICAgICAgIHRhcmdldHM6IGNvdW50ZXIsXG4gICAgICAgICAgICBpbm5lckhUTUw6IFswLCBjb3VudGVyLmdldEF0dHJpYnV0ZShcImRhdGEtY291bnRcIildLFxuICAgICAgICAgICAgZWFzaW5nOiBcImVhc2VJbk91dFNpbmVcIixcbiAgICAgICAgICAgIHJvdW5kOiAxLFxuICAgICAgICAgICAgZHVyYXRpb246IDQwMDAsXG4gICAgICAgICAgfSk7XG4gICAgICAgIH0pO1xuICAgICAgfVxuICAgIH1cblxuICAgIGZ1bmN0aW9uIGFuaW1hdGVIb3dzKCkge1xuICAgICAgaWYgKGRvY3VtZW50LnF1ZXJ5U2VsZWN0b3JBbGwoJy5ob3cnKSkge1xuICAgICAgICBhbmltZSh7XG4gICAgICAgICAgdGFyZ2V0czogXCIuaG93XCIsXG4gICAgICAgICAgdHJhbnNsYXRlWDogNTYsXG4gICAgICAgICAgZWFzaW5nOiBcImVhc2VJbk91dFNpbmVcIixcbiAgICAgICAgICBkdXJhdGlvbjogODAwLFxuICAgICAgICAgIG9wYWNpdHk6IDEsXG4gICAgICAgICAgZGVsYXk6IGFuaW1lLnN0YWdnZXIoMjAwLCB7IHN0YXJ0OiA1MDAgfSksXG4gICAgICAgIH0pO1xuICAgICAgfVxuICAgIH1cblxuICAgIGlmKGRvY3VtZW50LmdldEVsZW1lbnRCeUlkKCdjb3VudFRyaWdnZXInKSkge1xuICAgICAgbmV3IFNjcm9sbE1hZ2ljLlNjZW5lKHtcbiAgICAgICAgdHJpZ2dlckVsZW1lbnQ6ICcjY291bnRUcmlnZ2VyJyxcbiAgICAgICAgdHJpZ2dlckhvb2s6ICdvbkVudGVyJyxcbiAgICAgICAgZHVyYXRpb246ICcxMDAlJyxcbiAgICAgICAgcmV2ZXJzZTogZmFsc2UsXG4gICAgICAgIG9mZnNldDogNTBcbiAgICAgIH0pLm9uKCdlbnRlcicsIGZ1bmN0aW9uKCkge1xuICAgICAgICBzdGFydENvdW50aW5nKCk7XG4gICAgICB9KS5hZGRUbyhjb250cm9sbGVyKTtcbiAgICB9XG5cbiAgICBpZihkb2N1bWVudC5nZXRFbGVtZW50QnlJZCgndHJhY2snKSkge1xuICAgICAgICBuZXcgU2Nyb2xsTWFnaWMuU2NlbmUoe1xuICAgICAgICB0cmlnZ2VyRWxlbWVudDogJyN0cmFjaycsXG4gICAgICAgIHRyaWdnZXJIb29rOiAnb25FbnRlcicsXG4gICAgICAgIGR1cmF0aW9uOiAnMTAwJScsXG4gICAgICAgIHJldmVyc2U6IHRydWUsXG4gICAgICAgIG9mZnNldDogNTBcbiAgICAgIH0pLm9uKCdlbnRlcicsIGZ1bmN0aW9uKCkge1xuICAgICAgICBjYXJEcml2ZSgpO1xuICAgICAgfSkuYWRkVG8oY29udHJvbGxlcik7XG4gICAgfVxuXG5cbiAgICBpZihkb2N1bWVudC5nZXRFbGVtZW50QnlJZCgnaG93cycpKSB7XG4gICAgICBuZXcgU2Nyb2xsTWFnaWMuU2NlbmUoe1xuICAgICAgICB0cmlnZ2VyRWxlbWVudDogJyNob3dzJyxcbiAgICAgICAgdHJpZ2dlckhvb2s6ICdvbkVudGVyJyxcbiAgICAgICAgZHVyYXRpb246ICcxMDAlJyxcbiAgICAgICAgcmV2ZXJzZTogZmFsc2UsXG4gICAgICAgIG9mZnNldDogMTAwXG4gICAgICB9KS5vbignZW50ZXInLCBmdW5jdGlvbigpIHtcbiAgICAgICAgYW5pbWF0ZUhvd3MoKTtcbiAgICAgIH0pLmFkZFRvKGNvbnRyb2xsZXIpO1xuICAgIH1cblxuICAgIGlmKGRvY3VtZW50LnF1ZXJ5U2VsZWN0b3JBbGwoJy5pbnRybycpKSB7XG4gICAgICBhbmltZSh7XG4gICAgICAgIHRhcmdldHM6IFwiLmludHJvXCIsXG4gICAgICAgIHRyYW5zbGF0ZVg6IC01NixcbiAgICAgICAgZWFzaW5nOiBcImVhc2VJbk91dFNpbmVcIixcbiAgICAgICAgZHVyYXRpb246IDgwMCxcbiAgICAgICAgb3BhY2l0eTogMSxcbiAgICAgICAgZGVsYXk6IGFuaW1lLnN0YWdnZXIoMjAwLCB7IHN0YXJ0OiA1MDAgfSksXG4gICAgICB9KTtcbiAgICB9XG5cblxuICAgIGZ1bmN0aW9uIGNhckRyaXZlKCkge1xuICAgICAgaWYgKGNhcikge1xuICAgICAgICBhbmltZSh7XG4gICAgICAgICAgdGFyZ2V0czogXCIjY2FyXCIsXG4gICAgICAgICAgdHJhbnNsYXRlWDoge1xuICAgICAgICAgICAgdmFsdWU6IFwiLTEwMHZ3XCIsXG4gICAgICAgICAgICBkdXJhdGlvbjogNTAwMCxcbiAgICAgICAgICB9LFxuICAgICAgICAgIGVhc2luZzogXCJlYXNlSW5PdXRTaW5lXCIsXG4gICAgICAgICAgb3BhY2l0eTogMSxcbiAgICAgICAgICBkZWxheTogYW5pbWUuc3RhZ2dlcigyMDAsIHsgc3RhcnQ6IDUwMCB9KSxcbiAgICAgICAgICBkaXJlY3Rpb246IFwibm9ybWFsXCIsXG4gICAgICAgICAgbG9vcDogZmFsc2UsXG4gICAgICAgIH0pO1xuICAgICAgfVxuICAgIH1cbiAgfSk7XG59KTtcbiIsImltcG9ydCBheGlvcyBmcm9tIFwiLi9heGlvc0ZhY3RvcnlcIjtcbmltcG9ydCBodG14IGZyb20gXCJodG14Lm9yZy9kaXN0L2h0bXhcIjtcbmltcG9ydCBpemlUb2FzdCBmcm9tICdpeml0b2FzdC9kaXN0L2pzL2l6aVRvYXN0Lm1pbi5qcyc7ICAvLyB5b3UgaGF2ZSBhY2Nlc3MgdG8gaXppVG9hc3Qgbm93XG5cblxuZnVuY3Rpb24gc2xlZXAobXMpIHtcbiAgICByZXR1cm4gbmV3IHdpbmRvdy5Qcm9taXNlKHJlc29sdmUgPT4gc2V0VGltZW91dChyZXNvbHZlLCBtcykpO1xufVxuXG5mdW5jdGlvbiB2YWxpZGF0ZUZpZWxkKGZvcm1FbGVtZW50LCBmaWVsZEVsZW1lbnQpIHtcbiAgICBsZXQgZm9ybURhdGEgPSBuZXcgRm9ybURhdGEoZm9ybUVsZW1lbnQpO1xuICAgIGZvcm1EYXRhLmFwcGVuZChcIl9fZmllbGRfbmFtZV9fXCIsIGZpZWxkRWxlbWVudC5uYW1lKTtcblxuICAgIGF4aW9zLnBvc3QoZm9ybUVsZW1lbnQuYWN0aW9uLCBmb3JtRGF0YSkudGhlbihmdW5jdGlvbiAocmVzcG9uc2UpIHtcbiAgICAgIGxldCBlcnJvcnMgPSByZXNwb25zZS5kYXRhLmVycm9ycztcbiAgICAgIGxldCBlcnJvcnNXcmFwcGVyRWxlbWVudCA9IGRvY3VtZW50LmdldEVsZW1lbnRCeUlkKGBlcnJvci13cmFwcGVyLSR7ZmllbGRFbGVtZW50Lm5hbWV9YCk7XG4gICAgICBpZiAoZXJyb3JzLmxlbmd0aCA9PT0gMCkge1xuICAgICAgICBkb2N1bWVudC5nZXRFbGVtZW50QnlJZCgnc3VibWl0Rm9ybScpLmNsYXNzTGlzdC5yZW1vdmUoJ2hpZGRlbicpO1xuICAgICAgICBlcnJvcnNXcmFwcGVyRWxlbWVudC5jbGFzc0xpc3QuYWRkKCdoaWRkZW4nKTtcbiAgICAgICAgaWYgKGVycm9yc1dyYXBwZXJFbGVtZW50KSB7XG4gICAgICAgICAgZXJyb3JzV3JhcHBlckVsZW1lbnQuaW5uZXJIVE1MID0gXCJcIjtcbiAgICAgICAgfVxuICAgICAgfSBlbHNlIHtcbiAgICAgICAgZG9jdW1lbnQuZ2V0RWxlbWVudEJ5SWQoJ3N1Ym1pdEZvcm0nKS5jbGFzc0xpc3QuYWRkKCdoaWRkZW4nKTtcbiAgICAgICAgZXJyb3JzV3JhcHBlckVsZW1lbnQuY2xhc3NMaXN0LnJlbW92ZSgnaGlkZGVuJyk7XG4gICAgICAgIGVycm9yc1dyYXBwZXJFbGVtZW50LmNsYXNzTGlzdC5hZGQoJ2ZsZXgnKTtcbiAgICAgICAgaWYgKGVycm9yc1dyYXBwZXJFbGVtZW50KSB7XG4gICAgICAgICAgbGV0IGVycm9yc0h0bWwgPSAnJztcbiAgICAgICAgICBmb3IgKGxldCBpID0gMDsgaSA8IGVycm9ycy5sZW5ndGg7IGkrKykge1xuICAgICAgICAgICAgZXJyb3JzSHRtbCArPSBgJHtlcnJvcnNbaV19YDtcbiAgICAgICAgICB9XG4gICAgICAgICAgZXJyb3JzV3JhcHBlckVsZW1lbnQuaW5uZXJIVE1MID0gZXJyb3JzSHRtbDtcbiAgICAgICAgfVxuICAgICAgfVxuICAgIH0pO1xuICB9XG5cblxuZXhwb3J0IGRlZmF1bHQgZnVuY3Rpb24gQWNjb3VudEZvcm0oKSB7XG4gICAgcmV0dXJuIHtcbiAgICAgICAgcHJvY2Vzc2luZzogZmFsc2UsXG5cbiAgICAgICAgYXN5bmMgc3VibWl0Rm9ybSgpIHtcbiAgICAgICAgICAgIHRoaXMucHJvY2Vzc2luZyA9IHRydWU7XG5cbiAgICAgICAgICAgIGNvbnN0IGZvcm1FbGVtZW50ID0gdGhpcy4kcmVmcy5mb3JtO1xuICAgICAgICAgICAgY29uc3QgZGl2ID0gZG9jdW1lbnQuZ2V0RWxlbWVudEJ5SWQoJ2Zvcm0nKTtcbiAgICAgICAgICAgIGNvbnN0IGFjdGlvbiA9IGZvcm1FbGVtZW50LmFjdGlvbjtcbiAgICAgICAgICAgIGNvbnN0IHJlZGlyZWN0ID0gZm9ybUVsZW1lbnQuZGF0YXNldC5yZWRpcmVjdDtcbiAgICAgICAgICAgIGNvbnN0IGNzcmYgPSBmb3JtRWxlbWVudC5kYXRhc2V0LmNzcmY7XG4gICAgICAgICAgICBsZXQgZGF0YSA9IG5ldyBGb3JtRGF0YShmb3JtRWxlbWVudCk7XG4gICAgICAgICAgICBmb3JtRWxlbWVudC5xdWVyeVNlbGVjdG9yQWxsKFwiW25hbWVdXCIpLmZvckVhY2goZmllbGRFbGVtZW50ID0+IHtcbiAgICAgICAgICAgICAgICBpZiAoZmllbGRFbGVtZW50LnR5cGUgPT09IFwidGV4dGFyZWFcIikge1xuICAgICAgICAgICAgICAgICAgICBsZXQgdGV4dGFyZWEgPSBmaWVsZEVsZW1lbnQuaWQ7XG4gICAgICAgICAgICAgICAgICAgIGNvbnNvbGUubG9nKCd0ZXh0YXJlYSBjb250ZW50OiAnLCB3aW5kb3cucGFyZW50LnRpbnltY2UuZ2V0KHRleHRhcmVhKS5nZXRDb250ZW50KCkpO1xuICAgICAgICAgICAgICAgICAgICBkYXRhLmFwcGVuZChmaWVsZEVsZW1lbnQubmFtZSwgd2luZG93LnBhcmVudC50aW55bWNlLmdldCh0ZXh0YXJlYSkuZ2V0Q29udGVudCgpKTtcbiAgICAgICAgICAgICAgICB9XG5cbiAgICAgICAgICAgICAgICBpZiAoZmllbGRFbGVtZW50LnR5cGUgIT09IFwidGV4dGFyZWFcIil7XG4gICAgICAgICAgICAgICAgICAgIGRhdGEuYXBwZW5kKGZpZWxkRWxlbWVudC5uYW1lLCBmaWVsZEVsZW1lbnQudmFsdWUpO1xuICAgICAgICAgICAgICAgIH1cbiAgICAgICAgICAgIH0pO1xuXG4gICAgICAgICAgICBpZiAoZm9ybUVsZW1lbnQuY2hlY2tWYWxpZGl0eSgpKSB7XG4gICAgICAgICAgICAgICAgYXdhaXQgYXhpb3MucG9zdChhY3Rpb24sIGRhdGEsIHtcbiAgICAgICAgICAgICAgICAgICAgaGVhZGVyczoge1xuICAgICAgICAgICAgICAgICAgICAgICdYLUNTUkZUb2tlbic6IGNzcmYsXG4gICAgICAgICAgICAgICAgICAgIH19KVxuICAgICAgICAgICAgICAgICAgICAudGhlbihmdW5jdGlvbiAocmVzcG9uc2UpIHtcbiAgICAgICAgICAgICAgICAgICAgICAgIC8vIGNvbnNvbGUuaW5mbyhcIlJFU1BPTlNFIERBVEE6IFwiLCByZXNwb25zZSk7XG5cbiAgICAgICAgICAgICAgICAgICAgICAgIGlmIChyZXNwb25zZS5zdGF0dXMgPT09IDIwMCB8fCByZXNwb25zZS5zdGF0dXMgPT09IDIwMSkge1xuICAgICAgICAgICAgICAgICAgICAgICAgICAgIGRpdi5pbm5lckhUTUwgPSBgXG4gICAgICAgICAgICAgICAgICAgICAgICAgICAgJHtmb3JtRWxlbWVudH1cbiAgICAgICAgICAgICAgICAgICAgICAgICAgICBgO1xuICAgICAgICAgICAgICAgICAgICAgICAgICAgIGl6aVRvYXN0LnN1Y2Nlc3Moe1xuICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICB0aXRsZTogcmVzcG9uc2UuZGF0YS50aXRsZSxcbiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgYmFsbG9vbjogdHJ1ZSxcbiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgcG9zaXRpb246IFwidG9wUmlnaHRcIixcbiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgYW5pbWF0ZUluc2lkZTogdHJ1ZSxcbiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgbWVzc2FnZTogcmVzcG9uc2UuZGF0YS5tZXNzYWdlXG4gICAgICAgICAgICAgICAgICAgICAgICAgICAgfSk7XG4gICAgICAgICAgICAgICAgICAgICAgICAgICAgc2xlZXAoMzUwMCk7IC8vd2FpdCAxIHNlYyBhbmQgdGhlbiBodG14IHJlZGlyZWN0IGdldFxuICAgICAgICAgICAgICAgICAgICAgICAgICAgIGh0bXguYWpheCgnR0VUJywgcmVkaXJlY3QsIHt0YXJnZXQ6J21haW4nLCBzd2FwOidvdXRlckhUTUwnfSk7XG4gICAgICAgICAgICAgICAgICAgICAgICAgICAgLy8gc2xlZXAoMzUwMCk7IC8vd2FpdCAxIHNlYyBhbmQgdGhlbiBodG14IHJlZGlyZWN0IGdldFxuICAgICAgICAgICAgICAgICAgICAgICAgICAgIC8vIGxvY2F0aW9uLnJlbG9hZCgpO1xuICAgICAgICAgICAgICAgICAgICAgICAgfSBlbHNlIHtcbiAgICAgICAgICAgICAgICAgICAgICAgICAgICBpemlUb2FzdC5lcnJvcih7XG4gICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIHRpdGxlOiByZXNwb25zZS5kYXRhLnRpdGxlLFxuICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICBiYWxsb29uOiB0cnVlLFxuICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICBwb3NpdGlvbjogXCJ0b3BSaWdodFwiLFxuICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICBhbmltYXRlSW5zaWRlOiB0cnVlLFxuICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICBtZXNzYWdlOiByZXNwb25zZS5kYXRhLm1lc3NhZ2VcbiAgICAgICAgICAgICAgICAgICAgICAgICAgICB9KTtcbiAgICAgICAgICAgICAgICAgICAgICAgIH1cblxuICAgICAgICAgICAgICAgICAgICAgICAgY29uc29sZS5sb2cocmVzcG9uc2UpO1xuICAgICAgICAgICAgICAgICAgICB9KS5jYXRjaChmdW5jdGlvbiAoZXJyb3IpIHtcbiAgICAgICAgICAgICAgICAgICAgICAgIGl6aVRvYXN0LmVycm9yKHtcbiAgICAgICAgICAgICAgICAgICAgICAgICAgICB0aXRsZTogXCJGb3JtIEVycm9yXCIsXG4gICAgICAgICAgICAgICAgICAgICAgICAgICAgYmFsbG9vbjogdHJ1ZSxcbiAgICAgICAgICAgICAgICAgICAgICAgICAgICBwb3NpdGlvbjogXCJ0b3BSaWdodFwiLFxuICAgICAgICAgICAgICAgICAgICAgICAgICAgIGFuaW1hdGVJbnNpZGU6IHRydWUsXG4gICAgICAgICAgICAgICAgICAgICAgICAgICAgbWVzc2FnZTogYFNvbWV0aGluZyB3cm9uZyBoYXBwZW5lZDogJHtlcnJvcn1gXG4gICAgICAgICAgICAgICAgICAgICAgICB9KTtcbiAgICAgICAgICAgICAgICAgICAgfSk7XG4gICAgICAgICAgICAgICAgICAgIC8vIC5maW5hbGx5KGZ1bmN0aW9uICgpIHtcbiAgICAgICAgICAgICAgICAgICAgLy8gICAgIGNvbnNvbGUubG9nKFwiZmluYWxseVwiKTtcbiAgICAgICAgICAgICAgICAgICAgLy8gfSk7XG5cbiAgICAgICAgICAgICAgICB0aGlzLnByb2Nlc3NpbmcgPSBmYWxzZTtcbiAgICAgICAgICAgIH0gZWxzZSB7XG4gICAgICAgICAgICAgICAgaXppVG9hc3QuZXJyb3Ioe1xuICAgICAgICAgICAgICAgICAgICB0aXRsZTogXCJGb3JtIFNlbmRpbmcgSW5jb21wbGV0ZVwiLFxuICAgICAgICAgICAgICAgICAgICBiYWxsb29uOiB0cnVlLFxuICAgICAgICAgICAgICAgICAgICBwb3NpdGlvbjogXCJ0b3BSaWdodFwiLFxuICAgICAgICAgICAgICAgICAgICBhbmltYXRlSW5zaWRlOiB0cnVlLFxuICAgICAgICAgICAgICAgICAgICBtZXNzYWdlOiBgRm9ybSBkYXRhIGlzIG5vdCB2YWxpZC4gRW5zdXJlIHlvdSBoYXZlIGZpbGxlZCBhbGwgZmllbGRzIGFjY3VyYXRlbHkhICR7Zm9ybUVsZW1lbnQucmVwb3J0VmFsaWRpdHkoKX1gXG4gICAgICAgICAgICAgICAgfSk7XG4gICAgICAgICAgICAgICAgc2xlZXAoMjUwMCk7IC8vd2FpdCAyLjUgc2VjIGFuZCB0aGVuIGh0bXggcmVkaXJlY3QgZ2V0XG4gICAgICAgICAgICAgICAgdGhpcy5wcm9jZXNzaW5nID0gZmFsc2U7XG4gICAgICAgICAgICAgICAgaHRteC5hamF4KCdHRVQnLCByZWRpcmVjdCwge3RhcmdldDonbWFpbicsIHN3YXA6J291dGVySFRNTCd9KTtcbiAgICAgICAgICAgIH1cblxuICAgICAgICB9LFxuXG4gICAgICAgIGFzeW5jIHN1Ym1pdEZpbGVGb3JtKCkge1xuICAgICAgICAgICAgdGhpcy5wcm9jZXNzaW5nID0gdHJ1ZTtcblxuICAgICAgICAgICAgY29uc3QgZm9ybUVsZW1lbnQgPSB0aGlzLiRyZWZzLmZvcm07XG4gICAgICAgICAgICBjb25zdCBkaXYgPSBkb2N1bWVudC5nZXRFbGVtZW50QnlJZCgnZm9ybScpO1xuICAgICAgICAgICAgY29uc3QgYWN0aW9uID0gZm9ybUVsZW1lbnQuYWN0aW9uO1xuICAgICAgICAgICAgY29uc3QgcmVkaXJlY3QgPSBmb3JtRWxlbWVudC5kYXRhc2V0LnJlZGlyZWN0O1xuICAgICAgICAgICAgY29uc3QgY3NyZiA9IGZvcm1FbGVtZW50LmRhdGFzZXQuY3NyZjtcbiAgICAgICAgICAgIGxldCBkYXRhID0gbmV3IEZvcm1EYXRhKGZvcm1FbGVtZW50KTtcbiAgICAgICAgICAgIGZvcm1FbGVtZW50LnF1ZXJ5U2VsZWN0b3JBbGwoXCJbbmFtZV1cIikuZm9yRWFjaChmaWVsZEVsZW1lbnQgPT4ge1xuICAgICAgICAgICAgICAgIGlmIChmaWVsZEVsZW1lbnQudHlwZSA9PT0gXCJ0ZXh0YXJlYVwiKSB7XG4gICAgICAgICAgICAgICAgICAgIGxldCB0ZXh0YXJlYSA9IGZpZWxkRWxlbWVudC5pZDtcbiAgICAgICAgICAgICAgICAgICAgY29uc29sZS5sb2coJ3RleHRhcmVhIGNvbnRlbnQ6ICcsIHdpbmRvdy5wYXJlbnQudGlueW1jZS5nZXQodGV4dGFyZWEpLmdldENvbnRlbnQoKSk7XG4gICAgICAgICAgICAgICAgICAgIGRhdGEuYXBwZW5kKGZpZWxkRWxlbWVudC5uYW1lLCB3aW5kb3cucGFyZW50LnRpbnltY2UuZ2V0KHRleHRhcmVhKS5nZXRDb250ZW50KCkpO1xuICAgICAgICAgICAgICAgIH1cblxuICAgICAgICAgICAgICAgIGlmIChmaWVsZEVsZW1lbnQudHlwZSAhPT0gXCJ0ZXh0YXJlYVwiKXtcbiAgICAgICAgICAgICAgICAgICAgZGF0YS5hcHBlbmQoZmllbGRFbGVtZW50Lm5hbWUsIGZpZWxkRWxlbWVudC52YWx1ZSk7XG4gICAgICAgICAgICAgICAgfVxuICAgICAgICAgICAgfSk7XG5cbiAgICAgICAgICAgIGlmIChmb3JtRWxlbWVudC5jaGVja1ZhbGlkaXR5KCkpIHtcbiAgICAgICAgICAgICAgICBhd2FpdCBheGlvcy5wb3N0KGFjdGlvbiwgZGF0YSwge1xuICAgICAgICAgICAgICAgICAgICBoZWFkZXJzOiB7XG4gICAgICAgICAgICAgICAgICAgICAgJ1gtQ1NSRlRva2VuJzogY3NyZixcbiAgICAgICAgICAgICAgICAgICAgICAnQ29udGVudC1UeXBlJzonbXVsdGlwYXJ0L2Zvcm0tZGF0YSdcbiAgICAgICAgICAgICAgICAgICAgfX0pXG4gICAgICAgICAgICAgICAgICAgIC50aGVuKGZ1bmN0aW9uIChyZXNwb25zZSkge1xuICAgICAgICAgICAgICAgICAgICAgICAgLy8gY29uc29sZS5pbmZvKFwiUkVTUE9OU0UgREFUQTogXCIsIHJlc3BvbnNlKTtcblxuICAgICAgICAgICAgICAgICAgICAgICAgaWYgKHJlc3BvbnNlLnN0YXR1cyA9PT0gMjAwIHx8IHJlc3BvbnNlLnN0YXR1cyA9PT0gMjAxKSB7XG4gICAgICAgICAgICAgICAgICAgICAgICAgICAgZGl2LmlubmVySFRNTCA9IGBcbiAgICAgICAgICAgICAgICAgICAgICAgICAgICAke2Zvcm1FbGVtZW50fVxuICAgICAgICAgICAgICAgICAgICAgICAgICAgIGA7XG4gICAgICAgICAgICAgICAgICAgICAgICAgICAgaXppVG9hc3Quc3VjY2Vzcyh7XG4gICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIHRpdGxlOiByZXNwb25zZS5kYXRhLnRpdGxlLFxuICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICBiYWxsb29uOiB0cnVlLFxuICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICBwb3NpdGlvbjogXCJ0b3BSaWdodFwiLFxuICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICBhbmltYXRlSW5zaWRlOiB0cnVlLFxuICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICBtZXNzYWdlOiByZXNwb25zZS5kYXRhLm1lc3NhZ2VcbiAgICAgICAgICAgICAgICAgICAgICAgICAgICB9KTtcbiAgICAgICAgICAgICAgICAgICAgICAgICAgICBzbGVlcCgzNTAwKTsgLy93YWl0IDEgc2VjIGFuZCB0aGVuIGh0bXggcmVkaXJlY3QgZ2V0XG4gICAgICAgICAgICAgICAgICAgICAgICAgICAgaHRteC5hamF4KCdHRVQnLCByZWRpcmVjdCwge3RhcmdldDonbWFpbicsIHN3YXA6J291dGVySFRNTCd9KTtcbiAgICAgICAgICAgICAgICAgICAgICAgICAgICAvLyBzbGVlcCgzNTAwKTsgLy93YWl0IDEgc2VjIGFuZCB0aGVuIGh0bXggcmVkaXJlY3QgZ2V0XG4gICAgICAgICAgICAgICAgICAgICAgICAgICAgLy8gbG9jYXRpb24ucmVsb2FkKCk7XG4gICAgICAgICAgICAgICAgICAgICAgICB9IGVsc2Uge1xuICAgICAgICAgICAgICAgICAgICAgICAgICAgIGl6aVRvYXN0LmVycm9yKHtcbiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgdGl0bGU6IHJlc3BvbnNlLmRhdGEudGl0bGUsXG4gICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIGJhbGxvb246IHRydWUsXG4gICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIHBvc2l0aW9uOiBcInRvcFJpZ2h0XCIsXG4gICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIGFuaW1hdGVJbnNpZGU6IHRydWUsXG4gICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIG1lc3NhZ2U6IHJlc3BvbnNlLmRhdGEubWVzc2FnZVxuICAgICAgICAgICAgICAgICAgICAgICAgICAgIH0pO1xuICAgICAgICAgICAgICAgICAgICAgICAgfVxuXG4gICAgICAgICAgICAgICAgICAgICAgICBjb25zb2xlLmxvZyhyZXNwb25zZSk7XG4gICAgICAgICAgICAgICAgICAgIH0pLmNhdGNoKGZ1bmN0aW9uIChlcnJvcikge1xuICAgICAgICAgICAgICAgICAgICAgICAgaXppVG9hc3QuZXJyb3Ioe1xuICAgICAgICAgICAgICAgICAgICAgICAgICAgIHRpdGxlOiBcIkZvcm0gRXJyb3JcIixcbiAgICAgICAgICAgICAgICAgICAgICAgICAgICBiYWxsb29uOiB0cnVlLFxuICAgICAgICAgICAgICAgICAgICAgICAgICAgIHBvc2l0aW9uOiBcInRvcFJpZ2h0XCIsXG4gICAgICAgICAgICAgICAgICAgICAgICAgICAgYW5pbWF0ZUluc2lkZTogdHJ1ZSxcbiAgICAgICAgICAgICAgICAgICAgICAgICAgICBtZXNzYWdlOiBgU29tZXRoaW5nIHdyb25nIGhhcHBlbmVkOiAke2Vycm9yfWBcbiAgICAgICAgICAgICAgICAgICAgICAgIH0pO1xuICAgICAgICAgICAgICAgICAgICB9KTtcbiAgICAgICAgICAgICAgICAgICAgLy8gLmZpbmFsbHkoZnVuY3Rpb24gKCkge1xuICAgICAgICAgICAgICAgICAgICAvLyAgICAgY29uc29sZS5sb2coXCJmaW5hbGx5XCIpO1xuICAgICAgICAgICAgICAgICAgICAvLyB9KTtcblxuICAgICAgICAgICAgICAgIHRoaXMucHJvY2Vzc2luZyA9IGZhbHNlO1xuICAgICAgICAgICAgfSBlbHNlIHtcbiAgICAgICAgICAgICAgICBpemlUb2FzdC5lcnJvcih7XG4gICAgICAgICAgICAgICAgICAgIHRpdGxlOiBcIkZvcm0gU2VuZGluZyBJbmNvbXBsZXRlXCIsXG4gICAgICAgICAgICAgICAgICAgIGJhbGxvb246IHRydWUsXG4gICAgICAgICAgICAgICAgICAgIHBvc2l0aW9uOiBcInRvcFJpZ2h0XCIsXG4gICAgICAgICAgICAgICAgICAgIGFuaW1hdGVJbnNpZGU6IHRydWUsXG4gICAgICAgICAgICAgICAgICAgIG1lc3NhZ2U6IGBGb3JtIGRhdGEgaXMgbm90IHZhbGlkLiBFbnN1cmUgeW91IGhhdmUgZmlsbGVkIGFsbCBmaWVsZHMgYWNjdXJhdGVseSEgJHtmb3JtRWxlbWVudC5yZXBvcnRWYWxpZGl0eSgpfWBcbiAgICAgICAgICAgICAgICB9KTtcbiAgICAgICAgICAgICAgICBzbGVlcCgyNTAwKTsgLy93YWl0IDIuNSBzZWMgYW5kIHRoZW4gaHRteCByZWRpcmVjdCBnZXRcbiAgICAgICAgICAgICAgICB0aGlzLnByb2Nlc3NpbmcgPSBmYWxzZTtcbiAgICAgICAgICAgICAgICBodG14LmFqYXgoJ0dFVCcsIHJlZGlyZWN0LCB7dGFyZ2V0OidtYWluJywgc3dhcDonb3V0ZXJIVE1MJ30pO1xuICAgICAgICAgICAgfVxuXG4gICAgICAgIH0sXG5cbiAgICAgICAgYXN5bmMgY2hlY2tWYWxpZGl0eSgpIHtcbiAgICAgICAgICAgIGNvbnN0IGZvcm1FbGVtZW50ID0gdGhpcy4kcmVmcy5mb3JtO1xuICAgICAgICAgICAgZm9ybUVsZW1lbnQucXVlcnlTZWxlY3RvckFsbCgnW25hbWVdJykuZm9yRWFjaChmaWVsZEVsZW1lbnQgPT4ge1xuICAgICAgICAgICAgICAgIGZpZWxkRWxlbWVudC5hZGRFdmVudExpc3RlbmVyKCdjaGFuZ2UnLCBldmVudCA9PiB7XG4gICAgICAgICAgICAgICAgICAgIGNvbnNvbGUubG9nKGV2ZW50KTtcbiAgICAgICAgICAgICAgICAgICAgdmFsaWRhdGVGaWVsZChmb3JtRWxlbWVudCwgZmllbGRFbGVtZW50KTtcbiAgICAgICAgICAgICAgICB9KTtcbiAgICAgICAgICAgIH0pO1xuICAgICAgICB9LFxuXG4gICAgICAgIGdldEJ0blRleHQoKSB7XG4gICAgICAgICAgICByZXR1cm4gdGhpcy5wcm9jZXNzaW5nID8gJ1Byb2Nlc3NpbmcuLi4nIDogJ1N1Ym1pdCc7XG4gICAgICAgIH1cbiAgICB9O1xufVxuIiwiaW1wb3J0IGF4aW9zIGZyb20gXCIuL2F4aW9zRmFjdG9yeVwiO1xuaW1wb3J0IGh0bXggZnJvbSBcImh0bXgub3JnL2Rpc3QvaHRteFwiO1xuaW1wb3J0IGl6aVRvYXN0IGZyb20gJ2l6aXRvYXN0L2Rpc3QvanMvaXppVG9hc3QubWluLmpzJzsgIC8vIHlvdSBoYXZlIGFjY2VzcyB0byBpemlUb2FzdCBub3dcblxuLy8gZnVuY3Rpb24gc2VyaWFsaXplKGRhdGEpIHtcbi8vICAgICBsZXQgb2JqID0ge307XG4vLyAgICAgZm9yIChsZXQgW2tleSwgdmFsdWVdIG9mIGRhdGEpIHtcbi8vICAgICAgIGlmIChvYmpba2V5XSAhPT0gdW5kZWZpbmVkKSB7XG4vLyAgICAgICAgIGlmICghQXJyYXkuaXNBcnJheShvYmpba2V5XSkpIHtcbi8vICAgICAgICAgICBvYmpba2V5XSA9IFtvYmpba2V5XV07XG4vLyAgICAgICAgIH1cbi8vICAgICAgICAgb2JqW2tleV0ucHVzaCh2YWx1ZSk7XG4vLyAgICAgICB9IGVsc2Uge1xuLy8gICAgICAgICBvYmpba2V5XSA9IHZhbHVlO1xuLy8gICAgICAgfVxuLy8gICAgIH1cbi8vICAgICByZXR1cm4gb2JqO1xuLy8gfVxuXG5cbmZ1bmN0aW9uIHNsZWVwKG1zKSB7XG4gICAgcmV0dXJuIG5ldyB3aW5kb3cuUHJvbWlzZShyZXNvbHZlID0+IHNldFRpbWVvdXQocmVzb2x2ZSwgbXMpKTtcbn1cblxuZnVuY3Rpb24gdmFsaWRhdGVGaWVsZChmb3JtRWxlbWVudCwgZmllbGRFbGVtZW50KSB7XG4gICAgbGV0IGZvcm1EYXRhID0gbmV3IEZvcm1EYXRhKGZvcm1FbGVtZW50KTtcbiAgICBmb3JtRGF0YS5hcHBlbmQoXCJfX2ZpZWxkX25hbWVfX1wiLCBmaWVsZEVsZW1lbnQubmFtZSk7XG5cbiAgICBheGlvcy5wb3N0KGZvcm1FbGVtZW50LmFjdGlvbiwgZm9ybURhdGEpLnRoZW4oZnVuY3Rpb24gKHJlc3BvbnNlKSB7XG4gICAgICBsZXQgZXJyb3JzID0gcmVzcG9uc2UuZGF0YS5lcnJvcnM7XG4gICAgICBsZXQgZXJyb3JzV3JhcHBlckVsZW1lbnQgPSBkb2N1bWVudC5nZXRFbGVtZW50QnlJZChgZXJyb3Itd3JhcHBlci0ke2ZpZWxkRWxlbWVudC5uYW1lfWApO1xuICAgICAgaWYgKGVycm9ycy5sZW5ndGggPT09IDApIHtcbiAgICAgICAgZG9jdW1lbnQuZ2V0RWxlbWVudEJ5SWQoJ3N1Ym1pdCcpLmNsYXNzTGlzdC5yZW1vdmUoJ2hpZGRlbicpO1xuICAgICAgICBlcnJvcnNXcmFwcGVyRWxlbWVudC5jbGFzc0xpc3QuYWRkKCdoaWRkZW4nKTtcbiAgICAgICAgaWYgKGVycm9yc1dyYXBwZXJFbGVtZW50KSB7XG4gICAgICAgICAgZXJyb3JzV3JhcHBlckVsZW1lbnQuaW5uZXJIVE1MID0gXCJcIjtcbiAgICAgICAgfVxuICAgICAgfSBlbHNlIHtcbiAgICAgICAgZG9jdW1lbnQuZ2V0RWxlbWVudEJ5SWQoJ3N1Ym1pdCcpLmNsYXNzTGlzdC5hZGQoJ2hpZGRlbicpO1xuICAgICAgICBlcnJvcnNXcmFwcGVyRWxlbWVudC5jbGFzc0xpc3QucmVtb3ZlKCdoaWRkZW4nKTtcbiAgICAgICAgZXJyb3JzV3JhcHBlckVsZW1lbnQuY2xhc3NMaXN0LmFkZCgnZmxleCcpO1xuICAgICAgICBpZiAoZXJyb3JzV3JhcHBlckVsZW1lbnQpIHtcbiAgICAgICAgICBsZXQgZXJyb3JzSHRtbCA9ICcnO1xuICAgICAgICAgIGZvciAobGV0IGkgPSAwOyBpIDwgZXJyb3JzLmxlbmd0aDsgaSsrKSB7XG4gICAgICAgICAgICBlcnJvcnNIdG1sICs9IGAke2Vycm9yc1tpXX1gO1xuICAgICAgICAgIH1cbiAgICAgICAgICBlcnJvcnNXcmFwcGVyRWxlbWVudC5pbm5lckhUTUwgPSBlcnJvcnNIdG1sO1xuICAgICAgICB9XG4gICAgICB9XG4gICAgfSk7XG4gIH1cblxuXG5leHBvcnQgZGVmYXVsdCBmdW5jdGlvbiBDb250YWN0Rm9ybSgpIHtcbiAgICByZXR1cm4ge1xuICAgICAgICBwcm9jZXNzaW5nOiBmYWxzZSxcblxuICAgICAgICBhc3luYyBzdWJtaXRGb3JtKCkge1xuICAgICAgICAgICAgdGhpcy5wcm9jZXNzaW5nID0gdHJ1ZTtcblxuICAgICAgICAgICAgY29uc3QgZm9ybUVsZW1lbnQgPSB0aGlzLiRyZWZzLmNvbnRhY3RGb3JtO1xuICAgICAgICAgICAgY29uc3QgZGl2ID0gZG9jdW1lbnQuZ2V0RWxlbWVudEJ5SWQoJ2NvbnRhY3QnKTtcbiAgICAgICAgICAgIGNvbnN0IHJlZGlyZWN0ID0gZm9ybUVsZW1lbnQuYWN0aW9uO1xuICAgICAgICAgICAgY29uc3QgY3NyZiA9IGZvcm1FbGVtZW50LmRhdGFzZXQuY3NyZjtcbiAgICAgICAgICAgIGxldCBkYXRhID0gbmV3IEZvcm1EYXRhKGZvcm1FbGVtZW50KTtcbiAgICAgICAgICAgIGZvcm1FbGVtZW50LnF1ZXJ5U2VsZWN0b3JBbGwoXCJbbmFtZV1cIikuZm9yRWFjaChmaWVsZEVsZW1lbnQgPT4ge1xuICAgICAgICAgICAgICAgIGRhdGEuYXBwZW5kKGZpZWxkRWxlbWVudC5uYW1lLCBmaWVsZEVsZW1lbnQudmFsdWUpO1xuICAgICAgICAgICAgfSk7XG5cbiAgICAgICAgICAgIGNvbnNvbGUubG9nKGRhdGEpO1xuICAgICAgICAgICAgLy8gZGF0YS5hcHBlbmQoJ2NzcmZtaWRkbGV3YXJldG9rZW4nLCBjc3JmKTtcbiAgICAgICAgICAgIC8vIGRhdGEuYXBwZW5kKCduYW1lJywgZG9jdW1lbnQuZ2V0RWxlbWVudEJ5SWQoJ2lkX25hbWUnKS52YWx1ZSk7XG4gICAgICAgICAgICAvLyBkYXRhLmFwcGVuZCgnZW1haWwnLCBkb2N1bWVudC5nZXRFbGVtZW50QnlJZCgnaWRfZW1haWwnKS52YWx1ZSk7XG4gICAgICAgICAgICAvLyBkYXRhLmFwcGVuZCgnbWVzc2FnZScsIGRvY3VtZW50LmdldEVsZW1lbnRCeUlkKCdpZF9tZXNzYWdlJykudmFsdWUpO1xuXG4gICAgICAgICAgICAvLyBjb25zb2xlLmluZm8oXCJGT1JNIERBVEE6IFwiLCBkYXRhKTtcblxuICAgICAgICAgICAgLy8gbGV0IGZvcm1EYXRhID0gc2VyaWFsaXplKGRhdGEpO1xuICAgICAgICAgICAgLy8gY29uc29sZS5pbmZvKFwiU0VSSUFMSVpFRCBGT1JNIERBVEE6IFwiLCBmb3JtRGF0YSk7XG5cblxuICAgICAgICAgICAgaWYgKGZvcm1FbGVtZW50LmNoZWNrVmFsaWRpdHkoKSkge1xuICAgICAgICAgICAgICAgIGF3YWl0IGF4aW9zLnBvc3QocmVkaXJlY3QsIGRhdGEsIHtcbiAgICAgICAgICAgICAgICAgICAgaGVhZGVyczoge1xuICAgICAgICAgICAgICAgICAgICAgICdYLUNTUkZUb2tlbic6IGNzcmZcbiAgICAgICAgICAgICAgICAgICAgfX0pXG4gICAgICAgICAgICAgICAgICAgIC50aGVuKGZ1bmN0aW9uIChyZXNwb25zZSkge1xuICAgICAgICAgICAgICAgICAgICAgICAgLy8gY29uc29sZS5pbmZvKFwiUkVTUE9OU0UgREFUQTogXCIsIHJlc3BvbnNlKTtcblxuICAgICAgICAgICAgICAgICAgICAgICAgaWYgKHJlc3BvbnNlLnN0YXR1cyA9PT0gMjAwIHx8IHJlc3BvbnNlLmRhdGEubWVzc2FnZSA9PT0gXCJTdXBwb3J0IE1haWwgU3VjY2Vzc2Z1bGx5IFNlbnRcIikge1xuICAgICAgICAgICAgICAgICAgICAgICAgICAgIGRpdi5pbm5lckhUTUwgPSBgXG4gICAgICAgICAgICAgICAgICAgICAgICAgICAgPGRpdiBjbGFzcz1cInctZnVsbCB0ZXh0LWdyZWVuLTMwMCBzcGFjZS15LTggZmxleCBmbGV4LWNvbCBqdXN0aWZ5LWNlbnRlciBweS0yNFwiPlxuICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICA8c3ZnIHhtbG5zPVwiaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmdcIiBmaWxsPVwibm9uZVwiIHZpZXdCb3g9XCIwIDAgMjQgMjRcIiBzdHJva2Utd2lkdGg9XCIxLjVcIiBzdHJva2U9XCJjdXJyZW50Q29sb3JcIiBjbGFzcz1cImJsb2NrIHctMTQgaC0xNCBibG9jayBteC1hdXRvIGFuaW1hdGUtYm91bmNlIHRleHQtZ3JlZW4tMzAwXCI+XG4gICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICA8cGF0aCBzdHJva2UtbGluZWNhcD1cInJvdW5kXCIgc3Ryb2tlLWxpbmVqb2luPVwicm91bmRcIiBkPVwiTTIxLjc1IDYuNzV2MTAuNWEyLjI1IDIuMjUgMCAwMS0yLjI1IDIuMjVoLTE1YTIuMjUgMi4yNSAwIDAxLTIuMjUtMi4yNVY2Ljc1bTE5LjUgMEEyLjI1IDIuMjUgMCAwMDE5LjUgNC41aC0xNWEyLjI1IDIuMjUgMCAwMC0yLjI1IDIuMjVtMTkuNSAwdi4yNDNhMi4yNSAyLjI1IDAgMDEtMS4wNyAxLjkxNmwtNy41IDQuNjE1YTIuMjUgMi4yNSAwIDAxLTIuMzYgMEwzLjMyIDguOTFhMi4yNSAyLjI1IDAgMDEtMS4wNy0xLjkxNlY2Ljc1XCIgLz5cbiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgPC9zdmc+XG4gICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIDxkaXYgY2xhc3M9XCJ3LWZ1bGwgbWQ6dy0zLzUgdGV4dC1jZW50ZXIgc3BhY2UteS0zIG14LWF1dG9cIj5cbiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIDxoNCBjbGFzcz1cInRleHQtZ3JlZW4tNTAwIGZvbnQtc2VtaWJvbGQgdGV4dC0yeGwgbWQ6dGV4dC00eGxcIj5NYWlsIFNlbnQgU3VjY2Vzc2Z1bGx5PC9oND5cbiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIDxwPiR7cmVzcG9uc2UuZGF0YS5tZXNzYWdlfTwvcD5cbiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgPC9kaXY+XG4gICAgICAgICAgICAgICAgICAgICAgICAgICAgPC9kaXY+XG4gICAgICAgICAgICAgICAgICAgICAgICAgICAgYDtcbiAgICAgICAgICAgICAgICAgICAgICAgICAgICBpemlUb2FzdC5zdWNjZXNzKHtcbiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgdGl0bGU6IFwiRW1haWwgU2VudCBTdWNjZXNzZnVsXCIsXG4gICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIGJhbGxvb246IHRydWUsXG4gICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIHBvc2l0aW9uOiBcInRvcFJpZ2h0XCIsXG4gICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIGFuaW1hdGVJbnNpZGU6IHRydWUsXG4gICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIG1lc3NhZ2U6IHJlc3BvbnNlLmRhdGEubWVzc2FnZVxuICAgICAgICAgICAgICAgICAgICAgICAgICAgIH0pO1xuICAgICAgICAgICAgICAgICAgICAgICAgICAgIHNsZWVwKDM1MDApOyAvL3dhaXQgMSBzZWMgYW5kIHRoZW4gaHRteCByZWRpcmVjdCBnZXRcbiAgICAgICAgICAgICAgICAgICAgICAgICAgICBodG14LmFqYXgoJ0dFVCcsIHJlZGlyZWN0LCB7dGFyZ2V0OidtYWluJywgc3dhcDonb3V0ZXJIVE1MJ30pO1xuICAgICAgICAgICAgICAgICAgICAgICAgICAgIC8vIHNsZWVwKDM1MDApOyAvL3dhaXQgMSBzZWMgYW5kIHRoZW4gaHRteCByZWRpcmVjdCBnZXRcbiAgICAgICAgICAgICAgICAgICAgICAgICAgICAvLyBsb2NhdGlvbi5yZWxvYWQoKTtcbiAgICAgICAgICAgICAgICAgICAgICAgIH1cblxuICAgICAgICAgICAgICAgICAgICAgICAgY29uc29sZS5sb2cocmVzcG9uc2UpO1xuICAgICAgICAgICAgICAgICAgICB9KS5jYXRjaChmdW5jdGlvbiAoZXJyb3IpIHtcbiAgICAgICAgICAgICAgICAgICAgICAgIGl6aVRvYXN0LmVycm9yKHtcbiAgICAgICAgICAgICAgICAgICAgICAgICAgICB0aXRsZTogXCJFbWFpbCBTZW5kaW5nIEluY29tcGxldGVcIixcbiAgICAgICAgICAgICAgICAgICAgICAgICAgICBiYWxsb29uOiB0cnVlLFxuICAgICAgICAgICAgICAgICAgICAgICAgICAgIHBvc2l0aW9uOiBcInRvcFJpZ2h0XCIsXG4gICAgICAgICAgICAgICAgICAgICAgICAgICAgYW5pbWF0ZUluc2lkZTogdHJ1ZSxcbiAgICAgICAgICAgICAgICAgICAgICAgICAgICBtZXNzYWdlOiBgU29tZXRoaW5nIHdyb25nIGhhcHBlbmVkOiAke2Vycm9yfWBcbiAgICAgICAgICAgICAgICAgICAgICAgIH0pO1xuICAgICAgICAgICAgICAgICAgICB9KTtcbiAgICAgICAgICAgICAgICAgICAgLy8gLmZpbmFsbHkoZnVuY3Rpb24gKCkge1xuICAgICAgICAgICAgICAgICAgICAvLyAgICAgY29uc29sZS5sb2coXCJmaW5hbGx5XCIpO1xuICAgICAgICAgICAgICAgICAgICAvLyB9KTtcblxuICAgICAgICAgICAgICAgIHRoaXMucHJvY2Vzc2luZyA9IGZhbHNlO1xuICAgICAgICAgICAgfSBlbHNlIHtcbiAgICAgICAgICAgICAgICBpemlUb2FzdC5lcnJvcih7XG4gICAgICAgICAgICAgICAgICAgIHRpdGxlOiBcIlNlbmRpbmcgRW1haWwgSW5jb21wbGV0ZVwiLFxuICAgICAgICAgICAgICAgICAgICBiYWxsb29uOiB0cnVlLFxuICAgICAgICAgICAgICAgICAgICBwb3NpdGlvbjogXCJ0b3BSaWdodFwiLFxuICAgICAgICAgICAgICAgICAgICBhbmltYXRlSW5zaWRlOiB0cnVlLFxuICAgICAgICAgICAgICAgICAgICBtZXNzYWdlOiBgRm9ybSBkYXRhIGlzIG5vdCB2YWxpZC4gRW5zdXJlIHlvdSBoYXZlIGZpbGxlZCBhbGwgZmllbGRzIGFjY3VyYXRlbHkhICR7Zm9ybUVsZW1lbnQucmVwb3J0VmFsaWRpdHkoKX1gXG4gICAgICAgICAgICAgICAgfSk7XG4gICAgICAgICAgICAgICAgc2xlZXAoMjUwMCk7IC8vd2FpdCAyLjUgc2VjIGFuZCB0aGVuIGh0bXggcmVkaXJlY3QgZ2V0XG4gICAgICAgICAgICAgICAgdGhpcy5wcm9jZXNzaW5nID0gZmFsc2U7XG4gICAgICAgICAgICAgICAgaHRteC5hamF4KCdHRVQnLCByZWRpcmVjdCwge3RhcmdldDonbWFpbicsIHN3YXA6J291dGVySFRNTCd9KTtcbiAgICAgICAgICAgIH1cblxuICAgICAgICB9LFxuXG4gICAgICAgIGFzeW5jIGNoZWNrVmFsaWRpdHkoKSB7XG4gICAgICAgICAgICBjb25zdCBmb3JtRWxlbWVudCA9IHRoaXMuJHJlZnMuY29udGFjdEZvcm07XG4gICAgICAgICAgICBmb3JtRWxlbWVudC5xdWVyeVNlbGVjdG9yQWxsKCdbbmFtZV0nKS5mb3JFYWNoKGZpZWxkRWxlbWVudCA9PiB7XG4gICAgICAgICAgICAgICAgZmllbGRFbGVtZW50LmFkZEV2ZW50TGlzdGVuZXIoJ2NoYW5nZScsIGV2ZW50ID0+IHtcbiAgICAgICAgICAgICAgICAgICAgY29uc29sZS5sb2coZXZlbnQpO1xuICAgICAgICAgICAgICAgICAgICB2YWxpZGF0ZUZpZWxkKGZvcm1FbGVtZW50LCBmaWVsZEVsZW1lbnQpO1xuICAgICAgICAgICAgICAgIH0pO1xuICAgICAgICAgICAgfSk7XG4gICAgICAgIH0sXG5cbiAgICAgICAgZ2V0QnRuVGV4dCgpIHtcbiAgICAgICAgICAgIHJldHVybiB0aGlzLnByb2Nlc3NpbmcgPyAnUHJvY2Vzc2luZy4uLicgOiAnU3VibWl0JztcbiAgICAgICAgfVxuICAgIH07XG59XG4iLCJleHBvcnQgZGVmYXVsdCBmdW5jdGlvbiBTdGlja3lOYXYoKSB7XG4gICAgcmV0dXJuIHtcbiAgICAgICAgc2hvd05hdjogdHJ1ZSxcbiAgICAgICAgbmF2VG9wOiBmYWxzZSxcbiAgICAgICAgbGFzdFNjcm9sbDogMCxcblxuICAgICAgICBpbml0U3RhdGUoKSB7XG4gICAgICAgICAgICBjb25zdCBtYWluID0gZG9jdW1lbnQuZ2V0RWxlbWVudEJ5SWQoJ21haW4nKTtcbiAgICAgICAgICAgIGNvbnN0IG5hdmJhciA9IGRvY3VtZW50LmdldEVsZW1lbnRCeUlkKCduYXZiYXInKTtcblxuICAgICAgICAgICAgLy8gZ2V0IHRoZSBoZWlnaHQgb2YgdGhlIG5hdmJhciBhbmQgdGhlbiBhZGQgaXQgdG8gdGhlIHRvcCBwYWRkaW5nIG9mIHRoZSBtYWluIGNvbnRlbnRcbiAgICAgICAgICAgIGNvbnN0IGhlYWRlcl9oID0gbmF2YmFyLm9mZnNldEhlaWdodCArIDEwO1xuXG4gICAgICAgICAgICBtYWluLmNsYXNzTGlzdC5hZGQoYHB0LVske2hlYWRlcl9ofXB4XWApO1xuICAgICAgICAgICAgdGhpcy5uYXZUb3AgPSB0cnVlO1xuICAgICAgICAgICAgdGhpcy5zaG93TmF2ID0gZmFsc2U7XG4gICAgICAgIH0sXG5cbiAgICAgICAgc2Nyb2xsTmF2KCkge1xuICAgICAgICAgICAgbGV0IGN1cnJlbnRTY3JvbGwgPSB3aW5kb3cucGFnZVlPZmZzZXQ7XG4gICAgICAgICAgICBpZiAoY3VycmVudFNjcm9sbCA8PSAwKSB7XG4gICAgICAgICAgICAgICAgdGhpcy5zaG93TmF2ID0gdHJ1ZTtcbiAgICAgICAgICAgICAgICB0aGlzLm5hdlRvcCA9IHRydWU7XG4gICAgICAgICAgICB9XG5cbiAgICAgICAgICAgIGlmIChjdXJyZW50U2Nyb2xsID4gdGhpcy5sYXN0U2Nyb2xsICYmIHRoaXMuc2hvd05hdiA9PT0gZmFsc2UpIHtcbiAgICAgICAgICAgICAgICB0aGlzLnNob3dOYXYgPSB0cnVlO1xuICAgICAgICAgICAgICAgIHRoaXMubmF2VG9wID0gZmFsc2U7XG4gICAgICAgICAgICB9IGVsc2UgaWYgKGN1cnJlbnRTY3JvbGwgPCB0aGlzLmxhc3RTY3JvbGwgJiYgdGhpcy5zaG93TmF2ID09PSB0cnVlKSB7XG4gICAgICAgICAgICAgICAgdGhpcy5zaG93TmF2ID0gZmFsc2U7XG4gICAgICAgICAgICAgICAgdGhpcy5uYXZUb3AgPSB0cnVlO1xuICAgICAgICAgICAgfVxuICAgICAgICAgICAgdGhpcy5sYXN0U2Nyb2xsID0gY3VycmVudFNjcm9sbDtcbiAgICAgICAgfVxuICAgIH07XG59XG4iLCJpbXBvcnQgYXhpb3MgZnJvbSBcImF4aW9zXCI7XG5cbmF4aW9zLmRlZmF1bHRzLndpdGhDcmVkZW50aWFscyA9IHRydWU7XG5heGlvcy5kZWZhdWx0cy54c3JmQ29va2llTmFtZSA9ICdjc3JmdG9rZW4nO1xuYXhpb3MuZGVmYXVsdHMueHNyZkhlYWRlck5hbWUgPSBcIlgtQ1NSRlRPS0VOXCI7XG4vLyBheGlvcy5kZWZhdWx0cy5oZWFkZXJzWydYLUNTUkZUb2tlbiddID0gZG9jdW1lbnQuaGVhZC5xdWVyeVNlbGVjdG9yKCdtZXRhW25hbWU9XCJjc3JmLXRva2VuXCJdJykuZ2V0QXR0cmlidXRlKCdjb250ZW50Jyk7XG5heGlvcy5kZWZhdWx0cy50aW1lb3V0ID0gMTUwMDA7XG5cbmV4cG9ydCBkZWZhdWx0IGF4aW9zO1xuIiwiLy8gZXh0cmFjdGVkIGJ5IG1pbmktY3NzLWV4dHJhY3QtcGx1Z2luXG5leHBvcnQge307IiwiLyogKGlnbm9yZWQpICovIl0sIm5hbWVzIjpbImh0bXgiLCJBbHBpbmUiLCJldGhlcnMiLCJheGlvcyIsIlN0aWNreU5hdiIsIlN3aXBlciIsImRldGVjdCIsIml6aVRvYXN0IiwiYW5pbWUiLCJTY3JvbGxNYWdpYyIsIkNvbnRhY3RGb3JtIiwiQWNjb3VudEZvcm0iLCJsb3R0aWV3ZWIiLCJ3aW5kb3ciLCJzY3JvbGxNYWdpYyIsIml6aXRvYXN0IiwiZGF0YSIsInN0YXJ0Iiwic3ciLCJob21lIiwiYnJvd3NlciIsIkFQUExJQ0FUSU9OX1NFUlZFUl9LRVkiLCJDUkVBVEVfV1BfREVWSUNFIiwiU0VORF9OT1RJRklDQVRJT04iLCJXRUJfUFVTSF9DRkciLCJ1cmxCYXNlNjRUb1VpbnQ4QXJyYXkiLCJiYXNlNjRTdHJpbmciLCJwYWRkaW5nIiwicmVwZWF0IiwibGVuZ3RoIiwiYmFzZTY0IiwicmVwbGFjZSIsInJhd0RhdGEiLCJhdG9iIiwib3V0cHV0QXJyYXkiLCJVaW50OEFycmF5IiwiaSIsImNoYXJDb2RlQXQiLCJzYXZlU3Vic2NyaWJlT2JqIiwic3Vic2NyaXB0aW9uIiwic3Vic2NyaXB0aW9uSnNvbiIsInRvSlNPTiIsImVuZHBvaW50UGFydHMiLCJlbmRwb2ludCIsInNwbGl0IiwicmVnaXN0cmF0aW9uSWQiLCJwcmVkYXRhIiwic3RhdHVzX3R5cGUiLCJuYW1lIiwidG9Mb3dlckNhc2UiLCJwMjU2ZGgiLCJrZXlzIiwiYXV0aCIsInVzZXJfYWdlbnQiLCJuYXZpZ2F0b3IiLCJnZXRVc2VyQWdlbnQiLCJyZWdpc3RyYXRpb25faWQiLCJncm91cCIsIkpTT04iLCJzdHJpbmdpZnkiLCJwb3N0IiwiaGVhZGVycyIsInRoZW4iLCJyZXNwb25zZSIsInByb2Nlc3MiLCJlbnYiLCJOT0RFX0VOViIsInN1YnNjcmliZU5vdGlmaWNhdGlvbkJ1dHRvbiIsImRvY3VtZW50IiwiZ2V0RWxlbWVudEJ5SWQiLCJjbGFzc0xpc3QiLCJ0b2dnbGUiLCJzdWNjZXNzIiwidGl0bGUiLCJiYWxsb29uIiwicG9zaXRpb24iLCJhbmltYXRlSW5zaWRlIiwibWVzc2FnZSIsInN0YXR1c1RleHQiLCJzZXR1cFRyaWdnZXJCdXR0b24iLCJjYXRjaCIsImVycm9yIiwiY29uc29sZSIsImxvZyIsInNhdmVEcml2ZXJTdWJzY3JpYmVPYmoiLCJzYXZlQ29tcGFueVN1YnNjcmliZU9iaiIsInN1YnNjcmliZSIsInJlZ2lzdHJhdGlvbiIsInB1c2hNYW5hZ2VyIiwiZ2V0U3Vic2NyaXB0aW9uIiwib3B0aW9ucyIsInVzZXJWaXNpYmxlT25seSIsImFwcGxpY2F0aW9uU2VydmVyS2V5Iiwic3Vic2NyaWJlRHJpdmVyIiwic3Vic2NyaWJlQ29tcGFueSIsInNldHVwU3Vic2NyaWJlQnV0dG9uIiwicmVnIiwiYWRkRXZlbnRMaXN0ZW5lciIsInNldHVwRHJpdmVyU3Vic2NyaWJlQnV0dG9uIiwic3Vic2NyaWJlRHJpdmVyQnV0dG9uIiwic2V0dXBDb21wYW55U3Vic2NyaWJlQnV0dG9uIiwic3Vic2NyaWJlQ29tcGFueUJ1dHRvbiIsInN1Ykpzb24iLCJoZWFkIiwiYm9keSIsImluZm8iLCJkZXRhaWwiLCJzaGFyZUJ1dHRvbiIsInVybCIsImRhdGFzZXQiLCJzaGFyZSIsInRleHQiLCJ0b1VwcGVyQ2FzZSIsInNlcnZpY2VXb3JrZXIiLCJyZWdpc3RlciIsInNjb3BlIiwicmVhZHkiLCJhY3RpdmUiLCJpbml0aWFsaXNlU3RhdGUiLCJlcnIiLCJzaG93Tm90aWZpY2F0aW9uIiwiTm90aWZpY2F0aW9uIiwicGVybWlzc2lvbiIsIndhcm5pbmciLCJzdWIiLCJpbnN0YWxsQnV0dG9uIiwiZXZlbnQiLCJkZWZlcnJlZFByb21wdCIsInByb21wdEV2ZW50IiwicHJvbXB0IiwidXNlckNob2ljZSIsImNob2ljZSIsImxvZ0FsbCIsImZvckVhY2giLCJldnQiLCJjb3VudGVycyIsInF1ZXJ5U2VsZWN0b3JBbGwiLCJjYXIiLCJjb250cm9sbGVyIiwiQ29udHJvbGxlciIsInN0YXJ0Q291bnRpbmciLCJjb3VudGVyIiwidGFyZ2V0cyIsImlubmVySFRNTCIsImdldEF0dHJpYnV0ZSIsImVhc2luZyIsInJvdW5kIiwiZHVyYXRpb24iLCJhbmltYXRlSG93cyIsInRyYW5zbGF0ZVgiLCJvcGFjaXR5IiwiZGVsYXkiLCJzdGFnZ2VyIiwiU2NlbmUiLCJ0cmlnZ2VyRWxlbWVudCIsInRyaWdnZXJIb29rIiwicmV2ZXJzZSIsIm9mZnNldCIsIm9uIiwiYWRkVG8iLCJjYXJEcml2ZSIsInZhbHVlIiwiZGlyZWN0aW9uIiwibG9vcCIsInNsZWVwIiwibXMiLCJQcm9taXNlIiwicmVzb2x2ZSIsInNldFRpbWVvdXQiLCJ2YWxpZGF0ZUZpZWxkIiwiZm9ybUVsZW1lbnQiLCJmaWVsZEVsZW1lbnQiLCJmb3JtRGF0YSIsIkZvcm1EYXRhIiwiYXBwZW5kIiwiYWN0aW9uIiwiZXJyb3JzIiwiZXJyb3JzV3JhcHBlckVsZW1lbnQiLCJyZW1vdmUiLCJhZGQiLCJlcnJvcnNIdG1sIiwicHJvY2Vzc2luZyIsInN1Ym1pdEZvcm0iLCIkcmVmcyIsImZvcm0iLCJkaXYiLCJyZWRpcmVjdCIsImNzcmYiLCJ0eXBlIiwidGV4dGFyZWEiLCJpZCIsInBhcmVudCIsInRpbnltY2UiLCJnZXQiLCJnZXRDb250ZW50IiwiY2hlY2tWYWxpZGl0eSIsInN0YXR1cyIsImFqYXgiLCJ0YXJnZXQiLCJzd2FwIiwicmVwb3J0VmFsaWRpdHkiLCJzdWJtaXRGaWxlRm9ybSIsImdldEJ0blRleHQiLCJjb250YWN0Rm9ybSIsInNob3dOYXYiLCJuYXZUb3AiLCJsYXN0U2Nyb2xsIiwiaW5pdFN0YXRlIiwibWFpbiIsIm5hdmJhciIsImhlYWRlcl9oIiwib2Zmc2V0SGVpZ2h0Iiwic2Nyb2xsTmF2IiwiY3VycmVudFNjcm9sbCIsInBhZ2VZT2Zmc2V0IiwiZGVmYXVsdHMiLCJ3aXRoQ3JlZGVudGlhbHMiLCJ4c3JmQ29va2llTmFtZSIsInhzcmZIZWFkZXJOYW1lIiwidGltZW91dCJdLCJzb3VyY2VSb290IjoiIn0=