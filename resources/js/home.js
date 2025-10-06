function Time() {
    var today = new Date();
    var h = today.getHours();
    var m = today.getMinutes();
    var s = today.getSeconds();
    m = checkTime(m);
    s = checkTime(s);
    document.getElementById('horloge').innerHTML =
    h + ":" + m + ":" + s;
    var date = new Date;
    var annee = date.getFullYear();
    var moi = date.getMonth();
    var mois = new Array('Janvier', 'Février', 'Mars', 'Avril', 'Mai', 'Juin', 'Juillet', 'Aôut', 'Septembre', 'Octobre', 'Novembre', 'Décembre');
    var j = date.getDate();
    var jour = date.getDay();
    var jours = new Array('Dimanche', 'Lundi', 'Mardi', 'Mercredi', 'Jeudi', 'Vendredi', 'Samedi');
    var resultat = jours[jour]+' '+j+' '+mois[moi]+' '+annee;
    $('#date').text(resultat);
    var t = setTimeout(Time, 500);
}

function checkTime(i) {
  if (i < 10) {i = "0" + i};  // add zero in front of numbers < 10
    return i;
}

function weather() {
  var api = new XMLHttpRequest();
  api.open("GET", "http://api.openweathermap.org/data/2.5/weather?q=Villeurbanne&appid=33b1082fef775d69d48a6f08edbf88bb&lang=fr&units=metric");
  api.responseType = 'json';
  api.send();
  api.onload = function() {
    var api_json = api.response;
    $('#temp').text(api_json["main"]["temp"].toFixed(1) + ' °C');
    var cont_home = document.getElementById('img_home');
    var img_home = document.createElement('img');
    img_home.width = "70";
    img_home.src = "../image/weather/" + api_json["weather"]["0"]["icon"] + ".png";
    cont_home.appendChild(img_home);  
  };
}