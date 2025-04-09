import pandas as pd
import os
import tkinter as tk
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import matplotlib.pyplot as plt
import sys
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class AttendanceAnalyzer:
    OUTPUT_FOLDER = "Attendance_Graphs"

    def __init__(self, file_path, root):
        self.file_path = "C:\\Users\\lenovo\\Desktop\\Face_Recognition_System\\Attendance_Report\\sudha.csv"
        os.makedirs(self.OUTPUT_FOLDER, exist_ok=True)
        self.df = self.load_and_process_data()
        self.attendance_summary = None

        self.root = root
        self.setup_gui()

    def load_and_process_data(self):
        df = pd.read_csv(self.file_path, encoding="utf-8", header=None, on_bad_lines='skip')
        df.columns = ["Attendance ID", "Roll Number", "Name", "Department", "Time", "Date", "Attendance Status"]

        df["Date"] = pd.to_datetime(df["Date"], errors="coerce", dayfirst=True)
        df = df.dropna(subset=["Date"])
        df["Month_Year"] = df["Date"].dt.to_period("M").astype(str)

        df["Roll Number"] = pd.to_numeric(df["Roll Number"], errors="coerce")
        df = df.dropna(subset=["Roll Number"])
        df["Roll Number"] = df["Roll Number"].astype(int)

        return df

    def calculate_attendance_summary(self, month, working_days):
        month_data = self.df[self.df["Month_Year"] == month]

        if month_data.empty:
            self.attendance_summary = pd.DataFrame()
            return

        summary = month_data.groupby(["Roll Number", "Name"]).size().reset_index(name="Days Present")
        summary["Total Working Days"] = working_days
        summary["Month_Year"] = month
        summary["Attendance Percentage"] = (summary["Days Present"] / working_days) * 100
        summary["Attendance Percentage"] = summary["Attendance Percentage"].round(2)

        # Show warning if any percentage > 100%
        over_100 = summary[summary["Attendance Percentage"] > 100]
        if not over_100.empty:
            names = ", ".join(over_100["Name"].astype(str))
            messagebox.showwarning(
                "Attendance Warning",
                f"The following students have attendance over 100% (possible data error):\n{names}"
            )

        # Clamp the displayed attendance to max 100
        summary["Display Percentage"] = summary["Attendance Percentage"].clip(upper=100)

        self.attendance_summary = summary

    def setup_gui(self):
        self.root.title("Face Recognition System")
        self.root.geometry("1366x768")

        title_lbl = Label(self.root, text="Average Attendance", font=("times new roman", 32, "bold"), bg="black", fg="red")
        title_lbl.place(x=0, y=0, width=1366, height=60)

        self.selected_month = tk.StringVar()

        months = sorted(self.df["Month_Year"].unique())

        try:
            img = Image.open(r"C:college_images\graph2.png")
            img = img.resize((1366, 700))
            self.photoimage = ImageTk.PhotoImage(img)
            bg_img = Label(self.root, image=self.photoimage, bg="black")
            bg_img.place(x=0, y=60, width=1366, height=700)
        except Exception as e:
            print(f"Warning: Could not load background image: {e}")
            bg_img = Frame(self.root, bg="white")
            bg_img.place(x=0, y=60, width=1366, height=700)

        self.month_dropdown = ttk.Combobox(bg_img, textvariable=self.selected_month,
                                           values=months, state="readonly", font=("Arial", 12), width=15)
        self.month_dropdown.place(x=450, y=10, width=400, height=40)
        self.month_dropdown.set("Select Your Year & Month ===>")
        self.month_dropdown.config(foreground="black", font=("Arial", 18, "bold"))

        Label(bg_img, text="Enter Working Days:", font=("Arial", 14, "bold"), bg="white", fg="black").place(x=450, y=60)
        self.working_days_entry = tk.Entry(bg_img, font=("Arial", 14))
        self.working_days_entry.place(x=650, y=60, width=100)

        self.show_button = tk.Button(bg_img, text="Show Graph", command=self.show_graph,
                                     font=("times new roman", 20, "bold"), fg="purple", bg="pink")
        self.show_button.place(x=600, y=110, width=200, height=40)

        self.canvas_frame = tk.Frame(self.root)
        self.canvas_frame.pack()

    def show_graph(self):
        selected_month = self.selected_month.get().strip()
        working_days_input = self.working_days_entry.get().strip()

        if not selected_month or selected_month.startswith("Select"):
            messagebox.showerror("Input Error", "Please select a valid month.")
            return

        if not working_days_input.isdigit():
            messagebox.showerror("Input Error", "Please enter a valid number of working days.")
            return

        working_days = int(working_days_input)
        self.calculate_attendance_summary(selected_month, working_days)

        if self.attendance_summary.empty:
            messagebox.showinfo("No Data", f"No attendance data found for {selected_month}")
            return

        save_path = "C:\\Users\\lenovo\\Desktop\\Face_Recognition_System\\Attendance_Report\\Average_Atten.csv"

        try:
            if os.path.exists(save_path):
                existing_df = pd.read_csv(save_path)
                updated_df = existing_df[existing_df["Month_Year"] != selected_month]
                combined_df = pd.concat([updated_df, self.attendance_summary], ignore_index=True)
            else:
                combined_df = self.attendance_summary

            combined_df.to_csv(save_path, index=False)
        except Exception as e:
            messagebox.showerror("File Save Error", f"Could not save summary CSV.\nError: {e}")
            return

        month_data = self.attendance_summary.sort_values(by=["Roll Number"])

        graph_window = tk.Toplevel(self.root)
        graph_window.title(f"Attendance for {selected_month}")
        graph_window.geometry("1366x768")

        fig, ax = plt.subplots(figsize=(16, 10))
        ax.bar(month_data["Roll Number"].astype(str), month_data["Display Percentage"], color='skyblue')
        ax.set_xlabel("Roll Number")
        ax.set_ylabel("Attendance Percentage")
        ax.set_title(f"Attendance for {selected_month}")
        ax.set_ylim(0, 110)
        ax.grid(axis="y", linestyle="--", alpha=0.7)

        for i, value in enumerate(month_data["Display Percentage"]):
            ax.text(i, value + 2, f"{value}%", ha="center", fontsize=10, fontweight="bold")

        canvas = FigureCanvasTkAgg(fig, master=graph_window)
        canvas.draw()
        canvas.get_tk_widget().pack()

if __name__ == "__main__":

    def on_closing():
        root.quit()
        root.destroy()

    file_path = "C:\\Users\\lenovo\\Desktop\\Face_Recognition_System\\Attendance_Report\\sudha.csv"
    root = tk.Tk()
    root.protocol("WM_DELETE_WINDOW", on_closing)
    analyzer = AttendanceAnalyzer(file_path, root)
    root.mainloop()
