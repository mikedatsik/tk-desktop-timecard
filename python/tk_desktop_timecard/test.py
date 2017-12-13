import os
import sys
from pprint import pprint

sys.path.append(os.path.join(os.path.dirname(__file__), "lib"))
# sgtk.util.append_path_to_env_var("PYTHONPATH", startup_path)

from datetime import datetime, timedelta

# from aw_core.transforms import filter_period_intersect, filter_keyvals
# import aw_client

# client = aw_client.ActivityWatchClient()
# starttime = datetime.now().replace(hour=0, minute=0)

# windowevents = client.get_events("aw-watcher-window_OFG-TESTBENCH", start=starttime)
# chrome_events = filter_keyvals(windowevents, "app", ["sublime_text.exe"])

# afkevents = client.get_events("aw-watcher-afk_OFG-TESTBENCH", start=starttime)
# afkevents_filtered = filter_keyvals(afkevents, "status", ["not-afk"])

# chrome_events_filtered = filter_period_intersect(windowevents, afkevents_filtered)

# print chrome_events_filtered

from aw_core.transforms import full_chunk, filter_keyvals
import aw_client

client = aw_client.ActivityWatchClient()
# starttime = datetime.now().replace(hour=0, minute=0)
testdatatime = datetime.strptime("2017-12-06T00:00:00.134880", "%Y-%m-%dT%H:%M:%S.%f")
starttime = testdatatime.replace(hour=0, minute=0)
endtime = testdatatime.replace(hour=23, minute=59)

windowevents = client.get_events("aw-watcher-window_OFG-TESTBENCH",
                                 start=starttime,
                                 end=endtime,
                                 limit=-1)
# nuke_events = filter_keyvals(windowevents, "app", ["Nuke10.5.exe"])
chunk_result = full_chunk(windowevents, "app", False)
chunks = chunk_result.chunks
def chunkDuration(chunk):
    return chunks[chunk]['duration']

# pprint(sorted(chunks, key=chunkDuration, reverse=True))
pprint(chunk_result)
# pprint(chunk_result.duration)
# pprint(nuke_events)

# for chunk in chunks:
#     if chunks[chunk]['duration'] > timedelta(0, 60):
#         print("App: {}, Duration: {}".format(chunk, chunks[chunk]['duration']))