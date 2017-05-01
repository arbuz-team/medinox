/**
 * Created by mrskull on 17.12.16.
 */

import {Little_Form_Views} from './views'


export let Little_Form_Controllers = function(form_config)
{
  if(typeof form_config === 'undefined' && typeof form_config.container === 'undefined')
  {
    console.error('Exeption error: invalid container.');
    return {};
  }


  let
    little_form_views = {},


    manage_form = function(event)
    {
      event.preventDefault();
      event.stopPropagation();

      let
        form_name = $(this).parent().find('input').data('name'),
        value = $(this).parent().find('input').val();

      if(little_form_views[form_name])
        little_form_views[form_name].start(value);
      else
        console.error('Form "'+ form_name +'" doesn\'t exsist');
    },


    create_form_views = function()
    {
      form_config.this = this;

      form_config.action = $(this).data('action');
      form_config.origin = $(this).data('origin');
      form_config.name = $(this).find('input').data('name');
      form_config.value = $(this).find('input').val();

      form_config.reload = $(this).data('reload');
      form_config.redirect = $(this).data('redirect');
      form_config.event = $(this).data('event');

      little_form_views[form_config.name] = new Little_Form_Views(form_config);
    };


  this.define = function()
  {
    let $form = $('.little_form', form_config.container);

    $form
      .each(create_form_views);

    $form.find('button')
      .click(manage_form);
  };
};