
from pathlib import Path
import multiprocessing as mp
import shutil
import subprocess
import sys
import platform

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService

CACHE_DIR = Path.home() / ".cache" / "selenium"
START_TIMEOUT = 10


def normalize_version(full_version: str) -> str:
    return (full_version or "").split(" ")[0].strip()


def detect_platform() -> str:
    machine = platform.machine().lower()
    platform_map = {
        ("darwin", "arm64"): "mac-arm64",
        ("darwin", "x86_64"): "mac-x64",
        ("linux", "x86_64"): "linux64",
        ("linux", "aarch64"): "linux-aarch64",
        ("win32", "amd64"): "win64",
        ("cygwin", "amd64"): "win64",
    }
    return platform_map.get((sys.platform, machine), f"{sys.platform}-{machine}")


PLATFORM = detect_platform()


def remove_old_versions(base_dir: Path, keep_version: str, label: str) -> list[str]:
    removed = []

    if not base_dir.exists():
        print(f"[INFO] {label}: cache directory not found ({base_dir}), skipping")
        return removed

    for path in sorted(base_dir.iterdir()):
        if not path.is_dir():
            continue

        if path.name == keep_version:
            print(f"[KEEP]   {label} {path.name}")
        else:
            print(f"[DELETE] {label} {path.name}")
            shutil.rmtree(path, ignore_errors=True)
            removed.append(path.name)

    return removed


# ---------- Workers: only to read versions via Selenium ----------

def chrome_worker(queue: mp.Queue):
    try:
        # Let Selenium Manager resolve Chrome + chromedriver.
        service = ChromeService()
        options = webdriver.ChromeOptions()
        options.add_experimental_option("excludeSwitches", ["enable-logging"])

        driver = webdriver.Chrome(service=service, options=options)
        try:
            caps = driver.capabilities or {}
            browser_ver = caps.get("browserVersion", "").strip()
            driver_ver = normalize_version(
                (caps.get("chrome") or {}).get("chromedriverVersion", "")
            )
            queue.put(("ok", browser_ver, driver_ver))
        finally:
            driver.quit()
    except Exception as e:
        queue.put(("skip", str(e)))


def firefox_worker(queue: mp.Queue):
    try:
        service = FirefoxService(log_output=subprocess.DEVNULL)
        options = webdriver.FirefoxOptions()

        driver = webdriver.Firefox(service=service, options=options)
        try:
            caps = driver.capabilities or {}
            browser_ver = caps.get("browserVersion", "").strip()
            driver_ver = normalize_version(
                caps.get("moz:geckodriverVersion", "")
            )
            queue.put(("ok", browser_ver, driver_ver))
        finally:
            driver.quit()
    except Exception as e:
        queue.put(("skip", str(e)))


def edge_worker(queue: mp.Queue):
    try:
        service = EdgeService()
        options = webdriver.EdgeOptions()

        driver = webdriver.Edge(service=service, options=options)
        try:
            caps = driver.capabilities or {}
            browser_ver = caps.get("browserVersion", "").strip()
            driver_ver = normalize_version(
                (caps.get("msedge") or {}).get("msedgedriverVersion", "")
            )
            queue.put(("ok", browser_ver, driver_ver))
        finally:
            driver.quit()
    except Exception as e:
        queue.put(("skip", str(e)))


def run_with_timeout(worker, label: str, timeout: int = START_TIMEOUT):
    queue = mp.Queue()
    process = mp.Process(target=worker, args=(queue,))
    process.start()
    process.join(timeout)

    if process.is_alive():
        process.terminate()
        process.join()
        print(f"[SKIP] {label}: startup timed out after {timeout} seconds")
        return None

    if queue.empty():
        print(f"[SKIP] {label}: no result returned from worker")
        return None

    result = queue.get()
    if result[0] == "ok":
        return result[1], result[2]

    print(f"[SKIP] {label}: failed to start: {result[1]}")
    return None


# ---------- Cleanup per browser: ONLY cache folders ----------

def cleanup_chrome():
    print("\n--- Chrome ---")
    result = run_with_timeout(chrome_worker, "Chrome")
    if not result:
        return

    browser_ver, driver_ver = result
    print(f"[INFO] Chrome: browser={browser_ver}, driver={driver_ver}")

    remove_old_versions(CACHE_DIR / "chrome" / PLATFORM, browser_ver, "Chrome")
    remove_old_versions(CACHE_DIR / "chromedriver" / PLATFORM, driver_ver, "ChromeDriver")


def cleanup_firefox():
    print("\n--- Firefox ---")
    result = run_with_timeout(firefox_worker, "Firefox")
    if not result:
        return

    browser_ver, driver_ver = result
    print(f"[INFO] Firefox: browser={browser_ver}, driver={driver_ver}")

    remove_old_versions(CACHE_DIR / "firefox" / PLATFORM, browser_ver, "Firefox")
    remove_old_versions(CACHE_DIR / "geckodriver" / PLATFORM, driver_ver, "GeckoDriver")


def cleanup_edge():
    print("\n--- Edge ---")
    result = run_with_timeout(edge_worker, "Edge")
    if not result:
        return

    browser_ver, driver_ver = result
    print(f"[INFO] Edge: browser={browser_ver}, driver={driver_ver}")

    remove_old_versions(CACHE_DIR / "msedge" / PLATFORM, browser_ver, "Edge")
    remove_old_versions(CACHE_DIR / "msedgedriver" / PLATFORM, driver_ver, "MSEdgeDriver")


# ---------- Main ----------

def main() -> int:
    print(f"[INFO] Selenium cache directory: {CACHE_DIR}")
    print(f"[INFO] Platform key: {PLATFORM}")
    print(f"[INFO] Startup timeout: {START_TIMEOUT} seconds")

    cleanup_chrome()
    cleanup_firefox()
    cleanup_edge()

    print("\n[DONE] Cleanup finished.")
    return 0


if __name__ == "__main__":
    mp.set_start_method("spawn", force=True)
    sys.exit(main())