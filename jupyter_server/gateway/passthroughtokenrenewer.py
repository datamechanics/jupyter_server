import typing as ty

from jupyter_server.gateway.gateway_client import GatewayTokenRenewerBase

class PassthroughTokenRenewer(GatewayTokenRenewerBase):

    def get_token(
            self,
            auth_header_key: str,
            auth_scheme: ty.Union[str, None],
            auth_token: str,
            **kwargs: ty.Any,
    ) -> str:
        print("trying to get token")
        print(kwargs)
        #request = jupyter_server.base.handlers.get_current_request()
        #if request is None:
        #    logging.error("Could not get current request")
        #    return auth_token

        #auth_header_value = get_header_value(request, auth_header_key)
        #if auth_header_value:
        #    try:
        #        # We expect the header value to be of the form "Bearer: XXX"
        #       auth_token = auth_header_value.split(" ", maxsplit=1)[1]
        #    except Exception as e:
        #        logging.error(f"Could not read token from auth header: {str(e)}")

        return auth_token
