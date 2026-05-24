from fastapi import FastAPI
import json

app = FastAPI(title="Product Categories API")

with open("product_category_name_translation.json") as f:
    categories = json.load(f)

@app.get("/categories")
def get_all_categories():
    return categories