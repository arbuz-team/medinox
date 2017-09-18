/**
 * Created by mrskull on 17.12.16.
 */

import {Post_Button_Views} from './views'
import {get_and_remove_data} from 'form/js/utilities'


export let Post_Button_Controllers = function(config)
{
	if(typeof config === 'undefined' && typeof config.container === 'undefined')
	{
		console.error('Exeption error: invalid container.');
		return {};
	}


	let
		buttons_views = {},


		manage_buttons = function(event)
		{
			event.preventDefault();
			event.stopPropagation();

			let
				button_id = this;

			if(buttons_views[button_id])
				buttons_views[button_id].start();
			else
			{
				console.group('Button doesn\'t exsist');
				console.error(button_id);
				console.groupEnd();
			}
		},


		create_button_views = function()
		{
			let
				button_id = this;
			config.button = this;

			config.button_name =        get_and_remove_data(this, 'name');
			config.button_action =      get_and_remove_data(this, 'action');
			config.button_value =       get_and_remove_data(this, 'value');
			config.button_other_1 =     get_and_remove_data(this, 'other_1');
			config.button_other_2 =     get_and_remove_data(this, 'other_2');
			config.button_other_3 =     get_and_remove_data(this, 'other_3');
			config.button_reload =      get_and_remove_data(this, 'reload');
			config.button_redirect =    get_and_remove_data(this, 'redirect');
			config.button_event =       get_and_remove_data(this, 'event');
			config.button_url =         get_and_remove_data(this, 'url');

			if($(this).hasClass('is-text_icon'))
				config.button_html = $(this).find('.button-text').html();
			else
				config.button_html = $(this).html();

			buttons_views[button_id] = new Post_Button_Views(config);
		};


	this.define = function()
	{
		let $post_buttons = $('.post_button', config.container);

		$post_buttons.each(create_button_views);

		$post_buttons.click(manage_buttons);
	};
};