/**
 * Created by mrskull on 19.09.17.
 */

import {Event_Button} from './controller'



export let

	define_event_button = function(config)
	{
		let $buttons = $('.event_button', config.container);

		$buttons.each(function()
		{
			new Event_Button(this, config.part_name);
		});
	};