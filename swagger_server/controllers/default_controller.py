import connexion
import six

from swagger_server.models.playbook_input import PlaybookInput  # noqa: E501
from swagger_server.models.playbook_result import PlaybookResult  # noqa: E501
from swagger_server import util
from ansible_runner import run_playbook


def playbook_post(body=None):  # noqa: E501
    """run a playbook

    Run a playbook with relevant options similar to ansible-playbook  # noqa: E501

    :param body: Playbook to run with options
    :type body: dict | bytes

    :rtype: PlaybookResult
    """
    if connexion.request.is_json:
        body = PlaybookInput.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
