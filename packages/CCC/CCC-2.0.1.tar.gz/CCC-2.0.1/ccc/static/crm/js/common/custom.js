let pikaDayInstances = []
let flatpickrInstances = []
let flatpickrInstancesNoMin = []
let formBuilderDatePickers = []

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

const basic_ckeditor = {
    toolbarGroups: [
        {
            "name": "basicstyles",
            "groups": ["basicstyles"]
        },
        {
            "name": "links",
            "groups": ["links"]
        },
        {
            "name": "paragraph",
            "groups": ["list", "blocks"]
        },
        {
            "name": "document",
            "groups": ["mode"]
        },
        {
            "name": "insert",
            "groups": ["insert"]
        },
        {
            "name": "styles",
            "groups": ["styles"]
        },
        {
            "name": "about",
            "groups": ["about"]
        }
    ],
    // Remove the redundant buttons from toolbar groups defined above.
    removeButtons: 'Underline,Strike,Subscript,Superscript,Anchor,Styles,Specialchar'
}

function toggleSubSideMenu (event) {
    // Collapse all menu children first
    event.preventDefault()
    // Check if the sub sidebar is open, if not open it
    const subSideBar = document.querySelector('#srm-sub-sidebar')
    const sideMenuLinks = document.querySelectorAll('.srm-sidebar > ul > li > a')

    const sideBarNest = document.querySelector('.srm-sidebar-full-container > .srm-sidebar-nest')


    if (!subSideBar.classList.contains('srm-open') || !sideBarNest.classList.contains('collapsed')) {
        subSideBar.classList.add('srm-open')

        sideBarNest.classList.add('open')
        sideBarNest.classList.remove('collapsed')
    }

    // If the link clicked is the one that is currently opened, then close the sidebar
    if (event.target.classList.contains('srm-open-children')) {
        // Close the sidebar
        subSideBar.classList.remove('srm-open')

        sideBarNest.classList.remove('open')
        sideBarNest.classList.add('collapsed')

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

function addOffsetsToSubSideMenuItems () {
    const sideMenuItems = document.querySelectorAll('.srm-sidebar-list > li')
    for(let i=0; i < sideMenuItems.length; i++) {
        if (sideMenuItems[i].getElementsByClassName('srm-submenu').length > 0) {
            sideMenuItems[i].getElementsByClassName('srm-submenu')[0].style.marginTop = sideMenuItems[i].offsetTop + 10 + 'px'
        }
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

function handleFiles(files, thumbnailElementSelector, infoElementSelector) {
    const infoElement = document.querySelector(infoElementSelector),
        imageElement = document.querySelector(thumbnailElementSelector)

    if (!files.length) {
        infoElement.innerHTML = "No files selected!";
    } else {
        infoElement.innerHTML = "";
        imageElement.style.backgroundImage = 'url(' + window.URL.createObjectURL(files[0]) + ')';
        imageElement.onload = function () {
            window.URL.revokeObjectURL(this.src);
        }
        infoElement.innerHTML = files[0].name + ": " + files[0].size + " bytes";
    }
}

function formBuilderDateInstances () {
    const flatpickrs = document.querySelectorAll('.formbuilder-datepicker')

    for (let i=0; i < formBuilderDatePickers.length; i++) {
        formBuilderDatePickers[i].destroy()
    }

    for (let i=0; i < flatpickrs.length; i++) {
        formBuilderDatePickers.push(
            flatpickrs[i].flatpickr({
                enableTime: false,
                dateFormat: "Y-m-d",
                defaultDate: flatpickrs[i].getAttribute('data-initial') ? new Date(flatpickrs[i].getAttribute('data-initial')) : null,
            })
        )
    }

}

function initFlatPickerInstances () {
    const flatpickrs = document.querySelectorAll('.flat-datepicker')
    //Destroy if any is existing
    for (let i=0; i < flatpickrInstances.length; i++) {
        flatpickrInstances[i].destroy()
    }

    for (let i=0; i < flatpickrs.length; i++) {
        flatpickrInstances.push(
            flatpickrs[i].flatpickr({
                enableTime: true,
                dateFormat: "Y-m-d H:i",
                defaultDate: flatpickrs[i].getAttribute('data-initial') ? new Date(flatpickrs[i].getAttribute('data-initial')) : null,
                minDate: 'today'
            })
        )
    }
}

function initFlatPickerWithNoMinDate () {
    const flatpickrs = document.querySelectorAll('.flat-datepicker-no-min')
    //Destroy if any is existing
    for (let i=0; i < flatpickrInstancesNoMin.length; i++) {
        flatpickrInstancesNoMin[i].destroy()
    }

    for (let i=0; i < flatpickrs.length; i++) {
        flatpickrInstances.push(
            flatpickrs[i].flatpickr({
                enableTime: true,
                dateFormat: "Y-m-d H:i",
                defaultDate: flatpickrs[i].getAttribute('data-initial') ? new Date(flatpickrs[i].getAttribute('data-initial')) : null,
            })
        )
    }
}


// nav search
const navSearchContainer = document.querySelector('.uk-navbar-right');
const navbarTitle = document.querySelector('#navbar-title');
const closeNavSearchBtn = document.querySelector('#close-nav-search-btn');
const navSearchInput = document.querySelector('#nav-search-input');
const navSearchResultsContainer = document.querySelector('#nav-search-results-container');

let isSearchOpen = false;

function openNavSearch () {
    navSearchContainer.style.marginLeft = 0;
    navSearchContainer.classList.add('expand-nav-search');
    navbarTitle.style.display = 'none';
    closeNavSearchBtn.style.display = 'block';
    isSearchOpen = true;
    setTimeout(() => {
        navSearchInput.focus();
    }, 100);
}

function closeNavSearch () {
    navSearchContainer.style.marginLeft = 'auto';
    navSearchContainer.classList.remove('expand-nav-search');
    navbarTitle.style.display = 'block';
    closeNavSearchBtn.style.display = 'none';
    isSearchOpen = false;
    navSearchResultsContainer.classList.remove('expand');
    navSearchInput.value = '';
}

function addEventListenerToGlobalSearch () {
    navSearchInput.addEventListener('keyup', function (event) {
        if (event.target.value) {
            navSearchResultsContainer.classList.add('expand');
        } else {
            navSearchResultsContainer.classList.remove('expand');
        }
    });
}


const dictToFormData = (dict, formData) => {
    if (!formData) {
        // if no formdata is supplied for merging
        formData = new FormData();
    }

    for ( let key in dict ) {
        if (dict.hasOwnProperty(key)) {
            formData.append(key, dict[key]);
        }
    }
    return formData
}

const formToDict = (form) => {
    let dict = {}
    let form_elements = form.elements
    for (let i=0; i < form_elements.length; i++) {
        if (form_elements[i].name) {
            dict[form_elements[i].name] =form_elements[i].value
        }
    }
    return dict
}

function showDialog (message) {

}

function dictToURLArgs (dict) {
    let query = ''
    let size = Object.keys(dict).length

    let i = 0

    for (let key in dict) {
        i++
        if (dict.hasOwnProperty(key)) {
            if (dict[key]) {
                // Check if the value is not empty or null
                query += key + '=' + dict[key].toString()
                i < size ? query += '&' : null // If the counter is less than the size, add '&'
            }
        }
    }
    return query
}

onload_functions.push(addListenersToSideMenuLinks)
onload_functions.push(enableToggleSubMenuChildren)
onload_functions.push(enableDateInputs)
onload_functions.push(enableSrmRadioButtons)
onload_functions.push(enableCheckAllForTables)
onload_functions.push(enableAutoResizeTextArea)
onload_functions.push(addEventListenersToUpload)
onload_functions.push(addEventListenerToGlobalSearch)
onload_functions.push(initFlatPickerInstances)
onload_functions.push(initFlatPickerWithNoMinDate)
onload_functions.push(formBuilderDateInstances)
onload_functions.push(addOffsetsToSubSideMenuItems)



