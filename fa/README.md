<picture>
  <source media="(prefers-color-scheme: dark)" srcset="resources/logos/claude-howto-logo-dark.svg">
  <img alt="Claude How To" src="resources/logos/claude-howto-logo.svg">
</picture>

<p align="center">
  <a href="https://github.com/trending">
    <img src="https://img.shields.io/badge/GitHub-🔥%20%231%20Trending-purple?style=for-the-badge&logo=github"/>
  </a>
</p>

[![GitHub Stars](https://img.shields.io/github/stars/luongnv89/claude-howto?style=flat&color=gold)](https://github.com/luongnv89/claude-howto/stargazers)
[![GitHub Forks](https://img.shields.io/github/forks/luongnv89/claude-howto?style=flat)](https://github.com/luongnv89/claude-howto/network/members)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Version](https://img.shields.io/badge/version-2.1.302-brightgreen)](CHANGELOG.md)
[![Claude Code](https://img.shields.io/badge/Claude_Code-2.1+-purple)](https://code.claude.com)

🌐 **Language / Ngôn ngữ / 语言 / Мова:** [English](../README.md) | [Tiếng Việt](../vi/README.md) | [中文](../zh/README.md) | [Українська](../uk/README.md) | [日本語](../ja/README.md) | [فارسی](README.md)

# کد کلود را در یک آخر هفته مسلط شوید

از تایپ کردن `claude` تا orchestration ایجنت‌ها، هوک‌ها، skillها و سرورهای MCP — با آموزش‌های تصویری، قالب‌های copy-paste و یک مسیر یادگیری هدایت‌شده.

**[در ۱۵ دقیقه شروع کنید](#get-started-in-15-minutes)** | **[سطح خود را پیدا کنید](#not-sure-where-to-start)** | **[کاتالوگ ویژگی‌ها را مرور کنید](CATALOG.md)**

---

## فهرست مطالب

- [مشکل](#the-problem)
- [چگونه کد کلود این را حل می‌کند](#how-claude-how-to-fixes-this)
- [چگونه کار می‌کند](#how-it-works)
- [مطمئن نیستید از کجا شروع کنید؟](#not-sure-where-to-start)
- [در ۱۵ دقیقه شروع کنید](#get-started-in-15-minutes)
- [با این چه می‌توانید بسازید؟](#what-can-you-build-with-this)
- [سوالات متداول](#faq)
- [مشارکت](#contributing)
- [مجوز](#license)

---

## مشکل

شما کد کلود را نصب کردید. چند prompt اجرا کردید. حالا چه؟

- **مستندات رسمی ویژگی‌ها را توصیف می‌کنند — اما نشان نمی‌دهند چگونه آن‌ها را ترکیب کنید.** می‌دانید slash commandها وجود دارند، اما نمی‌دانید چگونه آن‌ها را با hookها، memory و subagentها در یک workflow زنجیر کنید که واقعاً ساعت‌ها ذخیره کند.
- **مسیر یادگیری واضحی وجود ندارد.** باید MCP را قبل از hookها یاد بگیرید؟ skillها قبل از subagentها؟ به همه چیز نگاه می‌کنید و هیچ‌چیز را مسلط نمی‌شوید.
- **مثال‌ها بسیار پایه‌ای هستند.** یک slash command "hello world" به شما کمک نمی‌کند یک pipeline تولیدی code review بسازید که از memory استفاده کند، به ایجنت‌های تخصصی تفویض کند و اسکن‌های امنیتی را به‌طور خودکار اجرا کند.

شما ۹۰٪ قدرت کد کلود را روی میز می‌گذارید — و نمی‌دانید چه چیزی را نمی‌دانید.

---

## چگونه کد کلود این را حل می‌کند

این یک reference دیگر ویژگی نیست. این یک **راهنمای ساختاریافته، تصویری و مثال‌محور** است که به شما یاد می‌دهد از هر ویژگی کد کلود با قالب‌های دنیای واقعی استفاده کنید که امروز می‌توانید در پروژه خود کپی کنید.

---
| | مستندات رسمی | این راهنما |
|--|---------------|------------|
| **Format** | Reference documentation | آموزش‌های تصویری با دیاگرام‌های Mermaid |
| **Depth** | توصیف ویژگی | نحوه کار در زیر کاپوت |
| **Examples** | snippetهای پایه | قالب‌های production-ready که فوراً استفاده می‌کنید |
| **Structure** | سازمان‌دهی بر اساس ویژگی | مسیر یادگیری progressive (beginner تا advanced) |
| **Onboarding** | self-directed | roadmap هدایت‌شده با تخمین زمان |
| **Self-Assessment** | هیچ | quizهای تعاملی برای یافتن شکاف‌ها و ساخت مسیر personalized |

### چه چیزی دریافت می‌کنید:

- **۱۰ ماژول آموزشی** پوشش‌دهنده هر ویژگی کد کلود — از slash commandها تا تیم‌های ایجنت سفارشی
- **قالب‌های copy-paste** که می‌توانید فوراً در پروژه‌های خود استفاده کنید
- **دیاگرام‌های Mermaid** که نحوه کار هر ویژگی را نشان می‌دهند
- **مسیر یادگیری هدایت‌شده** با تخمین زمان (۱۱-۱۳ ساعت برای مسلط شدن)
- **Self-assessment** برای یافتن شکاف‌ها و ساخت مسیر personalized

---

> **⭐ این ریپو مفید بود؟** یک ستاره به آن بدهید — به دیگران کمک می‌کند آن را پیدا کنند و به من انگیزه می‌دهد برای به‌روز نگه داشتن آن!

---

## چگونه کار می‌کند

```
شما (Developer)
       │
       ▼
┌─────────────────────────────────────────┐
│  کد کلود CLI / VS Code / Desktop / Web  │
└────────────┬────────────────────────────┘
             │
             ▼
┌─────────────────────────────────────────┐
│        Claude Code Core Engine          │
│  (پردازش prompt، orchestration ابزار)    │
└────────────┬────────────────────────────┘
             │
    ┌────────┴────────┬──────────────┐
    ▼                 ▼              ▼
┌────────┐      ┌──────────┐   ┌──────────┐
│ Tools  │      │  Memory  │   │ Extensions│
│ (Read, │      │ (CLAUDE. │   │ (Skills, │
│ Edit,  │      │  md)     │   │ Subagents│
│ Bash,  │      └──────────┘   │ Hooks,   │
│ Grep)  │                    │ MCP)     │
└────────┘                    └──────────┘
```

| مفهوم | یک جمله | مثال |
|---------|-------------|---------|
| **Slash Commands** | دستورات تعریف‌شده توسط کاربر | `/review`، `/deploy` |
| **Memory** | Context بین sessionها | `CLAUDE.md` |
| **Skills** | قابلیت‌های قابل استفاده مجدد | Auto code review |
| **Subagents** | AI assistantهای تخصصی | Security reviewer |
| **MCP Servers** | اتصالات ابزار خارجی | GitHub، DB |
| **Hooks** | دستورات shell رویدادمحور | Auto-format بعد از edit |
| **Plugins** | bundleهای قابل نصب | DevOps automation |
| **Checkpoints** | ذخیره/rewind state | آزمایش امن |
| **Advanced Features** | Planning، thinking، background tasks | Reasoning پیچیده |
| **CLI Reference** | Command line interface | `claude -p "query"` |

---

## مطمئن نیستید از کجا شروع کنید؟

یک quiz تعاملی بگیرید تا شکاف‌های خود را پیدا کنید و مسیر یادگیری personalized بسازید:

```bash
/lesson-quiz
```

یا از [Self-Assessment](.claude/skills/self-assessment/SKILL.md) برای ارزیابی دستی استفاده کنید.

### مسیرهای یادگیری بر اساس سطح

| سطح | ماژول‌ها | زمان | تمرکز |
|-------|----------|------|-------|
| **Level 1: Beginner** | Slash Commands → Memory | 2-3 ساعت | workflowهای پایه |
| **Level 2: Intermediate** | Skills → Hooks | 3-4 ساعت | automation |
| **Level 3: Advanced** | Subagents → MCP | 4-5 ساعت | orchestration |
| **Level 4: Expert** | Plugins → Advanced Features | 5-6 ساعت | production systems |

هر ماژول مستقل است اما بهترین نتیجه را با دنبال کردن ترتیب پیشنهادی به دست می‌آورید.

---

## در ۱۵ دقیقه شروع کنید

### مرحله ۱: اولین slash command خود را نصب کنید (۲ دقیقه)

```bash
mkdir -p .claude/commands
cp 01-slash-commands/optimize.md .claude/commands/
```

سپس در Claude Code تایپ کنید: `/optimize`

### مرحله ۲: project memory خود را اضافه کنید (۳ دقیقه)

```bash
cp 02-memory/project-CLAUDE.md ./CLAUDE.md
```

در صورت نیاز ویرایش کنید.

### مرحله ۳: اولین skill خود را نصب کنید (۵ دقیقه)

```bash
cp -r 03-skills/code-review ~/.claude/skills/
```

### مرحله ۴: با یک command امتحان کنید (۵ دقیقه)

```bash
claude
# سپس تایپ کنید: /optimize
```

**می‌خواهید بیشتر؟** [Learning Roadmap](LEARNING-ROADMAP.md) کامل را برای مسیر یادگیری ۱۱-۱۳ ساعته ببینید.

---

## با این چه می‌توانید بسازید؟

| Use Case | ویژگی‌های استفاده‌شده | زمان | سطح |
|-----------|---------------------|------|-------|
| **Automated Code Review** | Slash Commands + Subagents + Memory + Hooks | 2-3 ساعت | Intermediate |
| **Team Onboarding Bot** | Memory + Slash Commands + MCP | 3-4 ساعت | Intermediate |
| **CI/CD Pipeline** | CLI Reference + Hooks + Background Tasks | 2-4 ساعت | Advanced |
| **Documentation Generator** | Skills + Subagents + MCP/Filesystem | 2-3 ساعت | Intermediate |
| **Security Audit System** | Subagents + Skills + Hooks (Read-only) | 3-5 ساعت | Advanced |
| **DevOps Automation** | Plugins + MCP + Hooks + Background Tasks | 4-6 ساعت | Expert |
| **Incident Response Playbook** | Slash Commands + Subagents + Memory | 2-3 ساعت | Intermediate |

---

## سوالات متداول

**آیا این رسمی Anthropic است؟**
خیر. این یک راهنمای مستقل از جامعه است. برای مستندات رسمی، به [code.claude.com/docs](https://code.claude.com/docs/en/overview) مراجعه کنید.

**آیا این با Claude Code Pro/Max کار می‌کند؟**
بله. همه مثال‌ها با هر tier کار می‌کنند. برخی ویژگی‌ها (مثل background tasks) ممکن است بسته به tier متفاوت باشند.

**چقدر طول می‌کشد تا مسلط شوم؟**
- **Quick Start**: ۱۵-۳۰ دقیقه (ماژول‌های ۰۱-۰۲)
- **Intermediate**: ۲-۳ ساعت (ماژول‌های ۰۱-۰۵)
- **Advanced**: ۵-۸ ساعت (ماژول‌های ۰۱-۰۹)
- **Mastery**: ۱۱-۱۳ ساعت (همه ماژول‌ها + تمرین)

**آیا می‌توانم این را در تیم خود استفاده کنم؟**
بله! این برای استفاده تیمی طراحی شده است. commit کردن `.claude/` directory به git تا همه از commands، skills و configurationهای یکسان استفاده کنند.

**چه نسخه‌ای از Claude Code پشتیبانی می‌شود؟**
این راهنما برای Claude Code 2.1+ به‌روز است. ویژگی‌های خاص ممکن است نسخه‌های جدیدتری نیاز داشته باشند.

**آیا محتوای رسمی Anthropic را کپی کرده‌ام؟**
خیر. این راهنمای اصلی است که ویژگی‌های مستندات رسمی را توضیح می‌دهد. هیچ متن محافظت‌شده‌ای از مستندات Anthropic را کپی نکرده‌ام.

**چگونه شکاف‌های خود را پیدا کنم؟**
`/lesson-quiz` را اجرا کنید یا [Self-Assessment](.claude/skills/self-assessment/SKILL.md) را امتحان کنید.

---

## مشارکت

یافته‌ای دارید یا می‌خواهید مثالی کمک کنید؟ ما عاشق کمک شما هستیم!

**لطفاً [CONTRIBUTING.md](CONTRIBUTING.md) را برای دستورالعمل‌های تفصیلی بخوانید درباره:**
- انواع مشارکت (مثال‌ها، docs، ویژگی‌ها، bugها، بازخورد)
- نحوه راه‌اندازی محیط توسعه
- ساختار directory و نحوه اضافه کردن محتوا
- دستورالعمل‌های نگارش و best practiceها
- فرآیند commit و PR

**استانداردهای جامعه ما:**
- [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) - چگونه با یکدیگر رفتار می‌کنیم
- [SECURITY.md](SECURITY.md) - سیاست امنیتی و گزارش آسیب‌پذیری

### گزارش مسائل امنیتی

اگر آسیب‌پذیری امنیتی یافتید، لطفاً به‌طور مسئولانه گزارش دهید:

1. **استفاده از GitHub Private Vulnerability Reporting**: https://github.com/luongnv89/claude-howto/security/advisories
2. **یا بخوانید** [.github/SECURITY_REPORTING.md](.github/SECURITY_REPORTING.md) برای دستورالعمل‌های تفصیلی
3. **عمومی issue باز نکنید** برای آسیب‌پذیری‌های امنیتی

شروع سریع:
1. Fork و clone کردن repository
2. ایجاد branch توصیفی (`add/feature-name`، `fix/bug`، `docs/improvement`)
3. ایجاد تغییرات طبق دستورالعمل‌ها
4. ارسال pull request با توضیح واضح

**نیاز به کمک دارید؟** یک issue یا discussion باز کنید و ما شما را راهنمایی می‌کنیم.

---

## مجوز

MIT License - به [LICENSE](LICENSE) مراجعه کنید. استفاده، تغییر و توزیع آزاد است. تنها الزام شامل کردن license notice است.

---

**آخرین به‌روزرسانی**: October 18, 2026
**نسخه کد کلود**: 2.1.302
**منابع**:
- https://code.claude.com/docs/en/tools-reference#task-tool-availability
- https://code.claude.com/docs/en/hooks
- https://code.claude.com/docs/en/overview
- https://code.claude.com/docs/en/changelog
- https://code.claude.com/docs/en/permission-modes
- https://platform.claude.com/docs/en/about-claude/models/overview
- https://github.com/anthropics/claude-code/releases
- https://github.com/anthropics/claude-code/releases/tag/v2.1.154
- https://code.claude.com/docs/en/model-config
- https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md
- https://github.com/anthropics/claude-code/releases/tag/v2.1.296
- https://code.claude.com/docs/en/setup
- https://code.claude.com/docs/en/mcp
- https://code.claude.com/docs/en/plugins/install
- https://code.claude.com/docs/en/checkpointing
- https://github.com/anthropics/claude-code
- https://code.claude.com/docs/en/changelog#2-1-302
**مدل‌های سازگار**: Claude Fable 5.1, Claude Fable 5, Claude Opus 5, Claude Sonnet 5, Claude Sonnet 4.6, Claude Opus 4.8, Claude Haiku 4.5

