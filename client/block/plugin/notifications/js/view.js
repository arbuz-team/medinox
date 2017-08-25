/**
 * Created by mrskull on 25.08.17.
 */

import {Notifications_Model} 		from './model'


export function Notifications_View()
{
	let
		model = this.model,

		$list_notifications;


	this.model = new Notifications_Model();


	this.set_list = function(response)
	{
		let html = model.receive_response(response);

		$list_notifications.append(html);
	};


	this.get_list = function(button)
	{
		let
			$button = $(button),
			$container = $button.parents(model.selector.container),
			$list = $container.find(model.selector.list),
			$last_notification = $list.children().last(),

			pk = $last_notification.data('pk');

		$list_notifications = $list;

		return model.get_ten_notifications(pk);
	};
}