# aevo_bridge.py
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fastmcp import Client
import sys
import json
import uvicorn
from fastapi.middleware.cors import CORSMiddleware
import config

# --- Pydantic Models for Data Validation ---
class PlaceOrderRequest(BaseModel):
    symbol: str
    side: str
    amount: float
    price: float
    wallet_address: str

app = FastAPI(
    title="Aevo MCP Bridge",
    description="Translates HTTP requests into FastMCP tool calls."
)

# --- CORS Middleware ---
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# --- Helper function to parse MCP responses ---
def parse_mcp_response(mcp_result):
    if hasattr(mcp_result, 'content') and isinstance(mcp_result.content, list):
        return mcp_result.content[0].text if hasattr(mcp_result.content[0], 'text') else '{}'
    elif hasattr(mcp_result, 'content') and isinstance(mcp_result.content, str):
        return mcp_result.content
    return '{}'

# ---------------------------------------------------------------------
# Endpoint 1: GET (Market Data)
# ---------------------------------------------------------------------
@app.get("/api/data/market_data/{asset}")
async def get_market_data_endpoint(asset: str):
    """Fetches market statistics by calling the get_market_data MCP tool."""
    try:
        async with Client(config.MCP_SERVER_SCRIPT) as client:
            mcp_result = await client.call_tool("get_market_data", {"asset": asset})
            text_content = parse_mcp_response(mcp_result)
            return json.loads(text_content)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error communicating with MCP Backend: {e}")

# ---------------------------------------------------------------------
# Endpoint 2: GET (Price History for Charts) - THIS IS THE CRUCIAL PART
# ---------------------------------------------------------------------
@app.get("/api/data/price_history/{asset}")
async def get_price_history_endpoint(asset: str):
    """Fetches historical price data for charts."""
    try:
        async with Client(config.MCP_SERVER_SCRIPT) as client:
            mcp_result = await client.call_tool("get_price_history", {"asset": asset})
            text_content = parse_mcp_response(mcp_result)
            return json.loads(text_content)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error fetching price history: {e}")

# ---------------------------------------------------------------------
# Endpoint 3: POST (Place Order)
# ---------------------------------------------------------------------
@app.post("/api/trade/place_order")
async def place_order_endpoint(request: PlaceOrderRequest):
    """Places an order by calling the place_limit_order MCP tool."""
    try:
        async with Client(config.MCP_SERVER_SCRIPT) as client:
            mcp_result = await client.call_tool("place_limit_order", {
                "symbol": request.symbol, "side": request.side, "amount": request.amount,
                "price": request.price, "wallet_address": request.wallet_address,
            })
            message = parse_mcp_response(mcp_result)
            return {"status": "success", "message": message}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error placing order via MCP Backend: {e}")


if __name__ == "__main__":
    print(f"Starting FastAPI Bridge on http://{config.BRIDGE_HOST}:{config.BRIDGE_PORT}...")
    uvicorn.run(app, host=config.BRIDGE_HOST, port=config.BRIDGE_PORT)