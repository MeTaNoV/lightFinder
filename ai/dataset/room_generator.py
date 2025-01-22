import json
from typing import List

from room_data import Coordinate, Room

MIN_LIGHT_SPACING_1 = 10
MIN_LIGHT_SPACING_2 = 15
MIN_BORDER_MARGIN_1 = 10
MIN_BORDER_MARGIN_2 = 20


def generate_room(length: float, width: float) -> Room:
    """
    Generates a dictionary representation of a room with the given length and width.

    Args:
        length: The length of the room.
        width: The width of the room.

    Returns:
        A dictionary representing the room with four coordinates oriented clockwise
    """
    coordinates = [
        Coordinate(x=0, y=0),  # Bottom-left
        Coordinate(x=0, y=width),  # Top-left
        Coordinate(x=length, y=width),  # Top-right
        Coordinate(x=length, y=0),  # Bottom-right
    ]

    room = {
        "length": length,
        "width": width,
        "coordinates": coordinates,
    }

    return Room(**room)


def generate_lights(room: Room, room_type: str) -> tuple[List[Coordinate], List[Coordinate]]:
    """
    Generates a list of lights for the given room based on the room type.

    Args:
        room: A dictionary representing the room.
        room_type: The type of the room (e.g., "living_room", "bedroom").

    Returns:
        A tuple composed of a light pattern and the light layout
    """
    length = room.length
    width = room.width
    light_pattern = []
    light_layout = []

    if room_type == "1":
        # for this configuration, we place the light in a uniform pattern to have one light
        # approximately every MIN_LIGHT_SPACING unit so that the spacing between lights and walls are equal
        length_light_count = int((length - 2 * MIN_BORDER_MARGIN_1) / MIN_LIGHT_SPACING_1) + 1
        width_light_count = int((width - 2 * MIN_BORDER_MARGIN_1) / MIN_LIGHT_SPACING_1) + 1
        length_light_interval = (length - 2 * MIN_BORDER_MARGIN_1) / length_light_count
        width_light_interval = (width - 2 * MIN_BORDER_MARGIN_1) / width_light_count

        for i in range(0, length_light_count + 1):
            for j in range(0, width_light_count + 1):
                x = MIN_BORDER_MARGIN_1 + i * length_light_interval
                y = MIN_BORDER_MARGIN_1 + j * width_light_interval
                # we oinly add lights to the pattern the first few examples
                if i < 2:
                    light_pattern.append(Coordinate(x, y))
                light_layout.append(Coordinate(x, y))
    elif room_type == "2":
        # for this configuration, we place the light on the border of the room with a distance
        # of MIN_BORDER_MARGIN_2 unit and spaced by MIN_LIGHT_SPACING_2 units minimum
        length_light_count = int((length - 2 * MIN_BORDER_MARGIN_2) / MIN_LIGHT_SPACING_2) + 1
        width_light_count = int((width - 2 * MIN_BORDER_MARGIN_2) / MIN_LIGHT_SPACING_2) + 1
        length_light_interval = (length - 2 * MIN_BORDER_MARGIN_2) / length_light_count
        width_light_interval = (width - 2 * MIN_BORDER_MARGIN_2) / width_light_count

        for i in range(0, length_light_count + 1):
            for j in range(0, width_light_count + 1):
                x = MIN_BORDER_MARGIN_2 + i * length_light_interval
                y = MIN_BORDER_MARGIN_2 + j * width_light_interval

                if i == 0:
                    light_pattern.append(Coordinate(x, y))
                    light_layout.append(Coordinate(x, y))
                elif i == (length_light_count):
                    light_layout.append(Coordinate(x, y))
                elif j == 0 or j == (width_light_count):
                    if i < 2:
                        light_pattern.append(Coordinate(x, y))
                    light_layout.append(Coordinate(x, y))
    else:
        print(f"Error: Unknown room type '{room_type}'.")

    return light_pattern, light_layout


def save_room_to_file(room: Room, filename: str) -> None:
    """
    Saves the given room to a JSON file with the specified filename.

    Args:
        room: A dictionary representing the room.
        filename: The name of the file to save the room to.
    """
    with open(filename, "w") as file:
        json.dump(room.to_dict(), file)


def save_room_to_string(room: Room) -> str:
    """
    Saves the given room to a JSON string.

    Args:
        room: A dictionary representing the room.
        filename: The name of the file to save the room to.
    """
    return json.dumps(room.to_dict())


if __name__ == "__main__":
    # try:
    #     length = float(sys.argv[1])
    #     width = float(sys.argv[2])
    #     room_type = sys.argv[3]
    # except ValueError:
    #     print("Error: Length and width must be numbers.")
    #     sys.exit(1)
    length = 100
    width = 60
    room_type = "2"

    room = generate_room(length, width)
    lights_pattern, lights_layout = generate_lights(room, room_type)
    room["lights"] = lights_pattern
    print(json.dumps(room, indent=2))
    save_room_to_file(room, "room_pattern.json")
    room["lights"] = lights_layout
    print(json.dumps(room, indent=2))
    save_room_to_file(room, "room_layout.json")
