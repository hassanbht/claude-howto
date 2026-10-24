import os

fa_dir = r"D:\Project\claude-howto\fa"

content = """<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../resources/logos/claude-howto-logo-dark.svg">
  <img alt="Claude How To" src="../resources/logos/claude-howto-logo.svg">
</picture>

# فهرست قابلیت‌های کلود کد

> یک مرجع سریع برای همه قابلیت‌های کلود کد: دستورات، agentها، مهارت‌ها، پلاquinها و胡ک‌ها.

**تنقل**: [دستورات slash](#دستورات-slash) | [حالت‌های مجاز](#حالت‌های-مجاز) | [Subagentها](#subagentها) | [مهارت‌ها](#مهارت‌ها) | [پلاquinها](#پلاquinها) | [سرورهای MCP](#سرورهای-mcp) | [هوک‌ها](#هوک‌ها) | [فایل‌های Memory](#فایل‌های-memory) | [ویژگی‌های جدید مارس ۲۰۲۶](#ویژگی‌های-جدید-مارس-۲۰۲۶)

---

## مرور کلی

| قابلیت | داخلی | مثال | مجموع | مرجع |
|---------|----------|----------|-------|-----------|
| **دستورات Slash** | ۶۰+ | ۸ | ۶۸+ | [۰۱-دستورات-slash/README.md](01-slash-commands/README.md) |
| **Subagentها** | ۶ | ۸ | ۱۴ | [۰۴-subagents/README.md](04-subagents/README.md) |
| **مهارت‌ها** | ۱۰ داخلی | ۶ | ۱۶ | [۰۳-مهارت‌ها/README.md](03-skills/README.md) |
| **پلاquinها** | - | ۳ | ۳ | [۰۷-پلاquinها/README.md](07-plugins/README.md) |
| **سرورهای MCP** | - | ۰ | ۰ | [۰۵-mcp/README.md](05-mcp/README.md) |
| **هوک‌ها** | ۳۳ رویداد | ۰ | ۳۳ | [۰۶-هوک‌ها/README.md](06-hooks/README.md) |
| **Memory** | ۷ نوع | ۳ | ۱۰ | [۰۲-pāyādar/README.md](02-memory/README.md) |
| **مجموع** | **۱۱۶** | **۲۸** | **۱۴۴** | |

---

## دستورات Slash

دستورهای کاربر-manual برای انجام وظایف خاص.

### دستورات داخلی

| دستور | توضیح | سناریو کاربرد |
|---------|-------------|-------------|
| `/help` | نمایش اطلاعات راهنما | شروع یادگیری، آموختن دستورات |
| `/btw` | پرسیدن سوال اضافی بدون نوشتن در contexte | تکمیل موقت سوال |
| `/chrome` | پیکربندی ادغام کروم | اتوماسیون مرورگر |
| `/clear` | پاک کردن تاریخچه peril.session | شروع مجدد، کاهش contexte |
| `/diff` | نمایشگر diff تعاملی | بررسی تغییرات |
| `/config` | نمایش/ویرایش پیکربندی | سفارشی‌سازی رفتار |
| `/status` | نمایش وضعیت peril.session | بررسی وضعیت فعلی |
| `/agents` | حذف شده: راهنمای در v2.1.198 حذف شد، این دستور در v2.1.281 از منوی `/` و `/help` حذف شده — لطفاً به Claude بگویید تا subagent بسازد یا مدیریت کند، یا `.claude/agents/` را ویرایش کنید | اجازه به Claude برای مدیریت subagentها |
| `/skills` | لیست مهارت‌های موجود | مشاهده قابلیت‌های خود-حادثه-trigger |
| `/hooks` | لیست胡ک‌های پیکربندی شده | اشکال‌زدایی اتوماسیون |
| `/insights` | تحلیل الگوهای peril.session | بهینه‌سازی استفاده از peril.session |
| `/install-slack-app` | نصب برنامه Slack Claude | ادغام Slack |
| `/keybindings` | سفارشی‌سازی میانبرهای کلید | تنظیم کلیدها |
| `/mcp` | لیست سرورهای MCP | بررسی یکپارچگی‌های خارجی |
| `/memory` | نمایش فایل‌های memory بارگذاری شده | عیب‌ジャー بارگذاری contexte |
| `/mobile` | تولید کد QR موبایل | دسترسی از تلفن همراه |
| `/passes` | Sharing یک هفته رایگان Claude Code با دوستان (فقط حساب‌های sure) | توصیه به دوستان |
| `/plugin` | مدیریت پلاquinها | نصب/حذف افزونه‌ها |
| `/plan` | ورود به حالت برنامه‌ریزی | پیاده‌سازی پیچیده |
| `/rewind` | بازگشت به checkpoint | لغو تغییرات، کاوش گزینه‌های جایگزین |
| `/checkpoint` | نام مستعار `/rewind` | همان `/rewind` |
| `/cost` | نمایش مصرف توکن | نظارت بر هزینه‌ها |
| `/context` | نمایش استفاده از janbe contexte | مدیریت طول peril.session |
| `/export` | خروجی peril.session | ذخیره برای مرجع |
| `/extra-usage` | پیکربندی محدودیت‌های استفاده اضافی | مدیریت نرخ |
| `/feedback` | ارسال بازخورد یا گزارش باگ | گزارش مشکل |
| `/login` | احراز هویت از طریق Anthropic | دسترسی به قابلیت‌ها |
| `/logout` | خروج از حساب | تغییر حساب |
| `/sandbox` | تغییر حالت sandbox | اجرای امن دستورات |
| `/doctor` | اجرای تشخیص | عیب‌ジャー |
| `/reload-plugins` | بارگذاری مجدد پلاquinهای نصب شده. از v2.1.221 به بعد، بیشتر نصب‌ها به طور فوری فعال می‌شوند؛ فقط وقتی خلاصه-install نشان می‌دهد `Run /reload-plugins to activate.` نیاز است | مدیریت پلاquin |
| `/release-notes` | نمایش توضیحات آپدیت | مشاهده ویژگی‌های جدید |
| `/remote-control` | فعال‌سازی کنترل از راه دور | دسترسی از راه دور |
| `/permissions` | مدیریت مجوزها | کنترل دسترسی |
| `/rename` | تغییر نام peril.session فعلی | سازمانdding peril.sessionها |
| `/resume` | بازیابی peril.session قبلی | ادامه کار |
| `/tasks` | نمایش وظایف پس‌زمینه | نظارت بر عملیات async |
| `/copy` | کپی آخرین پاسخ به کلیپ بورد | به اشتراک گذاشتن سریع خروجی |
| `/teleport` | انتقال peril.session به ماشین دیگر | ادامه کار از راه دور |
| `/desktop` | باز کردن برنامه Claude Desktop | تغییر به رابط دسکتاپ |
| `/theme` | تغییر رنگ posed | سفارشی‌سازی ظاهر |
| `/usage` | نمایش آمار استفاده از API | نظارت بر سهم و مصرف |
| `/fork` | کپی peril.session فعلی به یک peril.session پس‌زمینه جدید (v2.1.212+) | کاوش موازی گزینه‌های جایگزین |
| `/subtask` | ایجاد یک subagent forked که peril.session کامل را ارث می‌برد، نتیجه را به peril.session فعلی برمی‌گرداند (v2.1.212+) | تفویض وظایف جانبی بدون متدelling sketch |
| `/stats` | نمایش آمار peril.session | مشاهده شاخص‌های peril.session |
| `/statusline` | پیکربندی وضعیت خط | سفارشی‌سازی نمایش وضعیت |
| `/stickers` | سفارش březهای Claude Code | جایزه تفریحی |
| `/fast` | تغییر حالت خروجی سریع | شتاب دادن پاسخ |
| `/terminal-setup` | پیکربندی ادغام ترمینال | تنظیم ویژگی‌های ترمینال |
| `/upgrade` | باز کردن صفحه ارتقا برای تغییر به طرح بالاتر | ارتقا طرح |

### دستورات سفارشی (نمونه‌ها)

| دستور | توضیح | سناریو کاربرد | دامنه |
|---------|-------------|-------------|--------|
"""
with open(os.path.join(fa_dir, "CATALOG.md"), "w", encoding="utf-8") as f:
    f.write(content)

print("CATALOG.md part 1 written!")