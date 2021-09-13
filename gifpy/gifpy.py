import requests
from .errors import GifpyInvalidArgument
from .gif import Gif
from .categories import Category

class Gifpy():

    def __init__(self, key, locale:str = "en_US"):
        self.key = key
        self.locale = locale

    def _get_request(self, method, **kwargs):
        """
        Base GET request for API
        """

        base_url = f"https://g.tenor.com/v1/{method}"
        kwargs["key"] = self.key
        kwargs["locale"] = self.locale

        request = requests.get(base_url, kwargs)
        request.raise_for_status()

        return request.json()

    def search(self, q:str, con_filter = "off", limit:int = 20, med_filter = "minimal", ar_range = "all"):
        """
        Get a list of Gif objects containing the most relevant GIFs 
        for a given search term(s), category(ies), emoji(s), or any combination thereof.

        Parameters
        ----------
        q: `str`
            Search query string
        con_filter: `str`
            Sets contect filters (values: off | low | medium | high)
            specify the content safety filter level
        limit: `int`
            Fetch up to a specified number of results (max: 50).
        media_filter: `str`
            (values: basic | minimal) Reduce the Number of GIF formats returned in the GIF_OBJECT list.
            - minimal - tinygif, gif, and mp4.
            - basic - nanomp4, tinygif, tinymp4, gif, mp4, and nanogif
        ar_range: `str`
            (values: all | wide | standard ) Filter the response GIF_OBJECT list to only include GIFs
            with aspect ratios that fit with in the selected range.
            - all - no constraints
            - wide - 0.42 <= aspect ratio <= 2.36
            - standard - .56 <= aspect ratio <= 1.78
        pos: `str`
            get results starting at position "value". Use a non-zero "next" value returned by API
            results to get the next set of results. pos is not an index and may be an
            integer, float, or string

        Returns
        --------
        List[:class:`Gif`]
            List of Gif objects containing all search results
        """

        search = self._get_request(
            "search",
            q = q,
            limit = limit,
            contentfilter = con_filter,
            media_filter = med_filter,
            ar_range = ar_range
            )

        return [Gif(i) for i in search["results"]]

    def trending(self, con_filter = "off", limit:int = 20, med_filter = "minimal", ar_range = "all"):
        """
        Get a json object containing a list of the current global trending GIFs.
        The trending stream is updated regularly throughout the day.
        """

        search_trending = self._get_request(
            "trending",
            limit = limit,
            contentfilter = con_filter,
            media_filter = med_filter,
            ar_range = ar_range
            )

        return [Gif(i) for i in search_trending["results"]]

    def categories(self, _type: str = "featured", con_filter = "off"):
        """
        Get a list containing Categories object associated with the provided type.
        Each category will include a corresponding search URL to be used if the
        user clicks on the category. The search URL will include the apikey, 
        anonymous id, and locale that were used on the original call to the categories endpoint

        Parameters
        ----------
        type: `str`
            (values: featured | emoji | trending ) determines the type of categories returned
        con_filter: `str`
            Sets contect filters (values: off | low | medium | high)
            specify the content safety filter level

        Returns
        --------
        List[:class:`Catefory`]
            List of Gif objects containing all search results
        """

        search_category = self._get_request(
            "categories",
            type = _type,
            contentfilter = con_filter
            )

        return [Category(i, _type) for i in search_category["tags"]]

    def search_suggestions(self, query, limit = 20) -> list:
        """
        Returns a list of search suggestions
        """

        search_sugg = self._get_request("search_suggestions", q = query, limit = limit)

        return search_sugg["results"]

    def autocomplete(self, query, limit = 20) -> list:
        """
        Returns a list of search autocompletions based on a query
        """

        search_auto = self._get_request("autocomplete", q = query, limit = limit)

        return search_auto["results"]

    def trending_terms(self, limit = 20) -> list:
        """
        Get a list of the current trending search terms.
        The list is updated Hourly by Tenor’s AI.
        """

        search = self._get_request("trending_terms", limit = limit)
        return search["results"]

    def gifs(self, ids, media_filter = "minimal", limit = 20):
        """
        Get the GIF(s) for the corresponding id(s)
        If only one id is fetch a single Gif object will be returned
        If multiple ids are fetched a list

        Parameters
        ----------
        
        ids: `str`
            Comma separated list of GIF IDs (max: 50)
        media_filter `str`
            (values: basic | minimal) Reduce the Number of GIF formats
            returned in the GIF_OBJECT list.
            - minimal - tinygif, gif, and mp4.
            - basic - nanomp4, tinygif, tinymp4, gif, mp4, and nanogif
        limit `int`
            Fetch up to a specified number of results (max: 50).

        Returns
        --------
        If only one id is fetched:
        :class: `Gif`

        If multiple ids are fetched
        List[:class:`Gif`]
            List of Gif objects containing all search results
        """

        if media_filter not in ("basic", "minimal"):
            raise GifpyInvalidArgument()

        if limit > 50:
            raise GifpyInvalidArgument()

        search = self._get_request("gifs", ids = ids, media_filter = media_filter, limit = limit)
        gifs = [Gif(i) for i in search["results"]]

        if len(gifs) == 1:
            return gifs[0]

        return gifs

    def random_gif(self, q:str, con_filter = "off", limit:int = 20, med_filter = "minimal", ar_range = "all"):

        """
        Get a randomized list of GIFs for a given search term. 
        This differs from the search endpoint which returns a rank 
        ordered list of GIFs for a given search term.
        """

        random_search = self._get_request(
            "search",
            q = q,
            limit = limit,
            contentfilter = con_filter,
            media_filter = med_filter,
            ar_range = ar_range
            )

        return [Gif(i) for i in random_search["results"]]

    def anon_id(self, key:str):
        """
        Get an anonymous ID for a new user. Store the ID in the client’s
        cache for use on any additional API calls made by the user, either
        in this session or any future sessions.
        """

        requested_id = self._get_request("anonid", key = key)

        return requested_id["anonId"]