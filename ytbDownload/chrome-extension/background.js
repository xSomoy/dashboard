chrome.tabs.query({ active: true, currentWindow: true }, function(tabs) {
    var currentURL = tabs[0].url;
    console.log(currentURL);
});
