/**
 * Created by mrskull on 18.12.16.
 */

import {Post_Button}     from './model'
export {Post_Button}     from './model'

import {reload_plugins, redirect_ground, launch_event} from 'form/js/utilities'
import {timeout_promise} from 'arbuz/plugin/utilities/standard'


let

	if_not_button_text = function($button)
	{
		return $button.hasClass('is-icon');
	};


Post_Button.prototype._insert_text = function(text)
{
	let $button = $(this._button_data.elem);

	if(if_not_button_text($button))
		return false;

	if($button.hasClass('is-text_icon'))
		$button.find('.button-text').html(text);
	else
		$button.html(text);
};


Post_Button.prototype._set_text_sending = function()
{
	this._insert_text(this._text_data.sending);

	return timeout_promise(this._text_data.delay_after_sending);
};


Post_Button.prototype._set_text_waiting = function()
{
	if(this._is_loading())
		this._insert_text(this._text_data.waiting);
};


Post_Button.prototype._set_text_done = function()
{
	this._insert_text(this._text_data.done);

	return timeout_promise(this._text_data.delay_after_done);
};


Post_Button.prototype._set_text_standard = function()
{
	if(this._is_not_loading())
		this._insert_text(this._text_data.standard);
};


Post_Button.prototype._set_text_error = function()
{
	this._insert_text(this._text_data.error);
};


Post_Button.prototype._run_events = function()
{
	let events = {
		reload:     this._button_data.reload,
		redirect:   this._button_data.redirect,
		events:     this._button_data.event,
		delay:      this._button_data.delay,
	};

	reload_plugins(events);
	redirect_ground(events);
	launch_event(events);
};


Post_Button.prototype._send = function()
{
	this._prepare_post_data();

	return this._send_post();
};
