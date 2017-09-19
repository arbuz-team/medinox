/**
 * Created by mrskull on 17.12.16.
 */

import {Post_Button} from './view'
export {Post_Button} from './view'

import {get_and_remove_data} from 'form/js/utilities'
import {event_broker} from 'arbuz/plugin/utilities/event'



// Post_Button.prototype._manage_buttons = function(event)
// {
// 	event.preventDefault();
// 	event.stopPropagation();
//
// 	let
// 		button_id = this;
//
// 	if(buttons_views[button_id])
// 		buttons_views[button_id].start();
// 	else
// 	{
// 		console.group('Button doesn\'t exsist');
// 		console.error(button_id);
// 		console.groupEnd();
// 	}
// };


let
	get_button_text = function(button)
	{
		let $button = $(button);

		if($button.hasClass('is-text_icon'))
			return $button.find('.button-text').html();
		else
			return $button.html();
	};


Post_Button.prototype.collect_data = function(button)
{
	this._button_data = {
		elem:       button,
		elem_text:  get_button_text(button),
		name:       get_and_remove_data(button, 'name'),
		action:     get_and_remove_data(button, 'action'),
		value:      get_and_remove_data(button, 'value'),
		other_1:    get_and_remove_data(button, 'other_1'),
		other_2:    get_and_remove_data(button, 'other_2'),
		other_3:    get_and_remove_data(button, 'other_3'),
		reload:     get_and_remove_data(button, 'reload'),
		redirect:   get_and_remove_data(button, 'redirect'),
		event:      get_and_remove_data(button, 'event'),
		delay:      get_and_remove_data(button, 'delay'),
		url:        get_and_remove_data(button, 'url'),
	};
};


Post_Button.prototype.define_events = function(button)
{
	$(button).click(event_broker(() =>
	{
		if(this._is_not_loading())
		{
			this._set_loading();

			this._set_text_sending()
				.then(() => this._set_text_waiting());

			this._send().then((response) =>
			{
				this._set_end_loading();

				if(this._is_error(response))
					this._set_text_error();

				else
				{
					this._run_events();

					this._set_text_done()
						.then(() => this._set_text_standard());
				}
			});
		}
	}));
};