document.getElementById("submit").addEventListener("click", getWeather);
const input = document.getElementById("location");
const apiKey = "bce57c6c23e694e416c74b9220d5c3cf";

async function getWeather() {
  const city = input.value.trim();
  if (!city) {
    alert("Please enter a city name!");
    return;
  }

  const apiurl = `https://api.openweathermap.org/data/2.5/weather?q=${city}&appid=${apiKey}&units=metric`;

  try {
    const response = await fetch(apiurl);
    if (!response.ok) {
      throw new Error(`HTTP error! Status: ${response.status}`);
    }

    const weatherdata = await response.json();

    document.getElementById("weather").innerHTML = `
      <h1>${weatherdata.name}</h1>
      <p>Temperature: ${weatherdata.main.temp}°C</p>
      <p>${weatherdata.weather[0].description}</p>
      <p>${weatherdata.main.humidity}</p>
      <p>${weatherdata.wind.speed}</p>
    `;
    const message = new SpeechSynthesisUtterance(`in ${weatherdata.name} it is ${weatherdata.main.temp} and ${weatherdata.weather[0].description} also at ${weatherdata.main.humidity} humidity and ${weatherdata.wind.speed} wind speed`);
    message.rate = 0.5;  
    window.speechSynthesis.speak(message);
  } catch (error) {
    console.log(error);
  }
}
