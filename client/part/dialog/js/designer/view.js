/**
 * Created by mrskull on 18.07.17.
 */


export function Dialog_Designer_View(config)
{
	this.selector = {
		html_id: 	config.html_id,
		window: 	config.container,
		header: 	config.container +'-header',
		content: 	config.container +'-content',
	};


	this.show = function()
	{
		return new Promise((resolve) =>
		{
			$(this.selector.html_id)
				.css('opacity', '')
				.fadeIn(200, resolve);
		});
	};


	this.hide = function()
	{
		return new Promise((resolve) =>
		{
			$(this.selector.html_id).animate({opacity: 0}, 200, () =>
			{
				$(this.selector.html_id).hide();
				resolve();
			});
		});
	};


	this.dim = function()
	{
		return new Promise((resolve) =>
		{
			$(this.selector.html_id).animate({ opacity: .8 }, 200, resolve);
		});
	};


	this.lighten = function()
	{
		return new Promise((resolve) =>
		{
			$(this.selector.html_id).animate({ opacity: 1 }, 300, resolve);
		});
	};
}