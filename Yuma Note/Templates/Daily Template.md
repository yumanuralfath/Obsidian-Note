---
created: <% tp.date.now("YYYY-MM-DD") %>
day: <% tp.date.now("dddd") %>
weather: <%* tR += await tp.user.weather(tp) %>
mood: <% tp.system.suggester(["😊 Senang", "😌 Tenang", "😐 Biasa", "😓 Lelah"], ["happy", "calm", "neutral", "tired"]) %>
tags: [Daily]
---
<%*
const w = await tp.user.weatherDetailed(tp);

if (w) {
tR += `
<details style="
  border: 1px solid #777;
  border-radius: 10px;
  padding: 8px 12px;
  margin: 12px 0;
  backdrop-filter: blur(6px);
  background-color: color-mix(in srgb, var(--background-primary) 90%, transparent);
  transition: all 0.3s ease;
">
  <summary style="
    font-size: 1.05em;
    font-weight: 600;
    cursor: pointer;
    display: flex;
    align-items: center;
    gap: 8px;
    list-style: none;
    padding: 4px 0;
  ">
    ${w.icon} Cuaca ${w.city} — ${w.condition}
  </summary>

  <div style="margin-top: 8px; padding-left: 6px; line-height: 1.7; font-size: 0.95em;">

  <p><b>🌡️ Suhu Udara</b><br>
  • Saat ini: <b>${w.temp}</b> (terasa ${w.feelsLike})<br>
  • Range: ${w.tempRange}</p>

  <p><b>🌤️ Kondisi Atmosfer</b><br>
  • 💧 Kelembaban: ${w.humidity}<br>
  • 🌬️ Angin: ${w.wind}<br>
  • ☁️ Awan: ${w.clouds}<br>
  • 👁️ Jarak Pandang: ${w.visibility}<br>
  • 🔽 Tekanan: ${w.pressure}</p>

  <p><b>🌅 Matahari</b><br>
  • Terbit: ${w.sunrise} | Terbenam: ${w.sunset}</p>

  </div>
</details>
`;
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

## 🗓️ Tomorrow Plans 
- 
---
*Dibuat: <% tp.date.now("HH:mm") %> | Week <% tp.date.now("ww") %>*