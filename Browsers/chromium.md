# chromium
- For Google Chrome, Microsoft Edge and other Chromium-based browsers, by default, Playwright uses open source Chromium builds.
- these brosers lag behind the open source Chromium builds
- As a result because Playwright uses open source Chromium builds it will automatically also support the next version of thes brosers

## Chromium: headless shell
Playwright ships a regular Chromium build for headed operations and a separate [chromium headless shell](https://developer.chrome.com/blog/chrome-headless-shell) for headless mode.

If you are only running tests in headless shell (i.e. the channel option is not specified), for example on CI, you can avoid downloading the full Chromium browser by passing --only-shell during installation.
```# only running tests headlessly
playwright install --with-deps --only-shell`
```
## Google Chrome & Microsoft Edge

While Playwright can download and use the recent Chromium build, it can operate against the branded Google Chrome and Microsoft Edge browsers available on the machine (note that Playwright doesn't install them by default). In particular, the current Playwright version will support Stable and Beta channels of these browsers.

Available channels are `chrome, msedge, chrome-beta, msedge-beta, chrome-dev, msedge-dev, chrome-canary, msedge-canary`.