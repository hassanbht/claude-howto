import os

fa_dir = r"D:\Project\claude-howto\fa"

content = ""

# Add the security and architecture sections
content = """

## امنیت Subagent در پلاگین

subagent‌های توزیع شده در پلاگین باید به مجوزها، دامنه ابزار و شرایط مرز توجه ویژه‌ای داشته باشند.

## معماری

### معماری بلندمدت

دستیار اصلی، subagent، سیستم فایل و مجوزهای ابزار به’ensemble زنجیره اجرا را تشکیل می‌دهند.

### چرخه عمر

1. ایجاد
2. تفویض وظیفه
3. اجرا
4. بازگشت نتیجه
5. پایان یا بازیابی

## مدیریت زمینه

### نکات کلیدی

- زمینه زیرد minimal باشد
- هر subagent فقط به کارهای خود مسئولیت بپذیرد
- همه اطلاعات را در یک جا decisión نکنید

### ملاحظات عملکرد

بیش از حد بالا بودن سرعت را کاهش می‌دهد و درستی را پایین می‌آورد.

### رفتار کلیدی

subagent در زمینه ایزولته کار می‌کند، اما می‌تواند نتیجه را به peril.session اصلی بازگرداند.

## چه زمانی از Subagent استفاده کنیم

- وظیفه را می‌توان تفکیک کرد
- نیاز به ایزولاسیون زمینه
- نیاز به تقطيع واضح نقش‌ها
- نیاز به همکاری موازی

## بهترین شیوه‌ها

### اصول طراحی

- مسئولیت واحد
- توضیحات مشخص
- به حداقل رساندن مجوزهای ابزار

### بهترین شیوه‌ها برای System Prompt

- توضیحات وظیفه را مشخص بنویسید
- خیلی طولانی ننویسید
- فقط اطلاعات مورد نیاز برای انجام وظیفه را حفظ کنید

### استراتژی دسترسی به ابزار

- subagent بازبینیی فقط-خواندن
- subagent اجرا Ilende به程度 محدود حق نوشتن
- اقدامات با ریسک بالا باید تایید شوند

## مثال‌های Subagent در این دایرکتوری

### ۱. [Code Reviewer](./code-reviewer.md)

برای بازبینی جامع کیفیت کد.

### ۲. [Test Engineer](./test-engineer.md)

برای استراتژی تست، پوشش و تولید تست.

### ۳. [Documentation Writer](./documentation-writer.md)

برای نوشتن و به‌روزرسانی مستندات فنی.

### ۴. [Secure Reviewer](./secure-reviewer.md)

برای بررسی‌های امنیتی، معمولاً فقط-خواندن.

### ۵. [Implementation Agent](./implementation-agent.md)

برای پیاده‌سازی قابلیت و تغییر کد.

### ۶. [Debugger](./debugger.md)

برای شناسایی باگ و تجزیه و تحلیل استثناها.

### ۷. [Data Scientist](./data-scientist.md)

برای تحلیل داده، تفسیر نتایج و تولید گزارش.

### ۸. [Clean Code Reviewer](./clean-code-reviewer.md)

برای بازبینی متمرکز بر اصول Clean Code.
"""

with open(os.path.join(fa_dir, "04-subagents", "README.md"), "a", encoding="utf-8") as f:
    f.write(content)

print("04-subagents/README.md part 4 written!")