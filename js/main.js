window.onscroll = function() {
    // 当页面滚动超过100px时显示按钮
    let scrollToTopBtn = document.getElementById
    ("scroll-to-top");
    if (document.body.scrollTop > 1400 || document.documentElement.scrollTop > 1400) {
        scrollToTopBtn.style.display = "block";
    } else {
        scrollToTopBtn.style.display = "none";
    }
};

/* 欢迎部分点击 */
function welcomeSectionClick() {
    let seClick = document.getElementById('welcome-section-h1');
    let secText = seClick.textContent;
    if (secText === "WELCOME") {
        seClick.textContent = '欢迎来到此网页';
        seClick.style.fontFamily = 'sans-serif';
      } else {
        seClick.textContent = 'WELCOME';
        seClick.style.fontFamily = "Georgia, 'Times New Roman', Times, serif";
      }
};
