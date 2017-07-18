/**
 * Created by mrskull on 18.12.16.
 */

import {Event_Button_Models} from './models'
import * as utilities from 'form/js/utilities'


export let Event_Button_Views = function(config)
{

	let
		models = new Event_Button_Models(config);

	this.models = models;


	this.start = function()
	{
		let events = {
			reload: models.settings.button_reload,
			redirect: models.settings.button_redirect,
			events: models.settings.button_event,
			delay: models.settings.button_delay,
		};

		utilities.reload_plugins(events);
		utilities.redirect_ground(events);
		utilities.launch_event(events);
	};

};