# Memory Management

Premiere Pro has a media cache in which it stores imported frames, intermediate frames (intermediate stages of a render), fully rendered frames, and audio.

This is sized based on a specific percentage of physical memory, taking into account if multiple Adobe applications are also running.

Premiere Pro manages this cache itself, so as it adds new items to the cache, it flushes least recently used items.

---

## What Really is a Memory Problem?

Often, users monitoring memory usage are alarmed when they see memory growing to a specific point during a render or playback. When the memory doesn’t drop right back down after a render or playback, they might think they have found a memory leak. However, keeping in mind the function of the Premiere Pro media cache, this behavior is to be expected.

On the other hand, memory contention between plugins and the rest of Premiere Pro can lead to memory problems. If a plugin allocates a significant amount of memory and the Premiere Pro media cache has not accounted for it, this means there is less free memory available after the media cache grows to the predefined size. Even if Premiere Pro does not completely run out of memory, limited memory can cause memory thrashing as memory is moved around to make room for video frames, which in turn can cause poor performance.

---

## Solutions for Memory Contention

The best approach to reduce memory contention is to reduce the memory requirements of each plugin. However, if the memory requirements of a plugin are significant, it should also use the [Memory Manager Suite](sweetpea-suites.md#universals-sweetpea-suites-memory-manager-suite) to report any memory usage that would not already be accounted for.

Frames allocated using the [PPix Creator Suite](sweetpea-suites.md#universals-sweetpea-suites-ppix-creator-suite) are accounted for, but any memory allocated using the old PPix and Memory functions are not automatically accounted for.
