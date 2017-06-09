/**
 * Created by mrskull on 17.01.17.
 */

/**
 *    Defining private functions
 */

let send_prepare_post = function(name, value)
{
  return {
    __edit__ : name,
    value : value,
  };
};


/**
 *    Defining public functions
 */

export let send = function(field, callback)
{
  let $field = $(field),
    field_name = $field.attr('name'),
    field_value = $field.val(),
    post_data = send_prepare_post(field_name, field_value);
  
  window.APP.http_request(undefined, post_data, callback)
};