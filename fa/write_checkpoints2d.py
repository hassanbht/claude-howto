import os

fa_dir = r"D:\Project\claude-howto\fa"

content = """

## عیب‌یابی

### پیدا نشدن Checkpoints

- بررسی کنید آیا در نسخه Claude Code که این ویژگی را پشتیبانی می‌کند هستید
- تأیید کنید checkpoint خودکار غیرفعال نشده است
- peril.session را دوباره باز کنید و دوباره امتحان کنید

### شکست در Rewind

- تأیید کنید یک checkpoint معتبر انتخاب شده است
- بررسی کنید آیا محدودیت‌های مربوط به فایل سیستم یا مجوز وجود دارد
- ابتدا کد یا peril.session را به صورت جداگانه بازیابی کنید، سپس تصمیم بگیرید آیا هر دو را به صورت همزمان بازیابی کنید یا خیر

## یکپارچگی با Git

Checkpoints و git یک تکمیلی هستند:

- Checkpoints برای کاوش در peril.session و آزمایش امن استفاده می‌شوند
- Git برای حفظ پایدار تاریخچه کد استفاده می‌شود
- شما می‌توانید ابتدا از checkpoints برای کاوش سریع استفاده کنید، سپس طرح نهایی را در git commit کنید

## شروع سریع

### گردش کار پایه

```text
1. قبل از شروع تغییرات به صورت خودکار checkpoint ایجاد می‌شود
2. یک راه حل را امتحان کنید
3. اگر نتیجه مناسب نیست، دو بار Esc بزنید
4. گزینه rewind مناسب را انتخاب کنید
5. ادامه کاوش کنید یا طرح نهایی را ارسال کنید
```

### میانبرهای کلیدی

- `Esc` + `Esc`: باز کردن مرورگر checkpoints
- `/rewind`: ورود به antarmuka بازگشت از طریق دستور
- `/checkpoint`، `/undo`: نام مستعار برای `/rewind`

## چه زمانی باید rewind: مانیتور링 contexte

اگر این نشانه‌ها را متوجه شدید، معمولاً بهتر است بازگردید:

- راه فعلی پیچیده می‌شود و هنوز اینکه کدام راه است مشخص نیست
- تست قبلاً شکست داده است و مشکل ممکن است یک یا دو گام قبلی ایجاد شده باشد
- می‌خواهید دو روش پیاده‌سازی را مقایسه کنید
- می‌خواهید یک "نقطه شروع تمیز" برای ادامه کاوش داشته باشید

## مفاهیم مرتبط

- **حافظه**: contexte بلندمدت در peril.sessionهای مختلف، به [02-memory/README.md](../02-memory/README.md) مراجعه کنید
- **胡ک‌ها**: اتوماسیون رویداد، به [06-hooks/README.md](../06-hooks/README.md) مراجعه کنید
- **پلاگین‌ها**: مجموعه قابلیت‌های بسته‌بندی شده، به [07-plugins/README.md](../07-plugins/README.md) مراجعه کنید
- **ویژگی‌های پیشرفته**: شامل التخطيط و وظایف پس‌زمینه، به [09-advanced-features/README.md](../09-advanced-features/README.md) مراجعه کنید

## منابع بیشتر

- [راهنمای ریشه](../README.md)
- [مستندات رسمی checkpoint Claude Code](https://code.claude.com/docs/en/checkpointing)
- [راهنمای ویژگی‌های پیشرفته Claude Code](../09-advanced-features/README.md)

## جمع‌بندی

ارزش Checkpoints در این است که به شما اجازه می‌دهد با اطمینان خطا کنید. این ویژگی باعث می‌شود که "اولاً اجرا، سپس برای خطا بازگشت" امن شود، و به شما کمک می‌کند به سرعت به راه حل درست برسید.

---

**آخرین به‌روزرسانی**: ۱۸ آبان ۲۰۲۶
**نسخه Claude Code**: ۲.۱.۳۰۲
**منبع**:
- https://code.claude.com/docs/en/checkpointing
- https://code.claude.com/docs/en/commands
- https://code.claude.com/docs/en/settings-reference
"""

with open(os.path.join(fa_dir, "08-checkpoints", "README.md"), "a", encoding="utf-8") as f:
    f.write(content)

print("08-checkpoints/README.md part 2d written!")