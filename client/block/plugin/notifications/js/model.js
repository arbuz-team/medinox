/**
 * Created by mrskull on 25.08.17.
 */

import {Request_Manager} from 'arbuz/plugin/request_manager/_controller'


export function Notifications_Model()
{
	let
		request_manager = new Request_Manager(),

		variable = {
			post_url:   '/notification/',
			post_data:  undefined,
			post_name:  '__ground__',
		};


	this.selector = {
		container:          '.notifications',
		list:               '.notifications-list',
		show_more_button:   '.notifications-show_more-button',
	};





	this.prepare_post_data = function(pk)
	{
		if(!pk)
			pk = '';

		variable.post_data = {
			_name_:                'ten_notifications',
			last_notification_pk:   pk,
		};

		variable.post_data[variable.post_name] = 'get';
	};


	this.receive_response = function(response)
	{
		if(response && response.html)
			return response.html;
	};


	this.get_ten_notifications = function()
	{
		return request_manager.send(variable.post_url, variable.post_data, variable.post_name);
	};
}