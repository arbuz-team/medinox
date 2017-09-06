/**
 * Created by mrskull on 17.07.17.
 */

import {Block_Loader_Dialog} 	from 'block/plugin/block_loader/dialog'



export function Block_Loader_Dialog_Form(config)
{
	Block_Loader_Dialog.call(this, config);
}

Block_Loader_Dialog_Form.prototype = Object.create(Block_Loader_Dialog.prototype);



Block_Loader_Dialog_Form.prototype._prepare_post_data = function(post_data)
{
	if(!post_data)
		post_data = {};

	post_data[this._settings.post_name] = 'form';

	this._variables.post_data = post_data;
};