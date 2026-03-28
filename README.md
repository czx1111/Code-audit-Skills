---
name: code-audit-skills
description: AI原生代码安全审计工具，支持多语言AST分析、调用图分析、漏洞检测、AI深度审计。使用此Skill进行代码安全审计、漏洞扫描、架构分析和代码质量评估。支持Python/JavaScript/TypeScript/Go/Java/PHP/Rust等多种语言。
license: MIT
---
# Code Audit Skills - AI原生代码安全审计

## 概述

Code Audit Skills 是一个强大的代码安全审计工具，提供：

- **多语言AST解析**：支持 Python、JavaScript/TypeScript、Go、Java、PHP、Rust 等
- **调用图分析**：构建函数调用关系图，追踪数据流
- **漏洞检测引擎**：内置 OWASP Top 10、CWE 等安全规则
- **AI深度审计**：利用 LLM 进行语义级安全分析
- **报告生成**：生成专业的安全审计报告

## 触发条件

- 用户请求代码安全审计、漏洞扫描
- 需要分析代码中的安全风险
- 进行代码质量评估
- 分析函数调用关系和数据流
- 检测特定类型的安全漏洞（SQL注入、XSS、命令注入等）

## 必要输入

```text
Target Path: /path/to/code
Language: auto | python | javascript | go | java | php | rust
Audit Mode: quick | standard | deep
Scan Scope: all | security | quality | architecture
Output Format: markdown | json | html
```

最少必填字段：

- `Target Path`：要审计的代码路径

可选字段：

- `Language`：指定语言，默认自动检测
- `Audit Mode`：审计模式，默认 standard
- `Scan Scope`：扫描范围，默认 security
- `Output Format`：输出格式，默认 markdown

## 目录结构

```
code-audit-skills/
├── SKILL.md                    # 主控文件
├── agents/
│   └── default.yaml            # Agent 配置
├── scripts/
│   ├── run_audit.py            # 审计启动脚本
│   ├── generate_report.py      # 报告生成脚本
│   └── validate_results.py     # 结果验证脚本
├── references/
│   ├── vulnerability-db.md     # 漏洞数据库参考
│   ├── call-graph-guide.md     # 调用图分析指南
│   ├── ai-audit-workflow.md    # AI审计工作流
│   └── rules-syntax.md         # 规则语法参考
└── rules/
    ├── owasp-top10/            # OWASP Top 10 规则
    ├── cwe/                    # CWE 规则
    ├── lang-specific/          # 语言特定规则
    └── custom/                 # 自定义规则
```

## 阶段流程

### Phase 1: 项目分析与语言检测

- 扫描目标路径，识别项目结构
- 自动检测编程语言和框架
- 分析依赖关系和配置文件

### Phase 2: AST解析与代码建模

- 解析源代码生成 AST
- 提取函数、类、变量定义
- 识别导入和依赖关系

### Phase 3: 调用图构建

- 构建函数调用关系图
- 分析数据流和控制流
- 识别敏感数据传播路径

### Phase 4: 规则引擎扫描

- 应用 OWASP Top 10 规则
- 应用 CWE 漏洞规则
- 应用语言特定安全规则

### Phase 5: AI深度审计（可选）

- 语义级安全分析
- 业务逻辑漏洞检测
- 认证授权问题分析
- 复杂漏洞链识别

### Phase 6: 结果整合与报告生成

- 汇总所有发现的漏洞
- 按严重程度分类排序
- 生成修复建议
- 输出审计报告

## 可用的 Skill 工具

### 核心审计工具

| 工具名称                   | 功能描述                 |
| -------------------------- | ------------------------ |
| `audit_scan`             | 执行完整代码审计扫描     |
| `audit_quick_scan`       | 快速扫描，仅检测高危漏洞 |
| `audit_analyze_file`     | 分析单个文件             |
| `audit_analyze_function` | 分析特定函数             |

### 分析工具

| 工具名称                   | 功能描述     |
| -------------------------- | ------------ |
| `build_call_graph`       | 构建调用图   |
| `analyze_data_flow`      | 数据流分析   |
| `detect_vulnerabilities` | 漏洞检测     |
| `check_dependencies`     | 依赖安全检查 |

### AI审计工具

| 工具名称                | 功能描述         |
| ----------------------- | ---------------- |
| `ai_deep_audit`       | AI深度语义分析   |
| `ai_analyze_auth`     | 认证授权分析     |
| `ai_detect_biz_logic` | 业务逻辑漏洞检测 |
| `ai_suggest_fix`      | AI修复建议       |

### 报告工具

| 工具名称            | 功能描述      |
| ------------------- | ------------- |
| `generate_report` | 生成审计报告  |
| `export_sarif`    | 导出SARIF格式 |
| `export_json`     | 导出JSON格式  |

## 漏洞严重级别

| 级别               | 描述                   | 示例                     |
| ------------------ | ---------------------- | ------------------------ |
| **Critical** | 可直接被利用的高危漏洞 | SQL注入、RCE、认证绕过   |
| **High**     | 有较高利用价值的漏洞   | XSS、SSRF、信息泄露      |
| **Medium**   | 需要特定条件的漏洞     | 弱密码策略、不安全的配置 |
| **Low**      | 潜在风险点             | 缺少日志、代码异味       |
| **Info**     | 信息提示               | 最佳实践建议             |

## 支持的漏洞类型

### 注入类

- SQL注入 (CWE-89)
- 命令注入 (CWE-78)
- LDAP注入 (CWE-90)
- XPath注入 (CWE-91)
- NoSQL注入

### 认证授权

- 身份认证绕过 (CWE-287)
- 权限提升 (CWE-269)
- 会话管理问题 (CWE-384)
- 不安全的直接对象引用 (CWE-639)

### 数据安全

- 敏感数据泄露 (CWE-200)
- 硬编码密码 (CWE-798)
- 不安全的加密 (CWE-327)
- 日志注入 (CWE-117)

### 其他

- XSS (CWE-79)
- SSRF (CWE-918)
- XXE (CWE-611)
- 路径遍历 (CWE-22)
- 不安全的反序列化 (CWE-502)

## 输出要求

### Markdown报告格式

```markdown
# 代码安全审计报告

## 概要
- 扫描路径: /path/to/code
- 扫描时间: 2024-01-01 10:00:00
- 扫描模式: standard
- 总文件数: 100
- 发现问题: 25

## 统计
| 严重级别 | 数量 |
|---------|------|
| Critical | 2 |
| High | 5 |
| Medium | 10 |
| Low | 8 |

## 详细问题

### [Critical] SQL注入 - main.py:45
**描述**: 用户输入未经过滤直接拼接到SQL查询中
**代码位置**: `main.py:45`
**代码片段**:
```python
query = f"SELECT * FROM users WHERE id = {user_input}"
```

**修复建议**: 使用参数化查询

```python
query = "SELECT * FROM users WHERE id = ?"
cursor.execute(query, (user_input,))
```

**调用链**: process_request() -> get_user() -> execute_query()
**CWE**: CWE-89

```

## 错误处理

- 如果目标路径不存在，返回明确的错误信息
- 如果无法识别语言，提示用户手动指定
- 如果内存不足，建议使用 quick 模式
- 如果 AI 服务不可用，降级为规则引擎扫描

## 性能优化

- 使用增量扫描，仅分析变更文件
- 并行处理多个文件
- 缓存 AST 解析结果
- 按需加载规则集

## 验收要求

- [ ] AST 解析正确，能识别所有语法元素
- [ ] 调用图完整，能追踪跨文件调用
- [ ] 规则引擎能检测常见漏洞
- [ ] AI 审计能发现语义级问题
- [ ] 报告格式规范，信息完整
- [ ] 性能满足要求（1000文件 < 5分钟）
```
