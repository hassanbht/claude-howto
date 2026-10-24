import os

fa_dir = r"D:\Project\claude-howto\fa"

content = """

### ویژگی‌های پیشرفته

```bash
# در تنظیمات پیکربندی شود (.claude/settings.json)
# به 09-advanced-features/config-examples.json مراجعه کنید

# حالت برنامه‌ریزی
/plan توضیح وظیفه

# حالت‌های مجاز (از --permission-mode استفاده شود)
# default          - عملیات خطرناک نیاز به تایید دارند
# acceptEdits      - به صورت خودکار ویرایش فایل‌ها را می‌پذیرد، سایر عملیات همچنان نیاز به تایید دارند
# plan             - فقط تحلیل خواندنی، بدون تغییر
# dontAsk          - فقط ابزارهای تایید شده قبلاً اجرا می‌شوند، بقیه رد می‌شوند
# auto             - کار classifying پس‌زمینه هر مراحلpermission را تصمیم می‌گیرد
# bypassPermissions - همه چیز پذیرفته می‌شود (--permission-mode bypassPermissions؛ --dangerously-skip-permissions معادل است)

# مدیریت peril.session
/resume                # بازگشت به peril.session قبلی
/rename "name"         # نامگذاری peril.session فعلی
/fork                  # Schippe peril.session فعلی
claude -c              # ادامه peril.session اخیر
claude -r "session"    # بازگشت peril.session با نام/شناسه
```

---

## 📋 مروری بر قابلیت‌ها

| قابلیت | مسیر نصب | نحوه استفاده |
|--------|----------|--------------|
| **دستورات Slash (۵۵+)** | `.claude/commands/*.md` | `/command-name` |
| **حافظه** | `./CLAUDE.md` | بارگذاری خودکار |
| **مهارت‌ها** | `.claude/skills/*/SKILL.md` | فعال‌سازی خودکار |
| **Subagentها** | `.claude/agents/*.md` | تفویض خودکار |
| **MCP** | `.mcp.json` (پروژه) یا `~/.claude.json` (کاربر) | `/mcp__server__action` |
| **هوک‌ها (۳۳ رویداد)** | `~/.claude/hooks/*.sh` | Event-trigger (۵ نوع) |
| **پلاquinها** | از طریق `/plugin install` | بسته‌بندی همه قابلیت‌ها |
| **Checkpoints** | درون‌ساخت | `Esc+Esc` یا `/rewind` |
| **حالت برنامه‌ریزی** | درون‌ساخت | `/plan <task>` |
| **حالت‌های مجاز (۶ نوع)** | درون‌ساخت | `--allowedTools`، `--permission-mode` |
| **peril.sessionها** | درون‌ساخت | `/resume`، `/rename`، `/branch`، `/fork` |
| **وظایف پس‌زمینه** | درون‌ساخت | در پس‌زمینه اجرا |
| **کنترل از راه دور** | درون‌ساخت | `claude --remote-control` یا `/remote-control` |
| **peril.sessionهای وب** | درون‌ساخت | در ترمینال با `claude --cloud "task"` |
| **Git Worktrees** | درون‌ساخت | `claude -w <name>` |
| **حافظه خودکار** | درون‌ساخت | ذخیره خودکار در `~/.claude/projects/<project>/memory/` |
| **لیست وظایف** | درون‌ساخت | `Ctrl+T` (لیست)،`/tasks` (کارهای پس‌زمینه) |
| **مهارت‌های داخلی (۵ عدد)** | درون‌ساخت | `/simplify`、`/loop`、`/claude-api`、`/voice`、`/browse` |
"""

with open(os.path.join(fa_dir, "QUICK_REFERENCE.md"), "a", encoding="utf-8") as f:
    f.write(content)

print("QUICK_REFERENCE.md part 2 written!")