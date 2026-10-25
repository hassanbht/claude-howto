# ثبت تغییرات

## v2.3.0 — ۲۰۲۶-۰۴-۰۷

### ویژگی‌ها

- ساخت و انتشار EPUB برای هر زبان (۹۰e9c۳۰) @Thiên Toán
- افزودن هوک pre-tool-check.sh به ۰۶-hookها (b511ed۱) @JiayuWang
- افزودن ترجمه چینی در دایرکتوری zh/ (۸۹e۸۹d۴) @Luong Nguyen
- افزودن Subagent بهینه‌سازی عملکرد و هوک بررسی وابستگی (f53d۰۸۰) @qk

### رفع باگ

- سازگاری Git Bash ویندوز + پروتکل JSON stdin (۲cbb۱۰c) @Luong Nguyen
- رفع tài liệu پیکربندی autoCheckpoint در ۰۸-checkpoint (۷۴۹c۷۹f) @JiayuWang
- جایگزینی جای گذار به جای embedded تصاویر SVG (۱b۱۶۷۰۹) @Thiên Toán
- رفع نمایش code block تو در تو در README حافظه (ce24۴۲۳) @Zhaoshan Duan
- بازبینی اصلاحات بررسی که توسط squash merge رد شدند (۳۴۲۵۹ca) @Luong Nguyen
- سازگاری اسکریپت‌های هوک با Git Bash ویندوز و استفاده از پروتکل JSON stdin (۱۰۷۱۵۳d) @binyu li

### tài liệu

- همزمانی همه آموزش‌ها با مستندات جدیدترین Claude Code (اکتبر ۲۰۲۶) (۷۲d۳۰۱) @Luong Nguyen
- افزودن لینک زبان چینی در 스위چر زبان (۶cbaa۴d) @Luong Nguyen
- افزودن 스위چر زبان بین انگلیسی و ویتنامی (۱۰۰c۵۱e) @Luong Nguyen
- افزودن نشان #۱ Trending GitHub (۰ca۸۳۷) @Luong Nguyen
- معرفی cc-context-stats برای مانیتور링 منطقه زمینه (d41b۳۳۵) @Luong Nguyen
- معرفی مجموعه luongnv89/skills و مدیر مهارت luongnv89/asm (۷e۳c۰۶) @Luong Nguyen
- به‌روزرسانی آمار README برای بازتاب معیارهای فعلی GitHub (۵۹۰۰+ ستاره، ۶۹۰+ فورک) (۵۰۰۱۵۲۵) @Luong Nguyen
- به‌روزرسانی آمار README برای بازتاب معیارهای فعلی GitHub (۳۹۰۰+ ستاره، ۴۶۰+ فورک) (۹cb۹۲d۶) @Luong Nguyen

### بازسازی

- جایگزینی وابستگی HTTP Kroki با رندر محلی mmdc (e76bbee) @Luong Nguyen
- انتقال بررسی کیفیت به pre-commit، CI به عنوان خط دوم دفاع (۶d۱e۰ae) @Luong Nguyen
- کوچک کردن خط م Bear alap مجوز حالت خودکار (۲۷۹۰fb۲) @Luong Nguyen
- جایگزینی هوک تطابق خودکار با اسکریپت تنظیم مجوز یکباره (۹۹۵a۵۹۶) @Luong Nguyen

### سایر

- جابجایی Key quality gates به phía trước — اضافه کردن mypy به pre-commit، رفع شکست CI (۶۹۹fb۹۱) @Luong Nguyen
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
  - اضافه کردن WebSocket MCP transport، elicitation، محدودیت ۲KB ابزار
  - اضافه کردن پشتیبانی LSP به پلاگین، `userConfig`، `${CLAUDE_PLUGIN_DATA}`
  - به‌روزرسانی همه tài liệu مرجع (CATALOG، QUICK_REFERENCE، LEARNING-ROADMAP، INDEX)
- بازنویسی README به عنوان راهنما Landing Page ساختارمند (۳۲a۰۷۷۶) @luongnv89

### رفع باگ

- تکمیل verloren واژه‌های cSpell و بخش‌های README برای تایید از طریق CI (۹۳f۹d۵۱) @luongnv89
- اضافه کردن `Sandboxing` به واژه‌نامه cSpell (b۸۰cef۶) @luongnv89

**ثبت تغییرات کامل**: https://github.com/luongnv89/claude-howto/compare/v2.1.1...v2.2.0


---

## v2.1.1 — ۲۰۲۶-۰۳-۱۳

### رفع باگ

- حذف لینک‌های marketplace معتبر نشده که باعث شکست بررسی پیوند CI شدند (۳fdf۰۶d) @luongnv89
- اضافه کردن `sandboxed` و `pycache` به واژه‌نامه cSpell (dc۶۴۱۸) @luongnv89

**ثبت تغییرات کامل**: https://github.com/luongnv89/claude-howto/compare/v2.1.0...v2.1.1

---

## v2.1.0 — ۲۰۲۶-۰۳-۱۳

### ویژگی‌ها

- افزودن مسیر یادگیری تطبیقی با مهارت‌های خودارزیابی و lesson quiz (۱ef۴۶cd) @luongnv89
  - `/self-assessment` - تست تعاملی مهارت در ۱۰ alue він поusza، و تولید مسیر یادگیری شخصی‌سازی شده
  - `/lesson-quiz [lesson]` - بررسی دانش هر درس، شامل ۸-۱۰ سوال پرaks

### رفع باگ

- به‌روزرسانی URLهای معتبر، موارد منسوخ و ارجاعات قدیمی (۸fe۰c۹۶) @luongnv89
- رفع پیوندهای خراب در منابع و مهارت self-assessment (۷a۰۵۸۶۳) @luongnv89
- استفاده از tilde fences برای کدهای تو در تو در راهنمای مفاهیم (۵f۸۲۷۱۹) @VikalpP
- تکمیل واژگان ghteaume به واژه‌نامه cSpell (۸df۷۲۷۲) @luongnv89

### tài liệu

- QA فاز ۵ - رفع incongruencyها، URLها و مصطلحات در tài liệu‌ها (۰۰bbe۴c) @luongnv89
- تکمیل فاز ۳-۴ - تکمیل پوشش ویژگی‌های جدید و به‌روزرسانی tài liệu مرجع (۱۳۲de۱۵) @luongnv89
- افزودن MCPorter runtime به بخش س expandsissement زمینه MCP (ef۵۲۷۰۵) @luongnv89
- تکمیل دستورات، ویژگی‌ها و تنظیمات گم شده برای ۶ راهنما (۴bc۸f۱۵) @luongnv89
- تکمیل راهنمای سبک بر اساس استانداردهای موجود در مخزن (۸۴۱۴۱d۰) @luongnv89
- افزودن خط خودارزیابی به جدول مقایسه راهنماها (۸fe۰c۹۶) @luongnv89
- اضافه کردن @VikalpP به لیست مشارکت‌کنندگان، ثبت PR #۷ (d۵b۴۳۵۰) @luongnv89
- افزودن مرجع به skillهای self-assessment و lesson-quiz در README و roadmap (d۵a۶۱۰۶) @luongnv89

### مشارکت‌کنندگان جدید

- @VikalpP مشارکت اول خود را انجام داد، ببینید #۷

**ثبت تغییرات کامل**: https://github.com/luongnv89/claude-howto/compare/v2.0.0...v2.1.0

---

## v2.0.0 — ۲۰۲۶-۰۲-۰۱

### ویژگی‌ها

- به‌روزرسانی همه tài liệu همقابلیت با ویژگی‌های Claude Code فوریه ۲۰۲۶ (۴۸۷c۹۶d)
  - به‌روزرسانی ۲۶ فایل در همه ۱۰ دایرکتوری آموزش و ۷ tài liệu مرجع
  - تکمیل tài liệu Auto Memory - توانایی یادگیری پایدار برای هر پروژه
  - تکمیل tài liệu Remote Control، Web Sessions و Desktop App
  - تکمیل tài liệu Agent Teams (تعاون چند Agen آزمایشی)
  - تکمیل tài liệu OAuth ۲.۰ MCP، جستجوی ابزار و Connectorهای Claude.ai
  - تکمیل tài liệu حافظه پایدار Subagent و عزل Worktree
  - تکمیل tài liệu Subagentهای پس‌زمینه، لیست وظایف و پیشنهادات پرامپت
  - تکمیل tài liệu Sandboxing و تنظیمات مدیریت (Enterprise)
  - تکمیل tài liệu HTTP Hooks و ۷ رویداد هوک جدید
  - تکمیل tài liệu تنظیمات پلاگین، سرورهای LSP و به‌روزرسانی‌های Marketplace
  - تکمیل tài liệu گزینه بازخوانی Checkpoint - خلاصه‌سازی از Checkpoint
  - ثبت ۱۷ دستور Slash جدید (`/fork`، `/desktop`، `/teleport`، `/tasks`، `/fast` و غیره)
  - ثبت flags جدید CLI (`--worktree`، `--from-pr`، `--remote`، `--teleport`، `--teammate-mode` و غیره)
  - ثبت متغیرهای محیطی جدید (حافظه خودکار، سطح effort، تیم‌های Agen و غیره)

### طراحی

- باز طراحی logo به علامت compass-bracket با رنگ Painting� (۲۰۷۷۹db)

### رفع باگ / اصلاح

- به‌روزرسانی نام مدل‌ها: Sonnet ۴.۵ → **Sonnet ۴.۶**، Opus ۴.۵ → **Opus ۴.۶**
- تصحیح نام حالت مجاز: جایگزینی “Unrestricted/Confirm/Read-only” فرضی با `default` / `acceptEdits` / `plan` / `dontAsk` / `bypassPermissions` واقعی
- تصحیح رویدادهای هوک: حذف رویداد‌های فرضی `PreCommit` / `PostCommit` / `PrePush`، اضافه کردن رویداد‌های واقعی (`SubagentStart`، `WorktreeCreate`، `ConfigChange` و غیره)
- تصحیح نحوی CLI: جایگزینی `claude-code --headless` فرضی با `claude -p` (حالت چاپ)
- تصحیح دستور checkpoint: جایگزینی `/checkpoint save/list/rewind/diff` فرضی با antarmuka واقعی `Esc+Esc` / `/rewind`
- تصحیح مدیریت peril.session: جایگزینی `/session list/new/switch/save` فرضی با `/resume` / `/rename` / `/fork` واقعی
- تصحیح فرمت manifist پلاquin: از `plugin.yaml` به `.claude-plugin/plugin.json`
- تصحیح مسیر پیکربندی MCP: `~/.claude/mcp.json` → `.mcp.json` (پروژه) / `~/.claude.json` (کاربر)
- تصحیح URL tài liệu: `docs.claude.com` → `docs.anthropic.com`؛ حذف `plugins.claude.com` فرضی
- حذف چندین تنظیمmade-up در چند فایل
- به‌روزرسانی همه تاریخ “آخرین به‌روزرسانی” به فوریه ۲۰۲۶

**ثبت تغییرات کامل**: https://github.com/luongnv89/claude-howto/compare/20779db...v2.0.0
