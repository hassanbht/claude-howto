import os

fa_dir = r"D:\Project\claude-howto\fa"

content = """<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../../resources/logos/claude-howto-logo-dark.svg">
  <img alt="Claude How To" src="../../resources/logos/claude-howto-logo.svg">
</picture>

# 草稿博客模板

这些模板可以帮助你为 `blog-draft` 技能生成结构清晰、与品牌一致的博客文章。

---

## 草稿模板

### 博客文章

```markdown
# 文章标题

## 引言

- 吸引读者注意
- 说明文章价值
- 概述将要讲解的内容

## 主要内容

### 章节 1

### 章节 2

### 章节 3

## 结论

## 附录（可选）

```

---

## 文章大纲模板

```markdown
# 文章大纲

## 标题

## 摘要

## 1. 引言

### 1.1 背景

### 1.2 目标

## 2. 主要内容

### 2.1 第一部分

### 2.2 第二部分

## 3. 结论

## 关键词

## 推荐标签
```

---

## 产品更新文章模板

```markdown
# 产品更新：[产品名称]

## 摘要

简述本次更新的核心内容。

## 更新内容

- 更新 1
- 更新 2
- 更新 3

## 如何开始

## 常见问题

## 路线图
```

---

## 开发者教程模板

```markdown
# 教程：[主题]

## 学习目标

在本教程结束时，您将能够：

## 环境要求

## 第 1 步：[操作名称]

## 第 2 步：[操作名称]

## 注意事项

## 常见问题

## 延伸阅读
```

---

## 分析文章模板

```markdown
# [主题] 分析

## 摘要

## 背景

## 方法

## 结果

## 讨论

## 建议

## 结论
```

---

## 品牌语气指南模板

```markdown
# 品牌语气指南

## 主要语气

## 风格关键词

## 禁用词/短语

## 示例

### 好的示例

### 不好的示例
```

---

## 版权声明

这些模板适用于 `blog-draft` skill。根据特定需求调整。
"""
with open(os.path.join(fa_dir, "03-skills", "blog-draft", "templates", "outline-template.md"), "w", encoding="utf-8") as f:
    f.write(content)

print("03-skills/blog-draft/templates/outline-template.md written!")