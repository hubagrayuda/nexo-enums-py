from enum import StrEnum
from pydantic import BaseModel, Field
from typing import Annotated, Generic, Sequence, TypeVar
from nexo.types.string import ListOfStrs


class ServiceType(StrEnum):
    BACKEND = "backend"
    FRONTEND = "frontend"

    @classmethod
    def choices(cls) -> ListOfStrs:
        return [e.value for e in cls]


ServiceTypeT = TypeVar("ServiceTypeT", bound=ServiceType)
OptServiceType = ServiceType | None
OptServiceTypeT = TypeVar("OptServiceTypeT", bound=OptServiceType)


class SimpleServiceTypeMixin(BaseModel, Generic[OptServiceTypeT]):
    type: Annotated[OptServiceTypeT, Field(..., description="Service Type")]


class FullServiceTypeMixin(BaseModel, Generic[OptServiceTypeT]):
    service_type: Annotated[OptServiceTypeT, Field(..., description="Service Type")]


ListOfServiceTypes = list[ServiceType]
ListOfServiceTypesT = TypeVar("ListOfServiceTypesT", bound=ListOfServiceTypes)
OptListOfServiceTypes = ListOfServiceTypes | None
OptListOfServiceTypesT = TypeVar("OptListOfServiceTypesT", bound=OptListOfServiceTypes)


class SimpleServiceTypesMixin(BaseModel, Generic[OptListOfServiceTypesT]):
    types: Annotated[OptListOfServiceTypesT, Field(..., description="Service Types")]


class FullServiceTypesMixin(BaseModel, Generic[OptListOfServiceTypesT]):
    service_types: Annotated[
        OptListOfServiceTypesT, Field(..., description="Service Types")
    ]


SeqOfServiceTypes = Sequence[ServiceType]
SeqOfServiceTypesT = TypeVar("SeqOfServiceTypesT", bound=SeqOfServiceTypes)
OptSeqOfServiceTypes = SeqOfServiceTypes | None
OptSeqOfServiceTypesT = TypeVar("OptSeqOfServiceTypesT", bound=OptSeqOfServiceTypes)


class ServiceCategory(StrEnum):
    CORE = "core"
    AI = "ai"

    @classmethod
    def choices(cls) -> ListOfStrs:
        return [e.value for e in cls]


ServiceCategoryT = TypeVar("ServiceCategoryT", bound=ServiceCategory)
OptServiceCategory = ServiceCategory | None
OptServiceCategoryT = TypeVar("OptServiceCategoryT", bound=OptServiceCategory)


class SimpleServiceCategoryMixin(BaseModel, Generic[OptServiceCategoryT]):
    category: Annotated[OptServiceCategoryT, Field(..., description="Service Category")]


class FullServiceCategoryMixin(BaseModel, Generic[OptServiceCategoryT]):
    service_category: Annotated[
        OptServiceCategoryT, Field(..., description="Service Category")
    ]


ListOfServiceCategories = list[ServiceCategory]
ListOfServiceCategoriesT = TypeVar(
    "ListOfServiceCategoriesT", bound=ListOfServiceCategories
)
OptListOfServiceCategories = ListOfServiceCategories | None
OptListOfServiceCategoriesT = TypeVar(
    "OptListOfServiceCategoriesT", bound=OptListOfServiceCategories
)


class SimpleServiceCategoriesMixin(BaseModel, Generic[OptListOfServiceCategoriesT]):
    categories: Annotated[
        OptListOfServiceCategoriesT, Field(..., description="Service Categories")
    ]


class FullServiceCategoriesMixin(BaseModel, Generic[OptListOfServiceCategoriesT]):
    service_categories: Annotated[
        OptListOfServiceCategoriesT, Field(..., description="Service Categories")
    ]


SeqOfServiceCategories = Sequence[ServiceCategory]
SeqOfServiceCategoriesT = TypeVar(
    "SeqOfServiceCategoriesT", bound=SeqOfServiceCategories
)
OptSeqOfServiceCategories = SeqOfServiceCategories | None
OptSeqOfServiceCategoriesT = TypeVar(
    "OptSeqOfServiceCategoriesT", bound=OptSeqOfServiceCategories
)
