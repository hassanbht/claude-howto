import os

fa_dir = r"D:\Project\claude-howto\fa"

# File: 01-slash-commands/pr.md
content = """---
description: بازسازی کد، استیج تغییرات و آماده‌سازی Pull Request
allowed-tools: Bash(git add:*), Bash(git status:*), Bash(git diff:*), Bash(npm test:*), Bash(npm run lint:*)
---

# فهرست بررسی Pull Request

قبل از ایجاد PR، مراحل زیر را انجام دهید:

1. اجرای فرمت화: `prettier --write .`
2. اجرای تست‌ها: `npm test`
3. مشاهده git diff: `git diff HEAD`
4. استیج تغییرات: `git add .`
5. ایجاد پیام commit با فرمت conventional commits:
   - `fix:` رفع باگ
   - `feat:` ویژگی جدید
   - `docs:` مستندات
   - `refactor:` بازسازی کد
   - `test:` تست جدید
   - `chore:` نگهداری

6. تولید خلاصه PR شامل:
   - چه چیزی تغییر کرد
   - دلیل تغییر
   - چه تست‌هایی انجام شد
   - پیامدهای ممکن
"""

with open(os.path.join(fa_dir, "01-slash-commands", "pr.md"), "w", encoding="utf-8") as f:
    f.write(content)

# File: 01-slash-commands/setup-ci-cd.md
content = """---
name: setup-ci-cd
description: راه‌اندازی هوک‌های pre-commit و GitHub Actions برای تضمین کیفیت
---

# راه‌اندازی خط لوله CI/CD

یک خط لوله DevOps کامل را بر اساس نوع پروژه پیاده‌سازی کنید:

1. **تجزیه و تحلیل پروژه**: شناسایی زبان، چارچوب، سیستم ساخت و زنجیره ابزار موجود
2. **پیکربندی هوک‌های pre-commit**، استفاده از ابزارهای متناسب با زبان:
   - فرمت화: Prettier/Black/gofmt/rustfmt و غیره
   - بررسی کد: ESLint/Ruff/golangci-lint/Clippy و غیره
   - امنیت: Bandit/gosec/cargo-audit/npm audit و غیره
   - بررسی نوع: TypeScript/mypy/flow (در صورت مناسب بودن)
   - تست: اجرای مجموعه تست مربوطه
3. **ایجاد گردش کار GitHub Actions** (`.github/workflows/`):
   - منعکس کردن بررسی‌های pre-commit در push/PR
   - ماتریس نسخه/پلتفرم (در صورت مناسب بودن)
   - تأیید ساخت و تست
   - مراحل استقرار (در صورت نیاز)
4. **تأیید خط لوله**: تست محلی، ایجاد یک PR تست، تأیید اینکه همه بررسی‌ها Durch شده‌اند

از ابزارهای رایگان/مفتولاست استفاده کنید. پیکربندی‌های موجود را حفظ کنید. اجرا را سریع نگه دارید.
"""

with open(os.path.join(fa_dir, "01-slash-commands", "setup-ci-cd.md"), "w", encoding="utf-8") as f:
    f.write(content)

print("pr.md and setup-ci-cd.md written!")