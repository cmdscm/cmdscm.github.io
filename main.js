var titletext = ['Welcome','欢迎','Willkommen','歡迎','Вітаем']
var titlenum = 0
var cards = document.getElementsByClassName('card')
var title = document.getElementById('header-title');
var idSection = document.querySelector('.id-card')
var ID = [
    {
        'img': 'https://i2.hdslb.com/bfs/face/a88d3fcd35445501bfd36f990bca54089cd8756b.jpg@240w_240h_1c_1s_!web-avatar-nav.avif',
        'title': 'B站',
        'name': '聪明的电八',
        'link': 'https://space.bilibili.com/1402300157',
    },
    {
        'img': 'https://i2.hdslb.com/bfs/face/a88d3fcd35445501bfd36f990bca54089cd8756b.jpg@240w_240h_1c_1s_!web-avatar-nav.avif',
        'title': '抖音',
        'name': '聪明的电八',
        'link': 'https://www.douyin.com/user/MS4wLjABAAAAirUr-0g0uV7dLXxfVRLd7Ksngu0Ln2X_e5Ydc3RcTxAOHjFYCIx-3ORgRSUJpq9v',
    },
    {
        'img': 'https://avatars.githubusercontent.com/u/134817738?v=4',
        'title': 'Github',
        'name': 'cmdscm',
        'link': 'https://github.com/cmdscm',
    },
    {
        'img': 'https://m.ccw.site/avatar/62df9aa87c888254d55b6f6a/6768a331-c1cc-4767-896c-895ed1791c05.jpg?x-oss-process=image%2Fresize%2Cs_150%2Fformat%2Cwebp',
        'title': '共创世界',
        'name': '懒得要告诉你',
        'link': 'https://www.ccw.site/student/62df9aa87c888254d55b6f6a',
    },
    {
        'img': 'https://m.ccw.site/avatar/62df9aa87c888254d55b6f6a/6768a331-c1cc-4767-896c-895ed1791c05.jpg?x-oss-process=image%2Fresize%2Cs_150%2Fformat%2Cwebp',
        'title': 'QQ',
        'name': '懒得要告诉你',
        'link': 'https://im.qq.com/index/',
    },
    {
        'img': 'https://assets.codepen.io/t-1/user-default-avatar.jpg?fit=crop&format=auto&height=512&version=0&width=512',
        'title': 'codepen',
        'name': 'cmdscm',
        'link': 'https://codepen.io/cmdscm',
    },
]
var profiles = [
    {
        'title': '性别' ,
        'text': '男',
        'i': "fa-solid fa-mars",
        'iColor': 'blue',
    },
    {
        'title': '年龄' ,
        'text': '12',
        'i': 'fa-solid fa-cake-candles',
        'iColor': 'pink',
    },
    {
        'title': '生肖' ,
        'text': '兔',
        'i': "fa-solid fa-paw",
        'iColor': 'lightgreen',
    },
    {
        'title': '星座' ,
        'text': '处女',
        'i': "fa-solid fa-star-and-crescent",
        'iColor': 'purple',
    },
    {
        'title': '兴趣爱好' ,
        'text': '编程',
        'i': "fa-solid fa-code",
        'iColor': 'green',
    },
    {
        'title': '喜欢的游戏' ,
        'text': 'MC/蛋仔',
        'i': "fa-solid fa-gamepad",
        'iColor': 'red',
    },
]
var updates = [
    {
        'title': '1.0',
        'time': '23/02/11',
    },
    {
        'title': '2.0',
        'time': '23/04/29',
    },
    {
        'title': '3.0',
        'time': '23/05/17',
    },
    {
        'title': '4.0',
        'time': '23/09/05',
    },
    {
        'title': '5.0',
        'time': '23/12/04',
    },
    {
        'title': '6.0',
        'time': '24/07/xx',
    },
]

var isdoing = false
function makeId(){
    for (var i = 0; i<ID.length;i++){
        let idCard = document.createElement('div');
        idCard.className = 'id-id'
        idSection.appendChild(idCard)
        let img = document.createElement('img');
        img.src = ID[i].img
        idCard.appendChild(img);
        let title = document.createElement('h4');
        title.className = 'id-title'
        title.innerHTML = ID[i].title
        idCard.appendChild(title);
        let name = document.createElement('p');
        name.className = 'id-name'
        name.innerHTML = ID[i].name
        idCard.appendChild(name);
        let link = document.createElement('a');
        link.className = 'id-link'
        link.target = '_blank'
        link.href = ID[i].link
        idCard.appendChild(link);
        let I = document.createElement('i');
        I.className = "fa-solid fa-angles-right"
        link.appendChild(I)
    }
}

function makeProfile(){
    var profile = document.querySelector('#profile .section .profile-card')
    for(var i = 0;i<profiles.length;i++){
        let txt = `<div class="profile-item">
            <div class="profile-title">
                <h4>${profiles[i].title}</h4>
            </div>
            <div class="profile-i">
                <i class="${profiles[i].i}" style="color:${profiles[i].iColor};"></i>
            </div>
            <div class="profile-text">
                <p>${profiles[i].text}</p>
            </div>
        </div>`
        profile.innerHTML += txt
    }
}

function makeUpdate(){
    var update = document.querySelector('#update .section .update-card')
    for(var i = 0;i<updates.length;i++){
        let txt = `<div class="update-item">
        <div class="update-title">
            <h4>${updates[i].title}</h4>
        </div>
        <div class="update-time">
            <p>${updates[i].time}</p>
        </div>
    </div>`
        update.innerHTML += txt
    }
}

function reTitle(){
    titlenum += 1
    if (titlenum > titletext.length-1){
        titlenum = 0
    }
    title.innerHTML = titletext[titlenum]
    title.className = 'show'
}

function getRandom(start,end){
    list = []
    for(let i = start;i<=end;i++){
        list += i
    }
    let a = Math.random().toFixed(1) * 10
    if (a >= list.length){
        return list[a % list.length]
    }
    return list[a]
}

function showCard(showNum,cardNum){
    let card = cards[cardNum]
    card.classList.remove('transparent1')
    if (showNum == 1){card.style.top = '-100%'} else
    if (showNum == 2){card.style.top = '100%'} else
    if (showNum == 3){card.style.left = '-100%'} else
    if (showNum == 4){card.style.left = '100%'}
    setTimeout(() => {
        card.style.top = '0'
        card.style.left = '0'
        card.classList.add('show')
        isdoing = false
    }, 100); 
}

var num = '1'
function recard(event,cardNum=-1){
    if (isdoing){return}
    var isdoing = true
    if (event != undefined && num == event.srcElement.ariaValueText){
        var isdoing = false
        return
    }
    for (let i = 0; i<cards.length;i++){
            cards[i].classList.add('transparent1')
            cards[i].classList.remove('show')
    }
    if (event == undefined && cardNum > -1){
        return showCard(getRandom(1,4),cardNum)
    }
    var num = event.srcElement.ariaValueText
    return showCard(getRandom(1,4),num-1)
}
makeId();
makeProfile();
makeUpdate();
recard(undefined,0)
setInterval(()=>{
    title.className = 'transparent'
    setTimeout(reTitle,300)
},10000);