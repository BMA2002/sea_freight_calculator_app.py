import tkinter as tk
from tkinter import ttk, messagebox
from tkinter.ttk import Progressbar

# Sea Freight Rate Calculator Function
def calculate_sea_freight_rate(weight, distance, container_size, goods_type):
    """
    Calculate the sea freight rate based on weight, distance, container size, and type of goods.
    
    Parameters:
    weight (float): Weight of the goods in kilograms
    distance (float): Distance from port of origin to destination port in kilometers
    container_size (str): Type of container, either '20ft' or '40ft'
    goods_type (str): Type of goods ('general', 'hazardous', 'perishable')
    
    Returns:
    float: Estimated sea freight cost
    """
    
    # Base rate per kilometer per ton
    base_rate_per_km = 0.5  # $ per km per ton
    
    # Adjust rates for container size
    if container_size == '40ft':
        container_factor = 1.5  # 40ft container is 1.5 times more expensive
    else:
        container_factor = 1  # 20ft container

    # Adjust rates for goods type
    if goods_type == 'hazardous':
        goods_factor = 2  # Hazardous goods are twice as expensive
    elif goods_type == 'perishable':
        goods_factor = 1.5  # Perishable goods cost 1.5 times more
    else:
        goods_factor = 1  # General goods

    # Calculate the rate based on weight (in tons)
    weight_in_tons = weight / 1000  # Convert weight to tons

    # Estimate cost
    estimated_cost = base_rate_per_km * weight_in_tons * distance * container_factor * goods_factor

    return estimated_cost

# GUI Application
class SeaFreightCalculatorApp:
    def __init__(self, root):
def generate_random_password(length=5, use_upper=True, use_lower=True, use_digits=True, use_special=True):
    if length < 5:
        raise ValueError("Password length must be at least 5 characters for a strong password.")

    character_sets = []
    if use_upper:
        character_sets.append(string.ascii_uppercase)
    if use_lower:
        character_sets.append(string.ascii_lowercase)
    if use_digits:
        character_sets.append(string.digits)
    if use_special:
        character_sets.append(string.punctuation)

    if not character_sets:
        raise ValueError("At least one character set must be selected.")

    # Ensure at least one character from each selected set is included
    password = [random.choice(char_set) for char_set in character_sets]

    # Fill the remaining length with random choices from all selected sets
    all_characters = ''.join(character_sets)
    password += [random.choice(all_characters) for _ in range(length - len(password))]

    # Shuffle the password to avoid predictable patterns
    random.shuffle(password)

    return ''.join(password)

# GUI Application
class SeaFreightCalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Sea Freight Rate Calculator")
        
        # Main frame
        main_frame = ttk.Frame(root, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        # Weight Input
        self.weight_label = ttk.Label(main_frame, text="Enter the weight of the goods (kg):")
        self.weight_label.grid(row=0, column=0, padx=10, pady=5, sticky=tk.W)
        self.weight_entry = ttk.Entry(main_frame)
        self.weight_entry.grid(row=0, column=1, padx=10, pady=5, sticky=tk.E)
        self.create_tooltip(self.weight_entry, "Enter the weight of the goods in kilograms.")

        # Distance Input
        self.distance_label = ttk.Label(main_frame, text="Enter the distance (km):")
        self.distance_label.grid(row=1, column=0, padx=10, pady=5, sticky=tk.W)
        self.distance_entry = ttk.Entry(main_frame)
        self.distance_entry.grid(row=1, column=1, padx=10, pady=5, sticky=tk.E)
        self.create_tooltip(self.distance_entry, "Enter the distance from port of origin to destination port in kilometers.")

        # Container Size Input
        self.container_label = ttk.Label(main_frame, text="Select the container size:")
        self.container_label.grid(row=2, column=0, padx=10, pady=5, sticky=tk.W)
        self.container_size = tk.StringVar()
        self.container_combobox = ttk.Combobox(main_frame, textvariable=self.container_size, state="readonly")
        self.container_combobox['values'] = ('20ft', '40ft')
        self.container_combobox.grid(row=2, column=1, padx=10, pady=5, sticky=tk.E)
        self.create_tooltip(self.container_combobox, "Select the size of the container.")

        # Goods Type Input
        self.goods_label = ttk.Label(main_frame, text="Select the type of goods:")
        self.goods_label.grid(row=3, column=0, padx=10, pady=5, sticky=tk.W)
        self.goods_type = tk.StringVar()
        self.goods_combobox = ttk.Combobox(main_frame, textvariable=self.goods_type, state="readonly")
        self.goods_combobox['values'] = ('general', 'hazardous', 'perishable')
        self.goods_combobox.grid(row=3, column=1, padx=10, pady=5, sticky=tk.E)
        self.create_tooltip(self.goods_combobox, "Select the type of goods.")

        # Calculate Button
        self.calculate_button = ttk.Button(main_frame, text="Calculate", command=self.calculate_rate)
        self.calculate_button.grid(row=4, column=0, pady=10)

        # Reset Button
        self.reset_button = ttk.Button(main_frame, text="Reset", command=self.reset_fields)
        self.reset_button.grid(row=4, column=1, pady=10)

        # Progress Bar
        self.progress = Progressbar(main_frame, orient=tk.HORIZONTAL, length=200, mode='determinate')
        self.progress.grid(row=5, column=0, columnspan=2, pady=10)

        # Result Label
        self.result_label = ttk.Label(main_frame, text="Estimated Sea Freight Rate: $0.00")
        self.result_label.grid(row=6, column=0, columnspan=2, pady=10)

    def calculate_rate(self):
        try:
            # Start progress bar
            self.progress.start()

            # Get the input values
            weight = float(self.weight_entry.get())
            distance = float(self.distance_entry.get())
            container_size = self.container_size.get().strip().lower()
            goods_type = self.goods_type.get().strip().lower()

            # Validate weight and distance
            if weight <= 0 or distance <= 0:
                raise ValueError("Weight and distance must be positive numbers.")

            # Validate container size
            if container_size not in ['20ft', '40ft']:
                raise ValueError("Container size must be '20ft' or '40ft'.")

            # Validate goods type   
            if goods_type not in ['general', 'hazardous', 'perishable']:
                raise ValueError("Goods type must be 'general', 'hazardous', or 'perishable'.")

            # Call the calculation function
            rate = calculate_sea_freight_rate(weight, distance, container_size, goods_type)

            # Display the result
            self.result_label.config(text=f"Estimated Sea Freight Rate: ${rate:.2f}")

            # Stop progress bar
            self.progress.stop()
        except ValueError as e:
            self.progress.stop()
            messagebox.showerror("Input Error", str(e))

    def reset_fields(self):
        self.weight_entry.delete(0, tk.END)
        self.distance_entry.delete(0, tk.END)
        self.container_combobox.set('')
        self.goods_combobox.set('')
        self.result_label.config(text="Estimated Sea Freight Rate: $0.00")

    def create_tooltip(self, widget, text):
        tooltip = ttk.Label(widget, text=text, background="yellow", relief="solid", borderwidth=1, wraplength=150)
        tooltip.place_forget()

        def enter(event):
            tooltip.place(x=widget.winfo_x(), y=widget.winfo_y() - 30)

        def leave(event):
            tooltip.place_forget()

        widget.bind("<Enter>", enter)
        widget.bind("<Leave>", leave)

# Create the main window and pass it to the app class
if __name__ == "__main__":
    root = tk.Tk()
    app = SeaFreightCalculatorApp(root)
    root.mainloop()

