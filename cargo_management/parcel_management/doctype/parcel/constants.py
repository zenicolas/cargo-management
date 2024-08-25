from enum import StrEnum


class Status(StrEnum):
	""" Parcel Statuses """

	AWAITING_RECEIPT = 'Awaiting Receipt'
	AWAITING_CONFIRMATION = 'Awaiting Confirmation'
	IN_EXTRAORDINARY_CONFIRMATION = 'In Extraordinary Confirmation'  # FIXME: We can remove "IN"
	AWAITING_DEPARTURE = 'Awaiting Departure'
	IN_TRANSIT = 'In Transit'
	IN_CUSTOMS = 'In Customs'
	SORTING = 'Sorting'
	TO_BILL = 'To Bill'
	UNPAID = 'Unpaid'
	FOR_DELIVERY_OR_PICKUP = 'Delivery or Pickup'  # FIXME, we can make to DELIVERY_OR_PICKUP
	FINISHED = 'Finished'
	CANCELLED = 'Cancelled'
	NEVER_ARRIVED = 'Never Arrived'
	RETURNED_TO_SENDER = 'Returned to Sender'


class StatusMessage(StrEnum):
	# Awaiting Receipt Explanations
	TRANSPORTATION_NOT_DELIVERED_YET = 'The package has not yet been delivered by the transport company.'
	ESTIMATED_DELIVERY_DATE_TODAY = 'The scheduled delivery date is today.'
	ESTIMATED_DELIVERY_DATE_TOMORROW = 'The scheduled date is tomorrow.'
	ESTIMATED_DELIVERY_DATE = 'The scheduled date is: [DATE]'
	DELAYED_DELIVERY_DATE = 'It is delayed. It should have been delivered on: [DATE]'
	NOT_DELIVERY_DATE_ESTIMATED = 'No estimated delivery date has been indicated.'

	TRANSPORTATION_DELIVERED_DATE = 'The carrier indicated that it was delivered: [DATE]'
	SIGNED_BY = 'Signed by: [SIGNER]'
	HAS_BEEN_1_DAY = 'It's been 1 day'
	HAS_BEEN_X_DAYS = 'It's been [DAYS] days'
	WAIT_FOR_24_HOURS_CONFIRMATION = 'Please allow 24 business hours for the warehouse to confirm receipt.'
	TRANSPORTER_INDICATE_ESTIMATE_DELIVERY_DATE = 'The carrier indicated an estimated delivery date: [DATE]'
	PACKAGE_IN_EXTRAORDINARY_REVISION = 'The package is currently undergoing an extraordinary review.'
	TRANSPORTER_DELIVERY_DATE = 'The carrier indicated that it delivered the package on: [DATE].'
	NO_CARGO_SHIPPING = 'There is no cargo shipment'
	PACKAGE_IN_TRANSIT_TO_DESTINATION = 'The package is in transit to destination.'	
	DEPARTURE_DATE = 'Dispatch date: [DATE]'
	ESTIMATED_RECEPTION_DATE = 'Expected date of receipt in Managua: [DATE]'
	CARGO_SHIPMENT = 'Shipment: [SHIPMENT]'
	PACKAGE_IN_CUSTOMS = 'The package is in the process of customs clearance.'
	PACKAGE_IN_OFFICE_SORTING = 'The package is being sorted in the office.'
	PACKAGE_READY = 'The package is ready to be picked up.'
	PACKAGE_FINISHED = 'Package finished.'
	CONTACT_AGENT_FOR_PACKAGE_INFO = 'Contact an agent for more information about the package.'
	PACKAGE_NEVER_ARRIVED = 'The package did not arrive at the warehouse.'
	PACKAGE_RETURNED = 'The package was returned by the carrier to the seller.'
	CONTACT_FOR_MORE_INFO = 'Contact your seller and/or carrier for more information.'

	CONTACT_YOUR_PROVIDER_FOR_INFO = 'Contact your provider for more information.'
