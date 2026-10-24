import os

fa_dir = r"D:\Project\claude-howto\fa"

content = """<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../../resources/logos/claude-howto-logo-dark.svg">
  <img alt="Claude How To" src="../../resources/logos/claude-howto-logo.svg">
</picture>

# 重构目录

这是 Martin Fowler《Refactoring》（第 2 版）中的一份精选重构目录。每个重构都包含动机、操作步骤和示例。

> “重构由它的操作步骤来定义，也就是你执行这个变化时遵循的精确过程。” — Martin Fowler

---

## 如何使用这个目录

1. **识别异味**：先用代码异味目录定位问题
2. **找到对应重构**：在这里查找匹配的手法
3. **按步骤执行**：一步一步来
4. **每步都测试**：确保行为不变

**黄金法则：** 如果某一步超过 10 分钟，就把它拆得更小。

---

## 最常见的重构

### Extract Method

**何时使用**：长函数、重复代码、需要为概念命名

**动机**：把一段代码抽成一个名字能说明意图的方法。

**步骤：**

1. 创建一个新方法，名字应描述“做什么”而不是“怎么做”
2. 把代码片段复制到新方法里
3. 检查片段里用了哪些局部变量
4. 把局部变量作为参数传入，或在方法内声明
5. 正确处理返回值
6. 用新方法调用替换原始片段
7. 测试

**前：**

```javascript
function printOwing(invoice) {
  let outstanding = 0;

  console.log("***********************");
  console.log("**** Customer Owes ****");
  console.log("***********************");

  // Calculate outstanding
  for (const order of invoice.orders) {
    outstanding += order.amount;
  }

  // Print details
  console.log(`name: ${invoice.customer}`);
  console.log(`amount: ${outstanding}`);
}
```

**后：**

```javascript
function printOwing(invoice) {
  printBanner();
  const outstanding = calculateOutstanding(invoice);
  printDetails(invoice, outstanding);
}

function printBanner() {
  console.log("***********************");
  console.log("**** Customer Owes ****");
  console.log("***********************");
}

function calculateOutstanding(invoice) {
  return invoice.orders.reduce((sum, order) => sum + order.amount, 0);
}

function printDetails(invoice, outstanding) {
  console.log(`name: ${invoice.customer}`);
  console.log(`amount: ${outstanding}`);
}
```
"""

with open(os.path.join(fa_dir, "03-skills", "refactor", "references", "refactoring-catalog.md"), "w", encoding="utf-8") as f:
    f.write(content)

print("refactoring-catalog.md part 1 written!")