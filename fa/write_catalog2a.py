import os

fa_dir = r"D:\Project\claude-howto\fa"

content = """

### دستورات سفارشی (نمونه‌ها)

| دستور | توضیح | سناریو کاربرد | دامنه |
|---------|-------------|-------------|--------|
| `/review-pr` | بازبینی Pull Request با بررسی امنیتی و تست | گردش کار PR | پروژه‌ای |
| `/doc-refactor` | بازسازی مستندات برای بهن明白了 | بهینه‌سازی مستندات | پروژه‌ای |
| `/generate-api-docs` | تولید مستندات API از کد | ایجاد مستندات API | پروژه‌ای |
| `/setup-ci-cd` | راه‌اندازی خط لوله CI/CD | اتوماسیون DevOps | پروژه‌ای |
| `/unit-test-expand` | گسترش پوشش تست یکتایی | اتوماسیون تست | پروژه‌ای |
| `/push-all` | استیج و commit همه تغییرات | استیج سریع | پروژه‌ای |

---

## حالت‌های مجاز (Permission Modes)

| حالت | توضیح | سناریو کاربرد |
|---------|-------------|-------------|
| `default` | حالت مجاز استاندارد | توسعه عمومی |
| `acceptEdits` | پذیرش خودکار ویرایش‌های فایل | گردش کار confident editing |
| `plan` | فقط تحلیل، تغییر در فایل‌ها | بازبینی، برنامه‌ریزی |
| `auto` | تایید خودکار عملیات امن | تعادل خودmayı و امنیت |
| `dontAsk` | اجرای فقط ابزارهای تایید شده قبلاً، بقیه رد شده | کاربر حرفه‌ای / اتوماسیون |
| `bypassPermissions` | بدون محدودیت | CI/CD، اسکریپت‌های معتبر |

---

## Subagentها

دستیارهای AI متخصص برای تسهیل کارهای پیچیده.

### Subagentهای داخلی

| نام | توضیح | سناریو کاربرد |
|---------|-------------|-------------|
| `code-reviewer` | بررسی کیفیت کد و مسائل امنیتی | بازبینی کد |
| `test-engineer` | استراتژی تست، پوشش و تولید تست | اتوماسیون تست |
| `documentation-writer` | نوشتن و به‌روزرسانی مستندات فنی | مستندات |
| `secure-reviewer` | بررسی امنیتی، معمولاً فقط-خواندن | بررسی امنیت |
| `implementation-agent` | پیاده‌سازی قابلیت و تغییر کد | پیاده‌سازی |
| `debugger` | شناسایی باگ و تحلیل استثناها | اشکال‌زدایی |

### Subagentهای سفارشی (نمونه‌ها)

| نام | توضیح | سناریو کاربرد | دامنه |
|---------|-------------|-------------|--------|
| `performance-analyzer` | تحلیل отставادگی و بهینه‌سازی | بررسی عملکرد | پروژه‌ای |
| `deployment-specialist` | مدیریت استقرار و rollback | استقرار DevOps | پروژه‌ای |
| `incident-commander` | پذیرش حادثه تولید | مدیریت حادثه | پروژه‌ای |
| `alert-analyzer` | تحلیل هشدارهای سیستم | مانیتورینگ | پروژه‌ای |
| `api-documenter` | تولید مستندات API | مستندات | پروژه‌ای |
| `code-commentator` | افزودن نظرات به کد | بهبود کد | پروژه‌ای |
| `example-generator` | تولید مثال‌های کد | آموزش | پروژه‌ای |

---

## مهارت‌ها

قابلیت‌های خود-حادثه-trigger همراه با اسکریپت‌ها و قالب‌ها.

### مهارت‌های داخلی

| نام | توضیح | سناریو کاربرد |
|---------|-------------|-------------|
| `code-review-specialist` | بازبینی جامع کد: امنیت، کیفیت، عملکرد | بازبینی کد |
| `doc-generator` | تولید مستندات API کامل | مستندات API |
| `refactor` | بازسازی سیستمندی کد بر اساس Fowler | بازسازی کد |
| `brand-voice` | بررسی لحن برند در خروجی | کپی‌رايتینگ |
| `blog-draft` | تولید قالب مقاله وبلاگ | محتوای وبلاگ |
| `claude-md` | مدیریت و بهینه‌سازی فایل CLAUDE.md | پیکربندی |

### مهارت‌های سفارشی (نمونه‌ها)

| نام | توضیح | سناریو کاربرد | دامنه |
|---------|-------------|-------------|--------|
| `docstring` | تولید docstring برای توابع | مستندات کد | پروژه‌ای |
| `optimize` | تحلیل کد برای مشکلات عملکرد | بهینه‌سازی | پروژه‌ای |
| `pr` | آماده‌سازی Pull Request | گردش کار PR | پروژه‌ای |
| `commit` | ایجاد commit با contexte | git workflow | پروژه‌ای |

---

## پلاquinها

مجموعه‌های قابلیت بسته‌بندی شده که به صورت یکپارچه قابل نصب هستند.

| نام | توضیح | السناريوهای کاربرد |
|---------|-------------|-------------|
| `devops-automation` | خط لوله DevOps کامل: استقرار،Rollback،انتظار،پ incident | استقرار و مدیریت incident |
| `pr-review` | بازبینی PR کامل: امنیت، تست، مستندات، کیفیت | بازبینی Pull Request |
| `documentation` | توليد مستندات کامل پروژه | مستنداتowania |

---

## سرورهای MCP

هادرهای MCP برای دسترسی به ابزارها و داده‌های خارجی.

| نام | توضیح | سناریو کاربرد |
|---------|-------------|-------------|
| *هیچ سرور داخلی نیست* | - | - |

---

## هوک‌ها (Hooks)

اسکریپت‌های اتوماسیون مدفوع-رویداد.

### انواع رویدادهای هوک

| گروه | رویدادها |
|---------|-------------|
| Tool Hooks | PreToolUse، PostToolUse، PostToolUseFailure، PostToolBatch، PermissionRequest، PermissionDenied |
| Session Hooks | SessionStart، Setup، SessionEnd، Stop، StopFailure، SubagentStart، SubagentStop |
| Task Hooks | UserPromptSubmit، UserPromptExpansion، MessageDisplay، TaskCompleted، TaskCreated، TeammateIdle |
| Lifecycle Hooks | ConfigChange، CwdChanged، DirectoryAdded، FileChanged، PreCompact، PostCompact، PreModelSwitch، PostModelSwitch، WorktreeCreate، WorktreeRemove، Notification، InstructionsLoaded، Elicitation، ElicitationResult |

---

## فایل‌های Memory (حافظه)

فایل‌های contexte پایدار برای peril.sessionهای مختلف.

| نام | توضیح | دامنه | محل |
|---------|-------------|-------------|--------|
| `project-CLAUDE.md` | استانداردهای تیمی پروژه | کل پروژه | `./CLAUDE.md` |
| `directory-api-CLAUDE.md` | قوانین ویژه API | سطح دایرکتوری | `./src/api/CLAUDE.md` |
| `personal-CLAUDE.md` | ترجیحات شخصی | سطح کاربر | `~/.claude/CLAUDE.md` |

"""
with open(os.path.join(fa_dir, "CATALOG.md"), "a", encoding="utf-8") as f:
    f.write(content)

print("CATALOG.md part 2a written!")