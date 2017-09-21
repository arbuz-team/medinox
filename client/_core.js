/**
 * Created by mrskull on 24.11.16.
 */

import {Page_Controller} from 'arbuz/js/controllers';


let page_controller = new Page_Controller();

window.APP.add_own_event('load', () => {
	page_controller.start();
});

