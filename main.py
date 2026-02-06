# Options Data Analyzer
# Step 1: Sample option chain data

option_chain = [
    {"strike": 25200, "type": "CE", "oi": 120000, "iv": 18.2},
    {"strike": 25200, "type": "PE", "oi": 180000, "iv": 19.1},
    {"strike": 25300, "type": "CE", "oi": 150000, "iv": 17.5},
    {"strike": 25300, "type": "PE", "oi": 210000, "iv": 18.9},
    {"strike": 25400, "type": "CE", "oi": 130000, "iv": 16.8},
    {"strike": 25400, "type": "PE", "oi": 160000, "iv": 17.2},
]
print("option chain data loaded successfully")

# Step 2: Find highest IV option

highest_iv = 0
highest_iv_option = None

for option in option_chain:
    if option["iv"] > highest_iv:
        highest_iv = option["iv"]
        highest_iv_option = option

print(
    "Highest IV:",
    highest_iv_option["strike"],
    highest_iv_option["type"],
    "(" + str(highest_iv_option["iv"]) + ")"
)

# Step 3: Calculate Put-Call Ratio (PCR)

total_put_oi = 0
total_call_oi = 0

for option in option_chain:
    if option["type"] == "PE":
        total_put_oi += option["oi"]
    elif option["type"] == "CE":
        total_call_oi += option["oi"]

pcr = total_put_oi / total_call_oi

print("total Put OI:", total_put_oi)
print("total Call OI:", total_call_oi)
print("PCR:", round(pcr,2))
       















