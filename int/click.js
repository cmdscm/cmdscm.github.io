/* search */
var searchWayNum = 1
var searchSec = document.querySelector("#search")
var searchWay = document.getElementById("search-way");
var searchSub = document.getElementById("search-submit");
var searchImg = document.getElementById("search-img");
function searchWays(){
    let searchImg = document.getElementById("search-img");
    let searchSub = document.getElementById("search-submit");
    let searchSec = document.querySelector("#search");
    let searchWay = document.getElementById("search-way");
    if(searchWayNum == 1){
        searchSec.classList.remove("search-bd");
        searchSec.classList.add("search-ts");
        searchWay.innerHTML = "切换至百度搜索";
        searchSub.value = "360搜索";
        searchWayNum = 2;
    }else{
        searchSec.classList.replace("search-ts","search-bd");
        searchWay.innerHTML = "切换至360搜索";
        searchSub.value = "百度一下";
        searchWayNum = 1;
    }; 
};

