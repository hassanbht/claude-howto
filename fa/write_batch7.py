import os

fa_dir = r"D:\Project\claude-howto\fa"

# File: 01-slash-commands/generate-api-docs.md
content = """---
description: تولید مستندات کامل API از کد منبع
---

# تولیدکنندهٔ مستندات API

برای تولید مستندات API مراحل زیر را دنبال کنید:

1. اسکن کردن تمام فایل‌ها در `/src/api/`
2. استخراج امضای توابع و نظرات JSDoc
3. سازماندهی بر اساس نقطه پایگاه/ماژول
4. تولید Markdown همراه با مثال‌ها
5. اضافه کردن Schema درخواست/پاسخ
6. اضافه کردن مستندات خطا

فرمت خروجی:
- خروجی به صورت فایل Markdown در `/docs/api.md`
- اضافه کردن مثال curl برای تمام نقاط پایگاه
- اضافه کردن نوع‌های TypeScript
"""

with open(os.path.join(fa_dir, "01-slash-commands", "generate-api-docs.md"), "w", encoding="utf-8") as f:
    f.write(content)

# File: 01-slash-commands/unit-test-expand.md
content = """---
name: unit-test-expand
description: افزایش پوشش تست با پوشش شاخه‌های بدون تست و موارد مرزی
---

# گسترش تست واحد

بر اساس چارچوب تست پروژه، تست‌های واحد موجود را گسترش دهید:

1. **تحلیل پوشش**: گزارش پوشش را اجرا کنید، شاخه‌های بدون تست، موارد مرزی و مناطق با پوشش پایین را یافته‌اید
2. **شناسایی فاصلة**: شاخه‌های منطقی، مسیرهای خطا، شرایط مرزی، ورودی خالی/نال را در کد بررسی کنید
3. **نوشتن تست**، از چارچوب موجود پروژه استفاده کنید:
   - Jest/Vitest/Mocha (جاوااسکریپت/تایپ‌اسکریپت)
   - pytest/unittest (پایتون)
   - Go testing/testify (گ/widgets)
   - چارچوب تست Rust (Rust)
4. **دست یابی به سناریوهای خاص**:
   - مدیریت خطا و استثناها
   - مقادیر مرزی (حداقل/حداکثر، نال، ورودی خالی)
   - سناریوهای لبه و extrema
   - تغییر وضعیت و اثر جانبی
5. **تأیید بهبود**: دوباره گزارش پوشش را اجرا کنید، تضمین کنید که بهبود قابل اندازه‌گیری وجود دارد

فقط بلوک‌های کد تست جدید را نمایش دهید. به الگوهای و عرف نام‌گذاری تست‌های موجود پیروی کنید.
"""

with open(os.path.join(fa_dir, "01-slash-commands", "unit-test-expand.md"), "w", encoding="utf-8") as f:
    f.write(content)

print("generate-api-docs.md and unit-test-expand.md written!")