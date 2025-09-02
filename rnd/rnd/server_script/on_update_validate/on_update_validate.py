def var_set_totals(d):
    rows = d.get('container_barrels') or []
    tg = tt = tn = 0.0
    cnt = 0
    for r in rows:
        if r.get('gross_weight') is not None:
            tg += float(r.get('gross_weight'))
        if r.get('tara_weight') is not None:
            tt += float(r.get('tara_weight'))
        if r.get('net_weight') is not None:
            tn += float(r.get('net_weight'))
        if (r.get('barrel_serial_number') or '').strip():
            cnt += 1
    d.total_gross_weight = tg
    d.total_tara_weight = tt
    d.total_net_weight = tn
    d.barrel_count = cnt

if str(doc.custom_batch_level) == '3':
    var_set_totals(doc)
    if not doc.is_new():
        frappe.db.set_value('Batch AMB', doc.name, {
            'total_gross_weight': doc.total_gross_weight or 0,
            'total_tara_weight': doc.total_tara_weight or 0,
            'total_net_weight': doc.total_net_weight or 0,
            'barrel_count': doc.barrel_count or 0
        })