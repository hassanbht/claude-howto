<picture>
  <source media="(prefers-color-scheme: dark)" srcset="resources/logos/claude-howto-logo-dark.svg">
  <img alt="Claude How To" src="resources/logos/claude-howto-logo.svg">
</picture>

# 📚 مسیر یادگیری کد کلود

**جدید در کد کلود؟** این راهنما به شما کمک می‌کند ویژگی‌های کد کلود را با سرعت خود مسلط شوید. چه یک مبتدی کامل باشید چه یک developer با تجربه، با quiz self-assessment زیر شروع کنید تا مسیر مناسب برای خود را پیدا کنید.

---

## 🧭 یافتن سطح خود

همه از یک جا شروع نمی‌کنند. این self-assessment سریع را بگیرید تا entry point مناسب را پیدا کنید.

**به این سؤالات به‌طور صادقانه پاسخ دهید:**

- [ ] می‌توانم کد کلود را شروع کنم و یک مکالمه داشته باشم (`claude`)
- [ ] یک فایل CLAUDE.md ایجاد یا ویرایش کرده‌ام
- [ ] حداقل 3 slash command داخلی استفاده کرده‌ام (مثلاً /help، /compact، /model)
- [ ] یک slash command یا skill سفارشی (SKILL.md) ایجاد کرده‌ام
- [ ] یک سرور MCP پیکربندی کرده‌ام (مثلاً GitHub، database)
- [ ] hookها را در ~/.claude/settings.json تنظیم کرده‌ام
- [ ] subagentهای سفارشی (.claude/agents/) ایجاد یا استفاده کرده‌ام
- [ ] از print mode (`claude -p`) برای scripting یا CI/CD استفاده کرده‌ام

**سطح شما:**

| Checks | سطح | شروع از | زمان تکمیل |
|--------|-------|----------|------------------|
| 0-2 | **Level 1: Beginner** — Getting Started | [Milestone 1A](#milestone-1a-first-commands--memory) | ~3 ساعت |
| 3-5 | **Level 2: Intermediate** — Building Workflows | [Milestone 2A](#milestone-2a-automation-skills--hooks) | ~5 ساعت |
| 6-8 | **Level 3: Advanced** — Power User & Team Lead | [Milestone 3A](#milestone-3a-advanced-features) | ~5 ساعت |

> **Tip**: اگر مطمئن نیستید، یک سطح پایین‌تر شروع کنید. بهتر است متریال آشنا را سریع review کنید تا مفاهیم foundational را از دست بدهید.

> **نسخه تعاملی**: `/self-assessment` را در کد کلود اجرا کنید برای یک quiz هدایت‌شده تعاملی که proficiency شما را در همه ۱۰ حوزه ویژگی امتیازدهی می‌کند و یک مسیر یادگیری personalized تولید می‌کند.

---

## 🎯 فلسفه یادگیری

پوشه‌های این repository به **ترتیب یادگیری توصیه‌شده** شماره‌گذاری شده‌اند بر اساس سه اصل کلیدی:

1. **Dependencies** - مفاهیم foundational اول می‌آیند
2. **Complexity** - ویژگی‌های آسان قبل از پیشرفته
3. **Frequency of Use** - رایج‌ترین ویژگی‌ها زودتر آموزش داده می‌شوند

این رویکرد اطمینان می‌دهد که یک foundation جامد می‌سازید در حالی که فوراً مزایای بهره‌وری به دست می‌آورید.

---

## 🗺️ مسیر یادگیری شما

```mermaid
graph TD
    Q["🧭 Self-Assessment Quiz<br/>Find Your Level"] --> L1
    Q --> L2
    Q --> L3
## 🎯 Milestoneها

### Level 1: Beginner — Getting Started (~3 ساعت)

#### Milestone 1A: First Commands & Memory
- **ماژول‌ها**: `01-slash-commands`، `02-memory`
- **یاد می‌گیرید**: slash commandها، CLAUDE.md، memory persistence
- **تمرین**: یک slash command نصب کنید، یک CLAUDE.md بسازید
- **پیش‌نیاز**: هیچ

#### Milestone 1B: Safe Exploration
- **ماژول‌ها**: `08-checkpoints`، `10-cli` (basics)
- **یاد می‌گیرید**: checkpointها، CLI basics، rewind
- **تمرین**: از checkpoint برای آزمایش امن استفاده کنید
- **پیش‌نیاز**: Milestone 1A

### Level 2: Intermediate — Building Workflows (~5 ساعت)

#### Milestone 2A: Automation (Skills + Hooks)
- **ماژول‌ها**: `03-skills`، `06-hooks`
- **یاد می‌گیرید**: skillها، hookها، event-driven automation
- **تمرین**: یک skill نصب کنید، یک hook تنظیم کنید
- **پیش‌نیاز**: Level 1

#### Milestone 2B: Integration (MCP + Subagents)
- **ماژول‌ها**: `05-mcp`، `04-subagents`
- **یاد می‌گیرید**: سرورهای MCP، subagentها، delegation
- **تمرین**: یک MCP server پیکربندی کنید، یک subagent استفاده کنید
- **پیش‌نیاز**: Milestone 2A

### Level 3: Advanced — Power User (~5 ساعت)

#### Milestone 3A: Advanced Features
- **ماژول‌ها**: `09-advanced-features`
- **یاد می‌گیرید**: planning mode، permission modes، background tasks
- **تمرین**: از planning mode و auto mode استفاده کنید
- **پیش‌نیاز**: Level 2

#### Milestone 3B: Team & Distribution
- **ماژول‌ها**: `07-plugins`، `10-cli` (advanced)
- **یاد می‌گیرید**: pluginها، CLI mastery، توزیع تیمی
- **تمرین**: یک plugin نصب کنید، تنظیمات تیم را به اشتراک بگذارید
- **پیش‌نیاز**: Milestone 3A

---

## 🎯 پس از تکمیل چه کنیم؟

پس از تکمیل همه milestoneها:

1. **مستندات تیم ایجاد کنید** - تنظیمات Claude Code تیم خود را مستند کنید
2. **پلاگین‌های سفارشی بسازید** - workflowهای تیم خود را package کنید، شامل manifest fieldهای جدیدتر (`workflows`، `channels`، `dependencies`)
3. **`/design` را امتحان کنید** - یک mockup UI، screen flow یا landing page را روی design canvas طراحی کنید به جای نوشتن دستی HTML (v2.1.265+)
4. **Remote Control را کاوش کنید** - یک session محلی Claude Code را از phone، browser یا app Claude ادامه دهید، یا از phone از طریق device card در app Claude شروع کنید
5. **Web Sessions را استفاده کنید** - Claude Code را از طریق interfaceهای browser-based برای remote development استفاده کنید
6. **Desktop App را استفاده کنید** - به ویژگی‌های Claude Code از طریق application دسکتاپ native دسترسی داشته باشید
7. **Auto Mode را استفاده کنید** - بگذارید Claude به‌طور autonomous با یک safety classifier background کار کند
8. **Auto Memory را leverage کنید** - بگذارید Claude preferences شما را به‌طور خودکار در طول زمان یاد بگیرد
9. **Agent Teams را تنظیم کنید** - چند ایجنت را روی taskهای پیچیده و چندوجهی coordinate کنید
10. **Channels را استفاده کنید** - یک MCP server متصل کنید که eventها (CI results، chat messages، webhooks) را به session در حال اجرا push می‌کند
11. **Voice Dictation را امتحان کنید** - ورودی voice hands-free برای تعامل با Claude Code
12. **Scheduled Tasks را استفاده کنید** - چک‌های recurring را با `/loop` و cron tools automate کنید
13. **مثال‌ها را contribute کنید** - با community به اشتراک بگذارید
14. **دیگران را mentor کنید** - به teammates یاد بدهید
15. **workflowها را optimize کنید** - به‌طور مداوم بر اساس استفاده بهبود دهید
16. **به‌روز بمانید** - Claude Code releases و ویژگی‌های جدید را دنبال کنید

---

## 📚 منابع اضافی

### مستندات رسمی
- [Claude Code Documentation](https://code.claude.com/docs/en/overview)
- [Anthropic Documentation](https://docs.anthropic.com)
- [MCP Protocol Specification](https://modelcontextprotocol.io)

### Blog Posts
- [Discovering Claude Code Slash Commands](https://medium.com/@luongnv89/discovering-claude-code-slash-commands-cdc17f0dfb29)

### Community
- [Anthropic Cookbook](https://github.com/anthropics/anthropic-cookbook)
- [MCP Servers Repository](https://github.com/modelcontextprotocol/servers)

---

## 💬 Feedback & Support

- **issue یافتید؟** در repository یک issue ایجاد کنید
- **پیشنهاد دارید؟** یک pull request submit کنید
- **نیاز به کمک؟** مستندات را چک کنید یا از community بپرسید

---

**آخرین به‌روزرسانی**: October 18, 2026
**نسخه کد کلود**: 2.1.302
**منابع**:
- https://code.claude.com/docs/en/overview
- https://code.claude.com/docs/en/hooks
- https://code.claude.com/docs/en/permission-modes
- https://github.com/anthropics/claude-code/releases/tag/v2.1.144
- https://github.com/anthropics/claude-code/releases/tag/v2.1.145
- https://code.claude.com/docs/en/model-config
- https://code.claude.com/docs/en/agent-teams
- https://code.claude.com/docs/en/mcp
- https://code.claude.com/docs/en/plugins/install
- https://code.claude.com/docs/en/channels
- https://code.claude.com/docs/en/remote-control
- https://code.claude.com/docs/en/scheduled-tasks
- https://code.claude.com/docs/en/commands
- https://code.claude.com/docs/en/sub-agents
**مدل‌های سازگار**: Claude Fable 5.1, Claude Fable 5, Claude Opus 5, Claude Sonnet 5, Claude Sonnet 4.6, Claude Opus 4.8, Claude Haiku 4.5
**Maintained by**: Claude How-To Contributors
**مجوز**: Educational purposes, free to use and adapt

---

[← بازگشت به README اصلی](README.md)


    subgraph L1["🟢 Level 1: Beginner — Getting Started"]
        direction LR
        A["1A: First Commands & Memory<br/>Slash Commands + Memory"] --> B["1B: Safe Exploration<br/>Checkpoints + CLI Basics"]
    end

    subgraph L2["🔵 Level 2: Intermediate — Building Workflows"]
        direction LR
        C["2A: Automation<br/>Skills + Hooks"] --> D["2B: Integration<br/>MCP + Subagents"]
    end

    subgraph L3["🔴 Level 3: Advanced — Power User"]
        direction LR
        E["3A: Advanced Features<br/>Planning + Permissions"] --> F["3B: Team & Distribution<br/>Plugins + CLI Mastery"]
    end

    L1 --> L2
    L2 --> L3

    style Q fill:#6A1B9A,color:#fff,stroke:#9C27B0,stroke-width:2px
    style A fill:#2E7D32,color:#fff
    style B fill:#2E7D32,color:#fff
    style C fill:#1565C0,color:#fff
    style D fill:#F57C00,color:#fff
    style E fill:#C62828,color:#fff
    style F fill:#B71C1C,color:#fff
```

**راهنمای رنگ:**
- 💜 Purple = شروع (self-assessment)
- 💚 Green = Level 1 (Beginner)
- 💙 Blue = Level 2 (Intermediate)
- 🔴 Red = Level 3 (Advanced)

---
