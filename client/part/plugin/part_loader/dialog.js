/**
 * Created by mrskull on 17.07.17.
 */

import {Request_Manager_Dialog} from '../../../arbuz/plugin/request_manager/dialog'
import {Part_Loader} from './_controller'




export function Part_Loader_Dialog(config)
{
	Part_Loader.call(this, config);
}

Part_Loader_Dialog.prototype = Object.create(Part_Loader.prototype);






// ------------------------------------------


Part_Loader_Dialog.prototype.send_request = function(actually_url)
{
	let
		post_data = this.variables.post_data,
		request_manager = new Request_Manager_Dialog();

	this.response = request_manager.send(actually_url, post_data);
};




Part_Loader_Dialog.prototype.close_dialog_if_json = function(response, status)
{
	if(status !== 'success')
		return false;

	if(response === '{"__form__": "true"}')
	{
		APP.DATA.delay = 0;
		APP.throw_event(EVENTS.part.close_dialog);
		return true;
	}

	return false;
};


Part_Loader_Dialog.prototype.load_content = function(url, post_data, callback)
{
	this.variables.url = url;
	this.external_callback = callback;


	this.prepare_content_to_change(url, post_data);

	this.send_request(url);

	this.hide_content().then(() =>
	{
		this.receive_response().then((data) =>
		{
			if(this.close_dialog_if_json(data))
				return false;

			this.prepare_content_to_show(data);

			this.show_content().then(() =>
			{
				this.after_show_content(data);
			});
		});
	});
};