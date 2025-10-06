const { app, BrowserWindow } = require('electron')

function createWindow() {
  const mainWindow = new BrowserWindow({
    width: 1920,
    height: 1080,
    autoHideMenuBar: true,
    useContentSize: true,
    transparent: false,
    frame: true,
    resizable: true,
    webPreferences: {
        nodeIntegration: true
    }
})
  mainWindow.loadFile('resources/html/home.html')
}
app.whenReady().then(() => {
  createWindow()
  app.on('activate', function () {
    if (BrowserWindow.getAllWindows().length === 0) createWindow()
  })
})
app.on('window-all-closed', function () {
  if (process.platform !== 'darwin') app.quit()
})