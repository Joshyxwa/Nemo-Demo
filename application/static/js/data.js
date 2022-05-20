$(document).ready(function () {
  $('#audiofile').on("change",function() {
    var i = $(this).prev('label').clone();
    var file = $('#audiofile')[0].files[0].name;
    $(this).prev('label').text(file);
  });
  
  function retrieveJson() {

      const fs = require('fs')
      fs.readFile('../json/punc_text.json', 'utf8', (err, jsonString) => {
      if (err) {
          console.log("File read failed:", err)
          return
      }
      return jsonString
      // console.log('File data:', jsonString) 
  })
  }
  document.body.onload = addElement;
  function addElement () {
      // create a new div element
      const newDiv = document.createElement("p");
    
      const obj = JSON.parse(retrieveJson());

      console.log(obj.punc_text)
      // and give it some content
      const newContent = document.createTextNode(obj.punc_text);
    
      // add the text node to the newly created div
      newDiv.appendChild(newContent);
    
      // add the newly created element and its content into the DOM
      const element = document.getElementById("result");
      const child = document.getElementById("transcribed_header");
      element.insertAdjacentElement(newDiv, child);
    }

  $(function(){
      $(".dropdown-menu").on('click', 'a', function(){
        $(".btn:first-child").text($(this).text());
        $(".btn:first-child").val($(this).text());
    });
  });

})