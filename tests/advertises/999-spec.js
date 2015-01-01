var ad = require('../999.json');
var creds = require('../../creds.json');
var base_url = "http://999.md/";

module.exports = {
    "Open the Website" : function (browser) {
        browser
            .url(base_url)
            .waitForElementVisible('body', 1000, true, function() {}, 'Wait for 999 to load')
            .click('.header_menu_nav a[data-popup="login"]')
            .assert.visible('#topbar-popup', 'Popup Window is open');
    },

    "Login" : function (browser) {
        browser.getAttribute('#topbar-popup', 'src', function (result) {
            browser.url(result.value)
                .setValue('.popup-login-form-control input[name="login"]', creds.user)
                .setValue('.popup-login-form-control input[name="password"]', creds.pass)
                .pause(200)
                .click('.popup-login-form-footer button[type="submit"]');
        });
    },

    "Go To Advertise Page" : function (browser) {
        browser.url(base_url).waitForElementVisible('body', 1000, true, function() {}, 'Wait for 999 to load');
        browser.url(ad.url).waitForElementVisible('body', 1000, true, function () {

            browser.useXpath();
            handleValue(browser, ad.data);

        }, 'Add the Advertise Text');
    },

    "Place the Advertise" : function (browser) {
        // browser.useCss().pause(500).click('.board__content__further__body').pause(100000).end();
    }
};

function handleValue(browser, data) {
    var value = data.shift();

    for(var key in value) {

        if(typeof value[key] == 'string') {
            browser.click(value[key], function () {
                if( data.length ) handleValue(browser, data);
            });
        }
        else {
            if(key == 'number') {
                browser.setValue(value[key][0], parseInt(value[key][1]), function () {
                    if( data.length ) handleValue(browser, data);
                });
            }
            else
            {
                browser.setValue(value[key][0], value[key][1], function () {
                    if( data.length ) handleValue(browser, data);
                });
            }
        }

    }
}
