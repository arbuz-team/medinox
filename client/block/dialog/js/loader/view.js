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
			_type_:    		    $button.data('type'),
			_name_:    		    $button.data('name'),
			value:    		    $button.data('value'),
			other_1:    		$button.data('other_1'),
			other_2:    		$button.data('other_2'),
			other_3:    		$button.data('other_3'),

			// --- Data for button in dialog
			accept_name:       	$button.data('dialog-name'),
			accept_action:   	$button.data('dialog-action'),
			accept_value:      	$button.data('dialog-value'),
			accept_reload:     	$button.data('dialog-reload'),
			accept_redirect:   	$button.data('dialog-redirect'),
			accept_event:      	$button.data('dialog-event'),
			accept_url:        	$button.data('dialog-url'),

			accept_other_1:    	$button.data('dialog-other_1'),
			accept_other_2:    	$button.data('dialog-other_2'),
			accept_other_3:    	$button.data('dialog-other_3'),
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


	this.set_text = function(data)
	{
		let content =
			'<div class="dialog-content-part">'+ data.content +'</div>' +
			'<div class="dialog-content-part">'+
				'<button class="button event_button"' +
						'type="button"' +
						'data-name="button_close_dialog"' +
						'data-event="part.close_dialog">' +
					'Close</button>' +
			'</div>'

		$(model.settings.header).html(data.title);
		$(model.settings.content).html(content);
	};


	this.set_loading = function()
	{
		this.set_text({
			title: '<div class="container-part-loading"> Loading... </div>',
			content: '<div class="dialog-message"> Loading... </div>',
		})
	};
}