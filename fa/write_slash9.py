import os

fa_dir = r"D:\Project\claude-howto\fa"

content = """<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../../resources/logos/claude-howto-logo-dark.svg">
  <img alt="Claude How To" src="../../resources/logos/claude-howto-logo.svg">
</picture>

# دستور گسترش و تنظیم تست‌ها

دستور `/unit-test-expand`، پیک‌کردن‌ها، و تنظیم، برای کشف و توسعه‌ی تست‌های واحد، مخصوص، پیک‌کردن‌ها، را مدیریت می‌کند. این دستور، از API‌های گیت، گیت‌چپی، و ریپازیتوری‌ها، استفاده می‌کند.

## چیستی

دستور `/unit-test-expand`:

۱. فایل‌ها و اسکریپت‌های تست، را شناسایی می‌کند
۲. فایل‌ها، به‌سختی، و پیک‌کردن‌ها را تا حد امکان، به‌روزرسانی می‌کند
۳. می‌تواند، پیک‌کردن‌های تکراری و شاخص‌ها، پاک‌سازی کند

## مثال‌ها

### مثال ۱: گسترش تست‌ها

```bash
# گسترش تست‌ها
/unit-test-expand

# محدود کردن به فایل‌ها
/unit-test-expand --paths "**/*.test.js"
```

### مثال ۲: چک‌لیست تست‌ها

```bash
# چک‌لیست
/unit-test-expand --check
```

## مراحل

۱. فرآیند، فایل‌ها و پیک‌کردن‌ها را شناسایی می‌کند
۲. می‌خواند و می‌سازد
۳. کارها را به‌جای، تنظیم می‌کند
۴. فایل‌ها، را در آپ‌سارکر، می‌گذارد

## اشکال‌پردازی

- دستور نا‌موجود: فایل‌ها باید در پوشه‌ی `.claude/commands/` قرار داشته باشند
- خطای authorization: اطمینان حاصل کنید که توکن‌های GitHub، صحیح هستند
- خطای پیک‌کردن: هم‌گام‌سازی‌ها را بررسی کنید

---

**آخرین به‌روزرسانی**: ۱۸ آبان ۲۰۲۶
**نسخه کلود کد**: ۲.۱.۳۰۲
"""
with open(os.path.join(fa_dir, "01-slash-commands", "unit-test-expand.md"), "w", encoding="utf-8") as f:
    f.write(content)

print("01-slash-commands/unit-test-expand.md written!")