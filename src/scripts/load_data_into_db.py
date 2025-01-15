import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from sqlalchemy.exc import SQLAlchemyError
from custom_types.db_models import Base  
from utils.db import get_engine, get_session 
from utils.db_insert import (
    insert_order_data,
    insert_product_data,
    insert_aisle_data,
    insert_departments_data,
    insert_einkaufskorb_data,
    insert_tip_bools
)


def main():
    engine = get_engine()

    
    Base.metadata.drop_all(engine)
    print("Tabellen wurden gelöscht.")


    Base.metadata.create_all(engine)
    print("Tabellen wurden erstellt.")

    session = get_session(engine)
    try:
        script_dir = os.path.dirname(os.path.abspath(__file__))
        data_dir = os.path.join(os.path.dirname(script_dir), '..', 'Daten')
        order_data_path = os.path.join(data_dir, 'oders_s.csv')
        product_data_path = os.path.join(data_dir, 'products.csv')
        aisle_data_path = os.path.join(data_dir, 'aisles.csv')
        department_data_path = os.path.join(data_dir, 'departments.csv')
        einkaufskorb_data_path = os.path.join(data_dir, 'oder_products_s.csv')
        tips_data_path = os.path.join(data_dir, 'tips.csv')
        
        
        insert_aisle_data(aisle_data_path, session)
        insert_departments_data(department_data_path, session)
        insert_order_data(order_data_path, session)
        insert_tip_bools(tips_data_path, session)
        insert_product_data(product_data_path, session)
        insert_einkaufskorb_data(einkaufskorb_data_path, session)
        
        
    except SQLAlchemyError as e:
        print("Fehler beim Einfügen in die Datenbank:", e)
        session.rollback()

    finally:
        session.close()

if __name__ == "__main__":
    main()
