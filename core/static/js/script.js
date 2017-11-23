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

function selection_list() {
    disciplinas=document.getElementById("disciplinas");
    if (disciplinas.classList.contains('show')){
        disciplinas.classList.remove('show');
    } else{
        disciplinas.classList.toggle('show');
    }
}


function error_message() {
  alert('{{ form.error }}');
}


function chkView(){
    width=document.documentElement.clientWidth;
    if (width <= 736){
        document.getElementById("bannerIndex").src = "/static/img/bannerCell.png";
        document.getElementById("bannerIndex").class = "BannerCell";
    }
}

function check_codigo() {
    var flag = document.getElementsByClassName("flag");
    var codigo = prompt("Digite o codigo de acesso", "");
    if (codigo == "ACERTOUMISERAVI"){
        alert("Codigo Correto");
        flag = "T";
    }else if(codigo == null){
        flag = "F";
    }else{
        alert("Código Invalido")
        check_codigo();
    }

function filtrarAlunos() {
    var getCurso=document.getElementById("filtroCurso").value;
    var getTurma=document.getElementById("filtroTurma").value;
    return getCurso,getTurma;
}
   /*//var flag = false;
    Do{
        var codigo = prompt("Digite o codigo de acesso", "");
        if (codigo == "ACERTOUMISERAVI"){
            alert("Codigo Correto");
            flag = true;
            break
        }else if(codigo == null){
            break
        }else{
            alert("Codigo Incorreto");
        }
    }while(true);
    //return flag;*/
}