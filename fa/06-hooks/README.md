<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../resources/logos/claude-howto-logo-dark.svg">
  <img alt="Claude How To" src="../resources/logos/claude-howto-logo.svg">
</picture>

# Hooks

Hooks scriptهای automated هستند که در پاسخ به eventهای specific در طول sessionهای Claude Code اجرا می‌شوند. آن‌ها automation، validation، permission management و custom workflowها را فراهم می‌کنند.

## مرور کلی

Hooks actionهای automated (shell commands، HTTP webhooks، LLM prompts، MCP tool calls، یا subagent evaluations) هستند که به‌طور خودکار هنگام رخ دادن eventهای specific در Claude Code اجرا می‌شوند. آن‌ها JSON input دریافت می‌کنند و نتایج را از طریق exit codeها و JSON output communicate می‌کنند.

**ویژگی‌های کلیدی:**
- automation event-driven
- input/output مبتنی بر JSON
- پشتیبانی از hook typeهای `command`، `http`، `mcp_tool`، `prompt` و `agent`
- pattern matching برای hookهای tool-specific

## Configuration

Hooks در settings files با structure specific configure می‌شوند:
- `~/.claude/settings.json` - تنظیمات کاربر (همه پروژه‌ها)
- `.claude/settings.json` - تنظیمات پروژه (shareable، committed)
- `.claude/settings.local.json` - تنظیمات محلی پروژه (committed نمی‌شود)
- Managed policy - تنظیمات organization-wide
- Plugin `hooks/hooks.json` - hookهای plugin-scoped
- Skill/Agent frontmatter - hookهای component lifetime

### Basic Configuration Structure
```json
{
  "hooks": {
    "EventName": [
      {
        "matcher": "ToolPattern",
        "hooks": [
          {
            "type": "command",
            "command": "your-command-here",
            "timeout": 60
          }
        ]
      }
    ]
  }
}
```

**فیلدهای کلیدی:** `matcher` (pattern برای match کردن نام tool)، `hooks` (array تعریف hookها)، `type` (command/prompt/http/mcp_tool/agent)، `command`، `timeout`، `once`، `async`، `asyncRewake`، `shell`، `statusMessage`، `onFailure`.

> **یادداشت**: برخی eventها default timeout پایین‌تری دارند. `UserPromptSubmit` default command/http/mcp_tool را به 30 ثانیه کاهش می‌دهد و `MessageDisplay` به 10 ثانیه. hookهای `SessionEnd` budget 1.5 ثانیه‌ای share می‌کنند.

## Matcher Patterns

patternهای مختلف برای match کردن نام toolها پشتیبانی می‌شوند (`"Write"`، `"Edit|Write"`، `"*"`). برای جزئیات exact به فایل اصلی `06-hooks/README.md` مراجعه کنید.

## Hook Types

- **command**: اجرای shell command
- **prompt**: evaluation مبتنی بر LLM
- **http**: webhook خارجی
- **mcp_tool**: invocation ابزار MCP (v2.1.118+)
- **agent**: subagent evaluation

## Hook Events

eventهای مختلفی پشتیبانی می‌شوند (PreToolUse، PostToolUse، UserPromptSubmit، Stop، SessionStart، SessionEnd، MessageDisplay و ...). برای لیست کامل و payloadها به فایل اصلی مراجعه کنید.

## Examples

فایل اصلی چند example ارائه می‌دهد (auto-format، security scanner، prompt validator، context tracker، ...). برای کد کامل به `06-hooks/README.md` مراجعه کنید.

## Best Practices

- hookها را focused و سریع نگه دارید.
- از `async` برای عملیات طولانی استفاده کنید.
- timeoutها را مناسب تنظیم کنید.
- JSON output را validate کنید.

## Additional Resources

- [Official Hooks Documentation](https://code.claude.com/docs/en/hooks)
- [Skills Guide](../03-skills/)
- [MCP Guide](../05-mcp/)

---

**Last Updated**: October 18, 2026
**Claude Code Version**: 2.1.302

*Part of the [Claude How To](../) guide series*
