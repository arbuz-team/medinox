/**
 * Created by mrskull on 18.07.17.
 */

import {Part_Loader_Dialog} from '../../..//plugin/part_loader/dialog'


export function Dialog_Loader_Model(config)
{

	let part_dialog_loader = new Part_Loader_Dialog(config);

	this.variable = {
		post_data: 		undefined,
		response:		undefined,
	};


	this.prepare_post_data = function()
	{
		let
			new_post_data = {},
			post_data = this.variable.post_data;

		for(let data in post_data)
			if(post_data.hasOwnProperty(data))
				new_post_data[data] = post_data[data] || '';

		this.variable.post_data = new_post_data;
	};


	this.send_request = function()
	{
		return part_dialog_loader.load_content(undefined, this.variable.post_data);
	};
}