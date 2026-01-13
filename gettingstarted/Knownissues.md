# Known issues

## time.sleep() leads to outdated state
we actually dont need to wait manually because playwright has `auto-waiting` which makes sure that befor taking an action everithing requred is already performed.

### Auto-waiting
Playwright performs a range of actionability checks on the elements before making actions to ensure these actions behave as expected. It auto-waits for all the relevant checks to pass and only then performs the requested action. If the required checks do not pass within the given timeout, action fails with the TimeoutError.

For example, for locator.click(), Playwright will ensure that:

    locator resolves to exactly one element
    element is Visible
    element is Stable, as in not animating or completed animation
    element Receives Events, as in not obscured by other elements
    element is Enabled

## Threading
Playwright's API is not thread-safe. If you are using Playwright in a multi-threaded environment, you should create a playwright instance per thread. See threading issue for more details.