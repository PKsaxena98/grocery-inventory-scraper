import time

def slow_scroll_to_bottom(driver, pause_time=1, scroll_step=250, max_scrolls=80):
    current_scroll = 0
    for _ in range(max_scrolls):
        driver.execute_script(f"window.scrollBy(0, {scroll_step});")
        time.sleep(pause_time)

        new_height = driver.execute_script("return window.scrollY + window.innerHeight")
        total_height = driver.execute_script("return document.body.scrollHeight")
        
        if new_height >= total_height:
            break
