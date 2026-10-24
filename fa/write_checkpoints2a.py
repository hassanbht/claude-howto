import os

fa_dir = r"D:\Project\claude-howto\fa"

content = """

## نحوه استفاده از Checkpoints

### مشاهده و بازگردانی

دو بار `Esc` را بزنید، یا از `/rewind` برای باز کردن مرورگر checkpoints استفاده کنید. شما antarmuka‌ای از checkpoints موجود با تاریخچه می‌بینید. هر checkpoint را انتخاب کنید تا به آن وضعیت بازگردید.

## جزئیات Checkpoint

هر checkpoint موارد زیر را نمایش می‌دهد:

- زمان ایجاد
- فایل‌های تغییر یافته
- تعداد پیام‌ها در peril.session
- ابزارهای استفاده شده
"""

with open(os.path.join(fa_dir, "08-checkpoints", "README.md"), "a", encoding="utf-8") as f:
    f.write(content)

print("08-checkpoints/README.md part 2a written!")