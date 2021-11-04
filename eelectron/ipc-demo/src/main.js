const electron = require('electron')

const  countdown = require('./countdown')

const app = electron.app
const BrowserWindow = electron.BrowserWindow
const ipc = electron.ipcMain

let mainWindow

app.on('ready', _ => {
    console.log('ready!')
    mainWindow = new BrowserWindow({
        height: 400,
        width: 400,
        webPreferences: {
            nodeIntegration: true,
            contextIsolation: false
        }
    })

    mainWindow.loadURL(`file://${__dirname}/countdown.html`)

    mainWindow.on('closed', _ => {
        console.log('closed')
        mainWindow = null
    })
})

ipc.on('countdown-start', _ => {
    console.log('caught it!')
    countdown(count => {
        mainWindow.webContents.send('countdown', count)
    })
})
