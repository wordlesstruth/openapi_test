import connexion
import six

from openapi_server.models.api_response import ApiResponse
from openapi_server.models.pet import Pet
from openapi_server import util


def add_pet(body):
    """Add a new pet to the store



    :param body: Pet object that needs to be added to the store
    :type body: dict | bytes

    :rtype: None
    """
    return 'do some magic!'


def delete_pet(pet_id, api_key=None):
    """Deletes a pet



    :param pet_id: Pet id to delete
    :type pet_id: int
    :param api_key:
    :type api_key: str

    :rtype: None
    """
    return 'do some magic!'


def find_pets_by_status(status):
    """Finds Pets by status

    Multiple status values can be provided with comma separated strings

    :param status: Status values that need to be considered for filter
    :type status: List[str]

    :rtype: List[Pet]
    """
    return 'do some magic!'


def find_pets_by_tags(tags):
    """Finds Pets by tags

    Muliple tags can be provided with comma separated strings. Use         tag1, tag2, tag3 for testing.

    :param tags: Tags to filter by
    :type tags: List[str]

    :rtype: List[Pet]
    """
    return 'do some magic!'


def get_pet_by_id(pet_id):
    """Find pet by ID

    Returns a single pet

    :param pet_id: ID of pet to return
    :type pet_id: int

    :rtype: Pet
    """
    return 'do some magic!'


def update_pet(body):
    """Update an existing pet



    :param body: Pet object that needs to be added to the store
    :type body: dict | bytes

    :rtype: None
    """
    return 'do some magic!'


def update_pet_with_form(pet_id, name=None, status=None):
    """Updates a pet in the store with form data



    :param pet_id: ID of pet that needs to be updated
    :type pet_id: int
    :param name: Updated name of the pet
    :type name: str
    :param status: Updated status of the pet
    :type status: str

    :rtype: None
    """
    return 'do some magic!'


def upload_file(pet_id, additional_metadata=None, file=None):
    """uploads an image



    :param pet_id: ID of pet to update
    :type pet_id: int
    :param additional_metadata: Additional data to pass to server
    :type additional_metadata: str
    :param file: file to upload
    :type file: str

    :rtype: ApiResponse
    """
    return 'do some magic!'
