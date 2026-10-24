import os

fa_dir = r"D:\Project\claude-howto\fa"

content = """
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

### نصب پلاquinها

#### از مسیر محلی

```bash
# نصب از مسیر محلی
claude --plugin-dir ./path/to/plugin-directory
```

### از GitHub نصب

```bash
/plugin marketplace add username/repo                    # اضافه کردن مخزن GitHub به عنوان مارکت
/plugin install plugin-name@marketplace-name             # سپس نصب پلاquin از آن مارکت
/plugin install plugin-name --marketplace username/repo  # یا انجام هم‌زمان هر دو (v2.1.275+)
```

### فهرست پلاquin‌های نصب شده

```bash
/plugin list             # همه پلاquin‌های نصب شده
/plugin list --enabled   # فقط پلاquin‌های فعال
/plugin list --disabled  # فقط پلاquin‌های غیرفعال
```

### به‌روزرسانی پلاquin

از فرمت CLI استفاده شود — این فرمت در [`plugin update`](https://code.claude.com/docs/en/plugins-reference) ثبت شده است، و همچنین زمانی که به‌روزرسانی در دسترس باشد کلود کد از شما می‌خواهد از آن استفاده کنید:

```bash
claude plugin update plugin-name
```

### غیرفعال / فعال کردن پلاquin

```bash
# غیرفعال‌سازی موقت
/plugin disable plugin-name

# فعال‌سازی مجدد
/plugin enable plugin-name
```

### حذف کردن پلاquin

```bash
/plugin uninstall plugin-name
```

## مفاهیم مرتبط

قابلیت‌های زیر کلود کد با پلاquinها همکاری می‌کنند:

- **[دستورات Slash](../01-slash-commands/README.md)** - دستورات جداگانه بسته‌بندی شده در پلاquin
- **[حافظه](../02-memory/README.md)** - contexte پایدار پلاquin
- **[مهارت‌ها](../03-skills/README.md)** - قابلیت‌های stromal که می‌توانند در پلاquin بسته شوند
- **[Subagentها](../04-subagents/README.md)** - agentهای تخصصی که به عنوان اجزای پلاquin شامل می‌شوند
- **[سرورهای MCP](../05-mcp/README.md)** - یکپارچگی‌های MCP بسته‌بندی شده در پلاquin
- **[هوک‌ها](../06-hooks/README.md)** - پردازشگرهای رویداد که گردش کار پلاquin را فعال می‌کنند
"""

with open(os.path.join(fa_dir, "07-plugins", "README.md"), "a", encoding="utf-8") as f:
    f.write(content)

print("07-plugins/README.md part 2 written!")