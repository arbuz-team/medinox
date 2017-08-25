/**
 * Created by mrskull on 25.08.17.
 */

import {Request_Manager} from 'arbuz/plugin/request_manager/_controller'


export function Notifications_Model()
{
	let
		request_manager = new Request_Manager(),

		variable = {
			post_data:  undefined,
			post_name:  '__get__',
		};


	this.selector = {
		container:          '.notifications',
		list:               '.notifications-list',
		show_more_button:   '.notifications-show_more-button',
	};





	this.prepare_post_data = function(pk)
	{
		variable.post_data = {
			__get__:                'ten_notifications',
			last_notification_id:   pk,
		};
	};


	this.receive_response = function(response)
	{
		if(response && response.html)
			return response.html;
	};


	this.get_ten_notifications = function()
	{
		return request_manager.send(undefined, variable.post_data, variable.post_name);
	};
}