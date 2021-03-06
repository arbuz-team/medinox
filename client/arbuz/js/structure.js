/**
 * Created by mrskull on 24.11.16.
 */


/*---------------- Page structure ----------------*/

export let data_controller = new function Data_Controller()
{
	let private_data,
		public_data;

	this.reset = function()
	{
		private_data = {
			path :                location.pathname,
			all_url :             location.href,
			history :             [],
			csrf_token :          $( 'input[ name=csrfmiddlewaretoken ]').val() || '',
		};

		public_data = {
			can_do_redirect :     false,
			can_do_open_plugin :  true,
			page_name :           'Medinox',
			title :               'Loading - Medinox',
			description :         'This page is shop, which is ownership Medinox.',
			statement_content :   'Empty statement.',
		};
	};

	this.reset();


	this.get = function(name)
	{
		if( typeof  private_data[name] !== 'undefined' )
			return private_data[name];

		else if( typeof public_data[name] !== 'undefined' )
			return public_data[name];
		else
		{
			console.warn('Data structure error: Wrong call! Veriable with this name doesn\'t exist: "'+ name +'".');
		}
	};


	this.get_crsf = function(what)
	{
		if(what === 'name')
			return 'csrfmiddlewaretoken';
		else if(what === 'value')
			return private_data.csrf_token;
		else
			console.warn('Data structure error: Wrong call! Veriable with this name doesn\'t exist (crsf).');
	};


	this.change = function( name, value )
	{
		if(typeof public_data[name] !== 'undefined' && typeof value !== 'undefined')
			public_data[name] = value;
		else
			console.warn('Data structure error: Wrong call! Veriable with this name doesn\'t exist: "'+ name +'".');
	};


	this.change_much = function( object )
	{
		for( let name in object )
			if( object.hasOwnProperty( name ) )
			{
				if( name === 'title' )
				{
					if( object[name] !== '' )
						this.change( name, object[name] +' - '+ public_data.page_name );
					else
						this.change( name, public_data.page_name );
				}
				else
					this.change( name, object[name] );
			}
	};

};
