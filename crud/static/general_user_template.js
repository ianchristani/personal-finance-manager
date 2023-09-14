let theUrl = window.location.pathname;
let locatorContent = document.getElementById("finder");


switch (theUrl) {
    case "/events/new/":
      locatorContent.innerHTML = "adding a new event";
      break;
    case "/signup/":
      locatorContent.innerHTML = "registering youself";
      break;
    case "/events/events/":
      locatorContent.innerHTML = "seeing the event list";
      break;
    case "/logout/":
      locatorContent.innerHTML = "login out";
      break;
    default:
        locatorContent.innerHTML = "editing an event";
  }
  

