import os

fa_dir = r"D:\Project\claude-howto\fa"

content = """

## راهنمای نصب

### روش ۱: استفاده از `/agents`

> **نکته**: راهنمای تعاملی `/agents` در v2.1.198 حذف شد و از v2.1.281 `/agents` دیگر در منوی `/` یا `/help` نمایش داده نمی‌شود. لطفاً به Claude بگویید تا subagent بسازد یا مدیریت کند، یا مستقیماً فایل `.claude/agents/<name>.md` اضافه کنید.

```text
یک subagent سطح پروژه بساز که تست‌ها را اجرا و خطاها را برطرف کند.
هر آن را به Bash، Read، Edit و Grep دسترسی بده.
```

Claue فایل `.claude/agents/<name>.md` را با frontmatter مناسب می‌نویسد. پس از بررسی فایل تولید شده، می‌توانید از آن استفاده کنید.

### روش ۲: کپی به پروژه

```bash
mkdir -p .claude/agents
cp 04-subagents/*.md .claude/agents/
```

### روش ۳: کپی به دایرکتوری کاربر

```bash
mkdir -p ~/.claude/agents
cp 04-subagents/*.md ~/.claude/agents/
```

### تأیید

- به Claude بگویید تا یک subagent بسازد، یا مستقیماً فایل `.claude/agents/<name>.md` اضافه کنید
- لیست دایرکتوری را بررسی کنید تا validated باشد که فایل‌ها در جای خود هستند: `ls .claude/agents/`
- همچنین می‌توانید از Claude بپرسید چه subagent‌هایی در peril.session فعلی موجود است؛ سپس از شما گزارش می‌دهد که chefどのような�שימות قابل تفويض هستند
- سعی کنید به Claude بگویید یک وظیفه ساده را تفويض کند

## ساختار فایل‌ها

```text
.claude/agents/
├── clean-code-reviewer.md
├── code-reviewer.md
├── data-scientist.md
├── debugger.md
├── documentation-writer.md
├── implementation-agent.md
├── secure-reviewer.md
├── test-engineer.md
└── README.md
```

## مفاهیم مرتبط

- [راهنمای Skills](../03-skills/README.md)
- [راهنمای حافظه](../02-memory/README.md)
- [راهنمای胡ک‌ها](../06-hooks/README.md)
- [راهنمای پلاگین‌ها](../07-plugins/README.md)

---

**آخرین به‌روزرسانی**: ۱۵ آبان ۲۰۲۶
**نسخه Claude Code**: ۲.۱.۳۰۰
**منبع**:
- https://code.claude.com/docs/en/sub-agents
- https://code.claude.com/docs/en/commands
- https://code.claude.com/docs/en/hooks
- https://code.claude.com/docs/en/cli-reference
- https://code.claude.com/docs/en/agent-view
- https://code.claude.com/docs/en/sub-agents#permission-modes
- https://code.claude.com/docs/en/sub-agents#available-tools
"""

with open(os.path.join(fa_dir, "04-subagents", "README.md"), "a", encoding="utf-8") as f:
    f.write(content)

print("04-subagents/README.md part 5 written!")