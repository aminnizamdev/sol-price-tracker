# SOL Price Tracker

<div align="center">
  <img src="https://pyth.network/assets/logo.svg" alt="Pyth Network" width="300"/>
  <br><br>
  
  [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](https://opensource.org/licenses/MIT)
  [![Python 3.6+](https://img.shields.io/badge/python-3.6+-blue.svg?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/downloads/)
  [![Pyth Network](https://img.shields.io/badge/Pyth-Network-4A56FF?style=for-the-badge)](https://pyth.network/)
  [![WebSocket](https://img.shields.io/badge/WebSocket-Protocol-2ea44f?style=for-the-badge&logo=socketdotio&logoColor=white)](https://websocket.org/)
</div>

<hr>

<div align="center">
  <h3>High-performance terminal-based price oracle for real-time Solana price monitoring</h3>
</div>

## 📋 Overview

**SOL Price Tracker** is a high-performance, terminal-based application designed for real-time monitoring of Solana (SOL) price data via the Pyth Network Oracle. This tool provides developers and traders with accurate, low-latency price feeds with visual indicators optimized for terminal environments.

<div align="center">
  <img src="https://solana.com/src/images/logo.svg" alt="Solana Logo" width="150"/>
</div>

## 🏗️ Technical Architecture

The application implements a WebSocket client that connects to Pyth Network's price oracle infrastructure. It leverages the following technical components:

<table>
  <tr>
    <td><img src="https://cdn-icons-png.flaticon.com/512/8002/8002111.png" width="40"></td>
    <td><b>Data Source</b></td>
    <td>Pyth Network Hermes WebSocket API endpoint</td>
  </tr>
  <tr>
    <td><img src="https://cdn-icons-png.flaticon.com/512/1163/1163412.png" width="40"></td>
    <td><b>Data Processing</b></td>
    <td>Real-time JSON parsing and numerical transformations</td>
  </tr>
  <tr>
    <td><img src="https://cdn-icons-png.flaticon.com/512/1005/1005142.png" width="40"></td>
    <td><b>Display Logic</b></td>
    <td>Terminal-optimized visualization with ANSI color coding</td>
  </tr>
  <tr>
    <td><img src="https://cdn-icons-png.flaticon.com/512/2620/2620865.png" width="40"></td>
    <td><b>Updates Management</b></td>
    <td>Conditional refresh based on configurable price delta thresholds</td>
  </tr>
</table>

## 💻 Core Technologies

<div align="center">
  <table>
    <tr>
      <td align="center" width="200">
        <img src="https://www.python.org/static/community_logos/python-logo.png" width="150"><br>
        <b>Python 3.6+</b><br>
        Core runtime environment<br>
        <a href="https://www.python.org/">python.org</a>
      </td>
      <td align="center" width="200">
        <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/8/8d/WebSocket_Logo.svg/1200px-WebSocket_Logo.svg.png" width="120"><br>
        <b>websocket-client</b><br>
        WebSocket connectivity<br>
        <a href="https://github.com/websocket-client/websocket-client">GitHub</a>
      </td>
      <td align="center" width="200">
        <img src="https://pyth.network/assets/logo.svg" width="120"><br>
        <b>Pyth Network API</b><br>
        Price oracle data source<br>
        <a href="https://docs.pyth.network/">docs.pyth.network</a>
      </td>
      <td align="center" width="200">
        <img src="https://cdn-icons-png.flaticon.com/512/906/906324.png" width="70"><br>
        <b>ANSI Terminal</b><br>
        Visual output formatting<br>
        <a href="https://en.wikipedia.org/wiki/ANSI_escape_code">ANSI Reference</a>
      </td>
    </tr>
  </table>
</div>

## 🔧 Technical Specifications

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

<div align="center">
  <img src="https://cdn-icons-png.flaticon.com/512/6119/6119338.png" width="80">
</div>

1. **Subscription Initialization**: On connection, the client subscribes to the SOL price feed
2. **Message Processing**: Incoming WebSocket messages are parsed from JSON format
3. **Price Extraction**: Price, exponent, confidence and timestamp values are extracted
4. **Numerical Transformation**: Raw integer values are converted using the provided exponent
5. **Delta Calculation**: Price changes are computed against previous values
6. **Threshold Filtering**: Updates are displayed only when meeting configurable thresholds (currently 0.001)
7. **Visual Formatting**: Output is formatted with directional indicators and magnitude representations

### Sample Output

<div align="center">
  <img src="https://cdn-icons-png.flaticon.com/512/8695/8695801.png" width="80">
</div>

```
Subscribed to SOL/USD feed
SOL/USD | $  123.4567 ± 0.0123 | 13:45:22 UTC | START | Change: N/A
SOL/USD | $  123.4789 ± 0.0125 | 13:45:24 UTC | ▲| | Change: +0.0222
SOL/USD | $  123.4321 ± 0.0124 | 13:45:30 UTC | ▼||| | Change: -0.0468
```

## 📥 Installation & Configuration

<div align="center">
  <img src="https://cdn-icons-png.flaticon.com/512/8422/8422322.png" width="80">
</div>

### System Requirements

<table>
  <tr>
    <td><img src="https://cdn-icons-png.flaticon.com/512/5968/5968350.png" width="30"></td>
    <td>Python 3.6 or higher</td>
  </tr>
  <tr>
    <td><img src="https://cdn-icons-png.flaticon.com/512/2885/2885404.png" width="30"></td>
    <td>Network connectivity to Pyth Network endpoints</td>
  </tr>
  <tr>
    <td><img src="https://cdn-icons-png.flaticon.com/512/5756/5756494.png" width="30"></td>
    <td>Terminal with ANSI color support</td>
  </tr>
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

## ⚙️ Technical Customization Options

<div align="center">
  <img src="https://cdn-icons-png.flaticon.com/512/1622/1622816.png" width="80">
</div>

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

## ⚠️ Error Handling

<div align="center">
  <img src="https://cdn-icons-png.flaticon.com/512/4492/4492643.png" width="80">
</div>

The application implements comprehensive error handling strategies:

- WebSocket connection errors are captured and displayed
- Message parsing exceptions are trapped and reported
- Connection closure events are logged with status codes

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👏 Credits & Acknowledgments

<div align="center">
  <table>
    <tr>
      <td align="center" width="200">
        <img src="https://pyth.network/assets/logo.svg" width="120"><br>
        <b>Pyth Network</b><br>
        Provider of decentralized financial market data<br>
        <a href="https://pyth.network/">pyth.network</a>
      </td>
      <td align="center" width="200">
        <img src="https://avatars.githubusercontent.com/u/663326?s=280&v=4" width="80"><br>
        <b>websocket-client</b><br>
        Python WebSocket client library<br>
        <a href="https://pypi.org/project/websocket-client/">PyPI</a>
      </td>
      <td align="center" width="200">
        <img src="https://www.python.org/static/community_logos/python-logo.png" width="120"><br>
        <b>Python Software Foundation</b><br>
        Core language and standard libraries<br>
        <a href="https://www.python.org/psf/">PSF</a>
      </td>
    </tr>
  </table>
</div>

## 📞 Contact Information

<div align="center">
  <table>
    <tr>
      <td align="center" width="200">
        <img src="https://cdn-icons-png.flaticon.com/512/25/25657.png" width="60"><br>
        <b>Developer</b><br>
        Amin Nizam
      </td>
      <td align="center" width="200">
        <img src="https://cdn-icons-png.flaticon.com/512/25/25231.png" width="60"><br>
        <b>GitHub</b><br>
        <a href="https://github.com/aminnizamdev">@aminnizamdev</a>
      </td>
      <td align="center" width="200">
        <img src="https://cdn-icons-png.flaticon.com/512/1183/1183671.png" width="60"><br>
        <b>Repository</b><br>
        <a href="https://github.com/aminnizamdev/sol-price-tracker">sol-price-tracker</a>
      </td>
    </tr>
  </table>
</div>

---

<div align="center">
  <h2>🔮 SOL Price Tracker</h2>
  <p>A high-performance terminal-based Solana price oracle</p>
  <img src="https://solana.com/src/images/logo.svg" height="60">
  &nbsp;&nbsp;&nbsp;&nbsp;
  <img src="https://www.python.org/static/community_logos/python-logo.png" height="60">
  &nbsp;&nbsp;&nbsp;&nbsp;
  <img src="https://pyth.network/assets/logo.svg" height="60">
</div>