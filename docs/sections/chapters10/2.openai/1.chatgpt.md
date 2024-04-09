## python代码配置

```python
from openai import OpenAI
import httpx

client = OpenAI(
    base_url="https://api.xty.app/v1", 
    api_key="sk-xxx",
    http_client=httpx.Client(
        base_url="https://api.xty.app/v1",
        follow_redirects=True,
    ),
)

completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "Hello!"}
  ]
)

print(completion)
```

说明：添加http_client是为了解决307自动重定向的问题，若无此问题，可以删除此项

