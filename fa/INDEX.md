<picture>
  <source media="(prefers-color-scheme: dark)" srcset="resources/logos/claude-howto-logo-dark.svg">
  <img alt="Claude How To" src="resources/logos/claude-howto-logo.svg">
</picture>

# شاخص کامل مثال‌های کد کلود

این سند یک شاخص کامل از تمام فایل‌های مثال سازمان‌دهی‌شده بر اساس نوع ویژگی ارائه می‌دهد.

## آمار خلاصه

- **تعداد کل فایل‌ها**: ۱۰۰+ فایل
- **دسته‌ها**: ۱۰ دسته ویژگی
- **پلاگین‌ها**: ۳ پلاگین کامل
- **Skillها**: ۶ skill کامل
- **Hookها**: ۱۱ مثال hook
- **آماده استفاده**: همه مثال‌ها

---

## ۰۱. Slash Commands (۱۰ فایل)

میانبرهای تعریف‌شده توسط کاربر برای workflowهای رایج.

| فایل | توضیحات | Use Case |
|------|-------------|----------|
| `optimize.md` | analyzer بهینه‌سازی کد | یافتن مسائل performance |
| `pr.md` | آماده‌سازی pull request | automation workflow PR |
| `generate-api-docs.md` | generator مستندات API | تولید مستندات API |
| `commit.md` | helper پیام commit | commitهای استاندارد |
| `setup-ci-cd.md` | راه‌اندازی CI/CD pipeline | automation DevOps |
| `push-all.md` | push همه تغییرات | workflow push سریع |
| `unit-test-expand.md` | گسترش coverage تست واحد | automation تست |
| `doc-refactor.md` | refactoring مستندات | بهبود مستندات |
| `pr-slash-command.png` | مثال screenshot | reference تصویری |
| `README.md` | مستندات | راهنمای setup و استفاده |

**مسیر نصب**: `.claude/commands/`

**استفاده**: `/optimize`، `/pr`، `/generate-api-docs`، `/commit`، `/setup-ci-cd`، `/push-all`، `/unit-test-expand`، `/doc-refactor`

---

## ۰۲. Memory (۶ فایل)

Context بین sessionها و استانداردهای پروژه.

| فایل | توضیحات | Scope | Location |
|------|-------------|-------|----------|
## ۰۳. Skills (۲۳ فایل)

قابلیت‌های auto-invoked با scriptها و templateها.

### Code Review Skill (۵ فایل)
```
code-review-specialist/
├── SKILL.md                          # تعریف skill
├── scripts/
│   ├── analyze-metrics.py            # analyzer متریک‌های کد
│   └── compare-complexity.py         # مقایسه complexity
└── templates/
    ├── review-checklist.md           # checklist review
    └── finding-template.md           # مستندات finding
```

**هدف**: Code review جامع با security، performance و quality analysis

**Auto-invoked**: هنگام review کد

---

### Brand Voice Skill (۴ فایل)
```
brand-voice/
├── SKILL.md                          # تعریف skill
├── templates/
│   ├── email-template.txt            # فرمت email
│   └── social-post-template.txt      # فرمت social media
└── tone-examples.md                  # پیام‌های نمونه
```

**هدف**: اطمینان از brand voice یکنواخت در ارتباطات

**Auto-invoked**: هنگام نگارش content

---

### Doc Generator Skill (۵ فایل)
```
doc-generator/
├── SKILL.md                          # تعریف skill
├── templates/
│   ├── api-endpoint.md               # template endpoint API
│   ├── function-docs.md              # template مستندات function
│   └── adr-template.md               # template تصمیم architecture
└── (examples)
```

**هدف**: تولید مستندات API و code
## ۰۶-۱۰. ماژول‌های باقی‌مانده

- **۰۶. Hooks**: Event-driven automation (pre-commit، format، security scan و غیره) — ۱۱ مثال
- **۰۷. Plugins**: bundleهای قابل نصب (devops-automation، documentation، pr-review)
- **۰۸. Checkpoints**: ذخیره/rewind state برای آزمایش امن
- **۰۹. Advanced Features**: Planning mode، extended thinking، background tasks، permission modes
- **۱۰. CLI Reference**: Command line interface و flags

## جستجو بر اساس کلمه کلیدی

### Performance
- `01-slash-commands/optimize.md` - تحلیل performance
- `04-subagents/code-reviewer.md` - review performance
- `03-skills/code-review-specialist/` - متریک‌های performance
- `07-plugins/pr-review/agents/performance-analyzer.md` - specialist performance

### Security
- `04-subagents/secure-reviewer.md` - security review
- `03-skills/code-review-specialist/` - security analysis
- `07-plugins/pr-review/` - security checks

### Testing
- `04-subagents/test-engineer.md` - test engineer
- `07-plugins/pr-review/commands/check-tests.md` - test coverage

### Documentation
- `01-slash-commands/generate-api-docs.md` - دستور مستندات API
- `04-subagents/documentation-writer.md` - doc writer agent
- `03-skills/doc-generator/` - doc generator skill
- `07-plugins/documentation/` - پلاگین کامل مستندات

### Deployment
- `07-plugins/devops-automation/` - راه‌حل کامل DevOps

### Automation
- `06-hooks/` - automation رویدادمحور
- `06-hooks/pre-commit.sh` - automation pre-commit
- `06-hooks/format-code.sh` - auto-formatting
- `09-advanced-features/` - headless mode برای CI/CD

### Validation
- `06-hooks/security-scan.sh` - اعتبارسنجی امنیتی
- `06-hooks/validate-prompt.sh` - اعتبارسنجی prompt

### Experimentation
- `08-checkpoints/` - آزمایش امن با rewind
- `08-checkpoints/checkpoint-examples.md` - مثال‌های دنیای واقعی

### Planning
- `09-advanced-features/planning-mode-examples.md` - مثال‌های planning mode
- `09-advanced-features/README.md` - extended thinking

### Configuration
- `09-advanced-features/config-examples.json` - مثال‌های پیکربندی

---

## یادداشت‌ها

- همه مثال‌ها آماده استفاده هستند
- برای نیازهای خاص خود تغییر دهید
- مثال‌ها بهترین practiceهای کد کلود را دنبال می‌کنند
- هر دسته README خود را با دستورالعمل‌های تفصیلی دارد
- scriptها شامل error handling مناسب هستند
- templateها قابل سفارشی‌سازی هستند

---

## مشارکت

می‌خواهید مثال بیشتری اضافه کنید؟ ساختار را دنبال کنید:
1. ایجاد subdirectory مناسب
2. شامل README.md با usage
3. دنبال کردن naming conventions
4. تست کامل
5. به‌روزرسانی این شاخص

---

**آخرین به‌روزرسانی**: October 18, 2026
**نسخه کد کلود**: 2.1.302
**منابع**:
- https://code.claude.com/docs/en/tools-reference#task-tool-availability
- https://code.claude.com/docs/en/workflows#set-a-size-guideline
- https://code.claude.com/docs/en/memory#agents-md
- https://code.claude.com/docs/en/overview
- https://code.claude.com/docs/en/hooks
- https://code.claude.com/docs/en/commands
- https://code.claude.com/docs/en/permission-modes
- https://github.com/anthropics/claude-code/releases/tag/v2.1.153
- https://github.com/anthropics/claude-code/releases/tag/v2.1.154
- https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md
- https://code.claude.com/docs/en/model-config
- https://code.claude.com/docs/en/workflows#let-claude-decide-with-ultracode
- https://code.claude.com/docs/en/cli-reference
- https://code.claude.com/docs/en/plugins/install
- https://code.claude.com/docs/en/checkpointing
- https://code.claude.com/docs/en/remote-control
- https://code.claude.com/docs/en/chrome
**مدل‌های سازگار**: Claude Fable 5, Claude Opus 5, Claude Sonnet 5, Claude Sonnet 4.6, Claude Opus 4.8, Claude Haiku 4.5
**Total Examples**: 100+ files
**Categories**: 10 features
**Hooks**: 11 automation scripts
**Configuration Examples**: 10+ scenarios
**Ready to Use**: All examples


**Auto-invoked**: هنگام مستندسازی code

---

## ۰۴. Subagents (۱۰ فایل)

AI assistantهای تخصصی برای taskهای خاص.

| فایل | تخصص | Use Case |
|------|-------------|----------|
| `code-reviewer.md` | Review کد | Quality analysis |
| `test-engineer.md` | ایجاد تست | Test coverage |
| `documentation-writer.md` | نگارش مستندات | Doc generation |
| `secure-reviewer.md` | Security review | Vulnerability scanning |
| `implementation-agent.md` | پیاده‌سازی | Feature development |
| `debugger.md` | Debugging | Bug investigation |
| `data-scientist.md` | Data analysis | Data insights |
| `clean-code-reviewer.md` | Code quality | Refactoring |
| `performance-optimizer.md` | Performance | Optimization |
| `README.md` | مستندات | Setup guide |

**نصب**: `.claude/agents/`

**استفاده**: Auto-delegated یا explicit invocation

---

## ۰۵. MCP (Model Context Protocol) (۱۰ فایل)

اتصالات ابزار خارجی.

| فایل | توضیحات | Integration |
|------|-------------|-------------|
| `github-mcp.json` | GitHub integration | Repository management |
| `database-mcp.json` | Database access | SQL queries |
| `filesystem-mcp.json` | File operations | File management |
| `multi-mcp.json` | Multiple servers | Combined setup |
| `README.md` | مستندات | Setup guide |

**نصب**: تنظیم در `.mcp.json`

**استفاده**: Claude به‌طور خودکار ابزارهای MCP را استفاده می‌کند

---

| `project-CLAUDE.md` | استانداردهای پروژه تیم | Project-wide | `./CLAUDE.md` |
| `directory-api-CLAUDE.md` | قوانین خاص API | Directory | `./src/api/CLAUDE.md` |
| `personal-CLAUDE.md` | ترجیحات شخصی | User | `~/.claude/CLAUDE.md` |
| `memory-saved.png` | Screenshot: memory saved | - | reference تصویری |
| `memory-ask-claude.png` | Screenshot: ask Claude | - | reference تصویری |
| `README.md` | مستندات | - | Reference |

**نصب**: کپی به location مناسب

**استفاده**: به‌طور خودکار توسط Claude بارگذاری می‌شود

**AGENTS.md** (v2.1.277): به عنوان project instructions خوانده می‌شود وقتی `CLAUDE.md`، `.claude/CLAUDE.md` یا `CLAUDE.local.md` در یا بالای working directory وجود نداشته باشد — `02-memory/README.md#agentsmd` را ببینید

---
