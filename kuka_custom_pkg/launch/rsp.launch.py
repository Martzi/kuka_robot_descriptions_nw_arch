from moveit_configs_utils import MoveItConfigsBuilder
from moveit_configs_utils.launches import generate_rsp_launch


def generate_launch_description():
    moveit_config = MoveItConfigsBuilder("kr10_r1100_2", package_name="kuka_custom_pkg").to_moveit_configs()
    return generate_rsp_launch(moveit_config)
