<picture>
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


### Inline Method

**何时使用**：方法体和名字一样清楚，或者只是多余转发

**动机**：当方法没有额外价值时，去掉不必要的间接层。

**步骤：**

1. 确认这个方法不是多态方法
2. 找到所有调用点
3. 用方法体替换每个调用
4. 每替换一次就测试一次
5. 删除方法定义

**前：**

```javascript
function getRating(driver) {
  return moreThanFiveLateDeliveries(driver) ? 2 : 1;
}

function moreThanFiveLateDeliveries(driver) {
  return driver.numberOfLateDeliveries > 5;
}
```

**后：**

```javascript
function getRating(driver) {
  return driver.numberOfLateDeliveries > 5 ? 2 : 1;
}
```

---

### Extract Variable

**何时使用**：复杂表达式难以理解

**动机**：给复杂表达式的一部分起名字。

**步骤：**

1. 确保表达式没有副作用
2. 声明一个不可变变量
3. 将表达式结果赋给变量
4. 用变量替换原表达式
5. 测试

**前：**

```javascript
return order.quantity * order.itemPrice -
  Math.max(0, order.quantity - 500) * order.itemPrice * 0.05 +
  Math.min(order.quantity * order.itemPrice * 0.1, 100);
```

**后：**

```javascript
const basePrice = order.quantity * order.itemPrice;
const quantityDiscount = Math.max(0, order.quantity - 500) * order.itemPrice * 0.05;
const shipping = Math.min(basePrice * 0.1, 100);
return basePrice - quantityDiscount + shipping;
```

---

### Inline Variable

**何时使用**：变量名没有比表达式更清楚

**动机**：移除没必要的间接层。

**步骤：**

1. 检查右侧表达式没有副作用
2. 如果变量不是不可变的，先改成不可变并测试
3. 找到第一次引用并替换成表达式
4. 测试
5. 对所有引用重复
6. 删除变量声明和赋值
7. 测试

---

### Rename Variable

**何时使用**：名字没有清楚表达用途

**动机**：好名字是清晰代码的基础。

**步骤：**

1. 如果变量有多个引用，先重命名所有引用
2. 确保新名字能符合代码风格
3. 测试


### Replace Temp with Query

**何时使用**：临时变量阻碍提取方法

**动机**：把临时变量变成一个查询方法。

**步骤：**

1. 确认临时变量只读
2. 把临时变量的计算移到一个新方法中
3. 用新方法替换临时变量
4. 测试

---

### Introduce Parameter Object

**何时使用**：多个参数总是成组出现

**动机**：用一个对象封装一组相关参数。

**步骤：**

1. 创建新对象，把相关参数移入
2. 更新调用点
3. 测试

**前：**

```javascript
function createUser(firstName, lastName, email, phone,
                    street, city, state, zip,
                    isAdmin, isActive, createdBy)
```

**后：**

```javascript
function createUser(personalInfo, address, options)
```

---

### Move Method

**何时使用**：方法更适合在另一个类里

**动机**：让行为放在合适的地方。

**步骤：**

1. 检查方法是否依赖其他类的状态
2. 复制方法到目标类
3. 更新引用
4. 测试
5. 删除原方法


### Extract Class

**何时使用**：大类里有多个职责

**动机**：拆分类以维持单一职责。

**步骤：**

1. 决定如何拆分职责
2. 创建新类
3. 把字段从原类移到新类
4. 测试
5. 把方法从原类移到新类
6. 每次移动后测试
7. 重新检查并命名两个类
8. 决定如何暴露新类

**前：**

```javascript
class Person {
  get name() { return this._name; }
  set name(arg) { this._name = arg; }
  get officeAreaCode() { return this._officeAreaCode; }
  set officeAreaCode(arg) { this._officeAreaCode = arg; }
  get officeNumber() { return this._officeNumber; }
  set officeNumber(arg) { this._officeNumber = arg; }

  get telephoneNumber() {
    return `(${this._officeAreaCode}) ${this._officeNumber}`;
  }
}
```

**后：**

```javascript
class Person {
  constructor() {
    this._telephoneNumber = new TelephoneNumber();
  }
  get name() { return this._name; }
  set name(arg) { this._name = arg; }
  get telephoneNumber() { return this._telephoneNumber.toString(); }
  get officeAreaCode() { return this._telephoneNumber.areaCode; }
  set officeAreaCode(arg) { this._telephoneNumber.areaCode = arg; }
}

class TelephoneNumber {
  get areaCode() { return this._areaCode; }
  set areaCode(arg) { this._areaCode = arg; }
  get number() { return this._number; }
  set number(arg) { this._number = arg; }
  toString() { return `(${this._areaCode}) ${this._number}`; }
}
```

---

## 异味到重构快速映射

| 代码异味 | 主要重构 | 备选方案 |
|----------|---------|---------|
| 长函数 | Extract Method | Replace Temp with Query |
| 重复代码 | Extract Method | Pull Up Method |
| 大类 | Extract Class | Extract Subclass |
| 长参数列表 | Introduce Parameter Object | Preserve Whole Object |
| Feature Envy | Move Method | Extract Method + Move |
| 数据泥团 | Extract Class | Introduce Parameter Object |
| 基础类型沉迷 | Replace Primitive with Object | Replace Type Code |
| switch 语句 | Replace Conditional with Polymorphism | Replace Type Code |
| 临时字段 | Extract Class | Introduce Null Object |
| 消息链 | Hide Delegate | Extract Method |
| 中间人 | Remove Middle Man | Inline Method |
| 发散式变化 | Extract Class | Split Phase |
| 散弹式修改 | Move Method | Inline Class |
| 死代码 | Remove Dead Code | - |
| 臆想泛化 | Collapse Hierarchy | Inline Class |

---

## 参考

- Fowler, M. (2018). *Refactoring: Improving the Design of Existing Code* (第 2 版)
- 在线目录：https://refactoring.com/catalog/
