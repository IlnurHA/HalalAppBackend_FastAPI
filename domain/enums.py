from enum import Enum


class LegalType(str, Enum):
    NOT_SET = "Not set"
    INDIVIDUAL_ENTREPRENEUR = "Individual Entrepreneur"
    LIMITED_LIABILITY_COMPANY = "Limited Liability Company"
    JOINT_STOCK_COMPANY = "Joint Stock Company"
    GROUP_OF_COMPANIES = "Group Of Companies"
    CLOSED_JOINT_STOCK_COMPANY = "Closed Joint Stock Company"


class ContactTypes(str, Enum):
    EMAIL = "Email"
    PHONE = "Phone"
    TELEGRAM = "Telegram"
    WHATSUP = "What's App"
    VK = "VK"
    LANDMARK = "Landmark"
    WEBSITE = "Website"


class FoodPointTypes(str, Enum):
    CAFE = "cafe"
    CANTEEN = "canteen"
    RESTAURANT = "restaurant"
    STREET_FOOD = "street_food"
    BAKERY = "bakery"
    SUSHI_BAR = "sushi_bar"
    BURGER_JOINT = "burger_joint"
    QUICK_SERVICE_RESTAURANT = "quick_service_restaurant"
    GAS_STATION = "gas_station"
    HALAL_STORE = "halal_store"


class CuisineTypes(str, Enum):
    ASIAN = "asian"
    TATAR = "tatar"
    EUROPEAN = "european"
    TURKISH = "turkish"
    EASTERN = "eastern"
    HOMEMADE_MEALS = "homemade_meals"
    BAKED_PRODUCTS = "baked_products"
    FAST_FOOD = "fast_food"
    MIXED = "mixed"


class DaysOfWeek(str, Enum):
    MONDAY = "Monday"
    TUESDAY = "Tuesday"
    WEDNESDAY = "Wednesday"
    THURSDAY = "Thursday"
    FRIDAY = "Friday"
    SATURDAY = "Saturday"
    SUNDAY = "Sunday"


class ExceptionalDayReason(str, Enum):
    MAINTENANCE_WORK = "Maintenance Work"
    HOLIDAY_NON_WORKING_DAY = "Holiday Non Working Day"


class Permissiveness(str, Enum):
    HALAL = "halal"
    HARAM = "haram"
    DOUBTFUL = "doubtful"
