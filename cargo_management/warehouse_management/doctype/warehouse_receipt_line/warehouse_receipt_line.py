from frappe.model.document import Document


class WarehouseReceiptLine(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		height: DF.Float
		length: DF.Float
		parcel: DF.Link
		parcel_customer: DF.Link | None
		parcel_customer_name: DF.ReadOnly | None
		parcel_transportation: DF.ReadOnly | None
		parent: DF.Data
		parentfield: DF.Data
		parenttype: DF.Data
		type: DF.Literal["", "Box", "Envelope", "Pallet", "Mail"]
		volumetric_weight: DF.Float
		warehouse_est_weight: DF.Float
		width: DF.Float
	# end: auto-generated types
	pass
