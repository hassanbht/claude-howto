import os

fa_dir = r"D:\Project\claude-howto\fa"

# File 1: .github/ISSUE_TEMPLATE/question.md
with open(os.path.join(fa_dir, ".github", "ISSUE_TEMPLATE", "question.md"), "w", encoding="utf-8") as f:
    f.write('''---
name: Question
about: سؤال در مورد Claude Code یا این راهنما
title: "[QUESTION] "
labels: question
assignees: ''

---

## سؤال
چه می‌خواهید بدانید؟

## پیش‌زمینه
چند خط پیش‌زمینه یا زمینه ارائه دهید:
- می‌خواهید چه کاری انجام دهید؟
- قبلاً چه کارهایی امتحان کرده‌اید؟
- چه مثال‌ها یا راهنمایی‌هایی را دیده‌اید؟

## موضوع مرتبط
این سؤال متعلق به کدام موضوع است؟
- [ ] Slash Commands
- [ ] Memory
- [ ] Skills
- [ ] Subagents
- [ ] MCP Protocol
- [ ] Hooks
- [ ] Plugins
- [ ] Checkpoints
- [ ] Advanced Features
- [ ] CLI Reference
- [ ] سایر

## کارهایی که امتحان کرده‌اید
چه کارهایی را امتحان کرده‌اید؟ نتیجه چه بود؟

## نتیجه مورد انتظار
چه نتیجه‌ای می‌تواند به حل مشکل شما کمک کند؟

## منابع دیگر
چه لینک‌ها یا منابعی مرتبط ممکن است وجود داشته باشند؟
''')

# File 2: .github/ISSUE_TEMPLATE/bug_report.md
with open(os.path.join(fa_dir, ".github", "ISSUE_TEMPLATE", "bug_report.md"), "w", encoding="utf-8") as f:
    f.write('''---
name: Bug Report
about: گزارش مشکل در مثال، راهنما یا مستندات
title: "[BUG] "
labels: bug
assignees: ''

---

## توضیح مشکل
مشکل را به طور خلاصه شرح دهید.

## گام‌های تکرار
1. گام اول
2. گام دوم
3. گام سوم

## رفتار انتظاری
چه باید اتفاق بیفتد؟

## رفتار واقعی
چه اتفاقی در واقع افتاد؟

## محیط
- **نسخه Claude Code**: (مثال: 1.0.5)
- **سیستم عامل**: (مثال: macOS 14.1، Ubuntu 22.04، Windows 11)
- **نسخه Python**: (در صورت مرتبط بودن، مثال: 3.11)
- **کامپوننت مرتبط**: (مثال: 01-slash-commands، 03-skills و غیره)

## کد نمونه
در صورت نیاز، کد نمونه‌ای که به درستی کار نمی‌کند ارائه دهید:
```
[کد خود را اینجا قرار دهید]
```

## اسکرین‌شات
در صورت نیاز، اسکرین‌شات نشان‌دهنده مشکل ضمیمه کنید.

## سایر زمینه‌ها
چه اطلاعات دیگری ممکن است درک مشکل شما را کمک کند؟

## راه‌حل پیشنهادی
اگر راه‌حلی دارید، در اینجا بنویسید.
''')

print("Template files written!")