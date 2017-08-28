/**
 * Created by mrskull on 17.07.17.
 */

import {Request_Manager_Block} 	from 'arbuz/plugin/request_manager/block'
import {Block_Loader_Part} 		from './block'


export function Block_Loader_Form(config)
{
	Block_Loader_Part.call(this, config);
}

Block_Loader_Form.prototype = Object.create(Block_Loader_Part.prototype);





// ------------------------------------------


Block_Loader_Form.prototype._prepare_post_data = function(post_data)
{
	if(!post_data)
		post_data = {};

	post_data[this._settings.post_name] = 'form';

	this._variables.post_data = post_data;
};


Block_Loader_Form.prototype._send_request = function()
{
	let
		post_url = this._variables.post_url,
		post_data = this._variables.post_data,
		post_name = this._settings.post_name,
		request_manager = new Request_Manager_Block();

	this._response = request_manager.next(post_url, post_data, post_name);
};


Block_Loader_Form.prototype.load_simple_content = function(post_url, post_data)
{
	let
		request_manager,
		loading;

	request_manager = new Request_Manager_Block();

	loading = this.load_content(post_url, post_data);
	request_manager.send_list();

	return loading;
};