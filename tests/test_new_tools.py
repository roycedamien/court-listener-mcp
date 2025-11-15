"""Tests for new CourtListener MCP server tools."""

import json
from typing import Any

from fastmcp import Client
import pytest

from app.server import mcp


@pytest.fixture
def client() -> Client[Any]:
    """Create a test client connected to the real server.

    Returns
    -------
    Client
        A FastMCP test client connected to the server instance.

    """
    return Client(mcp)


@pytest.mark.asyncio
async def test_new_tools_available(client: Client[Any]) -> None:
    """Test that new tools were properly imported.

    Parameters
    ----------
    client : Client
        The FastMCP test client fixture.

    """
    async with client:
        # List all available tools
        tools = await client.list_tools()
        tool_names = [tool.name for tool in tools]

        # Check new search tools are present with prefix
        expected_new_search_tools = [
            "search_financial_disclosures",
        ]

        for tool_name in expected_new_search_tools:
            assert (
                tool_name in tool_names
            ), f"Expected tool '{tool_name}' not found. Available: {tool_names}"

        # Check new get tools are present with prefix
        expected_new_get_tools = [
            "get_financial_disclosure",
            "get_position",
            "get_education",
            "get_school",
            "get_docket_entry",
            "get_originating_court_information",
        ]

        for tool_name in expected_new_get_tools:
            assert (
                tool_name in tool_names
            ), f"Expected tool '{tool_name}' not found. Available: {tool_names}"


@pytest.mark.asyncio
async def test_financial_disclosures_search_structure(client: Client[Any]) -> None:
    """Test that search_financial_disclosures has proper error handling.

    This test verifies the tool structure without requiring an API key.

    Parameters
    ----------
    client : Client
        The FastMCP test client fixture.

    """
    async with client:
        # Test that the tool exists and can be called
        # Without API key it should raise ValueError
        try:
            result = await client.call_tool(
                "search_financial_disclosures", {"q": "test"}
            )
            # If we get here, either API key exists or the error handling changed
            assert isinstance(result, list)
        except Exception as e:
            # Expected: ValueError about missing API key
            assert "COURT_LISTENER_API_KEY" in str(e) or "API" in str(e)


@pytest.mark.asyncio
async def test_get_tools_structure(client: Client[Any]) -> None:
    """Test that new get tools have proper error handling.

    This test verifies the tool structure without requiring an API key.

    Parameters
    ----------
    client : Client
        The FastMCP test client fixture.

    """
    async with client:
        # Test each new get tool
        new_get_tools = [
            ("get_financial_disclosure", "disclosure_id", "123"),
            ("get_position", "position_id", "123"),
            ("get_education", "education_id", "123"),
            ("get_school", "school_id", "123"),
            ("get_docket_entry", "entry_id", "123"),
            ("get_originating_court_information", "oci_id", "123"),
        ]

        for tool_name, param_name, test_value in new_get_tools:
            try:
                result = await client.call_tool(tool_name, {param_name: test_value})
                # If we get here, either API key exists or the error handling changed
                assert isinstance(result, list)
            except Exception as e:
                # Expected: ValueError about missing API key or HTTP error
                assert (
                    "COURT_LISTENER_API_KEY" in str(e)
                    or "API" in str(e)
                    or "HTTP" in str(e)
                ), f"Unexpected error for {tool_name}: {e}"
