# Code Audit MCP

<div align="center">

![Version](https://img.shields.io/badge/version-1.0.0-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Languages](https://img.shields.io/badge/languages-Python%20%7C%20JS%20%7C%20Go%20%7C%20Java%20%7C%20PHP%20%7C%20Rust-orange.svg)

**AI 原生代码安全审计工具**

[English](#english) | [中文](#中文)

</div>

---

## 中文

### 概述

Code Audit MCP 是一个强大的 AI 原生代码安全审计工具，基于 Model Context Protocol (MCP) 构建。它结合了传统静态分析技术与大语言模型 (LLM) 的深度语义理解能力，能够高效检测代码中的安全漏洞和潜在风险。

### ✨ 核心特性

- **多语言 AST 解析**: 支持 Python、JavaScript/TypeScript、Go、Java、PHP、Rust 等主流编程语言
- **调用图分析**: 构建函数调用关系图，追踪数据流和敏感信息传播路径
- **智能漏洞检测**: 内置 OWASP Top 10 和 CWE 安全规则库
- **AI 深度审计**: 利用 LLM 进行语义级安全分析，发现业务逻辑漏洞
- **专业报告生成**: 支持 Markdown、JSON、SARIF 等多种输出格式

### 🚀 快速开始

#### 安装

```bash
# 克隆仓库
git clone https://github.com/czx1111/Code-audit-Skills.git

# 进入目录
cd Code-audit-Skills
```

#### 基本使用

```python
# 快速扫描
audit_quick_scan(targetPath="/path/to/code")

# 完整审计
audit_scan(
    targetPath="/path/to/code",
    language="auto",           # 自动检测语言
    mode="standard",           # quick | standard | deep
    scope="security",          # all | security | quality | architecture
    outputFormat="markdown"    # markdown | json | sarif
)

# 分析单个文件
audit_analyze_file(filePath="/path/to/file.py")

# 构建调用图
build_call_graph(targetPath="/path/to/code", language="python")

# 数据流分析
analyze_data_flow(targetPath="/path/to/code", language="python")
```

### 📊 支持的漏洞类型

| 类别 | 漏洞类型 | CWE 编号 |
|------|----------|----------|
| 注入类 | SQL注入、命令注入、XSS、LDAP注入 | CWE-89, CWE-78, CWE-79 |
| 认证授权 | 身份认证绕过、权限提升、会话管理 | CWE-287, CWE-269, CWE-384 |
| 数据安全 | 敏感数据泄露、硬编码密码、弱加密 | CWE-200, CWE-798, CWE-327 |
| 其他 | SSRF、XXE、路径遍历、反序列化 | CWE-918, CWE-611, CWE-22, CWE-502 |

### 🔧 审计模式

| 模式 | 描述 | 适用场景 |
|------|------|----------|
| `quick` | 快速扫描高危漏洞 | CI/CD 流水线 |
| `standard` | 标准安全审计 | 常规代码审查 |
| `deep` | 深度分析包含 AI 审计 | 重要项目安全评估 |

### 📁 项目结构

```
code-audit-mcp/
├── SKILL.md                    # 主控配置文件
├── agents/
│   └── default.yaml            # Agent 配置
├── scripts/
│   └── run_audit.py            # 命令行启动脚本
├── references/
│   ├── vulnerability-db.md     # 漏洞数据库参考
│   ├── call-graph-guide.md     # 调用图分析指南
│   └── ai-audit-workflow.md    # AI 审计工作流
└── rules/                      # 安全规则目录
```

### 📖 文档

- [漏洞数据库参考](references/vulnerability-db.md)
- [调用图分析指南](references/call-graph-guide.md)
- [AI 审计工作流](references/ai-audit-workflow.md)

### 🤝 贡献

欢迎提交 Issue 和 Pull Request！

### 📄 许可证

本项目采用 MIT 许可证 - 详见 [LICENSE](LICENSE) 文件

---

## English

### Overview

Code Audit MCP is a powerful AI-native code security audit tool built on the Model Context Protocol (MCP). It combines traditional static analysis techniques with Large Language Model (LLM) deep semantic understanding to efficiently detect security vulnerabilities and potential risks in code.

### ✨ Key Features

- **Multi-language AST Parsing**: Support for Python, JavaScript/TypeScript, Go, Java, PHP, Rust, and more
- **Call Graph Analysis**: Build function call relationship graphs, track data flow and sensitive information propagation
- **Intelligent Vulnerability Detection**: Built-in OWASP Top 10 and CWE security rule libraries
- **AI Deep Audit**: Leverage LLM for semantic-level security analysis to discover business logic vulnerabilities
- **Professional Report Generation**: Support Markdown, JSON, SARIF, and other output formats

### 🚀 Quick Start

```python
# Quick scan
audit_quick_scan(targetPath="/path/to/code")

# Full audit
audit_scan(
    targetPath="/path/to/code",
    language="auto",
    mode="standard",
    scope="security",
    outputFormat="markdown"
)
```

### 📊 Supported Vulnerability Types

- **Injection**: SQL Injection, Command Injection, XSS, LDAP Injection
- **Authentication**: Auth Bypass, Privilege Escalation, Session Management
- **Data Security**: Sensitive Data Exposure, Hardcoded Credentials, Weak Cryptography
- **Others**: SSRF, XXE, Path Traversal, Insecure Deserialization

### 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

<div align="center">

**⭐ If this project helps you, please give it a star! ⭐**

Made with ❤️ by [czx1111](https://github.com/czx1111)

</div>
