from fpdf import FPDF
from datetime import datetime
import sqlite3

# Input
client_name = input("Enter client name: ")

items = []

while True:
    item_name = input("Enter item name (or 'done'): ")
    if item_name.lower() == "done":
        break

    qty = int(input("Enter quantity: "))
    price = float(input("Enter price: "))
    total = qty * price

    items.append((item_name, qty, price, total))

# Calculations
subtotal = sum(item[3] for item in items)
gst = subtotal * 0.18
grand_total = subtotal + gst

# Create PDF
pdf = FPDF()
pdf.add_page()

# Title
pdf.set_font("Arial", "B", 18)
pdf.cell(200, 10, "INVOICE", ln=True, align="C")

# Invoice Info
pdf.set_font("Arial", size=12)
pdf.cell(100, 10, f"Client: {client_name}", ln=True)
pdf.cell(100, 10, f"Date: {datetime.now().strftime('%d-%m-%Y')}", ln=True)

pdf.ln(5)

# Table Header
pdf.set_font("Arial", "B", 12)
pdf.cell(70, 10, "Item", border=1, align="C")
pdf.cell(30, 10, "Qty", border=1, align="C")
pdf.cell(40, 10, "Price (Rs.)", border=1, align="C")
pdf.cell(40, 10, "Total (Rs.)", border=1, align="C")
pdf.ln()

# Table Data
pdf.set_font("Arial", size=12)
for item in items:
    pdf.cell(70, 10, item[0], border=1)
    pdf.cell(30, 10, str(item[1]), border=1, align="C")
    pdf.cell(40, 10, f"{item[2]:.2f}", border=1, align="R")
    pdf.cell(40, 10, f"{item[3]:.2f}", border=1, align="R")
    pdf.ln()

# Summary Section
pdf.ln(5)
pdf.set_font("Arial", "B", 12)

pdf.cell(140, 10, "Subtotal", border=0)
pdf.cell(40, 10, f"Rs. {subtotal:.2f}", ln=True, align="R")

pdf.cell(140, 10, "GST (18%)", border=0)
pdf.cell(40, 10, f"Rs. {gst:.2f}", ln=True, align="R")

pdf.cell(140, 10, "Total Amount", border=0)
pdf.cell(40, 10, f"Rs. {grand_total:.2f}", ln=True, align="R")

# Save PDF
pdf.output("invoice.pdf")

# Save to Database
conn = sqlite3.connect("invoice.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS invoices (
    client TEXT,
    item TEXT,
    quantity INTEGER,
    price REAL,
    total REAL
)
""")

for item in items:
    cursor.execute("INSERT INTO invoices VALUES (?, ?, ?, ?, ?)",
                   (client_name, item[0], item[1], item[2], item[3]))

conn.commit()
conn.close()

print("Invoice Generated!")