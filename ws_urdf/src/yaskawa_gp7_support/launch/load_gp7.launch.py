from launch import LaunchDescription
from launch_ros.actions import Node
from launch.substitutions import Command
from ament_index_python.packages import get_package_share_directory
import os

def generate_launch_description():
    # Get the path to your package
    pkg_path = get_package_share_directory('yaskawa_gp7_support')

    # Join the package path with the relative path to your xacro file
    xacro_file_path = os.path.join(pkg_path, '/home/adm-vsp-dv/ws_urdf/src/yaskawa_gp7_support/urdf/gp7_macro.xacro')

    robot_description_content = Command(['xacro ', xacro_file_path])

    return LaunchDescription([
        Node(
            package='rviz2',
            executable='rviz2',
            name='rviz2',
            output='screen',
            parameters=[{'robot_description': robot_description_content}],
            arguments=['-d', '/home/adm-vsp-dv/ws_urdf/src/yaskawa_gp7_support/config/test.rviz'],
            env={'QT_QPA_PLATFORM': 'xcb'}
        ),
    ])
