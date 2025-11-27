from flask import Flask, render_template_string ,render_template
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

app = Flask(__name__)

gms_3pl_planning = "https://docs.google.com/spreadsheets/d/1T-m_5qRCIr2nBdPUiF-u8_Ph0bX2KACsU5_UAC1oVKk/edit?gid=0#gid=0"

TEMPLATE = r"""
<!DOCTYPE html>
<html lang="zh-Hant">
<head>
    <meta charset="UTF-8">
    <title>測試流程工具頁</title>
    <!-- Bootstrap CDN，純前端用，不影響你後續改程式 -->
    <link
      href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css"
      rel="stylesheet"
      integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH"
      crossorigin="anonymous"
    >
    <style>
        body {
            background-color: #0f172a; /* 深色底 */
            color: #e5e7eb;
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
        }
        .container-main {
            max-width: 1100px;
            margin-top: 40px;
            margin-bottom: 40px;
        }
        .card {
            background: #020617;
            border-radius: 18px;
            border: 1px solid #1f2937;
            box-shadow: 0 22px 45px rgba(15,23,42,.8);
        }
        .nav-pills .nav-link {
            border-radius: 999px;
            color: #9ca3af;
        }
        .nav-pills .nav-link.active {
            background: linear-gradient(135deg, #22c55e, #0ea5e9);
            color: #0b1120;
            font-weight: 600;
        }
        .tab-pane {
            padding-top: 20px;
        }
        .tab-title {
            font-size: 1.25rem;
            font-weight: 600;
            margin-bottom: 10px;
        }
        .tab-subtitle {
            font-size: 0.95rem;
            color: #9ca3af;
            margin-bottom: 18px;
        }
        .code-block {
            background: #020617;
            border-radius: 12px;
            padding: 14px 16px;
            font-family: "JetBrains Mono", "Fira Code", monospace;
            font-size: 0.85rem;
            border: 1px solid #1f2937;
            color: #e5e7eb;
            white-space: pre-wrap;
        }
        a, a:hover {
            color: #22c55e;
        }
        .badge-tag {
            background-color: #1d283a;
            color: #9ca3af;
            border-radius: 999px;
            padding: 4px 10px;
            font-size: 0.75rem;
            margin-right: 4px;
        }
        
        .beauty-btn {
            padding: 6px 16px;
            background: transparent;                 
            color: #e5e7eb;                          
            border: 1px solid #22c1c3;               
            border-radius: 999px;                   
            cursor: pointer;
            font-size: 13px;
            font-weight: 500;
            display: inline-flex;
            align-items: center;
            justify-content: center;
            gap: 6px;
            margin-top: 16px;                        
            transition: background 0.18s ease, 
                        color 0.18s ease, 
                        box-shadow 0.18s ease, 
                        transform 0.18s ease;
        }
        
        .beauty-btn:hover {
            background: rgba(34, 193, 195, 0.15);    
            box-shadow: 0 0 0 1px rgba(34,193,195,0.4);
            transform: translateY(-1px);
        }
        
        .beauty-btn:active {
            transform: translateY(0);
            background: rgba(34, 193, 195, 0.25);
        }

        
    </style>
</head>
<body>
<div class="container container-main">
    <div class="card p-4 p-md-5">
        <div class="d-flex flex-column flex-md-row justify-content-between align-items-md-center mb-4">
            <div>
                <h1 class="h3 mb-1" style="color:#e5e7eb;">3PL Google XTS 測試流程</h1>
                <div style="color:#9ca3af; font-size:1.2rem;">
                    注意事項<br>
                    <a href="https://docs.google.com/spreadsheets/d/1T-m_5qRCIr2nBdPUiF-u8_Ph0bX2KACsU5_UAC1oVKk/edit?gid=0#gid=0">3PL Planning </a>

                </div>
            </div>
            <div class="mt-3 mt-md-0">
                <span class="badge-tag">Flash</span>
                <span class="badge-tag">CTS / GTS</span>
                <span class="badge-tag">Retry</span>
                <span class="badge-tag">Waiver</span>
            </div>
        </div>

        <!-- Tabs -->
        <ul class="nav nav-pills mb-3" id="main-tabs" role="tablist">
            <li class="nav-item" role="presentation">
                <button class="nav-link active"
                        id="flash-tab"
                        data-bs-toggle="pill"
                        data-bs-target="#flash"
                        type="button"
                        role="tab"
                        aria-controls="flash"
                        aria-selected="true">
                    Flash
                </button>
            </li>
            <li class="nav-item" role="presentation">
                <button class="nav-link"
                        id="sop-tab"
                        data-bs-toggle="pill"
                        data-bs-target="#sop"
                        type="button"
                        role="tab"
                        aria-controls="sop"
                        aria-selected="false">
                    SOP
                </button>
            </li>
            <li class="nav-item" role="presentation">
                <button class="nav-link"
                        id="ctsv-tab"
                        data-bs-toggle="pill"
                        data-bs-target="#ctsv"
                        type="button"
                        role="tab"
                        aria-controls="ctsv"
                        aria-selected="false">
                    CTSV / GTSI
                </button>
            </li>
            <li class="nav-item" role="presentation">
                <button class="nav-link"
                        id="retry-tab"
                        data-bs-toggle="pill"
                        data-bs-target="#retry"
                        type="button"
                        role="tab"
                        aria-controls="retry"
                        aria-selected="false">
                    Retry 方法
                </button>
            </li>
            <li class="nav-item" role="presentation">
                <button class="nav-link"
                        id="waiver-tab"
                        data-bs-toggle="pill"
                        data-bs-target="#waiver"
                        type="button"
                        role="tab"
                        aria-controls="waiver"
                        aria-selected="false">
                    Wavier
                </button>
            </li>
        </ul>

        <!-- Tab contents -->
        <div class="tab-content" id="main-tabs-content">
            <!-- Flash -->
            <div class="tab-pane fade show active" id="flash" role="tabpanel" aria-labelledby="flash-tab">
                <div class="tab-title">Flash 流程</div>
                <div class="tab-subtitle">
                    這裡之後可以整理你真正的 flash 指令、log 存放路徑、常見錯誤處理。現在先放一個簡單骨架。
                </div>
                <div class="code-block">
                    @echo off
                    REM 這裡可以放你現在習慣用的 flash batch / shell
                    
                    fastboot devices
                    fastboot flashing unlock
                    
                    REM TODO：之後你可以把實際專案用到的指令貼進來
                </div>
                
                <button  class="beauty-btn" onclick="window.location.href='/flash_image'">
                    Flash Image 介紹
                </button> 
                
            </div>

            <!-- SOP -->
            <div class="tab-pane fade" id="sop" role="tabpanel" aria-labelledby="sop-tab">
                <div class="tab-title">SOP（標準作業流程）</div>
                <div class="tab-subtitle">
                    這一頁可以當作「人看得懂」的版本：步驟拆開、注意事項寫清楚，真正用來丟給新同事或 RD/PM 的。
                </div>
                <ul>
                    <li>Step 1：確認機種、Android 版本、build type（user / userdebug）。</li>
                    <li>Step 2：確認測試項目（CTS / GTS / STS / AACT / MADA...）。</li>
                    <li>Step 3：準備測試環境（網路、SIM、log 工具、CAN / DLT 等）。</li>
                    <li>Step 4：執行測試並紀錄 log 位置。</li>
                    <li>Step 5：整理結果、retry、判斷是否要提 waiver。</li>
                </ul>
                <div style="font-size:0.85rem; color:#9ca3af;">
                    之後你可以把這些條列換成你實際的 SOP，一條一條貼上去就好。
                </div>
                
                <button  class="beauty-btn" onclick="window.location.href='/sop'">
                    測試SOP
                </button> 
                
            </div>

            <!-- CTSV / GTSI -->
            <div class="tab-pane fade" id="ctsv" role="tabpanel" aria-labelledby="ctsv-tab">
                <div class="tab-title">CTSV / GTSI 區塊</div>
                <div class="tab-subtitle">
                    這裡可以放：subplan 命名規則、run / retry 指令、常用 exclude、log 存放位置說明。
                </div>
                <div class="code-block">
                    # CTS 例：跑特定 subplan
                    cts-tradefed run cts \
                      --subplan My_SubPlan \
                      --max-testcase-run-count 1
                    
                    # GTSI / CTSV 例：retry
                    cts-tradefed run cts \
                      --retry 3 \
                      --subplan My_SubPlan
                    
                    # TODO：你之後可以把你真正在用的 command 貼上來
                </div>
            
                
            </div>

            <!-- Retry -->
            <div class="tab-pane fade" id="retry" role="tabpanel" aria-labelledby="retry-tab">
                <div class="tab-title">Retry 方法</div>
                <div class="tab-subtitle">
                    這一頁可以整理：什麼情境用 retry，怎麼決定 retry 次數、怎麼記錄每次 retry 的差異。
                </div>
                <ul>
                    <li>Retry 條件：暫時性環境問題（network、server、lab 狀態不穩）。</li>
                    <li>不建議 retry 的情況：穩定重現的功能 bug、明顯的 device 行為異常。</li>
                    <li>建議紀錄：第幾次 run、環境差異、是否更換 device / port / cable。</li>
                </ul>
                <div class="code-block">
                    # 範例：只 retry previously failed tests
                    cts-tradefed run cts --retry 2
                    
                    # 範例：針對指定模組 retry
                    cts-tradefed run cts --module CtsNetTestCases --retry 2
                </div>
                
                <button  class="beauty-btn" onclick="window.location.href='/retry'">
                    開啟 Retry 方法頁面
                </button> 
                
            </div>

            <!-- Waiver -->
            <div class="tab-pane fade" id="waiver" role="tabpanel" aria-labelledby="waiver-tab">
                <div class="tab-title">Wavier / Waiver 區塊</div>
                <div class="tab-subtitle">
                    這裡之後可以放：什麼情況可以提 waiver、要附哪些證據、跟誰確認、怎麼寫理由比較安全。
                </div>
                <ol>
                    <li>確認：是 Google 既知 issue / Doc mismatch / Spec 例外。</li>
                    <li>蒐集：log、測試環境、重現步驟、對應的 test case ID。</li>
                    <li>內部確認：先跟 RD / PM / 客戶窗口對齊，再對外送審。</li>
                    <li>後續追蹤：記錄 waiver ID、對應 build、下次測試是否沿用。</li>
                </ol>
                <div style="font-size:0.85rem; color:#9ca3af;">
                    你之後可以把公司內部真正在用的 Waiver 模板或連結貼在這裡（例如：JIRA、Confluence、Google Form）。
                </div>
                
                <button  class="beauty-btn" onclick="window.location.href='/waiver'">
                    開啟 Waiver 管理頁
                </button> 
                          
            </div>
        </div>
    </div>
</div>


<script
  src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js"
  integrity="sha384-YvpcrYf0tY3lHB60NNkmXc5s9fDVZLESaAA55NDzOxhy9GkcIdslK1eN7N6jIeHz"
  crossorigin="anonymous"
></script>
</body>
</html>
"""

@app.route("/")
def index():
    return render_template_string(TEMPLATE)

@app.route("/flash_image")
def flash_image():
    return render_template("flash_image.html")

@app.route("/sop")
def sop():
    return render_template("sop.html")

@app.route("/retry")
def retry():
    return render_template("retry.html")

@app.route("/waiver")
def waiver():
    return render_template("waiver.html")

if __name__ == "__main__":
    # 你可以改成 host="0.0.0.0" 讓其他機器也能連
    app.run(debug=True)
