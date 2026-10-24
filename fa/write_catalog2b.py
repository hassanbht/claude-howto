import os

fa_dir = r"D:\Project\claude-howto\fa"

content = """

## ویژگی‌های جدید (مارس ۲۰۲۶)

### ویژگی‌های جدید

| ویژگی | توضیح | نحوه فعال‌سازی |
|---------|-------------|-------------|
| **حالت خودکار (Auto Mode)** | اجرا خود pilote با بررسی后台 Sicherheits catégorie | `Shift+Tab` و یا `--permission-mode auto` |
| **کانال‌ها (Channels)** | ارتباط چندکانال (Telegram، Slack و غیره) (Research Preview) | پیکربندی channel plugins؛ Mars ۲۰۲۶ |
| **ورودی صوتی (Voice Dictation)** | وارد کردن پرامپت با صدای | آیکون میکروفون یا میانبر sound |
| **نوع هوک Agent** | هوکی که subagent را اجرا می‌کند نه دستور shell | در پیکربندی هوک `"type": "agent"` |
| **نوع هوک Prompt** | ارسال prompt به مدل Claude برای ارزیابی یکمرحله‌ای، مدل در پاسخ JSON تصمیم می‌گیرد | در پیکربندی هوک `"type": "prompt"` |
| **MCP Elicitation** | سرورهای MCP می‌توانند در طول اجرای ابزار از کاربر ورودی بگیرند | از طریق رویدادهای胡ک `Elicitation` و `ElicitationResult` |
| **WebSocket MCP Transport** | اتصال به سرور MCP از طریق WebSocket | در پیکربندی سرور MCP `"transport": "websocket"` |
| **پشتیبانی LSP پلاquin** | یکپارچگی زبان سیلور Protokol (LSP) از طریق پلاquinها | در `plugin.json` LSP servers را پیکربندی کنید |
| **Drop-ins مدیریت شده** | پیکربندی drop-in مدیریت شده توسط سازمان (v2.1.83) | توسط quản trị viên از طریق managed policies، به طور خودکار برای همه کاربران اعمال می‌شود |

---

## ماتریس مرجع سریع

### راهنمای انتخاب قابلیت

| نیاز | قابلیت پیشنهادی | دلیل |
|------|---------------------|-----|
| دستور سریع | Slash Command | دستی، اجرا فوری |
| contexte پایدار | Memory | بارگذاری خودکار |
| اتوماسیون پیچیده | Skill | فعال‌سازی خودکار |
| وظیفه تخصصی | Subagent | ایزولاسیون contexte |
| داده خارجی | MCP Server | دسترسی در زمان واقعی |
| اتوماسیون رویداد | Hook | Event-trigger |
| راه حل کامل | Plugin | بسته‌بندی یکپارچه |

### اولویت نصب

| اولویت | قابلیت | دستور |
|----------|---------|---------|
| 1. essential | Memory | `cp 02-memory/project-CLAUDE.md ./CLAUDE.md` |
| 2. daily | Slash Commands | `cp 01-slash-commands/*.md .claude/commands/` |
| 3. quality | Subagents | `cp 04-subagents/*.md .claude/agents/` |
| 4. automation | Hooks | `cp 06-hooks/*.sh ~/.claude/hooks/` |
| 5. integration | MCP Servers | `claude mcp add github -- npx -y @modelcontextprotocol/server-github` |
| 6. full package | Plugins | `/plugin install <name>` |

---

## نصب با یک دستور

```bash
# ایجاد دایرکتوری‌ها
mkdir -p .claude/commands .claude/agents ~/.claude/hooks ~/.claude/skills

# نصب همه قابلیت‌ها
cp 01-slash-commands/*.md .claude/commands/
cp 04-subagents/*.md .claude/agents/
cp -r 03-skills/* ~/.claude/skills/
cp 06-hooks/*.sh ~/.claude/hooks/
chmod +x ~/.claude/hooks/*.sh

# پیکربندی MCP
export GITHUB_TOKEN="your_token"
claude mcp add github -- npx -y @modelcontextprotocol/server-github

# استفاده از پلاquinها
claude --plugin-dir ./07-plugins/pr-review
/plugin install devops-automation
```

---

## منابع دیگر

- [مستندات کلود کد](https://code.claude.com/docs/en/overview)
- [مقدمه پروتکل MCP](https://modelcontextprotocol.io)
- [مخزن مهارت‌ها](https://github.com/luongnv89/skills) - مجموعه مهارت‌های آماده برای استفاده
- [Anthropic Cookbook](https://github.com/anthropics/anthropic-cookbook)
- [گ گردش کار باور شرنی کلود کد](https://x.com/bcherny/status/2007179832300581177) - ساختار کلود کد گردش کار سازمانی خود را به اشتراک گذاشته است: subagentها در کار موازی، `CLAUDE.md` مشترک، حالت Plan، دستورات slash، subagentها، و胡کهای اعتبارسنجی برای peril.sessionهای自立 طولانی مدت.

---

**آخرین به‌روزرسانی**: ۱۸ آبان ۲۰۲۶
**نسخه کلود کد**: ۲.۱.۳۰۲
**منبع**:
- https://code.claude.com/docs/en/tools-reference#task-tool-availability
- https://code.claude.com/docs/en/commands
- https://code.claude.com/docs/en/hooks
- https://code.claude.com/docs/en/plugins-reference
- https://code.claude.com/docs/en/discover-plugins
- https://code.claude.com/docs/en/sub-agents
- https://code.claude.com/docs/en/permission-modes
- https://code.claude.com/docs/en/cli-reference
- https://code.claude.com/docs/en/skills
- https://code.claude.com/docs/en/mcp
- https://code.claude.com/docs/en/chrome
- https://code.claude.com/docs/en/plugins/manifest-reference
- https://code.claude.com/docs/en/plugins/cli-reference
"""
with open(os.path.join(fa_dir, "CATALOG.md"), "a", encoding="utf-8") as f:
    f.write(content)

print("CATALOG.md part 2b written!")