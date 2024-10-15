from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()

    # Define the bounding box coordinates (top-left and bottom-right pixels)
    top_left_x, top_left_y = 100, 200
    bottom_right_x, bottom_right_y = 300, 400

    for x in range(top_left_x, bottom_right_x + 1):
        for y in range(top_left_y, bottom_right_y + 1):
            page.mouse.move(x, y)
            page.mouse.down()
            page.mouse.up()

            context = browser.
            element = context.evaluate("args => args.execute Inspector.get_selected_element()", {})
            html = context.evaluate("args => args.execute('JSON.stringify(Inspector.elementStringify(arguments[0]))', {runScripts: false})", 
element['value'])
            print(f"HTML for pixel ({x}, {y}): {html}")

    browser.close()

