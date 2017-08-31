/**
 * Created by mrskull on 29.08.17.
 */

import {Request_Manager} from './_controller'


export function Request_Manager_Main()
{
	Request_Manager.call(this);
}

Request_Manager_Main.prototype = Object.create(Request_Manager.prototype);