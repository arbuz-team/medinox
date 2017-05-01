/**
 * Created by mrskull on 21.01.17.
 */


export let Form_Models = function(content_loader_controllers)
{

  /**
   *    Defining settings
   */

  this.loader_controllers = content_loader_controllers;

  this.variables = {
    name: undefined,
  };


  /**
   *    Defining private functions
   */

  let prepare_post_data = function(form_name, post_data)
  {
    if(!post_data)
      post_data = {};

    post_data.__form__ = form_name;

    return post_data;
  };


  /**
   *    Defining public functions
   */

  this.send = function(form_name, url, post_data)
  {
    post_data = prepare_post_data(form_name, post_data);

    if(typeof this.loader_controllers !== 'undefined')
      this.loader_controllers.load(url, post_data);
    else
      console.error('Valid config object.');
  };

};