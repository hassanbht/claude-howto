import os

fa_dir = r"D:\Project\claude-howto\fa"

content = """

## منابع امنیتی

### استانداردهای رسمی

- [OWASP Top 10](https://owasp.org/www-project-top-ten/)
- [CWE Top 25](https://cwe.mitre.org/top25/)
- [CVSS Calculator](https://www.first.org/cvss/calculator/3.1)

### امنیت Python

- [Python Security Advisories](https://www.python.org/dev/security/)
- [PyPI Security](https://pypi.org/help/#security)
- [Bandit Documentation](https://bandit.readthedocs.io/)

### مدیریت وابستگی

- [OWASP Dependency Check](https://owasp.org/www-project-dependency-check/)
- [GitHub Security Alerts](https://docs.github.com/en/code-security/dependabot/dependabot-alerts/about-dependabot-alerts)

### امنیت عمومی

- [Anthropic Security](https://www.anthropic.com/)
- [GitHub Security Best Practices](https://docs.github.com/en/code-security)

## آرشیو اعلامیه‌های امنیتی

اطلاعیه‌های امنیتی گذشته را در برگه [Security Advisories](https://github.com/luongnv89/claude-howto/security/advisories) GitHub می‌توانید مشاهده کنید.

## تماس با ما

برای سوال در مورد مسائل امنیتی یا بحث در مورد شیوه‌های امنیتی:

1. **گزارش امنیتی شخصی**: از گزارش شخصی GitHub استفاده کنید
2. **سوالات عمومی امنیتی**: با برچسب `[SECURITY]` یک discussion ایجاد کنید
3. **بازخورد politicy امنیتی**: یک issue با برچسب `security` ایجاد کنید

## اشعار

از محققان امنیتی و اعضای جامعه که کمک می‌کنند پروژه را امن نگه دارند، تشکر می‌کنیم. مشارکت‌کنندگان که آسیب‌پذیری‌ها را به صورت مسئولانه گزارش می‌کنند در اعلامیه‌های امنیتی ما به شما اشعار می‌دهیم (مگر شما داشته باشید anonym بنویسید).

## به‌روزرسانی سیاست

این سیاست امنیتی در موارد زیر به‌روزرسانی می‌شود:

- هنگام شناسایی آسیب‌پذیری جدید
- هنگام تکالیف شدن بهترین شیوه‌های امنیتی
- وقتی دامنه پروژه تغییر می‌کند
- حداقل یک بار در سال

**آخرین به‌روزرسانی**: ۲۵ آذر ۲۰۲۶
**نسخه Claude Code**: ۲.۱.۲۴۵
**منبع**:
- https://code.claude.com/docs/en/overview
**بازبینی بعدی**: ژانویه ۲۰۲۷

---

از شما برای کمک به Claude How To برای حفظ امنیت تشکر می‌کنیم! 🔒
"""

with open(os.path.join(fa_dir, "SECURITY.md"), "a", encoding="utf-8") as f:
    f.write(content)

print("SECURITY.md part 7 written!")