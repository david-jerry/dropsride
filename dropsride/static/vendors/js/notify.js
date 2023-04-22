/* eslint-disable no-unused-vars */
var notify_badge_class;
var notify_menu_class;
var notify_api_url;
var notify_fetch_count;
var notify_unread_url;
var notify_mark_all_unread_url;
var notify_refresh_period = 15000;
var consecutive_misfires = 0;
var registered_functions = [];

// eslint-disable-next-line no-unused-vars
function fill_notification_badge(data) {
    var badges = document.getElementsByClassName(notify_badge_class);
    if (badges) {
        for(var i = 0; i < badges.length; i++){
            badges[i].innerHTML = data.unread_count;
        }
    }
}

function my_special_notification_callback(data) {
    let menu = document.getElementsByClassName('live_notify_list');
    let message = "";
    let icon = "";
    let title = "";

    if (menu) {
      var messages = data.unread_list.map(function (item) {
        if(typeof item.verb !== 'undefined'){
            icon = '<h6 class="text-warning p-2 bg-warning/40 rounded-full object-fit flex-none"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" class="w-4 h-4"><path fill-rule="evenodd" d="M15.75 1.5a6.75 6.75 0 00-6.651 7.906c.067.39-.032.717-.221.906l-6.5 6.499a3 3 0 00-.878 2.121v2.818c0 .414.336.75.75.75H6a.75.75 0 00.75-.75v-1.5h1.5A.75.75 0 009 19.5V18h1.5a.75.75 0 00.53-.22l2.658-2.658c.19-.189.517-.288.906-.22A6.75 6.75 0 1015.75 1.5zm0 3a.75.75 0 000 1.5A2.25 2.25 0 0118 8.25a.75.75 0 001.5 0 3.75 3.75 0 00-3.75-3.75z" clip-rule="evenodd" /></svg></h6>';
            title = `<h6 class="text-gray-700 font-bold text-sm">${item.verb}</h6>`;
        }
        if(typeof item.description !== 'undefined'){
            message += '<p class="font-semibold text-gray-600 text-s line-clamp-5 leading-3 block break-words">' + item.description + "</h6>";
        }
        if(typeof item.timestamp !== 'undefined'){
            message += '<p class="time">' + new Date(item.timestamp).toLocaleDateString('en-US', {
              day:   'numeric',
              month: 'short',
              year:  'numeric',
            }); + '</p>';
        }
        // var unread = ((item.unread) ? 'unread' : 'read');
        return `
        <li @click="markRead(${item.id})" class=" unread">
            <div class="space-x-1 flex items-center">${icon} ${title}</div>
            <div class="space-y-1 line-clamp-1 break-words w-full flex-none">
                ${message}
            </div>
        </li>
        `;
      }).join('');

      for (var i=0; i < menu.length; i++) {
          menu[i].innerHTML = messages;
      }
    }
}

// eslint-disable-next-line no-unused-vars
function fill_notification_list(data) {
    var menus = document.getElementsByClassName(notify_menu_class);
    if (menus) {
        var messages = data.unread_list.map(function (item) {
            var message = "";
            if(typeof item.actor !== 'undefined'){
                message = item.actor;
            }
            if(typeof item.verb !== 'undefined'){
                message = message + " " + item.verb;
            }
            if(typeof item.target !== 'undefined'){
                message = message + " " + item.target;
            }
            if(typeof item.timestamp !== 'undefined'){
                message = message + " " + item.timestamp;
            }
            return '<li>' + message + '</li>';
        }).join('');

        for (var i = 0; i < menus.length; i++){
            menus[i].innerHTML = messages;
        }
    }
}

// eslint-disable-next-line no-unused-vars
function register_notifier(func) {
    registered_functions.push(func);
}

function fetch_api_data() {
    if (registered_functions.length > 0) {
        //only fetch data if a function is setup
        var r = new XMLHttpRequest();
        r.addEventListener('readystatechange', function(event){
            console.log(event);
            if (this.readyState === 4){
                if (this.status === 200){
                    consecutive_misfires = 0;
                    var data = JSON.parse(r.responseText);
                    for(var i = 0; i < registered_functions.length; i++) {
                       registered_functions[i](data);
                    }
                }else{
                    consecutive_misfires++;
                }
            }
        });
        r.open("GET", notify_api_url+'?max='+notify_fetch_count, true);
        r.send();
    }
    if (consecutive_misfires < 10) {
        setTimeout(fetch_api_data,notify_refresh_period);
    } else {
        var badges = document.getElementsByClassName(notify_badge_class);
        if (badges) {
            for (var i = 0; i < badges.length; i++){
                badges[i].innerHTML = "!";
                badges[i].title = "Connection lost!";
            }
        }
    }
}

setTimeout(fetch_api_data, 1000);
