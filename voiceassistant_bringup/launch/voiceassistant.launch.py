from launch import LaunchDescription
from launch_ros.actions import Node

from launch.actions import TimerAction


def generate_launch_description():

    ld = LaunchDescription()

    stt_node = Node(
        package="speech_to_text",
        executable="stt"
    )
    
    tts_node = Node(
        package="text_to_speech", 
        executable="tts"
    )

    nlu_node = Node(
        package="nl_understanding",
        executable="nlu",
    )

    # Timing
    delayed_tts = TimerAction(period=2.0, actions=[tts_node])
    delayed_nlu =  TimerAction(period=1.0, actions=[nlu_node])

    ld.add_action(stt_node)
    ld.add_action(delayed_tts)
    ld.add_action(delayed_nlu)

    return ld
