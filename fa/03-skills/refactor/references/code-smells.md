<picture>
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


---

### 重复代码

**迹象：**

- 复制/粘贴出来的代码块
- 多个文件里有类似的逻辑
- 两个方法有相似的条件分支

**为什么不好：**

- 修复 bug 时要改多处
- 概念不一致
- 维护负担增加

**可用重构：**

- Extract Method
- Pull Up Method
- Form Template Method
- Substitute Algorithm

**检测规则：**

任何重复 3 次以上的代码都应该考虑提取。

---

### 惰性类

**迹象：**

- 类做的事情不足以支撑它的存在
- 只是一个没有增值的包装器
- 过度设计的产物

**为什么不好：**

- 增加维护开销
- 多了一层没必要的间接
- 有复杂度但没收益

**可用重构：**

- Inline Class
- Collapse Hierarchy

---

### 死代码

**迹象：**

- 无法到达的代码
- 未使用的变量 / 方法 / 类
- 注释掉的代码
- 位于不可能条件分支后的代码

**为什么不好：**

- 造成困惑
- 增加维护负担
- 降低理解速度

**可用重构：**

- Remove Dead Code
- Safe Delete

**检测：**

```bash
# 查找未使用的导出
# 查找未引用的函数
# IDE 的“unused”警告
```

---

### 臆想泛化

**迹象：**

- 只有一个子类的抽象类
- 为“未来可能需要”而加的未使用参数
- 只是转发的函数
- 为一个用例设计的“框架”

**为什么不好：**

- 复杂度没有收益
- 违背 YAGNI
- 更难理解

**可用重构：**

- Collapse Hierarchy
- Inline Class
- Remove Parameter
- Rename Method

---

## 耦合类异味

表示类之间耦合过强。

### Feature Envy

**迹象：**

- 一个方法使用别的类的数据比自己更多
- 对另一个对象调用很多 getter
- 数据和行为分离

**为什么不好：**

- 行为放错地方了
- 封装性差
- 难维护

**可用重构：**

- Move Method
- Move Field
- Extract Method（然后移动）

**示例（重构前）：**

```javascript
class Order {
  getDiscountedPrice(customer) {
    // 这里大量使用 customer 数据
    if (customer.loyaltyYears > 5) {
      return this.price * customer.discountRate;
    }
    return this.price;
  }
}
```

**示例（重构后）：**

```javascript
class Customer {
  getDiscountedPriceFor(price) {
    if (this.loyaltyYears > 5) {
      return price * this.discountRate;
    }
    return price;
  }
}
```

---

### 不恰当的亲密

**迹象：**

- 类之间互相访问私有细节
- 双向引用很多
- 子类知道父类太多细节

**为什么不好：**

- 耦合高
- 改一边会连带另一边
- 难单独修改

**可用重构：**

- Move Method
- Move Field
- Change Bidirectional to Unidirectional
- Extract Class
- Hide Delegate

---

### 消息链

**迹象：**

- 方法调用链很长：`a.getB().getC().getD().getValue()`
- 客户端依赖导航结构
- “火车残骸”式代码

**为什么不好：**

- 很脆弱，任何一层变动都会坏
- 违反迪米特法则
- 绑定到对象结构

**可用重构：**

- Hide Delegate
- Extract Method
- Move Method

**示例：**

```javascript
// 差：消息链
const managerName = employee.getDepartment().getManager().getName();

// 更好：隐藏委派
const managerName = employee.getManagerName();
```

---

### 中间人

**迹象：**

- 类只是把调用转发给另一个类
- 一半以上的方法都是委派
- 没有额外价值

**为什么不好：**

- 多了一层没必要的间接
- 维护成本更高
- 架构令人困惑

**可用重构：**

- Remove Middle Man
- Inline Method

---

## 严重性指南

| 严重性 | 说明 | 处理方式 |
|--------|------|---------|
| **Critical** | 阻塞开发，导致 bug | 立刻修复 |
| **High** | 明显增加维护负担 | 本迭代修复 |
| **Medium** | 有问题但还能接受 | 近期计划修复 |
| **Low** | 小问题 | 视情况顺手修 |

---

## 快速检测清单

扫描代码时使用这个清单：

- [ ] 有没有超过 30 行的函数？
- [ ] 有没有超过 300 行的类？
- [ ] 有没有参数超过 4 个的函数？
- [ ] 有没有重复代码块？
- [ ] 有没有按类型码分支的 switch/case？
- [ ] 有没有未使用的代码？
- [ ] 有没有大量使用其他类数据的方法？
- [ ] 有没有很长的方法调用链？
- [ ] 有没有解释“是什么”而不是“为什么”的注释？
- [ ] 有没有应该封装成对象的基础类型？
