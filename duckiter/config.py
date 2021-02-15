def get_config() -> dict:
    """
            get config from user ( CLI )

    """
    python_version = input(
        "please enter python version that you need insert in your Docker ? ( blank will consider as 3.8) : ")

    python_version = python_version if python_version else '3.8'

    is_migration = input(
        "Do you want add 'python manage.py migrate' in your docker file ? (y/n) : ")

    is_migration = True if is_migration == 'y' else False

    config = {
        'python_version': python_version,
        'is_migration': is_migration,

    }
    return config
