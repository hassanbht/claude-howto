# برنامه ترجمه فارسی (Persian Translation Plan)

## وضعیت کلی

- مسیر ترجمه: `D:\Project\claude-howto\fa\`
- الگوی ساختار: همان ساختار ریپوی اصلی (فایل‌ها با همان مسیر نسبی در `fa/` قرار می‌گیرند)
- قوانین ترجمه:
  - **متن توضیحات، عنوان‌ها، توضیحات جداول → فارسی**
  - **دستورات، flagها، نام فایل‌ها، نام ابزارها، کد → انگلیسی (ترجمه نشود)**
  - **کدهای داخل code block → بدون تغییر**
  - **لینک‌ها → حفظ مسیر، فقط متن anchor ترجمه شود**

## فایل‌های ترجمه‌شده (۵ فایل)

- `fa/03-skills/doc-generator/SKILL.md`
- `fa/04-subagents/clean-code-reviewer.md`
- `fa/04-subagents/data-scientist.md`
- `fa/04-subagents/performance-optimizer.md`
- `fa/10-cli/README.md`

## مراحل پیشنهادی (Priority Order)

### Phase 1 — راهنماها و مستندات اصلی (High Priority)
1. `README.md` (root)
2. `INDEX.md`
3. `LEARNING-ROADMAP.md`
4. `QUICK_REFERENCE.md`
5. `claude_concepts_guide.md`
6. `resources/QUICK-START.md`
7. `resources/README.md`

### Phase 2 — ماژول‌های numbered (01–09)
- `01-slash-commands/README.md` + تمام command mdها (متن توضیحات فقط)
- `02-memory/README.md`
- `03-skills/README.md` + SKILL.mdها (فقط توضیحات، دستورات نه)
- `04-subagents/README.md` + agent mdها
- `05-mcp/README.md`
- `06-hooks/README.md`
- `07-plugins/README.md` + plugin files
- `08-checkpoints/README.md`
- `09-advanced-features/README.md`

### Phase 3 — CLI (تکمیل)
- `10-cli/README.md` ✓ (done)

### Phase 4 — منابع و docs
- `resources/*.md`
- `docs/*.md`
- `prompts/*.md`
- `scripts/README.md`

### Phase 5 — فایل‌های ریشه (meta)
- `CATALOG.md`, `CHANGELOG.md`, `CLAUDE.md`, `CONTRIBUTING.md`, `CODE_OF_CONDUCT.md`, `SECURITY.md`, `STYLE_GUIDE.md`, `clean-code-rules.md`, `resources.md`

### Phase 6 — GitHub templates (اختیاری)
- `.github/ISSUE_TEMPLATE/*.md`
- `.github/pull_request_template.md`

### Phase 7 — Skills داخلی (اختیاری)
- `.claude/skills/*/SKILL.md` و references

## فایل‌هایی که ترجمه نمی‌شوند
- کدهای داخل code block
- دستورات shell/CLI
- نام‌های فایل، pathها، flagها
- frontmatter keys در SKILL.md (name, description keys باید حفظ شوند، فقط values ترجمه)

## مراحل اجرا
برای هر فایل:
1. خواندن فایل اصلی
2. ترجمه متن (نه دستورات)
3. ایجاد فایل معادل در `fa/<relative-path>`
4. بررسی diff و commit

## تخمین حجم
- ۱۰۹ فایل markdown برای ترجمه
- ~۴۰۰k کاراکتر متن
- پیشنهاد: ترجمه تدریجی در چند PR/commit
