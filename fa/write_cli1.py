import os

fa_dir = r"D:\Project\claude-howto\fa"

content = """<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../../resources/logos/claude-howto-logo-dark.svg">
  <img alt="Claude How To" src="../../resources/logos/claude-howto-logo.svg">
</picture>

# مرجع CLI

## مرور کلی

CLI (رابط خط فرمان) کلود کد، روش اصلی برای تعامل با کلود کد است. پارامترهای و دستورات قدرتمند آن برای اجرای پرس‌وجو، مدیریت سیشن، انتخاب مدل و یکپارچگی کلود کد در گردش‌کارهای توسعه شما فراهم می‌کند.

## معماری

```mermaid
graph TD
    A["ترمینال کاربر"] -->|\"claude [options] [query]\"| B["CLI کلود کد"]
    B -->|تعاملی| C["حالت REPL"]
    B -->|\"--print\"| D["حالت چاپ (SDK)"]
    B -->|\"--resume\"| E["بازیابی سیشن"]
    C -->|گفتگو| F["API کلود"]
    D -->|پرس‌وجو تکی| F
    E -->|بارگذاری context| F
    F -->|پاسخ| G["خروجی"]
    G -->|text/json/stream-json| H["ترمینال / پمپ"]
```

## دستورات CLI

| دستور | توضیح | مثال |
|---------|-------------|---------|
| `claude` | راه‌اندازی REPL تعاملی | `claude` |
| `claude \"query\"` | launch REPL با پرامپت اولیه | `claude \"توضیح این پروژه\"` |
| `claude -p \"query\"` | حالت چاپ، پرس‌وجو و خروج | `claude -p \"توضیح این تابع\"` |
| `cat file \| claude -p \"query\"` | پردازش ادرس ورودی از طریق کانال | `cat logs.txt \| claude -p \"توضیح این لاگ‌ها\"` |
| `claude -c` | ادامه به سیشن اخیر | `claude -c` |
| `claude -c -p \"query\"` | ادامه یافتن در حالت چاپ | `claude -c -p \"بررسی خطاهای تایپ\"` |
| `claude -r \"<session>\" \"query\"` | بازیابی سیشن با ID یا نام | `claude -r \"auth-refactor\" \"پایان این PR\"` |

---

## پرچم‌های اصلی

| پرچم | توضیح | مثال |
|------|-------------|---------|
| `-p、--print` | بدون ورود به حالت تعاملی، خروجی را مستقیماً چاپ کنید | `claude -p \"query\"` |
| `-c、--continue` | بارگذاری به سیشن اخیر | `claude --continue` |
| `-r、--resume` | بازیابی سیشن مشخص شده با ID یا نام | `claude --resume auth-refactor` |
| `-v、--version` | چاپ شماره نسخه | `claude -v` |
| `-w、--worktree` | شروع در کارخونه مجزایتلاف بومی | `claude -w` |
| `-n、--name` | تنظیم نام نمایش سیشن | `claude -n \"auth-refactor\"` |
| `--from-pr <number>` | بازیابی سیشن مرتبط با GitHub PR | `claude --from-pr 42` |
| `--cloud [description\|session_id\|url]` | با وصف داده‌شده در claude.ai یک سیشن ابری ایجاد کرده یا از طریق session ID/claude.ai/code URL به یک سیشن موجود متصل شوید | `claude --cloud \"implement API\"` |
| `--remote \"task\"` | **استعارت منسوخ‌شده‌ی `--cloud`** (از جمله دسترسی به سیشن‌های موجود). به جای آن `--cloud` را استفاده کنید | `claude --remote \"implement API\"` |
| `--remote-control、--rc` | ورود به سیشن تعاملی از کنترل از راه دور | `claude --rc` |
| `--teleport` | بازیابی سیشن وب به محلی | `claude --teleport` |
| `--teammate-mode` | حالت نمایش کار تیمی | `claude --teammate-mode tmux` |
| `--bare` | حالت صرف‌کردنی، همه‌پرسی‌های شکننده را رد می‌کند (hookها، مهارت‌ها، پلاquinها، MCP، حافظه خودکار و `CLAUDE.md`) | `claude --bare` |
| `--enable-auto-mode` | قابلیت حالت مجوز خودکار را فعال می‌کند | `claude --enable-auto-mode` |
| `--channels` | اشتراک‌گذاری پلاquin کانتینر MCP. هر مورد باید به صورت `plugin:<name>@<marketplace>` ذکر شود؛ فقط نوشتن نام رد می‌شود | `claude --channels plugin:discord@my-marketplace` |
| `--chrome / --no-chrome` | فعال/غیرفعال کردن یکپارچگی مرورگر Chrome | `claude --chrome` |
| `--effort` | تنظیم شدت استدلال | `claude --effort high` |
| `--init / --init-only` | `--init` قبل از شروع سیشن، اجرا می‌کند Setup hooks، فقط در حالت چاپ؛ `--init-only` اجرای Setup و SessionStart hooks | `claude --init-only` |
"""
with open(os.path.join(fa_dir, "10-cli", "README.md"), "w", encoding="utf-8") as f:
    f.write(content)

print("10-cli/README.md part 1 written!")