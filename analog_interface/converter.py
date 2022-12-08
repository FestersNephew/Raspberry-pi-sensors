from sensor import MCP3004

# SPI bus=0, CS=0, V_ref=3.3V
mcp = MCP3004(bus=0, addr=0, vref=3.3)

mcp.voltage(0)  # read voltage on channel 0