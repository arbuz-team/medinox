/**
 * Created by mrskull on 31.01.17.
 */

import {Request_Manager} from 'arbuz/plugin/request_manager/_init'


export function Post_Button_Models(config)
{
	let
		that = this,
		dictionary = APP.dictionary;

	this.settings = {
		container:          undefined,
		part_name:          undefined,
		post_name:          undefined,
		button:             undefined,

		button_name:        undefined,
		button_action:      undefined,
		button_value:       undefined,
		button_other_1:     undefined,
		button_other_2:     undefined,
		button_other_3:     undefined,
		button_reload:      undefined,
		button_redirect:    undefined,
		button_event:       undefined,
		button_url:         undefined,

		callback:           undefined,

		text_sending:       dictionary.get_word('Sending...'),
		text_waiting:       dictionary.get_word('Waiting...'),
		text_done:          dictionary.get_word("It's done!"),
		text_error:         dictionary.get_word('Error / Resend'),
		text_standard:      undefined,

		delay_text_waiting: 500,
		delay_text_standard: 1000,
	};

	let load_settings = () =>
	{
		if(typeof config !== 'undefined')
		{
			APP.add_if_isset(config, that.settings, 'container');
			APP.add_if_isset(config, that.settings, 'part_name');
			this.settings.post_name = '__'+ this.settings.part_name +'__';

			APP.add_if_isset(config, that.settings, 'callback');

			APP.add_if_isset(config, that.settings, 'button');

			APP.add_if_isset(config, that.settings, 'button_name');
			APP.add_if_isset(config, that.settings, 'button_action');
			APP.add_if_isset(config, that.settings, 'button_value');
			APP.add_if_isset(config, that.settings, 'button_other_1');
			APP.add_if_isset(config, that.settings, 'button_other_2');
			APP.add_if_isset(config, that.settings, 'button_other_3');
			APP.add_if_isset(config, that.settings, 'button_reload');
			APP.add_if_isset(config, that.settings, 'button_redirect');
			APP.add_if_isset(config, that.settings, 'button_event');
			APP.add_if_isset(config, that.settings, 'button_url');

			APP.add_if_isset(config, that.settings, 'button_html', 'text_standard');
		}
	};

	load_settings();


	/////////////////////////

	this.state = {
		is_loading: false,
	};


	this.is_loading = function()
	{
		return that.state.is_loading;
	};


	/////////////////////////

	let prepare_post_data = function()
	{
		let
			data = {},
			value = that.settings.button_value;

		data[that.settings.post_name] = 'button';
		data._name_= that.settings.button_action;

		if(value)
			data.value = value;

		data.other_1 = that.settings.button_other_1 || '';
		data.other_2 = that.settings.button_other_2 || '';
		data.other_3 = that.settings.button_other_3 || '';

		return data;
	};


	this.send_post = function()
	{
		return new Promise(resolve =>
		{
			setTimeout(function()
			{
				let
					post_url = that.settings.button_url,
					post_data = prepare_post_data(),
					request_manager = new Request_Manager();


				request_manager.send(post_url, post_data).then(resolve);
			}, 200);
		});
	};

}