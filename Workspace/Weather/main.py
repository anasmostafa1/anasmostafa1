import requests
import customtkinter as ctk
from tkinter import messagebox
from PIL import Image, ImageTk
import io
import config  # Import the configuration file

# Create the main window
ctk.set_appearance_mode("dark")  # Modes: "System", "Dark", "Light"
ctk.set_default_color_theme("green")  # Themes: "blue", "green", "dark-blue"

root = ctk.CTk()
root.title("Weather App")
root.geometry("600x600")

# Main frame with modern styling
main_frame = ctk.CTkFrame(root, corner_radius=20)
main_frame.pack(padx=20, pady=20, fill="both", expand=True)

# Header frame
header_frame = ctk.CTkFrame(main_frame, corner_radius=20)
header_frame.pack(pady=10, fill="x")

header_label = ctk.CTkLabel(header_frame, text="Weather App", font=("Arial", 28, "bold"), text_color="skyblue")
header_label.pack(pady=10)

# Input frame
input_frame = ctk.CTkFrame(main_frame, corner_radius=20)
input_frame.pack(pady=20, fill="x")

city_label = ctk.CTkLabel(input_frame, text="Enter City:", font=("Arial", 16))
city_label.pack(pady=10)

city_entry = ctk.CTkEntry(input_frame, placeholder_text="City Name", width=200)
city_entry.pack(pady=10)

# Fetch weather button
fetch_button = ctk.CTkButton(input_frame, text="Fetch Weather", corner_radius=10, fg_color="green", hover_color="darkgreen")
fetch_button.pack(pady=10)

# Weather info frame
weather_frame = ctk.CTkFrame(main_frame, corner_radius=20)
weather_frame.pack(pady=20, fill="both", expand=True)

weather_label = ctk.CTkLabel(weather_frame, text="", justify="left", font=("Arial", 16))
weather_label.pack(pady=20)

# Modern icon label
icon_label = ctk.CTkLabel(weather_frame, text="", font=("Arial", 50))  # Placeholder for icon
icon_label.pack(pady=10)

# Define the function to fetch weather data
def fetch_weather():
    city = city_entry.get().strip()  # Trim whitespace
    if not city:  # Check if the input is empty
        messagebox.showerror("Error", "Please enter a city name")
        return

    api_key = config.API_KEY  # Get API key from config
    url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={city}"

    try:
        response = requests.get(url)
        response.raise_for_status()  # Raises an HTTPError for bad responses
        data = response.json()

        if "error" in data:
            messagebox.showerror("Error", "City not found")
            return

        temperature = data["current"]["temp_c"]
        weather = data["current"]["condition"]["text"]
        icon_url = data["current"]["condition"]["icon"]  # Get the icon URL

        weather_label.configure(text=f"Temperature: {temperature}°C\nWeather: {weather}")

        # Fetch and display the icon
        icon_response = requests.get(f"http:{icon_url}")  # Prepend 'http:' to the icon URL
        icon_image = Image.open(io.BytesIO(icon_response.content))  # Load image from response
        icon_image = icon_image.resize((70, 70))  # Resize the icon if needed
        icon_photo = ImageTk.PhotoImage(icon_image)  # Convert to PhotoImage

        icon_label.configure(image=icon_photo)  # Set the image in the label
        icon_label.image = icon_photo  # Keep a reference to avoid garbage collection

    except requests.exceptions.RequestException as e:
        messagebox.showerror("Error", f"Network error: {e}")
    except ValueError:
        messagebox.showerror("Error", "Error parsing response data")
    except Exception as e:
        messagebox.showerror("Error", f"An unexpected error occurred: {e}")

# Connect the button to the function
fetch_button.configure(command=fetch_weather)

# Start the GUI main loop
root.mainloop()