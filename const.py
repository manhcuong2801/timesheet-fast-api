
from datetime import datetime



month = datetime.now().strftime("%b")
month_num = datetime.now().month
year = datetime.now().year
export_day = (
    f"{year}-0{month_num - 1}-21"
    if month_num < 10
    else f"{year}-{month_num - 1}-21"
)
OUT_FILE = f"WorkingdayTemplate.xlsx"

STATUS_OK = ""
STATUS_DAY_OFF = 1
IGNORE_EMP_ID = [
    "ECO0001",  # CEO
    "ECO0003",  # A. Trung Bom
    "ECO0012",  # Ma Nhu
    "ECO0038",  # Chi Chung
    "ECO0089",  # Vuong
    "ECO0345",  # Co Sam
    "ECO",  # May Cham Cong ?? :D ??
]


EMP_OM_ITA = [
    "ECO0419",  # Nguyen Cong Thanh
    "ECO0803",  # Nguyen Van Thang
    "ECO0545",  # Tran Van Nghia
    "ECO0474",  # Tran Dinh Do
    "ECO0709",  # Lo Tien Thanh
    "ECO0710",  # Can Hai Linh
    "ECO0713",  # Pham The Trong
    "ECO0716",  # Bui Doan Quang Huy
    "ECO0717",  # Ngo Manh Quynh
    "ECO0719",  # Tran Anh Vu
    "ECO0591",  # Nguyen Ngoc Phuong Huy
    "ECO0871",  # Nguyen Thanh Tung
    "ECO0873",  # Nguyen Duc Manh
    "ECO0877",  # Nguyn Phu Tien
    "ECO0878",  # Nguyen The Nguyen
    "ECO0881",  # Tran Dinh Duan
    "ECO0923",  # Nguyen Tien Nam
    "ECO0879",  # Nghiem Van Thang
]

NO_CHECKOUT = "NO CHECKOUT"

data = {}

working_days = []
SAMPLE_FILE = "WorkingdayTemplate.xlsx"

datetimeFormat = "%Y-%m-%d %H:%M:%S"

