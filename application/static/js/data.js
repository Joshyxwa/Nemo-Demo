
function retrieveJson() {
    // var config = {};
    // config.JSON_DATA = {JSON_DATA};
    // const jsonData= require(os.join(config.JSON_DATA, 'punc_text.json')); 
    // console.log(jsonData);
    // alert(str(jsonData))
    const fs = require('fs')
    fs.readFile('../json/punc_text.json', 'utf8', (err, jsonString) => {
    if (err) {
        console.log("File read failed:", err)
        return
    }
    console.log('File data:', jsonString) 
})
}

$(function(){
    $(".dropdown-menu").on('click', 'a', function(){
      $(".btn:first-child").text($(this).text());
      $(".btn:first-child").val($(this).text());
   });
});