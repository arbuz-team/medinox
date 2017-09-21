/**
 * Created by mrskull on 17.12.16.
 */

import {Event_Button} from './view'
export {Event_Button} from './view'

import {get_and_remove_data} from 'form/js/utilities'
import {event_broker} from 'arbuz/plugin/utilities/event'


Event_Button.prototype.collect_data = function(button)
{
	this._button_data = {
		elem:       button,
		reload:     get_and_remove_data(button, 'reload'),
		redirect:   get_and_remove_data(button, 'redirect'),
		event:      get_and_remove_data(button, 'event'),
		delay:      get_and_remove_data(button, 'delay'),
	};
};


Event_Button.prototype.define_events = function(button)
{
	$(button).click(event_broker(() =>
	{
		if(this._is_not_loading())
		{
			this._set_loading();

			this._run_events();

			this._set_end_loading();
		}
	}));
};