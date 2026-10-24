import os

fa_dir = r"D:\Project\claude-howto\fa"

content = """<picture>
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
"""

with open(os.path.join(fa_dir, "QUICK_REFERENCE.md"), "w", encoding="utf-8") as f:
    f.write(content)

print("QUICK_REFERENCE.md part 1 written!")