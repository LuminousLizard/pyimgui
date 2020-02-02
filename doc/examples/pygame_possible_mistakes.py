# -*- coding: utf-8 -*

'''
This is an example script and is intended to alert the user to possible
sources of errors and unwanted program sequences.
'''

# required packages
import sys # for close call

# render engine
import pygame
import OpenGL.GL as gl

# GUI library
from imgui.integrations.pygame import PygameRenderer
import imgui

# Main function
# It creates the instance and the program loop, and holds the
# frames and individual windows.
# It's called at the bottom of this file to start the application.
def main():
    # Initialize a pygame instance
    pygame.init()

    imgui.create_context()

    # Size of the main screen
    size = 800, 600

    # Initialize the screen for display
    pygame.display.set_mode(size, pygame.DOUBLEBUF | pygame.OPENGL)
    # Set screen title
    pygame.display.set_caption("Pyimgui: Mistakes")

    io = imgui.get_io()
    io.fonts.add_font_default()
    io.display_size = size

    # Declares pygame as render engine
    render_engine = PygameRenderer()

    # IMPORTANT: the variables storing the state of elements
    # (e.g. checkbox) must be inserted BEFORE the main loop

    value_slider_1 = 70.0
    value_slider_2 = 10.5

    # MAIN LOOP
    # This keeps the application running until the "exit" command is called
    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            render_engine.process_event(event)

        # creates a new imgui frame for individual windows in the main screen
        imgui.new_frame()

        # ------------------------
        # GUI code
        # ------------------------
        imgui.set_next_window_size(
            width = 500,
            height = 200,
            condition = imgui.ONCE
        )
        # Create a window within the frame
        imgui.begin("Example: Mistakes")

        # Mistake: Same widget ID
        imgui.text("Two sliders with different assigned variables and start "
            "values.\nBut if you change on slider the other changes too.\n"
            "The mistake is that both elements have the same label und \n"
            "thus internally the same ID (see source code).")

        # The following example shows 2 sliders with different variables
        # and start values (see line 51).
        # But since they have the same label, they influence each other.
        changed, value_slider_1 = imgui.slider_float(
            "Slider floats", # same label
            value_slider_1,
            min_value = 0.0,
            max_value = 100.0,
            power = 1.0
        )

        imgui.separator()

        # Slider with 2 float values
        changed, value_slider_2 = imgui.slider_float(
            "Slider floats", # same label
            value_slider_2,
            min_value = 0.0,
            max_value = 100,
            power = 1.0
        )

        imgui.end()
        
        # ------------------------

        # note: cannot use screen.fill((1, 1, 1)) because pygame's screen
        #       does not support fill() on OpenGL sufraces
        gl.glClearColor(0.1, 0.1, 0.1, 1) # Background color of the main screen
        gl.glClear(gl.GL_COLOR_BUFFER_BIT)
        imgui.render()
        render_engine.render(imgui.get_draw_data())

        # Update the full display surface to the screen
        pygame.display.flip()

# Application call for start
if __name__ == "__main__":
    main()
