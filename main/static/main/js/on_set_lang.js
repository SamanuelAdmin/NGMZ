const langCookieName = "setlang";

let langInputs = document.getElementsByClassName('setLanguageInput');

function getCookie(cname) {
  let name = cname + "=";
  let decodedCookie = decodeURIComponent(document.cookie);
  let ca = decodedCookie.split(';');
  for(let i = 0; i <ca.length; i++) {
    let c = ca[i];
    while (c.charAt(0) == ' ') {
      c = c.substring(1);
    }
    if (c.indexOf(name) == 0) {
      return c.substring(name.length, c.length);
    }
  }
  return "";
}

function onLiClick() {
    const d = new Date();
    d.setTime(d.getTime() + (1*24*60*60*1000)); // on one day
    let expires = "expires="+ d.toUTCString();

    document.cookie = langCookieName + "=" + "true" + ";" + expires + ";path=/";
}

for (let li of langInputs) {
    li.onclick = onLiClick;
}

// show changeLang window is lang is not changed
if (getCookie(langCookieName) !== "true" ) {
    document.getElementById("changeLanguageWindow").style.display = "flex";
}