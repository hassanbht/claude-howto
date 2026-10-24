import os

fa_dir = r"D:\Project\claude-howto\fa"

# File: 01-slash-commands/commit.md
content = """---
allowed-tools: Bash(git add:*), Bash(git status:*), Bash(git commit:*), Bash(git diff:*)
argument-hint: [message]
description: ایجاد یک Git commit با زمینه
---

## زمینه

- وضعیت فعلی git: !`git status`
- diff فعلی git: !`git diff HEAD`
- Branch فعلی: !`git branch --show-current`
- آخرین commitها: !`git log --oneline -10`

## وظیفه شما

بر اساس تغییرات بالا، یک commit Git جداگانه بسازید.

اگر message از طریق پارامتر ارسال شده باشد، از آن استفاده کنید: $ARGUMENTS

در غیر این صورت، این تغییرات را تحلیل کنید و با فرمت conventional commits یک پیام commit مناسب بسازید:
- `feat:` ویژگی جدید
- `fix:` رفع باگ
- `docs:` تغییر مستندات
- `refactor:` بازسازی کد
- `test:` تست جدید
- `chore:` وظیفه نگهداری
"""

with open(os.path.join(fa_dir, "01-slash-commands", "commit.md"), "w", encoding="utf-8") as f:
    f.write(content)

print("commit.md fixed!")