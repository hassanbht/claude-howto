import os

fa_dir = r"D:\Project\claude-howto\fa"

content = """

| دستور | توضیح | مثال |
|---------|-------------|---------|
| `claude update` | به‌روزرسانی به آخرین نسخه | `claude update` |
| `claude mcp` | پیکربندی سرورهای MCP | به [مستندات MCP](../05-mcp/README.md) مراجعه کنید |
| `claude mcp serve` | کلود کد را به عنوان MCP server اجرا کنید | `claude mcp serve` |
| `claude agents` | لیست subagents پیکربندی شده | `claude agents` |
| `claude auto-mode defaults` | مدل‌های پیش‌فرض حالت خودکار را به صورت JSON چاپ کنید | `claude auto-mode defaults` |
| `claude remote-control` | سرور کنترل از راه دور را راه‌اندازی کنید (حالت سرور، بدون سیشن تعاملی محلی؛ ظرفیت از ۳۲ پیش‌فرض) | `claude remote-control --name \"My Project\"` |
| `claude --remote-control [name]` | شروع سیشن تعاملی فعال شده از کنترل از راه دور (نام مستعار `--rc`) | `claude --rc` |
| `claude plugin` | مدیریت پلاquinها (نصب، فعال‌سازی، غیرفعال‌سازی) | `claude plugin install my-plugin` |
| `claude auth login` | ورود (پشتیبانی از `--email`، `--sso`) | `claude auth login --email user@example.com` |
| `claude auth logout` | خروج از حساب جاری | `claude auth logout` |
| `claude auth status` | بررسی وضعیت ورود (0 معتبر، ۱ نامعتبر) | `claude auth status` |

---

## مثال‌های کاربردی

### کاربرد‌های روزمره

```bash
# سیشن تعاملی
claude

# پرس‌وجو سریع
claude -p "explain this repo"

# ادامه‌های اخیر
claude -c

# بررسی فایل
claude -p "review README.md"

# JSON برای اسکریپت
claude -p --output-format json "list all classes"
```

---

## ترکیب پرچم‌ها

```bash
# مرور فقط‌خواندنی
claude --permission-mode plan -p "review this codebase"

# مدل پیشرفته + خروجی JSON
claude --model opus -p --output-format json "analyze architecture"

# دایرکتوری کاری سفارشی + MCP
claude --working-directory ./backend --mcp-config ./mcp.json
```

---

## مدل‌ها

### انتخاب مدل

```bash
# استفاده از نام‌های کوتاه
claude --model sonnet
claude --model opus
claude --model haiku

# استفاده از opusplan alias (Opus برای برنامه‌ریزی و Sonnet برای اجرا)
claude --model opusplan "design and implement the caching layer"

# تغییر به حالت speed در جلسه
claude --model haiku --effort low
```

### سطوح effort (Opus 4.6)

```bash
# تنظیم effort از طریق پارامتر CLI
claude --model opus --effort high "design the architecture"

# تنظیم effort از طریق دستور Slash
/effort max

# تنظیم effort از طریق متغیر محیطی
CLAUDE_EFFORT=medium claude --model opus
```

---

## متغیرهای محیطی رایج

| متغیر محیطی | توضیح |
|------|------|
| `ANTHROPIC_API_KEY` | کلید API |
| `CLAUDE_MODEL` | مدل پیش‌فرض |
| `CLAUDE_EFFORT` | شدت پیش‌فرض استدلال |
| `CLAUDE_WORKING_DIRECTORY` | دایرکتوری کاری پیش‌فرض |
| `CLAUDE_OUTPUT_FORMAT` | فرمت خروجی پیش‌فرض |
| `CLAUDE_MCP_CONFIG` | پیکربندی MCP پیش‌فرض |

---

## عیب‌یابی

### دستور پیدا نشد

- تایید اینکه `claude` نصب شده و در PATH است
- دوباره باز کردن ترمینال
- بررسی اینکه نیاز به ورود مجدد یا به‌روزرسانی است

### مشکل API Key

- بررسی `ANTHROPIC_API_KEY`
- تایید DecryptKey از آن گذشته نمی‌شود
- بررسی که شبکه به API قابل دسترس است

### سیشن پیدا نشد

- تایید نام یا شناسه سیشن صحیح است
- اول `claude --list-sessions` را اجرا کنید (اگر نسخه شما پشتیبانی می‌کند)
- بررسی برای مطابقت با حساب جاری

### مشکلات فرمت خروجی

- اطمینان حاصل کنید خروجی قابل تجزیه در `--output-format json` است
- اگر جاری است، `--include-partial-messages` را اضافه کنید

### مجوز رد شد

- بررسی `--permission-mode`
- بررسی `--allowedTools` و `--disallowedTools`
- در صورت نیاز، به‌صورت صریح ابزارهایی که نیاز است، اجازه دهید

### نمونه‌های پرکاربرد

```bash
# یافتن و مدیریت اتصالات مکرر
claude --remote-control

# استفاده از worktree
claude -w

# استفاده از 시가총액 mode
claude --permission-mode plan -p "analyze this codebase"
```

---

## منابع بیشتر

- [راهنمای ریشه](../README.md)
- [مرجع دستورات Slash](../01-slash-commands/README.md)
- [مستندات MCP](../05-mcp/README.md)
- [مستندات رسمی CLI کلود کد](https://code.claude.com/docs/en/cli-reference)

---

**آخرین به‌روزرسانی**: ۱۸ آبان ۲۰۲۶
**نسخه کلود کد**: ۲.۱.۳۰۲
**منبع**:
- https://code.claude.com/docs/en/cli-reference
- https://code.claude.com/docs/en/headless
- https://platform.claude.com/docs/en/about-claude/models/overview
- https://code.claude.com/docs/en/model-config
- https://code.claude.com/docs/en/remote-control
"""
with open(os.path.join(fa_dir, "10-cli", "README.md"), "a", encoding="utf-8") as f:
    f.write(content)

print("10-cli/README.md part 2 written!")