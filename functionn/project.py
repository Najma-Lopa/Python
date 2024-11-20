import tkinter as tk
import time
import math

class AnalogClock:
    def __init__(self, root):
        self.root = root
        self.root.title("Analog Clock with Digital Display")
        self.root.geometry("400x450")
        self.root.configure(bg="black")

        # Set up the canvas for drawing the clock
        self.canvas = tk.Canvas(root, width=400, height=400, bg="black")
        self.canvas.pack()

        # Digital Clock Display
        self.digital_display = tk.Label(root, font=("Helvetica", 16), bg="black", fg="cyan")
        self.digital_display.pack(pady=10)

        # Start updating the clock
        self.update_clock()

    def draw_hand(self, length, angle, width, color):
        """Draws a clock hand on the canvas."""
        angle_rad = math.radians(angle)
        x = 200 + length * math.sin(angle_rad)
        y = 200 - length * math.cos(angle_rad)
        self.canvas.create_line(200, 200, x, y, width=width, fill=color)

    def draw_ticks(self):
        """Draws hour and minute ticks around the clock face."""
        for i in range(60):
            angle = math.radians(i * 6)  # Each tick is 6 degrees apart
            start_x = 200 + 150 * math.sin(angle)
            start_y = 200 - 150 * math.cos(angle)
            if i % 5 == 0:  # Hour tick
                end_x = 200 + 140 * math.sin(angle)
                end_y = 200 - 140 * math.cos(angle)
                self.canvas.create_line(start_x, start_y, end_x, end_y, width=3, fill="white")
            else:  # Minute tick
                end_x = 200 + 145 * math.sin(angle)
                end_y = 200 - 145 * math.cos(angle)
                self.canvas.create_line(start_x, start_y, end_x, end_y, width=1, fill="grey")

    def draw_numbers(self):
        """Draws hour numbers around the clock face."""
        for i in range(1, 13):
            angle = math.radians(i * 30)  # Each hour is 30 degrees apart
            x = 200 + 120 * math.sin(angle)
            y = 200 - 120 * math.cos(angle)
            self.canvas.create_text(x, y, text=str(i), font=("Helvetica", 14, "bold"), fill="cyan")

    def update_clock(self):
        """Updates the clock hands and digital display based on the current time."""
        self.canvas.delete("all")  # Clear the canvas

        # Draw the clock face
        self.canvas.create_oval(50, 50, 350, 350, width=4, outline="white")
        self.draw_ticks()  # Draw the hour and minute ticks
        self.draw_numbers()  # Draw the hour numbers

        # Get the current time
        current_time = time.localtime()
        hours = current_time.tm_hour % 12
        minutes = current_time.tm_min
        seconds = current_time.tm_sec

        # Update the digital display
        digital_time = time.strftime("%I:%M:%S %p", current_time)
        self.digital_display.config(text=digital_time)

        # Calculate angles for each hand
        second_angle = seconds * 6  # 360 degrees / 60 seconds
        minute_angle = minutes * 6  # 360 degrees / 60 minutes
        hour_angle = (hours + minutes / 60) * 30  # 360 degrees / 12 hours

        # Draw the hands
        self.draw_hand(90, hour_angle, 6, "white")  # Hour hand
        self.draw_hand(120, minute_angle, 4, "blue")  # Minute hand
        self.draw_hand(140, second_angle, 2, "red")  # Second hand

        # Draw the clock center
        self.canvas.create_oval(195, 195, 205, 205, fill="white")

        # Update the clock every 1000 milliseconds (1 second)
        self.root.after(1000, self.update_clock)

# Run the application
root = tk.Tk()
clock = AnalogClock(root)
root.mainloop()
