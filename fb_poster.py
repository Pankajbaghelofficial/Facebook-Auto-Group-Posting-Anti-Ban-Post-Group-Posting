import time
import random
import os
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException

GROUPS_FILE = "groups.json"

def log(message):
    timestamp = time.strftime("[%H:%M:%S] ")
    print(f"{timestamp} {message}")

def safe_delay(min_sec, max_sec):
    delay = random.uniform(min_sec, max_sec)
    log(f"Waiting for {delay:.1f} seconds to mimic human behavior...")
    time.sleep(delay)

def load_groups():
    if os.path.exists(GROUPS_FILE):
        try:
            with open(GROUPS_FILE, "r") as f:
                return json.load(f)
        except Exception:
            return []
    return []

def save_groups(groups):
    try:
        with open(GROUPS_FILE, "w") as f:
            json.dump(groups, f)
    except Exception as e:
        log(f"Failed to save groups locally: {e}")

def main():
    print("="*50)
    print("   Facebook Poster Assistant (CLI Version)")
    print("="*50)

    # 1. Setup Groups
    saved_groups = load_groups()
    groups = []
    
    if saved_groups:
        print(f"\nFound {len(saved_groups)} saved groups.")
        use_saved = input("Do you want to use the saved groups? (y/n): ").strip().lower()
        if use_saved == 'y':
            groups = saved_groups
    
    if not groups:
        print("\nEnter group URLs one by one. Press ENTER on an empty line to finish.")
        while True:
            url = input("Group URL: ").strip()
            if not url:
                break
            groups.append(url)
        if groups:
            save_prompt = input("Save these groups for next time? (y/n): ").strip().lower()
            if save_prompt == 'y':
                save_groups(groups)

    if not groups:
        print("No groups specified. Exiting.")
        return

    # 2. Setup Post Content
    print("\nEnter post text content. Type 'END' on a new blank line to finish text:")
    content_lines = []
    while True:
        line = input()
        if line == "END":
            break
        content_lines.append(line)
    content = "\n".join(content_lines)

    img_path = input("\nEnter Image path (optional, press ENTER to skip): ").strip()

    # 3. Selenium Login
    print("\n--- Starting Browser ---")
    log("Opening Chrome...")
    try:
        driver = webdriver.Chrome()
    except Exception as e:
        print(f"Failed to start Chrome: {e}\nMake sure ChromeDriver is up to date.")
        return

    try:
        driver.get("https://www.facebook.com/")
        print(">> Action Required: Please log in to Facebook manually in the opened browser window.")
        input(">> Press ENTER in this console *ONLY AFTER* you have fully logged in... ")
        log("Proceeding with post sequences.")

        # 4. Processing Queue
        for idx, url in enumerate(groups):
            print("\n-------------------------------------------")
            log(f"[{idx+1}/{len(groups)}] Navigating to group: {url}")
            try:
                driver.get(url)
            except Exception as e:
                log(f"Failed to navigate: {e}")
                continue
            
            safe_delay(5, 10)

            # Try to click create post
            try:
                log("Finding post composer area...")
                try:
                    compose_trigger = WebDriverWait(driver, 10).until(
                        EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Write something...')]"))
                    )
                    compose_trigger.click()
                except TimeoutException:
                    compose_trigger = driver.find_element(By.XPATH, "//div[contains(@aria-label, 'Create a public post')]")
                    compose_trigger.click()
            except Exception:
                log("Could not find the 'Write something...' button. Skipped.")
                continue

            safe_delay(2, 4)

            # Fill Text
            if content:
                log("Filling text content...")
                try:
                    text_area = WebDriverWait(driver, 10).until(
                        EC.presence_of_element_located((By.XPATH, "//div[@role='textbox']"))
                    )
                    text_area.click()
                    time.sleep(1)
                    text_area.send_keys(content)
                except Exception as e:
                    log(f"Failed to fill text: {e}")

            # Image
            if img_path and os.path.exists(img_path):
                log(f"Attaching image from {img_path}...")
                try:
                    file_inputs = driver.find_elements(By.XPATH, "//input[@type='file']")
                    if file_inputs:
                        for file_input in file_inputs:
                            try:
                                file_input.send_keys(os.path.abspath(img_path))
                                break
                            except Exception:
                                pass
                    else:
                        log("Could not find image upload input in the DOM.")
                except Exception as e:
                    log(f"Failed to attach image: {e}")

            safe_delay(2, 4)

            # Human Confirmation
            print("\n✨ READY TO POST ✨")
            print("The content has been prefilled in the browser.")
            choice = input(f">> Press ENTER to POST, or type 's' to SKIP this group: ").strip().lower()
            
            if choice == 's':
                log("User skipped this group.")
                continue
            
            # Post
            log("Attempting to click the Post button on Facebook...")
            try:
                post_btn = driver.find_element(By.XPATH, "//div[@aria-label='Post' and @role='button']")
                post_btn.click()
                log("Post clicked!")
            except NoSuchElementException:
                log("Could not find the 'Post' button automatically. Please click it manually in the browser.")
                input("Press ENTER after you clicked Post manually... ")

            safe_delay(4, 6)

            if idx < len(groups) - 1:
                log("Group completed. Delaying before next group to respect rate limits.")
                safe_delay(10, 15)

    except KeyboardInterrupt:
        log("Process interrupted by user (Ctrl+C).")
    except Exception as e:
        log(f"Unexpected error: {e}")
    finally:
        print("Finished processing. Quitting browser in 5 seconds...")
        time.sleep(5)
        try:
            driver.quit()
        except:
            pass

if __name__ == "__main__":
    main()
