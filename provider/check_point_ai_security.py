import requests
from typing import Any

from dify_plugin import ToolProvider
from dify_plugin.errors.tool import ToolProviderCredentialValidationError


class ChkpLakeraForDifyProvider(ToolProvider):
    
    def _validate_credentials(self, credentials: dict[str, Any]) -> None:
        api_key = credentials.get('lakera_guard_api_key')
        if not api_key:
            raise ToolProviderCredentialValidationError("Lakera Guard API Key is required.")

        try:
            # Use the /v2/guard endpoint for a more reliable validation check.
            # A successful response (like 200 OK) indicates a valid key,
            # while a 401 Unauthorized specifically points to an invalid key.
            response = requests.post(
                "https://api.lakera.ai/v2/guard",
                headers={
                    "Authorization": f"Bearer {api_key}",
                    "Content-Type": "application/json"
                },
                json={"messages": [{"role": "user", "content": "Dify plugin validation"}]}
            )
            # Check for specific error codes, providing a more informative message if the key is explicitly unauthorized.
            if response.status_code == 401:
                raise ToolProviderCredentialValidationError("The provided Lakera Guard API Key is invalid or has expired.")
            
            response.raise_for_status()  # Raise an exception for other bad status codes (4xx or 5xx)
        except requests.exceptions.RequestException as e:
            # This will catch network errors and the exceptions raised by raise_for_status()
            raise ToolProviderCredentialValidationError(f"Failed to validate Lakera Guard API Key: {e}")

    #########################################################################################
    # If OAuth is supported, uncomment the following functions.
    # Warning: please make sure that the sdk version is 0.4.2 or higher.
    #########################################################################################
    # def _oauth_get_authorization_url(self, redirect_uri: str, system_credentials: Mapping[str, Any]) -> str:
    #     """
    #     Generate the authorization URL for chkp-lakera-for-dify OAuth.
    #     """
    #     try:
    #         """
    #         IMPLEMENT YOUR AUTHORIZATION URL GENERATION HERE
    #         """
    #     except Exception as e:
    #         raise ToolProviderOAuthError(str(e))
    #     return ""
        
    # def _oauth_get_credentials(
    #     self, redirect_uri: str, system_credentials: Mapping[str, Any], request: Request
    # ) -> Mapping[str, Any]:
    #     """
    #     Exchange code for access_token.
    #     """
    #     try:
    #         """
    #         IMPLEMENT YOUR CREDENTIALS EXCHANGE HERE
    #         """
    #     except Exception as e:
    #         raise ToolProviderOAuthError(str(e))
    #     return dict()

    # def _oauth_refresh_credentials(
    #     self, redirect_uri: str, system_credentials: Mapping[str, Any], credentials: Mapping[str, Any]
    # ) -> OAuthCredentials:
    #     """
    #     Refresh the credentials
    #     """
    #     return OAuthCredentials(credentials=credentials, expires_at=-1)
