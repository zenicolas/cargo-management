import frappe


@frappe.whitelist(methods='GET')
def get_packages_and_wr_in_cargo_shipment(cargo_shipment: str):
	""" Get all packages and warehouse receipts connected to a cargo shipment. """

	# TODO: Delete: wrs and warehouse_receipts in sql
	# wrs = frappe.get_all('Cargo Shipment Line', fields='warehouse_receipt', filters={'parent': cargo_shipment}, order_by='idx', pluck='warehouse_receipt')

	# TODO: WORKING: OPTIMIZE FULL
	VIA_SQL = "CONCAT('Via: ', IF(p.transportation = 'Air', 'Aereo', 'Maritimo'))"

	packages = frappe.db.sql("""
 		SELECT
 			p.name, p.tracking_number, p.customer, p.customer_name, p.carrier_est_weight,
 			CONCAT(
 				IF(COUNT(pc.tracking_number) > 0, CONCAT({via_sql}, '\n\n'), ''),
 				GROUP_CONCAT(DISTINCT
 					pc.description,
 					IF(pc.tracking_number > '', CONCAT('\nTracking Number: ', pc.tracking_number), ''),

 					IF(pc.amount > 0,      CONCAT('\nDeclared Value: $', FORMAT(pc.amount, 2)), ''),
 					IF(pc.item_code > '',  CONCAT('\nCode: ', pc.item_code), ''),
 					IF(pc.import_rate > 0, CONCAT('\nRate: $', FORMAT(pc.import_rate, 2)), '')
 					ORDER BY pc.idx SEPARATOR '\n\n'
 				),
 				IF(COUNT(pc.tracking_number) = 0, CONCAT('\n\n', {via_sql}), ''),
 				IF(p.name != p.tracking_number, CONCAT(IF(COUNT(pc.tracking_number) > 0, '\n', ''), '\nTracking Number FINAL: ', p.tracking_number), '')
 			) AS customer_description
 		FROM tabParcel p
 			LEFT JOIN `tabParcel Content` pc ON pc.parent = p.name
 			INNER JOIN `tabCargo Shipment Line` csl ON csl.package = p.name
 		WHERE csl.parent = %(cargo_shipment)s
 		GROUP BY p.name
 		ORDER BY p.customer_name
 	""".format(via_sql=VIA_SQL), {
 		'cargo_shipment': cargo_shipment
 	}, as_dict=True)
	
	return {
		'packages': packages
	}
