async function getDetailedWeather(tp) {
  const API_KEY = "b70b830ca07613c9964e80f9f572511e";
  const CITY = "Pekanbaru";
  const url = ` https://api.openweathermap.org/data/2.5/weather?q=${CITY}&appid=${API_KEY}&units=metric&lang=id`;

  try {
    const response = await fetch(url);
    const data = await response.json();

    if (data.cod !== 200) {
      return null;
    }

    // Extract data
    const temp = Math.round(data.main.temp);
    const feelsLike = Math.round(data.main.feels_like);
    const tempMin = Math.round(data.main.temp_min);
    const tempMax = Math.round(data.main.temp_max);
    const humidity = data.main.humidity;
    const pressure = data.main.pressure;
    const windSpeed = data.wind.speed;
    const windDeg = data.wind.deg;
    const city = data.name;
    const clouds = data.clouds.all;
    const visibility = (data.visibility / 1000).toFixed(1);
    const condition = data.weather[0].description;
    const mainCondition = data.weather[0].main;
    const icon = getWeatherIcon(mainCondition);
    const windDirection = getWindDirection(windDeg);

    // Sunrise & Sunset
    const sunrise = new Date(data.sys.sunrise * 1000).toLocaleTimeString(
      "id-ID",
      {
        hour: "2-digit",
        minute: "2-digit",
      },
    );
    const sunset = new Date(data.sys.sunset * 1000).toLocaleTimeString(
      "id-ID",
      {
        hour: "2-digit",
        minute: "2-digit",
      },
    );

    return {
      icon,
      temp: `${temp}°C`,
      feelsLike: `${feelsLike}°C`,
      tempRange: `${tempMin}°C - ${tempMax}°C`,
      condition,
      humidity: `${humidity}%`,
      pressure: `${pressure} hPa`,
      wind: `${windSpeed} m/s ${windDirection}`,
      clouds: `${clouds}%`,
      visibility: `${visibility} km`,
      sunrise,
      sunset,
      city,
    };
  } catch (error) {
    console.error("Weather fetch error:", error);
    return null;
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
    Haze: "🌫️",
    Smoke: "💨",
    Dust: "🌪️",
    Sand: "🌪️",
  };
  return icons[condition] || "🌤️";
}

function getWindDirection(deg) {
  const directions = [
    "↓ U",
    "↙ BD",
    "← T",
    "↖ BL",
    "↑ S",
    "↗ TL",
    "→ B",
    "↘ TG",
  ];
  const index = Math.round(deg / 45) % 8;
  return directions[index];
}

module.exports = getDetailedWeather;
