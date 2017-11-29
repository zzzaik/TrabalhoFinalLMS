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

  var dropdowns = document.getElementsByClassName("conteudo");
  var i;
  for (i = 0; i < dropdowns.length; i++) {
    var openDropdown = dropdowns[i];
    if (openDropdown.classList.contains('show')) {
      openDropdown.classList.remove('show');
    }
  }
}
}

function matricula_function() {
  document.getElementById("liDrop").classList.toggle("show");
}

window.onclick = function(event) {
if (!event.target.matches('.matricula')) {

  var dropdowns = document.getElementsByClassName("selection_List");
  var i;
  for (i = 0; i < dropdowns.length; i++) {
    var openDropdown = dropdowns[i];
    if (openDropdown.classList.contains('show')) {
      openDropdown.classList.remove('show');
    }
  }
}
}

function selection_list() {
  disciplinas=document.getElementById("disciplinas");
  if (disciplinas.classList.contains('show')){
      disciplinas.classList.remove('show');
  } else{
      disciplinas.classList.toggle('show');
  }
}