/**
 * Created by mrskull on 29.12.16.
 */

import * as dialog_views from './views'
import * as interior_dialog_controllers from './interior/controllers'



/**
 *    Defining public functions
 */

export let

	define = function()
	{
		let
			selectors = dialog_views.selectors;

		$(selectors.container).click(close_with_cancel_event);
		$(selectors.window).click(cancel_event);

		$(selectors.external_buttons).click(open);

		APP.add_own_event('dialog_close', close_with_delay);
		APP.add_own_event('dialog_reload', reload);

		interior_dialog_controllers.define();
	};


/**
 *    Defining events functions
 */

let

	close_with_cancel_event = function(event)
	{
		cancel_event(event);
		close();
	},


	close_with_delay = function()
	{
		let delay;

		if(APP.DATA.delay >= 0)
			delay = APP.DATA.delay;
		else
			delay = 2000;

		setTimeout(close, delay);
	},


	cancel_event = function(event)
	{
		event.stopPropagation();
	};


/**
 *    Defining public functions
 */

export let

	open = function()
	{
		let
			$button = $(this),

			dialog_data = {
				type:     $button.data('type'),
				name:     $button.data('name'),
				value:    $button.data('value'),
				other_1:    $button.data('other_1'),
				other_2:    $button.data('other_2'),
				other_3:    $button.data('other_3'),
			},

			additional_data = {
				additional_name:       $button.data('dialog-name'),
				additional_action:     $button.data('dialog-action'),
				additional_value:      $button.data('dialog-value'),
				additional_reload:     $button.data('dialog-reload'),
				additional_redirect:   $button.data('dialog-redirect'),
				additional_event:      $button.data('dialog-event'),
				additional_url:        $button.data('dialog-url'),
			};

		dialog_views.open(dialog_data, additional_data);
	},


	reload = function()
	{
		dialog_views.reload();
	},


	close = dialog_views.close;