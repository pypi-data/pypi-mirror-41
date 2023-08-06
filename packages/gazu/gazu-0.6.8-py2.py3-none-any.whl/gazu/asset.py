from .helpers import normalize_model_parameter

from . import client
from . import project as gazu_project

from .sorting import sort_by_name

from .cache import cache


@cache
def all_assets_for_open_projects():
    """
    Retrieve all assets stored in the database or for open projects.
    """
    all_assets = []
    for project in gazu_project.all_open_projects():
        all_assets.extend(all_assets_for_project(project))
    return sort_by_name(all_assets)


@cache
def all_assets_for_project(project):
    """
    Retrieve all assets stored in the database or for given project.
    """
    project = normalize_model_parameter(project)

    if project is None:
        return sort_by_name(client.fetch_all("assets/all"))
    else:
        return sort_by_name(
            client.fetch_all("projects/%s/assets" % project["id"])
        )


@cache
def all_assets_for_episode(episode):
    """
    Retrieve all assets stored in the database or for given project.
    """
    episode = normalize_model_parameter(episode)

    return sort_by_name(
        client.fetch_all("assets?source_id=%s" % episode["id"])
    )


@cache
def all_assets_for_shot(shot):
    """
    Retrieve all assets casted in given shot.
    """
    shot = normalize_model_parameter(shot)
    return sort_by_name(client.fetch_all("shots/%s/assets" % shot["id"]))


@cache
def all_assets_for_project_and_type(project, asset_type):
    """
    Retrieve all assets for given project and given asset type.
    """
    project = normalize_model_parameter(project)
    asset_type = normalize_model_parameter(asset_type)

    project_id = project["id"]
    asset_type_id = asset_type["id"]
    path = "projects/{project_id}/asset-types/{asset_type_id}/assets"
    path = path.format(project_id=project_id, asset_type_id=asset_type_id)

    assets = client.fetch_all(path)
    return sort_by_name(assets)


@cache
def get_asset_by_name(project, name, asset_type=None):
    """
    Retrieve first asset matching given name.
    """
    project = normalize_model_parameter(project)

    if asset_type is None:
        path = "assets/all?project_id=%s&name=%s" % (project["id"], name)
    else:
        asset_type = normalize_model_parameter(asset_type)
        path = "assets/all?project_id=%s&name=%s&entity_type_id=%s" % (
            project["id"], name, asset_type["id"]
        )
    return client.fetch_first(path)


@cache
def get_asset(asset_id):
    """
    Retrieve given asset.
    """
    return client.fetch_one('assets', asset_id)


def new_asset(project, asset_type, name, description="", extra_data={}):
    """
    Create a new asset in the database.
    """
    project = normalize_model_parameter(project)
    asset_type = normalize_model_parameter(asset_type)

    data = {
        "name": name,
        "description": description,
        "data": extra_data
    }

    asset = get_asset_by_name(project, name, asset_type)
    if asset is None:
        asset = client.post("data/projects/%s/asset-types/%s/assets/new" % (
            project["id"],
            asset_type["id"]
        ), data)
    return asset


def update_asset(asset):
    """
    Save given asset data into the API.
    """
    return client.put('data/entities/%s' % asset["id"], asset)


def remove_asset(asset):
    """
    Remove given asset from database.
    """
    asset = normalize_model_parameter(asset)
    return client.delete("data/assets/%s" % asset["id"])


def new_asset_type(name):
    """
    Create a new asset type in the database.
    """
    data = {
        "name": name
    }
    asset_type = client.fetch_first("entity-types?name=%s" % name)
    if asset_type is None:
        asset_type = client.create("entity-types", data)
    return asset_type


def update_asset_type(asset_type):
    """
    Modify asset type name in the database.
    """
    data = {
        "name": asset_type["name"]
    }
    return client.put("data/asset-types/%s" % asset_type["id"], data)


def remove_asset_type(asset_type):
    """
    Remove given asset type from database.
    """
    asset_type = normalize_model_parameter(asset_type)
    return client.delete("data/asset-types/%s" % asset_type["id"])


@cache
def all_asset_types():
    """
    Retrieve all asset types stored in the database.
    """
    return sort_by_name(client.fetch_all("asset-types"))


@cache
def all_asset_types_for_project(project):
    """
    Retrieve all asset types from assets listed in given project.
    """
    return sort_by_name(client.fetch_all(
        "projects/%s/asset-types" % project["id"]
    ))


@cache
def all_asset_types_for_shot(shot):
    """
    Retrieve all asset types from assets casted in given shot.
    """
    return sort_by_name(client.fetch_all(
        "shots/%s/asset-types" % shot["id"]
    ))


@cache
def get_asset_type(asset_id):
    """
    Retrieve given asset type.
    """
    return client.fetch_one('asset-types', asset_id)


@cache
def get_asset_type_by_name(name):
    """
    Retrieve first asset matching given name.
    """
    return client.fetch_first("entity-types?name=%s" % name)


@cache
def get_asset_instance(asset_instance_id):
    """
    Retrieve given asset instance
    """
    return client.fetch_one("asset-instances", asset_instance_id)


@cache
def all_shot_asset_instances_for_asset(asset):
    """
    Retrieve all asset instances existing for a given asset.
    """
    asset = normalize_model_parameter(asset)
    return client.fetch_all("assets/%s/shot-asset-instances" % asset['id'])


def enable_asset_instance(asset_instance):
    """
    Set active flag of given asset instance to True.
    """
    asset_instance = normalize_model_parameter(asset_instance)
    data = {"active": True}
    return client.put("asset-instances/%s" % asset_instance["id"], data)


def disable_asset_instance(asset_instance):
    """
    Set active flag of given asset instance to False.
    """
    asset_instance = normalize_model_parameter(asset_instance)
    data = {"active": False}
    return client.put("asset-instances/%s" % asset_instance["id"], data)


@cache
def all_scene_asset_instances_for_asset(asset):
    """
    Retrieve all scene asset instances existing for a given asset.
    """
    asset = normalize_model_parameter(asset)
    return client.fetch_all("assets/%s/scene-asset-instances" % asset['id'])


@cache
def all_asset_instances_for_shot(shot):
    """
    Retrieve all asset instances existing for a given shot.
    """
    return client.fetch_all("shots/%s/asset-instances" % shot['id'])


@cache
def all_asset_instances_for_asset(asset):
    """
    Retrieve all asset instances existing for a given asset.
    """
    asset = normalize_model_parameter(asset)
    return client.fetch_all("assets/%s/asset-asset-instances" % asset['id'])


def new_asset_asset_instance(asset, asset_to_instantiate, description=""):
    """
    Creates a new asset instance for given asset. The instance number is
    automatically generated (increment highest number).
    """
    asset = normalize_model_parameter(asset)
    asset_to_instantiate = normalize_model_parameter(asset_to_instantiate)
    data = {
        "asset_to_instantiate_id": asset_to_instantiate["id"],
        "description": description
    }
    return client.post(
        "data/assets/%s/asset-asset-instances" % asset["id"],
        data
    )
