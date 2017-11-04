function dropMenu(){
    document.getElementById("dropmenu").classList.toggle("show");
}

function chkView(){
    width=document.documentElement.clientWidth;
    if (width <= 736){
        document.getElementById("bannerIndex").src = "/static/img/bannerCell.png";
        document.getElementById("bannerIndex").class = "BannerCell";
    }
}