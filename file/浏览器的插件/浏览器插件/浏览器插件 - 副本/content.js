function createUrlDiv() {
    const urlDiv = document.createElement('div');
    urlDiv.style.position = 'fixed';
    urlDiv.style.top = '10px';
    urlDiv.style.right = '10px';
    urlDiv.style.backgroundColor = 'rgba(0, 0, 0, 0.8)';
    urlDiv.style.color = '#fff';
    urlDiv.style.padding = '5px 10px';
    urlDiv.style.fontFamily = 'Arial, sans-serif';
    urlDiv.style.fontSize = '12px';
    urlDiv.style.zIndex = '9999';
    document.body.appendChild(urlDiv);
    return urlDiv;
  }
  
  function updateUrlDiv() {
    const currentUrl = window.location.href;
    const urlDiv = document.getElementById('urlDiv');
    if (urlDiv) {
      urlDiv.textContent = currentUrl;
    } else {
      const newUrlDiv = createUrlDiv();
      newUrlDiv.setAttribute('id', 'urlDiv');
      newUrlDiv.textContent = currentUrl;
    }
  }
  
  updateUrlDiv();
  