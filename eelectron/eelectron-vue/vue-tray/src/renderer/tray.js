import bus from './bus'
import { remote } from 'electron'

/**
 * I copied a font-awesome png to my clipboard for this example
 * https://raw.githubusercontent.com/encharm/Font-Awesome-SVG-PNG/master/black/png/16/gear.png
 *
 * You would probably want to use custom icons and place them in `static/`
 * and then use `__static` to get a path to them.
 * https://simulatedgreg.gitbooks.io/electron-vue/content/en/using-static-assets.html#use-case-within-js-with-fspath-and-static
 */
const tray = new remote.Tray(remote.clipboard.readImage())
const menu = remote.Menu.buildFromTemplate([
    {
        label: 'ping',
        click () {
            // Send event to Vue
            bus.$emit('ping')
        }
    }
])

tray.setToolTip('hello world')
tray.setContextMenu(menu)
