<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../resources/logos/claude-howto-logo-dark.svg">
  <img alt="Claude How To" src="../resources/logos/claude-howto-logo.svg">
</picture>

<p align="center">
  <a href="https://github.com/trending">
    <img src="https://img.shields.io/badge/GitHub-🔥%20%231%20Trending-purple?style=for-the-badge&logo=github"/>
  </a>
</p>

[![GitHub Stars](https://img.shields.io/github/stars/luongnv89/claude-howto?style=flat&color=gold)](https://github.com/luongnv89/claude-howto/stargazers)
[![GitHub Forks](https://img.shields.io/github/forks/luongnv89/claude-howto?style=flat)](https://github.com/luongnv89/claude-howto/network/members)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Version](https://img.shields.io/badge/version-2.1.112-brightgreen)](CHANGELOG.md)
[![Claude Code](https://img.shields.io/badge/Claude_Code-2.1+-purple)](https://code.claude.com)

# کنترل کامل Claude Code در یک آخر هفته

از تایپ `claude` تا هماهنگی ایجنت‌ها، هوک‌ها، مهارت‌ها و سرورهای MCP — با آموزش‌های تصویری، قالب‌های آماده کپی و مسیر یادگیری راهنماشده.

**[شروع در ۱۵ دقیقه](#شروع-در-۱۵-دقیقه)** | **[سطح خود را پیدا کنید](#مطمئن-نیستید-از-کجا-شروع-کنید)** | **[کاتالوگ ویژگی‌ها را ببینید](CATALOG.md)**

---

## فهرست مطالب

- [مشکل](#مشکل)
- [چگونه Claude How To این را حل می‌کند](#چگونه-claude-how-to-این-را-حل-میکند)
- [چگونه کار می‌کند](#چگونه-کار-میکند)
- [مطمئن نیستید از کجا شروع کنید؟](#مطمئن-نیستید-از-کجا-شروع-کنید)
- [شروع در ۱۵ دقیقه](#شروع-در-۱۵-دقیقه)
- [با این چه می‌توانید بسازید؟](#با-این-چه-میتوانید-بسازید)
- [سؤالات متداول](#سؤالات-متداول)
- [مشارکت](#مشارکت)
- [مجوز](#مجوز)

---

## مشکل

شما Claude Code را نصب کرده‌اید. چند prompt هم امتحان کرده‌اید. بعد چه؟

- **مستندات رسمی ویژگی‌ها را معرفی می‌کند، اما نه اینکه چگونه آن‌ها را با هم ترکیب کنید.** می‌دانید slash commandها وجود دارند، اما نمی‌دانید چگونه آن‌ها را با hookها، memory و subagentها ترکیب کنید تا یک گردش کاری واقعی بسازید که ساعت‌ها وقت ذخیره کند.
- **مسیر یادگیری واضحی وجود ندارد.** باید اول MCP را یاد بگیرید یا hookها را؟ skillها را یا subagentها را؟ نتیجه این است که کمی از همه چیز یاد می‌گیرید اما هیچ‌کدام را واقعاً تسلط نمی‌یابید.
- **مثال‌ها بسیار پایه‌ای هستند.** یک slash command سطح "hello world" به شما کمک نمی‌کند یک pipeline بررسی کد production-ready بسازید که memory را ترکیب کند، به یک agent متخصص واگذار کند و به طور خودکار اسکن امنیتی انجام دهد.

شما عملاً فقط از ۱۰٪ قابلیت‌های Claude Code استفاده می‌کنید، و ۹۰٪ باقی‌مانده را حتی نمی‌دانید که از دست داده‌اید.

---

## چگونه Claude How To این را حل می‌کند

این یک reference manual دیگر نیست، بلکه یک **راهنمای ساختاریافته، تصویری و مبتنی بر مثال** است. به شما یاد می‌دهد چگونه از هر ویژگی Claude Code استفاده کنید، با templateهای سناریوهای واقعی که می‌توانید امروز در پروژه خود کپی کنید.

| | مستندات رسمی | این راهنما |
|--|---------------|------------|
| **فرم** | reference | tutorial تصویری با نمودارهای Mermaid |
| **عمق** | توضیح ویژگی | توضیح چگونگی کار در پس‌زمینه |
| **مثال‌ها** | قطعات کد پایه | templateهای production-ready آماده استفاده |
| **ساختار** | بر اساس ویژگی | مسیر یادگیری پیشرونده (beginner تا advanced) |
| **شروع** | کشف خودسرانه | مسیر راهنمایشده با برآورد زمان |
| **خودارزیابی** | ندارد | quizهای تعاملی برای یافتن شکاف‌ها و تولید مسیر شخصی‌سازی‌شده |

### آنچه دریافت می‌کنید:

- **۱۰ ماژول آموزشی**، پوشش همه ویژگی‌های اصلی Claude Code، از slash commandها تا تیم‌های agent سفارشی
- **پیکربندی‌های copy-paste-ready**، شامل slash commandها، templateهای `CLAUDE.md`، scriptهای hook، پیکربندی MCP، تعریف subagent و plugin bundle کامل
- **نمودارهای Mermaid** که مکانیزم داخلی هر ویژگی را نشان می‌دهند، تا نه فقط "چگونه" بلکه "چرا"
- **یک مسیر یادگیری راهنمایشده** که شما را در ۱۱ تا ۱۳ ساعت از beginner به advanced می‌رساند
- **قابلیت self-test built-in**، که می‌توانید `/self-assessment` یا `/lesson-quiz hooks` را مستقیماً در Claude Code اجرا کنید تا blind spotهای دانش خود را بیابید

**[شروع مسیر یادگیری ->](LEARNING-ROADMAP.md)**

---

## چگونه کار می‌کند

### ۱. ابتدا سطح خود را بیابید

[Self-Assessment Quiz](LEARNING-ROADMAP.md#find-your-level) را تکمیل کنید، یا `/self-assessment` را در Claude Code اجرا کنید. سیستم یک مسیر یادگیری شخصی‌سازی‌شده بر اساس آنچه قبلاً می‌دانید تولید می‌کند.

### ۲. طبق مسیر راهنماشده یاد بگیرید

۱۰ ماژول را به ترتیب دنبال کنید، هر ماژول روی ماژول قبلی بنا شده است. می‌توانید هنگام یادگیری templateها را مستقیماً در پروژه خود کپی کنید.

### ۳. چند ویژگی را به یک گردش کار ترکیب کنید

قدرت واقعی از ترکیب ویژگی‌ها می‌آید. یاد می‌گیرید چگونه slash commandها، memory، subagentها و hookها را به pipelineهای خودکار برای code review، deployment و تولید مستندات متصل کنید.

### ۴. درک خود را بسنجید

پس از هر ماژول `/lesson-quiz [topic]` را اجرا کنید. quiz دقیقاً آنچه را که از دست داده‌اید شناسایی می‌کند تا بتوانید سریعاً شکاف‌ها را پر کنید.

**[شروع در ۱۵ دقیقه](#شروع-در-۱۵-دقیقه)**

---

## مورد اعتماد توسعه‌دهندگان

- **GitHub stars**، از توسعه‌دهندگانی که هر روز از Claude Code استفاده می‌کنند
- **Forkها**، بسیاری از تیم‌ها این راهنما را به نسخه گردش کاری خود تبدیل کرده‌اند
- **به طور مستمر نگهداری می‌شود**، همگام با هر انتشار Claude Code (آخرین نسخه: v2.1.112، آوریل ۲۰۲۶)
- **جامعه‌محور**، مشارکت‌کنندگان پیکربندی‌ها و تجربیات خود در کار واقعی را به اشتراک می‌گذارند

[![Star History Chart](https://api.star-history.com/svg?repos=luongnv89/claude-howto&type=Date)](https://star-history.com/#luongnv89/claude-howto&Date)

---

## مطمئن نیستید از کجا شروع کنید؟

ابتدا خودارزیابی انجام دهید، یا مستقیماً بر اساس سطح خود شروع کنید:

| سطح | شما می‌توانید... | از اینجا شروع کنید | زمان |
|-------|-----------|------------|------|
| **Beginner** | Claude Code را راه‌اندازی کرده و مکالمه کنید | [Slash Commands](01-slash-commands/README.md) | حدود ۲.۵ ساعت |
| **Intermediate** | از `CLAUDE.md` و commandهای سفارشی استفاده کنید | [Skills](03-skills/README.md) | حدود ۳.۵ ساعت |
| **Advanced** | پیکربندی MCP serverها و hookها | [Advanced Features](09-advanced-features/README.md) | حدود ۵ ساعت |

**مسیر یادگیری کامل، ۱۰ ماژول:**

| ترتیب | ماژول | سطح | زمان |
|-------|--------|-------|------|
| 1 | [Slash Commands](01-slash-commands/README.md) | مبتدی | ۳۰ دقیقه |
| 2 | [Memory](02-memory/README.md) | مبتدی+ | ۴۵ دقیقه |
| 3 | [Checkpoints](08-checkpoints/README.md) | متوسط | ۴۵ دقیقه |
| 4 | [CLI Basics](10-cli/README.md) | مبتدی+ | ۳۰ دقیقه |
| 5 | [Skills](03-skills/README.md) | متوسط | ۱ ساعت |
| 6 | [Hooks](06-hooks/README.md) | متوسط | ۱ ساعت |
| 7 | [MCP](05-mcp/README.md) | متوسط+ | ۱ ساعت |
| 8 | [Subagents](04-subagents/README.md) | متوسط+ | ۱.۵ ساعت |
| 9 | [Advanced Features](09-advanced-features/README.md) | پیشرفته | ۲ تا ۳ ساعت |
| 10 | [Plugins](07-plugins/README.md) | پیشرفته | ۲ ساعت |

**[نقشه راه یادگیری کامل ->](LEARNING-ROADMAP.md)**

---

## شروع در ۱۵ دقیقه

```bash
# 1. clone کردن این راهنما
git clone https://github.com/luongnv89/claude-howto.git
cd claude-howto

# 2. کپی کردن اولین slash command خود
mkdir -p /path/to/your-project/.claude/commands
cp 01-slash-commands/optimize.md /path/to/your-project/.claude/commands/

# 3. امتحان کنید: در Claude Code تایپ کنید
# /optimize

# 4. می‌خواهید بیشتر پیش بروید؟ project memory را تنظیم کنید:
cp 02-memory/project-CLAUDE.md /path/to/your-project/CLAUDE.md

# 5. نصب یک skill:
cp -r 03-skills/code-review-specialist ~/.claude/skills/
```

اگر می‌خواهید یک پیکربندی پایه کامل‌تر انجام دهید، این **طرح ۱ ساعته کلیدی** است:

```bash
# Slash commandها (۱۵ دقیقه)
cp 01-slash-commands/*.md .claude/commands/

# project memory (۱۵ دقیقه)
cp 02-memory/project-CLAUDE.md ./CLAUDE.md

# نصب یک skill (۱۵ دقیقه)
cp -r 03-skills/code-review-specialist ~/.claude/skills/

# هدف آخر هفته: ادامه افزودن hookها، subagentها، MCP و pluginها
# مرحله به مرحله طبق مسیر یادگیری
```

**[مرجع نصب کامل را ببینید](#شروع-در-۱۵-دقیقه)**

---

## با این چه می‌توانید بسازید؟

| مورد استفاده | ویژگی‌هایی که ترکیب می‌کنید |
|----------|------------------------|
| **بررسی کد خودکار** | Slash Commands + Subagents + Memory + MCP |
| **onboarding تیم** | Memory + Slash Commands + Plugins |
| **automation CI/CD** | CLI Reference + Hooks + Background Tasks |
| **تولید مستندات** | Skills + Subagents + Plugins |
| **audit امنیتی** | Subagents + Skills + Hooks (حالت read-only) |
| **pipeline DevOps** | Plugins + MCP + Hooks + Background Tasks |
| **refactor پیچیده** | Checkpoints + Planning Mode + Hooks |

---

## سؤالات متداول

**آیا این رایگان است؟**
بله. مجوز MIT، برای همیشه رایگان. می‌توانید آن را در پروژه‌های شخصی، کاری یا تیمی استفاده کنید، تنها الزام این است که اعلان مجوز را حفظ کنید.

**آیا نگهداری می‌شود؟**
بله، و به طور مستمر. این راهنما با هر انتشار Claude Code همگام می‌شود. نسخه فعلی v2.1.112 (آوریل ۲۰۲۶) است و با Claude Code 2.1+ سازگار است.

**چگونه با مستندات رسمی متفاوت است؟**
مستندات رسمی یک reference manual ویژگی است؛ این راهنما یک tutorial با نمودارها، templateهای production-ready و مسیر یادگیری پیشرونده است. این دو مکمل یکدیگر هستند؛ پیشنهاد می‌شود ابتدا با این راهنما یاد بگیرید، سپس برای جزئیات خاص به مستندات رسمی مراجعه کنید.

**完整学完需要多久？**
完整路径大约需要 11 到 13 小时。但你在 15 分钟内就能获得直接收益，只要复制一个 slash command 模板并试用即可。

**我可以搭配 Claude Sonnet / Haiku / Opus 使用吗？**
可以。所有模板都适用于 Claude Fable 5、Claude Opus 5、Claude Sonnet 5.5、Claude Sonnet 5、Claude Sonnet 4.6、Claude Opus 4.8、Claude Haiku 4.5。

**我可以参与贡献吗？**
当然可以。请查看 [CONTRIBUTING.md](CONTRIBUTING.md) 了解贡献规范。我们欢迎新的示例、bug 修复、文档改进以及社区模板。

**我可以离线阅读吗？**
可以。运行 `uv run scripts/build_epub.py`，即可生成包含全部内容和渲染后 Mermaid 图表的 EPUB 电子书。

---

## 今天就开始掌握 Claude Code

你已经安装好了 Claude Code。你和 10 倍生产力之间，差的只是知道该怎么正确使用它。这份指南会提供结构化路径、可视化解释和可直接复制的模板，帮助你真正掌握它。

MIT 许可证，永久免费。克隆它、fork 它、改造成适合你自己的版本。

**[开始学习路线 ->](LEARNING-ROADMAP.md)** | **[浏览功能目录](CATALOG.md)** | **[15 分钟快速上手](#15-分钟快速上手)**

---

<details>
<summary>快速导航：全部功能</summary>

| 功能 | 说明 | 文件夹 |
|---------|-------------|--------|
| **功能目录** | 包含安装命令的完整参考 | [CATALOG.md](CATALOG.md) |
| **Slash Commands** | 用户手动触发的快捷命令 | [01-slash-commands/README.md](01-slash-commands/README.md) |
| **Memory** | 持久上下文 | [02-memory/README.md](02-memory/README.md) |
| **Skills** | 可复用能力 | [03-skills/README.md](03-skills/README.md) |
| **Subagents** | 专门化 AI 助手 | [04-subagents/README.md](04-subagents/README.md) |
| **MCP Protocol** | 访问外部工具 | [05-mcp/README.md](05-mcp/README.md) |
| **Hooks** | 事件驱动自动化 | [06-hooks/README.md](06-hooks/README.md) |
| **Plugins** | 打包后的功能集合 | [07-plugins/README.md](07-plugins/README.md) |
| **Checkpoints** | 会话快照与回退 | [08-checkpoints/README.md](08-checkpoints/README.md) |
| **Advanced Features** | 规划、思考、后台任务 | [09-advanced-features/README.md](09-advanced-features/README.md) |
| **CLI Reference** | 命令、参数与选项 | [10-cli/README.md](10-cli/README.md) |
| **博客文章** | 真实使用案例 | [Blog Posts](https://medium.com/@luongnv89) |

</details>

<details>
<summary>功能对比</summary>

| 功能 | 调用方式 | 持久性 | 最适合 |
|---------|-----------|------------|----------|
| **Slash Commands** | 手动（`/cmd`） | 仅当前会话 | 快速快捷操作 |
| **Memory** | 自动加载 | 跨会话 | 长期记忆与学习 |
| **Skills** | 自动触发 | 文件系统级 | 自动化工作流 |
| **Subagents** | 自动委派 | 隔离上下文 | 任务拆分 |
| **MCP Protocol** | 自动查询 | 实时 | 获取实时数据 |
| **Hooks** | 事件触发 | 已配置 | 自动化与校验 |
| **Plugins** | 一条命令 | 全功能打包 | 完整解决方案 |
| **Checkpoints** | 手动/自动 | 会话级 | 安全试验 |
| **Planning Mode** | 手动/自动 | 规划阶段 | 复杂实现 |
| **Background Tasks** | 手动 | 任务持续期间 | 长时间运行的操作 |
| **CLI Reference** | 终端命令 | 会话/脚本级 | 自动化与脚本开发 |

</details>

<details>
<summary>安装速查表</summary>

```bash
# Slash Commands
cp 01-slash-commands/*.md .claude/commands/

# Memory
cp 02-memory/project-CLAUDE.md ./CLAUDE.md

# Skills
cp -r 03-skills/code-review-specialist ~/.claude/skills/

# Subagents
cp 04-subagents/*.md .claude/agents/

# MCP
claude mcp add --transport http github https://api.githubcopilot.com/mcp/ --header "Authorization: Bearer YOUR_GITHUB_PAT"

# Hooks
mkdir -p ~/.claude/hooks
cp 06-hooks/*.sh ~/.claude/hooks/
chmod +x ~/.claude/hooks/*.sh

# Plugins（在仓库根目录加载本地插件）
claude --plugin-dir ./07-plugins/pr-review

# Checkpoints（默认自动开启，可在设置中配置）
# 参见 08-checkpoints/README.md

# Advanced Features（在设置中配置）
# 参见 09-advanced-features/config-examples.json

# CLI Reference（无需安装）
# 使用示例见 10-cli/README.md
```

</details>

<details>
<summary>01. Slash Commands</summary>

**位置**: [01-slash-commands/README.md](01-slash-commands/README.md)

**是什么**: 以 Markdown 文件形式存储、由用户手动触发的快捷命令

**示例**:
- `optimize.md` - 代码优化分析
- `pr.md` - Pull Request 准备
- `generate-api-docs.md` - API 文档生成器

**安装**:
```bash
cp 01-slash-commands/*.md /path/to/project/.claude/commands/
```

**使用方法**:
```
/optimize
/pr
/generate-api-docs
```

**了解更多**: [Discovering Claude Code Slash Commands](https://medium.com/@luongnv89/discovering-claude-code-slash-commands-cdc17f0dfb29)

</details>

<details>
<summary>02. Memory</summary>

**位置**: [02-memory/README.md](02-memory/README.md)

**是什么**: 跨会话持久化的上下文

**示例**:
- `project-CLAUDE.md` - 团队共享的项目规范
- `directory-api-CLAUDE.md` - 目录级规则
- `personal-CLAUDE.md` - 个人偏好

**安装**:
```bash
# 项目记忆
cp 02-memory/project-CLAUDE.md /path/to/project/CLAUDE.md

# 目录记忆
cp 02-memory/directory-api-CLAUDE.md /path/to/project/src/api/CLAUDE.md

# 个人记忆
cp 02-memory/personal-CLAUDE.md ~/.claude/CLAUDE.md
```

**使用方法**: Claude 会自动加载

</details>

<details>
<summary>03. Skills</summary>

**位置**: [03-skills/README.md](03-skills/README.md)

**是什么**: 可复用、会在合适时自动触发的能力包，包含说明和脚本

**示例**:
- `code-review/` - 带脚本的完整代码审查能力
- `brand-voice/` - 品牌语气一致性检查
- `doc-generator/` - API 文档生成器

**安装**:
```bash
# 个人 skills
cp -r 03-skills/code-review-specialist ~/.claude/skills/

# 项目 skills
cp -r 03-skills/code-review-specialist /path/to/project/.claude/skills/
```

**使用方法**: 在相关场景下自动触发

</details>

<details>
<summary>04. Subagents</summary>

**位置**: [04-subagents/README.md](04-subagents/README.md)

**是什么**: 拥有隔离上下文和自定义提示词的专门化 AI 助手

**示例**:
- `code-reviewer.md` - 全面代码质量分析
- `test-engineer.md` - 测试策略与覆盖率
- `documentation-writer.md` - 技术文档编写
- `secure-reviewer.md` - 面向安全的审查（只读）
- `implementation-agent.md` - 完整功能实现

**安装**:
```bash
cp 04-subagents/*.md /path/to/project/.claude/agents/
```

**使用方法**: 由主 agent 自动委派

</details>

<details>
<summary>05. MCP Protocol</summary>

**位置**: [05-mcp/README.md](05-mcp/README.md)

**是什么**: 用于访问外部工具和 API 的 Model Context Protocol

**示例**:
- `github-mcp.json` - GitHub 集成
- `database-mcp.json` - 数据库查询
- `filesystem-mcp.json` - 文件操作
- `multi-mcp.json` - 多个 MCP servers 配置

**安装**:
```bash
# 设置环境变量
export DATABASE_URL="postgresql://..."

# 通过 CLI 添加 MCP server
claude mcp add --transport http github https://api.githubcopilot.com/mcp/ --header "Authorization: Bearer YOUR_GITHUB_PAT"

# 或手动添加到项目 .mcp.json（参见 [05-mcp/README.md](05-mcp/README.md) 中的示例）
```

**使用方法**: 配置完成后，Claude 会自动获得 MCP 工具能力

</details>

<details>
<summary>06. Hooks</summary>

**位置**: [06-hooks/README.md](06-hooks/README.md)

**是什么**: 基于事件触发的 shell 命令，会在 Claude Code 事件发生时自动执行

**示例**:
- `format-code.sh` - 写入后自动格式化代码
- `pre-commit.sh` - 提交前运行测试
- `security-scan.sh` - 扫描安全问题
- `log-bash.sh` - 记录所有 bash 命令
- `validate-prompt.sh` - 校验用户提示词
- `notify-team.sh` - 事件发生时发送通知

**安装**:
```bash
mkdir -p ~/.claude/hooks
cp 06-hooks/*.sh ~/.claude/hooks/
chmod +x ~/.claude/hooks/*.sh
```

在 `~/.claude/settings.json` 中配置 hooks：
```json
{
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "Write",
        "hooks": [
          { "type": "command", "command": "~/.claude/hooks/format-code.sh" },
          { "type": "command", "command": "~/.claude/hooks/security-scan.sh" }
        ]
      }
    ]
  }
}
```

**使用方法**: hooks 会在事件发生时自动执行

**Hook 类型**（5 种）：`command`、`http`、`prompt`、`mcp_tool`、`agent` — 决定 hook 如何运行。

**Hook 事件**（33 个，分 4 类）— 决定 hook 何时运行:
- **工具 Hook**: `PreToolUse`, `PostToolUse`, `PostToolUseFailure`, `PostToolBatch`, `PermissionRequest`, `PermissionDenied`
- **会话 Hook**: `SessionStart`, `Setup`, `SessionEnd`, `Stop`, `StopFailure`, `SubagentStart`, `SubagentStop`
- **任务 Hook**: `UserPromptSubmit`, `UserPromptExpansion`, `MessageDisplay`, `TaskCompleted`, `TaskCreated`, `TeammateIdle`（`TaskCompleted` 和 `TaskCreated` 仅在启用 todo 工具时触发 —— 默认仅在 Claude 3.x、Opus 4 至 4.7、Sonnet 4 至 4.6、Haiku 4.5 上可用；`CLAUDE_CODE_ENABLE_TODO_TOOLS=1` 可恢复）
- **生命周期 Hook**: `ConfigChange`, `CwdChanged`, `DirectoryAdded`, `FileChanged`, `PreCompact`, `PostCompact`, `PreModelSwitch`, `PostModelSwitch`, `WorktreeCreate`, `WorktreeRemove`, `Notification`, `InstructionsLoaded`, `Elicitation`, `ElicitationResult`

</details>

<details>
<summary>07. Plugins</summary>

**位置**: [07-plugins/README.md](07-plugins/README.md)

**是什么**: 把 commands、agents、MCP 和 hooks 打包在一起的功能集合

**示例**:
- `pr-review/` - 完整的 PR 审查工作流
- `devops-automation/` - 部署与监控
- `documentation/` - 文档生成

**安装**:
```bash
# 在仓库根目录运行（本仓库没有 marketplace，因此 /plugin install 不适用）
claude --plugin-dir ./07-plugins/pr-review
claude --plugin-dir ./07-plugins/devops-automation
claude --plugin-dir ./07-plugins/documentation
```

**使用方法**: 使用其中打包好的 slash commands 和功能

</details>

<details>
<summary>08. Checkpoints and Rewind</summary>

**位置**: [08-checkpoints/README.md](08-checkpoints/README.md)

**是什么**: 保存对话状态，并回退到之前的时间点，以探索不同方案

**核心概念**:
- **Checkpoint**: 对话状态快照
- **Rewind**: 回到之前的 checkpoint
- **Branch Point**: 从同一个 checkpoint 分叉出多种方案

**使用方法**:
```
# 每次用户提示后都会自动创建 checkpoint
# 如需回退，按两次 Esc，或者使用：
/rewind

# 然后从以下六个选项中选择：
# 1. 恢复代码和对话
# 2. 恢复对话
# 3. 恢复代码
# 4. 从这里开始总结
# 5. 总结到这里
# 6. 算了
```

**使用场景**:
- 尝试不同实现方式
- 从错误中恢复
- 安全试验
- 比较不同备选方案
- 对不同设计做 A/B 测试

</details>

<details>
<summary>09. Advanced Features</summary>

**位置**: [09-advanced-features/README.md](09-advanced-features/README.md)

**是什么**: 面向复杂工作流和自动化的高级能力

**包括**:
- **Planning Mode**：编码前先创建详细实现计划
- **Extended Thinking**：用于复杂问题的深度推理（用 `Alt+T` / `Option+T` 切换）
- **Background Tasks**：运行长时间操作且不阻塞当前会话
- **Permission Modes**：`default`、`acceptEdits`、`plan`、`dontAsk`、`bypassPermissions`
- **Headless Mode**：在 CI/CD 中运行 Claude Code：`claude -p "Run tests and generate report"`
- **Session Management**：`/resume`、`/rename`、`/fork`、`claude -c`、`claude -r`
- **Configuration**：在 `~/.claude/settings.json` 中自定义行为

完整配置请参见 [config-examples.json](09-advanced-features/config-examples.json)。

</details>

<details>
<summary>10. CLI Reference</summary>

**位置**: [10-cli/README.md](10-cli/README.md)

**是什么**: Claude Code 的完整命令行接口参考

**快速示例**:
```bash
# 交互模式
claude "explain this project"

# 输出模式（非交互）
claude -p "review this code"

# 处理文件内容
cat error.log | claude -p "explain this error"

# 为脚本输出 JSON
claude -p --output-format json "list functions"

# 恢复会话
claude -r "feature-auth" "continue implementation"
```

**使用场景**: CI/CD 流水线集成、脚本自动化、批处理、多会话工作流、自定义 agent 配置

</details>

<details>
<summary>示例工作流</summary>

### 完整代码审查工作流

```markdown
# 使用：Slash Commands + Subagents + Memory + MCP

用户：/review-pr

Claude：
1. 加载项目 memory（编码规范）
2. 通过 GitHub MCP 获取 PR
3. 委派给 code-reviewer subagent
4. 委派给 test-engineer subagent
5. 汇总发现
6. 提供完整审查结果
```

### 自动化文档生成

```markdown
# 使用：Skills + Subagents + Memory

用户："为 auth 模块生成 API 文档"

Claude：
1. 加载项目 memory（文档规范）
2. 识别出文档生成请求
3. 自动触发 doc-generator skill
4. 委派给 api-documenter subagent
5. 生成带示例的完整文档
```

### DevOps 部署

```markdown
# 使用：Plugins + MCP + Hooks

用户：/deploy production

Claude：
1. 运行部署前 hook（校验环境）
2. 委派给 deployment-specialist subagent
3. 通过 Kubernetes MCP 执行部署
4. 监控进度
5. 运行部署后 hook（健康检查）
6. 报告状态
```

</details>

<details>
<summary>目录结构</summary>

```
├── 01-slash-commands/
│   ├── optimize.md
│   ├── pr.md
│   ├── generate-api-docs.md
│   └── README.md
├── 02-memory/
│   ├── project-CLAUDE.md
│   ├── directory-api-CLAUDE.md
│   ├── personal-CLAUDE.md
│   └── README.md
├── 03-skills/
│   ├── code-review/
│   │   ├── SKILL.md
│   │   ├── scripts/
│   │   └── templates/
│   ├── brand-voice/
│   │   ├── SKILL.md
│   │   └── templates/
│   ├── doc-generator/
│   │   ├── SKILL.md
│   │   └── generate-docs.py
│   └── README.md
├── 04-subagents/
│   ├── code-reviewer.md
│   ├── test-engineer.md
│   ├── documentation-writer.md
│   ├── secure-reviewer.md
│   ├── implementation-agent.md
│   └── README.md
├── 05-mcp/
│   ├── github-mcp.json
│   ├── database-mcp.json
│   ├── filesystem-mcp.json
│   ├── multi-mcp.json
│   └── README.md
├── 06-hooks/
│   ├── format-code.sh
│   ├── pre-commit.sh
│   ├── security-scan.sh
│   ├── log-bash.sh
│   ├── validate-prompt.sh
│   ├── notify-team.sh
│   └── README.md
├── 07-plugins/
│   ├── pr-review/
│   ├── devops-automation/
│   ├── documentation/
│   └── README.md
├── 08-checkpoints/
│   ├── checkpoint-examples.md
│   └── README.md
├── 09-advanced-features/
│   ├── config-examples.json
│   ├── planning-mode-examples.md
│   └── README.md
├── 10-cli/
│   └── README.md
└── README.md（本文件）
```

</details>

<details>
<summary>最佳实践</summary>

### 应该做的
- 从简单的 slash commands 开始
- 逐步增加功能
- 用 memory 保存团队规范
- 先在本地测试配置
- 为自定义实现写文档
- 对项目配置做版本控制
- 和团队共享 plugins

### 不应该做的
- 不要创建重复功能
- 不要硬编码凭据
- 不要跳过文档
- 不要把简单任务过度复杂化
- 不要忽视安全最佳实践
- 不要提交敏感数据

</details>

<details>
<summary>故障排查</summary>

### 功能没有加载
1. 检查文件位置和命名
2. 验证 YAML frontmatter 语法
3. 检查文件权限
4. 查看 Claude Code 版本兼容性

### MCP 连接失败
1. 检查环境变量
2. 检查 MCP server 是否正确安装
3. 测试凭据
4. 检查网络连通性

### Subagent 没有发生委派
1. 检查工具权限
2. 确认 agent 描述是否清晰
3. 查看任务复杂度
4. 单独测试 agent

</details>

<details>
<summary>测试</summary>

本项目包含完整的自动化测试：

- **单元测试**：基于 pytest 的 Python 测试（Python 3.10、3.11、3.12）
- **代码质量**：使用 Ruff 做 lint 和格式化检查
- **安全**：使用 Bandit 做漏洞扫描
- **类型检查**：使用 mypy 做静态类型分析
- **构建验证**：测试 EPUB 生成功能
- **覆盖率跟踪**：集成 Codecov

```bash
# 安装开发依赖
uv pip install -r requirements-dev.txt

# 运行全部单元测试
pytest scripts/tests/ -v

# 运行带覆盖率报告的测试
pytest scripts/tests/ -v --cov=scripts --cov-report=html

# 运行代码质量检查
ruff check scripts/
ruff format --check scripts/

# 运行安全扫描
bandit -c pyproject.toml -r scripts/ --exclude scripts/tests/

# 运行类型检查
mypy scripts/ --ignore-missing-imports
```

每次 push 到 `main` / `develop`，以及每次向 `main` 提交 PR 时，测试都会自动运行。详情见 [TESTING.md](.github/TESTING.md)。

</details>

<details>
<summary>EPUB 生成</summary>

想离线阅读这份指南？你可以生成 EPUB 电子书：

```bash
uv run scripts/build_epub.py
```

这会生成包含全部内容与 Mermaid 渲染图表的 `claude-howto-guide.epub`。

更多选项见 [scripts/README.md](scripts/README.md)。

</details>

<details>
<summary>参与贡献</summary>

发现问题，或者想贡献一个示例？非常欢迎你的帮助。

**请先阅读 [CONTRIBUTING.md](CONTRIBUTING.md)，了解以下详细规范：**
- 可贡献的内容类型（示例、文档、功能、bug、反馈）
- 如何搭建开发环境
- 目录结构以及如何添加内容
- 编写规范与最佳实践
- Commit 和 PR 流程

**我们的社区标准：**
- [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) - 我们如何彼此相处
- [SECURITY.md](SECURITY.md) - 安全政策与漏洞报告方式

### 报告安全问题

如果你发现了安全漏洞，请负责任地报告：

1. **使用 GitHub 私密漏洞报告功能**：https://github.com/luongnv89/claude-howto/security/advisories
2. **或者阅读** [.github/SECURITY_REPORTING.md](.github/SECURITY_REPORTING.md) 获取详细说明
3. **不要**公开提交安全漏洞 issue

快速开始：
1. Fork 并克隆仓库
2. 创建一个清晰描述用途的分支（`add/feature-name`、`fix/bug`、`docs/improvement`）
3. 按规范进行修改
4. 提交一个说明清楚的 Pull Request

**需要帮助？** 打开一个 issue 或 discussion，我们会引导你完成整个过程。

</details>

<details>
<summary>更多资源</summary>

- [Claude Code Documentation](https://code.claude.com/docs/en/overview)
- [MCP Protocol Specification](https://modelcontextprotocol.io)
- [Skills Repository](https://github.com/luongnv89/skills) - 可直接使用的 skills 集合
- [Anthropic Cookbook](https://github.com/anthropics/anthropic-cookbook)
- [Boris Cherny's Claude Code Workflow](https://x.com/bcherny/status/2007179832300581177) - Claude Code 的创造者分享了他系统化的工作流：并行 agents、共享 `CLAUDE.md`、Plan mode、slash commands、subagents，以及用于长时间自主会话的验证 hooks。

</details>

---

## 参与贡献

欢迎贡献内容。如何开始请查看我们的[贡献指南](CONTRIBUTING.md)。

## 贡献者

感谢所有为本项目做出贡献的人。

| 贡献者 | PRs |
|-------------|-----|
| [wjhrdy](https://github.com/wjhrdy) | [#1 - add a tool to create an epub](https://github.com/luongnv89/claude-howto/pull/1) |
| [VikalpP](https://github.com/VikalpP) | [#7 - fix(docs): Use tilde fences for nested code blocks in concepts guide](https://github.com/luongnv89/claude-howto/pull/7) |

---

## 许可证

MIT 许可证，详见 [LICENSE](LICENSE)。你可以自由使用、修改和分发，唯一要求是保留许可证声明。

---

**最后更新**：2026 年 10 月 18 日
**Claude Code 版本**：2.1.302
**来源**：
- https://code.claude.com/docs/en/tools-reference#task-tool-availability
- https://code.claude.com/docs/en/hooks
- https://code.claude.com/docs/en/model-config
- https://code.claude.com/docs/en/mcp
- https://code.claude.com/docs/en/plugins/install
- https://code.claude.com/docs/en/checkpointing
**兼容模型**：Claude Fable 5、Claude Opus 5、Claude Sonnet 5、Claude Sonnet 4.6、Claude Opus 4.8、Claude Haiku 4.5
