/**
 * Created by mrskull on 31.01.17.
 */


export let Little_Form_Models = function(form_config)
{
  let
    that = this;

  this.settings = {
    container:    undefined,
    this:         undefined,

    action:       undefined,
    origin:       undefined,
    name:         undefined,
    value:        undefined,

    reload:       undefined,
    redirect:     undefined,
    event:        undefined,
  };


  (function load_settings()
  {
    window.APP.add_if_isset(form_config, that.settings, 'container');
    window.APP.add_if_isset(form_config, that.settings, 'this');

    window.APP.add_if_isset(form_config, that.settings, 'action');
    window.APP.add_if_isset(form_config, that.settings, 'origin');
    window.APP.add_if_isset(form_config, that.settings, 'name');
    window.APP.add_if_isset(form_config, that.settings, 'value');

    window.APP.add_if_isset(form_config, that.settings, 'reload');
    window.APP.add_if_isset(form_config, that.settings, 'redirect');
    window.APP.add_if_isset(form_config, that.settings, 'event');
  })();


/////////////////////////

  let state = {
    loading: false,
    error: false,
  };

  this.get_state_loading = function()
  {
    if(state.response)
      return true;
    else
      return false;
  };

  this.set_state_loading = function(setter)
  {
    if(setter)
      state.response = true;
    else
      state.response = false;
  };

  this.get_state_error = function()
  {
    if(state.error)
      return true;
    else
      return false;
  };

  this.set_state_error = function(setter)
  {
    if(setter)
      state.error = true;
    else
      state.error = false;
  };


/////////////////////////

  let prepare_post_data = function(name, value)
  {
    let post_data = {};

    if(that.settings.origin && typeof that.settings.origin === 'string')
      post_data['__'+that.settings.origin +'__'] = name;

    if(value)
      post_data.value = value;
    else
      post_data.value = '';

    return post_data;
  };


  this.is_error = function(JSON_response, status)
  {
    let response = JSON.parse(JSON_response);

    if(status !== 'success')
      return true;

    if(response['__'+ that.settings.origin +'__'] !== 'true')
      return true;

    return false;
  };


  this.send_post = function(callback)
  {
    setTimeout(function()
    {
      let
        name = that.settings.name,
        action = that.settings.action,
        value = that.settings.value,
        post_data = prepare_post_data(name, value);

      window.APP.http_request(action, post_data, callback);
    }, 200);
  };

};