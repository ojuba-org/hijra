
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

