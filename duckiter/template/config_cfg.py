config_cfg = \
"""
[project_info]
project_name = {{ project_name }}
python_version= {config['python_version']}
is_migration= {config['is_migration']}

[project_server]
project_server = {{ project_server }}
"""