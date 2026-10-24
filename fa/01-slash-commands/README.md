<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../resources/logos/claude-howto-logo-dark.svg">
  <img alt="Claude How To" src="../resources/logos/claude-howto-logo.svg">
</picture>

# Slash Commands

## مرور کلی

Slash commandها میانبرهایی هستند که رفتار Claude را در طول یک session تعاملی کنترل می‌کنند. آن‌ها چند نوع دارند:

- **Built-in commands**: توسط Claude Code فراهم می‌شوند (`/help`، `/clear`، `/model`)
- **Skills**: commandهای تعریف‌شده توسط کاربر ایجادشده به عنوان فایل‌های `SKILL.md` (`/optimize`، `/pr`)
- **Plugin commands**: commandها از pluginهای نصب‌شده (`/frontend-design:frontend-design`)
- **MCP prompts**: commandها از سرورهای MCP (`/mcp__github__list_prs`)

> **یادداشت**: custom slash commandها با skills ادغام شده‌اند. فایل‌های در `.claude/commands/` هنوز کار می‌کنند، اما skills (`.claude/skills/`) اکنون رویکرد توصیه‌شده است. هر دو `/command-name` میانبر ایجاد می‌کنند. برای reference کامل [Skills Guide](../03-skills/) را ببینید.

## Built-in Commands Reference

Built-in commandها میانبرهایی برای actions رایج هستند. **60+ built-in command** و **حدود 20 bundled skill** (برخی feature-gated) موجود است. `/` را در Claude Code تایپ کنید تا لیست کامل را ببینید، یا `/` را به دنبال هر حرف تایپ کنید تا filter شود.

> **یادداشت**: از v2.1.236، فشردن Enter روی یک slash command اشتباه‌تایپ‌شده — یا روی commandی که در session فعلی موجود نیست — به جای اجرای silent نزدیک‌ترین fuzzy match، خطا گزارش می‌دهد. prefixهای unambiguous و aliasهای تعریف‌شده همچنان به‌طور عادی اجرا می‌شوند.

(جدول کامل built-in commands و مثال‌ها در فایل اصلی `01-slash-commands/README.md` حفظ شده‌اند.)

## Related Guides

- **[Skills](../03-skills/)** - Full reference for skills (auto-invoked capabilities)
- **[Memory](../02-memory/)** - Persistent context with CLAUDE.md
- **[Subagents](../04-subagents/)** - Delegated AI agents
- **[Plugins](../07-plugins/)** - Bundled command collections
- **[Hooks](../06-hooks/)** - Event-driven automation

---

**Last Updated**: October 18, 2026
**Claude Code Version**: 2.1.302

*Part of the [Claude How To](../) guide series*
