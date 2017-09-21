/**
 * Created by mrskull on 31.01.17.
 */

import {Event_Button} from './_init'
export {Event_Button} from './_init'


Event_Button.prototype._is_not_loading = function()
{
	return this._variables.is_loading === false;
};


Event_Button.prototype._set_loading = function()
{
	this._variables.is_loading = true;
};


Event_Button.prototype._set_end_loading = function()
{
	this._variables.is_loading = false;
};