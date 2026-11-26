"""
Campaign Unit Economics & ROI Calculator
Author: danek-ceo-0586
Description: Basic CLI tool to calculate CTR, CR, CPA, Net Profit, and ROI for ad campaigns.
"""

def calculate_metrics(impressions, clicks, conversions, spend, revenue):
    print("=" * 45)
    print("       CAMPAIGN PERFORMANCE REPORT")
    print("=" * 45)
    
    # 1. CTR (Click-Through Rate)
    ctr = (clicks / impressions * 100) if impressions > 0 else 0.0
    print(f"CTR (Click-Through Rate):     {ctr:.2f}%")
    
    # 2. CR (Conversion Rate)
    cr = (conversions / clicks * 100) if clicks > 0 else 0.0
    print(f"CR (Conversion Rate):         {cr:.2f}%")
    
    # 3. CPA (Cost Per Action)
    cpa = (spend / conversions) if conversions > 0 else 0.0
    print(f"CPA (Cost Per Conversion):   ${cpa:.2f}")
    
    # 4. Net Profit
    profit = revenue - spend
    print(f"Net Profit / Loss:           ${profit:.2f}")
    
    # 5. ROI (Return on Investment)
    if spend > 0:
        roi = (profit / spend) * 100
        print(f"ROI:                          {roi:.2f}%")
    else:
        roi = 0.0
        print("ROI:                          N/A (Zero Spend)")
        
    print("-" * 45)
    
    # Verdict logic
    if profit > 0:
        print("STATUS: [PROFITABLE] -> Consider scaling.")
    elif profit == 0:
        print("STATUS: [BREAK-EVEN] -> Requires optimization.")
    else:
        print("STATUS: [NEGATIVE]   -> Cut non-performing zones.")
    print("=" * 45)

if __name__ == "__main__":
    # Test case: Popunder mobile traffic sample
    test_impressions = 15000
    test_clicks = 1200
    test_conversions = 18
    test_spend = 12.50
    test_revenue = 18.00

    print("Running test calculation with sample data...")
    calculate_metrics(
        impressions=test_impressions,
        clicks=test_clicks,
        conversions=test_conversions,
        spend=test_spend,
        revenue=test_revenue
    )
