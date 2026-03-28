# AI 审计工作流

## 概述

AI 审计利用大语言模型（LLM）进行深度语义分析，能够发现传统静态分析难以检测的漏洞，如：
- 业务逻辑漏洞
- 认证授权问题
- 复杂攻击链
- 上下文相关的安全问题

## 工作流程

### Phase 1: 准备阶段

1. **收集代码上下文**
   - 目标代码文件
   - 相关配置文件
   - 依赖信息

2. **确定分析重点**
   - 安全审计 (security)
   - 业务逻辑 (logic)
   - 性能问题 (performance)
   - 全面分析 (all)

### Phase 2: AI 分析

1. **函数级分析**
   - 提取每个函数的代码
   - 构建分析提示词
   - 调用 LLM 分析
   - 解析分析结果

2. **数据流分析**
   - 识别污点源和汇点
   - 追踪数据传播路径
   - 检测清理器缺失

3. **认证授权分析**
   - 识别认证相关代码
   - 检测认证绕过风险
   - 验证授权完整性

4. **业务逻辑分析**
   - 识别关键业务流程
   - 检测逻辑漏洞
   - 验证状态转换

### Phase 3: 结果整合

1. **去重和排序**
   - 合并重复发现
   - 按严重性排序

2. **置信度评估**
   - 评估每个发现的可靠性
   - 标记需要人工验证的发现

3. **生成报告**
   - 详细描述漏洞
   - 提供修复建议
   - 指出代码位置

## 提示词设计

### 函数分析提示词模板

```
You are a security expert analyzing code for vulnerabilities.

Analyze the following {language} function for security vulnerabilities:

Function: {function_name}
Language: {language}

```{language}
{code}
```

Focus on:
1. Input validation issues
2. Authentication/authorization bypasses
3. Insecure data handling
4. Race conditions
5. Error handling vulnerabilities
6. Resource management issues
7. Logic errors that could be exploited

Response format (JSON):
{
  "vulnerabilities": [
    {
      "type": "string",
      "severity": "critical|high|medium|low",
      "line": number,
      "description": "string",
      "recommendation": "string"
    }
  ]
}
```

### 认证分析提示词模板

```
You are a security expert analyzing authentication code.

Analyze the following code for authentication vulnerabilities:

```{language}
{auth_code}
```

Focus on:
1. Weak password policies
2. Missing rate limiting
3. Session fixation
4. Missing authentication checks
5. Authorization bypasses
6. Insecure token handling
7. Timing attacks
8. Missing or weak MFA
```

### 业务逻辑提示词模板

```
You are a security expert analyzing business logic for vulnerabilities.

Analyze the following business-critical code:

```{language}
{business_code}
```

Focus on:
1. Race conditions (TOCTOU)
2. Missing transaction checks
3. Integer overflow/underflow
4. Business rule bypasses
5. Missing state validation
6. Improper access control
7. Price/quantity manipulation
```

## 支持的 AI 提供商

### OpenAI

```typescript
const aiAnalyzer = new AIAnalyzer('python', {
  provider: 'openai',
  apiKey: process.env.OPENAI_API_KEY,
  model: 'gpt-4-turbo-preview',
});
```

### Anthropic

```typescript
const aiAnalyzer = new AIAnalyzer('python', {
  provider: 'anthropic',
  apiKey: process.env.ANTHROPIC_API_KEY,
  model: 'claude-3-opus-20240229',
});
```

### 自定义端点

```typescript
const aiAnalyzer = new AIAnalyzer('python', {
  provider: 'custom',
  baseUrl: 'https://your-llm-endpoint.com/v1/chat',
  apiKey: process.env.CUSTOM_API_KEY,
});
```

## 启发式分析（无需 API）

当没有配置 AI API 时，系统会使用启发式规则进行分析：

### 检测规则

1. **密码比较问题**
   ```python
   # 不安全
   if password == stored_password:
   ```
   应使用恒定时间比较函数

2. **不安全随机数**
   ```python
   # 不安全
   import random
   token = random.random()
   ```
   应使用 `secrets` 模块

3. **宽泛异常处理**
   ```python
   # 可能隐藏问题
   try:
       ...
   except:
       pass
   ```

4. **敏感信息日志**
   ```python
   # 危险
   print(f"User password: {password}")
   ```

## 结果验证

### 人工审查清单

- [ ] 漏洞是否真实存在？
- [ ] 严重级别是否正确？
- [ ] 修复建议是否可行？
- [ ] 是否有遗漏的上下文？

### 动态验证

1. **构建测试用例**
   - 基于漏洞描述构造输入
   - 在测试环境中验证

2. **渗透测试**
   - 尝试利用发现的漏洞
   - 记录利用过程

3. **代码审查**
   - 与开发人员确认
   - 了解业务上下文

## 最佳实践

### 1. 分层分析
- 先使用静态分析快速扫描
- 对高风险区域使用 AI 深度分析
- 人工审查关键发现

### 2. 上下文管理
- 提供足够的代码上下文
- 包含相关的配置和依赖信息
- 说明业务逻辑背景

### 3. 结果整合
- 合并不同分析方法的发现
- 去除重复和误报
- 提供统一的修复建议

### 4. 持续改进
- 记录误报和漏报
- 优化提示词模板
- 更新检测规则

## 局限性

1. **上下文窗口**: 大型代码库需要分段分析
2. **幻觉风险**: AI 可能产生虚假发现
3. **成本考量**: 大规模分析需要 API 费用
4. **语言限制**: 某些语言支持可能不够完善

## 参考配置

### 环境变量

```bash
# OpenAI
export OPENAI_API_KEY="sk-..."

# Anthropic
export ANTHROPIC_API_KEY="sk-ant-..."

# 自定义端点
export AI_ENDPOINT="https://your-endpoint.com/v1/chat"
export AI_API_KEY="your-key"
```

### MCP 工具调用

```json
{
  "name": "ai_deep_audit",
  "arguments": {
    "targetPath": "/app/src",
    "language": "python",
    "focus": "security",
    "context": "This is a web API handling user authentication"
  }
}
```
