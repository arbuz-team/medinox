/**
 *    Created by mrskull on 24.11.16.
 */

import {Plugins_Loader_Models} from './models'
import * as img_loader          from './img_loader';


export let Plugins_Loader_Views = function(config)
{
  let
    models = new Plugins_Loader_Models(config),
    external_callback,
    data_controller = models.data_controller;

  this.models = models;


  /**
   *    Defining showing functions
   */

  let

    load_header_page = function(object)
    {
      data_controller.change_much({
        title: object.title,
        description: object.description
      });

      $('title').html(data_controller.get('title'));
      $('meta[ name="description" ]').attr('content', data_controller.get('description'));
    },


    check_for_errors = function(status, code)
    {
      let
        container = models.settings.container,
        error = models.variables.error;

      if(status !== 'success')
        if(error === true)
          $(container)
          .html('An error has occurred while connecting to server. Please, refresh website or check your connect with network.');
        else
        {
          models.variables.error = true;

          models.prepare_post_data({__content__: 'ground'});
          models.download_content('/statement/' + code + '/', show_content);

          return true;
        }
      return false;
    },


    prepare_content_to_show = function(html, status, code)
    {
      let
        container = models.settings.container,
        $container = $(container),
        url = models.variables.url,
        error = models.variables.error;

      $container.scrollTop(0);

      if(check_for_errors(status, code))
        return false;

      if(error !== true || status === 'success')
        $container.html(html).add_data('url', url);

      models.variables.error = false;
      models.variables.url = '';

      models.refresh_events();
      models.refresh_scroll();
      img_loader.define();
    },


    show_content = function(response, status, code)
    {
      prepare_content_to_show(response, status, code);

      let
        container = models.settings.container,
        opacity = models.settings.opacity.show,
        duration = models.settings.duration.show;


      $(container)
        .animate({opacity: opacity}, duration, function()
        {
          if(external_callback)
            external_callback(response, status, code);

          if(models.settings.load_with_page && window.APP.DATA)
            load_header_page(window.APP.DATA);
        });
    };


  /**
   *    Defining hidding functions
   */

  let

    prepare_content_to_hide = function(url, post_data)
    {
      models.variables.can_do_redirect = false;

      models.refresh_data();
      models.prepare_url(url);
      models.prepare_post_data(post_data);
    },


    hide_content = function(url, post_data, callback)
    {
      external_callback = callback;
      prepare_content_to_hide(url, post_data);

      let
        container = models.settings.container,
        opacity = models.settings.opacity.hide,
        duration = models.settings.duration.hide;

      $(container)
        .animate({opacity: opacity}, duration, () =>
        {
          models.download_content(models.variables.url, show_content);
        });
    };


  /**
   *    Defining public functions
   */

  this.change_content = hide_content;
};