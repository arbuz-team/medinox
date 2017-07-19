/**
 * Created by mrskull on 17.07.17.
 */

import {data_controller} 			from 'arbuz/js/structure'
import {Request_Manager_Block} 		from 'arbuz/plugin/request_manager/block'
import {Part_Loader} 				from './_init'



// --------------------------    REQUEST    --------------------------


Part_Loader.prototype._if_reload = function(url)
{
	let
		old_url = data_controller.get('path'),
		new_url = url;

	return old_url === new_url || !new_url;
};


Part_Loader.prototype._refresh_events = function()
{
	APP.throw_event( EVENTS.define );
};


Part_Loader.prototype._prepare_to_change_content = function(post_url)
{
	this._variables.post_url = post_url;
	this._variables.can_do_redirect = false;
	this._state.reload = this._if_reload(post_url);

	data_controller.reset();
};


Part_Loader.prototype._prepare_post_data = function(post_data)
{
	if(!post_data)
		post_data = {};

	post_data[this._settings.post_name] = 'content';

	this._variables.post_data = post_data;
};


Part_Loader.prototype._send_request = function()
{
	let
		url = this._variables.post_url,
		data = this._variables.post_data,
		post_name = this._settings.post_name,
		request_manager = new Request_Manager_Block();

	this.response = request_manager.send(url, data, post_name);
};



// --------------------------    RESPONSE    --------------------------


Part_Loader.prototype._check_for_errors = function(response)
{
	if(typeof response.html === 'undefined' || typeof response.code === 'undefined')
		return true;

	return false;
};


Part_Loader.prototype._preprocess_response = function(response)
{
	return {
		html: response.html,
		code: response.code,
	};
};