function menu_function() {
    document.getElementById("drop").classList.toggle("show");
}

window.onclick = function(event) {
  if (!event.target.matches('.dropbtn')) {

    var dropdowns = document.getElementsByClassName("menu_content");
    var i;
    for (i = 0; i < dropdowns.length; i++) {
      var openDropdown = dropdowns[i];
      if (openDropdown.classList.contains('show')) {
        openDropdown.classList.remove('show');
      }
    }
  }
}

function login_function() {
  document.getElementById("drop_login").classList.toggle("show");
}

window.onclick = function(event) {
  if (!event.target.matches('.user')) {

    var dropdowns = document.getElementsByClassName("contudo");
    var i;
    for (i = 0; i < dropdowns.length; i++) {
      var openDropdown = dropdowns[i];
      if (openDropdown.classList.contains('show')) {
        openDropdown.classList.remove('show');
      }
    }
  }
}

function error_message() {
  alert('{{ form.error }}')  
}

