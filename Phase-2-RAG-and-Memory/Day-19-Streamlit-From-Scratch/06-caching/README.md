# 06 — Caching (don't repeat slow work every rerun)

Module 05 taught you that the **whole script reruns on every interaction.** That raises an obvious,
scary question:

> If the entire file runs again on every click, does my slow work run again too? Loading a 90 MB
> embedding model? Reading a big CSV? Calling an API?

By default, **yes** — and that would make apps painfully slow. Caching is the fix.

## What caching does
You put a decorator on a function. The **first** time it's called with given arguments, Streamlit
runs it and **stores the result**. Every later call with the same arguments returns the stored
result instantly, skipping the work — even across reruns and across users.

## Two caches — pick by what the function returns
| Decorator | Use for | Examples |
|-----------|---------|----------|
| `@st.cache_data` | **data**: things that can be copied/serialized | DataFrames, API JSON, computed numbers, lists |
| `@st.cache_resource` | **resources**: one shared live object, not copied | a loaded ML model, a DB connection, an API client |

Rule of thumb:
- Returning **values/data**? → `@st.cache_data`
- Returning a **connection or a loaded model**? → `@st.cache_resource`

```python
@st.cache_resource            # load the model ONCE, share it forever
def get_model():
    return SentenceTransformer("all-MiniLM-L6-v2")

@st.cache_data                # fetch/compute data once per unique input
def load_prices(city):
    return call_some_api(city)
```

## Why `cache_resource` for models specifically
An embedding model or a Groq client is a big live object you want **one** of, shared by everyone.
`cache_resource` returns the *same* object every time (no copying). `cache_data` would try to copy
the return value, which is wrong for a model or a connection. This is exactly why the chat app in
module 07 wraps its Groq client in `@st.cache_resource`.

## See it with your own eyes
`caching_app.py` has a deliberately slow function (`time.sleep(2)`) in two versions: uncached and
cached. Click the buttons:
- **uncached** waits 2 seconds *every* click,
- **cached** waits 2 seconds the *first* time, then is instant.

## Clearing the cache
While developing, if cached results go stale, the app menu (top-right **⋮**) has **"Clear cache"**.
In code you can call `st.cache_data.clear()`.

Run it:
```bash
streamlit run caching_app.py
```

➡ Next: [07-groq-chat-app](../07-groq-chat-app/) — everything so far, combined into a real AI chat app.
