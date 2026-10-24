import os

fa_dir = r"D:\Project\claude-howto\fa"

content = """

## روش نصب

### نقل و火柴 HTTP (توصیه می‌شود)

```bash
# اتصال پایه HTTP

# HTTP با هدر احراز هویت
```

### الفرقات stdio (مکانی)

```bash
# سرور Node.js محلی

# با متغیرهای محیطی
```

###flix actorsر transmisión SSE (م廃止 شده)

در نسخه‌های قدیمی، ممکن است همچنان روش SSE را ببینید، اما در پیکربندی‌های جدید معمولاً اولویت با HTTP یا stdio است.

### 발バル伝 WebSocket

برای سناریوهایی که نیاز به ارتباط دوقطری real-time دارند، مناسب است.

### توضیحات Windows

در ویندوز هنگام پیکربندی سرور محلی، به شل، متغیرهای محیطی و روش نوشتن مسیر توجه کنید.

### احراز هویت OAuth 2.0

برای سرورهای MCP که از OAuth پشتیبانی می‌کنند، Claude می‌تواند از طریق فرآیند تعاملی یا اعتبارنامه‌های پیش پیکربندی شده احراز هویت کند.
"""

with open(os.path.join(fa_dir, "05-mcp", "README.md"), "a", encoding="utf-8") as f:
    f.write(content)

print("05-mcp/README.md part 2 written!")