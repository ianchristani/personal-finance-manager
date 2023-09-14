let theUrl = window.location.pathname;
let locatorContent = document.getElementById("finder");


switch (theUrl) {
    case "/login/":
      locatorContent.innerHTML = "login in";
      break;
    case "/signup/":
      locatorContent.innerHTML = "signing up";
      break;
    default:
        locatorContent.innerHTML = "home";
  }