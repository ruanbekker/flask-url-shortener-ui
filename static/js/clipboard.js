function copyToClipboard() {
  var copyText = document.getElementById("input");
  copyText.select();
  document.execCommand("Copy");
}
