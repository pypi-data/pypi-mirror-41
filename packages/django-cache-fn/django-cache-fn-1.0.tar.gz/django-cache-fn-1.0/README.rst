=====
Cache Fn
=====
Use django cache to cache the `function(*arg, **kw)` with timeout.

Quick start
-----------

1. Install::
   
   pip install django-cache-fn

1. Add "cache_fn" to your INSTALLED_APPS setting like this::

   INSTALLED_APPS = [
   ...
   'cache_fn',
   ]

2. Start to use it in code::

   from cache_fn.decorators import cache_fn

   @cache_fn(prefix='myprefix', timeout=3600)
   def foo(k1, k2):
      return "%s %s"%(k1, k2)

Usage
--------
   
   def cache_fn(timeout=1, prefix=None, cache_ttl=MEMCACHE_MAX_EXPIRATION):
       """
       Retrieve data from cache if cacheable and no-stale,
       otherise refresh synchronously and cache it.
       * timeout: The stale timeout which would be handled in the decorator.
       * prefix: The prefix of cache key.
       * cache_ttl: The TTL(time to live) of key in memcache.
       NOTE: For HttpResponse, we just cache the response whose status code is 200.
       """
