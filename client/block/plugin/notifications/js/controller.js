/**
 * Created by mrskull on 25.08.17.
 */

import {Notifications_View} 		from './view'



export function Notifications_Controller(config)
{
	if(!config || !config.container)
	{
		console.error('Part Loader error: Invalid configuration.');
		return {};
	}


	let
		container = config.container,

		view = new Notifications_View(),
		model = view.model,


		updata_list_notifications = function()
		{
			view.get_list(this).then(view.set_list);
		};


	this.define = function()
	{
		$(model.selector.show_more_button, container).click(updata_list_notifications);
	}
}
