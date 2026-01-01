from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from typing import List
from database import session, engine
import db_models  # SQLAlchemy ORM model
from ProductModel import Product  # Pydantic model

# Create tables in the database
db_models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Product API")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
     allow_credentials=True,
    allow_methods=["*"],                       # allows all methods (GET, POST, etc.)
    allow_headers=["*"]  
)
# ---------- Routes ----------
@app.get("/")
def greet():
    return {"message": "Haseeb How are You"}



@app.get("/products")
def Get_All_products():
    db= session()
    products=db.query(db_models.Product).all()
    db.close()
    return products

@app.get("/products/{id}")
def Search_Product(id : int):
    db = session()
    product= db.query(db_models.Product).filter(db_models.Product.id==id).first()
    db.close()
    
    if product:
        return product
    else:
        raise HTTPException(status_code=404,detail="Product not found")
    
    
@app.post("/products")
def Add_Products(product: Product):
    db=session()
    product= db.add(db_models.Product(**product.model_dump()))
    db.commit()
    db.close()
    
    return product


@app.put("/products/{id}")
def Update(id : int, new_product: Product):
    db= session()
    product=db.query(db_models.Product).filter(db_models.Product.id==id).first()
    if not product:
        db.close()
        raise HTTPException(status_code=404, detail="Product not Found")
    
    product.name=new_product.name
    product.description=new_product.description
    product.price=new_product.price
    product.quantity=new_product.quantity
    
    db.commit()
    db.refresh(product)
    db.close()
    return product

@app.delete("/products/{id}")
def delete_Product(id : int):
    db = session()
    product= db.query(db_models.Product).filter(db_models.Product.id==id).first()
    if not product:
        db.close()
        raise HTTPException(status_code=404,detail="Error Not Found!")
    
    db.delete(product)
    db.commit()
    db.close()
    return "Product Deleted Sucessfully"