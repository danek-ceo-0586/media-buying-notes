"""
Zone & Spot ID Whitelist/Blacklist Cleaner
Author: danek-ceo-0586
Description: Utility script to clean, deduplicate, and format ad network zone lists.
"""

def clean_zones(raw_data: str, delimiter: str = ",") -> list:
    """
    Cleans raw zone input: strips whitespace, removes empty lines and duplicates.
    """
    # Split by commas or newlines
    raw_list = raw_data.replace("\n", ",").split(",")
    
    cleaned_zones = []
    seen = set()
    
    for item in raw_list:
        zone = item.strip()
        if zone and zone not in seen:
            seen.add(zone)
            cleaned_zones.append(zone)
            
    return cleaned_zones

def export_formats(zones: list):
    print("=" * 50)
    print(f"       ZONE LIST OPTIMIZER (Total Unique: {len(zones)})")
    print("=" * 50)
    
    print("\n1. Comma-Separated Format (OctoClick / Standard):")
    print(", ".join(zones))
    
    print("\n2. Line-by-Line Format (ClickAdilla / Excel / BeMob):")
    print("\n".join(zones))
    
    print("\n3. Python List Format (For scripts/bots):")
    print(zones)
    print("=" * 50)

if __name__ == "__main__":
    # Example test input with duplicates and spaces
    sample_raw_input = """
    378676, 1464311, 378104, 378676,
    994120,   1464311,
    554210, 378104, 887211
    """
    
    print("Processing sample raw zone data...")
    unique_zones = clean_zones(sample_raw_input)
    export_formats(unique_zones)
