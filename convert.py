from PIL import Image
ascii_chars = [' ', '.', ':', '-', '=', '+', '*', '#', '%', '@', 'W', 'M', '$', 'O', '8', 'B', 'D', 'K', 'H', 'N', 'Q', 'U', 'Y', 'X', 'A', 'Z', '0', '1', '2', '3', '4', '5', '6', '7', '9', 'C', 'G', 'P', 'S', 'V', 'f', 't', 'i', 'L', 'J', 'T', 'I', 'Y', 'R', 's', 'h', 'd', 'o', 'a', 'u', 'n', 'm', 'w', 'q', 'p', 'b', 'g', 'e', 'r', 'y', 'x', 'c', 'l', 'k', 'j', 'z', 'v', 'U', 'X', 'K', 'N', 'Q', 'E', 'B', 'D', 'H', 'M', 'W', 'O', 'A', 'Y', 'R', 'P', 'G', 'C', 'S', 'F', 'T', 'J', 'L', 'V', 'u', 'n', 'm', 'o', 'w', 'v', 'a', 'e', 'b', 'g', 'r', 'y', 'x', 'c', 'l', 'k', 'j', 'z', 't', 'i', 's', 'h', 'd', 'p', 'q', 'f']
image = Image.open("pic.png").convert('L')
width, height = image.size
new_width = min(width, 100)
aspect_ratio = height/width
new_height = int(aspect_ratio * new_width * 0.5)
image = image.resize((new_width, new_height))
ascii_art = ''
for y in range(new_height):
    for x in range(new_width):
        pixel_value = image.getpixel((x, y))
        char_index = int(pixel_value/25)
        if char_index >= len(ascii_chars):
            char_index = len(ascii_chars) - 1
        ascii_art += ascii_chars[char_index]
    ascii_art += '\n'
print(ascii_art)