/**
 * Created by mrskull on 17.07.17.
 */

import {data_controller} from '../../../arbuz/js/structure'
import {Part_Loader} from './_init'
import './_model'
import './_view'

export {Part_Loader} from './_init'




Part_Loader.prototype.redirect = function()
{
	let
		url = data_controller.get('path'),
		delay = 0,
		variables = this.variables;

	if(typeof APP.DATA.redirect !== 'undefined')
		url = APP.DATA.redirect;

	if(typeof APP.DATA.delay !== 'undefined')
	{
		delay = APP.DATA.delay;
		APP.DATA.delay = undefined;
	}

	variables.can_do_redirect = true;
	clearTimeout(variables.redirect_time_out);

	variables.redirect_time_out = setTimeout(() =>
	{
		if(this.variables.can_do_redirect === true)
			this.load_content(url);
	}, delay);
};


Part_Loader.prototype.reload = function()
{
	let delay = 0;

	if(typeof APP.DATA.delay !== 'undefined')
	{
		delay = APP.DATA.delay;
		APP.DATA.delay = undefined;
	}

	setTimeout(() => {
		this.load_content();
	}, delay);
};


Part_Loader.prototype.define = function()
{
	let
		part_name = this.settings.name;

	APP.add_own_event(part_name +'_reload', this.reload);
};