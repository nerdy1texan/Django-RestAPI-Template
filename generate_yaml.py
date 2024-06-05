import yaml
import os

def requirements_to_yaml(requirements_file, yaml_file):
    with open(requirements_file, 'r') as f:
        packages = f.readlines()

    packages = [pkg.strip() for pkg in packages]

    env = {
        'name': 'your_environment_name',
        'channels': ['defaults'],
        'dependencies': [
            'python=3.x',  # Replace with your Python version
        ]
    }

    for package in packages:
        env['dependencies'].append(package)

    with open(yaml_file, 'w') as f:
        yaml.dump(env, f, default_flow_style=False)

if __name__ == "__main__":
    requirements_file = 'requirements.txt'
    yaml_file = 'environment.yaml'
    requirements_to_yaml(requirements_file, yaml_file)
    print(f'Environment file {yaml_file} created successfully.')
