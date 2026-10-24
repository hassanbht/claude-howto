<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../../resources/logos/claude-howto-logo-dark.svg">
  <img alt="Claude How To" src="../../resources/logos/claude-howto-logo.svg">
</picture>

# 生成 CLAUDE.md Skill

这个 skill 用于根据项目文档和内容，生成或补充项目级 `CLAUDE.md` 文件。`CLAUDE.md` 是一种持久化的项目记忆，Claude 会在会话中自动加载。

## 用途

- 从 README、docs/ 目录和其他文档，生成 `CLAUDE.md`
- 补充现有 `CLAUDE.md`
- 更新项目概览、开发规范、团队信息
- 保持 `CLAUDE.md` 与项目同步

## 触发场景

当遇到任何以下情况时：

- 用户请求“生成/更新 CLAUDE.md”
- 需要项目级记忆时
- 想根据文档自动补充 `CLAUDE.md`
- 项目文档变更后，需要更新 CLAUDE.md
- 需提供项目上下文时

---

## 工作流程

```text
1. 扫描项目文档
2. 读取关键文件
3. 提取结构化信息
4. 生成并审核 CLAUDE.md 内容
5. 保存
```

---

## 输入

读取以下文件：

- `README.md`
- `docs/`（所有文档）
- `CONTRIBUTING.md`
- `CHANGELOG.md`
- 其他项目级描述文件

---

## 输出格式

```markdown
# 项目配置

## 项目概览

## 技术栈

## 开发规范

## 命名规范

## 流程规范

## 测试

## 部署

## 联系人

## 已知问题
```

---

## 最佳实践

### 1. 按需更新

- 只更新与项目级记忆相关的部分
- 保持 `CLAUDE.md` 简洁
- 避免重复

### 2. 与文档分离

- `CLAUDE.md` 是高度概要的
- 具体细节保留在 `docs/`

### 3. 保持可读性

- 使用 Markdown
- 采用表格
- 短句

### 4. 版本控制

- 提交变更
- 带上 `CHANGELOG.md`
