import os

fa_dir = r"D:\Project\claude-howto\fa"

content = """<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../../resources/logos/claude-howto-logo-dark.svg">
  <img alt="Claude How To" src="../../resources/logos/claude-howto-logo.svg">
</picture>

# مرجع کامل Subagents

## مروری کلی

Subagents دستیارهای AI هستند که متخصص در انجام نوعی از وظایف هستند. آن‌ها زمینه ایزولته، پرامپت‌های خود و مجوزهای ابزار را دارند، برای تقسیم کارهای پیچیده به نقش‌های مختلف مناسب هستند.

## مزایای اصلی

- ایزولاسیون زمینه
- تقسیم telegraph استفاده شده
- برای اجرای موازی و تفویض مناسب است
- به تقسیم کارهای پیچیده کمک می‌کند

## موقعیت فایل‌ها

- سطح پروژه: `.claude/agents/`
- سطح کاربر: `~/.claude/agents/`

## پیکربندی

### قالب فایل

Subagent معمولاً یک فایل Markdown با frontmatter است.

```yaml
---
name: code-reviewer
description: بازبینی کیفیت کد و مشکلات امنیتی
tools: Read, Grep, Bash
---

# Code Reviewer
```

### فیلدهای پیکربندی

| فیلد | توضیحات |
|------|--------|
| `name` | نام subagent |
| `description` | چه زمانی باید فراخوانی شود |
| `tools` | ابزارهای مجاز |
| `model` | مشخص کردن مدل |
| `prompt` | پرامپت وظیفه |
| `context` | استراتژی زمینه |

### انتخاب‌های پیکربندی ابزار

- فقط-خواندن برای بازبینی
- محدود کردن Bash
- مجاز کردن مجموعه-tools قوی‌تر

### پیکربندی مبتنی بر CLI

همچنین می‌توانید از طریق خط فرمان یا فایل تنظیمات subagent تعریف کنید.
"""

with open(os.path.join(fa_dir, "04-subagents", "README.md"), "w", encoding="utf-8") as f:
    f.write(content)

print("04-subagents/README.md part 1 written!")