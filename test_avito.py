import os
from playwright.sync_api import sync_playwright

OUTPUT_DIRECTORY = "output"
SELECTORS = {
    "co2": (".desktop-impact-item-eeQO3:has(.desktop-unit-puWVS:has-text('кг CO₂'))", "co2_counter.png"),
    "water": (".desktop-impact-item-eeQO3:has(.desktop-unit-puWVS:has-text('л воды'))", "water_counter.png"),
    "energy": (".desktop-impact-item-eeQO3:has(.desktop-unit-puWVS:has-text('кВт⋅ч энергии'))", "energy_counter.png"),
}

os.makedirs(OUTPUT_DIRECTORY, exist_ok=True)

def test_screenshot():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://www.avito.ru/avito-care/eco-impact")

        for element, (selector, file_name) in SELECTORS.items():
            page.wait_for_selector(selector)
            page.locator(selector).screenshot(path=os.path.join(OUTPUT_DIRECTORY, file_name))

        browser.close()

test_screenshot()
