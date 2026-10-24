import os

fa_dir = r"D:\Project\claude-howto\fa"

content = """
| **۷** | [MCP](05-mcp/README.md) | ⭐⭐⭐ پیشرفته | ۱ ساعت | Level ۲ | ابزارها، دستورات | دسترسی به داده‌های خارجی | جستجو در زمان واقعی |
| **۸** | [Subagentها](04-subagents/README.md) | ⭐⭐⭐ پیشرفته | ۱ ساعت | Level ۲ | MCP، ابزارها | کارهای تخصصی با ایزولاسیون contexte | تفویض کار، ایزولاسیون |
| **۹** | [مهارت‌ها](03-skills/README.md) | ⭐⭐⭐ پیشرفته | ۱ ساعت | Level ۲ | دستورات Slash، hookها | اتوماسیون گردش کار (۳۳ رویداد، ۵ نوع) | اعتبارسنجی، درگاه کیفیت |
| **۱۰** | [پلاquinها](07-plugins/README.md) | ⭐⭐⭐⭐ متخصص | ۱ ساعت | Level ۳ | همه قابلیت‌ها | یکپارچگی کامل | بسته‌بندی یکپارچه |

"""

with open(os.path.join(fa_dir, "LEARNING-ROADMAP.md"), "a", encoding="utf-8") as f:
    f.write(content)

print("LEARNING-ROADMAP.md part 2a written!")