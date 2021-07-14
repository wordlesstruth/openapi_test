import connexion
import six

from openapi_server.models.order import Order
from openapi_server import util


def delete_order(order_id):
    """Delete purchase order by ID

    For valid response try integer IDs with positive integer value.         Negative or non-integer values will generate API errors

    :param order_id: ID of the order that needs to be deleted
    :type order_id: int

    :rtype: None
    """
    return 'do some magic!'


def get_inventory():
    """Returns pet inventories by status

    Returns a map of status codes to quantities


    :rtype: Dict[str, int]
    """
    return 'do some magic!'


def get_order_by_id(order_id):
    """Find purchase order by ID

    For valid response try integer IDs with value &gt;&#x3D; 1 and &lt;&#x3D; 10.         Other values will generated exceptions

    :param order_id: ID of pet that needs to be fetched
    :type order_id: int

    :rtype: Order
    """
    return 'do some magic!'


def place_order(body):
    """Place an order for a pet



    :param body: order placed for purchasing the pet
    :type body: dict | bytes

    :rtype: Order
    """
    return 'do some magic!'
