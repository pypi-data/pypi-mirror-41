from pkg_resources import get_distribution


def version():
    return get_distribution("cone")
