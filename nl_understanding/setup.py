from setuptools import setup

package_name = 'nl_understanding'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='scarc_industries',
    maintainer_email='ale-scarciglia@libero.it',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
        "nlu = nl_understanding.nl_understanding:main",
        "client = nl_understanding.tcp_client:main"
        ],
    },
)
