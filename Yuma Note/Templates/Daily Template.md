---
created: <% tp.date.now("YYYY-MM-DD") %>
day: <% tp.date.now("dddd") %>
weather: <%* tR += await tp.user.weather(tp) %>
mood: <% tp.system.suggester(["😊 Senang", "😌 Tenang", "😐 Biasa", "😓 Lelah"], ["happy", "calm", "neutral", "tired"]) %>
tags: [Daily]
---

# <% tp.date.now("dddd, DD MMM YYYY") %>

<%* 
const detailedWeather = await tp.user.weatherDetailed(tp);
if (detailedWeather) {
    tR += `> [!info]- ${detailedWeather.icon} **Cuaca: ${detailedWeather.condition}**\n`;
    tR += `City 🏙️: **${detailedWeather.city}**\n`;
    tR += `> \n`;
    tR += `> **🌡️ Suhu Udara**\n`;
    tR += `> - Saat ini: **${detailedWeather.temp}** (terasa ${detailedWeather.feelsLike})\n`;
    tR += `> - Range: ${detailedWeather.tempRange}\n`;
    tR += `> \n`;
    tR += `> **🌤️ Kondisi Atmosfer**\n`;
    tR += `> - 💧 Kelembaban: ${detailedWeather.humidity}\n`;
    tR += `> - 🌬️ Angin: ${detailedWeather.wind}\n`;
    tR += `> - ☁️ Awan: ${detailedWeather.clouds}\n`;
    tR += `> - 👁️ Jarak Pandang: ${detailedWeather.visibility}\n`;
    tR += `> - 🔽 Tekanan: ${detailedWeather.pressure}\n`;
    tR += `> \n`;
    tR += `> **🌅 Matahari**\n`;
    tR += `> - Terbit: ${detailedWeather.sunrise} | Terbenam: ${detailedWeather.sunset}\n\n`;
}
%>

## ⚡ Prioritas
- [ ] <% tp.file.cursor() %>
- [ ] 
- [ ] 

## 🎯 Fokus Hari Ini
> 

## 📝 Catatan
**Yang Dilakukan:**
- 

**Learning:**
- 

**Gratitude:**
- 

---
*Dibuat: <% tp.date.now("HH:mm") %> | Week <% tp.date.now("ww") %>*