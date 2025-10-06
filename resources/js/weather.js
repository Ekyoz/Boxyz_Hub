function weather() {
    var api = new XMLHttpRequest();
    // Load configuration from config.js
    const config = require('../../config.js');
    const apiUrl = `http://api.openweathermap.org/data/2.5/weather?q=${config.weatherCity}&appid=${config.openWeatherMapApiKey}&lang=fr&units=metric`;
    api.open("GET", apiUrl);
    api.responseType = 'json';
    api.send();
    api.onload = function() {
        var api_json = api.response;
        $('#weather').text(api_json["weather"]["0"]["description"]);
        $('#hum').text(api_json["main"]["humidity"] + ' %');
        $('#vent').text(api_json["wind"]["speed"] + ' KM/H');
        $('#temp').text(api_json["main"]["temp"].toFixed(1) + ' °C');
        $('#temp_max').text(api_json["main"]["temp_max"].toFixed(0) + ' °C');
        $('#temp_min').text(api_json["main"]["temp_min"].toFixed(0) + ' °C');
        var cont = document.getElementById('img_weather');
        var img = document.createElement('img');
        img.src = "../image/weather/" + api_json["weather"]["0"]["icon"] + ".png";
        cont.appendChild(img);
    };
}