# Check Point AI Security Dify Plugin

**作者：** Birdlex Wu
**版本：** 0.0.1
**類型：** 工具

### 概述
本 Dify 外掛程式（下稱「本外掛」）提供連接至 Lakera Guard API 的介面，該產品為 **Check Point Software Technologies 旗下產品**。其設計旨在透過篩選使用者輸入及模型回應中的廣泛威脅，包括提示詞注入 (Prompt Injections)、有害內容及個人識別資訊 (PII) 洩露，以保護您的 AI 應用程式。

### 使用前重要須知

**API 金鑰安全：** 您有責任保護您的 Lakera Guard API 金鑰安全。請勿將其暴露於客戶端程式碼或提交至版本控制系統中。

**服務免責聲明：** 本外掛僅作為 Lakera Guard API 的介面。安全篩選的效能、準確性及可用性均受 Lakera 服務條款約束。本外掛作者不對 Lakera Guard API 提供的結果負責。

**授權免責聲明：** 本軟體按「原樣」提供，作者不對本軟體提供任何形式的擔保，包括所有適銷性及特定用途適用性的默示擔保。在任何情況下，無論是在合約訴訟、疏忽或其他侵權行為中，作者均不對因使用或執行本軟體而產生的任何特殊、直接、間接或後果性損害，或因使用、資料或利潤損失而導致的任何損害承擔責任。

### 先決條件

若要使用本外掛，您需要一組 Lakera Guard API 金鑰。
您可以在 [Lakera 網站](https://www.lakera.ai/) 註冊免費試用，並按照 [官方快速入門指南](https://docs.lakera.ai/docs/quickstart) 取得 API 金鑰並設定您的專案。
如果您無法透過官方網站取得 API 金鑰，請聯繫當地的 [Check Point 合作夥伴](https://partnerlocator.checkpoint.com/) 尋求協助。

### 主要功能

*   **全面威脅篩選**：整合 Lakera Guard 強大的 API，檢測並標記各種 AI 特有威脅，例如使用者輸入及 AI 模型輸出中的提示詞注入、資料洩露 (PII) 及有害內容。
*   **靈活配置**：允許使用者透過可選參數自訂篩選行為，如 `project_id`、`payload`（用於詳細檢測資訊）、`breakdown`（用於標記決策）、`metadata` 及 `dev_info`。
*   **清晰且可操作的輸出**：提供直觀的 `true` 或 `false` 布林值以指示是否檢測到威脅，同時提供來自 Lakera Guard 的完整原始 JSON 回應以供詳細分析。

### 使用方法

#### 安裝
從 `Dify Marketplace`、`GitHub` 或 `Local` 來源安裝本外掛，並設定您的 API 金鑰。

![img1](../_assets/README_assets/installation.png)

#### 將外掛新增至 Chatflow
您可以將本外掛新增至輸入 (Input) 或輸出 (Output) 流程中，以檢測可疑內容。您必須同時使用 `條件節點 (Conditional Node)` 進行判斷：如果檢測結果為 `true`，則終止流程；如果檢測結果為 `false`，則繼續流程。

![img2](../_assets/README_assets/chatflow.png)

外掛設定：

![img3](../_assets/README_assets/input.png)

參數說明如下：

*   **Project ID**：用於篩選的 Lakera Guard 專案 ID。（登入 Lakera 入口網站並建立新專案以取得專案 ID。）
*   **Include Payload**：設為 `true` 以在回應中包含詳細負載資訊 (payload)。
*   **Include Breakdown**：設為 `true` 以在回應中包含標記決策的分解資訊。
*   **Metadata**：包含請求中介資料的 JSON 字串。範例：`'{"user_id": "123"}'`
*   **Developer Info**：設為 `true` 以在回應中包含開發者資訊。

輸出變數：

*   **text**：回傳 `true` 或 `false`。
*   **json**：回傳更詳細的檢測資訊，以便您判斷是哪個政策阻擋了內容。

輸入條件流程：

![img4](../_assets/README_assets/input_condition.png)

Chatflow 展示：
![img5](../_assets/README_assets/chat.png)
