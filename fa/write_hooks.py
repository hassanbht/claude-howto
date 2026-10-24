import os

fa_dir = r"D:\Project\claude-howto\fa"

content = """<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../../resources/logos/claude-howto-logo-dark.svg">
  <img alt="Claude How To" src="../../resources/logos/claude-howto-logo.svg">
</picture>

# مرجع胡ک‌ها

胡ک‌ها دستورات شل هستند که در رخ دادن رویدادهای Claude Code به صورت خودکار اجرا می‌شوند، برای اتوماسیون کارهایی مانند فرمت화، اعتبارسنجی، اعلان، بررسی امنیتی و غیره.

## مروری کلی

胡ک‌ها یک مکانیزم اتوماسیون مبتنی بر رویداد هستند. آن‌ها در زمان انجام برخی اقدامات در Claude Code به صورت خودکار اجرا می‌شوند، بدون نیاز به فعال‌سازی دستی شما.

استفاده‌های رایج:

- فرمت화 خودکار قبل از نوشتن فایل
- اجرای تست قبل از commit
- اسکن مسائل امنیتی
- ثبت دستورات Bash
- اعتبارسنجی پرامپت کاربر
- ارسال اعلان به تیم

## انواع胡ک

Claude Code ۳۳ رویداد胡ک را پشتیبانی می‌کند، به چهار گروه بر اساس کاربرد تقسیم شده‌اند. ۵ نوع handler وجود دارد: `command`، `http`، `mcp_tool`، `prompt`، `agent`.

- **胡ک ابزارها**: `PreToolUse`، `PostToolUse`، `PostToolUseFailure`، `PostToolBatch`، `PermissionRequest`، `PermissionDenied`
- **胡ک جلسه**: `SessionStart`، `Setup`، `SessionEnd`، `Stop`، `StopFailure`، `SubagentStart`، `SubagentStop`
- **胡ک وظیفه**: `UserPromptSubmit`، `UserPromptExpansion`، `MessageDisplay`، `TaskCompleted`، `TaskCreated`، `TeammateIdle` (`TaskCompleted` و `TaskCreated` فقط وقتی ابزار todo فعال است اجرا می‌شوند — به طور پیش‌فرض فقط در مدل‌های Claude 3.x، Opus ۴ تا ۴.۷، Sonnet ۴ تا ۴.۶ و Haiku ۴.۵ در دسترس است؛ `CLAUDE_CODE_ENABLE_TODO_TOOLS=1` می‌تواند آن را بازیابی کند)
- **胡ک چرخه عمر**: `ConfigChange`، `CwdChanged`، `DirectoryAdded`، `FileChanged`، `PreCompact`، `PostCompact`، `PreModelSwitch`، `PostModelSwitch`، `WorktreeCreate`، `WorktreeRemove`، `Notification`، `InstructionsLoaded`، `Elicitation`، `ElicitationResult`

## نصب

```bash
mkdir -p ~/.claude/hooks
cp 06-hooks/*.sh ~/.claude/hooks/
chmod +x ~/.claude/hooks/*.sh
```

سپس در `~/.claude/settings.json` پیکربندی کنید:

```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Write",
        "hooks": [
          {
            "type": "command",
            "command": "~/.claude/hooks/format-code.sh"
          }
        ]
      }
    ],
    "PostToolUse": [
      {
        "matcher": "Write",
        "hooks": [
          {
            "type": "command",
            "command": "~/.claude/hooks/security-scan.sh"
          }
        ]
      }
    ]
  }
}
```

## استفاده

胡ک‌ها وقتی رویداد مطابق پیدا می‌شود، به صورت خودکار اجرا می‌شوند. می‌توانید آن‌ها را به عنوان 콜بک رویداد Claude Code در نظر بگیرید.

## مثال‌های رایج

- `format-code.sh` - فرمت화 خودکار قبل از نوشتن
- `pre-commit.sh` - اجرای تست قبل از commit
- `security-scan.sh` - انجام اسکن امنیتی
- `log-bash.sh` - ثبت دستورات Bash
- `validate-prompt.sh` - اعتبارسنجی ورودی
- `notify-team.sh` - ارسال اعلان

## بهترین شیوه‌ها

-胡ک‌ها را کوتاه و مشخص نگه دارید
- فقط مسئولیت واحد انجام دهید
- ابتدا در محیط محلی تست کنید
- منطق تجاری پیچیده را در胡ک قرار ندهید
- در مورد اثرات جانبی مراقب باشید

## عیب‌یابی

- مسیر فایل و مجوزها را بررسی کنید
- تأیید کنید اسکریپت قابل اجرا است
- نحوی settings.json را بررسی کنید
- سازگاری نسخه Claude Code را بررسی کنید

## مفاهیم مرتبط

- [Checkpoints و Rewind](../08-checkpoints/README.md)
- [دستورات Slash](../01-slash-commands/README.md)
- [مهارت‌ها](../03-skills/README.md)
- [Subagents](../04-subagents/README.md)
- [پلاگین‌ها](../07-plugins/README.md)
- [ویژگی‌های پیشرفته](../09-advanced-features/README.md)

## منابع بیشتر

- [راهنمای حافظه](../02-memory/README.md)
- [مستندات رسمی胡ک‌ها](https://code.claude.com/docs/en/hooks)
- [مرجع CLI](https://code.claude.com/docs/en/cli-reference)

---

**آخرین به‌روزرسانی**: ۱۹ شهریور ۲۰۲۶
**نسخه Claude Code**: ۲.۱.۲۷۸
**منبع**:
- https://code.claude.com/docs/en/hooks
- https://code.claude.com/docs/en/tools-reference#task-tool-availability
"""

with open(os.path.join(fa_dir, "06-hooks", "README.md"), "w", encoding="utf-8") as f:
    f.write(content)

print("06-hooks/README.md written!")