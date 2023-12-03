/* 查找 */
var canvas = document.querySelector("#header-logo");
var cl = canvas.getContext("2d");
/* 设置 */
cl.strokeStyle = 'yellow';
cl.fillStyle = 'orange';
cl.lineWidth = 10;
/* 字母G */
cl.beginPath();
cl.moveTo(80,10);
cl.lineTo(10,40);
cl.lineTo(40,120);
cl.lineTo(110,90);
cl.lineTo(90,45);
cl.lineTo(60,60);
cl.stroke();
cl.closePath();
/* 字母Y */
cl.strokeStyle = 'orange';
cl.beginPath();
cl.moveTo(105,10);
cl.lineTo(130,60);
cl.lineTo(130,120);
cl.stroke();
cl.closePath();
cl.strokeStyle = 'orange';
cl.beginPath();
cl.moveTo(130,60);
cl.lineTo(155,10);
cl.stroke();
cl.closePath();
/* 字母Q */
cl.strokeStyle = 'blue';
cl.beginPath();
cl.moveTo(220,80);
cl.lineTo(260,120);
cl.stroke();
cl.closePath();
cl.beginPath();
cl.arc(210,70,50,Math.PI*2.2,Math.PI*0.3,true);
cl.stroke();
cl.closePath();