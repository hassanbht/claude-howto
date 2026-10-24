<picture>
  <source media="(prefers-color-scheme: dark)" srcset="resources/logos/claude-howto-logo-dark.svg">
  <img alt="Claude How To" src="resources/logos/claude-howto-logo.svg">
</picture>

# مشارکت در Claude How To

از علاقه شما به مشارکت در این پروژه سپاسگزاریم! این راهنما به شما کمک می‌کند تا به‌طور مؤثر مشارکت کنید.

## درباره این پروژه

Claude How To یک راهنمای visual و example-driven برای Claude Code است. ما فراهم می‌کنیم:
- **دیاگرام‌های Mermaid** که توضیح می‌دهند featureها چگونه کار می‌کنند
- **templateهای production-ready** که می‌توانید بلافاصله استفاده کنید
- **مثال‌های real-world** با context و best practiceها
- **مسیرهای یادگیری progressive** از مبتدی تا پیشرفته

## انواع مشارکت

### 1. مثال یا template جدید
افزودن مثال برای featureهای موجود (slash commands، skills، hooks و غیره):
- کد copy-paste ready
- توضیح واضح نحوه کارکرد
- use caseها و مزایا
- نکات troubleshooting

### 2. بهبود مستندات
- شفاف‌سازی بخش‌های گیج‌کننده
- رفع typo و grammar
- افزودن اطلاعات missing
- بهبود مثال‌های کد

### 3. راهنماهای Feature
ایجاد راهنما برای featureهای جدید Claude Code:
- tutorialهای step-by-step
- دیاگرام‌های architecture
- patternها و anti-patternهای رایج
- workflowهای real-world

### 4. گزارش Bug
گزارش issueهایی که با آن‌ها مواجه شدید:
- توضیح آنچه انتظار داشتید
- توضیح آنچه واقعاً رخ داد
- شامل کردن مراحل reproduce
- افزودن نسخه Claude Code و OS مربوطه

### 5. بازخورد و پیشنهادات
کمک به بهبود راهنما:
- پیشنهاد توضیحات بهتر
- اشاره به gapهای coverage
- توصیه بخش‌ها یا reorganization جدید

## شروع کار

### 1. Fork and Clone
```bash
git clone https://github.com/luongnv89/claude-howto.git
cd claude-howto
```

### 2. ایجاد یک Branch
از نام branch توصیفی استفاده کنید:
```bash
git checkout -b add/feature-name
git checkout -b fix/issue-description
git checkout -b docs/improvement-area
```

### 3. تنظیم محیط

Hookهای pre-commit همان checkهای CI را به‌صورت محلی قبل از هر commit اجرا می‌کنند. هر پنج check باید قبل از پذیرش PR pass شوند.

**وابستگی‌های required:**

```bash
pip install uv
uv venv
source .venv/bin/activate
uv pip install -r scripts/requirements-dev.txt

npm install -g markdownlint-cli

node --version

uv pip install pre-commit
pre-commit install
```

**تأیید setup:**

```bash
pre-commit run --all-files
```

hookهایی که روی هر commit اجرا می‌شوند:

| Hook | آنچه بررسی می‌کند |
|------|-------------------|
| `markdown-lint` | فرمت و ساختار Markdown |
| `cross-references` | لینک‌های relative، anchorها، code fenceها |
| `mermaid-syntax` | همه بلوک‌های ` ```mermaid ` به‌درستی parse می‌شوند |
| `link-check` | URLهای خارجی reachable هستند |
| `build-epub` | EPUB build |

## فرآیند Review کد

reviewerها بررسی می‌کنند:
- **Accuracy**: آیا همان‌طور که توضیح داده شده کار می‌کند؟
- **Quality**: آیا production-ready است؟
- **Consistency**: آیا patternهای پروژه را دنبال می‌کند؟
- **Documentation**: آیا واضح و کامل است؟
- **Security**: آیا vulnerability وجود دارد؟

## گزارش Issue

### گزارش Bug
شامل:
- نسخه Claude Code
- سیستم‌عامل
- مراحل reproduce
- رفتار مورد انتظار
- رفتار واقعی
- اسکرین‌شات در صورت امکان

### درخواست Feature
شامل:
- use case یا problem being solved
- راه‌حل پیشنهادی
- alternativeهایی که در نظر گرفته‌اید
- context اضافی

### مسائل مستندات
شامل:
- آنچه گیج‌کننده یا missing است
- پیشنهادات بهبود
- مثال‌ها یا referenceها

## سیاست‌های پروژه

### اطلاعات حساس
- هرگز API key، token یا credential commit نکنید
- از placeholder valueها در مثال‌ها استفاده کنید
- `.env.example` را برای configuration fileها include کنید
- environment variableهای required را مستند کنید

### کیفیت کد
- مثال‌ها را focused و readable نگه دارید
- از over-engineering خودداری کنید
- برای logic غیربدیهی comment بگذارید
- قبل از submit به‌طور کامل تست کنید

### مالکیت معنوی
- محتوای original متعلق به author است
- پروژه از educational license استفاده می‌کند
- copyrightهای موجود را رعایت کنید
- attribution را در صورت نیاز فراهم کنید

## دریافت کمک

- **سؤالات**: یک discussion در GitHub Issues باز کنید
- **کمک عمومی**: مستندات موجود را بررسی کنید
- **کمک development**: مثال‌های مشابه را review کنید
- **Code review**: maintainerها را در PRها tag کنید

## شناسایی

مشارکت‌کنندگان در این بخش‌ها شناسایی می‌شوند:
- بخش Contributors در README.md
- صفحه contributors گیت‌هاب
- تاریخچه commit

## امنیت

هنگام مشارکت مثال‌ها و مستندات، لطفاً secure coding practiceها را دنبال کنید:

- **هرگز secret یا API key را hardcode نکنید** - از environment variableها استفاده کنید
- **درباره پیامدهای امنیتی هشدار دهید** - riskهای potential را highlight کنید
- **پیش‌فرض‌های امن استفاده کنید** - featureهای امنیتی را به‌طور پیش‌فرض فعال کنید
- **inputها را validate کنید** - input validation و sanitization مناسب را نشان دهید
- **نکات امنیتی include کنید** - security considerationها را مستند کنید

برای مسائل امنیتی، [SECURITY.md](SECURITY.md) را برای فرآیند گزارش vulnerability ببینید.

## کد رفتار

ما متعهد به فراهم کردن یک community خوشامدگو و فراگیر هستیم. لطفاً [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) را برای استانداردهای کامل community بخوانید.

به‌طور خلاصه:
- respectful و inclusive باشید
- بازخورد را با فروتنی بپذیرید
- به دیگران کمک کنید تا یاد بگیرند و رشد کنند
- از harassment یا discrimination خودداری کنید
- issueها را به maintainerها گزارش کنید

همه مشارکت‌کنندگان انتظار می‌رود این کد را رعایت کنند و با مهربانی و احترام با یکدیگر رفتار کنند.

## مجوز

با مشارکت در این پروژه، موافقت می‌کنید که مشارکت‌های شما تحت MIT License منتشر شوند. فایل [LICENSE](LICENSE) را برای جزئیات ببینید.

## سؤالی دارید؟

- [README](README.md) را بررسی کنید
- [LEARNING-ROADMAP.md](LEARNING-ROADMAP.md) را review کنید
- مثال‌های موجود را ببینید
- برای discussion یک issue باز کنید

از مشارکت شما سپاسگزاریم! 🙏

---

**Last Updated**: August 4, 2026
**Claude Code Version**: 2.1.220
**Sources**:
- https://code.claude.com/docs/en/overview
**Compatible Models**: Claude Fable 5, Claude Opus 5, Claude Sonnet 5, Claude Sonnet 4.6, Claude Opus 4.8, Claude Haiku 4.5
