from sqlmodel import Field , SQLModel

class Survey(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str
    age: int 
    gender: str
    marital_status: str 
    address: str
    contact_number: int 
    interest: str
    program: str
    year_level: str
    career_path: str
 
    

