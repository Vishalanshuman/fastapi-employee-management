import enum

class DepartmentEnum(str, enum.Enum):
    hr = "hr"
    engineering = "engineering"
    sales = "sales"

class RoleEnum(str, enum.Enum):
    manager = "manager"
    developer = "developer"
    analyst = "analyst"
