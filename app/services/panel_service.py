from sqlalchemy.orm import Session
from app.models import Panel
from app.schemas_panel import PanelCreate, PanelUpdate

# Obecná funkce pro odstranění záznamu podle ID a modelu
def delete_record_by_id(model, record_id: int, db: Session):
    record = db.get(model, record_id)
    if record:
        db.delete(record)
        db.commit()
        return True
    return False

# Přidání nového panelu
def add_panel(panel_data: PanelCreate, db: Session):
    panel = Panel(**panel_data.model_dump())
    db.add(panel)
    db.commit()
    db.refresh(panel)
    return panel

# Získání všech panelů (s možností filtru podle viditelnosti)
def get_all_panels(visible_only: bool, db: Session):
    query = db.query(Panel)
    if visible_only:
        query = query.filter(Panel.visible == True)
    return query.all()

# Získání jednoho panelu podle ID
def get_panel_by_id(panel_id: int, db: Session):
    return db.query(Panel).filter(Panel.id == panel_id).first()

# Aktualizace viditelnosti panelu
def update_panel_visibility(panel_id: int, panel_update: PanelUpdate, db: Session):
    panel = db.query(Panel).filter(Panel.id == panel_id).first()
    if not panel:
        return None
    panel.visible = panel_update.visible
    db.commit()
    db.refresh(panel)
    return panel

def update_panel(panel_id: int, panel_data: PanelUpdate, db: Session):
    panel = db.query(Panel).filter(Panel.id == panel_id).first()
    if not panel:
        return None

    # Přes exclude_unset=True se vezmou jen ta pole, která klient skutečně poslal
    to_update = panel_data.model_dump(exclude_unset=True)

    # Pro každé pole, které klient poslal, nastavíme tu hodnotu do panelu
    for field, value in to_update.items():
        setattr(panel, field, value)

    db.commit()
    db.refresh(panel)
    return panel

# Mazání panelu – Použití obecné funkce
def delete_panel(panel_id: int, db: Session):
    return delete_record_by_id(Panel, panel_id, db)
