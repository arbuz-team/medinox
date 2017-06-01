/**
 * Created by mrskull on 31.01.17.
 */


export let Post_Button_Models = function(config)
{
	let
		that = this,
		dictionary = window.APP.dictionary;

	this.settings = {
		container:          undefined,
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

	let load_settings = function()
	{
		if(typeof config !== 'undefined')
		{
			window.APP.add_if_isset(config, that.settings, 'container');

			window.APP.add_if_isset(config, that.settings, 'callback');

			window.APP.add_if_isset(config, that.settings, 'button');

			window.APP.add_if_isset(config, that.settings, 'button_name');
			window.APP.add_if_isset(config, that.settings, 'button_action');
			window.APP.add_if_isset(config, that.settings, 'button_value');
			window.APP.add_if_isset(config, that.settings, 'button_other_1');
			window.APP.add_if_isset(config, that.settings, 'button_other_2');
			window.APP.add_if_isset(config, that.settings, 'button_other_3');
			window.APP.add_if_isset(config, that.settings, 'button_reload');
			window.APP.add_if_isset(config, that.settings, 'button_redirect');
			window.APP.add_if_isset(config, that.settings, 'button_event');
			window.APP.add_if_isset(config, that.settings, 'button_url');

			window.APP.add_if_isset(config, that.settings, 'button_html', 'text_standard');
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
			obj = {__button__: that.settings.button_action},
			value = that.settings.button_value,
			other_1 = that.settings.button_other_1,
			other_2 = that.settings.button_other_2,
			other_3 = that.settings.button_other_3;

		if(value)
			obj.value = value;
		if(other_1)
			obj.other_1 = value;
		if(other_2)
			obj.other_2 = value;
		if(other_3)
			obj.other_3 = value;

		return obj;
	};


	this.send_post = function(callback)
	{
		setTimeout(function()
		{
			let
				url = that.settings.button_url,
				post_data = prepare_post_data();

			window.APP.http_request(url, post_data, callback);
		}, 200);
	};

};