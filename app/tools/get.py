"""Get tools for CourtListener MCP server."""

import os
from typing import Annotated, Any

from dotenv import load_dotenv
from fastmcp import Context, FastMCP
import httpx
from loguru import logger
from pydantic import Field

# Load environment variables
load_dotenv()

# Get API key from environment
API_KEY = os.getenv("COURT_LISTENER_API_KEY")

# Create the get server
get_server: FastMCP[Any] = FastMCP(
    name="CourtListener Get Server",
    instructions="Retrieval server for CourtListener legal database providing direct access to specific records by ID. "
    "This server enables fetching individual records including: court opinions, opinion clusters, court information, "
    "dockets, oral argument audio recordings, and judge/legal professional profiles. "
    "Each tool requires the specific ID of the record to retrieve and returns detailed information about that record. "
    "Use this server when you have a specific ID and need complete details about a particular legal entity.",
)


@get_server.tool()
async def opinion(
    opinion_id: Annotated[str, Field(description="The opinion ID to retrieve")],
    ctx: Context | None = None,
) -> dict[str, Any]:
    """Get a specific court opinion by ID from CourtListener.

    Args:
        opinion_id: The opinion ID to retrieve.
        ctx: Optional context for logging and error reporting.

    Returns:
        dict: The opinion data as returned by the CourtListener API.

    Raises:
        ValueError: If the COURT_LISTENER_API_KEY is not found in environment variables.

    """
    if ctx:
        await ctx.info(f"Getting opinion with ID: {opinion_id}")
    else:
        logger.info(f"Getting opinion with ID: {opinion_id}")

    if not API_KEY:
        error_msg = "COURT_LISTENER_API_KEY not found in environment variables"
        if ctx:
            await ctx.error(error_msg)
        else:
            logger.error(error_msg)
        raise ValueError(error_msg)

    headers = {"Authorization": f"Token {API_KEY}"}

    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(
                f"https://www.courtlistener.com/api/rest/v4/opinions/{opinion_id}/",
                headers=headers,
                timeout=30.0,
            )
            response.raise_for_status()

            if ctx:
                await ctx.info(f"Successfully retrieved opinion {opinion_id}")
            else:
                logger.info(f"Successfully retrieved opinion {opinion_id}")

            return response.json()

    except httpx.HTTPStatusError as e:
        error_msg = f"HTTP error getting opinion: {e}"
        if ctx:
            await ctx.error(error_msg)
        else:
            logger.error(error_msg)
        raise e
    except Exception as e:
        error_msg = f"Error getting opinion: {e}"
        if ctx:
            await ctx.error(error_msg)
        else:
            logger.error(error_msg)
        raise e


@get_server.tool()
async def docket(
    docket_id: Annotated[str, Field(description="The docket ID to retrieve")],
    ctx: Context | None = None,
) -> dict[str, Any]:
    """Get a specific court docket by ID from CourtListener.

    Args:
        docket_id: The docket ID to retrieve.
        ctx: Optional context for logging and error reporting.

    Returns:
        dict: The docket data as returned by the CourtListener API.

    Raises:
        ValueError: If the COURT_LISTENER_API_KEY is not found in environment variables.

    """
    if ctx:
        await ctx.info(f"Getting docket with ID: {docket_id}")
    else:
        logger.info(f"Getting docket with ID: {docket_id}")

    if not API_KEY:
        error_msg = "COURT_LISTENER_API_KEY not found in environment variables"
        if ctx:
            await ctx.error(error_msg)
        else:
            logger.error(error_msg)
        raise ValueError(error_msg)

    headers = {"Authorization": f"Token {API_KEY}"}

    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(
                f"https://www.courtlistener.com/api/rest/v4/dockets/{docket_id}/",
                headers=headers,
                timeout=30.0,
            )
            response.raise_for_status()

            if ctx:
                await ctx.info(f"Successfully retrieved docket {docket_id}")
            else:
                logger.info(f"Successfully retrieved docket {docket_id}")

            return response.json()

    except httpx.HTTPStatusError as e:
        error_msg = f"HTTP error getting docket: {e}"
        if ctx:
            await ctx.error(error_msg)
        else:
            logger.error(error_msg)
        raise e
    except Exception as e:
        error_msg = f"Error getting docket: {e}"
        if ctx:
            await ctx.error(error_msg)
        else:
            logger.error(error_msg)
        raise e


@get_server.tool()
async def audio(
    audio_id: Annotated[str, Field(description="The audio recording ID to retrieve")],
    ctx: Context | None = None,
) -> dict[str, Any]:
    """Get oral argument audio information by ID from CourtListener.

    Args:
        audio_id: The audio recording ID to retrieve.
        ctx: Optional context for logging and error reporting.

    Returns:
        dict: The audio data as returned by the CourtListener API.

    Raises:
        ValueError: If the COURT_LISTENER_API_KEY is not found in environment variables.

    """
    if ctx:
        await ctx.info(f"Getting audio with ID: {audio_id}")
    else:
        logger.info(f"Getting audio with ID: {audio_id}")

    if not API_KEY:
        error_msg = "COURT_LISTENER_API_KEY not found in environment variables"
        if ctx:
            await ctx.error(error_msg)
        else:
            logger.error(error_msg)
        raise ValueError(error_msg)

    headers = {"Authorization": f"Token {API_KEY}"}

    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(
                f"https://www.courtlistener.com/api/rest/v4/audio/{audio_id}/",
                headers=headers,
                timeout=30.0,
            )
            response.raise_for_status()

            if ctx:
                await ctx.info(f"Successfully retrieved audio {audio_id}")
            else:
                logger.info(f"Successfully retrieved audio {audio_id}")

            return response.json()

    except httpx.HTTPStatusError as e:
        error_msg = f"HTTP error getting audio: {e}"
        if ctx:
            await ctx.error(error_msg)
        else:
            logger.error(error_msg)
        raise e
    except Exception as e:
        error_msg = f"Error getting audio: {e}"
        if ctx:
            await ctx.error(error_msg)
        else:
            logger.error(error_msg)
        raise e


@get_server.tool()
async def cluster(
    cluster_id: Annotated[str, Field(description="The opinion cluster ID to retrieve")],
    ctx: Context | None = None,
) -> dict[str, Any]:
    """Get an opinion cluster by ID from CourtListener.

    Args:
        cluster_id: The opinion cluster ID to retrieve.
        ctx: Optional context for logging and error reporting.

    Returns:
        dict: The opinion cluster data as returned by the CourtListener API.

    Raises:
        ValueError: If the COURT_LISTENER_API_KEY is not found in environment variables.

    """
    if ctx:
        await ctx.info(f"Getting cluster with ID: {cluster_id}")
    else:
        logger.info(f"Getting cluster with ID: {cluster_id}")

    if not API_KEY:
        error_msg = "COURT_LISTENER_API_KEY not found in environment variables"
        if ctx:
            await ctx.error(error_msg)
        else:
            logger.error(error_msg)
        raise ValueError(error_msg)

    headers = {"Authorization": f"Token {API_KEY}"}

    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(
                f"https://www.courtlistener.com/api/rest/v4/clusters/{cluster_id}/",
                headers=headers,
                timeout=30.0,
            )
            response.raise_for_status()

            if ctx:
                await ctx.info(f"Successfully retrieved cluster {cluster_id}")
            else:
                logger.info(f"Successfully retrieved cluster {cluster_id}")

            return response.json()

    except httpx.HTTPStatusError as e:
        error_msg = f"HTTP error getting cluster: {e}"
        if ctx:
            await ctx.error(error_msg)
        else:
            logger.error(error_msg)
        raise e
    except Exception as e:
        error_msg = f"Error getting cluster: {e}"
        if ctx:
            await ctx.error(error_msg)
        else:
            logger.error(error_msg)
        raise e


@get_server.tool()
async def person(
    person_id: Annotated[str, Field(description="The person (judge) ID to retrieve")],
    ctx: Context | None = None,
) -> dict[str, Any]:
    """Get judge or legal professional information by ID from CourtListener.

    Args:
        person_id: The person (judge) ID to retrieve.
        ctx: Optional context for logging and error reporting.

    Returns:
        dict: The person data as returned by the CourtListener API.

    Raises:
        ValueError: If the COURT_LISTENER_API_KEY is not found in environment variables.

    """
    if ctx:
        await ctx.info(f"Getting person with ID: {person_id}")
    else:
        logger.info(f"Getting person with ID: {person_id}")

    if not API_KEY:
        error_msg = "COURT_LISTENER_API_KEY not found in environment variables"
        if ctx:
            await ctx.error(error_msg)
        else:
            logger.error(error_msg)
        raise ValueError(error_msg)

    headers = {"Authorization": f"Token {API_KEY}"}

    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(
                f"https://www.courtlistener.com/api/rest/v4/people/{person_id}/",
                headers=headers,
                timeout=30.0,
            )
            response.raise_for_status()

            if ctx:
                await ctx.info(f"Successfully retrieved person {person_id}")
            else:
                logger.info(f"Successfully retrieved person {person_id}")

            return response.json()

    except httpx.HTTPStatusError as e:
        error_msg = f"HTTP error getting person: {e}"
        if ctx:
            await ctx.error(error_msg)
        else:
            logger.error(error_msg)
        raise e
    except Exception as e:
        error_msg = f"Error getting person: {e}"
        if ctx:
            await ctx.error(error_msg)
        else:
            logger.error(error_msg)
        raise e


@get_server.tool()
async def court(
    court_id: Annotated[
        str, Field(description="The court ID to retrieve (e.g., 'scotus', 'ca9')")
    ],
    ctx: Context | None = None,
) -> dict[str, Any]:
    """Get court information by ID from CourtListener.

    Args:
        court_id: The court ID to retrieve (e.g., 'scotus', 'ca9').
        ctx: Optional context for logging and error reporting.

    Returns:
        dict: The court data as returned by the CourtListener API.

    Raises:
        ValueError: If the COURT_LISTENER_API_KEY is not found in environment variables.

    """
    if ctx:
        await ctx.info(f"Getting court with ID: {court_id}")
    else:
        logger.info(f"Getting court with ID: {court_id}")

    if not API_KEY:
        error_msg = "COURT_LISTENER_API_KEY not found in environment variables"
        if ctx:
            await ctx.error(error_msg)
        else:
            logger.error(error_msg)
        raise ValueError(error_msg)

    headers = {"Authorization": f"Token {API_KEY}"}

    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(
                f"https://www.courtlistener.com/api/rest/v4/courts/{court_id}/",
                headers=headers,
                timeout=30.0,
            )
            response.raise_for_status()

            if ctx:
                await ctx.info(f"Successfully retrieved court {court_id}")
            else:
                logger.info(f"Successfully retrieved court {court_id}")

            return response.json()

    except httpx.HTTPStatusError as e:
        error_msg = f"HTTP error getting court: {e}"
        if ctx:
            await ctx.error(error_msg)
        else:
            logger.error(error_msg)
        raise e
    except Exception as e:
        error_msg = f"Error getting court: {e}"
        if ctx:
            await ctx.error(error_msg)
        else:
            logger.error(error_msg)
        raise e


@get_server.tool()
async def financial_disclosure(
    disclosure_id: Annotated[
        str, Field(description="The financial disclosure ID to retrieve")
    ],
    ctx: Context | None = None,
) -> dict[str, Any]:
    """Get a specific judge financial disclosure report by ID from CourtListener.

    This is useful for researching judges presiding over cases to understand
    potential conflicts of interest, especially in medical malpractice cases.

    Args:
        disclosure_id: The financial disclosure ID to retrieve.
        ctx: Optional context for logging and error reporting.

    Returns:
        dict: The financial disclosure data as returned by the CourtListener API.

    Raises:
        ValueError: If the COURT_LISTENER_API_KEY is not found in environment variables.

    """
    if ctx:
        await ctx.info(f"Getting financial disclosure with ID: {disclosure_id}")
    else:
        logger.info(f"Getting financial disclosure with ID: {disclosure_id}")

    if not API_KEY:
        error_msg = "COURT_LISTENER_API_KEY not found in environment variables"
        if ctx:
            await ctx.error(error_msg)
        else:
            logger.error(error_msg)
        raise ValueError(error_msg)

    headers = {"Authorization": f"Token {API_KEY}"}

    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(
                f"https://www.courtlistener.com/api/rest/v4/financial-disclosures/{disclosure_id}/",
                headers=headers,
                timeout=30.0,
            )
            response.raise_for_status()

            if ctx:
                await ctx.info(
                    f"Successfully retrieved financial disclosure {disclosure_id}"
                )
            else:
                logger.info(
                    f"Successfully retrieved financial disclosure {disclosure_id}"
                )

            return response.json()

    except httpx.HTTPStatusError as e:
        error_msg = f"HTTP error getting financial disclosure: {e}"
        if ctx:
            await ctx.error(error_msg)
        else:
            logger.error(error_msg)
        raise e
    except Exception as e:
        error_msg = f"Error getting financial disclosure: {e}"
        if ctx:
            await ctx.error(error_msg)
        else:
            logger.error(error_msg)
        raise e


@get_server.tool()
async def position(
    position_id: Annotated[str, Field(description="The position ID to retrieve")],
    ctx: Context | None = None,
) -> dict[str, Any]:
    """Get a specific judge position/appointment information by ID from CourtListener.

    This provides details about a judge's appointment, including court, appointing
    authority, and dates of service.

    Args:
        position_id: The position ID to retrieve.
        ctx: Optional context for logging and error reporting.

    Returns:
        dict: The position data as returned by the CourtListener API.

    Raises:
        ValueError: If the COURT_LISTENER_API_KEY is not found in environment variables.

    """
    if ctx:
        await ctx.info(f"Getting position with ID: {position_id}")
    else:
        logger.info(f"Getting position with ID: {position_id}")

    if not API_KEY:
        error_msg = "COURT_LISTENER_API_KEY not found in environment variables"
        if ctx:
            await ctx.error(error_msg)
        else:
            logger.error(error_msg)
        raise ValueError(error_msg)

    headers = {"Authorization": f"Token {API_KEY}"}

    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(
                f"https://www.courtlistener.com/api/rest/v4/positions/{position_id}/",
                headers=headers,
                timeout=30.0,
            )
            response.raise_for_status()

            if ctx:
                await ctx.info(f"Successfully retrieved position {position_id}")
            else:
                logger.info(f"Successfully retrieved position {position_id}")

            return response.json()

    except httpx.HTTPStatusError as e:
        error_msg = f"HTTP error getting position: {e}"
        if ctx:
            await ctx.error(error_msg)
        else:
            logger.error(error_msg)
        raise e
    except Exception as e:
        error_msg = f"Error getting position: {e}"
        if ctx:
            await ctx.error(error_msg)
        else:
            logger.error(error_msg)
        raise e


@get_server.tool()
async def education(
    education_id: Annotated[str, Field(description="The education ID to retrieve")],
    ctx: Context | None = None,
) -> dict[str, Any]:
    """Get a specific judge education information by ID from CourtListener.

    This provides details about a judge's educational background, including
    law school and degrees obtained.

    Args:
        education_id: The education ID to retrieve.
        ctx: Optional context for logging and error reporting.

    Returns:
        dict: The education data as returned by the CourtListener API.

    Raises:
        ValueError: If the COURT_LISTENER_API_KEY is not found in environment variables.

    """
    if ctx:
        await ctx.info(f"Getting education with ID: {education_id}")
    else:
        logger.info(f"Getting education with ID: {education_id}")

    if not API_KEY:
        error_msg = "COURT_LISTENER_API_KEY not found in environment variables"
        if ctx:
            await ctx.error(error_msg)
        else:
            logger.error(error_msg)
        raise ValueError(error_msg)

    headers = {"Authorization": f"Token {API_KEY}"}

    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(
                f"https://www.courtlistener.com/api/rest/v4/educations/{education_id}/",
                headers=headers,
                timeout=30.0,
            )
            response.raise_for_status()

            if ctx:
                await ctx.info(f"Successfully retrieved education {education_id}")
            else:
                logger.info(f"Successfully retrieved education {education_id}")

            return response.json()

    except httpx.HTTPStatusError as e:
        error_msg = f"HTTP error getting education: {e}"
        if ctx:
            await ctx.error(error_msg)
        else:
            logger.error(error_msg)
        raise e
    except Exception as e:
        error_msg = f"Error getting education: {e}"
        if ctx:
            await ctx.error(error_msg)
        else:
            logger.error(error_msg)
        raise e


@get_server.tool()
async def school(
    school_id: Annotated[str, Field(description="The school ID to retrieve")],
    ctx: Context | None = None,
) -> dict[str, Any]:
    """Get a specific law school information by ID from CourtListener.

    This provides details about a law school attended by judges.

    Args:
        school_id: The school ID to retrieve.
        ctx: Optional context for logging and error reporting.

    Returns:
        dict: The school data as returned by the CourtListener API.

    Raises:
        ValueError: If the COURT_LISTENER_API_KEY is not found in environment variables.

    """
    if ctx:
        await ctx.info(f"Getting school with ID: {school_id}")
    else:
        logger.info(f"Getting school with ID: {school_id}")

    if not API_KEY:
        error_msg = "COURT_LISTENER_API_KEY not found in environment variables"
        if ctx:
            await ctx.error(error_msg)
        else:
            logger.error(error_msg)
        raise ValueError(error_msg)

    headers = {"Authorization": f"Token {API_KEY}"}

    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(
                f"https://www.courtlistener.com/api/rest/v4/schools/{school_id}/",
                headers=headers,
                timeout=30.0,
            )
            response.raise_for_status()

            if ctx:
                await ctx.info(f"Successfully retrieved school {school_id}")
            else:
                logger.info(f"Successfully retrieved school {school_id}")

            return response.json()

    except httpx.HTTPStatusError as e:
        error_msg = f"HTTP error getting school: {e}"
        if ctx:
            await ctx.error(error_msg)
        else:
            logger.error(error_msg)
        raise e
    except Exception as e:
        error_msg = f"Error getting school: {e}"
        if ctx:
            await ctx.error(error_msg)
        else:
            logger.error(error_msg)
        raise e


@get_server.tool()
async def docket_entry(
    entry_id: Annotated[str, Field(description="The docket entry ID to retrieve")],
    ctx: Context | None = None,
) -> dict[str, Any]:
    """Get a specific docket entry by ID from CourtListener.

    Docket entries represent individual items on a docket, such as motions,
    orders, and other filings. This is essential for tracking case progression
    in medical malpractice and other litigation.

    Args:
        entry_id: The docket entry ID to retrieve.
        ctx: Optional context for logging and error reporting.

    Returns:
        dict: The docket entry data as returned by the CourtListener API.

    Raises:
        ValueError: If the COURT_LISTENER_API_KEY is not found in environment variables.

    """
    if ctx:
        await ctx.info(f"Getting docket entry with ID: {entry_id}")
    else:
        logger.info(f"Getting docket entry with ID: {entry_id}")

    if not API_KEY:
        error_msg = "COURT_LISTENER_API_KEY not found in environment variables"
        if ctx:
            await ctx.error(error_msg)
        else:
            logger.error(error_msg)
        raise ValueError(error_msg)

    headers = {"Authorization": f"Token {API_KEY}"}

    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(
                f"https://www.courtlistener.com/api/rest/v4/docket-entries/{entry_id}/",
                headers=headers,
                timeout=30.0,
            )
            response.raise_for_status()

            if ctx:
                await ctx.info(f"Successfully retrieved docket entry {entry_id}")
            else:
                logger.info(f"Successfully retrieved docket entry {entry_id}")

            return response.json()

    except httpx.HTTPStatusError as e:
        error_msg = f"HTTP error getting docket entry: {e}"
        if ctx:
            await ctx.error(error_msg)
        else:
            logger.error(error_msg)
        raise e
    except Exception as e:
        error_msg = f"Error getting docket entry: {e}"
        if ctx:
            await ctx.error(error_msg)
        else:
            logger.error(error_msg)
        raise e


@get_server.tool()
async def originating_court_information(
    oci_id: Annotated[
        str, Field(description="The originating court information ID to retrieve")
    ],
    ctx: Context | None = None,
) -> dict[str, Any]:
    """Get originating court information by ID from CourtListener.

    This provides information about the court where a case originated before
    being appealed or transferred. Useful for understanding case history.

    Args:
        oci_id: The originating court information ID to retrieve.
        ctx: Optional context for logging and error reporting.

    Returns:
        dict: The originating court information data as returned by the CourtListener API.

    Raises:
        ValueError: If the COURT_LISTENER_API_KEY is not found in environment variables.

    """
    if ctx:
        await ctx.info(f"Getting originating court information with ID: {oci_id}")
    else:
        logger.info(f"Getting originating court information with ID: {oci_id}")

    if not API_KEY:
        error_msg = "COURT_LISTENER_API_KEY not found in environment variables"
        if ctx:
            await ctx.error(error_msg)
        else:
            logger.error(error_msg)
        raise ValueError(error_msg)

    headers = {"Authorization": f"Token {API_KEY}"}

    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(
                f"https://www.courtlistener.com/api/rest/v4/originating-court-information/{oci_id}/",
                headers=headers,
                timeout=30.0,
            )
            response.raise_for_status()

            if ctx:
                await ctx.info(
                    f"Successfully retrieved originating court information {oci_id}"
                )
            else:
                logger.info(
                    f"Successfully retrieved originating court information {oci_id}"
                )

            return response.json()

    except httpx.HTTPStatusError as e:
        error_msg = f"HTTP error getting originating court information: {e}"
        if ctx:
            await ctx.error(error_msg)
        else:
            logger.error(error_msg)
        raise e
    except Exception as e:
        error_msg = f"Error getting originating court information: {e}"
        if ctx:
            await ctx.error(error_msg)
        else:
            logger.error(error_msg)
        raise e
