function dropMenu(id){
    if (id == 'dropmenu'){
        document.getElementById(id).classList.toggle("show");
    } else if(id == 'loginForm'){
        document.getElementById(id).classList.toggle("showF");
    }
    
}

function chkView(){
    width=document.documentElement.clientWidth;
    if (width <= 736){
        document.getElementById("bannerIndex").src = "/static/img/bannerCell.png";
        document.getElementById("bannerIndex").class = "BannerCell";
    }
}