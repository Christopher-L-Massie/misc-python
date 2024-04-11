# import pyautogui

# import random
# import subprocess
# import json
import time
from evdev import UInput, InputDevice, ecodes as e

# print(
#     "Starting key actions sequence in 5 seconds. Please switch to the target application window."
# )
# time.sleep(5)  # Gives you time to switch to the target window

# Specify the actual device paths for your physical keyboard and mouse
keyboard_device_path = (
    "/dev/input/event4"  # Replace 'eventX' with your keyboard's event number
)
mouse_device_path = (
    "/dev/input/event7"  # Replace 'eventY' with your mouse's event number
)

print("Identifying devices...")
try:
    keyboard_device = InputDevice(keyboard_device_path)
    mouse_device = InputDevice(mouse_device_path)
    print(f"Keyboard identified: {keyboard_device.path}")
    print(f"Mouse identified: {mouse_device.path}")
except Exception as ex:
    print(f"Error identifying devices: {ex}")
    exit(1)

print("Creating a virtual input device based on the keyboard and mouse...")
try:
    ui = UInput.from_device(keyboard_device, name="keyboard-device")
    print(
        f"Virtual device created successfully with capabilities: {ui.capabilities(verbose=True).keys()}"
    )
    print(f"Virtual device file descriptor: {ui.fd}")
except Exception as ex:
    print(f"Error creating virtual device: {ex}")
    exit(1)

sleep_time = 30
print(
    f"Starting key actions sequence in {sleep_time} seconds. Please switch to the target application window."
)
time.sleep(sleep_time)  # Gives you time to switch to the target window

scan_code_space = 39

# Here you can define the sequence of events you want to simulate
events = [
    (e.EV_MSC, e.MSC_SCAN, scan_code_space),
    (e.EV_KEY, e.KEY_SPACE, 1),
    (e.EV_SYN, e.SYN_REPORT, 0),
    (e.EV_MSC, e.MSC_SCAN, scan_code_space),
    (e.EV_KEY, e.KEY_SPACE, 0),
    (e.EV_SYN, e.SYN_REPORT, 0),
]

# Execute the events
for event in events:
    event_type, event_code, value = event
    print(f"Writing event: {event_type}, {event_code}, {value}")
    ui.write(event_type, event_code, value)
    # ui.syn()  # Synchronize after each event

print("Events executed, closing device...")
ui.close()
print("Script completed.")


# cache_file_path = "image_cache.json"

# try:
#     with open(cache_file_path, "r") as cache_file:
#         image_cache = json.load(cache_file)
# except FileNotFoundError:
#     image_cache = {}


# def get_active_window_id():
#     try:
#         return subprocess.check_output(["xdotool", "getactivewindow"]).decode().strip()
#     except Exception as e:
#         print(f"Error getting active window ID: {e}")
#         return None


# def focus_on_window(window_name):
#     subprocess.run(["wmctrl", "-a", window_name])


# def focus_on_window_by_id(window_id):
#     subprocess.run(["xdotool", "windowactivate", window_id])


# def get_window_geometry(window_name, offset_y):
#     try:
#         output = subprocess.check_output(["wmctrl", "-l", "-G"]).decode("utf-8")
#         for line in output.splitlines():
#             if window_name in line:
#                 _, _, x, y, width, height, *_ = line.split(maxsplit=7)
#                 # Adjust the y-coordinate upwards by the offset amount
#                 y_adjusted = int(y) - offset_y
#                 # Optionally, you could also adjust the height if necessary
#                 # height_adjusted = int(height) + offset_y
#                 return int(x), y_adjusted, int(width), int(height)
#     except Exception as e:
#         print(f"Error retrieving window geometry: {e}")
#     return None


# def click_on_image(image_info, region):
#     image_path = image_info["path"]
#     confidence = image_info["confidence"]
#     image_click = image_info["click"]

#     # Check cache first
#     if image_path in image_cache:
#         center_x, center_y = image_cache[image_path]
#         print(f"Using cached coordinates for {image_path}.")
#     else:
#         # Locate image and cache coordinates
#         location = pyautogui.locateOnScreen(
#             image_path, confidence=confidence, region=region
#         )
#         if location:
#             center = pyautogui.center(location)
#             # Convert coordinates to Python native int types before caching
#             center_x, center_y = int(center.x), int(center.y)
#             image_cache[image_path] = [
#                 center_x,
#                 center_y,
#             ]  # Use list to ensure JSON serializability
#             print(
#                 f"Found {image_path} at {location} with confidence {confidence}. Caching coordinates."
#             )
#         else:
#             print(
#                 f"Image {image_path} not found in specified region with confidence {confidence}."
#             )
#             return

#     # Add randomness to click position based on cached coordinates
#     random_x = random.randint(center_x - 10, center_x + 10)
#     random_y = random.randint(center_y - 10, center_y + 10)
#     random_duration = random.uniform(0.1, 0.3)
#     pyautogui.moveTo(random_x, random_y, duration=random_duration)
#     if image_click:
#         pyautogui.click()


# def perform_actions(images, region):
#     """
#     Performs a sequence of actions moving to and clicking on images within a specific region, each with its specified confidence level.
#     Parameters:
#     - images: A list of dictionaries for images to find and click on, each containing 'path', 'confidence', and 'click'.
#     - region: The region within which to search for the images.
#     """
#     initial_position = pyautogui.position()
#     for image_info in images:
#         click_on_image(image_info, region)
#         random_sleep = random.uniform(0.1, 0.3)
#         time.sleep(random_sleep)
#     return_duration = random.uniform(0.1, 0.3)
#     pyautogui.moveTo(initial_position, duration=return_duration)
#     pyautogui.click()
#     print("All actions completed.")


# def focus_and_press_key(window_name, key_sequence):
#     """
#     Focuses on a specific window and presses a key using xte from xautomation.
#     """
#     try:
#         # Focus the window using its name
#         subprocess.run(["wmctrl", "-a", window_name])
#         time.sleep(0.2)  # Small delay to ensure the window has time to focus

#         # Simulate key press using xte
#         subprocess.run(["xte", key_sequence])
#     except Exception as e:
#         print(f"Error in focusing window or pressing key: {e}")


# def perform_key_actions_sequence(window_name, key_actions):
#     """
#     Performs a sequence of key press actions, each with specified wait times and repetition counts,
#     and repeats the entire sequence a specified number of times within a specified window.
#     """
#     sequence_repeat = key_actions["repeat"]
#     actions = key_actions["actions"]

#     for _ in range(sequence_repeat):
#         for action in actions:
#             key = action["key"]
#             wait_time = action["wait"]
#             repeat = action["repeat"]
#             # Convert the key to the xte input format
#             key_sequence = f"key {key}"
#             for _ in range(repeat):
#                 focus_and_press_key(window_name, key_sequence)
#                 print(f"Pressed {key} in {window_name}")
#                 time.sleep(wait_time)
#         print(f"Completed one sequence of actions in {window_name}.")
#     print(
#         f"Completed all sequences in {window_name}, each repeated {sequence_repeat} times."
#     )


# # Retrieve the geometry for the "Toontown Rewritten" window and set it as the region for image searches
# offset_y = 50
# window_name = "Toontown Rewritten"
# window_geometry = get_window_geometry(window_name, offset_y)
# if window_geometry:
#     print("Window Geometry:", window_geometry)
#     region = window_geometry
#     debug_screenshot = pyautogui.screenshot(region=region)
#     debug_screenshot.save("region_debug.png")
# else:
#     print("Unable to find 'Toontown Rewritten' window.")
#     region = None  # or set a default region
#     exit()

# # # List of image paths with confidence levels
# # images = [
# #     {"path": "./speedchat.png", "confidence": 0.999, "click": True},
# #     {"path": "./pets.png", "confidence": 0.9, "click": False},
# #     {"path": "./tricks.png", "confidence": 0.9, "click": False},
# #     {"path": "./speak.png", "confidence": 0.99, "click": True},
# # ]

# # praise = [
# #     {"path": "./speedchat.png", "confidence": 0.999, "click": True},
# #     {"path": "./pets.png", "confidence": 0.9, "click": False},
# #     {"path": "./gooddoodle.png", "confidence": 0.99, "click": True},
# # ]

# jellybeans = [
#     {"path": "./speedchat.png", "confidence": 0.999, "click": True},
#     {"path": "./trolley.png", "confidence": 0.999, "click": False},
#     {"path": "./jellybeans.png", "confidence": 0.8, "click": True},
# ]

# toontastic = [
#     {"path": "./speedchat.png", "confidence": 0.9, "click": True},
#     {"path": "./replies.png", "confidence": 0.999, "click": True},
#     {"path": "./good.png", "confidence": 0.999, "click": True},
#     {"path": "./toontastic.png", "confidence": 0.99, "click": True},
# ]

# # Assuming 'images' and 'praise' are already defined and now include 'region' information
# print("Starting in 5 seconds. Please switch to the screen with the images.")
# time.sleep(5)

# if region:
#     # perform_actions(jellybeans, region)
#     for _ in range(5000):
#         for _ in range(3):
#             random_sleep = random.uniform(0.1, 0.9) * 1000
#             print(f"Sleeping for: {random_sleep} seconds")
#             time.sleep(random_sleep)
#             original_window_id = get_active_window_id()
#             print(f"Captured originally focused window: {original_window_id}")
#             focus_on_window(window_name)
#             time.sleep(2)
#             print(f"Switching focus to: {window_name}")
#             perform_actions(jellybeans, region)
#             if original_window_id:
#                 print(f"Returning focus to: {original_window_id}")
#                 focus_on_window_by_id(original_window_id)
#         # perform_actions(toontastic, region)


# # key_actions = {
# #     "repeat": 100,
# #     "actions": [
# #         {"key": "space", "wait": 5, "repeat": 1},
# #         {"key": "Right", "wait": 5, "repeat": 1},
# #     ],
# # }

# # print(
# #     "Starting key actions sequence in 5 seconds. Please switch to the target application window."
# # )
# # time.sleep(5)  # Gives you time to switch to the target window

# # perform_key_actions_sequence(window_name, key_actions)


# with open(cache_file_path, "w") as cache_file:
#     json.dump(image_cache, cache_file)
