<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../../resources/logos/claude-howto-logo-dark.svg">
  <img alt="Claude How To" src="../../resources/logos/claude-howto-logo.svg">
</picture>

# MCP (پروتکل مدلِ بافتار)

این پوشه شامل مستندات و نمونه‌های جامع برای پیکربندی و استفاده از سرورهای MCP در Claude Code است.

## نمای کلی

MCP (Model Context Protocol) روشی استاندارد برای دسترسی Claude به ابزارهای خارجی، APIها و منابع دادهٔ زنده است. برخلاف حافظه، MCP دسترسی زنده به داده‌های در حال تغییر را فراهم می‌کند.

ویژگی‌های کلیدی:
- دسترسی بلادرنگ به سرویس‌های خارجی
- همگام‌سازی زندهٔ داده‌ها
- معماری قابل‌گسترش
- احراز هویت امن
- تعاملات مبتنی بر ابزار

## معماری MCP

```mermaid
graph TB
    A["Claude"]
    B["MCP Server"]
    C["External Service"]

    A -->|Request: list_issues| B
    B -->|Query| C
    C -->|Data| B
    B -->|Response| A

    A -->|Request: create_issue| B
    B -->|Action| C
    C -->|Result| B
    B -->|Response| A

    style A fill:#e1f5fe,stroke:#333,color:#333
    style B fill:#f3e5f5,stroke:#333,color:#333
    style C fill:#e8f5e9,stroke:#333,color:#333
```

## اکوسیستم MCP

```mermaid
graph TB
    A["Claude"] -->|MCP| B["Filesystem<br/>MCP Server"]
    A -->|MCP| C["GitHub<br/>MCP Server"]
    A -->|MCP| D["Database<br/>MCP Server"]
    A -->|MCP| E["Slack<br/>MCP Server"]
    A -->|MCP| F["Google Docs<br/>MCP Server"]

    B -->|File I/O| G["Local Files"]
    C -->|API| H["GitHub Repos"]
    D -->|Query| I["PostgreSQL/MySQL"]
    E -->|Messages| J["Slack Workspace"]
    F -->|Docs| K["Google Drive"]

    style A fill:#e1f5fe,stroke:#333,color:#333
    style B fill:#f3e5f5,stroke:#333,color:#333
    style C fill:#f3e5f5,stroke:#333,color:#333
    style D fill:#f3e5f5,stroke:#333,color:#333
    style E fill:#f3e5f5,stroke:#333,color:#333
    style F fill:#f3e5f5,stroke:#333,color:#333
    style G fill:#e8f5e9,stroke:#333,color:#333
    style H fill:#e8f5e9,stroke:#333,color:#333
    style I fill:#e8f5e9,stroke:#333,color:#333
    style J fill:#e8f5e9,stroke:#333,color:#333
    style K fill:#e8f5e9,stroke:#333,color:#333
```

## روش‌های نصب MCP

Claude Code از چندین پروتکل انتقال برای اتصال به سرورهای MCP پشتیبانی می‌کند:

### انتقال HTTP (توصیه‌شده)

```bash
# Basic HTTP connection
claude mcp add --transport http notion https://mcp.notion.com/mcp

# HTTP with authentication header
claude mcp add --transport http secure-api https://api.example.com/mcp \
  --header "Authorization: Bearer your-token"
```

### انتقال stdio (محلی)

برای سرورهای MCP که به‌صورت محلی اجرا می‌شوند:

```bash
# Local Node.js server
claude mcp add --transport stdio myserver -- npx @myorg/mcp-server

# With environment variables
claude mcp add --transport stdio myserver --env KEY=value -- npx server
```

#### `CLAUDE_PROJECT_DIR` برای سرورهای stdio (v2.1.139+)

هر سرور MCP از نوع stdio با `CLAUDE_PROJECT_DIR=<absolute path to repo root>` از پیش تنظیم‌شده در محیط خود راه‌اندازی می‌شود — همان قراردادی که برای هوک‌ها استفاده می‌شود. فایل‌های پلاگین و `.mcp.json` پروژه می‌توانند `${CLAUDE_PROJECT_DIR}` را در مقادیر `command`، `args` و `env` ارجاع دهند و جایگزینی پیش از `execve()` انجام می‌شود:

```json
{
  "mcpServers": {
    "repo-tools": {
      "type": "stdio",
      "command": "node",
      "args": ["${CLAUDE_PROJECT_DIR:-.}/.claude/mcp/repo-tools.js"],
      "env": {
        "REPO_ROOT": "${CLAUDE_PROJECT_DIR:-.}"
      }
    }
  }
}
```

> **نکته**: در پیکربندی پروژه، محلی و کاربر، همیشه `${CLAUDE_PROJECT_DIR:-.}` را با مقدار پیش‌فرض بنویسید: این متغیر در محیط سرور تنظیم می‌شود، نه در محیط خود Claude Code. فقط پیکربندی‌های MCP پلاگین `${CLAUDE_PROJECT_DIR}` را مستقیماً جایگزین می‌کنند.

وقتی سرور stdio شما نیاز دارد فایل‌هایی را نسبت به ریشهٔ پروژه بخواند، بدون توجه به اینکه Claude Code از کجا راه‌اندازی شده، از این استفاده کنید.

سرورهای MCP از نوع stdio همچنین `CLAUDE_CODE_SESSION_ID` را دریافت می‌کنند (مطابق مقدار ارسال‌شده به هوک‌ها و Bash)، از جمله وقتی نشست با `--resume` بازیابی می‌شود (v2.1.163+).

### انتقال SSE (منسوخ‌شده)

انتقال Server-Sent Events به نفع `http` منسوخ شده اما همچنان پشتیبانی می‌شود:

```bash
claude mcp add --transport sse legacy-server https://example.com/sse
```

### انتقال WebSocket (`ws`)

سرورهای WebSocket یک اتصال پایدار دوطرفه نگه می‌دارند که برای سرورهای MCP راه‌دور که رویدادها را بدون درخواست به Claude ارسال می‌کنند مناسب است. وقتی سرور شما فقط به درخواست‌ها پاسخ می‌دهد از HTTP استفاده کنید، زیرا HTTP از OAuth و پرچم `claude mcp add --transport` پشتیبانی می‌کند در حالی که WebSocket از هیچ‌یک پشتیبانی نمی‌کند.

از آنجا که `--transport` مقدار `ws` را نمی‌پذیرد، آن را در `.mcp.json` یا از طریق `claude mcp add-json` پیکربندی کنید:

```json
{
  "type": "ws",
  "url": "wss://mcp.example.com/socket",
  "headers": {
    "Authorization": "Bearer YOUR_TOKEN"
  }
}
```

مدخل `type: "ws"` همان فیلدهای `url`، `headers`، `headersHelper`، `timeout` و `alwaysLoad` را می‌پذیرد که `http`. احراز هویت **فقط از طریق هدر** است — جریان OAuth برای سرورهای WebSocket وجود ندارد.

> **نکته**: از v2.1.285، `claude mcp list` سرورهای WebSocket (`ws`) را با URL و وضعیت سلامت فهرست می‌کند (نسخه‌های قبلی آن‌ها را نشان نمی‌دادند). می‌توانید آن‌ها را با `claude mcp get <name>` یا پنل `/mcp` هم بررسی کنید.

مانند HTTP و SSE، اتصالات WebSocket از پنجرهٔ بیکاری ۵ دقیقه‌ای استفاده می‌کنند؛ stdio و WebSocket تایمر درخواستی ندارند. یک مدخل `url` بدون `type` یک خطا است که `"http"`، `"sse"` و `"ws"` را به‌عنوان مقادیر معتبر نام می‌برد.

### شاخه‌های کاری نشست (roots/list)

سرورهای MCP می‌توانند شاخه‌های کاری نشست را کشف کنند: شاخهٔ راه‌اندازی به‌علاوهٔ همهٔ مدخل‌های `--add-dir`/`additionalDirectories` از طریق درخواست MCP `roots/list` برگردانده می‌شوند و هر بار که مجموعه تغییر می‌کند یک اعلان `notifications/roots/list_changed` ارسال می‌شود (v2.1.203). تایم‌اوت بیکاری اکنون برای سرورهای stdio نیز اعمال می‌شود (۳۰ دقیقه)، با یک `timeout` برای هر سرور به‌عنوان کف بیکاری (v2.1.203).

### نکتهٔ مخصوص ویندوز

در ویندوز بومی (نه WSL)، از `cmd /c` برای دستورات npx استفاده کنید:

```bash
claude mcp add --transport stdio my-server -- cmd /c npx -y @some/package
```

### احراز هویت OAuth 2.0

Claude Code از OAuth 2.0 برای سرورهای MCP که به آن نیاز دارند پشتیبانی می‌کند. هنگام اتصال به یک سرور با OAuth، Claude Code کل جریان احراز هویت را مدیریت می‌کند:

```bash
# Connect to an OAuth-enabled MCP server (interactive flow)
claude mcp add --transport http my-service https://my-service.example.com/mcp

# Pre-configure OAuth credentials for non-interactive setup
claude mcp add --transport http my-service https://my-service.example.com/mcp \
  --client-id "your-client-id" \
  --client-secret "your-client-secret" \
  --callback-port 8080
```

| ویژگی | توضیحات |
|---------|-------------|
| **OAuth تعاملی** | از `/mcp` برای راه‌اندازی جریان OAuth مبتنی بر مرورگر استفاده کنید |
| | کلاینت‌های OAuth از پیش پیکربندی‌شده برای سرویس‌های رایج مانند Notion، Stripe و سایرین (v2.1.30+) |
| **احراز هویت از پیش پیکربندی‌شده** | پرچم‌های `--client-id`، `--client-secret`، `--callback-port` برای راه‌اندازی خودکار |
| **ذخیرهٔ توکن** | توکن‌ها به‌صورت امن در keychain سیستم شما ذخیره می‌شوند |
| **احراز هویت پلکانی** | از احراز هویت پلکانی (step-up) برای عملیات ممتاز پشتیبانی می‌کند |
| **کَش کشف** | فرادادهٔ کشف OAuth برای اتصال مجدد سریع‌تر کَش می‌شود |
| **بازنویسی فراداده** | `oauth.authServerMetadataUrl` در `.mcp.json` برای بازنویسی کشف پیش‌فرض فرادادهٔ OAuth |

#### بازنویسی کشف فرادادهٔ OAuth

اگر سرور MCP شما روی نقطهٔ پایانی استاندارد کشف OAuth (`/.well-known/oauth-authorization-server`) خطا برمی‌گرداند اما یک نقطهٔ پایانی OIDC کارآمد دارد، می‌توانید به Claude Code بگویید فرادادهٔ OAuth را از URL خاصی واکشی کند. `authServerMetadataUrl` را در شیء `oauth` پیکربندی سرور خود تنظیم کنید:

```json
{
  "mcpServers": {
    "my-server": {
      "type": "http",
      "url": "https://mcp.example.com/mcp",
      "oauth": {
        "authServerMetadataUrl": "https://auth.example.com/.well-known/openid-configuration"
      }
    }
  }
}
```

URL باید `https://` باشد. این گزینه به Claude Code v2.1.64 یا بالاتر نیاز دارد.

#### اعلان راه‌اندازی احراز هویت و بازخوانی هدر پویا (v2.1.193)

- **اعلان احراز هویت در راه‌اندازی (v2.1.193+)**: در راه‌اندازی، Claude Code اعلانی نمایش می‌دهد که سرورهای MCP نیازمند احراز هویت را فهرست می‌کند، تا سروری که نیاز به ورود دارد بی‌صدا از کار نیفتد.
- **بازخوانی خودکار `headersHelper` (v2.1.193+)**: اگر احراز هویت سفارشی از طریق `headersHelper` ارائه می‌کنید، هِلپر به‌صورت خودکار وقتی سرور HTTP 401 یا 403 برمی‌گرداند دوباره فراخوانی می‌شود. اعتبارنامه‌ها در لحظه بازخوانی می‌شوند بدون نیاز به اتصال مجدد دستی. بخش [Use dynamic headers for custom authentication](https://code.claude.com/docs/en/mcp) را ببینید.

> **هشدار** (v2.1.238): یک `headersHelper` در `.mcp.json` پروژه، و سرورهای MCP درون‌خطی در فایل‌های ایجنت پروژه یا `--add-dir`، اکنون نیازمند پذیرش گفت‌وگوی اعتماد آن پوشه هستند — از جمله تحت `claude -p`. چنین هِلپرهایی همچنین **بدون متغیرهای محیطی اعتبارنامهٔ ارثی** اجرا می‌شوند؛ هِلپرهای محدودهٔ کاربر، مدیریت‌شده و claude.ai از شاخهٔ پیکربندی Claude اجرا می‌شوند. یک پیکربندی پروژه که به اعتبارنامه‌های ارثی یا اجرای نامعتتمد وابسته بود تا پذیرش گفت‌وگوی اعتماد و تأمین اعتبارنامه از روش دیگری کار نخواهد کرد.

### اتصال‌دهنده‌های MCP Claude.ai

سرورهای MCP پیکربندی‌شده در حساب Claude.ai شما به‌طور خودکار در Claude Code در دسترسند. این یعنی هر اتصال MCP که از طریق رابط وب Claude.ai راه‌اندازی کنید بدون پیکربندی اضافی قابل دسترسی خواهد بود.

اتصال‌دهنده‌های MCP Claude.ai در حالت `--print` (v2.1.83+) نیز در دسترسند که استفادهٔ غیرتعاملی و اسکریپتی را ممکن می‌سازد.

> **نکتهٔ راه‌اندازی (v2.1.117+):** اتصال همزمان پیش‌فرض است وقتی هم سرورهای MCP محلی و هم claude.ai پیکربندی شده‌اند (قبلاً متوالی بود)، که تأخیر راه‌اندازی را هنگام استفاده از چندین سرور کاهش می‌دهد.

برای غیرفعال کردن سرورهای MCP Claude.ai در Claude Code، متغیر محیطی `ENABLE_CLAUDEAI_MCP_SERVERS` را روی `false` تنظیم کنید:

```bash
ENABLE_CLAUDEAI_MCP_SERVERS=false claude
```

> **نکته:** این ویژگی فقط برای کاربرانی که با حساب‌های Claude.ai وارد شده‌اند در دسترس است.

## فرآیند راه‌اندازی MCP

```mermaid
sequenceDiagram
    participant User
    participant Claude as Claude Code
    participant Config as Config File
    participant Service as External Service

    User->>Claude: Type /mcp
    Claude->>Claude: List available MCP servers
    Claude->>User: Show options
    User->>Claude: Select GitHub MCP
    Claude->>Config: Update configuration
    Config->>Claude: Activate connection
    Claude->>Service: Test connection
    Service-->>Claude: Authentication successful
    Claude->>User: ✅ MCP connected!
```

### دستور `/mcp`

برای فهرست سرورهای متصل، راه‌اندازی جریان‌های OAuth و بررسی وضعیت اتصال، `/mcp` را در نشست تایپ کنید.

- از **v2.1.121**، MCP اتصال اولیه را تا ۳ بار در خطاهای گذرا تلاش می‌کند.
- از **v2.1.128**، `/mcp` **تعداد ابزار** هر سرور متصل را نمایش می‌دهد و سرورهایی که **۰ ابزار** گزارش می‌کنند را بصری علامت می‌زند تا سرورهای نادرست در یک نگاه متمایز شوند.

## جستجوی ابزار MCP

جستجوی ابزار به‌صورت پیش‌فرض فعال است: ابزارهای MCP به تعویق افتاده و در صورت درخواست کشف می‌شوند، تا تعریف‌های آن‌ها بافتار مدل را پر نکنند. Claude Code آن را وقتی `ANTHROPIC_BASE_URL` به میزبان غیر اول‌طرفه اشاره می‌کند خاموش می‌کند، زیرا اکثر پراکسی‌ها بلوک‌های مورد نیاز آن را بازنشر نمی‌کنند.

| تنظیم | مقدار | توضیحات |
|---------|-------|-------------|
| `ENABLE_TOOL_SEARCH` | (تنظیم‌نشده — پیش‌فرض) | همهٔ ابزارهای MCP به تعویق افتاده و در صورت درخواست بارگذاری می‌شوند |
| `ENABLE_TOOL_SEARCH` | `auto` | حالت آستانه: ابزارها تا زمانی که تعریف‌هایشان به ۱۰٪ پنجرهٔ بافتار برسد بارگذاری می‌شوند، سپس همه به تعویق می‌افتند |
| `ENABLE_TOOL_SEARCH` | `auto:<N>` | حالت آستانه با درصد سفارشی (۰-۱۰۰) — مثلاً `auto:5` برای ۵٪ |
| `ENABLE_TOOL_SEARCH` | `true` | همهٔ ابزارهای MCP به تعویق افتاده |
| `ENABLE_TOOL_SEARCH` | `false` | غیرفعال؛ همهٔ توضیحات ابزار کامل ارسال می‌شوند |

> **نکته:** جستجوی ابزار نیازمند مدلی است که از بلوک‌های `tool_reference` پشتیبانی می‌کند: Claude Opus 4، Claude Sonnet 4، Claude Haiku 4.5 و مدل‌های بعدتر (Opus 4.5، Sonnet 4.5، Haiku 4.5 و بعدتر روی Agent Platform ابر گوگل).

### دور زدن جستجوی ابزار برای هر سرور (v2.1.121+)

اگر ابزارهای یک سرور MCP خاص در هر نوبت نیاز است، پیکربندی آن را با `"alwaysLoad": true` علامت بزنید تا از تعویق جستجوی ابزار صرف‌نظر شود و ابزارهایش همیشه در دسترس باشند:

```json
{
  "mcpServers": {
    "always-on-tool": {
      "command": "node",
      "args": ["./tools/always.js"],
      "alwaysLoad": true
    }
  }
}
```

ّبیش به‌کار نبرید — هر ابزار همیشه‌بارگذاری‌شده بافتاری را مصرف می‌کند که می‌توانست برای جستجوی ابزار به‌کار رود تا ابزار مرتبط‌تری را معرفی کند.

برای نگه‌داشتن همهٔ ابزارهای یک سرور پشت جستجوی ابزار، `"alwaysLoad": false` را در مدخل آن سرور تنظیم کنید (v2.1.287+). این شامل ابزارهایی است که نویسندهٔ سرور برای بارگذاری پیش‌رو علامت‌گذاری کرده؛ اگر `alwaysLoad` را نگذارید، آن ابزارهای علامت‌خورده پیش‌رو بارگذاری می‌شوند. نویسندگان سرور یک ابزار منفرد را با تنظیم `"anthropic/alwaysLoad"` در شیء `_meta` آن ابزار علامت می‌زنند و تنظیم `alwaysLoad` در سطح سرور در پیکربندی شما می‌تواند آن را بازنویسی کند.

## به‌روزرسانی پویای ابزار

Claude Code از اعلان‌های `list_changed` پشتیبانی می‌کند. وقتی یک سرور MCP ابزارهای در دسترس خود را پویا اضافه، حذف یا تغییر می‌دهد، Claude Code به‌روزرسانی را دریافت کرده و فهرست ابزار خود را به‌طور خودکار تنظیم می‌کند — نیازی به اتصال مجدد یا راه‌اندازی دوباره نیست.

## اپ‌های MCP

اپ‌های MCP نخستین توسعهٔ رسمی MCP است که فراخوانی ابزار MCP می‌تواند اجزای رابط کاربری تعاملی برگرداند که مستقیماً در رابط چت نمایش داده می‌شوند. به‌جای پاسخ متنی ساده، سرورهای MCP می‌توانند داشبورد غنی، فرم، بصری‌سازی داده و جریان‌کار چندمرحله‌ای تحویل دهند — همگی درون‌خطی بدون ترک گفت‌وگو نمایش داده می‌شوند.

## درخواست ورودی از کاربر (Elicitation) در MCP

سرورهای MCP می‌توانند از طریق دیالوگ‌های تعاملی از کاربر ورودی ساخت‌یافته درخواست کنند (v2.1.49+). این به سرور MCP اجازه می‌دهد در میانهٔ جریان‌کار برای اطلاعات اضافی درخواست کند — مثلاً درخواست تأیید، انتخاب از فهرست گزینه‌ها یا پر کردن فیلدهای ضروری — و تعامل را به تعاملات سرور MCP می‌افزاید.

## کَش توضیحات ابزار و دستورالعمل

Claude Code توضیحات هر ابزار MCP و دستورالعمل‌های هر سرور را کوتاه می‌کند تا سرورهای پرحرف بافتار را متورم نکنند. محدودیت‌های پیش‌فرض **۴٬۰۹۶ نویسه** برای دستورالعمل‌های سرور و توضیحات ابزارهایی که پیش‌رو بارگذاری می‌شوند (v2.1.296؛ ۲٬۰۴۸ از v2.1.84 تا آن زمان) و **۱۶٬۳۸۴ نویسه** برای توضیحاتی است که Claude از طریق جستجوی ابزار بارگذاری می‌کند (v2.1.295). از v2.1.280، `CLAUDE_CODE_MAX_MCP_DESCRIPTION_LENGTH` آن‌ها را بازنویسی می‌کند: شماره‌ای که تنظیم می‌کنید **هر دو** محدودیت را جایگزین می‌کند (`8192` محدودیت کوتاه‌تر را بالا و بلندتر را پایین می‌برد). از v2.1.299، توضیحات و دستورالعمل‌های سرورهای MCP اول‌طرفهٔ Anthropic در `api.anthropic.com` به‌طور کامل به Claude می‌رسند. جزئیات حیاتی را نزدیک آغاز توضیحات قرار دهید.

## پرامپت‌های MCP به‌عنوان دستورات اسلش

سرورهای MCP می‌توانند پرامپت‌هایی را عرضه کنند که به‌عنوان دستورات اسلش در Claude Code ظاهر می‌شوند. پرامپت‌ها با قرارداد نام‌گذاری زیر در دسترسند:

```
/mcp__<server>__<prompt>
```

مثلاً اگر سروری به نام `github` پرامپتی به نام `review` عرضه کند، می‌توانید آن را به‌صورت `/mcp__github__review` فراخوانی کنید.

## حذف تکراری سرور

وقتی همان سرور MCP در چندین محدوده (محلی، پروژه، کاربر) تعریف شود، پیکربندی محلی اولویت دارد. این به شما اجازه می‌دهد تنظیمات MCP در سطح پروژه یا کاربر را با سفارشی‌سازی‌های محلی بازنویسی کنید بدون ایجاد تعارض.

## رفع‌های اخیر چرخهٔ حیات (v2.1.136)

دو باگ قدیمی چرخهٔ حیات MCP در v2.1.136 رفع شد — ارتقا ارزشمند است اگر چندسروری می‌چرخانید:

- **سرورهای MCP در سراسر `/clear` پایدارند**: سرورهایی که از طریق `.mcp.json`، پلاگین‌ها یا اتصال‌دهنده‌های claude.ai پیکربندی شده‌اند دیگر بعد از `/clear` در VS Code، JetBrains یا Agent SDK ناپدید نمی‌شوند. نسخه‌های قبلی آن‌ها را بی‌صدا رها و نیازمند راه‌اندازی دوباره بودند.
- **رفحالتال توکن بازخوانی همزمان OAuth**: تنظیمات چندسروری OAuth دیگر توکن‌های بازخوانی را وقتی چند سرور رقابتی همزمان بازخوانی می‌کنند از دست نمی‌دهند. این الگوی «هر صبح باید دوباره احراز هویت کنم» را که تنظیمات با چند سرور OAuth-محافظت‌شده را آلوده می‌کرد از بین می‌برد.

## منابع MCP از طریق @ منشن

می‌توانید منابع MCP را مستقیماً در پرامپت‌های خود با نحو منشن `@` ارجاع دهید:

```
@server-name:protocol://resource/path
```

مثلاً برای ارجاع به یک منبع خاص دیتابیس:

```
@database:postgres://mydb/users
```

این به Claude اجازه می‌دهد محتوای منبع MCP را درون‌خطی به‌عنوان بخشی از بافتار گفت‌وگو واکشی و در بر گیرد.

## محدوده‌های MCP

پیکربندی‌های MCP می‌توانند در محدوده‌های مختلفی با سطوح اشتراک متغیر ذخیره شوند:

| محدوده | پرچم | مکان | توضیحات | مشترک با | نیازمند تأیید |
|-------|------|----------|-------------|-------------|------------------|
| **محلی** (پیش‌فرض) | `--scope local` | `~/.claude.json` (زیر مسیر پروژه) | خصوصی برای کاربر فعلی، فقط پروژه فعلی (در نسخه‌های قدیمی `project` نامیده می‌شد) | فقط شما | خیر |
| **پروژه** | `--scope project` | `.mcp.json` | در مخزن گیت commit می‌شود | اعضای تیم | بله (اولین استفاده) |
| **کاربر** | `--scope user` | `~/.claude.json` | در سراسر همهٔ پروژه‌ها در دسترس (در نسخه‌های قدیمی `global` نامیده می‌شد) | فقط شما | خیر |

هنگام افزودن سرور با `--scope` (شکل کوتاه `-s`) محدوده‌ای را انتخاب کنید. اگر آن را نگذارید،
Claude Code از `local` استفاده می‌کند:

```bash
# Project scope — writes to .mcp.json so the team shares it
claude mcp add --scope project --transport http github https://api.githubcopilot.com/mcp/ --header "Authorization: Bearer YOUR_GITHUB_PAT"

# User scope — available in every project
claude mcp add --scope user --transport stdio memory -- npx @modelcontextprotocol/server-memory
```

### استفاده از محدودهٔ پروژه

پیکربندی‌های MCP خاص پروژه را در `.mcp.json` ذخیره کنید:

```json
{
  "mcpServers": {
    "github": {
      "type": "http",
      "url": "https://api.githubcopilot.com/mcp/",
      "headers": {
        "Authorization": "Bearer ${GITHUB_PERSONAL_ACCESS_TOKEN}"
      }
    }
  }
}
```

اعضای تیم در اولین استفاده از MCP پروژه یک اعلان تأیید خواهند دید. در یک فضای کاری نامعتتمد، سرورهایی که یک مخزن از طریق `.claude/settings.json` commit‌شده خودتأیید کرده است توسط `claude mcp list`/`get` به‌طور خودکار راه‌اندازی نمی‌شوند — تا گفت‌وگوی اعتماد را نپذیرید `⏸ Pending approval` نشان می‌دهند و `enableAllProjectMcpServers` در یک پوشهٔ نامعتتمد نادیده گرفته می‌شود (v2.1.196).

## مدیریت پیکربندی MCP

### افزودن سرورهای MCP

```bash
# Add HTTP-based server
claude mcp add --transport http github https://api.githubcopilot.com/mcp/ --header "Authorization: Bearer YOUR_GITHUB_PAT"

# Add local stdio server
claude mcp add --transport stdio database -- npx @company/db-server

# List all MCP servers
claude mcp list

# Get details on specific server
claude mcp get github

# Remove an MCP server
claude mcp remove github

# Reset project-specific approval choices
claude mcp reset-project-choices

# Authenticate an MCP server from the CLI (v2.1.186+)
claude mcp login github

# Sign out of an MCP server (v2.1.186+)
claude mcp logout github

# Import from Claude Desktop
claude mcp add-from-claude-desktop

# Add a server from a JSON blob (useful for scripted setup)
claude mcp add-json events-server '{"type":"stdio","command":"npx","args":["@modelcontextprotocol/server-events"]}'
```

> **نکته**: در پیکربندی‌های JSON — `.mcp.json`، `~/.claude.json` یا `claude mcp add-json` — فیلد `type` مقدار `streamable-http` را به‌عنوان نام مستعار برای `http` می‌پذیرد. مشخصات MCP از نام `streamable-http` برای این انتقال استفاده می‌کند، تا پیکربندی‌های کپی‌شده از مستندات خود سرور بدون تغییر کار کنند.

از v2.1.238، `claude mcp list` و `claude mcp get` سرورهای غیرفعال را به‌عنوان `⊘ Disabled` بدون اتصال به آن‌ها برای بررسی سلامت نمایش می‌دهند.

`claude mcp login <name>` / `claude mcp logout <name>` معادل غیرتعاملی جریان OAuth در منوی `/mcp` هستند — احراز هویت یا خروج بدون باز کردن آن. `--no-browser` را به `login` اضافه کنید تا OAuth را از طریق SSH یا در نشست بی‌سر انجام دهید (جریان را از طریق stdin هدایت می‌کند).

## جدول سرورهای MCP در دسترس

| سرور MCP | هدف | ابزارهای رایج | احراز هویت | بلادرنگ |
|------------|---------|--------------|------|-----------|
| **Filesystem** | عملیات فایل | read، write، delete | اجازه‌های OS | ✅ بله |
| **GitHub** | مدیریت مخزن | list_prs، create_issue، push | OAuth | ✅ بله |
| **Slack** | ارتباط تیمی | send_message، list_channels | توکن | ✅ بله |
| **Database** | پرس‌وجوی SQL | query، insert، update | اعتبارنامه | ✅ بله |
| **Google Docs** | دسترسی سند | read، write، share | OAuth | ✅ بله |
| **Asana** | مدیریت پروژه | create_task، update_status | کلید API | ✅ بله |
| **Stripe** | دادهٔ پرداخت | list_charges، create_invoice | کلید API | ✅ بله |
| **Memory** | حافظهٔ پایدار | store، retrieve، delete | محلی | ❌ خیر |

## نمونه‌های عملی

### نمونهٔ ۱: پیکربندی GitHub MCP

**فایل:** `.mcp.json` (ریشهٔ پروژه)

```json
{
  "mcpServers": {
    "github": {
      "type": "http",
      "url": "https://api.githubcopilot.com/mcp/",
      "headers": {
        "Authorization": "Bearer ${GITHUB_PERSONAL_ACCESS_TOKEN}"
      }
    }
  }
}
```

**ابزارهای GitHub MCP در دسترس:**

#### مدیریت Pull Request
- `list_prs` - فهرست همهٔ PRها در مخزن
- `get_pr` - جزئیات PR از جمله diff
- `create_pr` - ایجاد PR جدید
- `update_pr` - به‌روزرسانی توضیحات/عنوان PR
- `merge_pr` - ادغام PR در شاخهٔ main
- `review_pr` - افزودن نظرات بازبینی

**نمونهٔ درخواست:**
```
/mcp__github__get_pr 456

# Returns:
Title: Add dark mode support
Author: @alice
Description: Implements dark theme using CSS variables
Status: OPEN
Reviewers: @bob, @charlie
```

#### مدیریت Issue
- `list_issues` - فهرست همهٔ issueها
- `get_issue` - جزئیات issue
- `create_issue` - ایجاد issue جدید
- `close_issue` - بستن issue
- `add_comment` - افزودن نظر به issue

#### اطلاعات مخزن
- `get_repo_info` - جزئیات مخزن
- `list_files` - ساختار درخت فایل
- `get_file_content` - خواندن محتوای فایل
- `search_code` - جستجو در سراسر کدبیس

#### عملیات Commit
- `list_commits` - تاریخچهٔ commit
- `get_commit` - جزئیات commit خاص
- `create_commit` - ایجاد commit جدید

**راه‌اندازی:**
```bash
export GITHUB_PERSONAL_ACCESS_TOKEN="your_github_token"
# Or use the CLI to add directly:
claude mcp add --transport http github https://api.githubcopilot.com/mcp/ --header "Authorization: Bearer YOUR_GITHUB_PAT"
```

### بسط متغیر محیطی در پیکربندی

پیکربندی‌های MCP از بسط متغیر محیطی با مقادیر پیش‌فرض بازگشتی پشتیبانی می‌کنند. نحو `${VAR}` و `${VAR:-default}` در فیلدهای `command`، `args`، `env`، `url` و `headers` کار می‌کند.

```json
{
  "mcpServers": {
    "api-server": {
      "type": "http",
      "url": "${API_BASE_URL:-https://api.example.com}/mcp",
      "headers": {
        "Authorization": "Bearer ${API_KEY}",
        "X-Custom-Header": "${CUSTOM_HEADER:-default-value}"
      }
    },
    "local-server": {
      "command": "${MCP_BIN_PATH:-npx}",
      "args": ["${MCP_PACKAGE:-@company/mcp-server}"],
      "env": {
        "DB_URL": "${DATABASE_URL:-postgresql://localhost/dev}"
      }
    }
  }
}
```

متغیرها در زمان اجرا بسط می‌یابند:
- `${VAR}` - از متغیر محیطی استفاده می‌کند؛ اگر تنظیم نشده باشد (و پیش‌فرض نداشته باشد)، سرور همچنان با `${VAR}` لفظی بارگذاری می‌شود و `claude mcp list` و `/mcp` دربارهٔ متغیر مفقود هشدار می‌دهند
- `${VAR:-default}` - از متغیر محیطی استفاده می‌کند، در صورت عدم تنظیم به پیش‌فرض بازمی‌گردد

### نمونهٔ ۲: راه‌اندازی MCP دیتابیس

**پیکربندی:**

```json
{
  "mcpServers": {
    "database": {
      "command": "npx",
      "args": ["-y", "@bytebase/dbhub", "--dsn", "${DATABASE_URL}"]
    }
  }
}
```

**نمونهٔ استفاده:**

```markdown
User: Fetch all users with more than 10 orders

Claude: I'll query your database to find that information.

# Using MCP database tool:
SELECT u.*, COUNT(o.id) as order_count
FROM users u
LEFT JOIN orders o ON u.id = o.user_id
GROUP BY u.id
HAVING COUNT(o.id) > 10
ORDER BY order_count DESC;

# Results:
- Alice: 15 orders
- Bob: 12 orders
- Charlie: 11 orders
```

**راه‌اندازی:**
```bash
export DATABASE_URL="postgresql://user:pass@localhost/mydb"
claude mcp add --transport stdio database -- npx -y @bytebase/dbhub \
  --dsn "$DATABASE_URL"
```

> **هشدار**: این راه‌اندازی به Claude دسترسی نوشتن می‌دهد. ابزار `execute_sql` در DBHub هر SQL دریافتی را اجرا می‌کند، از جمله `UPDATE`، `DELETE` و `DROP`، مگره حالت فقط‌خواندنی را فعال کنید. از دیتابیس محلی یا دورریختنی استفاده کنید، هرگز تولیدی.

**راه‌اندازی فقط‌خواندنی (توصیه‌شده):**

یک کاربر دیتابیس بسازید که فقط `SELECT` اجرا کند (نمونهٔ PostgreSQL):

```sql
CREATE ROLE claude_readonly LOGIN PASSWORD 'change-me';
GRANT CONNECT ON DATABASE mydb TO claude_readonly;
GRANT USAGE ON SCHEMA public TO claude_readonly;
GRANT SELECT ON ALL TABLES IN SCHEMA public TO claude_readonly;
```

حالت فقط‌خواندنی را در یک `dbhub.toml` فعال کنید. پرچم قدیمی `--readonly` دیگر کار نمی‌کند. DBHub `${DATABASE_URL}` را از محیط شما پر می‌کند، پس هیچ اعتبارنامه‌ای در فایل نمی‌رود:

```toml
[[sources]]
id = "default"
dsn = "${DATABASE_URL}"

[[tools]]
name = "execute_sql"
source = "default"
readonly = true
```

سپس DBHub را به فایل اشاره دهید به‌جای پاسخ `--dsn`. سرور دسترسی‌نوشتن `database` که در بالا اضافه کردید را ابتدا حذف کنید، زیرا Claude Code سرور دومی با همان نام اضافه نمی‌کند:

```bash
# Replace the write-access server added above
claude mcp remove database
export DATABASE_URL="postgresql://claude_readonly:change-me@localhost/mydb"
claude mcp add --transport stdio database -- npx -y @bytebase/dbhub \
  --config "$PWD/dbhub.toml"
```

حالت فقط‌خواندنی متن SQL را فیلتر می‌کند و در گذشته راه‌های دورزدن داشته (رفع‌شده در DBHub 0.22.6)، پس کاربر فقط‌`SELECT` است که واقعاً داده‌های شما را محافظت می‌کند. بخش [DBHub read-only mode](https://dbhub.ai/tools/execute-sql#read-only-mode) را ببینید.

### نمونهٔ ۳: جریان‌کار چند-MCP

**سناریو: تولید گزارش روزانه**

```markdown
# Daily Report Workflow using Multiple MCPs

## Setup
1. GitHub MCP - fetch PR metrics
2. Database MCP - query sales data
3. Slack MCP - post report
4. Filesystem MCP - save report

## Workflow

### Step 1: Fetch GitHub Data
/mcp__github__list_prs completed:true last:7days

Output:
- Total PRs: 42
- Average merge time: 2.3 hours
- Review turnaround: 1.1 hours

### Step 2: Query Database
SELECT COUNT(*) as sales, SUM(amount) as revenue
FROM orders
WHERE created_at > NOW() - INTERVAL '1 day'

Output:
- Sales: 247
- Revenue: $12,450

### Step 3: Generate Report
Combine data into HTML report

### Step 4: Save to Filesystem
Write report.html to /reports/

### Step 5: Post to Slack
Send summary to #daily-reports channel

Final Output:
✅ Report generated and posted
📊 47 PRs merged this week
💰 $12,450 in daily sales
```

**راه‌اندازی:**
```bash
export GITHUB_PERSONAL_ACCESS_TOKEN="your_github_token"
export DATABASE_URL="postgresql://user:pass@localhost/mydb"
export SLACK_BOT_TOKEN="your_slack_bot_token"
export SLACK_TEAM_ID="your_slack_team_id"
# Add each MCP server via the CLI or configure them in .mcp.json
```

### نمونهٔ ۴: عملیات MCP فایل‌سیستم

**پیکربندی:**

```json
{
  "mcpServers": {
    "filesystem": {
      "command": "npx",
      "args": ["@modelcontextprotocol/server-filesystem", "/home/user/projects"]
    }
  }
}
```

**عملیات در دسترس:**

| عملیات | دستور | هدف |
|-----------|---------|---------|
| فهرست فایل‌ها | `ls ~/projects` | نمایش محتوای شاخه |
| خواندن فایل | `cat src/main.ts` | خواندن محتوای فایل |
| نوشتن فایل | `create docs/api.md` | ایجاد فایل جدید |
| ویرایش فایل | `edit src/app.ts` | تغییر فایل |
| جستجو | `grep "async function"` | جستجو در فایل‌ها |
| حذف | `rm old-file.js` | حذف فایل |

**راه‌اندازی:**
```bash
# Use the CLI to add directly:
claude mcp add --transport stdio filesystem -- npx @modelcontextprotocol/server-filesystem /home/user/projects
```

## MCP در برابر حافظه: ماتریس تصمیم

```mermaid
graph TD
    A["Need external data?"]
    A -->|No| B["Use Memory"]
    A -->|Yes| C["Does it change frequently?"]
    C -->|No/Rarely| B
    C -->|Yes/Often| D["Use MCP"]

    B -->|Stores| E["Preferences<br/>Context<br/>History"]
    D -->|Accesses| F["Live APIs<br/>Databases<br/>Services"]

    style A fill:#fff3e0,stroke:#333,color:#333
    style B fill:#e1f5fe,stroke:#333,color:#333
    style C fill:#fff3e0,stroke:#333,color:#333
    style D fill:#f3e5f5,stroke:#333,color:#333
    style E fill:#e8f5e9,stroke:#333,color:#333
    style F fill:#e8f5e9,stroke:#333,color:#333
```

## الگوی درخواست/پاسخ

```mermaid
sequenceDiagram
    participant App as Claude
    participant MCP as MCP Server
    participant DB as Database

    App->>MCP: Request: "SELECT * FROM users WHERE id=1"
    MCP->>DB: Execute query
    DB-->>MCP: Result set
    MCP-->>App: Return parsed data
    App->>App: Process result
    App->>App: Continue task

    Note over MCP,DB: Real-time access<br/>No caching
```

## متغیرهای محیطی

اعتبارنامه‌های حساس را در متغیرهای محیطی ذخیره کنید:

```bash
# ~/.bashrc or ~/.zshrc
export GITHUB_PERSONAL_ACCESS_TOKEN="ghp_xxxxxxxxxxxxx"
export DATABASE_URL="postgresql://user:pass@localhost/mydb"
export SLACK_BOT_TOKEN="your-slack-bot-token"
export SLACK_TEAM_ID="T0000000000"
```

سپس آن‌ها را در پیکربندی MCP ارجاع دهید:

```json
{
  "env": {
    "GITHUB_PERSONAL_ACCESS_TOKEN": "${GITHUB_PERSONAL_ACCESS_TOKEN}"
  }
}
```

## Claude به‌عنوان سرور MCP (`claude mcp serve`)

خود Claude Code می‌تواند به‌عنوان سرور MCP برای سایر اپلیکیشن‌ها عمل کند. این به ابزارهای خارجی، ویرایشگرها و سیستم‌های خودکارسازی اجازه می‌دهد از توانایی‌های Claude از طریق پروتکل استاندارد MCP بهره ببرند.

```bash
# Start Claude Code as an MCP server on stdio
claude mcp serve
```

سایر اپلیکیشن‌ها سپس می‌توانند به این سرور متصل شوند مانند هر سرور MCP مبتنی بر stdio. مثلاً برای افزودن Claude Code به‌عنوان سرور MCP در یک نمونهٔ دیگر Claude Code:

```bash
claude mcp add --transport stdio claude-agent -- claude mcp serve
```

این برای ساخت جریان‌کارهای چندایجنتی مفید است که در آن یک نمونهٔ Claude دیگری را رهبری می‌کند.

## پیکربندی MCP مدیریت‌شده (سازمانی)

برای استقرارهای سازمانی، مدیران IT خط‌مشی سرور MCP را از طریق دو مکانیسم جداگانه اعمال می‌کنند: یک فایل `managed-mcp.json` که مجموعه‌ای ثابت از سرورها را با کنترل انحصاری مستقر می‌کند و کلیدهای تنظیمات `allowedMcpServers` / `deniedMcpServers` که فیلتر می‌کنند کدام سرورهای پیکربندی‌شده ممکن است بارگذاری شوند.

**مکان:**
- macOS: `/Library/Application Support/ClaudeCode/managed-mcp.json`
- Linux and WSL: `/etc/claude-code/managed-mcp.json`
- Windows: `C:\Program Files\ClaudeCode\managed-mcp.json`

`managed-mcp.json` از همان قالب فایل `.mcp.json` پروژه استفاده می‌کند — یک نقشهٔ `mcpServers` سطح‌بالا. سرورها را مستقر می‌کند؛ آن‌ها را فیلتر نمی‌کند:

```json
{
  "mcpServers": {
    "example-remote": {
      "type": "http",
      "url": "https://mcp.example.com/mcp"
    },
    "company-internal": {
      "type": "stdio",
      "command": "/usr/local/bin/company-mcp-server",
      "args": ["--config", "/etc/company/mcp-config.json"]
    }
  }
}
```

هر کاربری روی ماشین می‌تواند این فایل را بخواند، پس هرگز اعتبارنامه‌ای در بلوک `env` نگذارید. از بسط `${VAR}`، OAuth یا `headersHelper` استفاده کنید.

**فیلترکردن: فهرست‌های مجاز و غیرمجاز**

`allowedMcpServers`، `deniedMcpServers` و `allowAllClaudeAiMcps` **کلیدهای تنظیمات هستند، نه فیلدهایی از `managed-mcp.json`**. آن‌ها را در یک منبع تنظیمات مدیریت‌شده قرار دهید — تنظیمات مدیریت‌شدهٔ سرور، `managed-settings.json`، یک پروفایل MDM یا رجیستری — تا قابل اعمال باشند:

- `allowedMcpServers` -- فهرست مجاز سرورهای مجاز. `allowManagedMcpServersOnly: true` را در کنار آن، در همان منبع مدیریت‌شده تنظیم کنید، وگرنه فهرست‌های مجاز از هر محدوده‌ای ادغام می‌شوند و کاربر می‌تواند yours را گسترده‌تر کند.
- `deniedMcpServers` -- فهرست غیرمجاز سرورهای مسدودشده. از هر محدوده‌ای بدون توجه ادغام می‌شود.
- `allowAllClaudeAiMcps` -- اتصال‌دهنده‌های ابری claude.ai را در کنار یک `managed-mcp.json` مستقرشده بارگذاری می‌کند (v2.1.149+). فقط از لایه‌های خط‌مشی کنترل‌شدهٔ مدیر خوانده می‌شود.

هر مدخل یک شیء با **یک** کلید است:

| کلید | تطبیق می‌زند |
|-----|---------|
| `serverUrl` | یک URL سرور راه‌دور، دقیق یا با وایلدکارت `*` |
| `serverCommand` | دستور و آرگومان‌های دقیقی که یک سرور stdio را راه‌اندازی می‌کنند، به‌عنوان یک آرایه — هر آرگومان، به‌ترتیب |
| `serverName` | برچسب تعیین‌شده توسط کاربر. **فقط تطابق دقیق؛ وایلدکارت‌ها بسط نمی‌یابند** |

**نمونهٔ پیکربندی:**

```json
{
  "allowedMcpServers": [
    { "serverUrl": "https://mcp.example.com/*" },
    { "serverCommand": ["/usr/local/bin/company-mcp-server", "--config", "/etc/company/mcp-config.json"] }
  ],
  "deniedMcpServers": [
    { "serverName": "untrusted-server" },
    { "serverUrl": "http://*" }
  ],
  "allowManagedMcpServersOnly": true
}
```

یک تنظیم مدیریت‌شدهٔ سوم، `managedMcpServers` (v2.1.259+)، به یک سازمان اجازه می‌دهد سرورهای HTTP/SSE MCP را به هر کاربر عرضه کند. مدخل‌ها همان شکل `.mcp.json` را دارند؛ مدخل‌هایی که دستوری برای اجرا نام‌گذاری کنند رد می‌شوند.

> **نکته:** وقتی هم `allowedMcpServers` و هم `deniedMcpServers` با یک سرور تطبیق می‌زنند، قانون غیرمجاز اولویت دارد.

## سرورهای MCP ارائه‌شده توسط پلاگین

پلاگین‌ها می‌توانند سرورهای MCP خود را همراه داشته باشند، که هنگام نصب پلاگین به‌طور خودکار در دسترس قرار می‌گیرند. سرورهای MCP ارائه‌شده توسط پلاگین به دو روش تعریف می‌شوند:

1. **`.mcp.json` مستقل** -- یک فایل `.mcp.json` در شاخهٔ ریشهٔ پلاگین قرار دهید
2. **درون‌خطی در `plugin.json`** -- سرورهای MCP را مستقیماً در مانیفست پلاگین تعریف کنید

از متغیر `${CLAUDE_PLUGIN_ROOT}` برای ارجاع مسیرهای نسبی به شاخهٔ نصب پلاگین استفاده کنید:

```json
{
  "mcpServers": {
    "plugin-tools": {
      "command": "node",
      "args": ["${CLAUDE_PLUGIN_ROOT}/dist/mcp-server.js"],
      "env": {
        "CONFIG_PATH": "${CLAUDE_PLUGIN_ROOT}/config.json"
      }
    }
  }
}
```

## MCP با محدودهٔ ایجنتی

سرورهای MCP می‌توانند درون‌خطی در فرانت‌متر ایجنت با کلید `mcpServers:` تعریف شوند، که آن‌ها را به یک ایجنتی خاص محدود می‌کند به‌جای کل پروژه. این مفید است وقتی یک ایجنت نیاز به دسترسی به یک سرور MCP خاص دارد که سایر ایجنتهای جریان‌کار نیازی ندارند.

```yaml
---
name: my-tool-agent
description: Uses my-tool for specialized operations
mcpServers:
  my-tool:
    type: http
    url: https://my-tool.example.com/mcp
---

You are an agent with access to my-tool for specialized operations.
```

سرورهای MCP با محدودهٔ ایجنتی فقط در بافتار اجرای همان ایجنت در دسترسند و با ایجنتهای والد یا همزاد به‌اشتراک گذاشته نمی‌شوند.

## محدودیت‌های خروجی MCP

Claude Code محدودیت‌هایی را روی خروجی ابزار MCP اعمال می‌کند تا سرریز بافتار پیشگیری شود:

| محدودیت | آستانه | رفتار |
|-------|-----------|----------|
| **هشدار** | ۱۰٬۰۰۰ توکن | هشداری نمایش داده می‌شود که خروجی بزرگ است |
| **حداکثر پیش‌فرض** | ۲۵٬۰۰۰ توکن | خروجی بزرگ‌تر در یک فایل ذخیره می‌شود و مسیر فایل به‌جای آن وارد گفت‌وگو می‌شود |
| **پایماند روی دیسک** | ۵۰٬۰۰۰ نویسه | نتایج ابزار بیش از ۵۰K نویسه روی دیسک پایماند می‌شوند |

حداکثر محدودیت خروجی از طریق متغیر محیطی `MAX_MCP_OUTPUT_TOKENS` قابل پیکربندی است:

```bash
# Increase the max output to 50,000 tokens
export MAX_MCP_OUTPUT_TOKENS=50000
```

## پس‌زمینه‌ای خودکار فراخوانی‌های ابزار طولانی (v2.1.212)

فراخوانی‌های ابزار MCP که بیش از ۲ دقیقه طول می‌کشند اکنون به‌طور خودکار به پس‌زمینه منتقل می‌شوند، تا نشست قابل‌استفاده بماند به‌جای مسدود شدن روی یک ابزار کُند. آستانه قابل پیکربندی است و رفتار از طریق `CLAUDE_CODE_MCP_AUTO_BACKGROUND_MS` قابل تنظیم یا غیرفعال است:

```bash
# Change the auto-background threshold to 5 minutes (300,000ms)
export CLAUDE_CODE_MCP_AUTO_BACKGROUND_MS=300000
```

## حل تورم بافتار با اجرای کد

با مقیاس‌پذیری پذیرش MCP، اتصال به ده‌ها سرور با صدها یا هزاران ابزار چالش بزرگی ایجاد می‌کند: **تورم بافتار**. این مسئله بزرگ‌ترین مشکل MCP در مقیاس است و تیم مهندسی Anthropic راه‌حلی ظریف پیشنهاد داده — استفاده از اجرای کد به‌جای فراخوانی ابزار مستقیم.

> **منبع**: [Code Execution with MCP: Building More Efficient Agents](https://www.anthropic.com/engineering/code-execution-with-mcp) — بلاگ مهندسی Anthropic

### مشکل: دو منبع هدررفت توکن

**۱. تعریف‌های ابزار پنجرهٔ بافتار را اضافه‌بار می‌کنند**

اکثر کلاینت‌های MCP همهٔ تعریف‌های ابزار را پیش‌رو بارگذاری می‌کنند. هنگام اتصال به هزاران ابزار، مدل باید صدها هزار توکن را پیش از خواندن درخواست کاربر پردازش کند.

**۲. نتایج میانی توکن‌های اضافی مصرف می‌کنند**

هر نتیجهٔ ابزار میانی از بافتار مدل عبور می‌کند. انتقال رویداد جلسه از Google Drive به Salesforce را در نظر بگیرید — رویداد کامل دو بار از بافتار عبور می‌کند: یک‌بار هنگام خواندن، و دوباره هنگام نوشتن به مقصد. یک رویداد ۲-ساعته می‌تواند ۵۰٬۰۰۰+ توکن اضافی باشد.

```mermaid
graph LR
    A["Model"] -->|"Tool Call: getDocument"| B["MCP Server"]
    B -->|"Full transcript (50K tokens)"| A
    A -->|"Tool Call: updateRecord<br/>(re-sends full transcript)"| B
    B -->|"Confirmation"| A

    style A fill:#ffcdd2,stroke:#333,color:#333
    style B fill:#f3e5f5,stroke:#333,color:#333
```

### راه‌حل: ابزارهای MCP به‌عنوان API کد

به‌جای عبور تعریف‌های ابزار و نتایج از پنجرهٔ بافتار، ایجنت **کد می‌نویسد** که ابزارهای MCP را به‌عنوان API فراخوانی می‌کند. کد در یک محیط اجرای سندباکس‌شده اجرا می‌شود و فقط نتیجهٔ نهایی به مدل بازمی‌گردد.

```mermaid
graph LR
    A["Model"] -->|"Writes code"| B["Code Execution<br/>Environment"]
    B -->|"Calls tools directly"| C["MCP Servers"]
    C -->|"Data stays in<br/>execution env"| B
    B -->|"Only final result<br/>(minimal tokens)"| A

    style A fill:#c8e6c9,stroke:#333,color:#333
    style B fill:#e1f5fe,stroke:#333,color:#333
    style C fill:#f3e5f5,stroke:#333,color:#333
```

#### چگونه کار می‌کند

ابزارهای MCP به‌عنوان یک درخت فایل توابع نوع‌دار عرضه می‌شوند:

```
servers/
├── google-drive/
│   ├── getDocument.ts
│   └── index.ts
├── salesforce/
│   ├── updateRecord.ts
│   └── index.ts
└── ...
```

هر فایل ابزار حاوی یک پوشش نوع‌دار است:

```typescript
// ./servers/google-drive/getDocument.ts
import { callMCPTool } from "../../../client.js";

interface GetDocumentInput {
  documentId: string;
}

interface GetDocumentResponse {
  content: string;
}

export async function getDocument(
  input: GetDocumentInput
): Promise<GetDocumentResponse> {
  return callMCPTool<GetDocumentResponse>(
    'google_drive__get_document', input
  );
}
```

سپس ایجنت کدی می‌نویسد تا ابزارها را رهبری کند:

```typescript
import * as gdrive from './servers/google-drive';
import * as salesforce from './servers/salesforce';

// Data flows directly between tools — never through the model
const transcript = (
  await gdrive.getDocument({ documentId: 'abc123' })
).content;

await salesforce.updateRecord({
  objectType: 'SalesMeeting',
  recordId: '00Q5f000001abcXYZ',
  data: { Notes: transcript }
});
```

**نتیجه: مصرف توکن از ~۱۵۰٬۰۰۰ به ~۲٬۰۰۰ کاهش می‌یابد — ۹۸٫۷٪ کاهش.**

### مزایای کلیدی

| مزیت | توضیحات |
|---------|-------------|
| **افشونگی پیش‌رو** | ایجنت فایل‌سیستم را مرور می‌کند تا فقط تعریف‌های ابزاری که نیاز دارد بارگذاری کند، به‌جای همهٔ ابزارها پیش‌رو |
| **نتایج بافتار-کارآمد** | داده در محیط اجرا پیش از بازگشت به مدل فیلتر/تبدیل می‌شود |
| **جریان کنترل قدرتمند** | حلقه‌ها، شرطی‌سازی و مدیریت خطا در کد اجرا می‌شوند بدون رفت‌وبرگشت از مدل |
| **حفظ حریم خصوصی** | دادهٔ میانی (PII، رکوردهای حساس) در محیط اجرا می‌ماند؛ هرگز وارد بافتار مدل نمی‌شود |
| **پایماند وضعیت** | ایجنتهای میانی می‌توانند نتایج میانی را در فایل ذخیره کنند و توابع مهارت قابل‌استفاده‌ی مجدد بسازند |

#### نمونه: فیلترکردن مجموعه‌داده‌های بزرگ

```typescript
// Without code execution — all 10,000 rows flow through context
// TOOL CALL: gdrive.getSheet(sheetId: 'abc123')
//   -> returns 10,000 rows in context

// With code execution — filter in the execution environment
const allRows = await gdrive.getSheet({ sheetId: 'abc123' });
const pendingOrders = allRows.filter(
  row => row["Status"] === 'pending'
);
console.log(`Found ${pendingOrders.length} pending orders`);
console.log(pendingOrders.slice(0, 5)); // Only 5 rows reach the model
```

#### نمونه: حلقه بدون رفت‌وبرگشت

```typescript
// Poll for a deployment notification — runs entirely in code
let found = false;
while (!found) {
  const messages = await slack.getChannelHistory({
    channel: 'C123456'
  });
  found = messages.some(
    m => m.text.includes('deployment complete')
  );
  if (!found) await new Promise(r => setTimeout(r, 5000));
}
console.log('Deployment notification received');
```

### مصالحه‌های در نظر گرفته

اجرای کد پیچیدگی خود را وارد می‌کند. اجرای کد تولیدشده توسط ایجنت نیازمند:

- یک **محیط اجرای سندباکس‌شده امن** با محدودیت‌های منابع مناسب
- **پایش و ثبت** کد اجراشده
- **بار سرباز زیرساختی** اضافی نسبت به فراخوانی ابزار مستقیم

مزایا — کاهش هزینهٔ توکن، تأخیر پایین‌تر، ترکیب ابزار بهتر — باید در برابر این هزینه‌های پیاده‌سازی سنجیده شود. برای ایجنتهای با تنها چند سرور MCP، فراخوانی ابزار مستقیم ساده‌تر است. برای ایجنتهای در مقیاس (ده‌ها سرور، صدها ابزار)، اجرای کد بهبودی چشمگیر است.

### MCPorter: یک محیط‌اجرایی برای ترکیب ابزار MCP

[MCPorter](https://github.com/steipete/mcporter) یک محیط‌اجرایی TypeScript و جعبه‌ابزار CLI است که فراخوانی سرورهای MCP را بدون کد اضافی عملی می‌سازد — و کمک می‌کند تورم بافتار را از طریق عرضهٔ گزینشی ابزار و پوشش‌های نوع‌دار کاهش دهید.

**چه می‌حل کند:** به‌جای بارگذاری همهٔ تعریف‌های ابزار از همهٔ سرورهای MCP پیش‌رو، MCPorter به شما اجازه می‌دهد ابزارهای خاصی را در صورت درخواست کشف، بررسی و فراخوانی کنید — و بافتار خود را سبک نگه دارید.

**ویژگی‌های کلیدی:**

| ویژگی | توضیحات |
|---------|-------------|
| **کشف بدون‌پیکربندی** | سرورهای MCP را از Cursor، Claude، Codex یا پیکربندی‌های محلی به‌طور خودکار کشف می‌کند |
| | کلاینت‌های ابزار نوع‌دار: `mcporter emit-ts` رابط‌های `.d.ts` و پوشش‌های آماده‌اجرا تولید می‌کند |
| **API قابل‌ترکیب** | `createServerProxy()` ابزارها را به‌عنوان متدهای camelCase با راهنماهای `.text()`، `.json()`، `.markdown()` عرضه می‌کند |
| **تولید CLI** | `mcporter generate-cli` هر سرور MCP را به یک CLI مستقل با فیلتر `--include-tools` / `--exclude-tools` تبدیل می‌کند |
| **پنهان‌سازی پارامتر** | پارامترهای اختیاری به‌صورت پیش‌فرض پنهان می‌مانند، که اطناب طرح‌ک塌 را کاهش می‌دهد |

**نصب:**

```bash
npx mcporter list          # No install required — discover servers instantly
pnpm add mcporter          # Add to a project
brew install steipete/tap/mcporter  # macOS via Homebrew
```

**نمونه — ترکیب ابزار در TypeScript:**

```typescript
import { createRuntime, createServerProxy } from "mcporter";

const runtime = await createRuntime();
const gdrive = createServerProxy(runtime, "google-drive");
const salesforce = createServerProxy(runtime, "salesforce");

// Data flows between tools without passing through the model context
const doc = await gdrive.getDocument({ documentId: "abc123" });
await salesforce.updateRecord({
  objectType: "SalesMeeting",
  recordId: "00Q5f000001abcXYZ",
  data: { Notes: doc.text() }
});
```

**نمونه — فراخوانی ابزار CLI:**

```bash
# Call a specific tool directly
npx mcporter call linear.create_comment issueId:ENG-123 body:'Looks good!'

# List available servers and tools
npx mcporter list
```

MCPorter رویکرد اجرای کد توضیح‌شده در بالا را با تأمین زیرساخت محیط‌اجرایی برای فراخوانی ابزارهای MCP به‌عنوان API نوع‌دار تکمیل می‌کند — و نگه‌داشتن داده‌های میانی در خارج بافتار مدل را ساده می‌سازد.

## بهترین شیوه‌ها

### ملاحظات امنیتی

#### کارهای درست ✅
- از متغیرهای محیطی برای همهٔ اعتبارنامه‌ها استفاده کنید
- توکن‌ها و کلیدهای API را منظم بچرخانید (توصیهٔ ماهانه)
- وقتی ممکن است از توکن‌های فقط‌خواندنی استفاده کنید
- محدودهٔ دسترسی سرور MCP را به حداقل لازم محدود کنید
- استفادهٔ سرور MCP و لاگ‌های دسترسی را پایش کنید
- برای سرویس‌های خارجی وقتی در دسترس است از OAuth استفاده کنید
- محدودیت نرخ را روی درخواست‌های MCP پیاده کنید
- اتصالات MCP را پیش از استفادهٔ تولیدی آزمایش کنید
- همهٔ اتصالات MCP فعال را مستند کنید
- پکیج‌های سرور MCP را به‌روز نگه دارید

#### کارهای نادرست ❌
- اعتبارنامه‌ها را در فایل‌های پیکربندی هاردکد نکنید
- توکن‌ها یا اسرار را در گیت commit نکنید
- توکن‌ها را در چت‌های تیمی یا ایمیل به‌اشتراک نگذارید
- از توکن‌های شخصی برای پروژه‌های تیمی استفاده نکنید
- اجازه‌های غیرضروری ندهید
- خطاهای احراز هویت را نادیده نگیرید
- نقاط پایانی MCP را به‌صورت عمومی در دسترس نگذارید
- سرورهای MCP را با امتیازات root/مدیر اجرا نکنید
- داده‌های حساس را در لاگ‌ها کَش نکنید
- مکانیسم‌های احراز هویت را غیرفعال نکنید

### بهترین شیوه‌های پیکربندی

۱. **کنترل نسخه**: `.mcp.json` را در گیت نگه دارید اما برای اسرار از متغیرهای محیطی استفاده کنید
۲. **حداقل امتیاز**: حداقل اجازه‌های لازم برای هر سرور MCP را بدهید
۳. **ایزوله‌سازی**: وقتی ممکن است سرورهای MCP مختلف را در فرآیندهای جداگانه اجرا کنید
۴. **پایش**: همهٔ درخواست‌ها و خطاهای MCP را برای مسیرهای ممیزی لاگ کنید
۵. **آزمایش**: همهٔ پیکربندی‌های MCP را پیش از استقرار در تولید آزمایش کنید

### نکته‌های کارایی

- داده‌های پرمصرف را در سطح اپلیکیشن کَش کنید
- از پرس‌وجوی‌های MCP که ویژه‌اند استفاده کنید تا انتقال داده کاهش یابد
- زمان‌های پاسخ را برای عملیات MCP پایش کنید
- محدودیت نرخ را برای APIهای خارجی در نظر بگیرید
- هنگام انجام چندین عملیات از دسته‌بندی استفاده کنید

## دستورالعمل‌های نصب

### پیش‌نیازها
- Node.js و npm نصب‌شده
- Claude Code CLI نصب‌شده
- توکن‌ها/اعتبارنامه‌های API برای سرویس‌های خارجی

### راه‌اندازی گام‌به‌گام

۱. **اولین سرور MCP خود را اضافه کنید** با استفاده از CLI (نمونه: GitHub):
```bash
claude mcp add --transport http github https://api.githubcopilot.com/mcp/ --header "Authorization: Bearer YOUR_GITHUB_PAT"
```

   یا یک فایل `.mcp.json` در ریشهٔ پروژه بسازید:
```json
{
  "mcpServers": {
    "github": {
      "type": "http",
      "url": "https://api.githubcopilot.com/mcp/",
      "headers": {
        "Authorization": "Bearer ${GITHUB_PERSONAL_ACCESS_TOKEN}"
      }
    }
  }
}
```

۲. **متغیرهای محیطی را تنظیم کنید:**
```bash
export GITHUB_PERSONAL_ACCESS_TOKEN="your_github_personal_access_token"
```

۳. **اتصال را آزمایش کنید:**
```bash
claude /mcp
```

۴. **از ابزارهای MCP استفاده کنید:**
```bash
/mcp__github__list_prs
/mcp__github__create_issue "Title" "Description"
```

### نصب برای سرویس‌های خاص

**GitHub MCP:**
```bash
npm install -g @modelcontextprotocol/server-github
```

**Database MCP:**
```bash
npm install -g @bytebase/dbhub
```

**Filesystem MCP:**
```bash
npm install -g @modelcontextprotocol/server-filesystem
```

**Slack MCP (deprecated package):**
```bash
npm install -g @modelcontextprotocol/server-slack
```

## رفع اشکال

### از خروجی خطا آغاز کنید (v2.1.219+)

اگر سروری متصل نمی‌شود، پیش از تغییر چیز `claude mcp list` (یا `/mcp` در نشست) را اجرا کنید. Claude Code اکنون **کد وضعیت HTTP و متن خطای سرور** را کنار سرور ناموفق چاپ می‌کند، تا `401 Unauthorized` یا `404 Not Found` به‌جای یک «اتصال ناموفق» عمومی دریافت کنید:

```bash
# Shows connection status plus HTTP status and error text for failures
claude mcp list
```

ابتدا وضعیت را بخوانید — به شما می‌گوید کدام رفع applicable است:

- `401` / `403` → اعتبارنامه‌های بد یا منقضی؛ با `claude mcp login <name>` دوباره احراز هویت کنید
- `404` → URL نادرست (یک پسوند مسیر `/mcp` یا `/sse` مفقود علت رایج است)
- `5xx` / timeout → سرور راه‌دور از کار افتاخته؛ بخش [Connection Timeout](#connection-timeout) را ببینید

### فضای خالی پنهان در مقادیر پیکربندی (v2.1.219+)

Claude Code هشدار می‌دهد وقتی یک مقدار پیکربندی MCP **فضای خالی پیشرو یا پسرو** دارد. این علت رایج و دشوار‌یافت‌شدهٔ شکست احراز هویت است: توکنی که از مرورگر یا پیام چت کپی شده اغلب یک فاصله یا خط‌جدید پسرو دارد که وردست‌به‌وردست در هدر `Authorization` ارسال و به‌عنوان اعتبارنامهٔ نادرست رد می‌شود.

اگر این هشدار را دیدید، مقدار را در `.mcp.json` (یا متغیر محیطی که از آن بسط می‌یابد) دوباره بررسی و کوتاه کنید:

```bash
# Reveals hidden leading/trailing whitespace between the delimiters
printf '[%s]\n' "$GITHUB_PERSONAL_ACCESS_TOKEN"
```

### سرورهای رد‌شده در اجراهای بی‌سر (v2.1.219+)

سرورهای ارسال‌شده از طریق `--mcp-config` که اعتبارسنجی پیکربندی شکست می‌خورند **رد می‌شوند** به‌جای سقط اجرا، تا یک اسکریپت بی‌سر می‌تواند ظاهراً کار کند در حالی که نیمی از ابزارهایش را از دست داده. Claude Code اکنون گزارش می‌دهد کدام‌ها حذف شده‌اند:

- **اجراهای بی‌سر / `-p`**: رویداد `init` در stream-json یک فیلد `mcp_server_errors` دارد که هر مدخل رد‌شده را فهرست می‌کند. پیش از اعتماد به خروجی اجرا آن را بررسی کنید.
- **اجراهای ترمینال تعاملی**: همان مشکل به‌عنوان هشدار راه‌اندازی هنگام آغاز نشست چاپ می‌شود.

```bash
# Inspect skipped --mcp-config entries in a headless run
claude -p "list my tools" --mcp-config ./servers.json \
  --output-format stream-json --verbose \
  | jq -r 'select(.type == "system" and .subtype == "init") | .mcp_server_errors'
```

### سرور MCP یافت نشد
```bash
# Verify MCP server is installed
npm list -g @modelcontextprotocol/server-github

# Install if missing
npm install -g @modelcontextprotocol/server-github
```

### شکست احراز هویت
```bash
# Verify environment variable is set
echo $GITHUB_PERSONAL_ACCESS_TOKEN

# Re-export if needed
export GITHUB_PERSONAL_ACCESS_TOKEN="your_token"

# Verify token has correct permissions
# Check GitHub token scopes at: https://github.com/settings/tokens
```

### تایم‌اوت اتصال
- اتصال شبکه را بررسی کنید: `ping api.github.com`
- نقطهٔ پایانی API در دسترس را تأیید کنید
- محدودیت‌های نرخ روی API را بررسی کنید
- افزایش تایم‌اوت در پیکربندی را امتحان کنید
- فایروال یا مشکل پراکسی را بررسی کنید

### سقوط سرور MCP
- لاگ‌های سرور MCP را بررسی کنید: `~/.claude/logs/`
- همهٔ متغیرهای محیطی تنظیم‌شده را تأیید کنید
- اجازه‌های فایل مناسب را تأمین کنید
- نصب مجدد پکیج سرور MCP را امتحان کنید
- فرآیندهای متعارض روی همان پورت را بررسی کنید

## مفاهیم مرتبط

### حافظه در برابر MCP
- **حافظه**: دادهٔ پایدار و تغییرنایافته را ذخیره می‌کند (ترجیحات، بافتار، تاریخچه)
- **MCP**: به دادهٔ زنده و در حال تغییر دسترسی می‌دهد (APIها، دیتابیس‌ها، سرویس‌های بلادرنگ)

### کی از کدام استفاده کنید
- **از حافظه** برای: ترجیحات کاربر، تاریخچهٔ گفت‌وگو، بافتار آموخته‌شده
- **از MCP** برای: issueهای جاری GitHub، پرس‌وجوی‌های زندهٔ دیتابیس، دادهٔ بلادرنگ

### یکپارچه‌سازی با سایر ویژگی‌های Claude
- MCP را با حافظه برای بافتار غنی ترکیب کنید
- از ابزارهای MCP در پرامپت‌ها برای استدلال بهتر استفاده کنید
- برای جریان‌کارهای پیچیده از چندین MCP بهره ببرید

## منابع اضافی

- [مستندات رسمی MCP](https://code.claude.com/docs/en/mcp)
- [مشخصات پروتکل MCP](https://modelcontextprotocol.io/specification)
- [مخزن GitHub MCP](https://github.com/modelcontextprotocol/servers)
- [سرورهای MCP در دسترس](https://github.com/modelcontextprotocol/servers)
- [MCPorter](https://github.com/steipete/mcporter) — محیط‌اجرایی TypeScript و CLI برای فراخوانی سرورهای MCP بدون کد اضافی
- [Code Execution with MCP](https://www.anthropic.com/engineering/code-execution-with-mcp) — بلاگ مهندسی Anthropic دربارهٔ حل تورم بافتار
- [مرجع CLI Claude Code](https://code.claude.com/docs/en/cli-reference)
- [مستندات API Claude](https://docs.anthropic.com)

---

**آخرین به‌روزرسانی**: ۱۸ اکتبر ۲۰۲۶
**نسخهٔ Claude Code**: 2.1.302
**منابع**:
- https://code.claude.com/docs/en/mcp
- https://code.claude.com/docs/en/managed-mcp
- https://code.claude.com/docs/en/changelog
- https://github.com/anthropics/claude-code/releases/tag/v2.1.117
- https://github.com/anthropics/claude-code/releases/tag/v2.1.139
- https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md
- https://code.claude.com/docs/en/model-config
- https://code.claude.com/docs/en/mcp#configure-tool-search
- https://code.claude.com/docs/en/env-vars
- https://github.com/anthropics/claude-code/releases/tag/v2.1.285
- https://github.com/anthropics/claude-code/releases/tag/v2.1.296
- https://code.claude.com/docs/en/mcp#tool-search-for-mcp-server-authors
- https://code.claude.com/docs/en/mcp#environment-variable-expansion-in-mcp-json
- https://code.claude.com/docs/en/sub-agents
**مدل‌های سازگار**: Claude Fable 5, Claude Opus 5, Claude Sonnet 5, Claude Sonnet 4.6, Claude Opus 4.8, Claude Haiku 4.5
