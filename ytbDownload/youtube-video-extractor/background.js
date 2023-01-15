function extractYoutubeVideoUrl() {
    chrome.tabs.query({active: true, currentWindow: true}, function(tabs) {
        var currentTab = tabs[0];
        var url = currentTab.url;
        // Regular expression to match the YouTube video URL
        var regExp = /^(https?\:\/\/)?(www\.youtube\.com|youtu\.?be)\/.+$/;
        var match = url.match(regExp);

        if (match) {
            // Return the YouTube video URL
            return url;
        } else {
            // Return null if the current tab is not a YouTube video
            return null;
        }
    });
}

chrome.browserAction.onClicked.addListener(function(tab) {
    chrome.tabs.executeScript({
        code: '(' + extractYoutubeVideoUrl + ')();'
    }, (results) => {
        var videoUrl = results[0];
        alert(`The video url is ${videoUrl}`);
    });
});
