import os

fa_dir = r"D:\Project\claude-howto\fa"

content = """

## Subagent‌های داخلی

Claude Code همراه با برخی نقش‌های رایج است، مثلاً:

- دستیار عمومی
- Planning agent
- Explore agent
- claude агент پیش‌فرض
- Statusline+مربوط به агент
- claude-code-guide агент

## مدیریت Subagents

### استفاده از دستور `/agents` (توصیه می‌شود)

> **نکته**: راهنمای تعاملی `/agents` در v2.1.198 حذف شد و از v2.1.281 `/agents` دیگر در منوی `/` یا `/help` نمایش داده نمی‌شود. لطفاً به Claude بگویید تا subagent بسازد یا مدیریت کند، یا مستقیماً فایل `.claude/agents/<name>.md` اضافه کنید.

```text
یک subagent برای بازبینیsecurity کد بساز.
```

Claude برای شما فایل `.claude/agents/<name>.md` را می‌نویسد، و frontmatter مناسب را (ابزارها، مدل، توضیح) انتخاب می‌کند. سپس می‌توانید آن فایل را دستی تنظیم کنید، یا به Claude بگویید آن را تغییر دهد.

### مدیریت مستقیم فایل

#### ایجاد subagent پروژه

```bash
mkdir -p .claude/agents
```

#### ایجاد subagent کاربر

```bash
mkdir -p ~/.claude/agents
```

## استفاده از Subagents

### تفویض خودکار

دستیار اصلی می‌تواند بر اساس توضیح وظیفه، کار را به subagent مناسب تفویض کند.

### فراخوانی صریح

همچنین می‌توانید به صراحت به Claude بگویید تا از یک subagent خاص استفاده کند.

### فراخوانی با `@`

در برخی سناریوها، می‌توانید با `@agent-name` به آن ارجاع دهید.

### آDasgent سطح جلسه

می‌توانید در کل peril.session از یک agent ثابت استفاده کنید.

### لیست agent‌های موجود

برای مشاهده subagent‌های پیکربندی شده، می‌توانید از Claude بپرسید، یا `.claude/agents/` و `~/.claude/agents/` را مرور کنید.
"""

with open(os.path.join(fa_dir, "04-subagents", "README.md"), "a", encoding="utf-8") as f:
    f.write(content)

print("04-subagents/README.md part 2 written!")