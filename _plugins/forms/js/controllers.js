/**
 * Created by mrskull on 24.11.16.
 */

import {Form_Models} from './models'
import * as validator from './validator/controllers'
import * as hide_form from './hide_form/controllers'
import * as auto_form from './auto_form/controllers'
import * as selected_form from './selected_form/controllers'
import * as file_converter from './file_converter/controllers'

export let Form_Controllers = function(content_loader_controllers)
{
  let
    form_models = new Form_Models(content_loader_controllers);


  /**
   *    Defining private functions
   */

  let

    prepare_form_to_send = function(event)
    {
      let
        form_action = $(this).attr('action'),
        protocol;

      if(typeof form_action === 'string')
        protocol = form_action.substring(0, 4);

      if(protocol !== 'http')
      {
        event.preventDefault();

        let
          form_name = $(this).data('name'),
          url = $(this).attr('action'),
          form_object = $(this).serialize_object();

        form_models.send(form_name, url, form_object);
      }
    },


    show_hide_form_address = function(event)
    {
      let $element = $(this).parents('.form_block');
      event.stopPropagation();

      if($element.hasClass('visible'))
        $element.removeClass('visible');
      else
        $element.addClass('visible');
    },


    show_form_address = function(event)
    {
      event.stopPropagation();

      $(this).addClass('visible');
    };


  /**
   *    Defining public functions
   */

  this.define = function()
  {
    let $container = $(content_loader_controllers.container);
    
    $('form', $container).submit(prepare_form_to_send);

    $('.form_block', $container).click(show_form_address);

    $('.form_block .title', $container).click(show_hide_form_address);
    
    validator.define($container);
    hide_form.define($container);
    auto_form.define($container);
    selected_form.define($container);
    file_converter.define($container);
  };

};

