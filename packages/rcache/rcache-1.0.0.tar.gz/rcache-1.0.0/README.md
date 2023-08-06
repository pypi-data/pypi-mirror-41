# rcache.py

[![pipeline status](https://gitlab.com/the_speedball/redis.cache.py/badges/master/pipeline.svg)](https://gitlab.com/the_speedball/redis.cache.py/commits/master)

# What is it

rcache.py is a cache and works on redis so it is suitable for multi threaded and multi process applications.
It has been inspired and based on `cache.py` library https://github.com/bwasti/cache.py

# Usage

To use the file, `import rcache` and annotate functions with `@rcache.rcache()`.

```python
import rcache

@rcache.rcache()
def expensive_func(arg, kwarg=None):
  # Expensive stuff here
  return arg

```

The `@rcache.rcache()` function can take multiple arguments.

- `@rcache.rcache(timeout=20)` - Only caches the function for 20 seconds.
- `@rcache.rcache(url="http://other_redis:6379")` - Saves cache to specified Redis url (defaults to `http://localhost:6379`)
- `@rcache.rcache(key=rcache.ARGS[KWARGS,NONE])` - Check against args, kwargs or neither of them when doing a cache lookup.

# How it works

`rcache.py` queries `redis` and checks against the name, arguments and hash of a function's source
to decide if the function has been run before.  If it has it returns the cached result immediately.

