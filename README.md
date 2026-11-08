<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Владелец</title>
    <script src="https://telegram.org/js/telegram-web-app.js"></script>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            background-color: var(--tg-theme-bg-color, #ffffff);
            color: var(--tg-theme-text-color, #000000);
            padding: 16px;
        }
        h1 { font-size: 24px; font-weight: 600; margin-bottom: 20px; }
        .tabs {
            display: flex; gap: 8px; margin-bottom: 20px;
        }
        .tab {
            flex: 1; padding: 12px; border: none; border-radius: 8px;
            background-color: var(--tg-theme-secondary-bg-color, #f5f5f5);
            color: var(--tg-theme-text-color, #000000);
            font-size: 16px; font-weight: 500; cursor: pointer;
        }
        .tab.active {
            background-color: var(--tg-theme-button-color, #3390ec);
            color: var(--tg-theme-button-text-color, #ffffff);
        }
        .content { display: none; }
        .content.active { display: block; }
        .stats-card {
            background-color: var(--tg-theme-secondary-bg-color, #f5f5f5);
            border-radius: 12px; padding: 16px; margin-bottom: 12px;
        }
        .stat-row {
            display: flex; justify-content: space-between; align-items: center;
            padding: 8px 0; border-bottom: 1px solid var(--tg-theme-hint-color, #e0e0e0);
        }
        .stat-row:last-child { border-bottom: none; }
        .stat-label { font-size: 14px; color: var(--tg-theme-hint-color, #666666); }
        .stat-value { font-size: 16px; font-weight: 600; }
        .stat-value.positive { color: #4caf50; }
        .stat-value.negative { color: #f44336; }
        .stat-detail { font-size: 12px; color: var(--tg-theme-hint-color, #999999); margin-top: 4px; }
        
        .client-card {
            background-color: var(--tg-theme-secondary-bg-color, #f5f5f5);
            border-radius: 12px; padding: 16px; margin-bottom: 12px; cursor: pointer;
        }
        .client-header {
            display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px;
        }
        .client-name { font-size: 16px; font-weight: 600; }
        .client-debt { font-size: 16px; font-weight: 600; }
        .client-debt.zero { color: #4caf50; }
        .client-debt.has-debt { color: #f44336; }
        .client-stats {
            display: flex; gap: 16px; font-size: 13px;
            color: var(--tg-theme-hint-color, #666666);
        }
    </style>
</head>
<body>
    <h1>👔 Панель управления</h1>
    
    <div class="tabs">
        <button class="tab active" data-tab="results">💰 Итоги</button>
        <button class="tab" data-tab="clients">🤝 Клиенты</button>
    </div>
    
    <div id="results" class="content active">
        <div class="stats-card">
            <div class="stat-row">
                <span class="stat-label">Выручка</span>
                <span class="stat-value">1 250 000 сум</span>
            </div>
            <div class="stat-detail">50 порций × 25 000</div>
            
            <div class="stat-row">
                <span class="stat-label">Себестоимость</span>
                <span class="stat-value">650 000 сум</span>
            </div>
            <div class="stat-detail">проданных порций</div>
            
            <div class="stat-row">
                <span class="stat-label">До налогов</span>
                <span class="stat-value positive">400 000 сум</span>
            </div>
            <div class="stat-detail">после постоянных затрат</div>
        </div>
        
        <div class="stats-card">
            <div class="stat-row">
                <span class="stat-label">Долг клиентов</span>
                <span class="stat-value negative">250 000 сум</span>
            </div>
            
            <div class="stat-row">
                <span class="stat-label">Получено оплат</span>
                <span class="stat-value">1 000 000 сум</span>
            </div>
            
            <div class="stat-row">
                <span class="stat-label">Остаток продуктов</span>
                <span class="stat-value">400 000 сум</span>
            </div>
            <div class="stat-detail">Купили на 1 млн; израсходовали 600 тыс.</div>
        </div>
    </div>
    
    <div id="clients" class="content">
        <div class="client-card">
            <div class="client-header">
                <span class="client-name">Компания А</span>
                <span class="client-debt zero">Долг: 0</span>
            </div>
            <div class="client-stats">
                <span>Отгружено: 500 000</span>
                <span>Оплачено: 500 000</span>
            </div>
        </div>
        
        <div class="client-card">
            <div class="client-header">
                <span class="client-name">Компания Б</span>
                <span class="client-debt has-debt">Долг: 250 000</span>
            </div>
            <div class="client-stats">
                <span>Отгружено: 750 000</span>
                <span>Оплачено: 500 000</span>
            </div>
        </div>
    </div>
    
    <script>
        const tg = window.Telegram.WebApp;
        tg.ready();
        tg.expand();
        
        document.querySelectorAll('.tab').forEach(tab => {
            tab.addEventListener('click', () => {
                document.querySelectorAll('.tab').forEach(t => t.classList.remove('active'));
                document.querySelectorAll('.content').forEach(c => c.classList.remove('active'));
                tab.classList.add('active');
                document.getElementById(tab.dataset.tab).classList.add('active');
            });
        });
    </script>
</body>
</html>
