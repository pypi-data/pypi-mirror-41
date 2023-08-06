var currentDetailModule = null;
var remoteModuleInfo = {};
var localModuleInfo = {};
var filter = {};
var installQueue = [];
var installInfo = {};
var baseModuleNames = [];
var storeUrl = null;
var storeurl = $.get('/store/getstoreurl').done(function(response) {
    storeUrl = response;
});
var newModuleAvailable = false;
var storeFirstOpen = true;
var storeTileWidthStep = 294;
var modulesToIgnore = [
    'aggregator',
];
var storeLogos = {};

function getEl(tag){
	var new_node = document.createElement(tag);
	return new_node;
}

function getTn(text){
	var new_text_node = document.createTextNode(text);
	return new_text_node;
}

function addEl (pelem, child) {
	pelem.appendChild(child);
	return pelem;
}

function onClickStoreHome () {
    var homediv = document.getElementById('store-home-div');
    var allDiv = document.getElementById('store-allmodule-div');
    var homeButton = document.getElementById('store-home-button');
    var homeButtonClass = homeButton.className;
    if (homeButtonClass == 'store-front-all-button-on') {
        homediv.style.display = 'none';
        allDiv.style.display = 'block';
        homeButton.className = 'store-front-all-button-off';
        updateFilter();
    } else if (homeButtonClass == 'store-front-all-button-off') {
        homediv.style.display = 'block';
        allDiv.style.display = 'none';
        homeButton.className = 'store-front-all-button-on';
        document.getElementById('store-tag-reset-button').className = 'store-front-all-button-off';
    }
}

function onClickStoreTagResetButton () {
    document.getElementById('store-namefilter').value = '';
    $('.store-tag-checkbox').each(function () {
        this.checked = false;
    });
    updateFilter();
    document.getElementById('store-home-button').className = 'store-front-all-button-off';
    document.getElementById('store-tag-reset-button').className = 'store-front-all-button-on';
}

function clickTab (value) {
    var tabs = document.getElementById('pageselect').children;
    for (var i = 0; i < tabs.length; i++) {
        var tab = tabs[i];
        if (tab.getAttribute('value') == value) {
            tab.click();
            return;
        }
    }
}

function getLocal () {
	$.get('/store/local').done(function(data){
        localModuleInfo = data;
        newModuleAvailable = false;
        var moduleNamesInInstallQueue = Object.keys(installInfo);
        for (var remoteModuleName in remoteModuleInfo) {
            var mI = remoteModuleInfo[remoteModuleName];
            var tags = mI['tags'];
            if (tags == null) {
                tags = [];
                mI['tags'] = tags;
            }
            if (remoteModuleName in localModuleInfo) {
                var idx = tags.indexOf('installed');
                if (idx == -1) {
                    tags.push('installed');
                }
                if (moduleNamesInInstallQueue.indexOf(remoteModuleName) == -1) {
                    var localVersion = localModuleInfo[remoteModuleName].version;
                    var remoteVersion = getHighestVersionForRemoteModule(remoteModuleName);
                    c = compareVersion(remoteVersion, localVersion);
                    if (c > 0) {
                        var idx = tags.indexOf('newavailable');
                        if (idx == -1) {
                            tags.push('newavailable');
                        }
                        newModuleAvailable = true;
                    } else {
                        var idx = tags.indexOf('newavailable');
                        if (idx >= 0) {
                            tags.splice(idx, 1);
                        }
                    }
                }
            } else {
                var idx = tags.indexOf('installed');
                if (idx >= 0) {
                    tags.splice(idx, 1);
                }
            }
        }
        for (var mn in localModuleInfo) {
            var localModule = localModuleInfo[mn];
            if (! ('tags' in localModule)) {
                localModule['tags'] = [];
            }
            var remoteModule = remoteModuleInfo[mn];
            if (remoteModule == undefined) {
                continue;
            }
            var localTags = localModule.tags;
            var remoteTags = remoteModule.tags;
            for (var i = 0; i < localTags.length; i++) {
                var tag = localTags[i];
                if (remoteTags.indexOf(tag) == -1) {
                    remoteTags.push(tag);
                }
            }
            remoteModule.tags = remoteTags;
        }
        var baseInstalled = true;
        var moduleNamesInInstallQueue = Object.keys(installInfo);
        var baseToInstall = [];
        for (var i = 0; i < baseModuleNames.length; i++) {
            var baseModuleName = baseModuleNames[i];
            if (! (baseModuleName in localModuleInfo)) {
                baseInstalled = false;
                if (moduleNamesInInstallQueue.indexOf(baseModuleName) == -1) {
                    baseToInstall.push(baseModuleName);
                }
            }
        }
        var div = document.getElementById('remotemodulepanels');
        if (div == null) {
            return;
        }
        if (baseInstalled) {
            trimRemote();
            var div = document.getElementById('messagediv');
            div.style.display = 'none';
            div = document.getElementById('remotemodulepanels');
            var input = document.getElementById('store-namefilter');
            input.disabled = false;
            var div = document.getElementById('moduledetaildiv_store');
            if (div != null) {
                if (div.style.display != 'none') {
                    activateDetailDialog(currentDetailModule);
                }
            }
            populateStoreHome();
            populateAllModulesDiv();
            if (storeFirstOpen) {
                showStoreHome();
            }
            storeFirstOpen = false;
        } else {
            hideStoreHome();
            showAllModulesDiv();
            populateAllModulesDiv('basetoinstall');
            if (baseToInstall.length > 0) {
                var div = document.getElementById('messagediv');
                emptyElement(div);
                div.style.display = 'block';
                div.style.top = '163px';
                div.style.left = '127px';
                var span = getEl('span');
                span.style.position = 'relative';
                span.textContent = 'Base modules (shown below) need to be installed to use Open-CRAVAT.';
                addEl(div, span);
                addEl(div, getEl('br'));
                var span = getEl('span');
                span.style.position = 'relative';
                span.textContent = 'Click this button to install them all: ';
                addEl(div, span);
                var button = getEl('button');
                button.style.position = 'relative';
                button.style.top = '-2px';
                button.textContent = 'Install base components';
                button.addEventListener('click', function (evt) {
                    installBaseComponents();
                    document.getElementById('messagediv').style.display = 'none';
                });
                addEl(div, button);
                div = document.getElementById('remotemodulepanels');
                div.style.top = '114px';
            }
            if (baseInstalled == false) {
                clickTab('storediv');
            }
        }
        var d = document.getElementById('store-update-all-div');
        if (newModuleAvailable) {
            var modulesInInstallQueue = Object.keys(installInfo);

            d.style.display = 'block';
            announceStoreUpdateAllAvailable();
        } else {
            d.style.display = 'none';
        }
        populateStoreTagPanel();
        showOrHideInstallAllButton();
	});
}

function showOrHideInstallAllButton () {
    var notInstalledModuleNames = getNotInstalledModuleNames();
    var div = document.getElementById('store-install-all-button-div');
    var display = null;
    if (notInstalledModuleNames.length == 0) {
        display = 'none';
    } else {
        display = 'block';
    }
    div.style.display = display;
}

function showStoreHome () {
    document.getElementById('store-home-div').style.display = 'block';
    document.getElementById('store-allmodule-div').style.display = 'none';
}

function hideStoreHome () {
    document.getElementById('store-home-div').style.display = 'none';
    document.getElementById('store-allmodule-div').style.display = 'block';
}

function getMostDownloadedModuleNames () {
    var moduleNames = Object.keys(remoteModuleInfo);
    for (var i = 0; i < moduleNames.length; i++) {
        for (var j = i + 1; j < moduleNames.length - 1; j++) {
            var d1 = remoteModuleInfo[moduleNames[i]].downloads;
            var d2 = remoteModuleInfo[moduleNames[j]].downloads;
            if (d1 < d2) {
                var tmp = moduleNames[i];
                moduleNames[i] = moduleNames[j];
                moduleNames[j] = tmp;
            }
        }
    }
    var top10ModuleNames = [];
    for (var i = 0; i < 10; i++) {
        top10ModuleNames.push(moduleNames[i]);
    }
    return top10ModuleNames;
}

function getNewestModuleNames () {
    var moduleNames = Object.keys(remoteModuleInfo);
    for (var i = 0; i < moduleNames.length; i++) {
        for (var j = i + 1; j < moduleNames.length - 1; j++) {
            var d1 = new Date(remoteModuleInfo[moduleNames[i]].publish_time);
            var d2 = new Date(remoteModuleInfo[moduleNames[j]].publish_time);
            if (d1 < d2) {
                var tmp = moduleNames[i];
                moduleNames[i] = moduleNames[j];
                moduleNames[j] = tmp;
            }
        }
    }
    var top10ModuleNames = [];
    for (var i = 0; i < 10; i++) {
        top10ModuleNames.push(moduleNames[i]);
    }
    return top10ModuleNames;
}

function populateStoreHome () {
    // Most Downloaded
    var div = document.getElementById('store-home-featureddiv');
    $(div).empty();
    var sdiv = getEl('div');
    var featuredModules = getMostDownloadedModuleNames();
    sdiv.style.width = (featuredModules.length * storeTileWidthStep) + 'px';
    for (var i = 0; i < featuredModules.length; i++) {
        var panel = getRemoteModulePanel(featuredModules[i]);
        addEl(sdiv, panel);
    }
    addEl(div, sdiv);
    // Newest
    var div = document.getElementById('store-home-newestdiv');
    $(div).empty();
    var sdiv = getEl('div');
    var newestModules = getNewestModuleNames();
    sdiv.style.width = (newestModules.length * storeTileWidthStep) + 'px';
    for (var i = 0; i < newestModules.length; i++) {
        var panel = getRemoteModulePanel(newestModules[i]);
        addEl(sdiv, panel);
    }
    addEl(div, sdiv);
}

function onClickStoreHomeLeftArrow (el) {
    var d = el.nextElementSibling;
    var dw = d.offsetWidth;
    var s = d.scrollLeft;
    s -= Math.floor(dw / storeTileWidthStep) * storeTileWidthStep;
    $(d).animate({scrollLeft: s});
    //d.scrollLeft = s;
}

function onClickStoreHomeRightArrow (el) {
    var d = el.previousElementSibling;
    var dw = d.offsetWidth;
    var s = d.scrollLeft;
    s += Math.floor(dw / storeTileWidthStep) * storeTileWidthStep;
    $(d).animate({scrollLeft: s});
    //d.scrollLeft = s;
}

function trimRemote () {
    var remoteModuleNames = Object.keys(remoteModuleInfo);
    var defaultWidgetNames = [];
    for (var i = 0; i < remoteModuleNames.length; i++) {
        var remoteModuleName = remoteModuleNames[i];
        var remoteModule = remoteModuleInfo[remoteModuleName];
        if (remoteModule.type == 'annotator') {
            defaultWidgetNames.push('wg' + remoteModuleName);
        }
    }
    for (var i = 0; i < remoteModuleNames.length; i++) {
        var remoteModuleName = remoteModuleNames[i];
        var remoteModule = remoteModuleInfo[remoteModuleName];
        if (remoteModule.tags == null) {
            remoteModule.tags = [];
        }
        if (modulesToIgnore.includes(remoteModuleName) && remoteModule.tags.includes('newavailable') == false){
            delete remoteModuleInfo[remoteModuleName];
            continue;
        }
        if (baseModuleNames.includes(remoteModuleName) && remoteModule.tags.includes('newavailable') == false) {
            delete remoteModuleInfo[remoteModuleName];
            continue;
        }
        var remoteModule = remoteModuleInfo[remoteModuleName];
        if (remoteModule.type == 'webviewerwidget' && 
                defaultWidgetNames.includes(remoteModuleName) && remoteModule.tags.includes('newavailable') == false) {
            delete remoteModuleInfo[remoteModuleName];
            continue;
        }
    }
}

function getRemote () {
	$.ajax({
        url: '/store/remote',
        async: true,
        success: function(data){
            remoteModuleInfo = data;
            for (var moduleName in remoteModuleInfo) {
                var moduleInfo = remoteModuleInfo[moduleName];
                if (! ('tags' in moduleInfo)) {
                    moduleInfo.tags = [];
                }
            }
            var modules = Object.keys(remoteModuleInfo);
            for (var i = 0; i < modules.length; i++) {
                var module = modules[i];
                var moduleInfo = remoteModuleInfo[module];
                if (moduleInfo['queued'] == true) {
                    installInfo[module] = {'msg': 'queued'};
                }
            }
            getLocal();
        }
	});
}

function removeElementFromArrayByValue (a, e) {
    var idx = a.indexOf(e);
    if (idx >= 0) {
        a.splice(idx, 1);
    }
}

function getNotInstalledModuleNames () {
    var notInstalledModuleNames = [];
    for (var module in remoteModuleInfo) {
        var tags = remoteModuleInfo[module].tags;
        var installedTagFound = false;
        for (var i = 0; i < tags.length; i++) {
            var tag = tags[i];
            if (tag == 'installed') {
                installedTagFound = true;
                break;
            }
        }
        if (installedTagFound == false) {
            if (module.startsWith('chasmplus_') == false) {
                notInstalledModuleNames.push(module);
            }
        }
    }
    return notInstalledModuleNames;
}

function populateStoreTagPanel () {
    tagsCollected = [];
    for (var module in remoteModuleInfo) {
        var tags = remoteModuleInfo[module].tags;
        for (var i = 0; i < tags.length; i++) {
            var tag = tags[i];
            if (tag == 'gene-level' || tag == 'variant-level') {
            }
            if (tagsCollected.indexOf(tag) == -1) {
                tagsCollected.push(tag);
            }
        }
    }
    for (var module in localModuleInfo) {
        var tags = localModuleInfo[module].tags;
        for (var i = 0; i < tags.length; i++) {
            var tag = tags[i];
            if (tagsCollected.indexOf(tag) == -1) {
                tagsCollected.push(tag);
            }
        }
    }
    removeElementFromArrayByValue(tagsCollected, 'installed');
    removeElementFromArrayByValue(tagsCollected, 'newavailable');
    tagsCollected.sort();
    var div = document.getElementById('store-tag-custom-div');
    $(div).empty();
    for (var i = 0; i < tagsCollected.length; i++) {
        var tag = tagsCollected[i];
        var input = getEl('input');
        input.type = 'checkbox';
        input.value = tag;
        input.className = 'store-tag-checkbox';
        input.addEventListener('click', function (evt) {
            onStoreTagCheckboxChange();
        });
        addEl(div, input);
        var span = getEl('span');
        span.class = 'store-tag-span';
        span.textContent = tag;
        addEl(div, span);
        addEl(div, getEl('br'));
    }
}

function installBaseComponents () {
    for (var i = 0; i < baseModuleNames.length; i++) {
        var module = baseModuleNames[i];
        if (localModuleInfo[module] == undefined || localModuleInfo[module]['exists'] == false) {
            queueInstall(module);
        }
    }
}

function emptyElement (elem) {
	var last = null;
    while (last = elem.lastChild) {
    	elem.removeChild(last);
    }
}

function updateFilter () {
    var nameinput = document.getElementById('store-namefilter');
    var nameStr = nameinput.value;
    filter = {};
    var filterHasValue = false;
    // Name filter
    if (nameStr != '') {
        filter['name'] = [nameStr];
        filterHasValue = true;
    }
    // Tag filter
    var checkboxes = $('.store-tag-checkbox:checked');
    var tags = [];
    for (var i = 0; i < checkboxes.length; i++) {
        tags.push(checkboxes[i].value);
        filterHasValue = true;
    }
    filter['tags'] = tags;
    populateAllModulesDiv();
    showAllModulesDiv();
    if (filterHasValue) {
        document.getElementById('store-tag-reset-button').className = 'store-front-all-button-off';
    } else {
        document.getElementById('store-tag-reset-button').className = 'store-front-all-button-on';
    }
    document.getElementById('store-home-button').className = 'store-front-all-button-off';
}

function getRemoteModulePanel (moduleName) {
    var moduleInfo = remoteModuleInfo[moduleName];
    var div = getEl('div');
    div.className = 'moduletile';
    div.setAttribute('module', moduleName);
    var sdiv = getEl('div');
    sdiv.id = 'logodiv_' + moduleName;
    sdiv.className = 'moduletile-logodiv';
    sdiv.setAttribute('module', moduleName);
    sdiv.onclick = function (evt) {
        var moduleName = this.getAttribute('module');
        var dialog = activateDetailDialog(moduleName);
        var storediv = document.getElementById('storediv');
        addEl(storediv, dialog);
        evt.stopPropagation();
    }
    var img = addLogo(moduleName, sdiv);
    if (img != null) {
        img.onclick = function (evt) {
            var pdiv = evt.target.parentElement;
            var moduleName = div.getAttribute('module');
            var storediv = document.getElementById('storediv');
            var dialog = activateDetailDialog(moduleName);
            addEl(storediv, dialog);
            evt.stopPropagation();
        }
    }
    addEl(div, sdiv);
    var span = null;
    span = getEl('div');
    span.style.height = '5px';
    addEl(div, span);
    span = getEl('div');
    span.className = 'modulepanel-title-span';
    var moduleTitle = moduleInfo.title;
    if (moduleTitle.length > 24) {
        span.style.fontSize = '14px';
    }
    addEl(span, getTn(moduleInfo.title));
    addEl(div, span);
    /*
    span = getEl('span');
    span.className = 'modulepanel-org-span';
    var organization = moduleInfo['developer']['organization'];
    if (organization != undefined && organization.length > 50) {
        span.style.fontSize = '10px';
    }
    span.textContent = organization;
    addEl(div, span);
    addEl(div, getEl('br'));
    */
    var sdiv = getEl('div');
    sdiv.className = 'modulepanel-typesizedate-div';
    span = getEl('span');
    span.className = 'modulepanel-type-span';
    span.textContent = moduleInfo['type'];
    span.title = 'module type';
    addEl(sdiv, span);
    span = getEl('span');
    span.className = 'modulepanel-divider-span';
    span.textContent = ' | ';
    addEl(sdiv, span);
    span = getEl('span');
    span.className = 'modulepanel-size-span';
    span.textContent = getSizeText(moduleInfo['size']);
    span.title = 'module size';
    addEl(sdiv, span);
    span = getEl('span');
    span.className = 'modulepanel-datasource-span';
    var datasource = moduleInfo['datasource'];
    if (datasource == null) {
        datasource = '';
    }
    span.textContent = datasource;
    span.title = 'Source data release date';
    addEl(div, span);
    addEl(div, sdiv);
    addEl(div, getEl('br'));
    var installStatus = '';
    if (installInfo[moduleName] != undefined) {
        var msg = installInfo[moduleName]['msg'];
        if (msg == 'uninstalling') {
            installStatus = 'Uninstalling...';
        } else if (msg == 'installing') {
            installStatus = 'Installing...';
        } else if (msg == 'queued') {
            installStatus = 'Queued';
        }
    } else {
        if (localModuleInfo[moduleName] != undefined && localModuleInfo[moduleName]['exists']) {
            installStatus = 'Installed';
        } else {
            installStatus = '';
        }
    }
    var progSpan = getEl('div');
    progSpan.id = 'panelinstallprogress_' + moduleName;
    progSpan.className = 'panelinstallprogressspan';
    addEl(div, progSpan);
    var span = getEl('div');
    span.id = 'panelinstallstatus_' + moduleName;
    addEl(div, span);
    if (installStatus == 'Installed') {
        /*
        var img2 = getEl('img');
        img2.src = '/store/done.png';
        img2.title = 'Installed';
        img2.className = 'donemark';
        addEl(span, img2);
        */
    } else {
        if (installStatus == 'Queued') {
            progSpan.textContent = 'Queued';
            progSpan.style.color = 'red';
        } else {
            progSpan.style.color = 'black';
        }
    }
    if (installStatus == 'Installed') {
        if (remoteModuleInfo[moduleName].tags.indexOf('newavailable') >= 0) {
            var button = getEl('button');
            button.className = 'modulepanel-update-button';
            button.textContent = 'Update available';
            button.setAttribute('module', moduleName);
            button.addEventListener('click', function (evt) {
                var moduleName = evt.target.getAttribute('module');
                queueInstall(moduleName);
            });
            addEl(div, button);
        }
        var button = getEl('button');
        button.className = 'modulepanel-uninstall-button';
        button.textContent = 'Uninstall';
        button.setAttribute('module', moduleName);
        button.addEventListener('click', function (evt) {
            var moduleName = evt.target.getAttribute('module');
            uninstallModule(moduleName);
        });
        addEl(div, button);
    } else {
        var button = getEl('button');
        button.className = 'modulepanel-install-button';
        button.textContent = 'Install';
        button.setAttribute('module', moduleName);
        button.addEventListener('click', function (evt) {
            var moduleName = evt.target.getAttribute('module');
            queueInstall(moduleName);
        });
        addEl(div, button);
    }
    return div
}

function getFilteredRemoteModules () {
    var filteredRemoteModules = {};
    var remoteModuleNames = Object.keys(remoteModuleInfo);
    var hasFilter = Object.keys(filter).length > 0;
    for (var i = 0; i < remoteModuleNames.length; i++) {
        var remoteModuleName = remoteModuleNames[i];
        var remoteModuleNameLower = remoteModuleName.toLowerCase();
        var remoteModule = remoteModuleInfo[remoteModuleName];
        if (hasFilter) {
            var typeYes = false;
            var nameYes = false;
            var tagYes = false;
            if (filter['type'] != undefined && filter['type'] != '') {
                if (filter['type'] == 'base') {
                    if (baseModuleNames.includes(remoteModuleName)) {
                        typeYes = true;
                    } else {
                        typeYes = false;
                    }
                } else {
                    if (filter['type'].includes(remoteModule['type'])) {
                        typeYes = true;
                    } else {
                        typeYes = false;
                    }
                }
            } else {
                typeYes = true;
            }
            if (filter['name'] != undefined && filter['name'] != '') {
                for (var j = 0; j < filter['name'].length; j++) {
                    var queryStr = filter['name'][j].toLowerCase();
                    if (remoteModule['title'].toLowerCase().includes(queryStr) || remoteModule['description'].toLowerCase().includes(queryStr)) {
                        nameYes = true;
                        break;
                    }
                }
            } else {
                nameYes = true;
            }
            if (filter['tags'] != undefined && filter['tags'].length > 0) {
                var checkbox = document.getElementById('store-tag-andor-checkbox');
                var op = 'and';
                if (checkbox.checked) {
                    op = 'or';
                }
                if (op == 'and') {
                    tagYes = true;
                    for (var j = 0; j < filter['tags'].length; j++) {
                        if (remoteModule['tags'].indexOf(filter['tags'][j]) == -1) {
                            tagYes = false;
                            break;
                        }
                    }
                } else if (op == 'or') {
                    tagYes = false;
                    for (var j = 0; j < filter['tags'].length; j++) {
                        if (remoteModule['tags'].indexOf(filter['tags'][j]) >= 0) {
                            tagYes = true;
                            break;
                        }
                    }
                }
            } else {
                tagYes = true;
            }
        } else {
            typeYes = true;
            nameYes = true;
            tagYes = true;
        }
        if (typeYes && nameYes && tagYes) {
            filteredRemoteModules[remoteModuleName] = remoteModule;
        }
    }
    return filteredRemoteModules;
}

function getSortedFilteredRemoteModuleNames () {
    var sel = document.getElementById('store-sort-select');
    var option = sel.options[sel.selectedIndex];
    var sortKey = option.value;
    var filteredRemoteModules = getFilteredRemoteModules();
    var sortedNames = null;
    if (sortKey == 'name') {
        sortedNames = Object.keys(filteredRemoteModules);
        sortedNames.sort();
    } else if (sortKey == 'size') {
        sortedNames = Object.keys(filteredRemoteModules);
        for (var i = 0; i < sortedNames.length - 1; i++) {
            for (var j = i + 1; j < sortedNames.length; j++) {
                var size1 = filteredRemoteModules[sortedNames[i]].size;
                var size2 = filteredRemoteModules[sortedNames[j]].size;
                if (size1 < size2) {
                    var tmp = sortedNames[i];
                    sortedNames[i] = sortedNames[j];
                    sortedNames[j] = tmp;
                }
            }
        }
    } else if (sortKey == 'date') {
        sortedNames = Object.keys(filteredRemoteModules);
        for (var i = 0; i < sortedNames.length - 1; i++) {
            for (var j = i + 1; j < sortedNames.length; j++) {
                var v1 = filteredRemoteModules[sortedNames[i]].publish_time;
                var v2 = filteredRemoteModules[sortedNames[j]].publish_time;
                v1 = new Date(v1);
                v2 = new Date(v2);
                if (v1 < v2) {
                    var tmp = sortedNames[i];
                    sortedNames[i] = sortedNames[j];
                    sortedNames[j] = tmp;
                }
            }
        }
    }
    return sortedNames;
}

function showAllModulesDiv () {
    var homediv = document.getElementById('store-home-div');
    var allmodulediv = document.getElementById('store-allmodule-div');
    homediv.style.display = 'none';
    allmodulediv.style.display = 'block';
}

function populateAllModulesDiv (group) {
    var div = document.getElementById('remotemodulepanels');
    emptyElement(div);
    var remoteModuleNames = getSortedFilteredRemoteModuleNames();
    for (var i = 0; i < remoteModuleNames.length; i++) {
        var remoteModuleName = remoteModuleNames[i];
        if (group == 'basetoinstall') {
            if (baseModuleNames.indexOf(remoteModuleName) == -1) {
                continue;
            }
            if (remoteModuleInfo[remoteModuleName].tags.indexOf('installed') > -1) {
                continue;
            }
        } else {
            if (remoteModuleName.startsWith('chasmplus_')) {
                continue;
            }
            if (remoteModuleName == 'example_annotator' || remoteModuleName == 'template') {
                continue;
            }
        }
        var remoteModule = remoteModuleInfo[remoteModuleName];
        var panel = getRemoteModulePanel(remoteModuleName);
        addEl(div, panel);
    }
}

function addLogo (moduleName, sdiv) {
    if (storeLogos[moduleName] != undefined) {
        var img = storeLogos[moduleName].cloneNode(true);
        addEl(sdiv, img);
        return img;
    }
    var moduleInfo = remoteModuleInfo[moduleName];
    var img = null;
    if (moduleInfo.has_logo == true) {
        img = getEl('img');
        img.className = 'moduletile-logo';
        img.src = storeUrl + '/modules/' + moduleName + '/' + moduleInfo['latest_version'] + '/logo.png';
        addEl(sdiv, img);
        storeLogos[moduleName] = img;
    } else {
        sdiv.classList.add('moduletile-nologo');
        var span = getEl('div');
        span.className = 'moduletile-title';
        var title = moduleInfo.title;
        span.textContent = title
        if (title.length > 30) {
            span.style.fontSize = '30px';
        }
        addEl(sdiv, span);
    }
    return img;
}

function activateDetailDialog (moduleName) {
    var div = document.getElementById('moduledetaildiv_store');
    if (div) {
        emptyElement(div);
    } else {
        div = getEl('div');
        div.id = 'moduledetaildiv_store';
    }
    currentDetailModule = moduleName;
    div.style.display = 'block';
    var moduleInfo = remoteModuleInfo[moduleName];
    var table = getEl('table');
    table.style.height = '100px';
    table.style.border = '0px';
    table.style.width = 'calc(100% - 20px)';
    var tr = getEl('tr');
    tr.style.border = '0px';
    var td = getEl('td');
    td.id = 'moduledetaillogotd';
    td.style.border = '0px';
    var sdiv = getEl('div');
    sdiv.className = 'moduletile-logodiv';
    var img = addLogo(moduleName, sdiv);
    if (img != null) {
        img.style.maxHeight = '84px';
    } else {
        sdiv.style.position = 'relative';
        sdiv.children[0].style.display = 'none';
    }
    addEl(td, sdiv);
    addEl(tr, td);
    td = getEl('td');
    td.style.border = '0px';
    var span = getEl('div');
    span.style.fontSize = '30px';
    span.textContent = moduleInfo.title;
    addEl(td, span);
    addEl(td, getEl('br'));
    span = getEl('span');
    span.style.fontSize = '12px';
    span.style.color = 'green';
    span.textContent = moduleInfo.type;
    addEl(td, span);
    span = getEl('span');
    span.style.fontSize = '12px';
    span.style.color = 'green';
    span.textContent = ' | ' + moduleInfo.developer.organization;
    addEl(td, span);
    addEl(tr, td);
    td = getEl('td');
    td.style.border = '0px';
    td.style.verticalAlign = 'top';
    td.style.textAlign = 'right';
    if (servermode == false || (logged == true && username == 'admin')) {
        var button = getEl('button');
        button.id = 'installbutton';
        var localInfo = localModuleInfo[moduleName];
        var buttonText = null;
        if (localInfo != undefined && localInfo.exists) {
            buttonText = 'Uninstall';
            button.style.backgroundColor = '#ffd3be';
            button.addEventListener('click', function (evt) {
                var btn = evt.target;
                btn.textContent = 'Uninstalling...';
                btn.style.color = 'red';
                uninstallModule(btn.getAttribute('module'));
                document.getElementById('moduledetaildiv_store').style.display = 'none';
            });
        } else {
            buttonText = 'Install';
            button.style.backgroundColor = '#beeaff';
            button.addEventListener('click', function (evt) {
                var btn = evt.target;
                var btnModuleName = btn.getAttribute('module');
                if (btnModuleName == 'chasmplus') {
                    var select = document.getElementById('chasmplustissueselect');
                    btnModuleName = select.value;
                }
                var buttonText = null;
                if (installQueue.length == 0) {
                    buttonText = 'Installing...';
                } else {
                    buttonText = 'Queued';
                }
                queueInstall(btnModuleName);
                btn.textContent = buttonText;
                btn.style.color = 'red';
                document.getElementById('moduledetaildiv_store').style.display = 'none';
            });
        }
        button.textContent = buttonText;
        button.style.padding = '8px';
        button.style.fontSize = '18px';
        button.style.fontWeight = 'bold';
        button.setAttribute('module', moduleName);
        if (buttonText == 'Uninstall') {
            var img2 = getEl('img');
            img2.id = 'installedicon';
            img2.src = '/store/done.png';
            img2.style.width = '20px';
            img2.title = 'Installed';
            addEl(td, img2);
        }
        addEl(td, getEl('br'));
        if (moduleName == 'chasmplus') {
            var span = getEl('span');
            span.textContent = 'Select tissue:';
            addEl(td, span);
            var select = getEl('select');
            select.id = 'chasmplustissueselect';
            var option = getEl('option');
            option.value = 'chasmplus';
            option.text = 'Generic';
            select.add(option);
            var modules = Object.keys(remoteModuleInfo);
            for (var i = 0; i < modules.length; i++) {
                var module = modules[i];
                if (module.startsWith('chasmplus_')) {
                    var option = getEl('option');
                    var tissue = module.replace('chasmplus_', '');
                    option.value = module;
                    option.text = tissue;
                    select.add(option);
                }
            }
            select.addEventListener('change', function (evt) {
                var value = select.options[select.selectedIndex].value;
                var m = localModuleInfo[value];
                if (m != undefined && m.exists == true) {
                    var button = document.getElementById('installbutton');
                    button.textContent = 'Uninstall';
                    button.addEventListener('click', function (evt) {
                        var btn = evt.target;
                        btn.textContent = 'Uninstalling...';
                        btn.style.color = 'red';
                        uninstallModule(btn.getAttribute('module'));
                        document.getElementById('moduledetaildiv_store').style.display = 'none';
                    });
                    var img2 = document.getElementById('installedicon');
                    img2.src = '/store/done.png';
                    img2.title = 'Installed';
                } else {
                    var button = document.getElementById('installbutton');
                    button.textContent = 'Install';
                    button.addEventListener('click', function (evt) {
                        var btn = evt.target;
                        var btnModuleName = btn.getAttribute('module');
                        if (btnModuleName == 'chasmplus') {
                            var select = document.getElementById('chasmplustissueselect');
                            btnModuleName = select.value;
                        }
                        var buttonText = null;
                        if (installQueue.length == 0) {
                            buttonText = 'Installing...';
                        } else {
                            buttonText = 'Queued';
                        }
                        queueInstall(btnModuleName);
                        btn.textContent = buttonText;
                        btn.style.color = 'red';
                        document.getElementById('moduledetaildiv_store').style.display = 'none';
                    });
                    var img2 = document.getElementById('installedicon');
                    img2.src = '/store/empty.png';
                    img2.title = 'Uninstalled';
                }
            });
            addEl(td, select);
        }
        addEl(td, button);
        var sdiv = getEl('div');
        sdiv.id = 'installstatdiv_' + moduleName;
        sdiv.style.marginTop = '10px';
        sdiv.style.fontSize = '12px';
        if (installInfo[moduleName] != undefined) {
            sdiv.textContent = installInfo[moduleName]['msg'];
        }
        addEl(td, sdiv);
    }
    addEl(tr, td);
    addEl(table, tr);
    addEl(div, table);
    addEl(div, getEl('hr'));
    table = getEl('table');
    table.style.height = 'calc(100% - 100px)';
    table.style.border = '0px';
    tr = getEl('tr');
    var tdHeight = (window.innerHeight * 0.8 - 150) + 'px';
    tr.style.border = '0px';
    td = getEl('td');
    td.style.border = '0px';
    td.style.width = '70%';
    td.style.verticalAlign = 'top';
    td.style.height = tdHeight;
    var mdDiv = getEl('div');
    mdDiv.style.height = '100%';
    mdDiv.style.overflow = 'auto';
    var wiw = window.innerWidth;
    mdDiv.style.maxWidth = (wiw * 0.8 * 0.68) + 'px';
    addEl(td, mdDiv);
    addEl(tr, td);
	$.get('/store/modules/'+moduleName+'/'+'latest'+'/readme').done(function(data){
		mdDiv.innerHTML = data;
	});
    td = getEl('td');
    td.style.width = '30%';
    td.style.border = '0px';
    td.style.verticalAlign = 'top';
    td.style.height = tdHeight;
    var infodiv = getEl('div');
    infodiv.style.height = '100%';
    infodiv.style.overflow = 'auto';
    infodiv.style.maxWidth = (wiw * 0.8 * 0.3) + 'px';
    var d = getEl('div');
    span = getEl('span');
    span.textContent = moduleInfo.description;
    addEl(d, span);
    addEl(infodiv, d);
    addEl(infodiv, getEl('br'));
    d = getEl('div');
    span = getEl('span');
    span.style.fontWeight = 'bold';
    span.textContent = 'Version: ';
    addEl(d, span);
    span = getEl('span');
    var remoteVersion = moduleInfo['latest_version'];
    span.textContent = remoteVersion;
    addEl(d, span);
    if (localModuleInfo[moduleName] != undefined) {
        var localVersion = localModuleInfo[moduleName].version;
        if (localVersion != remoteVersion) {
            var span = getEl('span');
            span.textContent = ' (' + localVersion + ' installed)';
            addEl(d, span);
            if (moduleInfo.tags.indexOf('newavailable') >= 0) {
                addEl(d, getEl('br'));
                var span = getEl('span');
                span.style.color = 'red';
                span.textContent = 'Updates to your installed modules are available!';
                addEl(d, span);
                var button = getEl('button');
                button.id = 'updatebutton';
                buttonText = 'Update';
                button.style.backgroundColor = '#beeaff';
                button.addEventListener('click', function (evt) {
                    var btn = evt.target;
                    var btnModuleName = btn.getAttribute('module');
                    if (btnModuleName == 'chasmplus') {
                        var select = document.getElementById('chasmplustissueselect');
                        btnModuleName = select.value;
                    }
                    var buttonText = null;
                    if (installQueue.length == 0) {
                        buttonText = 'Updating...';
                    } else {
                        buttonText = 'Queued';
                    }
                    queueInstall(btnModuleName);
                    btn.textContent = buttonText;
                    btn.style.color = 'red';
                    document.getElementById('moduledetaildiv_store').style.display = 'none';
                });
                button.textContent = buttonText;
                button.style.padding = '8px';
                button.style.fontSize = '18px';
                button.style.fontWeight = 'bold';
                button.setAttribute('module', moduleName);
                addEl(d, button);
            }
        }
    }
    addEl(infodiv, d);
    addEl(infodiv, getEl('br'));
    d = getEl('div');
    span = getEl('span');
    span.style.fontWeight = 'bold';
    span.textContent = 'Data source version: ';
    addEl(d, span);
    span = getEl('span');
    var datasource = moduleInfo['datasource'];
    if (datasource == null) {
        datasource = '';
    }
    span.textContent = datasource;
    addEl(d, span);
    addEl(d, getEl('br'));
    addEl(infodiv, d);
    addEl(infodiv, getEl('br'));
    d = getEl('div');
    span = getEl('span');
    span.style.fontWeight = 'bold';
    span.textContent = 'Maintainer: ';
    addEl(d, span);
    span = getEl('span');
    span.textContent = moduleInfo['developer']['name'];
    addEl(d, span);
    addEl(d, getEl('br'));
    addEl(d, getEl('br'));
    span = getEl('span');
    span.style.fontWeight = 'bold';
    span.textContent = 'e-mail: ';
    addEl(d, span);
    span = getEl('span');
    span.textContent = moduleInfo['developer']['email'];
    addEl(d, span);
    addEl(d, getEl('br'));
    addEl(d, getEl('br'));
    addEl(infodiv, d);
    d = getEl('div');
    span = getEl('span');
    span.style.fontWeight = 'bold';
    span.textContent = 'Citation: ';
    addEl(d, span);
    span = getEl('span');
    span.style.display = 'inline-block';
    span.style.width = 'calc(100% - 120px)';
    span.style.wordWrap = 'break-word';
    span.style.verticalAlign = 'text-top';
    var citation = moduleInfo['developer']['citation'];
    if (citation != undefined && citation.startsWith('http')) {
        var a = getEl('a');
        a.href = citation;
        a.target = '_blank';
        a.textContent = citation;
        addEl(span, a);
    } else {
        span.textContent = citation;
    }
    addEl(d, span);
    addEl(infodiv, d);
    addEl(infodiv, getEl('br'));
    d = getEl('div');
    span = getEl('span');
    span.style.fontWeight = 'bold';
    span.textContent = 'Organization: ';
    addEl(d, span);
    span = getEl('span');
    span.textContent = moduleInfo['developer']['organization'];
    addEl(d, span);
    addEl(infodiv, d);
    addEl(infodiv, getEl('br'));
    d = getEl('div');
    span = getEl('span');
    span.style.fontWeight = 'bold';
    span.textContent = 'Website: ';
    addEl(d, span);
    span = getEl('a');
    span.textContent = moduleInfo['developer']['website'];
    span.href = moduleInfo['developer']['website'];
    span.target = '_blank';
    span.style.wordBreak = 'break-all';
    addEl(d, span);
    addEl(infodiv, d);
    addEl(infodiv, getEl('br'));
    d = getEl('div');
    span = getEl('span');
    span.style.fontWeight = 'bold';
    span.textContent = 'Type: ';
    addEl(d, span);
    span = getEl('span');
    span.textContent = moduleInfo['type'];
    addEl(d, span);
    addEl(infodiv, d);
    addEl(infodiv, getEl('br'));
    d = getEl('div');
    span = getEl('span');
    span.style.fontWeight = 'bold';
    span.textContent = 'Size: ';
    addEl(d, span);
    span = getEl('span');
    span.textContent = getSizeText(moduleInfo['size']);
    addEl(d, span);
    addEl(infodiv, d);
    addEl(infodiv, getEl('br'));
    d = getEl('div');
    span = getEl('span');
    span.style.fontWeight = 'bold';
    span.textContent = 'Posted on: ';
    addEl(d, span);
    span = getEl('span');
    var t = new Date(moduleInfo['publish_time']);
    span.textContent = t.toLocaleDateString();
    addEl(d, span);
    addEl(infodiv, d);
    addEl(infodiv, getEl('br'));
    d = getEl('div');
    span = getEl('span');
    span.style.fontWeight = 'bold';
    span.textContent = 'Downloads: ';
    addEl(d, span);
    span = getEl('span');
    var t = moduleInfo['downloads'];
    span.textContent = t;
    addEl(d, span);
    addEl(infodiv, d);
    addEl(td, infodiv);
    addEl(tr, td);
    addEl(table, tr);
    addEl(div, table);
    var el = getEl('div');
    el.style.position = 'absolute';
    el.style.top = '0px';
    el.style.right = '0px';
    el.style.fontSize = '20px';
    el.style.padding = '10px';
    el.style.cursor = 'pointer';
    el.textContent = 'X';
    el.addEventListener('click', function (evt) {
        var pel = evt.target.parentElement;
        pel.parentElement.removeChild(pel);
    });
    addEl(div, el);
    return div;
}

function compareVersion (ver1, ver2) {
    var tok1 = ver1.split('.');
    var tok2 = ver2.split('.');
    var first1 = tok1[0];
    var first2 = tok2[0];
    if (first1 < first2) {
        return -1;
    } else if (first1 > first2) {
        return 1;
    } else {
        var second1 = tok1[1];
        var second2 = tok2[1];
        if (second1 < second2) {
            return -1;
        } else if (second1 > second2) {
            return 1;
        } else {
            var third1 = tok1[2];
            var third2 = tok2[2];
            if (third1 < third2) {
                return -1;
            } else if (third1 > third2) {
                return 1;
            } else {
                return 0;
            }
        }
    }
}

function getHighestVersionForRemoteModule (module) {
    var versions = remoteModuleInfo[module].versions;
    var highestVersion = '0.0.0';
    for (var i = 0; i < versions.length; i++) {
        var version = versions[i];
        var c = compareVersion(version, highestVersion);
        if (c > 0) {
            highestVersion = version;
        }
    }
    return highestVersion;
}

function getSizeText (size) {
    size = parseInt(size);
    if (size < 1024) {
        size = size + ' B';
    } else {
        size = size / 1024;
        if (size < 1024) {
            size = size.toFixed(0) + ' KB';
        } else {
            size = size / 1024;
            if (size < 1024) {
                size = size.toFixed(0) + ' MB';
            } else {
                size = size / 1024;
                size = size.toFixed(0) + ' GB';
            }
        }
    }
    return size;
}

function queueInstall (moduleName) {
    $.get('/store/queueinstall', {'module': moduleName}).done(
        function (response) {
            installInfo[moduleName] = {'msg': 'queued'};
            installQueue.push(moduleName);
            populateAllModulesDiv();
        }
    );
}

function installModule (moduleName) {
	var version = remoteModuleInfo[moduleName]['latest_version'];
	$.ajax({
		type:'GET',
		url:'/store/install',
		data: {name:moduleName, version:version},
        success: function (response) {
            getLocal();
        }
	});
}

function uninstallModule(moduleName) {
    installInfo[moduleName] = {'msg': 'uninstalling'};
    populateAllModulesDiv();
	$.ajax({
        type:'GET',
        url:'/store/uninstall',
        data: {name: moduleName},
        complete: function (response) {
            delete installInfo[moduleName];
            moduleChange(response);
            populateAnnotators();
        }
	});
}

function moduleChange (data) {
	getLocal();
}

function connectWebSocket () {
    var host = window.location.host;
    var ws = new WebSocket(`ws://${host}/store/connectwebsocket`);
    ws.onopen = function (evt) {
    }
    ws.onclose = function (evt) {
    }
    ws.onmessage = function (evt) {
        var data = JSON.parse(evt.data);
        var module = data['module'];
        var msg = data['msg'];
        var isbase = data['isbase'];
        if (installInfo[module] == undefined) {
            installInfo[module] = {};
        }
        installInfo[module]['msg'] = msg;
        if (isbase != undefined && isbase == true) {
            var installstatdiv = document.getElementById('installbasestatdiv');
            installstatdiv.textContent = msg;
        } else {
            var divModuleName = module;
            if (module.startsWith('chasmplus_')) {
                divModuleName = module.split('_')[0];
            }
            var installstatdiv = document.getElementById('installstatdiv_' + divModuleName);
            if (installstatdiv != null) {
                installstatdiv.textContent = msg;
            }
            var sdiv = document.getElementById('panelinstallprogress_' + divModuleName);
            sdiv.style.color = 'black';
            sdiv.textContent = msg;
            if (msg.startsWith('Finished installation of')) {
                delete installInfo[module];
                installQueue = installQueue.filter(e => e != module);
                moduleChange(null);
                populateAnnotators();
                if (installQueue.length > 0) {
                    var module = installQueue.shift();
                    installInfo[module] = {'msg': 'installing'};
                }
            }
        }
    }
}

function getBaseModuleNames () {
    $.get('/store/getbasemodules').done(function (response) {
        baseModuleNames = response;
    });
}

function onStoreTagCheckboxChange () {
    updateFilter();
}

function onClickStoreInstallAllButton () {
    var notInstalledModuleNames = getNotInstalledModuleNames();
    var totalSize = 0;
    var modulesToInstallStr = '[';
    for (var i = 0; i < notInstalledModuleNames.length; i++) {
        totalSize += remoteModuleInfo[notInstalledModuleNames[i]].size;
        modulesToInstallStr += notInstalledModuleNames[i];
        if (i < notInstalledModuleNames.length - 1) {
            modulesToInstallStr += ', ';
        }
    }
    modulesToInstallStr += ']';
    totalSize = getSizeText(totalSize);
    var yn = confirm('Modules to install are ' + modulesToInstallStr + ' and total installation size is ' + totalSize + '. Install them all?');
    if (yn == false) {
        return;
    }
    for (var i = 0; i < notInstalledModuleNames.length; i++) {
        queueInstall(notInstalledModuleNames[i]);
    }
}

function onClickStoreUpdateAllButton () {
    for (var moduleName in remoteModuleInfo) {
        if (remoteModuleInfo[moduleName]['tags'].indexOf('newavailable') >= 0) {
            queueInstall(moduleName);
        }
    }
    announceStoreUpdatingAll();
}

function announceStoreUpdatingAll () {
    var div = document.getElementById('store-update-all-div');
    var span = document.getElementById('store-update-all-span');
    var button = document.getElementById('store-update-all-button');
    span.textContent = 'Updating all update-available modules...';
    button.style.display = 'none';
}

function announceStoreUpdateAllAvailable () {
    var div = document.getElementById('store-update-all-div');
    var span = document.getElementById('store-update-all-span');
    var button = document.getElementById('store-update-all-button');
    span.textContent = 'Updates to your installed modules are available!';
    button.style.display = 'inline';
}

function webstore_run () {
    document.addEventListener('click', function (evt) {
        if (evt.target.closest('#moduledetaildiv_store') == null) {
            var div = document.getElementById('moduledetaildiv_store');
            if (div != null) {
                div.style.display = 'none';
            }
        }
    });
    connectWebSocket();
    getBaseModuleNames();
	getRemote();
}
