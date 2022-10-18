import { precacheAndRoute } from 'workbox-precaching/precacheAndRoute';
import { setCatchHandler, setDefaultHandler, registerRoute } from 'workbox-routing';
import { NetworkOnly, StaleWhileRevalidate } from 'workbox-strategies';
import { CacheableResponsePlugin } from "workbox-cacheable-response";
import { ExpirationPlugin } from "workbox-expiration";

const manifest = self.__WB_MANIFEST;
if (manifest) {
  console.log('precaching: ', manifest);
  precacheAndRoute(manifest);
}

// https://web.dev/offline-fallback-page/
const CACHE_NAME = 'offline-html';
const FALLBACK_HTML_URL = '/offline/';
const LOGO_URL = "/static/assets/favicon-48x48.png";


registerRoute(
  ({ url }) =>  url.origin === "https://fonts.googleapis.com" || url.origin === "https://fonts.gstatic.com",
  new StaleWhileRevalidate({
      cacheName: `google-fonts`,
      plugins: [
          new CacheableResponsePlugin({
              statuses: [0, 200],
          }),
          new ExpirationPlugin({ maxEntries: 20 }),
      ],
  })
);

registerRoute(
  ({ url }) =>  url.origin === "https://unpkg.com",
  new StaleWhileRevalidate({
      cacheName: `unpkg`,
      plugins: [
          new CacheableResponsePlugin({
              statuses: [0, 200],
          }),
          new ExpirationPlugin({ maxEntries: 20 }),
      ],
  })
);

registerRoute(
  ({ url }) =>  url.origin === "https://cdnjs.cloudflare.com",
  new StaleWhileRevalidate({
      cacheName: `cdnjs`,
      plugins: [
          new CacheableResponsePlugin({
              statuses: [0, 200],
          }),
          new ExpirationPlugin({ maxEntries: 20 }),
      ],
  })
);

registerRoute(
  ({ url }) =>  url.origin === "https://map.googleapis.com",
  new StaleWhileRevalidate({
      cacheName: `google-map`,
      plugins: [
          new CacheableResponsePlugin({
              statuses: [0, 200],
          }),
          new ExpirationPlugin({ maxEntries: 20 }),
      ],
  })
);

registerRoute(
  ({ url }) =>  url.origin === "https://api.tiles.mapbox.com",
  new StaleWhileRevalidate({
      cacheName: `mapbox-map`,
      plugins: [
          new CacheableResponsePlugin({
              statuses: [0, 200],
          }),
          new ExpirationPlugin({ maxEntries: 20 }),
      ],
  })
);

registerRoute(
  ({ request }) => request.destination === 'image',
  new StaleWhileRevalidate({
      cacheName: `image-cache`,
      plugins: [
          new CacheableResponsePlugin({
              statuses: [0, 200],
          }),
          new ExpirationPlugin({ maxEntries: 100, maxAgeSeconds: 30 * 24 * 60 * 60, }),
      ],
  })
);

registerRoute(
  ({ request }) => request.destination === 'audio',
  new StaleWhileRevalidate({
      cacheName: `audio-cache`,
      plugins: [
          new CacheableResponsePlugin({
              statuses: [0, 200],
          }),
          new ExpirationPlugin({ maxEntries: 60, maxAgeSeconds: 30 * 24 * 60 * 60, }),
      ],
  })
);

self.addEventListener('install',  (event) => {
  event.waitUntil(
    // Setting {cache: 'reload'} in the new request will ensure that the
    // response isn't fulfilled from the HTTP cache; i.e., it will be from
    // the network.
    caches.open(CACHE_NAME)
      .then((cache) => cache.add(
        new Request(FALLBACK_HTML_URL, { cache: "reload" })
      ))
  );

  // Force the waiting service worker to become the active service worker.
  self.skipWaiting();
});

self.addEventListener("activate", (event) => {
    console.log("👷", "activate", event);
  // Tell the active service worker to take control of the page immediately.
  self.clients.claim();
});

setDefaultHandler(
  new NetworkOnly()
);

// This "catch" handler is triggered when any of the other routes fail to
// generate a response.
setCatchHandler(({event}) => {
  // The FALLBACK_URL entries must be added to the cache ahead of time, either
  // via runtime or precaching. If they are precached, then call
  // `matchPrecache(FALLBACK_URL)` (from the `workbox-precaching` package)
  // to get the response from the correct cache.
  //
  // Use event, request, and url to figure out how to respond.
  // One approach would be to use request.destination, see
  // https://medium.com/dev-channel/service-worker-caching-strategies-based-on-request-types-57411dd7652c
  switch (event.request.destination) {
    case 'document':
      // If using precached URLs:
      // return matchPrecache(FALLBACK_HTML_URL);
      return caches.match(FALLBACK_HTML_URL);

    default:
      // If we don't have a fallback, just return an error response.
      return Response.error();
  }
});




// register event listener for the 'push' event.
self.addEventListener('push', function (event) {
  // Retrieve the textual payload from event.data (a PushMessageData object).
  // Other formats are supported (ArrayBuffer, Blob, JSON), check out the documentation
  // on https://developer.mozilla.org/en-US/docs/Web/API/PushMessageData.

  let notificationTitle = 'Push Notification';
  let notificationOptions;

  try {
    // Push is a JSON
    const responseJson = event.data.json();
    notificationTitle = responseJson.head.toUpperCase();
    if (responseJson.url !== undefined) {
      notificationOptions = {
        body: responseJson.body,
        icon: LOGO_URL,
        data: {url:responseJson.url ? responseJson.url : window.location.origin},
        actions: [{action: "open_url", title: "Open Link"}],
        vibrate: [200, 100, 200, 100, 200, 100, 200],
      };
    } else {
      notificationOptions = {
        body: responseJson.body,
        icon: LOGO_URL,
        vibrate: [200, 100, 200, 100, 200, 100, 200],
      };
    }
  } catch (err) {
    // Push is a simple text (usually debugging)
    notificationOptions = {
      icon: LOGO_URL,
      body: event.data.text(),
    };
  }

  // Keep the service worker alive until the notification is created.
  event.waitUntil(
    self.registration.showNotification(
      notificationTitle,
      notificationOptions
    )
  );
});

self.addEventListener('notificationclick', function(event) {
    if (event.notification.data !== null) {
      event.waitUntil(
        event.preventDefault(),
        event.notification.close(),
        self.clients.openWindow(event.notification.data.url)
      );
    }
});
