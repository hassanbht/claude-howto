import os

fa_dir = r"D:\Project\claude-howto\fa"

content = """<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../../resources/logos/claude-howto-logo-dark.svg">
  <img alt="Claude How To" src="../../resources/logos/claude-howto-logo.svg">
</picture>

# 代码异味目录

这是基于 Martin Fowler《Refactoring》（第 2 版）的代码异味参考目录。代码异味是更深层问题的表面症状，它们说明代码设计可能出了问题。

> “代码异味通常是系统中更深层问题的表面信号。” — Martin Fowler

---

## 过度膨胀类异味

表示对象或函数已经大到不再好用。

### 长函数

**迹象：**

- 函数超过 30-50 行
- 需要滚动才能看完整个函数
- 嵌套层级很多
- 需要注释来解释局部逻辑

**为什么不好：**

- 难理解
- 难单独测试
- 改动容易波及其他逻辑
- 重复逻辑容易藏在里面

**可用重构：**

- Extract Method
- Replace Temp with Query
- Introduce Parameter Object
- Replace Method with Method Object
- Decompose Conditional

**示例（重构前）：**

```javascript
function processOrder(order) {
  // Validate order (20 lines)
  if (!order.items) throw new Error('No items');
  if (order.items.length === 0) throw new Error('Empty order');
  // ... more validation

  // Calculate totals (30 lines)
  let subtotal = 0;
  for (const item of order.items) {
    subtotal += item.price * item.quantity;
  }
  // ... tax, shipping, discounts

  // Send notifications (20 lines)
  // ... email logic
}
```

**示例（重构后）：**

```javascript
function processOrder(order) {
  validateOrder(order);
  const totals = calculateOrderTotals(order);
  sendOrderNotifications(order, totals);
  return { order, totals };
}
```

---

### 大类

**迹象：**

- 实例变量很多（>7-10）
- 方法很多（>15-20）
- 类名含糊（Manager、Handler、Processor）
- 方法没有用到全部字段

**为什么不好：**

- 违反单一职责原则
- 难测试
- 改动会波及无关功能
- 难以复用局部能力

**可用重构：**

- Extract Class
- Extract Subclass
- Extract Interface

**检测参考：**

```text
代码行数 > 300
方法数量 > 15
字段数量 > 10
```

---

### 基础类型沉迷

**迹象：**

- 用基础类型表达领域概念（用 string 表示邮箱、用 int 表示金额）
- 使用基础类型数组，而不是对象
- 用字符串常量表示类型码
- 大量 magic number / magic string

**为什么不好：**

- 类型层面没有验证
- 逻辑散落在整个代码库里
- 容易传错值
- 缺少领域对象

**可用重构：**

- Replace Primitive with Object
- Replace Type Code with Class
- Replace Type Code with Subclasses
- Replace Type Code with State/Strategy

**示例（重构前）：**

```javascript
const user = {
  email: 'john@example.com',     // 只是字符串
  phone: '1234567890',           // 只是字符串
  status: 'active',              // 魔法字符串
  balance: 10050                 // 以分为单位的整数
};
```

**示例（重构后）：**

```javascript
const user = {
  email: new Email('john@example.com'),
  phone: new PhoneNumber('1234567890'),
  status: UserStatus.ACTIVE,
  balance: Money.cents(10050)
};
```

---

### 长参数列表

**迹象：**

- 方法参数超过 4 个
- 一些参数总是一起出现
- 布尔参数改变方法行为
- 经常传 null / undefined

**为什么不好：**

- 难正确调用
- 参数顺序容易搞混
- 暗示方法做了太多事
- 难以增加新参数

**可用重构：**

- Introduce Parameter Object
- Preserve Whole Object
- Replace Parameter with Method Call
- Remove Flag Argument

**示例（重构前）：**

```javascript
function createUser(firstName, lastName, email, phone,
                    street, city, state, zip,
                    isAdmin, isActive, createdBy) {
  // ...
}
```

**示例（重构后）：**

```javascript
function createUser(personalInfo, address, options) {
  // personalInfo: { firstName, lastName, email, phone }
  // address: { street, city, state, zip }
  // options: { isAdmin, isActive, createdBy }
}
```

---

### 数据泥团

**迹象：**

- 同样的 3 个以上字段反复一起出现
- 参数总是成对或成组传递
- 类中的字段子集总是一起使用

**可用重构：**

- Extract Class
- Introduce Parameter Object
- Replace Data Value with Object
- Duplicate Observed Data
- Change Value to Reference
"""
with open(os.path.join(fa_dir, "03-skills", "refactor", "references", "code-smells.md"), "w", encoding="utf-8") as f:
    f.write(content)

print("03-skills/refactor/references/code-smells.md written!")