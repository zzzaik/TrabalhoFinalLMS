function dropMenu(id){
    document.getElementById(id).classList.toggle("show");
}

function dropLogin(id){
    document.getElementById(id).style.display='block';
}
function liftLogin(id){
    document.getElementById(id).style.display='none';
}




function chkView(){
    width=document.documentElement.clientWidth;
    if (width <= 736){
        document.getElementById("bannerIndex").src = "/static/img/bannerCell.png";
        document.getElementById("bannerIndex").class = "BannerCell";
    }
}