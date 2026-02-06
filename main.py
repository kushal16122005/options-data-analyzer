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


# Step 2: Find highest IV option

def get_highest_iv(option_chain):
    highest_iv = 0
    highest_iv_option = None

    for option in option_chain:
        if option["iv"] > highest_iv:
            highest_iv = option["iv"]
            highest_iv_option = option

    return highest_iv_option


# Step 3: Calculate Put-Call Ratio (PCR)

def calculate_pcr(option_chain):
    total_put_oi = 0
    total_call_oi = 0

    for option in option_chain:
        if option["type"] == "PE":
            total_put_oi += option["oi"]
        elif option["type"] == "CE":
            total_call_oi += option["oi"]

    return total_put_oi / total_call_oi
       
# Step 4: Market bias based on PCR

def market_bias(pcr):
    if pcr > 1.2:
        return "Bearish"
    elif pcr < 0.8:
        return "Bullish"
    else:
        return "Neutral"

# Step 5: Final Summary
def main():
    highest_iv_option = get_highest_iv(option_chain)
    pcr = calculate_pcr(option_chain)
    bias = market_bias(pcr)

    print("\n--- Options Data Summary --- ")
    print(
        "Highest iv option",
        highest_iv_option["strike"],
        highest_iv_option["type"],
        highest_iv_option["iv"]
    )
    print("PCR:", round(pcr,2))
    print("Market Bias",bias)


if __name__ == "__main__":
    main()

















