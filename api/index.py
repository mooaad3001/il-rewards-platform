from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse

app = FastAPI()

# الروابط المباشرة للشبكات الإعلانية المعتمدة
MONETAG_LINK = "https://omg10.com/4/11726757"
ADSTERRA_LINK = "https://your-adsterra-direct-link.com"  # استبدل هذا برابط Adsterra الخاص بك
HILLTOP_LINK = "https://idealistic-revenue.com/dhGPCs"

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    html_content = f"""
    <!DOCTYPE html>
    <html lang="he" dir="rtl">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <meta name="monetag" content="39c7e76a70083d023d1e2670edf0f16e">
        <title>IL Rewards - מערכת תגמולים</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                background-color: #f4f4f9;
                text-align: center;
                padding: 40px;
                color: #333;
            }}
            .container {{
                background: white;
                padding: 30px;
                border-radius: 12px;
                box-shadow: 0px 4px 15px rgba(0,0,0,0.1);
                display: inline-block;
                max-width: 450px;
                width: 100%;
            }}
            h1 {{ font-size: 22px; margin-bottom: 10px; color: #111; }}
            p {{ color: #666; font-size: 14px; margin-bottom: 25px; }}
            .btn {{
                display: block;
                width: 100%;
                padding: 14px;
                margin: 12px 0;
                background: #007bff;
                color: white;
                text-decoration: none;
                border-radius: 6px;
                font-size: 16px;
                font-weight: bold;
                box-sizing: border-box;
                transition: background 0.2s;
            }}
            .btn:hover {{ background: #0056b3; }}
            .btn-2 {{ background: #28a745; }}
            .btn-2:hover {{ background: #218838; }}
            .btn-3 {{ background: #ffc107; color: #333; }}
            .btn-3:hover {{ background: #e0a800; }}
        </style>
    </head>
    <body>
        <div class="container">
            <h1>מערכת תגמולים והרווחת בונוסים</h1>
            <p>לחץ על הקישורים أدناه للتفاعل وبدء تجميع الأرباح:</p>
            <a href="{MONETAG_LINK}" class="btn" target="_blank">رابط إعلاني 1 (Monetag)</a>
            <a href="{ADSTERRA_LINK}" class="btn btn-2" target="_blank">رابط إعلاني 2 (Adsterra)</a>
            <a href="{HILLTOP_LINK}" class="btn btn-3" target="_blank">رابط إعلاني 3 (HilltopAds)</a>
        </div>
    </body>
    </html>
    """
    return HTMLResponse(content=html_content)