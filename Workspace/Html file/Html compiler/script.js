function run() {
    var code = document.getElementById("codeInput");
    var output = document.getElementById("output");
    output.innerHTML = code.value;
}
function copy() {
    var textToCopy = document.getElementById("codeInput");
    textToCopy.select();
    document.execCommand("copy");
}