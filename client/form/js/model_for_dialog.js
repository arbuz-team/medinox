/**
 * Created by mrskull on 6.09.17.
 */

import {Form_Models}            from './model'
import {Block_Loader_Dialog_Form}    from 'block/plugin/block_loader/dialog_form'


export function Dialog_Form_Models(config)
{
	Form_Models.call(this, config);

	this._dialog_form_loader = new Block_Loader_Dialog_Form(config);
}

Dialog_Form_Models.prototype = Object.create(Form_Models.prototype);



Dialog_Form_Models.prototype.send = function()
{
	let
		post_url = this.variables.post_url,
		post_data = this.variables.post_data;

	this._prepare_post_data();

	this._dialog_form_loader.load_content(post_url, post_data).then(this._end_loading);
};