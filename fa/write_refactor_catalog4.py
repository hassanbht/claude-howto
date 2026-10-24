import os

fa_dir = r"D:\Project\claude-howto\fa"

content = """

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
"""
with open(os.path.join(fa_dir, "03-skills", "refactor", "references", "refactoring-catalog.md"), "a", encoding="utf-8") as f:
    f.write(content)

print("refactoring-catalog.md finalized!")