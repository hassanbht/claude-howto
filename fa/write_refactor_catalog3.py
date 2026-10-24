import os

fa_dir = r"D:\Project\claude-howto\fa"

content = """

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
"""
with open(os.path.join(fa_dir, "03-skills", "refactor", "references", "refactoring-catalog.md"), "a", encoding="utf-8") as f:
    f.write(content)

print("refactoring-catalog.md part 3 written!")