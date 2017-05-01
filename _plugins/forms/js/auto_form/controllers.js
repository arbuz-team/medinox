/**
 * Created by mrskull on 17.01.17.
 */

import {Auto_Form_Views} from './views'


let
  add_event_on_fields = function(auto_form_views)
  {
    let
      settings = auto_form_views.models.settings,
      $field;

    settings.fields.each(function()
    {
      $field = $(this);


      if($field.is(':checkbox'))
        $field.change(auto_form_views.send_checkbox);


      else if($field.is(':text'))
      {
        if($field.hasClass('only_enter'))
          $field
            .keydown(auto_form_views.send_on_enter);
        else
        {
          if($field.hasClass('always'))
            $field
              .keyup(auto_form_views.send_if_number_only);

          if($field.hasClass('only_number_3'))
            $field
              .keydown(auto_form_views.try_press_number_max_3);

          $field
            .change(auto_form_views.send_default)
            .keydown(auto_form_views.send_on_enter);
        }
      }

      else
        $field.change(auto_form_views.send_default);
    });
  },


  do_nothing = function(event)
  {
    event.preventDefault();
    return false;
  };


export let define = function($container)
{
  let
    $forms = $('form.auto_form, .auto_form form', $container);

  $forms.each(function()
  {
    let
      $form = $(this),
      config = {
        form:     $form,
        fields:   $('.auto_field', $form),
      },
      auto_form_views = new Auto_Form_Views(config);

    $form.submit(do_nothing);
    add_event_on_fields(auto_form_views);
  });
};