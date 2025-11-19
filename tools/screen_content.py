import json
import requests
from collections.abc import Generator
from typing import Any

from dify_plugin import Tool
from dify_plugin.entities.invoke_message import InvokeMessage
from dify_plugin.errors.tool import ToolProviderCredentialValidationError

class ScreenContentTool(Tool):
    def _invoke(self, tool_parameters: dict[str, Any]) -> Generator[InvokeMessage]:
        api_key = self.runtime.credentials.get('lakera_guard_api_key')
        if not api_key:
            raise ToolProviderCredentialValidationError("Lakera Guard API Key not found.")

        user_input = tool_parameters.get('user_input')
        if not user_input:
            raise Exception("User input parameter is required.")

        # Construct the messages payload from the raw user_input string
        messages = [{"role": "user", "content": user_input}]

        payload = {
            "messages": messages
        }

        # Add optional parameters to the payload if they exist
        optional_params = ['project_id', 'payload', 'breakdown', 'dev_info']
        for param in optional_params:
            if param in tool_parameters:
                payload[param] = tool_parameters[param]
        
        if 'metadata' in tool_parameters:
            try:
                payload['metadata'] = json.loads(tool_parameters['metadata'])
            except json.JSONDecodeError:
                raise Exception("Invalid JSON format for metadata.")

        try:
            response = requests.post(
                "https://api.lakera.ai/v2/guard",
                headers={
                    "Authorization": f"Bearer {api_key}",
                    "Content-Type": "application/json"
                },
                json=payload
            )
            response.raise_for_status()
            
            # Get the JSON response
            result_json = response.json()

            # Extract the 'flagged' value and create a text summary
            is_flagged = result_json.get('flagged', False) # Default to False if not present
            summary_text = str(is_flagged).lower()
            
            # Yield the text summary first
            yield self.create_text_message(summary_text)
            # Then yield the full JSON response
            yield self.create_json_message(result_json)

        except requests.exceptions.RequestException as e:
            raise Exception(f"API request failed: {e}")
