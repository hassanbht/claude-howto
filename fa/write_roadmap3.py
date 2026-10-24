import os

fa_dir = r"D:\Project\claude-howto\fa"

content = """

---

### M1 - بوت‌ساختار آمدن · پایان آوریل ۲۰۲۶

**فرستادن:**

- `scripts/quickstart.sh` - نصب خطی‌تلفتی برای کاربران جدید (آیین)
- `QUICKSTART.md` - راهنمای "۱۵ دقیقه‌ی اول" بصری
- تمام ۱۰ module، جایزه سخت‌گیری و پیش‌نمایش "چه می‌سازید"
- تمامی module‌ها، `WHATS-NEW.md` و جایزه نسخه
- `.github/workflows/staleness-check.yml` - بررسی هفتگی، به‌وجود‌آورنده issue اگر module ۳۰ روز از تایید گذشته است
- `CLAUDE.md` در ریشه - پیکربندی پروژه به‌عنوان نمونه
- `scripts/build-agent-index.py` - مایکروایند که از ۱۰ module خروجی `agent-manifest.json` + `AGENT-INDEX.md` تولید می‌کند
- **06-hooks** - پوشش کامل: ۵ اسکریپت، درخت تصمیم‌گیری، Try It Now، الگو
- **08-checkpoints** - پوشش کامل: ۳۱۱ ردیف به بیش از ۸۰۰، ۳ الگو، درخت تصمیم‌گیری، الگو

**چرا از اینجا شروع می‌شود:** بوت‌ساختار، همه مراحل بعدی را پوشش می‌دهد. hooks و checkpoints ضعیف‌ترین module‌ها هستند و حسگر مهم‌ترین کاربران جدید را دارند.

---

### M2 - ۶/۱۰ module به اتمام رسیده · پایان ژوئن ۲۰۲۶

**فرستادن (هر module یک بازرسی عمیق است):**

- **01-slash-commands** - مکالمه سناریویی، درخت تصمیم‌گیری، Try It Now، الگوهای نام‌گذاری
- **02-memory** - مکالمه سناریویی، درخت تصمیم‌گیری، Try It Now، الگوهای نام‌گذاری
- **03-skills** - مکالمه سناریویی، درخت تصمیم‌گیری، Try It Now، الگوهای نام‌گذاری
- **10-cli** - مکالمه سناریویی، درخت تصمیم‌گیری، Try It Now، الگوهای نام‌گذاری
- مرحله CI: تایید معتبر بودن `agent-manifest.json` در هر push

تمامی module‌ها، فرآیند تولید را اجرا می‌کنند تا خروجی manifests معتبر بودن اطمینان حاصل شود.

---

### M3 - ۱۰/۱۰ module به اتمام رسیده · انتهای اکتبر ۲۰۲۶

**فرستادن:**

- **04-subagents** - پوشش کامل (شامل الگوی Multi-Agent Review)
- **05-mcp** - پوشش کامل
- **07-plugins** - پوشش کامل
- **09-advanced-features** - پوشش کامل

حالا، تمام module‌ها دارای: مکالمه سناریویی، بیشتر از ۲ بسته Try It Now، درخت‌های Mermaid، بیشتر از ۲ الگوی نام‌گذاری.

---

### M4 - لایه proxy آمدن · پایان سپتامبر ۲۰۲۶

**فرستادن:**

- نسخه نهایی `agent-manifest.json`، پوشش ۱۰۰٪ module (تولید بر اساس محتوا)
- `AGENT-INDEX.md`، لینک‌شده در `README.md`
- `skills/claude-howto-lookup/SKILL.md` - skill خیلی‌ها، پرس‌وجو را بر اساس manifests
- `RECIPES.md` - ۵ الگو Multi-Capability Creator (schema: name، modules-used، problem، solution، expected outcome)
- `COMMUNITY-PROJECTS.md` - لیست انتخابی استاتیک، فرم‌ثبت‌کردن PR

**چرا سپتامبر؟** وقتی ۱۰ module، محتوا را کامل دارند، Index proxy معنایی دارد.

---

### M5 - ایزوگری کامل · پایان نوامبر ۲۰۲۶

**فرستادن:**

- ایزوگری کامل: تمام ۱۰ module، بر اساس ورژن فعلی ABC، تایید شده‌اند
- به‌روزرسانی `cc_version_verified` frontmatter و جایزه نسخه در تمام module‌ها
- `RECIPES.md` به ۸ یا بیشتر بازگو، مبتنی بر الگوهای سیت‌ابرداری‌های راست‌گشته
- چپ‌فیس‌نمادگذاری عمومی: "مشارکت در گردش‌کار کلود کد" - پشتیبانی از سیگنال‌های استفاده proxy‌ها

---

### M6 - خود‌بقری · انتهای مه ۲۰۲۷

**پایدار / ادامه ترتیبی:**

- مهارت `/docs-sync-claude-code` پس از هر نسخه‌ی CC، اجرا می‌شود -> به‌روزرسانی `WHATS-NEW.md`
- CI regression agent-manifest: پوشش ۱۰۰٪ module
- `RECIPES.md` به ۱۰ یا بیشتر بازگو
- `COMMUNITY-PROJECTS.md` رشد طبیعی
- ارزیابی سیگنال‌های استفاده proxy‌ها - اگر معتبر است، تبلیغ و ASM registry Lookup skill

---

## خلاصه پیش‌رفت

| deliverable | نوع | مرحله |
|------------------|------|-------|
| `scripts/quickstart.sh` | اسکریپت | P1 |
| `QUICKSTART.md` | مستند | P1 |
| `CLAUDE.md` در ریشه | پیکربندی | P1 |
| `WHATS-NEW.md` | مستند | P1 |
| `.github/workflows/staleness-check.yml` | CI | P1 |
| `scripts/build-agent-index.py` | اسکریپت | P1 |
| ۱۰ module پوشش عمیق (سناریو + Try It Now + درخت + الگو) | محتوا | P1–P3 |
| `agent-manifest.json` (تولید‌شده) | داده | P4 |
| `AGENT-INDEX.md` (تولید‌شده) | مستند | P4 |
| `skills/claude-howto-lookup/SKILL.md` | Skill | P4 |
| `RECIPES.md` (۵ تا ۱۰+ recipes) | مستند | P4–P6 |
| `COMMUNITY-PROJECTS.md` | مستند | P4 |

---

## موارد خروجی

این مقادیر، در `TODOS.md`، نقل‌قضا، ممنوع می‌شوند:

- بازار سخت‌افزار Skill یا registry قابل نصب
- سایت یا پنل سفارشی
- پیگیری اتمام (cc-progress)
- CI تأیید آموزش‌های جامعه
- CONTRIBUTORS.md خودکار
- ترجمه‌های چندزبانه
- بستر آزمون / ارزیابی
- آواندیار پروژه

---
"""
with open(os.path.join(fa_dir, "docs", "ROADMAP-20260401.md"), "a", encoding="utf-8") as f:
    f.write(content)

print("docs/ROADMAP-20260401.md part 2 written!")