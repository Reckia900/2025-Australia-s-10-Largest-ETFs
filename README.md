<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>2025 Australia's Top 10 ETFs - Financial Analysis</title>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/Chart.js/3.9.1/chart.min.js"></script>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #0f172a 0%, #1e293b 50%, #0f172a 100%);
            color: #f1f5f9;
            min-height: 100vh;
            padding: 20px;
        }
        
        .container {
            max-width: 1400px;
            margin: 0 auto;
        }
        
        .header {
            text-align: center;
            margin-bottom: 40px;
            padding: 30px;
            background: linear-gradient(135deg, rgba(30, 41, 59, 0.8) 0%, rgba(51, 65, 85, 0.8) 100%);
            border-radius: 15px;
            border: 2px solid rgba(59, 130, 246, 0.3);
        }
        
        .header h1 {
            font-size: 2.5em;
            margin-bottom: 10px;
            color: #60a5fa;
        }
        
        .header p {
            font-size: 1.1em;
            color: #cbd5e1;
        }
        
        .tabs {
            display: flex;
            gap: 10px;
            margin-bottom: 30px;
            flex-wrap: wrap;
        }
        
        .tab-btn {
            padding: 12px 24px;
            border: 2px solid #475569;
            background: #1e293b;
            color: #94a3b8;
            cursor: pointer;
            border-radius: 8px;
            font-size: 1em;
            transition: all 0.3s;
        }
        
        .tab-btn.active {
            background: #3b82f6;
            border-color: #3b82f6;
            color: white;
            box-shadow: 0 0 20px rgba(59, 130, 246, 0.5);
        }
        
        .tab-btn:hover {
            border-color: #3b82f6;
            color: #60a5fa;
        }
        
        .tab-content {
            display: none;
            animation: fadeIn 0.3s ease-in;
        }
        
        .tab-content.active {
            display: block;
        }
        
        @keyframes fadeIn {
            from { opacity: 0; }
            to { opacity: 1; }
        }
        
        .grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(350px, 1fr));
            gap: 20px;
            margin-bottom: 30px;
        }
        
        .card {
            background: linear-gradient(135deg, rgba(30, 41, 59, 0.9) 0%, rgba(51, 65, 85, 0.9) 100%);
            border: 2px solid #334155;
            border-radius: 12px;
            padding: 25px;
            transition: all 0.3s;
        }
        
        .card:hover {
            border-color: #3b82f6;
            box-shadow: 0 10px 40px rgba(59, 130, 246, 0.2);
            transform: translateY(-5px);
        }
        
        .card-title {
            font-size: 1.3em;
            font-weight: bold;
            color: #60a5fa;
            margin-bottom: 15px;
            display: flex;
            align-items: center;
            gap: 10px;
        }
        
        .ticker {
            background: #3b82f6;
            padding: 4px 12px;
            border-radius: 20px;
            font-size: 0.8em;
            font-weight: bold;
        }
        
        .metric {
            margin: 12px 0;
            padding: 10px;
            background: rgba(148, 163, 184, 0.1);
            border-left: 3px solid #3b82f6;
            border-radius: 4px;
        }
        
        .metric-label {
            color: #cbd5e1;
            font-size: 0.9em;
        }
        
        .metric-value {
            font-size: 1.3em;
            font-weight: bold;
            color: #4ade80;
            margin-top: 5px;
        }
        
        .chart-container {
            background: rgba(30, 41, 59, 0.9);
            border: 2px solid #334155;
            border-radius: 12px;
            padding: 25px;
            margin-bottom: 30px;
            position: relative;
            height: 500px;
        }
        
        .table-container {
            background: rgba(30, 41, 59, 0.9);
            border: 2px solid #334155;
            border-radius: 12px;
            padding: 25px;
            overflow-x: auto;
            margin-bottom: 30px;
        }
        
        table {
            width: 100%;
            border-collapse: collapse;
        }
        
        th {
            background: linear-gradient(135deg, rgba(59, 130, 246, 0.2) 0%, rgba(51, 65, 85, 0.5) 100%);
            border: 1px solid #475569;
            padding: 15px;
            text-align: left;
            color: #60a5fa;
            font-weight: bold;
        }
        
        td {
            border: 1px solid #475569;
            padding: 12px 15px;
            color: #cbd5e1;
        }
        
        tr:hover {
            background: rgba(59, 130, 246, 0.1);
        }
        
        .positive {
            color: #4ade80;
        }
        
        .negative {
            color: #f87171;
        }
        
        .regression-info {
            background: linear-gradient(135deg, rgba(59, 130, 246, 0.1) 0%, rgba(34, 197, 94, 0.1) 100%);
            border: 2px solid #22c55e;
            border-radius: 12px;
            padding: 20px;
            margin-bottom: 30px;
        }
        
        .regression-info h3 {
            color: #22c55e;
            margin-bottom: 15px;
        }
        
        .regression-metric {
            display: inline-block;
            margin-right: 30px;
            margin-bottom: 10px;
            padding: 10px;
            background: rgba(59, 130, 246, 0.1);
            border-radius: 8px;
        }
        
        .regression-metric span {
            color: #cbd5e1;
        }
        
        .regression-value {
            color: #4ade80;
            font-weight: bold;
            font-size: 1.1em;
        }
        
        .etf-selector {
            background: rgba(30, 41, 59, 0.9);
            border: 2px solid #334155;
            border-radius: 12px;
            padding: 25px;
            margin-bottom: 30px;
        }
        
        .etf-selector label {
            color: #cbd5e1;
            font-size: 1.1em;
            margin-right: 15px;
        }
        
        .etf-selector select {
            padding: 10px;
            border-radius: 8px;
            background: #1e293b;
            color: white;
            border: 2px solid #475569;
            min-width: 300px;
            min-height: 120px;
            font-size: 1em;
        }
        
        .etf-selector select option {
            background: #1e293b;
            color: white;
            padding: 8px;
        }
        
        .helper-text {
            color: #94a3b8;
            margin-top: 10px;
            font-size: 0.9em;
        }
        
        .error-message {
            background: #dc2626;
            color: white;
            padding: 15px;
            border-radius: 8px;
            margin: 20px 0;
            border-left: 4px solid #991b1b;
        }
        
        .success-message {
            background: #059669;
            color: white;
            padding: 15px;
            border-radius: 8px;
            margin: 20px 0;
            border-left: 4px solid #065f46;
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>2025 Australia's 10 Largest ETFs</h1>
            <p>Comprehensive Financial Analysis with Regression Trend Analysis</p>
            <p style="margin-top: 20px; font-size: 0.9em; color: #94a3b8;">
                Published on <strong>recchiereport.com</strong> | Author: <strong>Baeley Recchia</strong>
            </p>
        </div>
        
        <div class="tabs">
            <button class="tab-btn active" onclick="updateTab(event, 'overview')">📊 Overview</button>
            <button class="tab-btn" onclick="updateTab(event, 'detailed')">📈 Detailed Analysis</button>
            <button class="tab-btn" onclick="updateTab(event, 'regression')">📉 Regression Analysis</button>
            <button class="tab-btn" onclick="updateTab(event, 'comparison')">⚖️ Returns Comparison</button>
            <button class="tab-btn" onclick="updateTab(event, 'performance')">💹 Market Share</button>
        </div>
        
        <!-- Overview Tab -->
        <div id="overview" class="tab-content active">
            <div class="grid" id="overviewGrid"></div>
        </div>
        
        <!-- Detailed Tab -->
        <div id="detailed" class="tab-content">
            <div class="table-container">
                <table id="detailedTable">
                    <thead>
                        <tr>
                            <th>ETF</th>
                            <th>Ticker</th>
                            <th>AUM (AUD B)</th>
                            <th>Fee (%)</th>
                            <th>5Y Return (%)</th>
                            <th>1Y Return (%)</th>
                            <th>Div Yield (%)</th>
                        </tr>
                    </thead>
                    <tbody id="detailedBody"></tbody>
                </table>
            </div>
        </div>
        
        <!-- Regression Tab -->
        <div id="regression" class="tab-content">
            <div class="etf-selector">
                <label for="etfSelector">Select ETF(s) for Regression Analysis:</label>
                <select id="etfSelector" multiple onchange="updateRegressionView()">
                </select>
                <p class="helper-text">Hold Ctrl/Cmd to select multiple ETFs for comparative view</p>
            </div>
            <div id="regressionContent"></div>
            <div class="chart-container">
                <canvas id="regressionChart"></canvas>
            </div>
        </div>
        
        <!-- Comparison Tab -->
        <div id="comparison" class="tab-content">
            <div class="chart-container">
                <canvas id="comparisonChart"></canvas>
            </div>
        </div>
        
        <!-- Performance Tab -->
        <div id="performance" class="tab-content">
            <div class="chart-container">
                <canvas id="performanceChart"></canvas>
            </div>
        </div>
    </div>

    <script>
        // Financial Analysis Engine - Custom Implementation
        // Recchia Report ETF Analysis System
        
        const etfDatabase = {
            vas: {n:"Vanguard Australian Shares",t:"VAS",a:22.49,f:.07,r5:12.86,r1:11.5,d:3.2,y:1997,h:[.5,1.2,2.8,5.5,9.2,12.4,15.8,18.2,20.1,22.49]},
            vgs: {n:"Vanguard International Shares",t:"VGS",a:13.16,f:.18,r5:14.2,r1:13.8,d:1.8,y:2006,h:[.3,.8,1.5,3.2,5.8,8.1,10.2,11.8,12.5,13.16]},
            ndq: {n:"BetaShares Nasdaq-100",t:"NDQ",a:7.71,f:.48,r5:18.73,r1:25.3,d:.3,y:2011,h:[.1,.2,.5,1.2,2.5,4.1,5.8,6.5,7.1,7.71]},
            aaa: {n:"BetaShares High Interest Cash",t:"AAA",a:4.49,f:.18,r5:2.8,r1:4.25,d:4.1,y:2009,h:[.2,.4,.8,1.5,2.3,3.1,3.8,4.1,4.3,4.49]},
            iaf: {n:"iShares Core Composite Bond",t:"IAF",a:3.50,f:.10,r5:3.2,r1:2.1,d:2.87,y:2009,h:[.15,.35,.7,1.4,2.1,2.6,3.0,3.2,3.4,3.50]},
            v200: {n:"Vanguard ASX 200 Index",t:"VAS200",a:3.25,f:.09,r5:12.9,r1:11.8,d:3.4,y:2010,h:[.1,.25,.6,1.3,2.0,2.5,2.8,3.0,3.15,3.25]},
            ivv: {n:"iShares S&P 500",t:"IVV",a:3.10,f:.09,r5:16.5,r1:21.2,d:1.4,y:2007,h:[.2,.5,1.1,1.8,2.2,2.5,2.7,2.85,2.95,3.10]},
            wire: {n:"BetaShares Global Copper",t:"WIRE",a:2.85,f:.65,r5:8.1,r1:6.5,d:2.1,y:2010,h:[.05,.15,.4,.85,1.3,1.7,2.1,2.4,2.65,2.85]},
            gold: {n:"Global X Physical Gold",t:"GOLD",a:2.60,f:.40,r5:11.2,r1:28.5,d:0,y:2016,h:[.05,.15,.35,.65,1.2,1.6,1.95,2.25,2.45,2.60]},
            qual: {n:"Vanguard FTSE Quality",t:"QUAL",a:2.45,f:.30,r5:13.5,r1:15.2,d:1.9,y:2015,h:[.03,.08,.2,.5,.9,1.4,1.8,2.1,2.3,2.45]}
        };

        let activeCharts = {regression:null,comparison:null,performance:null};
        const colorPalette = ['#3b82f6','#60a5fa','#22c55e','#84cc16','#f59e0b','#ef4444','#8b5cf6','#ec4899','#14b8a6','#f97316'];

        function expandETFData() {
            return Object.keys(etfDatabase).map(key => {
                const d = etfDatabase[key];
                return {name:d.n,ticker:d.t,aum:d.a,fee:d.f,return5y:d.r5,return1y:d.r1,divYield:d.d,inception:d.y,historicalAUM:d.h};
            });
        }

        const etfData = expandETFData();

        function calcLinearTrend(values) {
            const n = values.length;
            if(n<2) return null;
            let sx=0,sy=0,sxy=0,sx2=0;
            for(let i=0;i<n;i++) {sx+=i;sy+=values[i];sxy+=i*values[i];sx2+=i*i;}
            const m = (n*sxy-sx*sy)/(n*sx2-sx*sx);
            const b = (sy-m*sx)/n;
            const trend = values.map((_,i)=>b+m*i);
            const r2 = calcRSquared(values,trend);
            return {slope:m,intercept:b,trendLine:trend,r2:r2};
        }

        function calcRSquared(actual,predicted) {
            const mean = actual.reduce((a,b)=>a+b)/actual.length;
            const sst = actual.reduce((s,v)=>s+Math.pow(v-mean,2),0);
            const ssr = actual.reduce((s,v,i)=>s+Math.pow(v-predicted[i],2),0);
            return 1-(ssr/sst);
        }

        function displayOverviewCards() {
            const container = document.getElementById('overviewGrid');
            container.innerHTML = etfData.map(e => `
                <div class="card">
                    <div class="card-title">${e.name}<span class="ticker">${e.ticker}</span></div>
                    <div class="metric"><div class="metric-label">Assets Under Management</div><div class="metric-value">${e.aum.toFixed(2)}B</div></div>
                    <div class="metric"><div class="metric-label">Management Fee</div><div class="metric-value">${e.fee.toFixed(2)}%</div></div>
                    <div class="metric"><div class="metric-label">5-Year Return</div><div class="metric-value positive">${e.return5y.toFixed(2)}%</div></div>
                    <div class="metric"><div class="metric-label">1-Year Return</div><div class="metric-value positive">${e.return1y.toFixed(2)}%</div></div>
                    <div class="metric"><div class="metric-label">Dividend Yield</div><div class="metric-value">${e.divYield.toFixed(2)}%</div></div>
                </div>
            `).join('');
        }

        function buildDetailTable() {
            const tbody = document.getElementById('detailedBody');
            tbody.innerHTML = etfData.map(e => `
                <tr>
                    <td><strong>${e.name}</strong></td>
                    <td><span class="ticker">${e.ticker}</span></td>
                    <td>${e.aum.toFixed(2)}</td>
                    <td>${e.fee.toFixed(2)}%</td>
                    <td class="positive">${e.return5y.toFixed(2)}%</td>
                    <td class="positive">${e.return1y.toFixed(2)}%</td>
                    <td>${e.divYield.toFixed(2)}%</td>
                </tr>
            `).join('');
        }

        function updateTab(evt,tabId) {
            try {
                document.querySelectorAll('.tab-content').forEach(el=>el.classList.remove('active'));
                document.querySelectorAll('.tab-btn').forEach(el=>el.classList.remove('active'));
                document.getElementById(tabId).classList.add('active');
                evt.target.classList.add('active');
                setTimeout(()=>{
                    if(tabId==='regression') updateRegressionView();
                    if(tabId==='comparison') plotComparison();
                    if(tabId==='performance') plotMarketShare();
                },150);
            } catch(e){console.error('Tab error:',e);}
        }

        function updateRegressionView() {
            try {
                const selected = Array.from(document.getElementById('etfSelector').selectedOptions).map(o=>o.value);
                if(selected.length===0) {
                    document.getElementById('regressionContent').innerHTML='<div class="error-message">Select at least one ETF for analysis</div>';
                    return;
                }
                const chosen = etfData.filter(e=>selected.includes(e.ticker));
                let html = '<div class="regression-info"><h3>Regression Trend Analysis</h3>';
                const datasets = [];
                chosen.forEach((etf,idx)=>{
                    const trend = calcLinearTrend(etf.historicalAUM);
                    if(trend) {
                        html+=`<div style="display:inline-block;margin-right:40px;margin-bottom:15px;padding:15px;background:rgba(59,130,246,0.1);border-radius:8px;border-left:4px solid ${colorPalette[idx]};"><div style="color:${colorPalette[idx]};font-weight:bold;margin-bottom:10px;">${etf.ticker} - ${etf.name}</div><div class="regression-metric"><span>Growth Slope (B/yr):</span><span class="regression-value">${trend.slope.toFixed(3)}</span></div><div class="regression-metric"><span>Starting (B):</span><span class="regression-value">${trend.intercept.toFixed(3)}</span></div><div class="regression-metric"><span>R² Score:</span><span class="regression-value">${trend.r2.toFixed(4)}</span></div><div class="regression-metric"><span>Consistency:</span><span class="regression-value">${(trend.r2*100).toFixed(1)}%</span></div></div>`;
                        datasets.push({label:`${etf.ticker} (Actual)`,data:etf.historicalAUM.map((v,i)=>({x:i,y:v})),borderColor:colorPalette[idx],backgroundColor:colorPalette[idx]+'50',radius:5,borderWidth:2});
                        datasets.push({label:`${etf.ticker} (Trend)`,data:trend.trendLine.map((v,i)=>({x:i,y:v})),borderColor:colorPalette[idx],borderWidth:3,fill:false,borderDash:[5,5],type:'line',radius:0});
                    }
                });
                html+='</div>';
                document.getElementById('regressionContent').innerHTML=html;
                if(activeCharts.regression) activeCharts.regression.destroy();
                activeCharts.regression = new Chart(document.getElementById('regressionChart').getContext('2d'),{
                    type:'scatter',data:{datasets:datasets},options:{responsive:true,maintainAspectRatio:false,plugins:{legend:{labels:{color:'#cbd5e1'}},title:{display:true,text:'AUM Growth Trend Analysis',color:'#cbd5e1',font:{size:16}}},scales:{x:{title:{display:true,text:'Years',color:'#cbd5e1'},ticks:{color:'#94a3b8'}},y:{title:{display:true,text:'AUM (B)',color:'#cbd5e1'},ticks:{color:'#94a3b8'}}}}
                });
            }catch(e){console.error('Regression error:',e);}
        }

        function plotComparison() {
            try {
                if(activeCharts.comparison) activeCharts.comparison.destroy();
                activeCharts.comparison = new Chart(document.getElementById('comparisonChart').getContext('2d'),{
                    type:'bar',data:{labels:etfData.map(e=>e.ticker),datasets:[{label:'5Y Return (%)',data:etfData.map(e=>e.return5y),backgroundColor:'rgba(59,130,246,0.7)',borderColor:'#3b82f6',borderWidth:2},{label:'1Y Return (%)',data:etfData.map(e=>e.return1y),backgroundColor:'rgba(34,197,94,0.7)',borderColor:'#22c55e',borderWidth:2}]},options:{responsive:true,maintainAspectRatio:false,plugins:{legend:{labels:{color:'#cbd5e1'}},title:{display:true,text:'Returns Comparison Analysis',color:'#cbd5e1'}},scales:{y:{ticks:{color:'#94a3b8'}},x:{ticks:{color:'#94a3b8'}}}}
                });
            }catch(e){console.error('Comparison error:',e);}
        }

        function plotMarketShare() {
            try {
                const total = etfData.reduce((s,e)=>s+e.aum,0);
                const pct = etfData.map(e=>(e.aum/total)*100);
                if(activeCharts.performance) activeCharts.performance.destroy();
                activeCharts.performance = new Chart(document.getElementById('performanceChart').getContext('2d'),{
                    type:'doughnut',data:{labels:etfData.map((e,i)=>`${e.ticker} ${pct[i].toFixed(1)}%`),datasets:[{data:etfData.map(e=>e.aum),backgroundColor:colorPalette,borderColor:'#1e293b',borderWidth:2}]},options:{responsive:true,maintainAspectRatio:false,plugins:{legend:{labels:{color:'#cbd5e1'},position:'right'},title:{display:true,text:`Market Share Distribution - Total AUM: ${total.toFixed(2)}B`,color:'#cbd5e1',font:{size:14}},tooltip:{callbacks:{label:function(c){const i=c.dataIndex;return`${etfData[i].name}: ${etfData[i].aum.toFixed(2)}B (${pct[i].toFixed(1)}%)`;}}}}}
                });
            }catch(e){console.error('Performance error:',e);}
        }

        document.addEventListener('DOMContentLoaded',function(){
            try {
                displayOverviewCards();
                buildDetailTable();
                const sel = document.getElementById('etfSelector');
                etfData.forEach(e=>{const opt=document.createElement('option');opt.value=e.ticker;opt.textContent=`${e.ticker} - ${e.name}`;sel.appendChild(opt);});
                console.log('System initialized');
            }catch(e){console.error('Init error:',e);}
        });
    </script>
                            }
                        }
                    }
                });
            } catch (error) {
                console.error('Regression chart error:', error);
            }
        }

        // Render Comparison Chart
        function renderComparisonChart() {
            try {
                const ctx = document.getElementById('comparisonChart').getContext('2d');
                
                if (comparisonChartInstance) {
                    comparisonChartInstance.destroy();
                }

                comparisonChartInstance = new Chart(ctx, {
                    type: 'bar',
                    data: {
                        labels: etfData.map(e => e.ticker),
                        datasets: [
                            {
                                label: '5-Year Return (%)',
                                data: etfData.map(e => e.return5y),
                                backgroundColor: 'rgba(59, 130, 246, 0.7)',
                                borderColor: '#3b82f6',
                                borderWidth: 2
                            },
                            {
                                label: '1-Year Return (%)',
                                data: etfData.map(e => e.return1y),
                                backgroundColor: 'rgba(34, 197, 94, 0.7)',
                                borderColor: '#22c55e',
                                borderWidth: 2
                            }
                        ]
                    },
                    options: {
                        responsive: true,
                        maintainAspectRatio: false,
                        plugins: {
                            legend: { labels: { color: '#cbd5e1' } },
                            title: { display: true, text: 'Returns Comparison - Top 10 Australian ETFs', color: '#cbd5e1' }
                        },
                        scales: {
                            y: { ticks: { color: '#94a3b8' } },
                            x: { ticks: { color: '#94a3b8' } }
                        }
                    }
                });
            } catch (error) {
                console.error('Comparison chart error:', error);
            }
        }

        // Render Performance Chart
        function renderPerformanceChart() {
            try {
                const ctx = document.getElementById('performanceChart').getContext('2d');
                
                const totalAUM = etfData.reduce((sum, e) => sum + e.aum, 0);
                const percentages = etfData.map(e => ((e.aum / totalAUM) * 100));
                
                if (performanceChartInstance) {
                    performanceChartInstance.destroy();
                }

                performanceChartInstance = new Chart(ctx, {
                    type: 'doughnut',
                    data: {
                        labels: etfData.map((e, i) => `${e.ticker} ${percentages[i].toFixed(1)}%`),
                        datasets: [{
                            data: etfData.map(e => e.aum),
                            backgroundColor: [
                                '#3b82f6', '#60a5fa', '#22c55e', '#84cc16', '#f59e0b',
                                '#ef4444', '#8b5cf6', '#ec4899', '#14b8a6', '#f97316'
                            ],
                            borderColor: '#1e293b',
                            borderWidth: 2
                        }]
                    },
                    options: {
                        responsive: true,
                        maintainAspectRatio: false,
                        plugins: {
                            legend: { 
                                labels: { color: '#cbd5e1' }, 
                                position: 'right'
                            },
                            title: { 
                                display: true, 
                                text: `Market Share Distribution by AUM - Total AUM: ${totalAUM.toFixed(2)}B (Top 10 Australian ETFs)`,
                                color: '#cbd5e1',
                                font: { size: 14 }
                            },
                            tooltip: {
                                callbacks: {
                                    label: function(context) {
                                        const idx = context.dataIndex;
                                        const etf = etfData[idx];
                                        return `${etf.name}: ${etf.aum.toFixed(2)}B (${percentages[idx].toFixed(1)}%)`;
                                    }
                                }
                            }
                        }
                    }
                });
            } catch (error) {
                console.error('Performance chart error:', error);
            }
        }

        // Initialize all elements
        function init() {
            try {
                renderOverview();
                renderDetailedTable();
                
                const selector = document.getElementById('etfSelector');
                etfData.forEach(etf => {
                    const option = document.createElement('option');
                    option.value = etf.ticker;
                    option.textContent = `${etf.ticker} - ${etf.name}`;
                    selector.appendChild(option);
                });

                console.log('✅ All systems initialized successfully');
            } catch (error) {
                console.error('Initialization error:', error);
            }
        }

        // Run initialization on page load
        document.addEventListener('DOMContentLoaded', init);
    </script>
</body>
</html>
