import os

fa_dir = r"D:\Project\claude-howto\fa"

content = """

## گردش کار کامل مثالی

### گردش کار کامل پلاquin بازبینی PR

```
1. کاربر: /review-pr

2. پلاquin اجرا می‌کند:
   ├──胡ک pre-review.js گنجینه git را تایید می‌کند
   ├── سرور MCP GitHub داده‌های PR را دریافت می‌کند
   ├── Subagent security-reviewer امنیت را تحلیل می‌کند
   ├── Subagent test-checker پوشش تست را تایید می‌کند
   └── Subagent performance-analyzer عملکرد را بررسی می‌کند

3. جمع‌آوری و نمایش نتایج:
   ✅ امنیت: مشکلی پیدا نشد
   ⚠️  تست: پوشش ۶۵٪ (پیشنهاد ۸۰٪+)
   ✅ عملکرد: تأثیری penting نیست
   📝 ۱۲ پیشنهاد ارائه شد
```

## عیب‌یابی

### پلاquin نصب نمی‌شود

- بررسی سازگاری نسخه کلود کد: `claude --version`
- اعتبارسنجی نحوی `plugin.json` با یک GitHub Schema
- بررسی اتصال شبکه (پلاquin‌های از راه دور)
- بررسی مجوز: `ls -la plugin/`

### اجزا بارگذاری نمی‌شوند

- تأیید مسیرها در `plugin.json` با ساختار دایرکتوری واقعی مطابقت دارند
- بررسی مجوز فایل: `chmod +x scripts/`
- بررسی نحوی فایل‌های componente
- مشاهده فهرست componente: `claude plugin details plugin-name`

### اتصال MCP شکست می‌خورد

- تأیید متغیرهای محیطی صحیح تنظیم شده‌اند
- بررسی نصب و وضعیت سلامت سرور MCP
- از `/mcp` برای مشاهده وضعیت سرورهای MCP استفاده کنید
- مشاهده پیکربندی MCP در پوشه `mcp/`

### دستورات پس از نصب در دسترس نیستند

- تأیید نصب موفقیت‌آمیز پلاquin: `/plugin list`
- بررسی فعال بودن پلاquin: `/plugin list --enabled`
- تأیید اینکه فعال شده است — به بخش [نحوه نصب](#نحوه-نصب) مراجعه کنید: `Plugin is now active.` نشان می‌دهد نیازی به عملیات دیگری نیست، `Run /reload-plugins to activate.` نشان می‌دهد دستور را اجرا کنید (بدون نیاز به راه‌اندازی مجدد)
- بررسی تداخل با دستورات موجود

### مشکل اجرای胡ک

- تأیید مجوزهای فایل胡ک صحیح هستند
- بررسی نحوی胡ک و نام رویداد
- بررسی لاگ‌های胡ک برای جزئیات خطا
- در صورت امکان،胡کها را به صورت دستی تست کنید

## منابع بیشتر

- [مستندات رسمی پلاquin](https://code.claude.com/docs/en/plugins)
- [کشف پلاquin](https://code.claude.com/docs/en/discover-plugins)
- [مارکت پلاquin](https://code.claude.com/docs/en/plugin-marketplaces)
- [مرجع پلاquin](https://code.claude.com/docs/en/plugins-reference)
- [مرجع سرور MCP](https://modelcontextprotocol.io/)
- [راهنمای پیکربندی Subagent](../04-subagents/README.md)
- [مرجع سیستم胡ک‌ها](../06-hooks/README.md)

---

**آخرین به‌روزرسانی**: ۱۸ آبان ۲۰۲۶
**نسخه کلود کد**: ۲.۱.۳۰۲
**منبع**:
- https://code.claude.com/docs/en/discover-plugins
- https://code.claude.com/docs/en/plugins-reference
- https://code.claude.com/docs/en/settings
- https://code.claude.com/docs/en/plugins/install
- https://code.claude.com/docs/en/plugins/cli-reference
- https://code.claude.com/docs/en/plugins/manifest-reference
- https://code.claude.com/docs/en/plugins/marketplace-reference
- https://code.claude.com/docs/en/plugins/components
- https://code.claude.com/docs/en/plugins/publish
- https://code.claude.com/docs/en/plugins/overview
"""

with open(os.path.join(fa_dir, "07-plugins", "README.md"), "a", encoding="utf-8") as f:
    f.write(content)

print("07-plugins/README.md part 3 written!")