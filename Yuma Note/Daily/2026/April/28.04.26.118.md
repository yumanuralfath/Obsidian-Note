---
created: <% tp.date.now("YYYY-MM-DD") %>
day: <% tp.date.now("dddd") %>
weather: <%* tR += await tp.user.weather(tp) %>
tags:
  - Daily
---
# ⚡ Priority

- [ ] <% tp.file.cursor() %>
- [ ] 

# 📝 Note

- 





---
<%*
const y = moment().subtract(1, 'day');
const t = moment().add(1, 'day');

const link = (m) => {
  return `[[${m.format("DD.MM.YY.DDD")}]]`;
};

tR += `⬅️ ${link(y)}  |  📅 ${moment().format("dddd, DD MMM YYYY")}  |  ${link(t)} ➡️`;
%>

*Dibuat: <% tp.date.now("HH:mm") %> | Week <% tp.date.now("ww") %>*