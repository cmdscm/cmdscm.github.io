/* search */
var searchWayNum = 1;
function searchWays(){
    let searchFom = document.getElementById("search-form");
    let searchPut = document.getElementById("search-input");
    let searchImg = document.getElementById("search-img");
    let searchSub = document.getElementById("search-submit");
    let searchSec = document.querySelector("#search");
    let searchWay = document.getElementById("search-way");
    if(searchWayNum == 1){
        searchSec.classList.remove("search-bd");
        searchSec.classList.add("search-ts");
        searchWay.innerHTML = "切换至百度搜索";
        searchSub.value = "360搜索";
        searchImg.src = "./360.png";
        searchPut.name = "q";
        searchFom.action = "https://www.so.com/s";
        searchWayNum = 2;
    }else{
        searchSec.classList.replace("search-ts","search-bd");
        searchWay.innerHTML = "切换至360搜索";
        searchSub.value = "百度一下";
        searchImg.src = "./baidu.png";
        searchPut.name = "wd";
        searchFom.action = "https://www.baidu.com/s"
        searchWayNum = 1;
    }; 
};

