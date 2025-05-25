from playwright.sync_api import sync_playwright, expect

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(storage_state='browser-state.json')
    page = context.new_page()
    page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/dashboard')
    page_title = page.get_by_test_id('dashboard-toolbar-title-text')
    expect(page_title).to_have_text('Dashboard')
