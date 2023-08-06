let pikaDayInstances = []
window.URL = window.URL || window.webkitURL;

function toggleSideBar (event) {
    const sideBar = document.querySelector('.srm-sidebar-full-container')
    if (sideBar.classList.contains('srm-open')) {
        sideBar.classList.remove('srm-open')
    }
    else {
        sideBar.classList.add('srm-open')
    }
}

function toggleSubSideMenu (event) {
    // Collapse all menu children first
    event.preventDefault()
    // Check if the sub sidebar is open, if not open it
    const subSideBar = document.querySelector('#srm-sub-sidebar')
    const sideMenuLinks = document.querySelectorAll('.srm-sidebar > ul > li > a')

    if (!subSideBar.classList.contains('srm-open')) {
        subSideBar.classList.add('srm-open')
    }

    // If the link clicked is the one that is currently opened, then close the sidebar
    if (event.target.classList.contains('srm-open-children')) {
        // Close the sidebar
        subSideBar.classList.remove('srm-open')
        for(let i=0; i < sideMenuLinks.length; i++) {
            sideMenuLinks[i].classList.remove('srm-open-children')
        }
    }
    else {
        // Close the currently opened options and open the clicked one
        for(let i=0; i < sideMenuLinks.length; i++) {
            sideMenuLinks[i].classList.remove('srm-open-children')
        }
        event.target.classList.add('srm-open-children')
    }
}

function enableToggleSubMenuChildren () {
    const subMenuToggleLinks = document.querySelectorAll('.srm-submenu .has-children > a')
    for (let i=0; i < subMenuToggleLinks.length; i++) {
        subMenuToggleLinks[i].addEventListener('click', function (event) {
            event.preventDefault()
            // Close every other open sub menu children
            for (let h=0; h < subMenuToggleLinks.length; h++) {
                subMenuToggleLinks[h].nextElementSibling.classList.remove('show')
            }
            subMenuToggleLinks[i].nextElementSibling.classList.toggle('show')
        })
    }
}

function enableDateInputs () {
    let dateObjects = document.querySelectorAll('.srm-date-input')
    for (let i=0; i < dateObjects.length; i++) {
        pikaDayInstances.push(
            new Pikaday({
                field: dateObjects[i],
                format: 'D/M/YYYY',
                toString: function (date, format) {
                    const day = date.getDate();
                    const month = date.getMonth() + 1;
                    const year = date.getFullYear();
                    return day + '/' + month + '/' + year;
                },
            })
        )
    }
}

function destroyAllPikadayInstances () {
    for (let i=0; i < pikaDayInstances.length; i++) {
        pikaDayInstances[i].destroy()
    }
    pikaDayInstances = []
}

function reinitPikaday () {
    destroyAllPikadayInstances()
    enableDateInputs()
}

function addListenersToSideMenuLinks () {
    const sideMenuLinks = document.querySelectorAll('.srm-sidebar > ul > li > a')
    for(let i=0; i < sideMenuLinks.length; i++) {
        sideMenuLinks[i].addEventListener('click', toggleSubSideMenu)
    }
}

function onSrmRadioButtonClick (evt) {
    evt.preventDefault()
    const coveredRadioButton = document.querySelector('#' + evt.target.getAttribute('data-source'))
    coveredRadioButton.click()
}

function enableSrmRadioButtons () {
    const radioButtons = document.querySelectorAll('.srm-radio-toggle')
    for(let i=0; i < radioButtons.length; i++) {
        radioButtons[i].addEventListener('click', onSrmRadioButtonClick)
    }
}

function enableCheckAllForTables () {
    //Allow check all for tables
    const tables = document.querySelectorAll('table')
    for (let h=0; h < tables.length; h++) {
        const checkAllInputs = tables[h].querySelectorAll('thead > tr > th input[type=checkbox]:first-child');
        for (let i=0; i < checkAllInputs.length; i++) {
            checkAllInputs[i].addEventListener('change', function () {
                const childrenCheckBoxes = tables[h].querySelectorAll('tbody input[type=checkbox]')
                for(let j=0; j < childrenCheckBoxes.length; j++) {
                    childrenCheckBoxes[j].checked = checkAllInputs[i].checked
                }
            })
        }
    }
}

function notify(message, status='success', timeout=1500) {
    UIkit.notification({
        message: message,
        status: status,
        timeout: timeout
    })
}

function copyToClipBoard(event, source) {
    event.preventDefault();
    const content = document.querySelector(source);
    content.select();
    document.execCommand('copy');
    notify('Copied to Clipboard');
}

function enableAutoResizeTextArea() {
    //AutoResize for resizable textarea such as that in the edit contract page
    const resizableTextAreas = document.querySelectorAll('textarea.autosize');
    for (let h=0; h < resizableTextAreas.length; h++) {
        autosize(resizableTextAreas[h]);
    }
}

function enableAllUploadCirclesAndRec (event) {
    let inputSelector = event.target.getElementsByTagName('input')[0]
    inputSelector ? inputSelector.click() : null
}

function addEventListenersToUpload () {
    const uploadIcons = document.querySelectorAll('[class*=srm-upload-]')
    for (let h=0; h < uploadIcons.length; h++) {
        uploadIcons[h].addEventListener('click', enableAllUploadCirclesAndRec)
    }
}

function removeEventListenersFromUpload () {
    const uploadIcons = document.querySelectorAll('[class*=srm-upload-]')
    for (let h=0; h < uploadIcons.length; h++) {
        uploadIcons[h].removeEventListener('click', enableAllUploadCirclesAndRec)
    }
}

function reattachAllUploadListeners () {
    setTimeout(function () {
        removeEventListenersFromUpload()
        addEventListenersToUpload()
    }, 600)
}

function handleFiles(files, imageElementSelector, infoElementSelector) {
    const infoElement = document.querySelector(infoElementSelector),
        imageElement = document.querySelector(imageElementSelector)

    if (!files.length) {
        infoElement.innerHTML = "No files selected!";
    } else {
        infoElement.innerHTML = "";
        imageElement.src = window.URL.createObjectURL(files[0]);
        imageElement.onload = function () {
            window.URL.revokeObjectURL(this.src);
        }
        infoElement.innerHTML = files[0].name + ": " + files[0].size + " bytes";
    }
}

function dictToQueryString (params) {
    const newParams = []
    Object.keys(params).map(function (key) {
        if(params[key]) newParams.push(key + '=' + params[key])
        return params[key] ? key + '=' + params[key] : ''
    })
    return newParams.join('&')
}


window.onload = function () {
    addListenersToSideMenuLinks();
    enableToggleSubMenuChildren();
    enableDateInputs();
    enableSrmRadioButtons();
    enableCheckAllForTables();
    enableAutoResizeTextArea();
    addEventListenersToUpload();
}



