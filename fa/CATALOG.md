<picture>
  <source media="(prefers-color-scheme: dark)" srcset="resources/logos/claude-howto-logo-dark.svg">
  <img alt="Claude How To" src="resources/logos/claude-howto-logo.svg">
</picture>

# Claude Code Feature Catalog

> راهنمای مرجع سریع برای همه featureهای Claude Code: commands، agents، skills، plugins و hooks.

## خلاصه

| Feature | Built-in | Examples | Total | Reference |
|---------|----------|----------|-------|-----------|
| Slash Commands | 60+ | 8 | 68+ | [01-slash-commands/](01-slash-commands/) |
| Subagents | 6 | 9 | 15 | [04-subagents/](04-subagents/) |
| Skills | 20 bundled | 6 | 26 | [03-skills/](03-skills/) |
| Plugins | - | 3 | 3 | [07-plugins/](07-plugins/) |
| MCP Servers | - | 4 | 4 | [05-mcp/](05-mcp/) |
| Hooks | 33 events | 11 | 44 | [06-hooks/](06-hooks/) |
| Memory | 7 types | 3 | 10 | [02-memory/](02-memory/) |
| **Total** | **126** | **44** | **170** | |

## Slash Commands

دستورهای user-invoked که actionهای مشخصی را اجرا می‌کنند. لیست کامل در [01-slash-commands/](01-slash-commands/) و [10-cli/](10-cli/).

## Permission Modes

manual/default، acceptEdits، plan، auto، dontAsk، bypassPermissions — کنترل می‌کنند Claude بدون prompt چه کاری می‌تواند انجام دهد.

## Subagents

subagentهای تخصصی برای taskهای isolated. [04-subagents/](04-subagents/)

## Skills

capabilityهای auto-invoke. [03-skills/](03-skills/)

## Plugins

bundleهای complete solution. [07-plugins/](07-plugins/)

## MCP Servers

external data integrations. [05-mcp/](05-mcp/)

## Hooks

event-triggered automation. [06-hooks/](06-hooks/)

## Memory

persistent context. [02-memory/](02-memory/)

## New Features

ویژگی‌های جدید در Claude Code — به [09-advanced-features/](09-advanced-features/) و [CATALOG](../CATALOG.md) انگلیسی برای جزئیات مراجعه کنید.

## Quick Reference Matrix

### Feature Selection Guide

| Need | Recommended Feature | Why |
|------|---------------------|-----|
| Quick shortcut | Slash Command | Manual, immediate |
| Persistent context | Memory | Auto-loaded |
| Complex automation | Skill | Auto-invoked |
| Specialized task | Subagent | Isolated context |
| External data | MCP Server | Real-time access |
| Event automation | Hook | Event-triggered |
| Complete solution | Plugin | All-in-one bundle |

### Installation Priority

1. Essential — Memory: `cp 02-memory/project-CLAUDE.md ./CLAUDE.md`
2. Daily Use — Slash Commands: `cp 01-slash-commands/*.md .claude/commands/`
3. Quality — Subagents: `cp 04-subagents/*.md .claude/agents/`
4. Automation — Hooks
5. External — MCP
6. Advanced — Skills
7. Complete — Plugins

## Complete One-Command Installation

```bash
mkdir -p .claude/{commands,agents,skills} ~/.claude/{hooks,skills}
# سپس فایل‌های مثال را کپی کنید (دستورات دقیق در نسخه انگلیسی CATALOG.md)
```

---

**Last Updated**: October 2026

*Part of the [Claude How To](../) guide series*
