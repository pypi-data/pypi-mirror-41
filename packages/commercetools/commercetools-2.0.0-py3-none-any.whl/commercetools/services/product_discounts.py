import typing
from typing import List, Optional

from marshmallow import fields

from commercetools import schemas, types
from commercetools.services import abstract
from commercetools.typing import OptionalListStr

__all__ = ["ProductDiscountService"]


class ProductDiscountDeleteSchema(abstract.AbstractDeleteSchema):
    data_erasure = fields.Bool(data_key="dataErasure", required=False)


class ProductDiscountQuerySchema(abstract.AbstractQuerySchema):
    pass


class ProductDiscountService(abstract.AbstractService):
    def get_by_id(self, id: str) -> Optional[types.ProductDiscount]:
        return self._client._get(f"product-discounts/{id}", {}, schemas.ProductDiscountSchema)

    def query(
        self,
        where: OptionalListStr = None,
        sort: OptionalListStr = None,
        expand: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
    ) -> types.ProductDiscountPagedQueryResponse:
        params = ProductDiscountQuerySchema().dump(
            {
                "where": where,
                "sort": sort,
                "expand": expand,
                "limit": limit,
                "offset": offset,
            }
        )
        return self._client._get(
            "product-discounts", params, schemas.ProductDiscountPagedQueryResponseSchema
        )

    def create(self, draft: types.ProductDiscountDraft) -> types.ProductDiscount:
        return self._client._post(
            "product-discounts",
            {},
            draft,
            schemas.ProductDiscountDraftSchema,
            schemas.ProductDiscountSchema,
        )

    def update_by_id(
        self, id: str, version: int, actions: List[types.ProductDiscountUpdateAction]
    ) -> types.ProductDiscount:
        update_action = types.ProductDiscountUpdate(version=version, actions=actions)
        return self._client._post(
            f"product-discounts/{id}",
            {},
            update_action,
            schemas.ProductDiscountUpdateSchema,
            schemas.ProductDiscountSchema,
        )

    def delete_by_id(
        self, id: str, version: int, data_erasure: bool = False
    ) -> types.ProductDiscount:
        params = ProductDiscountDeleteSchema().dump(
            {"version": version, "data_erasure": data_erasure}
        )
        return self._client._delete(
            f"product-discounts/{id}", params, schemas.ProductDiscountSchema
        )
