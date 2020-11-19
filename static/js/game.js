function processDatabase() {
   var txt=document.getElementById("fileproc").value;
   var url='/processDatabase/'+txt;
   fetch(url).then(function(response) {
      return response.json();
   }).then(function(response) {
      var mydata = response['filename'];
      console.log(mydata);
   });
}

function loadGame() {
   var url='/browser';
   fetch(url).then(function(response) {
      return response;
   })
}

function setVisible() {
  document.getElementById("uploadBtn").style.display = "block"
  document.getElementById("myload").style.display = "block"
}

function loadMoves() {
  var txt=document.getElementById("arena").value;
  document.getElementById("moves").value = "loading.."+txt;
  var url='/loadMoves/'+txt;
  fetch(url).then(function(response) {
      return response.json();
  }).then(function(response) {
      var mydata = response['filename'];
      console.log(mydata);
  });
}

$('#processBtn').on('click', processDatabase)
$('#loadGameBtn').on('click', loadGame)
$('#filenameBtn').on('click', setVisible)
$('#closeBtn').on('click', setVisible)
$('#arenaBtn').on('click', loadMoves)