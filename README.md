# Check Point AI Security Dify Plugin

**Author:** Birdlex Wu

**Version:** 0.0.1

**Type:** tool

[简中文档](https://github.com/birdlex/chkp-lakera-for-dify/blob/main/readme/README_zh_cn.md)

[繁中文檔](https://github.com/birdlex/chkp-lakera-for-dify/blob/main/readme/README_zh_tw.md)

[日本語文書](https://github.com/birdlex/chkp-lakera-for-dify/blob/main/readme/README_ja.md)

### Overview
This plugin for Dify ("the plugin") provides an interface to the Lakera Guard API, **a product of Check Point Software Technologies**. It is designed to secure your AI applications by screening user inputs and model responses for a wide range of threats, including prompt injections, toxic content, and PII (Personally Identifiable Information) leakage.

### IMPORTANT NOTICE BEFORE USE

**API Key Security:** You are responsible for the security of your Lakera Guard API Key. Do not expose it in client-side code or commit it to version control.

**Service Disclaimer:** This plugin is an interface to the Lakera Guard API. The performance, accuracy, and availability of the security screening are subject to Lakera's service terms. The author of this plugin is not responsible for the results provided by the Lakera Guard API.

**License Disclaimer:** The software is provided "as is," and the author disclaims all warranties with regard to this software, including all implied warranties of merchantability and fitness. In no event shall the author be liable for any special, direct, indirect, or consequential damages or any damages whatsoever resulting from loss of use, data or profits, whether in an action of contract, negligence or other tortious action, arising out of or in connection with the use or performance of this software.

### Prerequisites

To use this plugin, you will need a Lakera Guard API Key.
You can sign up for a free trial on the [Lakera website](https://www.lakera.ai/) and follow the [official quickstart guide](https://docs.lakera.ai/docs/quickstart) to get your API key and set up your project.
If you are unable to obtain an API key through the official website, please contact your local [Check Point Partner](https://partnerlocator.checkpoint.com/) for assistance.

### Main Features

*   **Comprehensive Threat Screening**: Integrates with Lakera Guard's powerful API to detect and flag various AI-specific threats, such as prompt injections, data leakage (PII), and harmful content in both user inputs and AI model outputs.
*   **Flexible Configuration**: Allows users to customize screening behavior through optional parameters like `project_id`, `payload` (for detailed detections), `breakdown` (for flagging decisions), `metadata`, and `dev_info`.
*   **Clear & Actionable Output**: Provides a straightforward `true` or `false` boolean indicating if a threat was detected, alongside the complete raw JSON response from Lakera Guard for detailed analysis.

### How to Use

#### Installation
Install the plugin from the `Dify Marketplace`, `GitHub`, or `Local` sources, and configure your API key.

![img1](_assets/README_assets/installation.png)

#### Add the Plugin to Chatflow
You can add this plugin to either the Input or Output flow to detect suspicious content. You must also use a `Conditional Node` to make a determination: if the detection result is `true`, terminate the flow; if the detection result is `false`, continue the flow.

![img2](_assets/README_assets/chatflow.png)

Plugin settings:

![img3](_assets/README_assets/input.png)

The parameters are described below:

*   **Project ID**: The ID of the Lakera Guard project to use for screening. (Log in to the Lakera portal and create a new project to get a project ID.)
*   **Include Payload**: Set to `true` to include the payload in the response.
*   **Include Breakdown**: Set to `true` to include a breakdown of the flagging decision in the response.
*   **Metadata**: A JSON string containing metadata for the request. Example: `'{"user_id": "123"}'`
*   **Developer Info**: Set to `true` to include developer information in the response.

The output variables:

*   **text**: Returns `true` or `false`.
*   **json**: Returns more detailed detection info so you can determine which policy blocked it.

The input condition flow:

![img4](_assets/README_assets/input_condition.png)

Chatflow Demo:
![img5](_assets/README_assets/chat.png)