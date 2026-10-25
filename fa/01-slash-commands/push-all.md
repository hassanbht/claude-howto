---
description: stage کردن همه تغییرات، ایجاد commit و push به remote (با احتیاط استفاده شود)
allowed-tools: Bash(git add:*), Bash(git status:*), Bash(git commit:*), Bash(git push:*), Bash(git diff:*), Bash(git log:*), Bash(git pull:*)
---

# commit و push همه چیز

⚠️ **هشدار**: همه تغییرات را stage می‌کند، commit می‌سازد و به remote ارسال می‌کند. فقط زمانی استفاده کنید که مطمئن هستید همه تغییرات متعلق به یک کار هستند.

## گردش کار

### ۱. تحلیل تغییرات

به‌صورت موازی اجرا کنید:
- `git status` - نمایش فایل‌های تغییر یافته/اضافه شده/حذف شده/untracked
- `git diff --stat` - نمایش آمار تغییرات
- `git log -1 --oneline` - نمایش commit اخیر برای سبک پیام

### ۲. بررسی‌های ایمنی

**❌ توقف و هشدار در صورت شناسایی:**
- اسرار: `.env*`, `*.key`, `*.pem`, `credentials.json`, `secrets.yaml`, `id_rsa`, `*.p12`, `*.pfx`, `*.cer`
- کلیدهای API: هر متغیر `*_API_KEY`, `*_SECRET`, `*_TOKEN` با مقادیر واقعی (نه placeholderهایی مثل `your-api-key`, `xxx`, `placeholder`)
- فایل‌های بزرگ: `>10MB` بدون Git LFS
- artifactهای build: `node_modules/`, `dist/`, `build/`, `__pycache__/`, `*.pyc`, `.venv/`
- فایل‌های موقت: `.DS_Store`, `thumbs.db`, `*.swp`, `*.tmp`

**اعتبارسنجی کلید API:**
فایل‌های تغییر یافته را برای الگوهایی مثل زیر بررسی کنید:
```bash
OPENAI_API_KEY=sk-proj-xxxxx  # ❌ کلید واقعی شناسایی شد!
AWS_SECRET_KEY=AKIA...         # ❌ کلید واقعی شناسایی شد!
STRIPE_API_KEY=sk_live_...    # ❌ کلید واقعی شناسایی شد!

# ✅ placeholderهای قابل قبول:
API_KEY=your-api-key-here
SECRET_KEY=placeholder
TOKEN=xxx
API_KEY=<your-key>
SECRET=${YOUR_SECRET}
```

**✅ تأیید:**
- `.gitignore` به‌درستی پیکربندی شده
- بدون تعارض merge
- شاخه صحیح (در صورت main/master هشدار دهید)
- کلیدهای API فقط placeholder هستند

### ۳. درخواست تأیید

خلاصه را ارائه دهید:
```
📊 خلاصه تغییرات:
- X فایل تغییر یافته، Y اضافه، Z حذف
- مجموع: +AAA درج، -BBB حذف

🔒 ایمنی: ✅ بدون اسرار | ✅ بدون فایل بزرگ | ⚠️ [هشدارها]
🌿 شاخه: [name] → origin/[name]

من این کار را انجام می‌دهم: git add . → commit → push

برای ادامه 'yes' یا برای لغو 'no' تایپ کنید.
```

**پیش از ادامه برای دریافت تأیید صریح «yes» صبر کنید.**

### ۴. اجرا (پس از تأیید)

به‌ترتیب اجرا کنید:
```bash
git add .
git status  # تأیید staging
```

### ۵. تولید پیام commit

تغییرات را تحلیل کنید و یک conventional commit ایجاد کنید:

**قالب:**
```
[type]: خلاصه کوتاه (حداکثر ۷۲ کاراکتر)

- تغییر کلیدی ۱
- تغییر کلیدی ۲
- تغییر کلیدی ۳
```

**typeها:** `feat`, `fix`, `docs`, `style`, `refactor`, `test`, `chore`, `perf`, `build`, `ci`

**مثال:**
```
docs: به‌روزرسانی فایل‌های README مفهومی با مستندات جامع

- افزودن نمودارهای معماری و جداول
- شامل مثال‌های عملی
- گسترش بخش‌های بهترین شیوه‌ها
```

### ۶. commit و push

```bash
git commit -m "$(cat <<'EOF'
[پیام commit تولید شده]
EOF
)"
git push  # در صورت شکست: git pull --rebase && git push
git log -1 --oneline --decorate  # تأیید
```

### ۷. تأیید موفقیت

```
✅ با موفقیت به remote push شد!

Commit: [hash] [message]
Branch: [branch] → origin/[branch]
Files changed: X (+insertions, -deletions)
```

## مدیریت خطا

- **git add ناموفق**: بررسی مجوزها، فایل‌های قفل‌شده، تأیید مقداردهی اولیه repo
- **git commit ناموفق**: رفع pre-commit hookها، بررسی git config (user.name/email)
- **git push ناموفق**:
  - Non-fast-forward: `git pull --rebase && git push`
  - بدون شاخه remote: `git push -u origin [branch]`
  - شاخه محافظت‌شده: به جای آن از گردش کار PR استفاده کنید

## چه زمانی استفاده شود

✅ **مناسب:**
- به‌روزرسانی‌های مستندات چندفایلی
- قابلیت با تست و مستندات
- رفع باگ در فایل‌های مختلف
- قالب‌بندی/بازسازی در سراسر پروژه
- تغییرات پیکربندی

❌ **اجتناب:**
- عدم اطمینان از آنچه commit می‌شود
- شامل اسرار/داده‌های حساس
- شاخه‌های محافظت‌شده بدون بازبینی
- وجود تعارض merge
- نیاز به تاریخ commit با دانه‌بندی ریز
- شکست pre-commit hookها

## جایگزین‌ها

اگر کاربر کنترل می‌خواهد، این موارد را پیشنهاد دهید:
1. **stage انتخابی**: بازبینی/stage کردن فایل‌های خاص
2. **stage تعاملی**: `git add -p` برای انتخاب patch
3. **گردش کار PR**: ایجاد شاخه → push → PR (از دستور `/pr` استفاده کنید)

**⚠️ به یاد داشته باشید**: همیشه پیش از push تغییرات را بازبینی کنید. در صورت تردید، از دستورات git تکی برای کنترل بیشتر استفاده کنید.

---
**آخرین به‌روزرسانی**: ۴ اوت ۲۰۲۶
**نسخه کلود کد**: ۲.۱.۲۲۰
**منبع**:
- https://code.claude.com/docs/en/commands
**مدل‌های سازگ**: Claude Fable 5, Claude Opus 5, Claude Sonnet 5, Claude Sonnet 4.6, Claude Opus 4.8, Claude Haiku 4.5
