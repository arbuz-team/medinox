/**
 * Created by mrskull on 22.08.17.
 */

import {Block_Loader_Part}     			from 'block/plugin/block_loader/block'
import {Page_Controller}                from 'arbuz/js/controllers';
import {Menu_Controller}     			from 'block/menu/js/controller'

import {Form_Controllers}               from 'form/js/controller'
import {Post_Button_Controllers}        from 'form/plugin/post_button/controllers'
import {Event_Button_Controllers}       from 'form/plugin/event_button/controllers'

import {timeout_promise}       from 'arbuz/plugin/utilities/standard'


export function Ground_Model()
{
	this.container = '.ground';

	this.config_loader = {
		part_name: 'ground',
		container: this.container,
		load_meta_tags: true,
	};
	this.config_form = {
		part_name: 'ground',
		container: this.container,
	};


	this.ground_loader =            new Block_Loader_Part(this.config_loader);

	this.post_button_controller =   new Post_Button_Controllers(this.config_form);
	this.event_button_controller =  new Event_Button_Controllers(this.config_form);
	this.ground_form_controller =   new Form_Controllers(this.config_loader);

	this.page_controller =          new Page_Controller();
	this.menu_controller =          new Menu_Controller();



	this.change_url = function(url)
	{
		history.pushState('', url, url);
	};


	this.is_redirect = function(response)
	{
		return response && response.code === 302;
	};


	this.check_redirect = function(response)
	{
		if(this.is_redirect(response))
		{
			this.change_url(response.url);
			this.load_single_ground_content();
		}
	};


	this.load_ground_content = function(url, data)
	{
		let result = this.ground_loader.load_content(url, data);

		result.then(response => this.check_redirect(response));
	};


	this.load_single_ground_content = function(url, data)
	{
		let result = this.ground_loader.load_simple_content(url, data);

		result.then(response => this.check_redirect(response));
	};


	this.redirect_ground = function()
	{
		let result = this.ground_loader.redirect(this.change_url);

		result.then(response => this.check_redirect(response));
	};


	this.back_url = function()
	{
		event.preventDefault();
		this.load_single_ground_content();
	};
}