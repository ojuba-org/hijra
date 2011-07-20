const Panel = imports.ui.panel;
const StatusIconDispatcher = imports.ui.statusIconDispatcher;

function main() {
    StatusIconDispatcher.STANDARD_TRAY_ICON_IMPLEMENTATIONS['hijriapplet'] = 'hijriapplet';
}
