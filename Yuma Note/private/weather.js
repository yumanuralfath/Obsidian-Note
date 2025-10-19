// weather.js
async function getWeather(tp) {
  const API_KEY = "b70b830ca07613c9964e80f9f572511e";
  const CITY = "Pekanbaru";
  const url = `https://api.openweathermap.org/data/2.5/weather?q=${CITY}&appid=${API_KEY}&units=metric&lang=id`;

  try {
    const response = await fetch(url);
    const data = await response.json();

    const temp = Math.round(data.main.temp);
    const desc = data.weather[0].description;
    const icon = getWeatherIcon(data.weather[0].main);

    return `${icon} ${temp}°C - ${desc}`;
  } catch (error) {
    return "☁️ Weather unavailable";
  }
}

function getWeatherIcon(condition) {
  const icons = {
    Clear: "☀️",
    Clouds: "☁️",
    Rain: "🌧️",
    Drizzle: "🌦️",
    Thunderstorm: "⛈️",
    Snow: "❄️",
    Mist: "🌫️",
    Fog: "🌫️",
  };
  return icons[condition] || "🌤️";
}

module.exports = getWeather;
