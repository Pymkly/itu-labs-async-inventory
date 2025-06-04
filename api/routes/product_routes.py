import psycopg2
from fastapi import APIRouter
from pydantic import BaseModel
from typing import List

from api.database.conn import get_conn
from api.entity.product.product_entity import get_products, to_products, save_products

router = APIRouter()

class ProductItem(BaseModel):
    title: str
    no: int


@router.post("/product")
def save_products_end_point(items:List[ProductItem]):
    conn = None
    cursor = None
    try:
        conn = get_conn()
        cursor = conn.cursor()
        print(items)
        _products = to_products(items)
        save_products(_cursor=cursor,_products=_products)
        conn.commit()
    except psycopg2.Error as e:
        print("Erreur lors de la connexion ou de la requête :", e)
        return None
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()
    return items

@router.get('/product')
async def list_products():
    conn = None
    cursor = None
    try:
        conn = get_conn()
        cursor = conn.cursor()
        report = get_products(cursor)
    except psycopg2.Error as e:
        print("Erreur lors de la connexion ou de la requête :", e)
        return None
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()
    return report