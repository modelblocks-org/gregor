import csv
import os
import psutil
import threading
import time


class MemoryLogger:
    def __init__(self, interval_sec=0.5, pid=None):
        """
        interval_sec: numeric
            Sampling interval in seconds
        pid: int or None | None 
            Process ID to monitor; defaults to current process
        """
        self.interval_sec = interval_sec
        self.pid = pid or os.getpid()
        self.mem_log = []  # list of (elapsed_seconds, rss_mib)
        self._thread = None
        self._stop_event = threading.Event()
        self._t0 = None

    def _worker(self):
        proc = psutil.Process(self.pid)
        self._t0 = time.time()
        while not self._stop_event.wait(self.interval_sec):
            try:
                rss = proc.memory_info().rss / 1024**2  # MiB
            except psutil.NoSuchProcess:
                break
            t = time.time() - self._t0
            self.mem_log.append((t, rss))

    def start(self):
        """Start background memory logging."""
        if self._thread is not None and self._thread.is_alive():
            return  # already running
        self._stop_event.clear()
        self._thread = threading.Thread(target=self._worker, daemon=True)
        self._thread.start()

    def stop(self):
        """Stop logging and wait for the thread to finish."""
        if self._thread is None:
            return
        self._stop_event.set()
        self._thread.join()
        self._thread = None

    def save_csv(self, destination):
        """Save memory log to a csv file."""
        with open(destination, "w", newline="") as f:
            w = csv.writer(f)
            w.writerow(["t_sec", "rss_mib"])
            w.writerows(self.mem_log)
