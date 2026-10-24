import os

fa_dir = r"D:\Project\claude-howto\fa"

content = """<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../../resources/logos/claude-howto-logo-dark.svg">
  <img alt="Claude How To" src="../../resources/logos/claude-howto-logo.svg">
</picture>

# MCP (بروتوكول زمینه مدل)

## مروری کلی

MCP استانداردی است که Claude Code برای دسترسی به ابزارها، سرویس‌ها و APIهای خارجی از طریق آن استفاده می‌کند. می‌توانید GitHub، پایگاه داده، سیستم فایل، سیستم‌های چت و غیره را به Claude وصل کنید.

## معماری MCP

MCP معمولاً از سه بخش تشکیل می‌شود:

1. Claude Code
2. سرور MCP
3. ابزار یا منبع داده خارجی

Claude از طریق پروتکل MCP به سرور فراخوانی ابزار می‌کند و نتیجه را به peril.session فعلی برمی‌گرداند.

## اکوسیستم MCP

- یکپارچه‌سازی GitHub
- یکپارچه‌سازی پایگاه داده
- یکپارچه‌سازی سیستم فایل
- ابزارهای داخلی سازمان
- سروسه‌های شخص ثالث
"""

with open(os.path.join(fa_dir, "05-mcp", "README.md"), "w", encoding="utf-8") as f:
    f.write(content)

print("05-mcp/README.md part 1 written!")