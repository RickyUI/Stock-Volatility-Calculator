from customtkinter import CTk, CTkFrame, CTkButton, CTkEntry, CTkLabel
import sys


def clear_frame(frame):
    """Function to clear the screen"""
    for widget in frame.winfo_children():
        widget.destroy()


def show_menu():
    """Function to return to the main menu"""
    clear_frame(content_frame)
    main_menu()


def calculate_results_volatility(volatility, price, label_volatility, label_calls, label_puts):
    try:
        volatility = float(volatility)
        price = float(price)
        three_volatility = round(3.0 * volatility, 2)
        calls = round((((volatility * 2) / 100.0) * price) + price, 2)
        puts = round(abs((((volatility * 2) / 100.0) * price) - price), 2)

        label_volatility.configure(text=f"3 Volatility Levels: {three_volatility}")
        label_calls.configure(text=f"CALL Strike Price: {calls}")
        label_puts.configure(text=f"PUT Strike Price: {puts}")
    except ValueError:
        label_volatility.configure(text="")
        label_calls.configure(text="Error: Invalid inputs", fg_color="red")
        label_puts.configure(text="")


def calculate_results_options(price, label_first, label_second, label_third):
    try:
        price = float(price)
        first = round(price + (price * 0.25), 2)
        second = round(price + (price * 0.55), 2)
        third = round(price + (price * 0.85), 2)

        label_first.configure(text=f"First Stop: {first}")
        label_second.configure(text=f"Second Stop: {second}")
        label_third.configure(text=f"Third Stop: {third}")
    except ValueError:
        label_first.configure(text="")
        label_second.configure(text="Error: Invalid inputs", fg_color="red")
        label_third.configure(text="")


def insert_volatility_price():
    clear_frame(content_frame)  # Clear the frame

    # Volatility input
    CTkLabel(content_frame, text="Enter Volatility:", font=("Arial", 18, 'bold')).pack(pady=5)
    volatility_box = CTkEntry(content_frame, font=("Arial,", 18))
    volatility_box.pack(pady=5)

    # Price input
    CTkLabel(content_frame, text="Enter Asset Price:", font=("Arial", 18, 'bold')).pack(pady=5)
    price_box = CTkEntry(content_frame, font=("Arial,", 18))
    price_box.pack(pady=5)

    # Result labels
    three_volatility = CTkLabel(content_frame, text="", text_color='blue', font=("Arial", 18, 'bold'))
    calls = CTkLabel(content_frame, text="", text_color='blue', font=("Arial", 18, 'bold'))
    puts = CTkLabel(content_frame, text="", text_color='blue', font=("Arial", 18, 'bold'))

    # Positioning result labels
    three_volatility.place(relx=0.05, rely=0.75, anchor="sw")
    calls.place(relx=0.05, rely=0.85, anchor="sw")
    puts.place(relx=0.05, rely=0.95, anchor="sw")

    # Calculate button
    CTkButton(
        content_frame, text="Calculate", font=("Arial", 18),
        command=lambda: calculate_results_volatility(volatility_box.get(), price_box.get(), three_volatility, calls, puts)
    ).pack(pady=10)

    # Back to menu button
    CTkButton(content_frame, text="Back to Menu", font=("Arial", 18), command=show_menu).place(relx=0.85, rely=0.85, anchor="center")


def insert_option_price():
    clear_frame(content_frame)  # Clear the frame

    # Option price input
    CTkLabel(content_frame, text="Enter Option Price:", font=("Arial", 18, 'bold')).pack(pady=5)
    option_box = CTkEntry(content_frame, font=("Arial", 18))
    option_box.pack(pady=5)

    # Result labels
    first = CTkLabel(content_frame, text="", text_color='blue', font=("Arial", 18, 'bold'))
    second = CTkLabel(content_frame, text="", text_color='blue', font=("Arial", 18, 'bold'))
    third = CTkLabel(content_frame, text="", text_color='blue', font=("Arial", 18, 'bold'))

    # Positioning result labels
    first.place(relx=0.05, rely=0.75, anchor="sw")
    second.place(relx=0.05, rely=0.85, anchor="sw")
    third.place(relx=0.05, rely=0.95, anchor="sw")

    # Calculate button
    CTkButton(
        content_frame, text='Calculate', font=('Arial', 18),
        command=lambda: calculate_results_options(option_box.get(), first, second, third)
    ).pack(pady=10)

    # Back to menu button
    CTkButton(content_frame, text="Back to Menu", font=("Arial", 18), command=show_menu).place(relx=0.85, rely=0.85, anchor="center")


def program_exit():
    """Exit the program"""
    sys.exit()


def main_menu():
    """Displays the main menu of the program"""
    CTkLabel(content_frame, text="Main Menu", font=('Arial', 35, 'bold')).pack(pady=30)
    CTkButton(content_frame, text="Insert Volatility and Asset Price", font=('Arial', 18), command=insert_volatility_price).pack(pady=10)
    CTkButton(content_frame, text="Insert Option Price", font=('Arial', 18), command=insert_option_price).pack(pady=10)
    CTkButton(content_frame, text="Exit", font=('Arial', 18), command=program_exit).pack(pady=10)


# Application setup
window = CTk()
window.geometry("800x450")
window.title("Volatility Calculator")

# Main content frame
content_frame = CTkFrame(window)
content_frame.pack(fill='both', expand=True)

# Initialize the main menu
main_menu()

# Start the application
window.mainloop()
