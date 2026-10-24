import os

fa_dir = r"D:\Project\claude-howto\fa"

content = """<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../../resources/logos/claude-howto-logo-dark.svg">
  <img alt="Claude How To" src="../../resources/logos/claude-howto-logo.svg">
</picture>

# 语气示例

本文件为 `brand-voice` skill 提供实际语言示例，展示不同语气在写作中的体现。

---

## 语气对照表

| 语气 | 英文 | 中文 |
|------|------|------|
| 直接 | Direct | 直白 |
| 友好 | Friendly | 友好 |
| 专业 | Professional | 专业 |
| 简洁 | Concise | 简洁 |
| 幽默 | Humorous | 幽默 |

---

## 写作示例

### 引言

#### 直接

> 本文档介绍了如何使用 API 客户端。请按照下面的步骤进行配置。

#### 友好

> 欢迎使用 API 客户端！下面我们会一步步教你完成配置。

#### 专业

> 本节介绍 API 客户端的配置方法与最佳实践。

#### 幽默

> 别担心，这并不是一份“语气”文档——而是关于如何与 API 客户端对话的指南。

---

### 说明

#### 直接

> 配置文件必须包含 `server_url` 字段。

#### 友好

> 别忘了在配置文件里填写 `server_url`。

#### 专业

> `server_url` 字段是必填项，必须为有效的 URL。

#### 幽默

> `server_url` 是最重要的字段——不要因为它被“忘记”而尴尬。

---

### 错误处理

#### 直接

> 如果请求失败，返回 400 错误。

#### 友好

> 请求失败时我们会给你一个 400 错误。不要紧张。

#### 专业

> 请求失败时应返回 400 错误码，错误响应包含字段级别的错误详情。

#### 幽默

> 如果错误发生，你可以试着笑一笑——然后检查 400 错误。

---

## 语气对比

### 普通句子

> 请在开始前确保配置文件齐全。

### 更友好

> 好消息是：开始前只需要确保配置文件齐全。

### 更专业

> 在开始之前，请验证配置文件是否完整且正确。

### 更幽默

> 别担心，我们先把“配置文件齐全”这件事搞定。

---

## 使用建议

- 选择一种主要语气，避免混用
- 根据受众调整
- 保持一致性
- 示例用作参考，而非模板
"""
with open(os.path.join(fa_dir, "03-skills", "brand-voice", "tone-examples.md"), "w", encoding="utf-8") as f:
    f.write(content)

print("03-skills/brand-voice/tone-examples.md written!")