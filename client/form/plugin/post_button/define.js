/**
 * Created by mrskull on 19.09.17.
 */

import {Post_Button} from './controller'



export let

	define_post_button = function(config)
	{
		let $post_buttons = $('.post_button', config.container);

		$post_buttons.each(function()
		{
			new Post_Button(this, config.part_name);
		});
	};