from setuptools import setup

package_name = 'ros2_chat'

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
    maintainer='sreeram3927',
    maintainer_email='sreeram292004@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'msg_subscriber = ros2_chat.msg_subscriber:main',
            'msg_publisher = ros2_chat.msg_publisher:main'
        ],
    },
)
