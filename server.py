#!/usr/bin/env python3
"""
FastMCP Server for Aevo Trading Client.
This version uses STATIC, pre-built data for stability and predictability.
"""
import json
from fastmcp import FastMCP

# --- Pre-built Static Chart & Market Data ---
# All price data is now fixed. No live simulation.
STATIC_ASSET_DATA = {
    "ETH": {
        "market_data": {"symbol": "ETH-PERP", "index_price": "4150.00", "daily_volume_usd": "1200000000.00", "24h_change": "+1.5%"},
        "chart_data": [
            {"t": 1729423800000, "y": 4120.55}, {"t": 1729424400000, "y": 4125.10}, {"t": 1729425000000, "y": 4130.90}, 
            {"t": 1729425600000, "y": 4128.75}, {"t": 1729426200000, "y": 4135.20}, {"t": 1729426800000, "y": 4140.00}, 
            {"t": 1729427400000, "y": 4145.80}, {"t": 1729428000000, "y": 4142.30}, {"t": 1729428600000, "y": 4150.00}
        ]
    },
    "BTC": {
        "market_data": {"symbol": "BTC-PERP", "index_price": "67000.00", "daily_volume_usd": "3500000000.00", "24h_change": "-0.5%"},
        "chart_data": [
            {"t": 1729423800000, "y": 67150.10}, {"t": 1729424400000, "y": 67100.20}, {"t": 1729425000000, "y": 67050.50}, 
            {"t": 1729425600000, "y": 67080.90}, {"t": 1729426200000, "y": 67020.30}, {"t": 1729426800000, "y": 66980.00}, 
            {"t": 1729427400000, "y": 66950.70}, {"t": 1729428000000, "y": 67010.40}, {"t": 1729428600000, "y": 67000.00}
        ]
    },
    "DOGE": {
        "market_data": {"symbol": "DOGE-PERP", "index_price": "0.15", "daily_volume_usd": "450000000.00", "24h_change": "-1.8%"},
        "chart_data": [
            {"t": 1729423800000, "y": 0.155}, {"t": 1729424400000, "y": 0.154}, {"t": 1729425000000, "y": 0.156}, 
            {"t": 1729425600000, "y": 0.153}, {"t": 1729426200000, "y": 0.152}, {"t": 1729426800000, "y": 0.151}, 
            {"t": 1729427400000, "y": 0.150}, {"t": 1729428000000, "y": 0.152}, {"t": 1729428600000, "y": 0.150}
        ]
    },
    "SOL": {
        "market_data": {"symbol": "SOL-PERP", "index_price": "165.50", "daily_volume_usd": "800000000.00", "24h_change": "+3.2%"},
        "chart_data": [
            {"t": 1729423800000, "y": 162.10}, {"t": 1729424400000, "y": 163.40}, {"t": 1729425000000, "y": 162.90}, 
            {"t": 1729425600000, "y": 164.80}, {"t": 1729426200000, "y": 165.10}, {"t": 1729426800000, "y": 164.50}, 
            {"t": 1729427400000, "y": 165.90}, {"t": 1729428000000, "y": 165.20}, {"t": 1729428600000, "y": 165.50}
        ]
    },
    "BNB": {
        "market_data": {"symbol": "BNB-PERP", "index_price": "605.00", "daily_volume_usd": "1500000000.00", "24h_change": "+0.8%"},
        "chart_data": [
            {"t": 1729423800000, "y": 602.30}, {"t": 1729424400000, "y": 601.90}, {"t": 1729425000000, "y": 603.50}, 
            {"t": 1729425600000, "y": 604.10}, {"t": 1729426200000, "y": 603.80}, {"t": 1729426800000, "y": 605.20}, 
            {"t": 1729427400000, "y": 604.90}, {"t": 1729428000000, "y": 605.50}, {"t": 1729428600000, "y": 605.00}
        ]
    }
}

mcp = FastMCP("Aevo Static Trading Server")

@mcp.tool()
async def get_market_data(asset: str) -> str:
    """Fetches STATIC market statistics for an asset."""
    asset_info = STATIC_ASSET_DATA.get(asset.upper())
    if asset_info:
        return json.dumps(asset_info["market_data"])
    return json.dumps({"error": "Asset not found"})

@mcp.tool()
async def get_price_history(asset: str) -> str:
    """Fetches a STATIC, pre-built price history for an asset."""
    asset_info = STATIC_ASSET_DATA.get(asset.upper())
    if asset_info:
        return json.dumps(asset_info["chart_data"])
    return json.dumps({"error": "Asset not found"})

@mcp.tool()
async def place_limit_order(symbol: str, side: str, amount: float, price: float, wallet_address: str) -> str:
    """Simulates placing a limit order."""
    return f"Order placed! {side} {amount} {symbol} @ {price} for wallet {wallet_address[:8]}... Sent to Aevo Testnet."

def main():
    mcp.run()

if __name__ == "__main__":
    main()
