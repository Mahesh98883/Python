import tkinter as tk
from tkinter import messagebox, ttk
from PIL import Image, ImageTk

class DiseasePredictionDashboard:
    def __init__(self, root):
        self.root = root
        self.root.title("Disease Prediction Dashboard")
        self.root.geometry("400x400")
        self.root.config(bg="#f0f0f0")  # Light gray background

       
        # Title frame
        title_frame = tk.Frame(self.root, bg="#4a90e2", padx=10, pady=10)
        title_frame.pack(fill=tk.X)

        # Title label
        title_label = tk.Label(title_frame, text="Disease Prediction Dashboard", font=("Arial", 18, "bold"), bg="#4a90e2", fg="white")
        title_label.pack()

        # Input frame
        input_frame = tk.Frame(self.root, bg="#f0f0f0", padx=20, pady=20)
        input_frame.pack(pady=20)

        # Input fields
        self.age_label = tk.Label(input_frame, text="Age:", bg="#f0f0f0")
        self.age_label.grid(row=0, column=0, sticky=tk.W, pady=5)
        self.age_entry = ttk.Entry(input_frame, font=("Arial", 14))
        self.age_entry.grid(row=0, column=1, pady=5)

        self.symptoms_label = tk.Label(input_frame, text="Symptoms:", bg="#f0f0f0")
        self.symptoms_label.grid(row=1, column=0, sticky=tk.W, pady=5)
        self.symptoms_entry = ttk.Entry(input_frame, font=("Arial", 14))
        self.symptoms_entry.grid(row=1, column=1, pady=5)

        self.conditions_label = tk.Label(input_frame, text="Previous Conditions:", bg="#f0f0f0")
        self.conditions_label.grid(row=2, column=0, sticky=tk.W, pady=5)
        self.conditions_entry = ttk.Entry(input_frame, font=("Arial", 14))
        self.conditions_entry.grid(row=2, column=1, pady=5)

        # Predict button
        self.predict_button = ttk.Button(self.root, text="Predict Disease", command=self.predict_disease)
        self.predict_button.pack(pady=20)

    def predict_disease(self):
        age = self.age_entry.get()
        symptoms = self.symptoms_entry.get()
        conditions = self.conditions_entry.get()

        # Display a simple message for demonstration
        messagebox.showinfo("Prediction Result", f"Predicted Disease for Age: {age}\nSymptoms: {symptoms}\nConditions: {conditions}")

if __name__ == "__main__":
    root = tk.Tk()
    app = DiseasePredictionDashboard(root)
    root.mainloop()
import tkinter as tk
from tkinter import messagebox, ttk
from PIL import Image, ImageTk

class DiseasePredictionDashboard:
    def __init__(self, root):
        self.root = root
        self.root.title("Disease Prediction Dashboard")
        self.root.geometry("400x400")
        self.root.config(bg="#f0f0f0")  # Light gray background

        # Load and set the background image
        self.background_image = Image.open("path/to/your/image.jpg")
        self.background_image = self.background_image.resize((400, 400), Image.ANTIALIAS)
        self.background_photo = ImageTk.PhotoImage(self.background_image)

        background_label = tk.Label(self.root, image=self.background_photo)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)

        # Title frame
        title_frame = tk.Frame(self.root, bg="#4a90e2", padx=10, pady=10)
        title_frame.pack(fill=tk.X)

        # Title label
        title_label = tk.Label(title_frame, text="Disease Prediction Dashboard", font=("Arial", 18, "bold"), bg="#4a90e2", fg="white")
        title_label.pack()

        # Input frame
        input_frame = tk.Frame(self.root, bg="#f0f0f0", padx=20, pady=20)
        input_frame.pack(pady=20)

        # Input fields
        self.age_label = tk.Label(input_frame, text="Age:", bg="#f0f0f0")
        self.age_label.grid(row=0, column=0, sticky=tk.W, pady=5)
        self.age_entry = ttk.Entry(input_frame, font=("Arial", 14))
        self.age_entry.grid(row=0, column=1, pady=5)

        self.symptoms_label = tk.Label(input_frame, text="Symptoms:", bg="#f0f0f0")
        self.symptoms_label.grid(row=1, column=0, sticky=tk.W, pady=5)
        self.symptoms_entry = ttk.Entry(input_frame, font=("Arial", 14))
        self.symptoms_entry.grid(row=1, column=1, pady=5)

        self.conditions_label = tk.Label(input_frame, text="Previous Conditions:", bg="#f0f0f0")
        self.conditions_label.grid(row=2, column=0, sticky=tk.W, pady=5)
        self.conditions_entry = ttk.Entry(input_frame, font=("Arial", 14))
        self.conditions_entry.grid(row=2, column=1, pady=5)

        # Predict button
        self.predict_button = ttk.Button(self.root, text="Predict Disease", command=self.predict_disease)
        self.predict_button.pack(pady=20)

    def predict_disease(self):
        age = self.age_entry.get()
        symptoms = self.symptoms_entry.get()
        conditions = self.conditions_entry.get()

        # Display a simple message for demonstration
        messagebox.showinfo("Prediction Result", f"Predicted Disease for Age: {age}\nSymptoms: {symptoms}\nConditions: {conditions}")

if __name__ == "__main__":
    root = tk.Tk()
    app = DiseasePredictionDashboard(root)
    root.mainloop()
