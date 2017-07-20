/**
 * Created by mrskull on 18.07.17.
 */

import {Dialog_Loader_Model} from './model'


export function Dialog_Loader_View(config)
{
	let model = new Dialog_Loader_Model(config);


	this.collect_data = function(button)
	{
		let
			$button = $(button);

		model.variable.post_data = {
			// --- Data for dialog
			dialog_type:    		$button.data('type'),
			dialog_name:    		$button.data('name'),
			dialog_value:    		$button.data('value'),
			dialog_other_1:    		$button.data('other_1'),
			dialog_other_2:    		$button.data('other_2'),
			dialog_other_3:    		$button.data('other_3'),

			// --- Data for button in dialog
			additional_name:       	$button.data('dialog-name'),
			additional_action:   	$button.data('dialog-action'),
			additional_value:      	$button.data('dialog-value'),
			additional_reload:     	$button.data('dialog-reload'),
			additional_redirect:   	$button.data('dialog-redirect'),
			additional_event:      	$button.data('dialog-event'),
			additional_url:        	$button.data('dialog-url'),

			additional_other_1:    	$button.data('dialog-other_1'),
			additional_other_2:    	$button.data('dialog-other_2'),
			additional_other_3:    	$button.data('dialog-other_3'),
		};
	};
	
	
	this.send_request = function()
	{
	    model.prepare_post_data();

		return model.send_request();
	};


	this.send_form = function()
	{
		$(config.form, config.container).submit();
	};


	this.set_loading = function()
	{
		$(model.settings.header).html('<div class="container-part-loading"> Loading... </div>');
		$(model.settings.content).html('<div class="container-part-loading"> Loading... </div>');
	};
}