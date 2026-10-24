import os

fa_dir = r"D:\Project\claude-howto\fa"

content = """

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
"""
with open(os.path.join(fa_dir, "03-skills", "refactor", "references", "refactoring-catalog.md"), "a", encoding="utf-8") as f:
    f.write(content)

print("refactoring-catalog.md part 2 written!")