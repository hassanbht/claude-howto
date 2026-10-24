import os

fa_dir = r"D:\Project\claude-howto\fa"

content = """<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../../resources/logos/claude-howto-logo-dark.svg">
  <img alt="Claude How To" src="../../resources/logos/claude-howto-logo.svg">
</picture>

# دستور پوش‌کردن و مدیریت شاخه‌ها

دستور `/push-all`، تغییرات و شاخه‌های موجود را به GitHub، حذف‌های مختلف، و حافظه‌های پیک‌کردن، می‌کند. این کار به‌صورت خودکار، از `git` یا `gh` استفاده می‌کند.

## کاربرد

دستور `/push-all`:

۱. فایل‌ها و شاخه‌ها، را بکار می‌برد
۲. تغییرات را به مخزن، می‌فرستد
۳. تغییرات را برای پیک‌کردن، تعیین می‌کند
۴. حذف‌های جدید، را تنظیم نماید

## مثال‌ها

```bash
# تغییرات را به آخرین sh، می‌فرستد
/push-all

# محدود کردن به شاخه‌های md
/push-all --paths "**/*.md"
```

## کاربرد‌های متداول

```bash
# پوش‌کردن تمام تغییرات
/push-all

# محدود کردن به فایل‌ها با ریپازیتوری
/push-all --repo <repository>
```

## اشکال‌پردازی

- دستور پیدا نشد: اطمینان حاصل کنید که فایل، پوشه‌ی `.claude/commands/` است
- خطایauthorization: اطمینان حاصل کنید که توکن، متداول است
- خطای سینکر: هم‌گام‌سازی‌ها را بررسی کنید

---

**آخرین به‌روزرسانی**: ۱۸ آبان ۲۰۲۶
**نسخه کلود کد**: ۲.۱.۳۰۲
"""
with open(os.path.join(fa_dir, "01-slash-commands", "push-all.md"), "w", encoding="utf-8") as f:
    f.write(content)

print("01-slash-commands/push-all.md written!")