### 年会抽奖和抽签系统

- 地址：http://xxxx

- 返回参数：
  - 正常返回
    ```json
    {
      "data": [],
      "message": "success",
      "state": 0
    }
    ```
  - 错误信息
    ```json
    {
      "data": [], 
      "message": "fail", 
      "state": 1
    }
    ```

1. state返回状态码，为0则正常返回，数据正常
2. data具体数据
3. message返回的具体参数

#### 抽奖接口：

- 地址：http://xxxx/lucky/[奖项参数]
- 奖项参数：类型int
- 返回数据：

```json
{
  "data": "张三",
  "message": "success",
  "state": 0
}
```
| 数据列 | 数据类型 | 说明    |
|-----|------|-------|
| 数据2 | name | 员工姓名  |

#### 查询中奖接口：

- 地址：http://xxxx/get_lucky_user
- 奖项参数：none
- 返回数据：

```json
{
  "data": [
    [
      4,
      "张三",
      1,
      "Thu, 12 Jan 2023 08:43:38 GMT"
    ]
  ],
  "message": "success",
  "state": 0
}
```

| 数据列 | 数据类型 | 说明    |
|-----|------|-------|
| 数据1 | id   | 用户id  |
| 数据2 | name | 员工姓名  |
| 数据3 | date | 获奖的时间 |

