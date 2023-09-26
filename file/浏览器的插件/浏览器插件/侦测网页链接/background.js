chrome.tabs.onUpdated.addListener(function(tabId, changeInfo, tab) {
    if (changeInfo.status === 'loading') {
      // 在这里定义你要监听的特定关键词
      var keyword = "迷你屎界";
      var url = tab.url;
      
      if (url.includes(keyword)) {
        chrome.tabs.remove(tabId);
        showNotification();
      }
    }
  });
  
  function showNotification() {
    // 创建一个1秒钟自动关闭的通知
    var options = {
      type: "basic",
      title: "警告",
      message: "此网页可能包含敏感信息",
      iconUrl: "icon.png"
    };
  
    chrome.notifications.create("", options, function(notificationId) {
      setTimeout(function() {
        chrome.notifications.clear(notificationId);
      }, 1000);
    });
  }
  