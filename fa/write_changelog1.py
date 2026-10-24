import os

fa_dir = r"D:\Project\claude-howto\fa"

content = """# ثبت تغییرات

## v2.3.0 — ۲۰۲۶-۰۴-۰۷

### ویژگی‌ها

- ساخت و انتشار翼 EPUB برای هر زبان (۹۰e9c۳۰) @Thiên Toán
- افزودن هوک pre-tool-check.sh به ۰۶-hookها (b511ed۱) @JiayuWang
- افزودن ترجمه چینی در دایرکتوری zh/ (۸۹e۸۹d۴) @Luong NGUYEN
- افزودن Subagent بهینه‌سازی عملکرد و هوک بررسی وابستگی (f53d۰۸۰) @qk

### رفع باگ

- سازگاری Git Bash ویندوز + پروتکل JSON stdin (۲cbb۱۰c) @Luong NGUYEN
- رفع tài liệu پیکربندی autoCheckpoint در ۰۸-checkpoint (۷۴۹c۷۹f) @JiayuWang
- جایگزینی جای گذار به جای embedded تصاویر SVG (۱b۱۶۷۰۹) @Thiên Toán
- رفع نمایش code block تو در تو در README حافظه (ce24۴۲۳) @Zhaoshan Duan
- بازبینی اصلاحات بررسی که توسط squash merge رد شدند (۳۴۲۵۹ca) @Luong NGUYEN
- سازگاری اسکریپت‌های هوک با Git Bash ویندوز و استفاده از پروتکل JSON stdin (۱۰۷۱۵۳d) @binyu li

### tài liệu

- همزمانی همه آموزش‌ها با مستندات جدیدترین Claude Code (اکتبر ۲۰۲۶) (۷۲d۳۰۱) @Luong NGUYEN
- افزودن لینک زبان چینی در 스위چر زبان (۶cbaa۴d) @Luong NGUYEN
- افزودن 스위چر زبان بین انگلیسی و ویتنامی (۱۰۰c۵۱e) @Luong NGUYEN
- افزودن نشان #۱ Trending GitHub (۰ca۸۳۷) @Luong NGUYEN
- معرفی cc-context-stats برای مانیتور링 منطقه زمینه (d41b۳۳۵) @Luong NGUYEN
- معرفی مجموعه luongnv89/skills و مدیر مهارت luongnv89/asm (۷e۳c۰۶) @Luong NGUYEN
- به‌روزرسانی آمار README برای بازتاب معیارهای فعلی GitHub (۵۹۰۰+ ستاره، ۶۹۰+ فورک) (۵۰۰۱۵۲۵) @Luong NGUYEN
- به‌روزرسانی آمار README برای بازتاب معیارهای فعلی GitHub (۳۹۰۰+ ستاره، ۴۶۰+ فورک) (۹cb۹۲d۶) @Luong NGUYEN

### بازسازی

- جایگزینی وابستگی HTTP Kroki با رندر محلی mmdc (e76bbee) @Luong NGUYEN
- انتقال بررسی کیفیت به pre-commit، CI به عنوان خط دوم دفاع (۶d۱e۰ae) @Luong NGUYEN
-縮 کوچک کردن خط م Bear alap مجوز حالت خودکار (۲۷۹۰fb۲) @Luong NGUYEN
- جایگزینی هوک تطابق خودکار با اسکریپت تنظیم مجوز یکباره (۹۹۵a۵۹۶) @Luong NGUYEN

### سایر

- جابجایی Key quality gates به phía trước — اضافه کردن mypy به pre-commit، رفع شکست CI (۶۹۹fb۹۱) @Luong NGUYEN
- افزودن محلی‌سازی ویتنامی (Tiếng Việt) (a۷۰۷۷۷e) @Thiên Toán

**ثبت تغییرات کامل**: https://github.com/luongnv89/claude-howto/compare/v2.2.0...v2.3.0

---

## v2.2.0 — ۲۰۲۶-۰۳-۲۶

### tài liệu

- به‌روزرسانی همه آموزش‌ها و tài liệu مرجع با Claude Code v2.1.۸۴ (f7۸c۰۹۴) @luongnv89
  - به‌روزرسانی دستورات slash به ۵۵+ دستور داخلی + ۵ skill بسته‌بندی شده، و علامت‌گذاری ۳ مورد منسوخ
  - گسترش رویدادهای هوک از ۱۸ به ۲۵ مورد، اضافه کردن نوع هوک `agent` (حالا ۴ نوع)
  - افزودن حالت خودکار (Auto Mode)، کانال‌ها (Channels)، ورودی صوتی (Voice Dictation) به ویژگی‌های پیشرفته
  - اضافه کردن فیلدهای `effort`، `shell` به skill frontmatter؛ اضافه کردن `initialPrompt`، `disallowedTools` به agent
  - اضافه کردن WebSocket MCP transport، elicitation،限制 ۲KB ابزار
  - اضافه کردن پشتیبانی LSP به پلاگین، `userConfig`، `${CLAUDE_PLUGIN_DATA}`
  - به‌روزرسانی همه tài liệu مرجع (CATALOG، QUICK_REFERENCE، LEARNING-ROADMAP، INDEX)
- بازنویسی README به عنوان راهنما Landing Page ساختارمند (۳۲a۰۷۷۶) @luongnv89

### رفع باگ

- تکمیل verloren واژه‌های cSpell و بخش‌های README برای تایید از طریق CI (۹۳f۹d۵۱) @luongnv89
- اضافه کردن `Sandboxing` به واژه‌نامه cSpell (b۸۰cef۶) @luongnv89

**ثبت تغییرات کامل**: https://github.com/luongnv89/claude-howto/compare/v2.1.1...v2.2.0
"""

with open(os.path.join(fa_dir, "CHANGELOG.md"), "w", encoding="utf-8") as f:
    f.write(content)

print("CHANGELOG.md part 1 written!")