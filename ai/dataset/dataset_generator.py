from typing import integer, List, Tuple
import random
import json

from .room_data import Room
from .room_generator import generate_room, generate_lights, save_room_to_string


def generate_random_size() -> Tuple(integer, integer):
    length = random.randint(50, 2000)
    width = random.randint(50, length)
    return length, width


def generate_random_type() -> str:
    return random.choice(["1", "2"])


def generate_dataset(num_rooms) -> List[Room]:
    dataset = []
    for i in range(num_rooms):
        length, width = generate_random_size()
        room = generate_room(length, width)
        room_type = generate_random_type()
        lights_pattern, lights_layout = generate_lights(room, room_type)
        room["lights"] = lights_pattern
        room_pattern = save_room_to_string(room)
        room["lights"] = lights_layout
        room_layout = save_room_to_string(room)

        dataset.append(
            {
                "conversations": [
                    {
                        "from": "human",
                        "value": f"Can you fill the room area with the same light pattern in: \\n{room_pattern}",
                    },
                    {
                        "from": "assistant",
                        "value": f"{room_layout}",
                    },
                ]
            }
        )
    return dataset


if __name__ == "__main__":
    dataset = generate_dataset(2)

    # save dataset to a json file
    with open("dataset.json", "w") as f:
        json.dump(dataset, f)
