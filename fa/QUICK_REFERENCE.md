<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../resources/logos/claude-howto-logo-dark.svg">
  <img alt="Claude How To" src="../resources/logos/claude-howto-logo.svg">
</picture>

# کارت مرجع سریع کلود کد

## 🚀 نصب دستورات سریع

### دستورات Slash

```bash
# نصب همه
cp 01-slash-commands/*.md .claude/commands/

# نصب تک‌تایی
cp 01-slash-commands/optimize.md .claude/commands/
```

### حافظه (Memory)

```bash
# حافظه پروژه
cp 02-memory/project-CLAUDE.md ./CLAUDE.md

# حافظه شخصی
cp 02-memory/personal-CLAUDE.md ~/.claude/CLAUDE.md
```

### مهارت‌ها (Skills)

```bash
# مهارت‌های شخصی
cp -r 03-skills/code-review-specialist ~/.claude/skills/

# مهارت‌های پروژه‌ای
cp -r 03-skills/code-review-specialist .claude/skills/
```

### Subagentها

```bash
# نصب همه
cp 04-subagents/*.md .claude/agents/

# نصب تک‌تایی
cp 04-subagents/code-reviewer.md .claude/agents/
```

### MCP

```bash
# تنظیم اعتبارنامه‌ها
export GITHUB_PERSONAL_ACCESS_TOKEN="your_token"
export DATABASE_URL="postgresql://..."

# پیکربندی (سطح پروژه)
cp 05-mcp/github-mcp.json .mcp.json

# یا سطح کاربر: افزودن به ~/.claude.json
```

### هوک‌ها

```bash
# نصب هوک‌ها
mkdir -p ~/.claude/hooks
cp 06-hooks/*.sh ~/.claude/hooks/
chmod +x ~/.claude/hooks/*.sh

# در تنظیمات پیکربندی شود (~/.claude/settings.json)
```

### پلاquinها

```bash
# نصب از نمونه‌ها (اگر منتشر شده باشد)
claude --plugin-dir ./07-plugins/pr-review
/plugin install devops-automation
/plugin install documentation
```

### Checkpoints

```bash
# بعد از هر پرامپت کاربر به صورت خودکار checkpoint ساخته می‌شود
# بازگشت: دو بار Esc بزنید یا از دستور زیر استفاده کنید:
/rewind

# سپس یکی از موارد زیر را انتخاب کنید: بازگردانی کد و peril.session، بازگردانی peril.session،
# بازگردانی کد، از اینجا خلاصه کنید، یاolc 내려گذارید
```


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
| **مهارت‌های داخلی (۵ عدد)** | درون‌ساخت | `/simplify`، `/loop`، `/claude-api`، `/voice`، `/browse` |
