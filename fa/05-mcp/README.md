<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../resources/logos/claude-howto-logo-dark.svg">
  <img alt="Claude How To" src="../resources/logos/claude-howto-logo.svg">
</picture>

# MCP (Model Context Protocol)

این پوشه مستندات جامع و مثال‌ها برای configuration و استفاده MCP server با Claude Code را شامل می‌شود.

## مرور کلی

MCP (Model Context Protocol) راه standardized برای دسترسی Claude به toolهای خارجی، APIها و real-time data sourceها است. برخلاف Memory، MCP دسترسی live به داده‌های در حال تغییر فراهم می‌کند.

ویژگی‌های کلیدی:
- دسترسی real-time به serviceهای خارجی
- synchronization live داده
- architecture extensible
- authentication امن
- interactionهای tool-based

## MCP Architecture

Claude ↔ MCP Server ↔ External Service. requestها و responseها بین آن‌ها جریان دارند.

## MCP Ecosystem

Claude می‌تواند به چند MCP server (Filesystem، GitHub، Database، Slack، Google Docs) متصل شود که هر کدام به service پشتیبان خود متصل هستند.

## MCP Installation Methods

Claude Code چند transport protocol برای اتصال MCP server پشتیبانی می‌کند:

### HTTP Transport (Recommended)
```bash
# اتصال HTTP basic
claude mcp add --transport http notion https://mcp.notion.com/mcp

# HTTP با authentication header
claude mcp add --transport http secure-api https://api.example.com/mcp \
  --header "Authorization: Bearer your-token"
```

### Stdio Transport (Local)
برای MCP serverهای محلی:
```bash
# Local Node.js server
claude mcp add --transport stdio myserver -- npx @myorg/mcp-server

# با environment variables
claude mcp add --transport stdio myserver --env KEY=value -- npx server
```

### `CLAUDE_PROJECT_DIR` for stdio servers (v2.1.139+)
هر MCP stdio server با `CLAUDE_PROJECT_DIR=<absolute path to repo root>` در environment spawn می‌شود. plugin و project `.mcp.json`ها می‌توانند `${CLAUDE_PROJECT_DIR}` را در `command`، `args` و `env` reference کنند.

## MCP Tool Search (v2.1.145+)

برای کاهش context overhead، Claude Code از MCP tool search پشتیبانی می‌کند که toolها را به‌طور progressive load می‌کند. این token usage را به‌طور چشمگیری کاهش می‌دهد (مثال: از ~150,000 به ~2,000 token).

## Additional Resources

- [Official MCP Documentation](https://code.claude.com/docs/en/mcp)
- [MCP Specification](https://modelcontextprotocol.io)
- [Skills Guide](../03-skills/)
- [Subagents Guide](../04-subagents/)

---

**Last Updated**: October 18, 2026
**Claude Code Version**: 2.1.302

*Part of the [Claude How To](../) guide series*
