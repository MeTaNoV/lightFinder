from PIL import Image, ImageDraw
from room_data import Room
from room_generator import load_room_from_file


def generate_room_image(room: Room, filename: str) -> None:
    # Room dimensions in pixels
    length_px = room.length * 4
    width_px = room.width * 4

    # Create blank image (white background)
    img = Image.new("RGB", (int(length_px), int(width_px)), "white")
    draw = ImageDraw.Draw(img)

    # Draw room borders (black)
    draw.rectangle([(0, 0), (length_px - 1, width_px - 1)], outline="black", width=4)

    # Draw lights (yellow circles with black outline)
    for coord in room.lights:
        x_px = coord.x * 4  # Convert units to pixels
        y_px = (room.width - coord.y) * 4  # Flip y-axis for image coordinates
        draw.ellipse([(x_px - 5, y_px - 5), (x_px + 5, y_px + 5)], fill="#FFD700", outline="black")  # Yellow

    # Save the image
    img.save(filename)


if __name__ == "__main__":
    room_0_176_146_2_phi4_2 = load_room_from_file("ai/dataset/generated/room_0_176_146_2_phi4-2.json")
    generate_room_image(room_0_176_146_2_phi4_2, "ai/dataset/generated/room_0_176_146_2_phi4-2.png")
