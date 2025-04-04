# SOL Price Tracker

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.6+](https://img.shields.io/badge/python-3.6+-blue.svg)](https://www.python.org/downloads/)
[![Pyth Network](https://img.shields.io/badge/Pyth-Network-4A56FF)](https://pyth.network/)

## Overview

SOL Price Tracker is a high-performance, terminal-based application designed for real-time monitoring of Solana (SOL) price data via the Pyth Network Oracle. This tool provides developers and traders with accurate, low-latency price feeds with visual indicators optimized for terminal environments.

## Technical Architecture

The application implements a WebSocket client that connects to Pyth Network's price oracle infrastructure. It leverages the following technical components:

- **Data Source**: Pyth Network Hermes WebSocket API endpoint
- **Data Processing**: Real-time JSON parsing and numerical transformations
- **Display Logic**: Terminal-optimized visualization with ANSI color coding
- **Updates Management**: Conditional refresh based on configurable price delta thresholds

## Core Technologies

| Technology | Purpose | Documentation |
|------------|---------|---------------|
| Python 3.6+ | Core runtime environment | [python.org](https://www.python.org/) |
| websocket-client | WebSocket connectivity | [GitHub](https://github.com/websocket-client/websocket-client) |
| Pyth Network API | Price oracle data source | [docs.pyth.network](https://docs.pyth.network/) |
| ANSI Terminal | Visual output formatting | [ANSI Codes Reference](https://en.wikipedia.org/wiki/ANSI_escape_code) |

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

1. **Subscription Initialization**: On connection, the client subscribes to the SOL price feed
2. **Message Processing**: Incoming WebSocket messages are parsed from JSON format
3. **Price Extraction**: Price, exponent, confidence and timestamp values are extracted
4. **Numerical Transformation**: Raw integer values are converted using the provided exponent
5. **Delta Calculation**: Price changes are computed against previous values
6. **Threshold Filtering**: Updates are displayed only when meeting configurable thresholds (currently 0.001)
7. **Visual Formatting**: Output is formatted with directional indicators and magnitude representations

### Sample Output

```
Subscribed to SOL/USD feed
SOL/USD | $  123.4567 ± 0.0123 | 13:45:22 UTC | START | Change: N/A
SOL/USD | $  123.4789 ± 0.0125 | 13:45:24 UTC | ▲| | Change: +0.0222
SOL/USD | $  123.4321 ± 0.0124 | 13:45:30 UTC | ▼||| | Change: -0.0468
```

## Installation & Configuration

### System Requirements

- Python 3.6 or higher
- Network connectivity to Pyth Network endpoints
- Terminal with ANSI color support

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

- WebSocket connection errors are captured and displayed
- Message parsing exceptions are trapped and reported
- Connection closure events are logged with status codes

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Credits & Acknowledgments

- [Pyth Network](https://pyth.network/) - Provider of decentralized financial market data
- [websocket-client](https://pypi.org/project/websocket-client/) - Python WebSocket client library
- [Python Software Foundation](https://www.python.org/psf/) - Core language and standard libraries

## Contact Information

- Developer: Amin Nizam
- GitHub: [@aminnizamdev](https://github.com/aminnizamdev)
- Repository: [https://github.com/aminnizamdev/sol-price-tracker](https://github.com/aminnizamdev/sol-price-tracker)

---

<p align="center">
  <img src="https://www.python.org/static/community_logos/python-logo.png" height="30">
  &nbsp;&nbsp;
  <img src="https://pyth.network/assets/logo.svg" height="30">
</p>