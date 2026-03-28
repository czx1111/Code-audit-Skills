# 调用图分析指南

## 概述

调用图分析是代码审计的核心技术之一，用于理解代码的执行流程和数据传播路径。本文档介绍如何使用调用图分析来识别潜在的安全漏洞。

## 调用图基础

### 什么是调用图

调用图（Call Graph）是一个有向图，其中：
- **节点** 代表函数/方法
- **边** 代表函数之间的调用关系

### 调用图的用途

1. **理解代码结构**: 可视化函数之间的依赖关系
2. **影响分析**: 修改某个函数会影响哪些其他函数
3. **漏洞追踪**: 从用户输入追踪到敏感操作
4. **入口点识别**: 找到攻击者可以触达的函数

## 构建调用图

### 使用 audit_scan 工具

```json
{
  "targetPath": "/path/to/code",
  "mode": "standard",
  "scope": "all"
}
```

### 使用 build_call_graph 工具

```json
{
  "targetPath": "/path/to/code",
  "language": "python",
  "maxDepth": 10
}
```

## 分析结果解读

### 入口点 (Entry Points)

入口点是调用图中没有被其他函数调用的函数。这些通常是：
- HTTP请求处理函数
- 命令行入口
- 事件处理函数
- 定时任务

**安全意义**: 入口点是攻击者可以直接触达的代码，需要特别关注输入验证。

### 敏感汇点 (Sensitive Sinks)

敏感汇点是执行敏感操作的函数，例如：
- 数据库操作: execute, query
- 文件操作: open, write
- 命令执行: system, exec
- 网络请求: fetch, request

**安全意义**: 如果用户输入能够到达这些函数，可能存在漏洞。

### 危险路径

从入口点到敏感汇点的路径。如果存在这样的路径，且中间没有足够的输入验证/清理，则可能存在漏洞。

## 数据流分析

### 污点传播

污点分析追踪用户输入（污点源）在程序中的传播：

```
用户输入 -> 函数A -> 函数B -> 敏感操作
```

### 清理器 (Sanitizer)

清理器是能够消除污点的函数：
- `escape_html()` - XSS清理
- `parameterize()` - SQL参数化
- `validate_input()` - 输入验证

### 分析示例

```python
# 污点源
user_input = request.args.get('id')

# 污点传播
def get_user(user_id):
    # 没有清理，污点继续传播
    return db.query(f"SELECT * FROM users WHERE id = {user_id}")

# 敏感汇点
user = get_user(user_input)  # 漏洞！SQL注入
```

## 实战案例

### 案例1: SQL注入链路分析

```
入口点: handle_request()
  └── 调用: process_query()
       └── 调用: execute_sql()  [敏感汇点]
            └── 参数: user_input [未清理]
```

**发现**: 用户输入从 `handle_request` 传播到 `execute_sql`，中间没有清理。

### 案例2: 认证绕过检测

```
入口点: api_endpoint()
  ├── 调用: check_permission()  [分支: 可能被绕过]
  │    └── 返回: True (无实际检查)
  └── 调用: sensitive_operation()
```

**发现**: `check_permission` 函数虽然被调用，但实际没有执行权限验证。

### 案例3: 敏感数据泄露

```
入口点: login()
  └── 调用: authenticate()
       └── 调用: log_error()  [敏感汇点]
            └── 参数: password [明文]
```

**发现**: 密码被记录到日志中。

## 工具使用

### MCP工具调用示例

```typescript
// 1. 构建调用图
const callGraph = await mcp.call('build_call_graph', {
  targetPath: '/app/src',
  language: 'python'
});

// 2. 查找危险路径
const dangerousPaths = callGraph.dangerousPaths;

// 3. 分析每条路径
for (const path of dangerousPaths) {
  console.log(`发现危险路径: ${path.entry} -> ${path.sink}`);
}
```

### 输出格式

```json
{
  "nodes": [
    {
      "id": "func_1",
      "name": "handle_request",
      "file": "app.py",
      "line": 10,
      "isSensitive": false
    }
  ],
  "edges": [
    {
      "from": "func_1",
      "to": "func_2",
      "type": "direct"
    }
  ],
  "entryPoints": ["func_1"],
  "sensitiveSinks": ["func_3"]
}
```

## 最佳实践

### 1. 关注入口点
- 分析所有公开的入口点
- 检查输入验证是否完整
- 识别隐藏的入口点

### 2. 追踪数据流
- 从用户输入开始追踪
- 记录所有数据转换
- 验证清理器的有效性

### 3. 验证清理
- 确认清理函数真正有效
- 检查是否有绕过方式
- 考虑编码和格式问题

### 4. 结合其他分析
- 静态分析 + 动态测试
- 人工审查关键路径
- 渗透测试验证漏洞

## 局限性

1. **动态调用**: 无法分析通过反射/动态加载的代码
2. **间接调用**: 函数指针/回调可能难以追踪
3. **跨语言**: 多语言项目可能需要单独分析
4. **外部库**: 第三方库内部调用通常不分析

## 参考资料

- [Static Program Analysis](https://cs.au.dk/~amoeller/spa/)
- [Call Graph Construction Algorithms](https://dl.acm.org/doi/10.1145/324162.324163)
- [Taint Analysis for Web Applications](https://owasp.org/www-community/vulnerabilities/)
