import json

import requests


class crtsh(object):
    """
    CertSpy is a Python client for the crt.sh website to retrieve subdomains information.
    ref: https://github.com/santosomar/certspy/blob/main/certspy/certspy.py
    """

    def search(self, domain: str, wildcard=True, expired=True, timeout=10):
        base_url = "https://crt.sh/?q={}&output=json"
        if not expired:
            base_url = base_url + "&exclude=expired"
        if wildcard and "%" not in domain:
            domain = "%.{}".format(domain)
        url = base_url.format(domain)

        req = requests.get(url, timeout=timeout)
        if req.ok:
            content = req.content.decode('utf-8')
            try:
                data = json.loads(content)
                return data
            except ValueError:
                data = json.loads("[{}]".format(content.replace('}{', '},{')))
                return data
            except Exception as err:
                print(f"Error retrieving information: {err}")
        return None

    def format_results(self, data, common_name_only=False):
        """
        Format the results based on the common_name_only flag.

        :param data: List of certificate data objects.
        :param common_name_only: Whether to return only common names. Default is False.
        :return: Formatted results (list of common names or full data).
        """
        if common_name_only:
            return list(set(item['common_name'] for item in data))
        return data
