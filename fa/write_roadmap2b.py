import os

fa_dir = r"D:\Project\claude-howto\fa"

content = """

##里程碑‌ها

### 🟢里程碑 ۱A: اولین دستور و حافظه - ۲۴ ساعت اول

** Ça می-enchoud:**

- [ ] به [۰۱-دستورات slash](01-slash-commands/README.md) مراجعه کنید
- [ ] یک دستور Slash نصب کنید
- [ ] دستور را امتحان کنید
- [ ] به [۰۲-حافظه](02-memory/README.md) مراجعه کنید
- [ ] فایل `CLAUDE.md` پروژه ایجاد کنید
- [ ] یک Subagent نصب کنید
- [ ] یک یکپارچگی MCP پیکربندی کنید
- [ ] یک مهارت نصب کنید
- [ ] یک پلاquin کامل امتحان کنید
- [ ] بر اساس نیاز خود شخصی‌سازی کنید
- [ ] با تیم به اشتراک بگذارید
- [ ] **انتقال به里程碀 ۱B**

### 🟢里程碑 ۱B: کاوش امن - ۲۴ ساعت دوم

- [ ] به [۰۸-checkpoints](08-checkpoints/README.md) مراجعه کنید
- [ ] یک checkpoint ایجاد کنید و به آن بازگردید
- [ ] از حالت تعاملی و حالت چاپ استفاده کنید
- [ ] **انتقال به里程碀 ۱B**

### 🔵 Level ۲: متوسط

- [ ] [۰۳-مهارت‌ها](03-skills/README.md) را تکمیل کنید
- [ ] [۰۶-هوک‌ها](06-hooks/README.md) را تکمیل کنید
- [ ] یک skill نصب کنید
- [ ] یک PreToolUse hook تنظیم کنید
- [ ] **انتقال به里程碀 ۲A**
- [ ] [۰۵-mcp](05-mcp/README.md) را تکمیل کنید
- [ ] [۰۴-subagents](04-subagents/README.md) را تکمیل کنید
- [ ] GitHub MCP را پیوسته کنید
- [ ] یک subagent سفارشی ایجاد کنید
- [ ] یکپارچگی‌های مختلف را در یک گردش کار ترکیب کنید
- [ ] **انتقال به里程碀 ۲B**

### 🔴 Level ۳: پیشرفته

- [ ] [۰۹-ویژگی‌های-پیشرفته](09-advanced-features/README.md) را تکمیل کنید
- [ ] با موفقیت از planning mode استفاده کنید
- [ ] حالت‌های مجاز را پیکربندی کنید (شامل ۶ حالت auto)
- [ ] از حالت خودکار (Auto mode) با学者هایمنی استفاده کنید
- [ ] از extended thinking استفاده کنید
- [ ] کانال‌ها (Channels) و ورودی صوتی (Voice Dictation) را کاوش کنید
- [ ] **انتقال به里程碀 ۳A**
- [ ] [۰۷-پلاquinها](07-plugins/README.md) را تکمیل کنید
- [ ] [۱۰-cli](10-cli/README.md) را در حالت پیشرفته تکمیل کنید
- [ ] حالت چاپ (`claude -p`) را برای CI/CD پیکربندی کنید
- [ ] برای اتوماسیون خروجی JSON ایجاد کنید
- [ ] کلود کد را در خط لوله CI/CD یکپارچ کنید
- [ ] یک پلاquin تیمی ایجاد کنید
- [ ] **انتقال به里程碀 ۳B**

"""

with open(os.path.join(fa_dir, "LEARNING-ROADMAP.md"), "a", encoding="utf-8") as f:
    f.write(content)

print("LEARNING-ROADMAP.md part 2b written!")