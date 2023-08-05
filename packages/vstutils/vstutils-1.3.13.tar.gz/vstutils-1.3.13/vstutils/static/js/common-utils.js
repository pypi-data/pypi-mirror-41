
// List of Gui Testing Files
if(!window.guiTestsFiles)
{
    window.guiTestsFiles = []
}

// Add a test file to the list of files for test gui
window.guiTestsFiles.push(hostname + window.guiStaticPath + 'js/tests/qUnitTest.js')
window.guiTestsFiles.push(hostname + window.guiStaticPath + 'js/tests/guiPaths.js')

window.guiTestsFiles.push(hostname + window.guiStaticPath + 'js/tests/guiElements.js')
window.guiTestsFiles.push(hostname + window.guiStaticPath + 'js/tests/guiCommon.js')
window.guiTestsFiles.push(hostname + window.guiStaticPath + 'js/tests/guiUsers.js')
window.guiTestsFiles.push(hostname + window.guiStaticPath + 'js/tests/guiSignals.js')

// Run tests
function loadQUnitTests()
{
    loadAllUnitTests(window.guiTestsFiles)
}

// Loads and runs tests in strict order.
function loadAllUnitTests(urls)
{
    let promises = []
    for(let i in urls)
    {
        let def = new $.Deferred();
        promises.push(def.promise());

        var link = document.createElement("script");
        link.setAttribute("type", "text/javascript");
        link.setAttribute("src", urls[i]+'?r='+Math.random());

        link.onload = function(def){
            return function(){
                def.resolve();
            }
        }(def)
        document.getElementsByTagName("head")[0].appendChild(link);

        break;
    }

    $.when.apply($, promises).done(() => {
        //injectQunit()

        if(urls.length == 1)
        {
            return injectQunit()
        }
        urls.splice(0, 1)
        loadAllUnitTests(urls)
    })
}




/**
 * Function to replace {.+?} in string to variables sended to this function,
 * array and single variable set ordered inside string
 * associative array and iterable objects set value for keys that original string have
 * @param takes array, associative array or single variable and insert it
 * @returns {String} - return string with inserted arguments
 */
String.prototype.format = function()
{
    let obj = this.toString();
    let arg_list;
    if (typeof arguments[0] == "object")
    {
        arg_list = arguments[0]
    }
    else if (arguments.length >= 1)
    {
        arg_list = Array.from(arguments);
    }
    for (let key of this.format_keys())
    {
        if (arg_list[key] != undefined)
        {
            obj = obj.replace('{'+ key + '}', arg_list[key])
        }
        else
        {
            throw "String don't have \'" + key + "\' key";
        }
    }
    return obj;
}

/**
 * Function search and return all `{key}` in string
 * @returns {array} array of {key} in string
 */
String.prototype.format_keys = function()
{
    let thisObj = this;
    //let regex = new RegExp("(?<={).+?(?=})", "g");
    //let match = thisObj.match(regex)
    //return match || [];
    let res = thisObj.match(/{([^\}]+)}/g)
    if(!res)
    {
        return []
    }

    return res.map((item) =>{ return item.slice(1, item.length - 1) })
}

function addslashes(string) {
    return string.replace(/\\/g, '\\\\').
    replace(/\u0008/g, '\\b').
    replace(/\t/g, '\\t').
    replace(/\n/g, '\\n').
    replace(/\f/g, '\\f').
    //replace(/\r/g, '\\r').
    //replace(/\a/g, '\\a').
    replace(/\v/g, '\\v').
    //replace(/\e/g, '\\e').
    replace(/'/g, '\\\'').
    replace(/"/g, '\\"');
}

function stripslashes (str) {
    //       discuss at: http://locutus.io/php/stripslashes/
    //      original by: Kevin van Zonneveld (http://kvz.io)
    //      improved by: Ates Goral (http://magnetiq.com)
    //      improved by: marrtins
    //      improved by: rezna
    //         fixed by: Mick@el
    //      bugfixed by: Onno Marsman (https://twitter.com/onnomarsman)
    //      bugfixed by: Brett Zamir (http://brett-zamir.me)
    //         input by: Rick Waldron
    //         input by: Brant Messenger (http://www.brantmessenger.com/)
    // reimplemented by: Brett Zamir (http://brett-zamir.me)
    //        example 1: stripslashes('Kevin\'s code')
    //        returns 1: "Kevin's code"
    //        example 2: stripslashes('Kevin\\\'s code')
    //        returns 2: "Kevin\'s code"
    return (str + '')
        .replace(/\\(.?)/g, function (s, n1) {
            switch (n1) {
                case '\\':
                    return '\\'
                case '0':
                    return '\u0000'
                case 't':
                    return "\t"
                case 'n':
                    return "\n"
                case 'f':
                    return "\f"
                //case 'e':
                //  return "\e"
                case 'v':
                    return "\v"
                //case 'a':
                //  return "\a"
                case 'b':
                    return "\b"
                //case 'r':
                //  return "\r"
                case '':
                    return ''
                default:
                    return n1
            }
        })
}
/**
 * Тестовый тест, чтоб было видно что тесты вообще хоть как то работают.
 */
function trim(s)
{
    if(s) return s.replace(/^ */g, "").replace(/ *$/g, "")
    return '';
}


function inheritance(obj, constructor)
{
    var object = undefined;
    var item = function()
    {
        if(constructor)
        {
            return constructor.apply(jQuery.extend(true, item, object), arguments);
        }

        return jQuery.extend(true, item, object);
    }

    object = jQuery.extend(true, item, obj)

    return object
}

function toIdString(str)
{
    return str.replace(/[^A-z0-9\-]/img, "_").replace(/[\[\]]/gi, "_");
}

function hidemodal()
{
    var def = new $.Deferred();
    $(".modal.fade.in").on('hidden.bs.modal', function (e) {
        def.resolve();
    })
    $(".modal.fade.in").modal('hide');

    return def.promise();
}


function capitalizeString(string)
{
    if(!string)
    {
        return "";
    }

    return string.charAt(0).toUpperCase() + string.slice(1).toLowerCase();
}

function sliceLongString(string="", valid_length=100)
{
    if(typeof string != "string")
    {
        return sliceLongString(""+string, valid_length);
    }

    var str = string.slice(0, valid_length);
    if(string.length > valid_length)
    {
        str += "...";
    }

    return str;
}

function isEmptyObject(obj)
{
    for (var i in obj) {
        if (obj.hasOwnProperty(i)) {
            return false;
        }
    }
    return true;
}

function readFileAndInsert(event, element)
{
    for (var i = 0; i < event.target.files.length; i++)
    {
        if (event.target.files[i].size > 1024 * 1024 * 1)
        {
            guiPopUp.error("File is too large")
            console.log("File is too large " + event.target.files[i].size)
            continue;
        }

        var reader = new FileReader();

        reader.onload = function (e)
        {
            $(element).val(e.target.result);
        }

        reader.readAsText(event.target.files[i]);
    }

    return false;
}

function addCssClassesToElement(element="", title, type)
{
    element = element.replace(/[\s\/]+/g,'-');

    let class_list = element + " ";

    if(title)
    {
        title = title.replace(/[\s\/]+/g,'-');
        class_list += element + "_" + title + " ";
    }


    if(title && type)
    {
        type = type.replace(/[\s\/]+/g,'-');
        class_list += element + "_" + type + " ";
        class_list += element + "_" + type + "_" + title;
    }

    return class_list.toLowerCase();
}

function addStylesAndClassesToListField(guiObj, field, data, opt)
{
    let output = "";

    if(field.style)
    {
        output += field.style.apply(guiObj, [data, opt]) + " ";
    }

    if(field.class)
    {
        output += field.class.apply(guiObj, [data, opt]) + " ";
    }
    else
    {
        output += "class='" + addCssClassesToElement('td', field.name, guiObj.api.short_name) + "' ";
    }

    return output;
}

/**
 * Function handles click on table row (<tr>), and depending to the place of user's click
 * it redirects user to <tr> link or to <td> link.
 * @param object - event - click event.
 * @param boolean - blank - if true, function opens link in new window.
 */
function turnTableTrIntoLink(event, blank)
{
    if(!blockTrLink(event.target, 'tr', 'highlight-tr-none'))
    {
        let href;
        if(event.target.hasAttribute('href'))
        {
            href =  event.target.getAttribute('href');
        }
        else if(event.currentTarget)
        {
            href =  event.currentTarget.getAttribute('data-href');
        }
        else
        {
            href =  event.target.getAttribute('data-href');
        }

        if(blank)
        {
            window.open(href);
        }
        else
        {
            vstGO(href);
        }
    }
}

/**
 * Function makes recursive search through DOM tree
 * and tries to find a search_class in the classList of DOM elements.
 * If function finds this search_class, it returns true.
 * Otherwise, it returns false.
 * @param object - element - DOM tree element.
 * @param string - stop_element_name - name of DOM tree element on which function stops search.
 * @param string - search_class - name of CSS class, which function tries to find.
 */
function blockTrLink(element, stop_element_name, search_class)
{
    if(!element)
    {
        return false;
    }

    if(element.classList.contains(search_class))
    {
        return true;
    }

    if(element.parentElement && element.parentElement.localName != stop_element_name)
    {
        return blockTrLink(element.parentElement, stop_element_name, search_class);
    }

    return false;
}

/*
 * Hides field 'id' in list.
 * This function is calling from signal openapi.schema.type.list
 */
function hideIdInList(listObj)
{
    try
    {
        let fields = listObj.value.schema.list.fields;
        if(fields['id'])
        {
            fields['id'].hidden = true;
        }
    }
    catch(e)
    {
        console.warn(e);
    }

}

tabSignal.connect("openapi.schema.type.list", function(listObj)
{
    hideIdInList.apply(this, arguments);
})

window.current_window_width = window.innerWidth;

window.onresize=function ()
{
    window.current_window_width = window.innerWidth;

    if(window.innerWidth>991)
    {
        if(guiLocalSettings.get('hideMenu'))
        {
            $("body").addClass('sidebar-collapse');
        }
        if ($("body").hasClass('sidebar-open'))
        {
            $("body").removeClass('sidebar-open');
        }
    }
    else
    {
        if ($("body").hasClass('sidebar-collapse')){
            $("body").removeClass('sidebar-collapse');
        }
    }
}

/**
 * Function is supposed to be called when push-menu button was clicked.
 */
function saveHideMenuSettings()
{
    if(window.innerWidth > 991)
    {
        if($('body').hasClass('sidebar-collapse'))
        {
            guiLocalSettings.set('hideMenu', false);
        }
        else
        {
            guiLocalSettings.set('hideMenu', true);
        }
    }
}

/**
 * Function makes a decision about grouping buttons or not.
 * The decision is based on analysis of width of window and buttons amount.
 */
function groupButtonsOrNot(window_width, buttons)
{
    let buttons_amount = 0;
    if(typeof buttons == "number")
    {
        buttons_amount = buttons;
    }
    else if(typeof buttons == "string")
    {
        buttons_amount = Number(buttons) || 0;
    }
    else if(typeof buttons == "object")
    {
        if($.isArray(buttons))
        {
            buttons_amount = buttons.length;
        }
        else
        {
            buttons_amount = Object.keys(buttons).length;
        }

        for(let i in buttons)
        {
            if(buttons[i].hidden)
            {
                buttons_amount--;
            }
        }
    }

    if(buttons_amount < 2)
    {
        return false;
    }
    else if(buttons_amount >= 2 && buttons_amount < 5)
    {
        if(window_width >= 992)
        {
            return false;
        }
    }
    else if(buttons_amount >= 5 && buttons_amount < 8 )
    {
        if(window_width >= 1200)
        {
            return false;
        }
    }
    else if(buttons_amount >= 8)
    {
        if(window_width >= 1620)
        {
            return false;
        }
    }

    return true;
}

var guiLocalSettings = {
    __settings:{ // object for storing current settings (including tmpSettings)
    },
    __tmpSettings: { // object for storing tmpSettings
    },
    __beforeAsTmpSettings: { // object for storing setting value, as it was before user set tmpSettings value
    },
    __removeTmpSettings: function() { // function removes tmpSettings from current settings and add previous values (if they were)
        for(var item in this.__tmpSettings)
        {
            if(this.__beforeAsTmpSettings[item])
            {
                this.__settings[item] = this.__beforeAsTmpSettings[item];
            }
            else
            {
                delete this.__settings[item];
            }
        }
    },
    get:function(name){
        return this.__settings[name];
    },
    delete:function(name){
        this.__removeTmpSettings();
        delete this.__settings[name];
        delete this.__tmpSettings[name];
        delete this.__beforeAsTmpSettings[name];
        window.localStorage['guiLocalSettings'] = JSON.stringify(this.__settings);
    },
    set:function(name, value){
        this.__removeTmpSettings();
        this.__settings[name] = value;
        window.localStorage['guiLocalSettings'] = JSON.stringify(this.__settings);
        tabSignal.emit('guiLocalSettings.'+name, {type:'set', name:name, value:value});
    },
    setAsTmp:function(name, value){
        if(this.__settings[name])
        {
            this.__beforeAsTmpSettings[name] = this.__settings[name];
        }
        this.__settings[name] = value;
        this.__tmpSettings[name] = value;
        tabSignal.emit('guiLocalSettings.'+name, {type:'set', name:name, value:value});
    },
    setIfNotExists:function(name, value){
        if(this.__settings[name] === undefined)
        {
            this.__settings[name] = value;
        }
    }
}

if(window.localStorage['guiLocalSettings'])
{
    try{
        guiLocalSettings.__settings = window.localStorage['guiLocalSettings'];
        guiLocalSettings.__settings = JSON.parse(guiLocalSettings.__settings)

    }catch (e)
    {

    }
}

function getNewId(){
    return ("id_"+ Math.random()+ "" +Math.random()+ "" +Math.random()).replace(/\./g, "")
}



window.url_delimiter = "#"
function vstMakeLocalUrl(url = "", vars = {})
{
    if(Array.isArray(url))
    {
        url = url.join("/")
    }

    if(typeof url == "string")
    {
        let new_url = url.format(vars)

        if(new_url.indexOf(window.hostname) != 0 && new_url.indexOf("//") != 0)
        {
            new_url = window.hostname + window.url_delimiter + new_url
        }
        else
        {
            //console.error("window.hostname already exist in vstMakeLocalUrl")
        }
        url = new_url.replace("#/", "#")
    }
    else
    {
        debugger;
        throw "Error in vstMakeLocalUrl"
    }

    return url.replace("#", "#/")
}


function vstGO()
{
    return spajs.openURL(vstMakeLocalUrl.apply(this, arguments))
}





function makeUrlForApiKeys(url_string)
{
    return url_string.replace(/\{([A-z0-9]+)\}/g, "{api_$1}")
}

function vstMakeLocalApiUrl(url, vars = {})
{
    if(Array.isArray(url))
    {
        url = url.join("/")
    }

    return vstMakeLocalUrl(makeUrlForApiKeys(url), vars)
}

function openHelpModal()
{
    let info = api.openapi.info;
    let opt = {};
    if(info.title)
    {
        opt.title = info.title;
    }
    let html = spajs.just.render('help_modal_content', {info: info});
    guiModal.setModalHTML(html, opt);
    guiModal.modalOpen();
}

/**
 * https://stackoverflow.com/a/25456134/7835270
 * @param {type} x
 * @param {type} y
 * @returns {Boolean}
 */
function deepEqual(x, y)
{
    if ((typeof x == "object" && x != null) && (typeof y == "object" && y != null))
    {
        if (Object.keys(x).length != Object.keys(y).length)
        {
            return false;
        }

        for (var prop in x)
        {
            if (y.hasOwnProperty(prop))
            {
                if (! deepEqual(x[prop], y[prop]))
                {
                    return false;
                }
            }
            else
            {
                return false;
            }
        }

        return true;
    }
    else if (x !== y)
    {
        return false;
    }
    else
    {
        return true;
    }
}

/**
 * Function checks string for keeping boolean value
 * @param {string} string - string, which we want to check on boolean value
 * @returns {Boolean}
 */
function stringToBoolean(string){

    if(string == null)
    {
        return false;
    }

    switch(string.toLowerCase().trim()){
        case "true": case "yes": case "1": return true;
        case "false": case "no": case "0": case null: return false;
    }
}

/**
 * Function for search on JS (when there is no opportunity to use API search).
 * Function gets 2 arguments:
 * @param {object} filters - object with search filters
 * @param {array} data - array with list of objects.
 * @returns {array} - search_results - data, that satisfies search filters.
 */
function searchObjectsInListByJs(filters, data)
{
    if(!data)
    {
        data = [];
    }

    if(!filters)
    {
        filters = {
            search_query: {}
        }
    }

    let search_results = [];

    let search_query_keys = Object.keys(filters.search_query);

    // in this loop we add to search results all objects from data
    // that satisfy the first search_query key
    for(let i in data)
    {
        let item = data[i];

        let search_key = search_query_keys[0];
        let search_value = filters.search_query[search_key];

        if(checkDataValidityForSearchQuery(item[search_key], search_value))
        {
            search_results.push(item);
        }
    }

    // in this loop we delete from search results all objects
    // that do not satisfy other search_query keys
    for(let i = 1; i < search_query_keys.length; i++)
    {
        let search_key = search_query_keys[i];
        let search_value =  filters.search_query[search_key];

        for(let j = 0; j < search_results.length; j++)
        {
            let item = search_results[j];

            if(!checkDataValidityForSearchQuery(item[search_key], search_value))
            {
                search_results.splice(j, 1);
                j -= 1;
            }
        }
    }

    return search_results;
}

/**
 * Function checks validity of data value to search query.
 * If it is valid, function returns true.
 * Otherwise, function returns false.
 * Function gets 2 arguments:
 * @param {string, number, boolean} data_value - data value
 * @param {string, number, boolean} search_value - search query
 * @returns {boolean}
 */
function checkDataValidityForSearchQuery(data_value, search_value)
{
    let valid = false;

    if(typeof data_value == 'string')
    {
        if(data_value.match(search_value) != null)
        {
            valid = true;
        }
    }
    else
    {
        if(typeof data_value == 'boolean' && typeof search_value == 'string')
        {
            search_value = stringToBoolean(search_value);
        }

        if(data_value == search_value)
        {
            valid = true;
        }
    }

    return valid;
}

/**
 * Function converts numbers from 0 to 9 into 00 to 09.
 * @param n(number) - number
 */
function oneCharNumberToTwoChar(n){
    return n > 9 ? "" + n: "0" + n;
}

/**
 * Function checks necessity of opening link in default browser in cordova app.
 */
function openExternalLink(event)
{
    if(isCordova())
    {
        let url = event.target.activeElement.href;
        window.parent.cordova.InAppBrowser.open(url, '_blank', 'location=yes');
        event.preventDefault()
        return false;
    }
}

window.onbeforeunload = openExternalLink;

if(isCordova())
{
    window.onunload = function(){
        inAppClose()
    }
}

/**
 * Function checks that all properties of object are also objects.
 * @param obj(object) - some object
 * @returns {boolean}
 */
function allPropertiesIsObjects(obj)
{
    for(let prop in obj)
    {
        if(typeof obj[prop] != 'object')
        {
            return false;
        }
        else
        {
            if($.isArray(obj[prop]))
            {
                return false;
            }
        }
    }
    return true;
}

/**
 * @param {type} f
 * @param {type} ms
 * @returns {Function}
 * @see https://learn.javascript.ru/task/debounce
 */
function debounce(f, ms) {

    let timer = null;

    return function (...args) {
        const onComplete = () => {
            f.apply(this, args);
            timer = null;
        }

        if (timer) {
            clearTimeout(timer);
        }

        timer = setTimeout(onComplete, ms);
    };
}

function addTableEntityClass(guiObj)
{
    let class_name = "";
    if(guiObj && guiObj.api && guiObj.api.extension_class_name)
    {
        if(typeof(guiObj.api.extension_class_name) == 'string')
        {
            class_name = guiObj.api.extension_class_name;
        }
        else if(Array.isArray(guiObj.api.extension_class_name) && guiObj.api.extension_class_name.length > 0)
        {
            class_name = String(guiObj.api.extension_class_name[0]);
        }
    }

    return  class_name.replace('gui_', '');
}

/**
 * Function hides sidebar on small screens.
 * Function calls when user click on a link from sidebar menu.
 */
function hideSidebar()
{
    if(window.innerWidth <= 991)
    {
        $('body').removeClass('sidebar-open');
        $('body').addClass('sidebar-collapse');
    }
}

/**
 * Function opens/collapses inner menu(".nav-treeview") of the sidebar element.
 */
function toggleMenuOpen(el, event)
{
    event.stopPropagation();

    let li = el.parentElement.parentElement.parentElement;
    let ul = $(li).find('ul.nav-treeview');

    $(li).toggleClass('menu-open');
    $(ul).slideToggle(300);

    setTimeout(function()
    {
        if($(li).hasClass('menu-open'))
        {
            $(ul).attr("style", "display:block;")
        }
        else
        {
            $(ul).attr("style", "display:none;")
        }
    }, 301)
}

function setActiveMenuLi( )
{
    let url = window.location.hash.replace("#", "")
    $(".nav-sidebar li[data-url]").removeClass("active");
    $(".nav-sidebar a.nav-link").removeClass('active')

    $(".nav-sidebar .menu-open").removeClass('menu-open')
    $(".nav-sidebar .nav-treeview").hide()

    let li = $(".nav-sidebar li[data-url]")

    let urllevel = url.split("/").length - 1

    for(let i=0; i< li.length; i++)
    {
        let val = $(li[i])
        let dataurl = val.attr('data-url')

        if(dataurl == "" && urllevel >= 1)
        {
            continue;
        }

        if(urllevel > 1 && url.indexOf(dataurl) != 0)
        {
            continue;
        }

        if(urllevel <= 1 && url != dataurl)
        {
            continue;
        }

        if(val.hasClass('has-treeview'))
        {
            val.addClass("menu-open")
            val.children(".nav-treeview").show()
        }

        val.children("a.nav-link").addClass('active')

        let parent = val.parent()
        let step = 0;
        do{
            step++;
            if($(parent).hasClass('has-treeview'))
            {
                $(parent).addClass("menu-open")
                parent.children(".nav-treeview").show()
            }
            parent = $(parent).parent()

        }while(parent.length && step < 10)

        break;
    }
}

tabSignal.connect("spajs.open", setActiveMenuLi);
tabSignal.connect("loading.completed", setActiveMenuLi)

/*
 * 2 handlers, that removes CSS-class 'hover-li' from menu elements, after losing focus on them.
 */
$(".content-wrapper").hover(function () {
    $(".hover-li").removeClass("hover-li");
})

$(".navbar").hover(function () {
    $(".hover-li").removeClass("hover-li");
})

/**
 * Function converts color from hex to rgba.
 */
function hexToRgbA(hex, alpha)
{
    if(alpha === undefined)
    {
        alpha = 1;
    }

    if(typeof(alpha) != "number")
    {
        alpha = Number(alpha);
        if(isNaN(alpha))
        {
            alpha = 1;
        }
    }

    if(alpha < 0 || alpha > 1)
    {
        alpha = 1;
    }

    let c;
    if(/^#([A-Fa-f0-9]{3}){1,2}$/.test(hex)){
        c= hex.substring(1).split('');
        if(c.length== 3){
            c= [c[0], c[0], c[1], c[1], c[2], c[2]];
        }
        c= '0x'+c.join('');
        return 'rgba('+[(c>>16)&255, (c>>8)&255, c&255].join(',')+',' + alpha +')';
    }
    return;
}

/**
 * Function returns prefetch text if prefetch exists, otherwise, it returns field value.
 * @param opt {object} - options for page/list render.
 * @param dataLine {object} - object with data from API.
 * @param field_name {string} - name of field
 * @param max_length {number} - max length of return text.
 * @returns {html}
 */
function getPrefetchText(opt, dataLine, field_name, max_length) {
    if(!max_length){
        max_length = 100;
    }

    if(opt.fields[field_name].prefetch && dataLine[field_name + '_info']) {
        if(opt.fields['job'].prefetch.field_name && dataLine[field_name + '_info'][opt.fields['job'].prefetch.field_name]){
            return sliceLongString(dataLine[field_name + '_info'][opt.fields['job'].prefetch.field_name], max_length);
        } else if (dataLine[field_name + '_info'].name) {
            return sliceLongString(dataLine[field_name + '_info'].name, max_length)
        }

    }

    return sliceLongString(dataLine[field_name], max_length);
}