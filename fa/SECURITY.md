<picture>
  <source media="(prefers-color-scheme: dark)" srcset="resources/logos/claude-howto-logo-dark.svg">
  <img alt="Claude How To" src="resources/logos/claude-howto-logo.svg">
</picture>

# سیاست امنیتی

## مرور کلی

امنیت پروژه Claude How To برای ما مهم است. این مستند practiceهای امنیتی ما را توضیح می‌دهد و نحوه گزارش responsible vulnerabilityها را بیان می‌کند.

## نسخه‌های پشتیبانی‌شده

| Version | Status | Support Until |
|---------|--------|---------------|
| Latest (main) | ✅ Active | Current + 6 months |

**نکته**: به‌عنوان یک پروژه راهنمای educational، روی حفظ best practiceهای فعلی و امنیت مستندات تمرکز داریم. updateها مستقیماً به branch main اعمال می‌شوند.

## Practiceهای امنیتی

### امنیت کد

1. **Dependency Management** - dependencies pin شده، updateهای منظم، Bandit scan روی هر commit
2. **کیفیت کد** - Ruff linting، mypy type checking، review قبل از merge
3. **کنترل دسترسی** - branch protection، required reviews، دسترسی write محدود

### امنیت مستندات

1. **بدون secret در مثال‌ها** - placeholderها، credentialهای hardcodeنشده، `.env.example`
2. **Best practiceهای امنیتی** - patternهای امن، هشدارها، لینک به راهنماهای رسمی
3. **Content review** - review برای issueهای امنیتی

## گزارش Vulnerability

### Security issueهایی که برای ما مهم هستند

vulnerabilityهای کد، dependencyها، cryptography، authentication/authorization، data exposure، injection، SSRF/XXE/Path traversal.

### Security issueهای خارج از scope

vulnerabilityهای Claude Code itself (به Anthropic گزارش)، external serviceها، social engineering، vulnerabilityهای نظری، dependencyها از channelهای رسمی.

### نحوه گزارش

**Private Reporting (ترجیحی)**: GitHub → Security → Report a vulnerability

**Public Reporting (non-sensitive)**: GitHub Issue با label `security` و عنوان `[SECURITY]`

## منابع امنیتی

- [OWASP Top 10](https://owasp.org/www-project-top-ten/)
- [CWE Top 25](https://cwe.mitre.org/top25/)
- [Bandit Documentation](https://bandit.readthedocs.io/)
- [Anthropic Security](https://www.anthropic.com/)

## تشکر

از security researcherها و community memberهایی که به امن نگه داشتن این پروژه کمک می‌کنند قدردانی می‌کنیم.

---

**Last Updated**: August 25, 2026
**Claude Code Version**: 2.1.245
**Next Review**: April 2027
