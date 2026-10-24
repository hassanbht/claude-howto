import os

fa_dir = r"D:\Project\claude-howto\fa"

content = """

```markdown
---
name: بهینه‌سازی کد
description: تحلیل مشکلات عملکردی و پیشنهاد بهینه‌سازی
tags: performance, analysis
---

# تحلیل و بهینه‌سازی کد

بر اساس اولویت‌های زیر، مسائل کد را بررسی کنید:

۱. **نقطه‌های عملکردی** - شناسایی عملیات O(n²) و حلقه‌های ناکارآمد
۲. **ناآșس‌اند حافظه** - یافتن منابع آزادنشده، ارجاعات دایره‌ای
۳. **بهبود الگوریتم** - پیشنهاد الگوریتم یا ساختار داده بهتر
۴. **فرصت‌های کش** - شناسایی محاسبات تکراری
۵. **مشکلات همزمانی** - شناسایی شرایط رقابت یا مشکلات thread

خروجی را به این فرمت ارائه دهید:
- شدت مشکل (Critical/High/Medium/Low)
- مکان کد
- توضیح
- راه‌حل پیشنهادی همراه با مثال کد
```

**استفاده:**

```bash
# کاربر در کلود کد ورودی می‌دهد
/optimize

# کلود کد محتوا را بارگذاری می‌کند و منتظر کد می‌ماند
```

---

#### مثال ۲: دستور آماده‌سازی Pull Request

**فایل**: `.claude/commands/pr.md`

```markdown
---
name: آماده‌سازی Pull Request
description: پاک‌سازی کد، استیج کردن تغییرات و آماده‌سازی یک Pull Request
tags: git, workflow
---

# فهرست آماده‌سازی Pull Request

قبل از ایجاد PR، مراحل زیر را انجام دهید:

۱. اجرای فرمت‌سازی: `prettier --write .`
۲. اجرای تست‌ها: `npm test`
۳. مشاهده git diff: `git diff HEAD`
۴. استیج کردن تغییرات: `git add .`
۵. ایجاد پیام commit با قوانین conventional commits:
  - `fix:` رفع باگ
  - `feat:` ویژگی جدید
  - `docs:` مستندات
  - `refactor:` بازسازی کد
  - `test:` تست‌های جدید
  - `chore:` نگهداری

۶. تولید خلاصه PR که شامل موارد زیر باشد:
  - چه چیزی تغییر کرد
  - چرا تغییر کرد
  - چه تست‌هایی انجام شد
  - پیامدهای احتمالی
```

**استفاده:**

```bash
/pr

# کلود کد لیست را از بالا به پایین بررسی می‌کند و PR را آماده می‌کند
```

---

## Slash Commands vs دیگر قابلیت‌ها

| قابلیت | روش فعال‌سازی | سناریو براساس کاربرد |
|--------|----------------------|
| **Skill‌ها** | خودکار / نیمه‌خودکار | قابلیت‌های قابل استفاده مجدد، استانداردسازی گردش کار |
| **دستورات Slash** | دستی | دستورات سریع |
| **Subagentها** | خودکار محتمل | تکمیل وظایف از طریق فراخوانی |


---
```

with open(os.path.join(fa_dir, "claude_concepts_guide.md"), "a", encoding="utf-8") as f:
    f.write(content)
print("claude_concepts_guide.md part 2 written!")
"""
with open(os.path.join(fa_dir, "claude_concepts_guide.md"), "a", encoding="utf-8") as f:
    f.write(content)

print("claude_concepts_guide.md part 2 written!")