// FIXME: Toggle comment lines (3-$), To add enable and disable functions 
// ^^ But we must enable HijtaApplet extension after install it.
/*
//const Panel = imports.ui.panel;
const StatusIconDispatcher = imports.ui.statusIconDispatcher;

function init(){
}

function enable() {
  StatusIconDispatcher.STANDARD_TRAY_ICON_IMPLEMENTATIONS['hijriapplet'] = 'hijriapplet';
}

function disable() {
    StatusIconDispatcher.STANDARD_TRAY_ICON_IMPLEMENTATIONS['hijriapplet'] = '';
}
*/

const Panel = imports.ui.panel;
const StatusIconDispatcher = imports.ui.statusIconDispatcher;

function init() {
    StatusIconDispatcher.STANDARD_TRAY_ICON_IMPLEMENTATIONS['hijriapplet'] = 'hijriapplet';
}


