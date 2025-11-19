# Check Point AI Security Dify Plugin

**作者：** Birdlex Wu
**版本：** 0.0.1
**类型：** 工具

### 概述
本 Dify 插件（“本插件”）提供了与 Lakera Guard API 的接口，**该产品由 Check Point Software Technologies 提供**。它旨在通过筛选用户输入和模型响应中的各种威胁（包括提示注入、有毒内容和个人身份信息（PII）泄露），来保护您的 AI 应用程序。

### 使用前重要须知

**API 密钥安全：** 您有责任保护您的 Lakera Guard API 密钥的安全。请勿在客户端代码中暴露或将其提交到版本控制中。

**服务免责声明：** 本插件是 Lakera Guard API 的一个接口。安全筛选的性能、准确性和可用性均受 Lakera 的服务条款约束。本插件的作者对 Lakera Guard API 提供的结果不承担任何责任。

**许可免责声明：** 本软件按“原样”提供，作者不承担与本软件相关的任何担保，包括所有关于适销性和特定用途适用性的默示担保。在任何情况下，作者均不对因使用或执行本软件而产生的任何特殊的、直接的、间接的或后果性的损害，或任何因使用、数据或利润损失而导致的损害承担任何责任，无论是在合同诉讼、疏忽或其他侵权行为中。

### 先决条件

若要使用本插件，您需要一个 Lakera Guard API 密钥。
您可以在 [Lakera 网站](https://www.lakera.ai/) 注册免费试用，并按照 [官方快速入门指南](https://docs.lakera.ai/docs/quickstart) 获取 API 密钥并设置您的项目。
如果您无法通过官方网站获取 API 密钥，请联系当地的 [Check Point 合作伙伴](https://partnerlocator.checkpoint.com/) 寻求帮助。

### 主要功能

*   **全面威胁筛选**：集成 Lakera Guard 强大的 API，可检测并标记各种 AI 特定威胁，例如提示注入、数据泄露（PII）以及用户输入和 AI 模型输出中的有害内容。
*   **灵活配置**：允许用户通过可选参数（如 `project_id`、`payload`（用于详细检测）、`breakdown`（用于标记决策）、`metadata` 和 `dev_info`）自定义筛选行为。
*   **清晰且可操作的输出**：提供一个直接的 `true` 或 `false` 布尔值，以指示是否检测到威胁，同时提供来自 Lakera Guard 的完整原始 JSON 响应，以供详细分析。

### 使用方法

#### 安装
从 `Dify Marketplace`、`GitHub` 或 `Local` 来源安装本插件，并配置您的 API 密钥。

![img1](../_assets/README_assets/installation.png)

#### 将插件添加到 Chatflow
您可以将本插件添加到输入 (Input) 或输出 (Output) 流程中，以检测可疑内容。您必须同时使用 `条件节点 (Conditional Node)` 进行判断：如果检测结果为 `true`，则终止流程；如果检测结果为 `false`，则继续流程。

![img2](../_assets/README_assets/chatflow.png)

插件设置：

![img3](../_assets/README_assets/input.png)

参数说明如下：

*   **Project ID**：用于筛选的 Lakera Guard 项目 ID。（登录 Lakera 门户并创建新项目以获取项目 ID。）
*   **Include Payload**：设置为 `true` 以在响应中包含详细有效载荷 (payload)。
*   **Include Breakdown**：设置为 `true` 以在响应中包含标记决策的分解信息。
*   **Metadata**：包含请求元数据的 JSON 字符串。示例：`'{"user_id": "123"}'`
*   **Developer Info**：设置为 `true` 以在响应中包含开发者信息。

输出变量：

*   **text**：返回 `true` 或 `false`。
*   **json**：返回更详细的检测信息，以便您确定是哪个策略阻止了内容。

输入条件流程：

![img4](../_assets/README_assets/input_condition.png)

Chatflow 演示：
![img5](../_assets/README_assets/chat.png)
