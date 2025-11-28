
const locationInput = document.getElementById("location_input");
const apiKey = "bce57c6c23e694e416c74b9220d5c3cf";

const locationOutput = document.getElementById("location_output");
const temperatureOutput = document.getElementById("temperature_output");
const windOutput = document.getElementById("wind_output");
const conditionOutput = document.getElementById("condition_output");

locationInput.addEventListener("keydown", function(event) {
    if (event.key === "Enter") {
        getWeather();
    }
});

async function getWeather() {
    const cityName = locationInput.value.trim();
    if (!cityName) return alert("Please enter a city name!");

    const apiUrl = `https://api.openweathermap.org/data/2.5/weather?q=${cityName}&appid=${apiKey}&units=metric`;

    try {
        const response = await fetch(apiUrl);
        if (!response.ok) throw new Error(`HTTP error! Status: ${response.status}`);

        const weatherData = await response.json();

        locationOutput.innerHTML = weatherData.name;
        temperatureOutput.innerHTML = `${weatherData.main.temp} °C`;
        windOutput.innerHTML = `${weatherData.wind.speed} MPH`;
        conditionOutput.innerHTML = weatherData.weather[0].description;

    } catch (error) {
        console.log(error);
        alert("Could not fetch weather data. Try again.");
    }
}
