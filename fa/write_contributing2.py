import os

fa_dir = r"D:\Project\claude-howto\fa"

content = """

## شروع سریع

### ۱. فورک و کلون

```bash
git clone https://github.com/luongnv89/claude-howto.git
cd claude-howto
```

### ۲. ایجاد شاخه

از نام شاخه‌ای که کار را مشخص کند استفاده کنید:

```bash
git checkout -b add/feature-name
git checkout -b fix/issue-description
git checkout -b docs/improvement-area
```

### ۳. پیکربندی محیط توسعه

هوک‌های pre-commit به صورت محلی و در هرcommit بررسی‌های مشابه CI را اجرا می‌کنند. قبل از پذیرش PR، چهار بررسی زیر باید successes کنند:

**نیازها:**

```bash
# زنجیره ابزار پایتون (uv مدیر بسته این پروژه است)
pip install uv
uv venv
source .venv/bin/activate
uv pip install -r scripts/requirements-dev.txt

# ابزار lint Markdown (Node.js)
npm install -g markdownlint-cli

# نمودارهای Mermaid توسط Pele رندر می‌شوند و نیاز به Node.js >= 20 دارند (نیازی به نصب سراسری هیچ بسته‌ای نیست)
# بررسی نسخه:
node --version

# نصب pre-commit و فعال‌سازی هوک‌ها
uv pip install pre-commit
pre-commit install
```

**تأیید پیکربندی:**

```bash
pre-commit run --all-files
```

در اجرای اول، برای هوک‌های Mermaid Node.js ۲۲ (توسط pre-commit ارائه می‌شود، بنابراین حتی اگر سیستم شما Node.js نداشته باشد نیز اجرا می‌شود) و بسته Pele نسخه 굳ه شده در `scripts/.vendor-cache/pele/` دانلود می‌شود؛ اجراهای بعد می‌توانند آفلاین انجام شوند. هوک‌های Mermaid در حالت سخت اجرا می‌شوند و اگر Pele نتواند اجرا شود، شکست می‌خورند. اگر قبل از اولین دانلود بخواهید آفلاین commit کنید، می‌توانید با `SKIP=mermaid,vietnamese-mermaid,japanese-mermaid` آن‌ها را رد کنید.

در هرcommit، هوک‌های زیر اجرا می‌شوند:

| هوک | بررسی |
|------|----------|
| `markdown-lint` | فرمت و ساختار Markdown |
| `cross-references` | پیوندهای نسبی، لنگرها، بلوک‌های کد |
| `mermaid-syntax` | آیا تمام بلوک‌های ` ```mermaid ` با درستی پارس می‌شوند |
| `link-check` | آیا URLهای خارجی قابل دسترسی هستند |
| `build-epub` | آیا در تغییر `.md` EPUB بدون خطا تولید می‌شود |

## ساختار دایرکتوری

```
├── 01-slash-commands/      # دستورات سریع دستی-trigger شده
├── 02-memory/              # مثال‌های contexte پایدار
├── 03-skills/              # قابلیت‌های قابل استفاده مجدد
├── 04-subagents/           # دستیارهای AI تخصصی
├── 05-mcp/                 # مثال‌های پروتکل مدل محیطی
├── 06-hooks/               # اتوماسیون مدفوع-رویداد
├── 07-plugins/             # مجموعه‌های قابلیت بسته‌بندی شده
├── 08-checkpoints/         # عکسبرداری peril.session
├── 09-advanced-features/   # برنامه‌ریزی، تفکر، وظایف پس‌زمینه
├── 10-cli/                 # مرجع CLI
├── scripts/                # اسکریپت‌های ساخت و ابزار
└── README.md            # راهنمای اصلی
```

## چگونه مثال اضافه کنیم

### اضافه کردن دستور Slash

۱. در `01-slash-commands/` یک فایل `.md` بسازید
۲. شامل موارد زیر باشد:
   - توضیح rõ کاربرد
   - سناریوهای استفاده
   - راهنمای نصب
   - مثال‌های استفاده
   - تکنیک‌های شخصی‌سازی
۳. فایل `01-slash-commands/README.md` را به‌روزرسانی کنید

### اضافه کردن مهارت

۱. در `03-skills/` یک دایرکتوری بسازید
۲. شامل موارد زیر باشد:
   - `SKILL.md` - سند اصلی
   - `scripts/` - در صورت نیاز اسکریپت‌های کمکی
   - `templates/` - قالب‌های پرامپت
   - در README نمونه استفاده
۳. فایل `03-skills/README.md` را به‌روزرسانی کنید

### اضافه کردن Subagent

۱. در `04-subagents/` یک فایل `.md` بسازید
۲. شامل موارد زیر باشد:
   - هدف و قابلیت‌های agent
   - ساختار پرامپت سیستم
   - سناریوهای استفاده مثالی
   - مثال‌های یکپارچگی
۳. فایل `04-subagents/README.md` را به‌روزرسانی کنید

### اضافه کردن MCP

۱. در `05-mcp/` یک فایل `.md` بسازید
۲. شامل موارد زیر باشد:
   - توضیح سرور MCP
   - پیکربندی نمونه‌ای
   - مثال‌های استفاده
۳. فایل `05-mcp/README.md` را به‌روزرسانی کنید

### اضافه کردن هوک

۱. در `06-hooks/` یک فایل `.sh` بسازید
۲. شامل موارد زیر باشد:
   - shebang و توضیحات
   - نظرات منطق روشن
   - مدیریت خطا
   - ملاحظات امنیتی
۳. فایل `06-hooks/README.md` را به‌روزرسانی کنید
"""

with open(os.path.join(fa_dir, "CONTRIBUTING.md"), "a", encoding="utf-8") as f:
    f.write(content)

print("CONTRIBUTING.md part 2 written!")