// This is global imports for css and javascripts //
//----------------------------------------------------------
import "../styles/index.scss";
import htmx from "htmx.org/dist/htmx";
import Alpine from "alpinejs";
import { ethers } from "ethers";
import axios from "../components/axiosFactory";
import StickyNav from "../components/StickyNav";
import Swiper from "swiper";
import { detect } from "detect-browser";
import "izitoast/dist/css/iziToast.min.css";
import "@lottiefiles/lottie-player";
import iziToast from "izitoast/dist/js/iziToast.min.js";
import anime from "animejs/lib/anime.es.js";
import ScrollMagic from "scrollmagic";
import ContactForm from "../components/ContactForm";
import AccountForm from "../components/AccountForm";
import lottieweb from "lottie-web";

// import { initializeApp } from "firebase/app";
// import { getAnalytics } from "firebase/analytics";
//----------------------------------------------------------

// Global Initializations for importedlibraries //
//----------------------------------------------------------
// initialize htmx
window.htmx = htmx;
// initialize lottie web and lottie player
window.lottieweb = lottieweb;
// initialize animejs
window.anime = anime;
window.scrollMagic = ScrollMagic;
// initialize ether js for crypto payment
window.ethers = ethers;
// initialize axios async post|get request
window.axios = axios;
// initialize swiper.js
window.Swiper = Swiper;
// initiailize izitoast alerts
window.izitoast = iziToast;
// Alpine JS Scripts
window.Alpine = Alpine;
Alpine.data("StickyNav", StickyNav);
Alpine.data("ContactForm", ContactForm);
Alpine.data("AccountForm", AccountForm);
Alpine.start();
//----------------------------------------------------------

// set service worker link and scope start link
//----------------------------------------------------------
const sw = "/sw.js";
const home = "/";
// detect browser type
const browser = detect();
//----------------------------------------------------------

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
  const { APPLICATION_SERVER_KEY, CREATE_WP_DEVICE, SEND_NOTIFICATION } =
    window.WEB_PUSH_CFG;
  //----------------------------------------------------------

  // generate key for push notifications
  //----------------------------------------------------------
  function urlBase64ToUint8Array(base64String) {
    // https://gist.github.com/Klerith/80abd742d726dd587f4bd5d6a0ab26b6#file-urlbase64touint8array-js
    var padding = "=".repeat((4 - (base64String.length % 4)) % 4);
    var base64 = (base64String + padding).replace(/\-/g, "+").replace(/_/g, "/");

    var rawData = window.atob(base64);
    var outputArray = new Uint8Array(rawData.length);

    for (var i = 0; i < rawData.length; ++i) {
      outputArray[i] = rawData.charCodeAt(i);
    }
    return outputArray;

    // const outputData = outputArray.map((output, index) =>
    //   rawData.charCodeAt(index)
    // );
    // return outputData;
  }
  //----------------------------------------------------------

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
      group: "users",
    };

    const data = JSON.stringify(predata);

    axios
      .post(CREATE_WP_DEVICE, data, {
        headers: {
          "Content-Type": "application/json",
        },
      })
      .then(function (response) {
        if (process.env.NODE_ENV === "development") {
          console.log(response);
          iziToast.success({
            title: "[PUSH NOTIFICATION SERVER]",
            balloon: true,
            position: "topRight",
            animateInside: true,
            message: `Notification Subscription ${response.statusText}`,
          });
        }
      })
      .catch(function (error) {
        if (process.env.NODE_ENV === "development") {
          console.log(error);
          iziToast.error({
            title: "[PUSH NOTIFICATION SERVER]",
            balloon: true,
            position: "topRight",
            animateInside: true,
            message: `Notification Subscription ${error.message}`,
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
      group: "drivers",
    };

    const data = JSON.stringify(predata);

    axios
      .post(CREATE_WP_DEVICE, data, {
        headers: {
          "Content-Type": "application/json",
        },
      })
      .then(function (response) {
        if (process.env.NODE_ENV === "development") {
          console.log(response);
          iziToast.success({
            title: "[PUSH NOTIFICATION SERVER]",
            balloon: true,
            position: "topRight",
            animateInside: true,
            message: `Notification Subscription ${response.statusText}`,
          });
        }
      })
      .catch(function (error) {
        if (process.env.NODE_ENV === "development") {
          console.log(error);
          iziToast.error({
            title: "[PUSH NOTIFICATION SERVER]",
            balloon: true,
            position: "topRight",
            animateInside: true,
            message: `Notification Subscription ${error.message}`,
          });
        }
      });
  }
  //----------------------------------------------------------

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
      userVisibleOnly: true, // required by chrome
      applicationServerKey: urlBase64ToUint8Array(APPLICATION_SERVER_KEY),
    };

    registration.pushManager.subscribe(options).then(
      // requesting to subscribe from the server
      function (subscription) {
        if (process.env.NODE_ENV === "development") {
          console.log(`subscription: `, subscription);
          console.log(subscription.endpoint);
        }

        // subscription is now saved to the server
        saveSubscribeObj(subscription);

        // if subscription is successfully saved to the server
        // then enable the test notification push button to be visible
        setupTriggerButton(subscription);

        iziToast.success({
          title: "[PUSH NOTIFICATION SUBSCRIPTION]",
          balloon: true,
          position: "topRight",
          animateInside: true,
          message: `Subscription Sent Successfully`,
        });
      },

      // if there is an error figure the error and throw an appropraite error message to
      // the user so he knows exactly what is wrong and can move forward or adjust for a
      // device.
      function (error) {
        if (process.env.NODE_ENV === "development") {
          console.log(error);
        }

        iziToast.error({
          title: "[PUSH NOTIFICATION SUBSCRIPTION]",
          balloon: true,
          position: "topRight",
          animateInside: true,
          message: `${error}`,
        });
      }
    );
  }

  function subscribeDriver(registration) {
    registration.pushManager.getSubscription().then(function (subscription) {
      if (subscription) {
        console.log("subscription exists");
        saveDriverSubscribeObj(subscription);
        setupTriggerButton(subscription);
        return;
      }
    });

    const options = {
      userVisibleOnly: true, // required by chrome
      applicationServerKey: urlBase64ToUint8Array(APPLICATION_SERVER_KEY),
    };

    registration.pushManager.subscribe(options).then(
      // requesting to subscribe from the server
      function (subscription) {
        if (process.env.NODE_ENV === "development") {
          console.log(`subscription: `, subscription);
          console.log(subscription.endpoint);
        }

        // subscription is now saved to the server
        saveSubscribeObj(subscription);

        // if subscription is successfully saved to the server
        // then enable the test notification push button to be visible
        setupTriggerButton(subscription);

        iziToast.success({
          title: "[PUSH NOTIFICATION SUBSCRIPTION]",
          balloon: true,
          position: "topRight",
          animateInside: true,
          message: `Subscription Sent Successfully`,
        });
      },

      // if there is an error figure the error and throw an appropraite error message to
      // the user so he knows exactly what is wrong and can move forward or adjust for a
      // device.
      function (error) {
        if (process.env.NODE_ENV === "development") {
          console.log(error);
        }

        iziToast.error({
          title: "[PUSH NOTIFICATION SUBSCRIPTION]",
          balloon: true,
          position: "topRight",
          animateInside: true,
          message: `${error}`,
        });
      }
    );
  }

  function subscribeCompany(registration) {
    registration.pushManager.getSubscription().then(function (subscription) {
      if (subscription) {
        console.log("subscription exists");
        saveDriverSubscribeObj(subscription);
        setupTriggerButton(subscription);
        return;
      }
    });

    const options = {
      userVisibleOnly: true, // required by chrome
      applicationServerKey: urlBase64ToUint8Array(APPLICATION_SERVER_KEY),
    };

    registration.pushManager.subscribe(options).then(
      // requesting to subscribe from the server
      function (subscription) {
        if (process.env.NODE_ENV === "development") {
          console.log(`subscription: `, subscription);
          console.log(subscription.endpoint);
        }

        // subscription is now saved to the server
        saveSubscribeObj(subscription);

        // if subscription is successfully saved to the server
        // then enable the test notification push button to be visible
        setupTriggerButton(subscription);

        iziToast.success({
          title: "[PUSH NOTIFICATION SUBSCRIPTION]",
          balloon: true,
          position: "topRight",
          animateInside: true,
          message: `Subscription Sent Successfully`,
        });
      },

      // if there is an error figure the error and throw an appropraite error message to
      // the user so he knows exactly what is wrong and can move forward or adjust for a
      // device.
      function (error) {
        if (process.env.NODE_ENV === "development") {
          console.log(error);
        }

        iziToast.error({
          title: "[PUSH NOTIFICATION SUBSCRIPTION]",
          balloon: true,
          position: "topRight",
          animateInside: true,
          message: `${error}`,
        });
      }
    );
  }
  //----------------------------------------------------------

  // The function to trigger the push notification from the browser
  //----------------------------------------------------------
  // subscribe(reg);
  function setupSubscribeButton(reg) {
    if (document.getElementById('subscribeNotificationButton')) {
      const subscribeNotificationButton = document.getElementById('subscribeNotificationButton');
      subscribeNotificationButton.classList.toggle('hidden', false);
      subscribeNotificationButton.addEventListener('click', () => {
        return subscribe(reg);
      });
    }
  }

  function setupDriverSubscribeButton(reg) {
    if (document.getElementById('subscribeDriver')) {
      const subscribeDriverButton = document.getElementById('subscribeDriver');
      subscribeDriverButton.addEventListener('click', () => {
        return subscribeDriver(reg);
      });
    }
  }

  function setupCompanySubscribeButton(reg) {
    if (document.getElementById('subscribeCompany')) {
      const subscribeCompanyButton = document.getElementById('subscribeCompany');
      subscribeCompanyButton.addEventListener('click', () => {
        return subscribeCompany(reg);
      });
    }
  }

  //----------------------------------------------------------
  // This function is for a user to test the push notification
  //----------------------------------------------------------
  function setupTriggerButton(subscription) {
    if (document.getElementById(
      "triggerNotificationButton"
    )){
      const triggerNotificationButton = document.getElementById(
        "triggerNotificationButton"
      );
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
          body: "This is a test notification",
        };

        const data = JSON.stringify(predata);

        axios
          .post(SEND_NOTIFICATION, data, {
            headers: {
              "Content-Type": "application/json",
            },
          })
          .then(function (response) {
            iziToast.success({
              title: "[PUSH NOTIFICATION TEST SUCCESSFUL]",
              balloon: true,
              position: "topRight",
              animateInside: true,
              message: response.data.message,
            });
          })
          .catch(function (error) {
            iziToast.error({
              title: "[PUSH NOTIFICATION TEST ERROR]",
              balloon: true,
              position: "topRight",
              animateInside: true,
              message: error.response.data.detail,
            });
          });
      });
    }
    return;
  }
  //----------------------------------------------------------
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
        url: url,
      })
        .then(() => iziToast.success({
          title: "[SHARE PAGE]",
          balloon: true,
          position: "topRight",
          animateInside: true,
          message: `Successfully share ${url}`,
        }))
        .catch((error) => iziToast.error({
          title: "[SHARE PAGE ERROR]",
          balloon: true,
          position: "topRight",
          animateInside: true,
          message: error,
        }));
      }
  });
 }

  //----------------------------------------------------------

  // enable service worker, then when service worker is enabled request
  // permission for push notification and location services from the browser
  //----------------------------------------------------------
  if ("serviceWorker" in navigator) {
    window.addEventListener("load", () => {
      navigator.serviceWorker
        .register(sw, { scope: home })
        .then((registration) => {
          if (process.env.NODE_ENV === "development") {
            console.log("Service worker registeration succeeded: ", registration);
          }

          navigator.serviceWorker.ready.then(function (registration) {
            if (process.env.NODE_ENV === "development") {
              console.log("Service worker is active: ", registration.active);
            }

            initialiseState(registration);
          });
        })
        .catch((err) => {
          iziToast.error({
            title: "[SERVICE WORKER]",
            balloon: true,
            position: "topRight",
            animateInside: true,
            message: "Service Worker Failed to Register",
          });

          if (process.env.NODE_ENV === "development") {
            console.log(err);
          }
        });
    });
  }

  const initialiseState = (reg) => {
    if (!reg.showNotification) {
      iziToast.error({
        title: "[PUSH UNSUPPORTED]",
        balloon: true,
        position: "topRight",
        animateInside: true,
        message: "Showing <strong>PUSH NOTIFICATIONS</strong> is unsupported",
      });
      return;
    }

    if (Notification.permission === "denied") {
      iziToast.warning({
        title: "[PUSH DENIED]",
        balloon: true,
        position: "topRight",
        animateInside: true,
        message:
          "You prevented us from shwoing notifications. Manually check if you have prevented push notifcation from us.",
      });
      return;
    }

    if (!("PushManager" in window)) {
      iziToast.info({
        title: "[PUSH BROWSER UNAVAILBALE]",
        balloon: true,
        position: "topRight",
        animateInside: true,
        message: "Push notification is not allowed in your browser.",
      });
      return;
    }

    reg.pushManager.getSubscription().then((sub) => {
      if (!sub) {
        setupSubscribeButton(reg);
        setupDriverSubscribeButton(reg);
        setupCompanySubscribeButton(reg);
      } else {
        setupTriggerButton(sub);
        iziToast.info({
          title: "[SERVICE WORKER]",
          balloon: true,
          position: "topRight",
          animateInside: true,
          message: "Push notification has already been subscribed to",
        });
      }
    });
  };

  //----------------------------------------------------------

  // -----------------------------------------------------------------
  // INSTALL BUTTON FOR PROGRESSIVE WEB APPLICATION
  // ------------------------------------------------------------------
  if (document.getElementById("installButton")){
    const installButton = document.getElementById("installButton");
  // when page loads for the first time, install button will be visible
  // if the user has not installed the app or PWA.
  window.addEventListener("beforeinstallprompt", (event) => {
    if (process.env.NODE_ENV === "development") {
      console.log("👍[PWA]", "beforeinstallprompt", event);
    }
    // Stash the event so it can be triggered later.
    window.deferredPrompt = event;
    // Remove the 'hidden' class from the install button container
    // if the PWA has been installed, hide the install button or if it has not
    // then allow for click
    installButton.classList.toggle("hidden", false);
  });

  installButton.addEventListener("click", () => {
    if (process.env.NODE_ENV === "development") {
      console.log("👍[PWA] Install Button Clicked");
    }

    const promptEvent = window.deferredPrompt;
    if (!promptEvent) {
      // The deferred prompt isn't available. so return nothing
      return;
    }
    promptEvent.prompt();
    promptEvent.userChoice.then((choice) => {
      if (process.env.NODE_ENV === "development") {
        console.log("👍[PWA] User Choice: ", choice);
      }
      // iziToast.success({
      //   title: `[PWA: ${choice}]`,
      //   message: '👍 You have successfully installed the readville app',
      // });
      // Reset the deferred prompt variable, since
      // prompt() can only be called once.
      window.deferredPrompt = null;
      // Hide the install button once the PWA has been installed
      installButton.classList.toggle("hidden", true);
    });
  });
  //----------------------------------------------------------
  }


  // if app is installed, thank the user for installing the app
  //----------------------------------------------------------
  window.addEventListener("appinstalled", (event) => {
    if (process.env.NODE_ENV === "development") {
      console.log("👍[PWA] Installed State: ", event);
    }

    iziToast.info({
      title: `[SERVICE WORKER]`,
      balloon: true,
      position: "topRight",
      animateInside: true,
      message: "Dropsride Appreciates Your Support.",
    });
  });
  //----------------------------------------------------------



  // HTMX Console logs
  if (process.env.NODE_ENV === "development") {
    // enable logging for htmx in development server only
    window.htmx.logAll();
  }

  [
    "htmx:onLoad",
    "htmx:load",
    "load",
    "htmx:afterSwap",
    "htmx:afterOnLoad",
    "htmx:afterRequest",
  ].forEach((evt) => {
    window.addEventListener(evt, function () {

    const counters = document.querySelectorAll(".counter");
    const car = document.getElementById('car');

    const controller = new ScrollMagic.Controller();

    // if(document.getElementById('const')){
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
        counters.forEach((counter) => {
          anime({
            targets: counter,
            innerHTML: [0, counter.getAttribute("data-count")],
            easing: "easeInOutSine",
            round: 1,
            duration: 4000,
          });
        });
      }
    }

    function animateHows() {
      if (document.querySelectorAll('.how')) {
        anime({
          targets: ".how",
          translateX: 56,
          easing: "easeInOutSine",
          duration: 800,
          opacity: 1,
          delay: anime.stagger(200, { start: 500 }),
        });
      }
    }

    if(document.getElementById('countTrigger')) {
      new ScrollMagic.Scene({
        triggerElement: '#countTrigger',
        triggerHook: 'onEnter',
        duration: '100%',
        reverse: false,
        offset: 50
      }).on('enter', function() {
        startCounting();
      }).addTo(controller);
    }

    if(document.getElementById('track')) {
        new ScrollMagic.Scene({
        triggerElement: '#track',
        triggerHook: 'onEnter',
        duration: '100%',
        reverse: true,
        offset: 50
      }).on('enter', function() {
        carDrive();
      }).addTo(controller);
    }


    if(document.getElementById('hows')) {
      new ScrollMagic.Scene({
        triggerElement: '#hows',
        triggerHook: 'onEnter',
        duration: '100%',
        reverse: false,
        offset: 100
      }).on('enter', function() {
        animateHows();
      }).addTo(controller);
    }

    if(document.querySelectorAll('.intro')) {
      anime({
        targets: ".intro",
        translateX: -56,
        easing: "easeInOutSine",
        duration: 800,
        opacity: 1,
        delay: anime.stagger(200, { start: 500 }),
      });
    }


    function carDrive() {
      if (car) {
        anime({
          targets: "#car",
          translateX: {
            value: "-100vw",
            duration: 5000,
          },
          easing: "easeInOutSine",
          opacity: 1,
          delay: anime.stagger(200, { start: 500 }),
          direction: "normal",
          loop: false,
        });
      }
    }
  });
});
