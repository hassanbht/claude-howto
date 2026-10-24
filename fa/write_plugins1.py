import os

fa_dir = r"D:\Project\claude-howto\fa"

content = """<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../../resources/logos/claude-howto-logo-dark.svg">
  <img alt="Claude How To" src="../../resources/logos/claude-howto-logo.svg">
</picture>

# پلاquinهای کلود کد

این دایرکتorial شامل مجموعه‌ای از مثال‌های کامل پلاquin است که قابلیت‌های مختلف کلود کد را در یک راه حل یکپارچه قابل نصب ترکیب می‌کنند.

## معرفی

پلاquinهای کلود کد مجموعه‌های قابلیت هستند که دستورات slash، subagentها، سرورهای MCP و胡ک‌ها را در یکجا قرار می‌دهند و می‌توانند با یک دستور نصب شوند. آن‌ها بالاترین سطح توسعه‌پذیری کلود کد را نشان می‌دهند و قابلیت‌های مختلف را در یک راه حل قابل به اشتراک گذاشتن و استفاده مجدد ترکیب می‌کنند.

## مروری کلی

یک پلاquin معمولاً gabliétهای زیر را در یکجا قرار می‌دهد:

- دستورات slash
- subagentها
- سرورهای MCP
-胡ک‌ها

مزیت این کار این است:

- نصب یک‌باره و استفاده از گردش کار کامل
- به اشتراک گذاشتن آسانتر در تیم
- پیکربندی‌های یکپارچه‌تر
- کنترل نسخه و توزیع آسان‌تر

## معماری پلاquin

```mermaid
graph TB
    A["پلاquin"]
    B["دستورات Slash"]
    C["Subagentها"]
    D["سرورهای MCP"]
    E["هوک‌ها"]
    F["پیکربندی"]

    A -->|بسته‌بندی| B
    A -->|بسته‌بندی| C
    A -->|بسته‌بندی| D
    A -->|بسته‌بندی| E
    A -->|بسته‌بندی| F
```

## نوع و توزیع پلاquin

| نوع | دامنه | به اشتراک گذاشته شده برای | نگهدارنده | مثال |
|------|------|------------------|---------|------|
| رسمی | سراسری | همه کاربران | Anthropic | بازبینی PR، راهنمای امنیت |
| جامعه | عمومی | همه کاربران | جامعه | DevOps، علوم داده |
| سازمانی | داخلی | اعضای تیم | شرکت | استانداردهای داخلی، ابزارها |
| شخصی | شخصی | تک کاربر | توسعه‌دهنده | گردش کارهای سفارشی |

## ساختار تعریف پلاquin

پیمانت پلاquin در `.claude-plugin/plugin.json` با قالب JSON استفاده می‌شود:

```json
{
  "name": "my-first-plugin",
  "description": "یک پلاquin سلام",
  "version": "1.0.0",
  "author": {
    "name": "نام شما"
  },
  "homepage": "https://example.com",
  "repository": "https://github.com/user/repo",
  "license": "MIT"
}
```

## مثال ساختار پلاquin

```
my-plugin/
├── .claude-plugin/
│   └── plugin.json       # پیمانت (نام، توضیح، نسخه، نویسنده)
├── commands/             # دستورات به صورت فایل‌های Markdown
│   ├── task-1.md
│   ├── task-2.md
│   └── workflows/
├── agents/               # تعریف‌های agent سفارشی
│   ├── specialist-1.md
│   ├── specialist-2.md
│   └── configs/
├── skills/               # مهارت‌هایی با فایل SKILL.md
│   ├── skill-1/
│   │   └── SKILL.md
│   └── skill-2/
│       └── SKILL.md
├── hooks/                # پردازشگرهای رویداد در hooks.json
│   └── hooks.json
├── .mcp.json             # پیکربندی سرور MCP
├── .lsp.json             # پیکربندی سرور LSP
├── settings.json         # تنظیمات پیش‌فرض
├── templates/
│   └── issue-template.md
├── scripts/
│   ├── helper-1.sh
│   └── helper-2.py
├── docs/
│   ├── README.md
│   └── USAGE.md
└── tests/
    └── plugin.test.js
```

### پیکربندی سرور LSP

پلاquinها می‌توانند از پشتیبانی Language Server Protocol (LSP) برای هوش کد در زمان واقعی استفاده کنند. سرور LSP در هنگام نوشتن کد، تشخیص، ناوبری کد و اطلاعات نماد را ارائه می‌دهد.

**مکان پیکربندی:**
- فایل `.lsp.json` در ریشه پلاquin
- کلید لایه‌ای `lsp` در `plugin.json`

#### مرجع فیلدها

| فیلد | الزامی | توضیح |
|------|--------|----------|
| `command` | بله | فایل اجرای سرور LSP (باید در PATH باشد) |
| `extensionToLanguage` | بله | گسترش فایل را به زبان ID نقشه می‌دهد |
| `args` | خیر | آرگumerانت‌های خط فرمان سرور |
| `transport` | خیر | روش ارتباط: `stdio` (پیش‌فرض) یا `socket` |
| `env` | خیر | متغیرهای محیطی فرآیند سرور |
| `initializationOptions` | خیر | گزینه‌های ارسالی در هنگام مقداردهی اولیه LSP |
| `settings` | خیر | پیکربندی فضای کاری ارسالی به سرور |
| `workspaceFolder` | خیر | تجاوز مسیر فضای کاری |
| `startupTimeout` | خیر | حداکثر زمان انتظار برای راه‌اندازی سرور (ملی‌ثانیه) |
| `shutdownTimeout` | خیر | حداکثر زمان برای ت끄 달闭outines |
| `restartOnCrash` | خیر | در صورت crash سرور، به صورت خودکار راه‌اندازی مجدد |
| `maxRestarts` | خیر | حداکثر تعداد راه‌اندازی مجدد قبل ازريكاaftن |

#### مثال پیکربندی

**گوس (gopls):**

```json
{
  "go": {
    "command": "gopls",
    "args": ["serve"],
    "extensionToLanguage": {
      ".go": "go"
    }
  }
}
```

**پایتون (pyright):**

```json
{
  "python": {
    "command": "pyright",
    "args": ["--stdio"],
    "extensionToLanguage": {
      ".py": "python"
    }
  }
}
```
"""

with open(os.path.join(fa_dir, "07-plugins", "README.md"), "w", encoding="utf-8") as f:
    f.write(content)

print("07-plugins/README.md part 1 written!")