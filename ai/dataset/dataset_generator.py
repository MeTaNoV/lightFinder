from typing import List, Tuple
import random
import json

from room_data import Room
from room_generator import generate_room, generate_lights, save_room_to_string
from image_generator import generate_room_image


def generate_random_size() -> Tuple[int, int]:
    length = random.randint(100, 200)
    width = random.randint(80, length)
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
        room.lights = lights_pattern
        generate_room_image(
            room,
            f"ai/dataset/generated/room_{i}_{length}_{width}_{room_type}_pattern.png",
        )
        with open(
            f"ai/dataset/generated/room_{i}_{length}_{width}_{room_type}_pattern.json",
            "w",
        ) as f:
            json.dump(room.to_dict(), f)
        room_pattern = save_room_to_string(room)
        room.lights = lights_layout
        generate_room_image(
            room,
            f"ai/dataset/generated/room_{i}_{length}_{width}_{room_type}_layout.png",
        )
        with open(
            f"ai/dataset/generated/room_{i}_{length}_{width}_{room_type}_layout.json",
            "w",
        ) as f:
            json.dump(room.to_dict(), f)
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
    dataset = generate_dataset(300)

    # save dataset to a json file
    with open("ai/dataset/generated/dataset.json", "w") as f:
        json.dump(dataset, f)
