/**
 * Created by mrskull on 19.09.17.
 */


export function Post_Button(button, part_name)
{
	let
		dictionary = APP.dictionary;


	this._button_data = {
		elem:       undefined,
		elem_text:  undefined,
		name:       undefined,
		action:     undefined,
		value:      undefined,
		other_1:    undefined,
		other_2:    undefined,
		other_3:    undefined,
		reload:     undefined,
		redirect:   undefined,
		event:      undefined,
		delay:      undefined,
		url:        undefined,
	};

	this.collect_data(button);


	this._text_data = {
		standard:      this._button_data.elem_text,
		sending:       dictionary.get_word('Sending...'),
		waiting:       dictionary.get_word('Waiting...'),
		done:          dictionary.get_word("It's done!"),
		error:         dictionary.get_word('Error / Resend'),

		delay_after_sending:    500,
		delay_after_done:       1000,
	};


	this._settings = {
		post_url:       this._button_data.url,
		post_name:      '__'+ part_name +'__',
		post_data:      undefined,
	};


	this._variables = {
		is_loading: false,
	};

	this._prepare_post_data();
	this.define_events(button);
}