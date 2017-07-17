/**
 * Created by mrskull on 31.01.17.
 */


export let Event_Button_Models = function(config)
{
	let that = this;

	this.settings = {
		container:          undefined,
		button:             undefined,

		button_name:        undefined,
		button_reload:      undefined,
		button_redirect:    undefined,
		button_event:       undefined,
		button_delay:       undefined,
	};


	(function load_settings()
	{
		if(typeof config !== 'undefined')
		{
			APP.add_if_isset(config, that.settings, 'container');

			APP.add_if_isset(config, that.settings, 'button');

			APP.add_if_isset(config, that.settings, 'button_name');
			APP.add_if_isset(config, that.settings, 'button_reload');
			APP.add_if_isset(config, that.settings, 'button_redirect');
			APP.add_if_isset(config, that.settings, 'button_event');
			APP.add_if_isset(config, that.settings, 'button_delay');
		}
	})();

};