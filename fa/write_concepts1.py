import os

fa_dir = r"D:\Project\claude-howto\fa"

content = """<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../resources/logos/claude-howto-logo-dark.svg">
  <img alt="Claude How To" src="../resources/logos/claude-howto-logo.svg">
</picture>

# رهنمای کامل مفاهیم کلود کد

این دفترچه مرجع جامعی است که Slash Commands، Subagents، Memory، MCP Protocol، Agent Skills، Plugins، Hooks، Checkpoints، Advanced Features و سایر مفاهیم کلود کد را پوشش می‌دهد و همراه با جداول، نمودارها و مثال‌های عملی است.

## فهرست مطالب

1. [دستورات Slash](#slash-commands)
2. [Subagents](#subagents)
3. [Memory](#memory)
4. [نCoderلوك PMC Protocol](#mcp-protocol)
5. [مهارت‌های Agent](#agent-skills)
6. [پلاquinها](#claude-code-plugins)
7. [هوک‌ها](#hooks)
8. [Checkpointها و Rewind](#checkpoints-and-rewind)
9. [ویژگی‌های پیشرفته](#advanced-features)
10. [مقایسه و یکپارچه‌سازی](#comparison--integration)

---

## دستورات Slash

### مرور کلی

دستورات Slash، دستورهای کوتاه هستند که کاربر به صورت دستی شروع می‌کنند، به صورت فایل‌های Markdown ذخیره می‌شوند و کلود کد می‌تواند آن‌ها را بخواند و اجرا کند. برای استاندارد کردن پرامپت‌های با فراوان و چرخه‌های کاری عادی، بسیار مناسبی هستند، از سوی کاربران، برای تعمیم این روش‌ها در تیم‌ها.

### معماری

```mermaid
graph TD
    A["ورودی کاربر: /command-name"] -->|trigger| B["Search .claude/commands/"]
    B -->|found| C["command-name.md"]
    C -->|load| D["Markdown content"]
    D -->|execute| E["Claude handle prompt"]
    E -->|return| F["Results in context"]
```

### ساختار فایل

```mermaid
graph LR
    A["Root of project"] -->|contains| B[".claude/commands/"]
    B -->|contains| C["optimize.md"]
    B -->|contains| D["test.md"]
    B -->|contains| E["docs/"]
    E -->|contains| F["generate-api-docs.md"]
    E -->|contains| G["generate-readme.md"]
```

### جدول سازمان‌یابی دستورات

| مکان | دامنه | محدوده در دسترس | سناریو کاربرد | ردیابی Git |
|------|--------|------------------|----------------|-------------|
| `.claude/commands/` | سطوح پروژه | اعضای تیم | گردش‌کار تیمی، استانداردهای مشترک | ✅ بله |
| `~/.claude/commands/` | سطوح کاربری | کاربر فعلی | دستورات سریع شخصی از پروژه‌ای به دیگر | ❌ خیر |
| Subdirectories | فضای نام‌گذاری | بسته به پدر | سازمان‌یابی دستورات بر اساس دامنه | ✅ بله |

### قابلیت‌ها و توانایی‌ها

| قابلیت | مثال | پشتیبانی می‌کند؟ |
|--------|------|------------------|
| اجرا اسکریپت‌های Sh | `bash scripts/deploy.sh` | ✅ بله |
| ارجاع فایل | `@path/to/file.js` | ✅ بله |
| یکپارچگی Bash | `$(git log --oneline)` | ✅ بله |
| آرگومان‌ها | `/pr --verbose` | ✅ بله |
| دستور MCP | `/mcp__github__list_prs` | ✅ بله |

### مثال‌های عملی

#### مثال ۱: دستور بهینه‌سازی کد

**فایل**: `.claude/commands/optimize.md`

```markdown
---
name: بهینه‌سازی کد
description: تحلیل مشکلات عملکردی و پیشنهاد بهینه‌سازی
tags: performance, analysis
---

# تحلیل کد

بر اساس اولویت‌های زیر، مسائل کد را بررسی کنید:

۱. **ظرفیت‌های عملکردی** - شناسایی عملیات O(n²) و حلقه‌های ناکارآمد
۲. **ر شیرش حافظه** - یافتن منابع آزاد نشده، ارجاعات دایره‌ای
۳. **بهبود الگوریتم** - پیشنهاد بهتر
... (truncated) ...
"""
with open(os.path.join(fa_dir, "claude_concepts_guide.md"), "w", encoding="utf-8") as f:
    f.write(content)

print("claude_concepts_guide.md part 1 written!")