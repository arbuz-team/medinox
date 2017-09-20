/**
 * Created by mrskull on 19.09.17.
 */

import {Event_Button} from './controller'



export let

	define_event_button = function(config)
	{
		let $post_buttons = $('.post_button', config.container);

		$post_buttons.each(function()
		{
			new Event_Button(this, config.part_name);
		});
	};