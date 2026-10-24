import os

fa_dir = r"D:\Project\claude-howto\fa"

# File: .github/pull_request_template.md
with open(os.path.join(fa_dir, ".github", "pull_request_template.md"), "w", encoding="utf-8") as f:
    f.write('''## توضیح
به طور خلاصه بگویید این PR چه کاری انجام می‌دهد.

## نوع تغییرات
- [ ] افزودن مثال یا قالب جدید
- [ ] بهبود مستندات
- [ ] رفع باگ
- [ ] راهنمای ویژگی
- [ ] سایر (لطفاً توضیح دهید)

## issueهای مرتبط
Closes #(issue number)

## تغییرات انجام شده
- تغییر 1
- تغییر 2
- تغییر 3

## نکات مهم برای مرور
چه نکته‌ای برای مرورگران مهم است؟

## فایل‌های تغییر یافته
- `path/to/file1.md`
- `path/to/file2.md`

## تست
چگونه تست کرده‌اید؟
- [ ] در Claude Code به صورت محلی تست شده است
- [ ] نمونه‌ها قابل استفاده تأیید شده‌اند
- [ ] لینک‌ها و ارجاع‌ها بررسی شده‌اند
- [ ] املاء و شفافیت بررسی شده است

## لیست بررسی
- [ ] با ساختار و قوانین پروژه همخوانی دارد
- [ ] شامل مستندات / مثال واضح است
- [ ] کد / مثال قابل کپی مستقیم است
- [ ] تمام لینک‌ها اعتبارسنجی و قابل دسترسی هستند
- [ ] شامل اطلاعات حساسی نیست (کلیدها، توکن‌ها، اعتبارنامه‌ها)
- [ ] READMEهای مرتبط به‌روزرسانی شده‌اند
- [ ] پیام Commit مطابق قالب conventional commit است
- [ ] شامل فایل بزرگ نیست (>1MB)

## اسکرین‌شات یا مثال
در صورت لزوم، محتوایی که این PR افزوده است نشان دهید:
```
[کد نمونه یا مقایسه قبل و بعد]
```

## تغییرات شکننده
آیا این تغییر بر روی محتوا یا رفتارهای موجود تأثیر می‌گذارد؟
- [ ] هیچ تغییر شکننده‌ای نیست
- [ ] بله، و در زیر توضیح داده شده است

در صورت وجود، توضیح دهید:

## سایر یادداشت‌ها
اطلاعات دیگری که مرورگران باید بدانند؟
''')

# File: 07-plugins/pr-review/commands/check-tests.md
with open(os.path.join(fa_dir, "07-plugins", "pr-review", "commands", "check-tests.md"), "w", encoding="utf-8") as f:
    f.write('''---
description: اعتبارسنجی پوشش تست و کیفیت
---

# بررسی پوشش تست

تحلیل پوشش تست و کیفیت:

1. بررسی درصد پوشش تست
2. شناسایی مسیرهای کد بدون تست
3. مرور کیفیت تست‌ها
4. پیشنهاد موارد تست گمشده
5. تأیید پوشش موارد مرزی

---

**آخرین به‌روزرسانی**: 15 اکتبر 2026
**نسخه Claude Code**: 2.1.300
**منابع**:
- https://code.claude.com/docs/en/plugins
- https://code.claude.com/docs/en/skills#frontmatter-reference
''')

# File: 07-plugins/pr-review/commands/check-security.md
with open(os.path.join(fa_dir, "07-plugins", "pr-review", "commands", "check-security.md"), "w", encoding="utf-8") as f:
    f.write('''---
description: اجرای بازبینی امنیتی متمرکز بر کد
---

# بررسی امنیت

تحلیل امنیتی متمرکز بر تغییرات کد:

1. بررسی احراز هویت/مجوز
2. خطرات نشت داده
3. آسیب‌پذیری‌های تزریق
4. نقاط ضعف رمزنگاری
5. داده‌های حساس در لاگ‌ها

---

**آخرین به‌روزرسانی**: 15 اکتبر 2026
**نسخه Claude Code**: 2.1.300
**منابع**:
- https://code.claude.com/docs/en/plugins
- https://code.claude.com/docs/en/skills#frontmatter-reference
''')

# File: 07-plugins/pr-review/commands/review-pr.md
with open(os.path.join(fa_dir, "07-plugins", "pr-review", "commands", "review-pr.md"), "w", encoding="utf-8") as f:
    f.write('''---
description: آغاز مرور کامل Pull Request با بررسی‌های امنیتی و تست
---

# مرور PR

این دستور یک مرور کامل Pull Request را آغاز می‌کند که شامل موارد زیر است:

1. تحلیل امنیت
2. اعتبارسنجی پوشش تست
3. به‌روزرسانی مستندات
4. بررسی کیفیت کد
5. ارزیابی تأثیر عملکرد

---

**آخرین به‌روزرسانی**: 15 اکتبر 2026
**نسخه Claude Code**: 2.1.300
**منابع**:
- https://code.claude.com/docs/en/plugins
- https://code.claude.com/docs/en/skills#frontmatter-reference
''')

# File: 07-plugins/devops-automation/commands/rollback.md
with open(os.path.join(fa_dir, "07-plugins", "devops-automation", "commands", "rollback.md"), "w", encoding="utf-8") as f:
    f.write('''---
description: بازگشت به آخرین استقرار
---

# بازگشت استقرار

به نسخه قبلی پایدار باز می‌گردید:

1. تأیید آخرین استقرار
2. بررسی سلامت هدف بازگشت
3. اجرای فرآیند بازگشت
4. اجرای بررسی سلامت
5. اطلاع‌رسانی به تیم

---

**آخرین به‌روزرسانی**: 15 اکتبر 2026
**نسخه Claude Code**: 2.1.300
**منابع**:
- https://code.claude.com/docs/en/plugins
- https://code.claude.com/docs/en/skills#frontmatter-reference
''')

# File: 07-plugins/devops-automation/commands/status.md
with open(os.path.join(fa_dir, "07-plugins", "devops-automation", "commands", "status.md"), "w", encoding="utf-8") as f:
    f.write('''---
description: بررسی وضعیت سلامت کلی سیستم
---

# بررسی وضعیت سیستم

بررسی سلامت سیستم تمام سرویس‌ها:

1. بررسی وضعیت پودهای Kubernetes
2. بررسی اتصال پایگاه داده
3. نظارت بر زمان پاسخ API
4. مشاهده نرخ خطا
5. بررسی استفاده از منابع
6. گزارش وضعیت کلی سلامت

---

**آخرین به‌روزرسانی**: 15 اکتبر 2026
**نسخه Claude Code**: 2.1.300
**منابع**:
- https://code.claude.com/docs/en/plugins
- https://code.claude.com/docs/en/skills#frontmatter-reference
''')

# File: 07-plugins/devops-automation/commands/incident.md
with open(os.path.join(fa_dir, "07-plugins", "devops-automation", "commands", "incident.md"), "w", encoding="utf-8") as f:
    f.write('''---
description: پردازش حوادث تولید با فرآیند پاسخ ساختاری
---

# پاسخ به حادثه

جریان کاری پاسخ ساختاری:

1. ایجاد سوابق حادثه
2. ارزیابی شدت و تأثیر
3. اطلاع‌رسانی به تیم شیفت
4. جمع‌آوری اطلاعات تشخیص
5. هماهنگی کارهای پاسخ
6. ثبت راه‌حل
7. برگزاری مرور پساز

---

**آخرین به‌روزرسانی**: 15 اکتبر 2026
**نسخه Claude Code**: 2.1.300
**منابع**:
- https://code.claude.com/docs/en/plugins
- https://code.claude.com/docs/en/skills#frontmatter-reference
''')

print("All files written!")