from app import classify_review, normalize_review

assert normalize_review("GOOD PRODUCT") == "good product"
assert normalize_review("   good    product  ") == "good product"
assert classify_review("It arrived on time") == "unknown"

print("All tests passed")
