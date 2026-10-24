<picture>
  <source media="(prefers-color-scheme: dark)" srcset="resources/logos/claude-howto-logo-dark.svg">
  <img alt="Claude How To" src="resources/logos/claude-howto-logo.svg">
</picture>

# کد کلود چگونه - کارت مرجع سریع

## 🚀 دستورات نصب سریع

### Slash Commands
```bash
# نصب همه
cp 01-slash-commands/*.md .claude/commands/

# نصب خاص
cp 01-slash-commands/optimize.md .claude/commands/
```

### Memory
```bash
# Project memory
cp 02-memory/project-CLAUDE.md ./CLAUDE.md

# Personal memory
cp 02-memory/personal-CLAUDE.md ~/.claude/CLAUDE.md
```

### Skills
```bash
# Personal skills
cp -r 03-skills/code-review-specialist ~/.claude/skills/

# Project skills
cp -r 03-skills/code-review-specialist .claude/skills/
```

### Subagents
```bash
# نصب همه
cp 04-subagents/*.md .claude/agents/

# نصب خاص
cp 04-subagents/code-reviewer.md .claude/agents/
```

### MCP
```bash
# تنظیم credentials
export GITHUB_PERSONAL_ACCESS_TOKEN="your_token"
export DATABASE_URL="postgresql://..."

# نصب config (project scope)
cp 05-mcp/github-mcp.json .mcp.json

# یا user scope: اضافه به ~/.claude.json
```

### Hooks
```bash
# نصب hookها
mkdir -p ~/.claude/hooks
cp 06-hooks/*.sh ~/.claude/hooks/
chmod +x ~/.claude/hooks/*.sh

# پیکربندی در settings (~/.claude/settings.json)
```

### Plugins
```bash
# نصب از مثال‌ها (اگر published)
claude --plugin-dir ./07-plugins/pr-review
/plugin install devops-automation
/plugin install documentation
```

### Checkpoints
```bash
# Checkpointها به‌طور خودکار با هر user prompt ایجاد می‌شوند
# برای rewind، دو بار Esc را بزنید یا استفاده کنید:
/rewind

# سپس انتخاب کنید: Restore code and conversation، Restore conversation،
# Restore code، Summarize from here، یا Never mind
```

### Advanced Features
```bash
# پیکربندی در settings (.claude/settings.json)
# 09-advanced-features/config-examples.json را ببینید

# Planning mode
/plan Task description

# Permission modes (استفاده از flag --permission-mode)
## 📊 Feature Matrix

| نیاز | استفاده از این | مثال |
|------|----------|---------|
| Quick shortcut | Slash Command (60+) | `01-slash-commands/optimize.md` |
| Team standards | Memory | `02-memory/project-CLAUDE.md` |
| Auto workflow | Skill | `03-skills/code-review-specialist/` |
| Specialized task | Subagent | `04-subagents/code-reviewer.md` |
| External data | MCP (+ Elicitation) | `05-mcp/github-mcp.json` |
| Event automation | Hook (33 events, 5 types) | `06-hooks/pre-commit.sh` |
| Complete solution | Plugin (+ LSP support) | `07-plugins/pr-review/` |
| Safe experiment | Checkpoint | `08-checkpoints/checkpoint-examples.md` |
| Fully autonomous | Auto Mode | `--permission-mode auto` or `Shift+Tab` |
| Chat integrations | Channels | `--channels` (Discord, Telegram) |
| CI/CD pipeline | CLI | `10-cli/README.md` |

---

## 🔗 Quick Links

- **Main Guide**: `README.md`
- **Complete Index**: `INDEX.md`
- **Original Guide**: `claude_concepts_guide.md`

---

## 📞 Common Questions

**Q: Which should I use?**
A: Start with slash commands، add features as needed.

**Q: Can I mix features?**
A: Yes! They work together. Memory + Commands + MCP = powerful.

**Q: How do I share with team?**
A: Commit `.claude/` directory to git.

**Q: What about secrets?**
A: Use environment variables، never hardcode.

**Q: Can I modify examples?**
A: Absolutely! They're templates to customize.

---

## ✅ Checklist

Getting started checklist:

- [ ] Read `README.md`
- [ ] Install 1 slash command
- [ ] Try the command
- [ ] Create project `CLAUDE.md`
- [ ] Install 1 subagent
- [ ] Set up 1 MCP integration
- [ ] Install 1 skill
- [ ] Try a complete plugin
- [ ] Customize for your needs
- [ ] Share with team

---

**Quick Start**: `cat README.md`

**Full Index**: `cat INDEX.md`

**This Card**: Keep it handy for quick reference!

---

**Last Updated**: October 18, 2026
**Claude Code Version**: 2.1.302
**Sources**:
- https://code.claude.com/docs/en/workflows#set-a-size-guideline
- https://code.claude.com/docs/en/memory#agents-md
- https://code.claude.com/docs/en/changelog
- https://code.claude.com/docs/en/cli-reference
- https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md
- https://code.claude.com/docs/en/sub-agents
- https://code.claude.com/docs/en/model-config
- https://code.claude.com/docs/en/settings
- https://code.claude.com/docs/en/hooks
- https://code.claude.com/docs/en/env-vars
- https://code.claude.com/docs/en/commands
- https://code.claude.com/docs/en/remote-control
- https://code.claude.com/docs/en/agent-teams
- https://code.claude.com/docs/en/memory#storage-location
- https://code.claude.com/docs/en/permission-modes
- https://code.claude.com/docs/en/managed-settings
- https://code.claude.com/docs/en/scheduled-tasks
- https://code.claude.com/docs/en/code-review-local
**Compatible Models**: Claude Fable 5.1, Claude Fable 5, Claude Opus 5, Claude Sonnet 5, Claude Sonnet 4.6, Claude Opus 4.8, Claude Haiku 4.5

# manual         - تأیید برای هر action (config value "default"; "manual" alias آن از v2.1.200)
# acceptEdits    - auto-accept file edits، سؤال برای بقیه
# plan           - تحلیل فقط خواندنی، بدون تغییر
# auto           - classifier background به‌طور خودکار permissionها را تصمیم می‌گیرد
# dontAsk        - فقط ابزارهای pre-approved اجرا می‌شوند؛ بقیه deny
# bypassPermissions - پذیرش همه actions (--permission-mode bypassPermissions; --dangerously-skip-permissions معادل است)

# مدیریت session
/resume                # resume مکالمه قبلی (بدون args = picker sessionهای گذشته)
/rename "name"         # نامگذاری session فعلی
/fork [prompt]         # کپی مکالمه به session background جدید؛ اینجا کار ادامه می‌یابد
/subtask <task>        # spawn یک subagent forked که مکالمه را inherit می‌کند و گزارش می‌دهد
/branch [name]         # switch به کپی مکالمه، حفظ original
claude -c              # ادامه جدیدترین مکالمه
claude -r "session"    # resume session با نام/ID
```

---

## 📋 Feature Cheat Sheet

| ویژگی | مسیر نصب | استفاده |
|---------|-------------|-------|
| **Slash Commands (60+)** | `.claude/commands/*.md` | `/command-name` |
| **Memory** | `./CLAUDE.md` | Auto-loaded |
| **Skills** | `.claude/skills/*/SKILL.md` | Auto-invoked |
| **Subagents** | `.claude/agents/*.md` | Auto-delegated |
| **MCP** | `.mcp.json` | Transparent tools |
| **Hooks** | `~/.claude/settings.json` | Event-triggered |
| **Plugins** | Installed via `/plugin` | Bundled features |
| **Checkpoints** | Auto-created | `Esc+Esc` یا `/rewind` |
| **Planning** | `/plan` command | `/plan <task>` |
| **Permission Modes** | `--permission-mode` flag | manual, acceptEdits, plan, auto, dontAsk, bypassPermissions |
| **Sessions** | `/resume`, `/rename`, `/fork` | مدیریت مکالمه |
| **Background Tasks** | `Ctrl+B` | Long-running commands |
| **Remote Control** | `/remote-control` | کنترل از راه دور |
| **Web Sessions** | `claude web` | Browser-based |
| **Auto Mode** | `--permission-mode auto` | Fully autonomous |
| **Channels** | `--channels` | Discord، Telegram، iMessage |
| **Voice Dictation** | `/voice` | Speech-to-text input |
| **Agent Teams** | `/team-onboarding` | مدیریت تیم |

---

## 📝 Common Patterns

### Pattern 1: Simple Command
```
User: /optimize
Claude: Analyzes code for performance issues
```

### Pattern 2: Command with Arguments
```
User: /pr 123
Claude: Reviews PR #123
```

### Pattern 3: Command Composition
```
User: /optimize then /pr
Claude: Optimizes code, then creates PR
```

### Pattern 4: Memory + Commands
```
User: /review (with CLAUDE.md context)
Claude: Reviews using project standards
```

### Pattern 5: Multi-tool Workflow
```
User: "Review code, run tests, create PR"
Claude: Uses subagent + bash + GitHub MCP
```

---

## 🔧 Troubleshooting Quick Fixes

| Issue | Solution |
|-------|----------|
| Command not found | Check `.claude/commands/` path |
| Permission denied | `chmod +x script.sh` |
| MCP not connecting | Check env vars |
| Memory not loading | Verify `CLAUDE.md` location |
| Skill not triggering | Check `SKILL.md` exists |
| Hook not firing | Check settings.json syntax |

---

## 💡 Pro Tips

1. **Start small**: با یک command شروع کنید
2. **Add incrementally**: ویژگی‌ها را به تدریج اضافه کنید
3. **Use memory**: برای استانداردهای تیم
4. **Automate**: از hookها برای automation
5. **Delegate**: از subagentها برای taskهای پیچیده
6. **Test safely**: از checkpointها برای آزمایش
7. **Monitor usage**: `/usage` را برای هزینه‌ها چک کنید
8. **Customize**: همه چیز قابل سفارشی‌سازی است

---
