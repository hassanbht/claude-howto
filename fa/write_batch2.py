import os

fa_dir = r"D:\Project\claude-howto\fa"

# File: 01-slash-commands/push-all.md
content = """---
description: استیج کردن تمام تغییرات، ایجاد commit و به‌روزرسانی از راه دور (با احتیاط استفاده شود)
allowed-tools: Bash(git add:*), Bash(git status:*), Bash(git commit:*), Bash(git push:*), Bash(git diff:*), Bash(git log:*), Bash(git pull:*)
---

# استیج و به‌روزرسانی تمام Contents

⚠️ **هشدار**: تمام تغییرات را استیج می‌کند، commit می‌کند و از راه دور به‌روزرسانی می‌کند. فقط استفاده کنید اگر اطمینان دارید تمام تغییرات باید در یک commit باشند.

## جریان کار

### 1. تحلیل تغییرات

به‌طور موازی اجرا کنید:
- `git status` - نمایش فایل‌های تغییر یافته/جدید/حذف شده/با تداخل
- `git diff --stat` - نمایش آمار تغییرات
- `git log -1 --oneline` - نمایش آخرین commit برای یکپarloifying استایل پیام commit

### 2. بررسی امنیت

**❌ اگر موارد زیر پیدا شد، بلافاصله متوقف شوید و هشدار دهید:**
- Secrets: `.env*`، `*.key`، `*.pem`، `credentials.json`، `secrets.yaml`، `id_rsa`، `*.p12`، `*.pfx`، `*.cer`
- کلیدهای API: هر متغیری که حاوی `*_API_KEY`، `*_SECRET`، `*_TOKEN` باشد و مقدار معتبر داشته باشد، نه مقادیر mengganti مانند `your-api-key`، `xxx`، `placeholder`
- فایل‌های بزرگ: `>10MB` بدون استفاده از Git LFS
- فایل‌های ساختگی: `node_modules/`، `dist/`، `build/`، `__pycache__/`، `*.pyc`، `.venv/`
- فایل‌های موقت: `.DS_Store`، `thumbs.db`، `*.swp`، `*.tmp`

**بررسی کلید API:**
بررسی کنید آیا در فایل‌های تغییر یافته الگوهای زیر وجود دارند:
```bash
OPENAI_API_KEY=sk-proj-xxxxx  # ❌ کلید معتبر شناسایی شد!
AWS_SECRET_KEY=AKIA...         # ❌ کلید معتبر شناسایی شد!
STRIPE_API_KEY=sk_live_...    # ❌ کلید معتبر شناسایی شد!

# ✅ مقادیر جایگزین قابل پذیرش:
API_KEY=your-api-key-here
SECRET_KEY=placeholder
TOKEN=xxx
API_KEY=<your-key>
SECRET=${YOUR_SECRET}
```

**✅ تأیید:**
- `.gitignore` صحیح پیکربندی شده است
- هیچ تداخلmerged وجود ندارد
- شاخه صحیح است (اگر `main`/`master` باشد هشدار دهید)
- کلید API فقط مقدار جایگزین است

### 3. درخواست تأیید

یک خلاصه نمایش دهید:
```
📊 خلاصه تغییرات:
- X فایل تغییر یافته، Y فایل جدید، Z فایل حذف شده
- مجموع: +AAA خط جدید، -BBB خط حذف

🔒 امنیت: ✅ بدون秘密 | ✅ بدون فایل بزرگ | ⚠️ [هشدار]
🌿 شاخه: [name] → origin/[name]

من می‌خواهم: git add . → commit → push

لطفاً 'yes' را برای ادامه یا 'no' برای لغو وارد کنید.
```

**قبل از دریافت "yes" صریح ادامه ندهید.**

### 4. اجرا (بعد از تأیید)

ترتیب بهینه اجرا کنید:
```bash
git add .
git status  # تأیید وضعیت استیج
```

### 5. تولید پیام commit

تغییرات را تجزیه و تحلیل کنید و یک conventional commit بسازید:

**فرمت:**
```
[type]: خلاصه کوتاه (حداکثر 72 کاراکتر)

- تغییر کلیدی 1
- تغییر کلیدی 2
- تغییر کلیدی 3
```

**انواع:** `feat`، `fix`، `docs`، `style`، `refactor`، `test`، `chore`، `perf`، `build`، `ci`

**نمونه:**
```
docs: به‌روزرسانی مستندات 개념، توضیحات کامل

- اضافه نمودار معماری و جدول
- نمونه کاربردی اضافه شده
- بخش بهترین شیوه‌ها گسترش یافت
```

### 6. commit و به‌روزرسانی

```bash
git commit -m "$(cat <<'EOF'
[پیام commit تولید شده]
EOF
)"
git push  # اگر شکست خورد: git pull --rebase && git push
git log -1 --oneline --decorate  # تأیید
```

### 7. تأیید موفقیت

```
✅ با موفقیت از راه دور به‌روزرسانی شد!

Commit: [hash] [message]
Branch: [branch] → origin/[branch]
Files changed: X (+insertions, -deletions)
```

## مدیریت خطا

- شکست `git add`: بررسی دسترسی، فایل‌های قفل شده، تایید化して شود که ذخیره راه‌اندازی شده است
- شکست `git commit`: رفع هوک‌های pre-commit، بررسی پیکربندی git (user.name/email)
- شکست `git push`:
  - غیر از fast-forward: `git pull --rebase && git push`
  - شاخه از راه دور ندارد: `git push -u origin [branch]`
  - شاخه محافظت شده: از جریان PR استفاده شود

## سناریوهای کاربردی

✅ **مناسب برای:**
- به‌روزرسانی مستندات چندفайلية
- همزمان شامل تست و مستندات برای ویژگی
- رفع باگ در چندین فایل
- بازسازی/فرمت화 پروژه级
- تغییرات پیکربندی

❌ **اجتناب کنید:**
- اگر مطمئن نیستید چه چیزی باید commit شود
- شامل secretها/داده‌های حساس
- شاخه محافظت شده بدون بازبینی
- وجود تداخلmerged
- اگر می‌خواهید تاریخچه commit دقیق‌تر باشد
- شکست هوک‌های pre-commit

## جایگزین‌ها

اگر کاربر control بیشتری می‌خواهد، پیشنهاد دهید:
1. **استیج انتخابی**: مشاهده و استیج فایل‌های خاص
2. **استیج تعاملی**: استفاده از `git add -p` انتخاب بلوک به بلوک
3. **جریان PR**: ایجاد شاخه → به‌روزرسانی → ایجاد PR (از دستور `/pr` استفاده شود)

**⚠️ به یاد داشته باشد**: قبل از به‌روزرسانی همیشه تغییرات را بررسی کنید. اگر مطمئن نیستید، استفاده از دستورات git جداگانه قابل کنترل‌تر است.
"""

with open(os.path.join(fa_dir, "01-slash-commands", "push-all.md"), "w", encoding="utf-8") as f:
    f.write(content)

print("push-all.md written!")