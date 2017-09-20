/**
 * Created by mrskull on 29.12.16.
 */

import {Dialog_Designer_Controller} from './designer/controller'
import {Dialog_Loader_Controller} from './loader/controller'


export function Dialog_Controller()
{
	if(typeof Dialog_Controller.instance === 'object')
		return Dialog_Controller.instance;

	Dialog_Controller.instance = this;


	let
		config = {
			part_name:				'dialog',
			html_id: 			'#DIALOG',
			container: 			'.dialog',
			header: 	        '.dialog-header',
			content: 	        '.dialog-content',
			internal_button: 	'.dialog_send',
			external_button: 	'.dialog_button',
			form: 				'.dialog_form',

			duration_show: 0,
			duration_hide: 0,
		},

		designer = new Dialog_Designer_Controller(config),
		loader = new Dialog_Loader_Controller(config),


		// ---------------------------------------------

		reload = function()
		{
			let loading = loader.reload_content(this);

			designer.set_loading().then(() =>
			{
				loading.then(() =>
				{
					// loader.define();
					designer.unset_loading();
				});
			});
		},


		close = function()
		{
			designer.close().then(loader.set_loading);
		},


		close_with_cancel_event = function()
		{
			designer.close_with_cancel_event(event).then(loader.set_loading);
		},


		open = function()
		{
			let loading = loader.get_content(this);

			designer.open().then(() =>
			{
				// loading.then(loader.define);
			});
		},


		open_with_my_text = function(event)
		{
			let
				title = event.detail.title,
				content = event.detail.content;

			designer.open().then(() =>
			{
				loader.set_text({
					title: title,
					content: content,
				});
			});
		};


	this.define = function()
	{
		designer.define();
		loader.define();

		$(config.html_id).click(close_with_cancel_event);
		$(config.external_button).click(open);
		APP.add_own_event('dialog_close', close);
		APP.add_own_event('dialog_reload', reload);
		APP.add_own_event('open_dialog_with_text', open_with_my_text);
	};
}