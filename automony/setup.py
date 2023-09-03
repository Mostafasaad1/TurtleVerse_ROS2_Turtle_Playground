from setuptools import find_packages, setup

package_name = 'automony'

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
    maintainer='mox',
    maintainer_email='mostafa.saad@ejust.edu.eg',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
        	'catch = automony.catch:main',
        	'client_spawn = automony.client_spawn:main',
        	'kill = automony.kill:main',
        	'pub_turtle = automony.pub_turtle:main',
            'random_Target = automony.random_Target:main',
        ],
    },
)
