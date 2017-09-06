/**
 * Created by mrskull on 29.08.17.
 */

export let
	_data = undefined,
	_data_block = undefined,
	_queue = [],
	_request_promise = undefined,
	_request_status = false;

window.queue = _queue;