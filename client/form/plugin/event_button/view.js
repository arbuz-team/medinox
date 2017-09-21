/**
 * Created by mrskull on 18.12.16.
 */

import {Event_Button} from './model'
export {Event_Button} from './model'

import {reload_plugins, redirect_ground, launch_event} from 'form/js/utilities'


Event_Button.prototype._run_events = function()
{
	let events = {
		reload:     this._button_data.reload,
		redirect:   this._button_data.redirect,
		events:     this._button_data.event,
		delay:      this._button_data.delay,
	};

	reload_plugins(events);
	redirect_ground(events);
	launch_event(events);
};