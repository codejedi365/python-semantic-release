"""Common functionality and interface for interacting with Git remote VCS"""

from __future__ import annotations

from pathlib import PurePosixPath
from typing import TYPE_CHECKING

from urllib3.util.url import Url, parse_url

if TYPE_CHECKING:
    pass


class HvcsUrlMixin:

    def create_server_url(
        self,
        path: str,
        auth: str | None = None,
        query: str | None = None,
        fragment: str | None = None,
    ) -> str:
        if not hasattr(self, "hvcs_domain"):
            raise AttributeError(
                "HvcsUrlMixin requires the hvcs_domain attribute to be set"
            )

        domain = getattr(self, "hvcs_domain")

        if not isinstance(domain, Url):
            raise TypeError(
                f"Invalid hvcs_domain type ({type(domain)}) received, expected Url"
            )

        # Ensure any path prefix is transferred but not doubled up on the derived url
        normalized_path = (
            f"{domain.path}/{path}"
            if domain.path and not path.startswith(domain.path)
            else path
        )
        return self._derive_url(
            domain,
            path=normalized_path,
            auth=auth,
            query=query,
            fragment=fragment,
        )

    def create_repo_url(
        self,
        repo_path: str,
        query: str | None = None,
        fragment: str | None = None,
    ) -> str:
        if not hasattr(self, "owner"):
            raise AttributeError("HvcsUrlMixin requires the owner attribute to be set")

        if not hasattr(self, "repo_name"):
            raise AttributeError(
                "HvcsUrlMixin requires the repo_name attribute to be set"
            )

        owner = getattr(self, "owner")
        repo_name = getattr(self, "repo_name")

        return self.create_server_url(
            path=f"/{owner}/{repo_name}/{repo_path}",
            query=query,
            fragment=fragment,
        )

    def create_api_url(
        self,
        endpoint: str,
        auth: str | None = None,
        query: str | None = None,
        fragment: str | None = None,
    ) -> str:
        if not hasattr(self, "api_url"):
            raise AttributeError("HvcsUrlMixin requires the api_url attribute to be set")

        api_url = getattr(self, "api_url")

        if not isinstance(api_url, Url):
            raise TypeError(
                f"Invalid api_url type ({type(api_url)}) received, expected Url"
            )

        # Ensure any api path prefix is transferred but not doubled up on the derived api url
        normalized_endpoint = (
            f"{api_url.path}/{endpoint}"
            if api_url.path and not endpoint.startswith(api_url.path)
            else endpoint
        )
        return self._derive_url(
            api_url,
            path=normalized_endpoint,
            auth=auth,
            query=query,
            fragment=fragment,
        )

    @staticmethod
    def _derive_url(
        base_url: Url,
        path: str,
        auth: str | None = None,
        query: str | None = None,
        fragment: str | None = None,
    ) -> str:
        overrides = dict(
            filter(
                lambda x: x[1] is not None,
                {
                    "auth": auth,
                    "path": str(PurePosixPath("/", path.lstrip("/"))),
                    "query": query,
                    "fragment": fragment,
                }.items(),
            )
        )
        return Url(
            **{
                **base_url._asdict(),
                **overrides,
            }
        ).url.rstrip("/")

    @staticmethod
    def _validate_url_scheme(url: Url, allow_insecure: bool = False) -> None:
        if url.scheme == "http" and not allow_insecure:
            raise ValueError("Insecure connections are currently disabled.")

        if url.scheme not in ["http", "https"]:
            raise ValueError(
                f"Invalid scheme {url.scheme} for {url.host}. "
                "Only http and https are supported."
            )

    @staticmethod
    def _normalize_url(url: Url | str, allow_insecure: bool = False) -> Url:
        """
        Function to ensure url scheme is populated & allowed

        Raises
        ------
        TypeError: when url parameter is not a string or parsable url
        ValueError: when the url scheme is not http or https

        """
        tgt_url = parse_url(url) if isinstance(url, str) else url
        if not isinstance(tgt_url, Url):
            raise TypeError(
                f"Invalid url type ({type(tgt_url)}) received, expected Url or string"
            )

        if not tgt_url.scheme:
            new_scheme = "http" if allow_insecure else "https"
            tgt_url = Url(**{**tgt_url._asdict(), "scheme": new_scheme})

        HvcsUrlMixin._validate_url_scheme(tgt_url, allow_insecure=allow_insecure)
        return tgt_url
