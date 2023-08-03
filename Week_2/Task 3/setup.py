from setuptools import find_packages, setup

package_name = 'project_altair_controller'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='shakib',
    maintainer_email='shakib@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            "node_publisher = project_altair_controller.node_publisher:main",
            "node_subscriber = project_altair_controller.node_subscriber:main",
        ],
    },
)
