
function changeGetArgs(func) {
    const queryString = window.location.search;
    return new URLSearchParams(queryString);
}

function reloadWithNewParams(urlParams) {
    window.location = window.location.href.split('?')[0] + '?' + urlParams.toString();
}

function changePathParams(key, value) {
    let urlParams = changeGetArgs();
    urlParams.set(key, value);
    reloadWithNewParams(urlParams);
}