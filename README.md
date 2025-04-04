# SOL Price Tracker

<div align="center">
  
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/Python-3.6+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![WebSocket](https://img.shields.io/badge/WebSocket-Client-2ea44f?style=for-the-badge&logo=socket.io&logoColor=white)](https://github.com/websocket-client/websocket-client)
[![Pyth Network](https://img.shields.io/badge/Pyth_Network-Oracle-4d276c?style=for-the-badge)](https://pyth.network/)
[![Solana](https://img.shields.io/badge/Solana-Price_Data-9945FF?style=for-the-badge&logo=solana&logoColor=white)](https://solana.com)

<br>
<a href="https://www.python.org/"><img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" width="50" height="50" alt="Python"/></a>&nbsp;
<a href="https://github.com/websocket-client/websocket-client"><img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/nodejs/nodejs-original.svg" width="50" height="50" alt="WebSocket"/></a>&nbsp;
<a href="https://solana.com"><img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/solana/solana-original.svg" width="50" height="50" alt="Solana"/></a>&nbsp;
<a href="https://pyth.network/"><img src="https://raw.githubusercontent.com/devicons/devicon/55609aa5bd817ff167afce0d965585c92040787a/icons/devicon/devicon-original.svg" width="50" height="50" alt="Pyth Network"/></a>

</div>

<div align="center">
<h3>High-performance terminal-based price oracle for real-time Solana price monitoring</h3>
</div>

<hr>

## Overview

SOL Price Tracker is a high-performance, terminal-based application designed for real-time monitoring of Solana (SOL) price data via the Pyth Network Oracle. This tool provides developers and traders with accurate, low-latency price feeds with visual indicators optimized for terminal environments.

## Technical Architecture

<table>
<tr>
<th width="180">Component</th>
<th>Description</th>
</tr>
<tr>
<td><b>Data Source</b></td>
<td>Pyth Network Hermes WebSocket API endpoint</td>
</tr>
<tr>
<td><b>Data Processing</b></td>
<td>Real-time JSON parsing and numerical transformations</td>
</tr>
<tr>
<td><b>Display Logic</b></td>
<td>Terminal-optimized visualization with ANSI color coding</td>
</tr>
<tr>
<td><b>Updates Management</b></td>
<td>Conditional refresh based on configurable price delta thresholds</td>
</tr>
</table>

## Core Technologies

<table>
<tr>
<th width="180"><div align="center">Technology</div></th>
<th width="180"><div align="center">Purpose</div></th>
<th><div align="center">Details</div></th>
</tr>
<tr>
<td align="center">
<img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" width="40" height="40"/><br>
<b>Python 3.6+</b>
</td>
<td>Core runtime environment</td>
<td>Primary programming language with standard libraries for JSON processing and datetime handling <a href="https://www.python.org/">python.org</a></td>
</tr>
<tr>
<td align="center">
<img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/socketio/socketio-original.svg" width="40" height="40"/><br>
<b>websocket-client</b>
</td>
<td>WebSocket connectivity</td>
<td>Reliable WebSocket client library for Python with comprehensive event handling <a href="https://github.com/websocket-client/websocket-client">GitHub</a></td>
</tr>
<tr>
<td align="center">
<img src="https://avatars.githubusercontent.com/u/68587457?s=200&v=4" width="40" height="40"/><br>
<b>Pyth Network API</b>
</td>
<td>Price oracle data source</td>
<td>Decentralized financial market data provider with low-latency WebSocket feeds <a href="https://docs.pyth.network/">docs.pyth.network</a></td>
</tr>
<tr>
<td align="center">
<img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/linux/linux-original.svg" width="40" height="40"/><br>
<b>ANSI Terminal</b>
</td>
<td>Visual output formatting</td>
<td>Color-coded terminal output using ANSI escape sequences for enhanced visualization <a href="https://en.wikipedia.org/wiki/ANSI_escape_code">ANSI Reference</a></td>
</tr>
</table>

## Technical Specifications

### WebSocket Implementation

The application establishes a persistent WebSocket connection to Pyth Network's API endpoint:

```python
WS_URL = "wss://hermes.pyth.network/ws"
```

### Price Feed Configuration

SOL/USD price data is sourced using Pyth Network's specific feed identifier:

```python
SOL_FEED_ID = "0xef0d8b6fda2ceba41da15d4095d1da392a0d2f8ed0c6c7bc0f4cfac8c280b56d"
```

### Data Processing Pipeline

<details>
<summary><b>Expand to view the data flow architecture</b></summary>

1. **Subscription Initialization**
   - Client connects to WebSocket endpoint
   - Subscription message sent with SOL feed ID
   - Connection established with Pyth Network oracle

2. **Message Processing**
   - WebSocket messages received as JSON payloads
   - Message type validation and filtering
   - JSON parsing and data extraction

3. **Price Data Extraction**
   - Raw price integer retrieval
   - Exponent application
   - Confidence interval calculation
   - Timestamp conversion to UTC

4. **Delta Calculation Logic**
   - Previous price state maintenance
   - Current vs previous price comparison
   - Directional change determination
   - Magnitude calculation for visual indicators

5. **Threshold-Based Display Logic**
   - Configurable update threshold (0.001)
   - Conditional output based on price delta
   - Optimization to reduce noise in output

6. **Visual Formatting**
   - ANSI color application (green/red)
   - Directional indicators (▲/▼)
   - Magnitude visualization via bar count
   - Precision-controlled decimal formatting
</details>

### Sample Output

```
Subscribed to SOL/USD feed
SOL/USD | $  123.4567 ± 0.0123 | 13:45:22 UTC | START | Change: N/A
SOL/USD | $  123.4789 ± 0.0125 | 13:45:24 UTC | ▲| | Change: +0.0222
SOL/USD | $  123.4321 ± 0.0124 | 13:45:30 UTC | ▼||| | Change: -0.0468
```

## Installation & Configuration

### System Requirements

<table>
<tr><td width="200"><b>Python 3.6+</b></td><td>Required for core application execution</td></tr>
<tr><td><b>Network Connectivity</b></td><td>Access to Pyth Network endpoints</td></tr>
<tr><td><b>Terminal</b></td><td>ANSI color support required for visual indicators</td></tr>
</table>

### Dependency Installation

```bash
pip install websocket-client
```

### Application Setup

```bash
git clone https://github.com/aminnizamdev/sol-price-tracker.git
cd sol-price-tracker
```

### Execution

```bash
python sol_price_tracker.py
```

## Technical Customization Options

The application architecture supports several customization points:

### Threshold Configuration

Modify the update threshold (currently 0.001) to control display frequency:

```python
# Example modification to increase threshold to 0.01
if last_price is None or abs(real_price - last_price) >= 0.01:
    # Display price update
```

### Asset Selection

Configure alternative price feeds by modifying the feed ID constant:

```python
# Example: BTC/USD feed
BTC_FEED_ID = "0xe62df6c8b4a85fe1a67db44dc12de5db330f7ac66b72dc658afedf0f4a415b43"
```

### Visual Output Configuration

The display formatting can be adjusted through the ANSI color codes and string formatting parameters:

```python
# Color configuration
GREEN = '\033[92m'  # Color for price increases
RED = '\033[91m'    # Color for price decreases
CYAN = '\033[96m'   # Color for neutral/info
```

## Error Handling

The application implements comprehensive error handling strategies:

```python
def on_error(ws, error):
    print(f"{RED}❌ WebSocket Error:{RESET} {error}")

def on_close(ws, close_status_code, close_msg):
    print(f"{RED}Connection closed:{RESET} {close_status_code} - {close_msg}")
```

- WebSocket connection errors are captured and displayed
- Message parsing exceptions are trapped and reported
- Connection closure events are logged with status codes

## Performance Considerations

<table>
<tr>
<th>Aspect</th>
<th>Implementation</th>
</tr>
<tr>
<td><b>Memory Usage</b></td>
<td>Minimal memory footprint with efficient state tracking</td>
</tr>
<tr>
<td><b>CPU Utilization</b></td>
<td>Event-driven approach reduces CPU overhead</td>
</tr>
<tr>
<td><b>Network Efficiency</b></td>
<td>WebSocket connection maintenance with minimal reconnect logic</td>
</tr>
<tr>
<td><b>Update Optimization</b></td>
<td>Threshold-based updates reduce unnecessary terminal output</td>
</tr>
</table>

## Implementation Details

The core implementation utilizes Python's websocket-client library to establish and maintain a connection to the Pyth Network WebSocket API. The application follows a reactive pattern where price updates are processed and displayed based on configurable thresholds:

```python
def on_message(ws, message):
    global last_price
    try:
        data = json.loads(message)
        if data.get("type") == "price_update" and "price_feed" in data:
            price_feed = data["price_feed"]
            price_data = price_feed["price"]
            
            # Extract price, exponent, timestamp, and confidence
            price = int(price_data["price"])
            expo = int(price_data["expo"])
            publish_time = price_data["publish_time"]
            conf = int(price_data["conf"])
            
            # Convert to real values
            real_price = price * (10 ** expo)
            real_conf = conf * (10 ** expo)
            
            # Visual trend indicator calculation
            if last_price is not None:
                price_change = real_price - last_price
                # Direction and magnitude visualization logic
                
            # Display update when threshold is met
            if last_price is None or abs(real_price - last_price) >= 0.001:
                # Format and display the price information
                last_price = real_price
    except Exception as e:
        print(f"{RED}❌ Error:{RESET} {e}")
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Credits & Acknowledgments

<table>
<tr>
<th width="200">Project</th>
<th>Contribution</th>
<th width="150">Link</th>
</tr>
<tr>
<td align="center">
<img src="https://avatars.githubusercontent.com/u/68587457?s=200&v=4" width="40" height="40"/><br>
<b>Pyth Network</b>
</td>
<td>Provider of decentralized financial market data with WebSocket API</td>
<td><a href="https://pyth.network/">pyth.network</a></td>
</tr>
<tr>
<td align="center">
<img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/socketio/socketio-original.svg" width="40" height="40"/><br>
<b>websocket-client</b>
</td>
<td>Python WebSocket client library enabling real-time data connection</td>
<td><a href="https://pypi.org/project/websocket-client/">PyPI</a></td>
</tr>
<tr>
<td align="center">
<img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" width="40" height="40"/><br>
<b>Python Software Foundation</b>
</td>
<td>Core language and standard libraries for application development</td>
<td><a href="https://www.python.org/psf/">PSF</a></td>
</tr>
<tr>
<td align="center">
<img src="https://cryptologos.cc/logos/solana-sol-logo.svg?v=025" width="40" height="40"/><br>
<b>Solana</b>
</td>
<td>Blockchain platform with price feed tracking implementation</td>
<td><a href="https://solana.com/">solana.com</a></td>
</tr>
</table>

## Contact Information

<table>
<tr>
<td width="120"><b>Developer</b></td>
<td>Amin Nizam</td>
</tr>
<tr>
<td><b>GitHub</b></td>
<td><a href="https://github.com/aminnizamdev">@aminnizamdev</a></td>
</tr>
<tr>
<td><b>Repository</b></td>
<td><a href="https://github.com/aminnizamdev/sol-price-tracker">sol-price-tracker</a></td>
</tr>
</table>

---

## About this Project

SOL Price Tracker demonstrates the implementation of a high-performance financial data monitoring tool using WebSocket technology and the Pyth Network oracle. The application is designed with a focus on reliability, performance, and developer experience.

<div align="center">
<hr>
<br>
<img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" width="40" height="40"/>
&nbsp;&nbsp;
<img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/socketio/socketio-original.svg" width="40" height="40"/>
&nbsp;&nbsp;
<img src="https://cryptologos.cc/logos/solana-sol-logo.svg?v=025" width="40" height="40"/>
&nbsp;&nbsp;
<img src="https://avatars.githubusercontent.com/u/68587457?s=200&v=4" width="40" height="40"/>
<br><br>
<p>Built with passion by <a href="https://github.com/aminnizamdev">@aminnizamdev</a> — powered by the Pyth Network</p>
<p>SOL Price Tracker | WebSocket-Based Price Oracle | MIT Licensed</p>
</div>