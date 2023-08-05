function(doc) {
	if (doc.type == 'slot-info') {
		emit(doc.date, {slot: doc.slot, build_id: doc.build_id});
	}
}
