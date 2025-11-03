import pandas as pd

df = pd.read_csv("test.csv")

df = df.drop(columns=["CAP Average","CAP Clean", "CAP Retail", "Sale Agreed Date", "Category", "ParkingLocation", "Branch", "TotalPurchaseIPT", "IPT Amount", "pxwithoverallowance", "Source", "Profit", "Sales Person", "Location", "Trim", "Selling/Margin VAT", "Part Exchange Over Allowance", "StockCosts", "Write Down Total", "Sales Invoice No", "Supplier", "Make and Model", "Sale Type Flag", "IfMarginVAT", "Purchase Total", "Sales Total EX VAT No Commission", "Sales Total Inc VAT No Commission", "FullDiscountAmount", "First Reg Fee", "ExtrasTotal", "Finance Commission", "PPP", "Bonus Total", "PurchasePricePlusMarginVAT", "Non IPT Warranty", "Warranty", "Stock Number", "Customer", "Sale Type Code", "Sales Total Inc VAT", "Delivered to Customer"])

df = df.rename(columns={"FullStockNumber": "Stock Number",
			"IfNotMargin": "VAT on VATQ Sale",
			"Selling Price": "Sales Total Inc VAT"
})


new_order = ["Purchase Type Group", "Purchased By", "Sales Total Inc VAT", "Sales Total EX VAT", "VAT on VATQ Sale", "Sale Type Group", "Stock Number", "Registration", "Supplier Name", "Customer PostCode", "Sale Date", "Purchase Price", "Make", "Model", "Description", "BodyStyle", "Days In Stock", "Sales Executive", "Customer Name", "Chassis Number", "Date of Registration", "Colour", "Purchase Date", "Mileage", "Road Fund Licence Cost", "CherishedFee", "ReconCosts"]

df = df[new_order]

df.loc[df["Customer Name"] == "Yorkshire Vehicle Solutions", "Sales Executive"] = "Rob Milner"
df.loc[df["Customer Name"] == "SAS Cars", "Sales Executive"] = "Rob Milner"
df.loc[df["Customer Name"] == "G3 Remarketing", "Sales Executive"] = "Paul Whinney"
df.loc[df["Customer Name"] == "Mr Andrew Dunne", "Sales Executive"] = "Rob Milner"

df["ReconCosts"] = df["ReconCosts"] - df["Road Fund Licence Cost"].fillna(0)

df.to_csv("output.csv", index=False)

print("Done! Saved as output.csv")
input("Press Enter to exit...")  # <-- keeps the window open