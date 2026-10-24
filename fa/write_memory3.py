import os

fa_dir = r"D:\Project\claude-howto\fa"

content = """

## بهترین شیوه‌ها

### چیزی که باید انجام دهید

- از حافظه پروژه برای حفظ استانداردهای تیم استفاده کنید
- از حافظه دایرکتوری برای حفظ تفاوت‌های محلی استفاده کنید
- ابتدا قوانین خلاصه بنویسید، سپس به تدریج تکمیل کنید
- محتوای تکرارپذیر را در `CLAUDE.md` بنویسید

### چیزی که نباید انجام دهید

- کل README را نocalize در `CLAUDE.md` نکنید
- جزئیات اجرای کد را به طور Пуств維 در حافظه ننوشتد
- حافظه را سطل زباله نکنید

### پیشنهادات مدیریت حافظه

- به مستندات موجود ارجاع دهید، نه کپی و چسباندن تکراری
- فقط اطلاعاتی که واقعاً رفتار Claude را تحت تأثیر قرار می‌دهد را نگه دارید
- laws‌های منسوخ یا تداخل شده را به طور منظم سازماندهی کنید

## راهنمای نصب

### تنظیم حافظه پروژه

#### روش ۱: استفاده از `/init` (توصیه می‌شود)

```bash
/init
```

#### روش ۲: ایجاد دستی

```bash
cp project-CLAUDE.md CLAUDE.md
```

#### روش ۳: به‌روزرسانی سریع

```text
# Use semantic versioning for all releases
# Always run tests before committing
# Prefer composition over inheritance
```

### تنظیم حافظه کاربر

```bash
cp personal-CLAUDE.md ~/.claude/CLAUDE.md
```

### تنظیم حافظه دایرکتوری

```bash
cp directory-api-CLAUDE.md src/api/CLAUDE.md
```

### تأیید نصب

- peril.session Claude Code را دوباره باز کنید
- بررسی کنید `CLAUDE.md` به صورت خودکار بارگذاری شده است
- با یک نشانه‌گذاری که明显 تحت تأثیر حافظه قرار می‌گیرد، تست کنید

## مستندات رسمی

اگر می‌خواهید تعریف‌های رفتاری دقیق‌تر، سازگاری و محدودیت‌های جدید را ببینید، به مستندات رسمی حافظه Claude Code مراجعه کنید.

## مفاهیم مرتبط

- [مرجع دستورات Slash](../01-slash-commands/README.md)
- [راهنمای Skills](../03-skills/README.md)
- [مرجع Subagents](../04-subagents/README.md)
- [راهنمای ویژگی‌های پیشرفته](../09-advanced-features/README.md)
"""

with open(os.path.join(fa_dir, "02-memory", "README.md"), "a", encoding="utf-8") as f:
    f.write(content)

print("02-memory/README.md part 3 written!")