/**
 * Created by mrskull on 17.12.16.
 */


  let

    change_fields = function(select_choice)
    {
      let
        important_fields = $(select_choice).data('important_fields'),
        fields_to_hide = $(select_choice).val();


      let hidden_fields = function(list, type)
      {
        let array, array_length;

        if(!list || typeof list !== 'string')
          return false;

        array = list.split(' ');
        array_length = array.length;

        for(let i = 0; i < array_length; ++i)
          if(array[i])
            if($('#id_'+ array[i]).length)
              $('#id_'+ array[i]).attr('hidden', type)
      };

      hidden_fields(important_fields, false);
      hidden_fields(fields_to_hide, true);
    },


    change_form = function(event)
    {
      event.preventDefault();
      event.stopPropagation();

      let
        $select_choice = $(this),
        $title_field = $('#id_title'),
        $options = $select_choice.children('option'),
        form_title = $title_field.val();

      $options.each(function(){
        if($(this).is(':selected'))
          form_title = $(this).text();
      });

      $title_field.attr('value', form_title);

      change_fields($select_choice);
    };


  export let

    define = function($container)
    {
      $('.selected_form-choice', $container).change(change_form);
    };