import os

fa_dir = r"D:\Project\claude-howto\fa"

content = """<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../../resources/logos/claude-howto-logo-dark.svg">
  <img alt="Claude How To" src="../../resources/logos/claude-howto-logo.svg">
</picture>

# دستور تعریف‌دهی (Commit)

این دستور، مدیریت định‌نمایی کد و مرج تعریف‌کردن را به‌عنوان یک لایه‌ی پشتیبانی دارد. برای توضیح مفاهیم پیچیده‌تر، استفاده‌ی ادامه، و پروژه‌های عمومی، استفاده می‌شود.

## فهرست مطالب

1. [چیست؟](#چه-چیست)
2. [فرمت‌های تعریف‌دهی](#فرمت‌های-تعمیق‌نمایی)
3. [ساخت یک فریم‌ورک](#ساخت-یک-فریم‌ورک)
4. [ارسال یک PR](#ارسال-یک-pr)
5. [ارسال نسخه‌ها](#ارسال-نسخه‌ها)
6. [بازیابی و روان‌سازی](#بازیابی-و-روان‌سازی)
7. [اشکال‌پردازی](#اشکال‌پردازی)

---

## چه چیست؟

دستور **commit**، یک efforts এক-لایه برای مدیریت تعریف‌نمایی و ترجمه ماهر کد به‌دست می‌آورد. از جمله دستورات، می‌توان هر تعریف که بکار برده شود را ذخیره کرد.

## فرمت‌های تعریف‌دهی

### تعریف‌های پیش‌فرض

```json
{
  "name": "commit-example",
  "description": "مثال تعریف",
  "documentation": "https://example.com/docs",
  "entrypoint": "./src/index.ts",
  "tags": ["commit", "example"]
}
```

### تعریف‌های مخصوص

```yaml
---
name: my-custom-command
description: توضیح خاص
tags: git, commit
custom_path: "./.custom-command"
version: "1.0.0"
---
```

## ساخت یک فریم‌ورک

فریم‌ورک، یک فایل مسدود یا گیتی‌های جداگانه است که به‌صورت خودکار؛ به‌عنوان یک "فایل تعریف‌دهی" استفاده می‌شود.

```bash
# ساخت دستور
claude /commit --name my-cmd --description "description"

# چک‌لیست
claude /commit --check
```

---

## ارسال یک PR

۱. دستور را اجرا کنید
۲. تغییرات را commit کنید
۳. PR را ارسال کنید
۴. کدنویسی را بررسی کنید

---

## ارسال نسخه‌ها

از دستور `/commit bum` برای نگهداری نسخه‌ها استفاده می‌شود.

```bash
# ارسال نسخه
claude /commit bump --version 1.2.3
```

---

## بازیابی و روان‌سازی

```bash
# بازگرداندن به نسخه قبل
claude /rewind

# روان‌سازی (commit)
claude /commit --squash
```

---

## اشکال‌پردازی

- دستور `/commit` پیدا نشد: اطمینان حاصل کنید که `.claude/commands/` پوشه‌ی صحیحی است
- خطای `name` یا `description`: XML یا YAML به‌درستی نوشته شده باشد
- دستور به‌جای رفتن: چک‌لیست دستور را بررسی می‌کنید

---

**آخرین به‌روزرسانی**: ۱۸ آبان ۲۰۲۶
**نسخه کلود کد**: ۲.۱.۳۰۲
"""
with open(os.path.join(fa_dir, "01-slash-commands", "commit.md"), "w", encoding="utf-8") as f:
    f.write(content)

print("01-slash-commands/commit.md written!")