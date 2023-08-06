from urllib.parse import urljoin

import requests
from .exceptions import PortainerError


class Portainer:
    FROM_VERSION = (0, 0)
    URL_STACKS = "api/endpoints/1/stacks"
    URL_STACK = "api/stacks/{stack_id}"

    def __init__(self, host: str):
        self.token = None
        self.host = host

    def login(self, username: str, password: str):
        """
        Logs in to the portainer API
        :param username:  Portainer username
        :param password: Portainer password
        :return: True if authentication was successful, False if not
        """
        data = {"Username": username, "Password": password}
        r = self.request("api/auth", method="POST", data=data)
        self.token = r.get("jwt")
        return bool(self.token)

    def get_stacks(self) -> dict:
        """
        Get all stacks on this portainer
        :return: a list of dicts
        """
        return self.request(self.URL_STACKS)

    def get_stack(self, stack_id) -> dict:
        """
        Get the stack by Id. Id might be a string or an int depending
        on the Portainer version
        :param stack_id:
        :return: A dict containing information about the stack
        :raises LookupError:
        """
        return self.request(self.URL_STACK.format(stack_id=stack_id))

    def stack_with_name(self, name) -> dict:
        stacks = self.get_stacks()
        for stack in stacks:
            if stack.get("Name") == name:
                return stack
        raise LookupError("No stack with name '{}'".format(name))

    def get_env_vars(self, stack_id) -> dict:
        response = self.get_stack(stack_id)
        return {item["name"]: item["value"] for item in response["Env"]}

    def update_stack(
        self,
        stack_id: str,
        stack_file_content: str,
        env_vars: dict = None,
        prune: bool = False,
    ) -> dict:
        url = self.URL_STACK.format(stack_id=stack_id)
        data = {
            "StackFileContent": stack_file_content,
            "Prune": prune,
            "Env": [{"name": k, "value": v} for k, v in env_vars.items()],
        }
        return self.request(url, method="PUT", data=data)

    def update_stack_with_file(
        self,
        stack_id: str,
        stack_file_path: str,
        env_vars: dict = None,
        prune: bool = False,
    ) -> dict:
        with open(stack_file_path, "r") as f:
            stack_file = f.read()
        return self.update_stack(stack_id, stack_file, env_vars=env_vars, prune=prune)

    def endpoints(self):
        return self.request("api/endpoints")

    def request(self, path: str, method: str = "GET", data: dict = None) -> dict:
        url = urljoin(self.host, path)
        headers = {}
        if self.token:
            headers["Authorization"] = "Bearer {}".format(self.token)
        response = requests.request(method, url, json=data, headers=headers)
        if response.status_code == requests.codes.ok:
            return response.json()
        else:
            raise PortainerError(response=response)
