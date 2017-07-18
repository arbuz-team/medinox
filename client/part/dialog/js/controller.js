/**
 * Created by mrskull on 29.12.16.
 */

import {Dialog_Designer_Controller} from './designer/controller'
import {Dialog_Loader_Controller} from './loader/controller'



let
	config = {
		name:				'dialog',
		html_id: 			'#DIALOG',
		container: 			'.dialog',
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
			loading.then(designer.unset_loading);
		});
	},


	close = function()
	{
		designer.close().then(() =>
		{
			loader.define();
		});
	},


	open = function()
	{
		let loading = loader.get_content(this);

		designer.open().then(() =>
		{
			loading.then(loader.define);
		});
	};

	// ---------------------------------------------


export let

	define = function()
	{
		designer.define();

		$(config.external_button).click(open);
		APP.add_own_event('dialog_close', close);
		//APP.add_own_event('dialog_reload', reload);
	};