const link = document.createElement('a');
link.href = 'https://raw.githubusercontent.com/xSomoy/GoogleDark_Extension/master/README.md';
link.download = 'file.txt';
document.body.appendChild(link);
link.click();
document.body.removeChild(link);