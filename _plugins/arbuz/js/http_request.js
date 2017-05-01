/**
 * Created by mrskull on 20.12.16.
 */

import {data_controller} from './structure'


/**
 *    Defining private functions
 */

let

  send_post_preprocess_url = function( response_url )
  {
    if( response_url )
      return response_url;
    else
      return data_controller.get( 'path' );
  },


  send_post_prepare = function(post_data)
  {
    if(!post_data)
      post_data = {};

    post_data[data_controller.get_crsf('name')] = data_controller.get_crsf('value');

    return post_data;
  },


  create_callback = function(callback)
  {
    return function(response, status)
    {
      let
        html = response.responseText,
        code = response.status;
      
      callback(html, status, code);
    };
  };


/**
 *    Defining global functions
 */

  window.APP.http_request = function(url, post_data, callback)
  {
    url = send_post_preprocess_url(url);
    post_data = send_post_prepare(post_data);

    $.ajax({
      type: 'POST',
      url: url,
      data: post_data,
      complete: create_callback(callback),
    });
  };