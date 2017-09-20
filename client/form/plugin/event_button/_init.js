/**
 * Created by mrskull on 19.09.17.
 */


export function Event_Button(button)
{
	this._button_data = {
		elem:       undefined,

		reload:     undefined,
		redirect:   undefined,
		event:      undefined,
		delay:      undefined,
	};

	this._variables = {
		is_loading: false,
	};

	this.collect_data(button);
	this.define_events(button);
}