import os

fa_dir = r"D:\Project\claude-howto\fa"

content = """---
name: doc-generator
description: تولید مستندات جامع و دقیق API از کد منبع. برای ایجاد یا به‌روزرسانی مستندات API، تولید مشخصات OpenAPI، یا وقتی که کاربر به مستندات API، نقاط پایگاه یا توضیحات اشاره می‌کند، مورد استفاده قرار می‌گیرد.
---

# مهارت تولید مستندات API

## موارد قابل تولید

- مشخصات OpenAPI / Swagger
- مستندات نقاط پایگاه API
- مثال‌های استفاده از SDK
- راهنمای یکپارچگی
- مرجع کدهای خطا
- راهنمای اعتبارسنجی

## ساختاری مستندات

### نحوه نوشتن هر نقطه پایگاه

````markdown
## GET /api/v1/users/:id

### توضیح
توضیح کوتاه چه کاری انجام می‌دهد

### پارامترها

| نام | نوع | الزامی | توضیح |
|------|------|------|------|
| id | string | بله | شناسه کاربر |

### پاسخ

**۲۰۰ موفقیت**

```json
{
  "id": "usr_123",
  "name": "John Doe",
  "email": "john@example.com",
  "created_at": "2025-01-15T10:30:00Z"
}
```

**۴۰۴ یافت نشد**

```json
{
  "error": "USER_NOT_FOUND",
  "message": "User does not exist"
}
```

### مثال

**cURL**

```bash
curl -X GET "https://api.example.com/api/v1/users/usr_123" \\
  -H "Authorization: Bearer YOUR_TOKEN"
```

**JavaScript**

```javascript
const user = await fetch('/api/v1/users/usr_123', {
  headers: { 'Authorization': 'Bearer token' }
}).then(r => r.json());
```

**Python**

```python
response = requests.get(
    'https://api.example.com/api/v1/users/usr_123',
    headers={'Authorization': 'Bearer token'}
)
user = response.json()
```
````
"""

with open(os.path.join(fa_dir, "03-skills", "doc-generator", "SKILL.md"), "w", encoding="utf-8") as f:
    f.write(content)

print("doc-generator SKILL.md written!")