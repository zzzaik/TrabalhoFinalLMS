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