# Telegram Bot for Monitoring VPS Fornex

<h4>Телеграмм бот для мониторинга конфигураций VPS на хостинге Fornex и управления ими через API Fornex.</h4>
<hr>
Бот сделан на <b>aiogram</b>, что позволяет асинхронно использовать функции бота.

Для использования достаточно изменить файл <b><i>.env.example</i></b> на <b><i>.env</i></b>, затем добавить в него ключи от телеграмм бота и API Fornex.

Бот запускается с команды:
<code>python bot.py</code>
<hr>

Помимо этого присутствует Dockerfile для контейнирезации:
<p style='text-align: center;'><code>docker build -t ваш тег .</code></p>
<p style="text-align: center;"><code>docker run -d ваш тег</code></p>